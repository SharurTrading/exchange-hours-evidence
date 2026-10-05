#!/usr/bin/env python3
"""U8 gate re-check, written independently of drift-computation.py.

No network. Pure IANA tz database via CPython zoneinfo. Answers four questions:
  Q1 how many distinct (reference_offset - chicago_offset) states exist per zone pair, 2010-2030
  Q2 the Chicago clock value of each shape's foreign-anchored boundary in each state
  Q3 the 2026 weekday split between the states
  Q4 which boundary sits nearest Chicago midnight (the wrap-flip margin)
"""
import datetime as dt
from zoneinfo import ZoneInfo

CHI = ZoneInfo("America/Chicago")
ZONES = {
    "Europe/London": ZoneInfo("Europe/London"),
    "Asia/Singapore": ZoneInfo("Asia/Singapore"),
    "Asia/Shanghai": ZoneInfo("Asia/Shanghai"),
    "Asia/Hong_Kong": ZoneInfo("Asia/Hong_Kong"),
    "Asia/Tokyo": ZoneInfo("Asia/Tokyo"),
    "America/New_York": ZoneInfo("America/New_York"),
}

def delta_h(day, zone):
    """reference_offset - chicago_offset in hours, measured at Chicago noon (as the crate does)."""
    noon = dt.datetime.combine(day, dt.time(12, 0), tzinfo=CHI)
    return (noon.astimezone(zone).utcoffset() - noon.utcoffset()).total_seconds() / 3600.0

def chicago_clock(day, zone, hh, mm):
    """The Chicago wall clock of <hh:mm local in `zone`> for the marker on `day`."""
    d = delta_h(day, zone)
    total = hh * 60 + mm - int(d * 60)
    return total % 1440, total // 1440   # (minutes after Chicago midnight, day offset)

def fmt(mins):
    return "%02d:%02d" % (mins // 60, mins % 60)

print("== Q1: distinct offset states per zone pair, 2010-01-01..2030-12-31 ==")
days = [dt.date(2010, 1, 1) + dt.timedelta(days=i) for i in range((dt.date(2030,12,31)-dt.date(2010,1,1)).days + 1)]
for name, z in ZONES.items():
    vals = sorted({delta_h(d, z) for d in days})
    print("  %-16s states=%s" % (name, vals))

print()
print("== Q2/Q3/Q4: per-shape boundary, both states, 2026 weekday split ==")
SHAPES = [
    ("energy TAM London  CLL BZL HOL RBL", "Europe/London", 16, 30),
    ("energy TAM Singapore CLS BZS",       "Asia/Singapore", 16, 30),
    ("energy TAM Shanghai CLC",            "Asia/Shanghai", 15,  0),
    ("gold TAM  GCD",                      "Europe/London", 15,  2),
    ("copper TAM HGF",                     "Europe/London", 12, 35),
    ("Europe index BTIC DVT E3T",          "Europe/London", 16, 30),
    ("FTSE China 50 BTIC FTC",             "Asia/Hong_Kong", 16, 0),
    ("Nikkei BTIC NIT NKT",                "Asia/Tokyo",    15, 30),
    ("TOPIX BTIC TPB TPT",                 "Asia/Tokyo",    15, 30),
    ("crypto BTIC London stop start",      "Europe/London", 16,  0),
    ("crypto BTIC APAC stop start",        "Asia/Hong_Kong", 16, 0),
    ("FX BTIC 6EB gap start",              "Europe/London", 15, 40),
    ("FX BTIC 6EB gap end",                "Europe/London", 16, 30),
    ("TMAC / equity BTIC (control)",       "America/New_York", 16, 0),
]
wd2026 = [dt.date(2026,1,1) + dt.timedelta(days=i) for i in range(365)]
wd2026 = [d for d in wd2026 if d.weekday() < 5]
nearest = []
for label, zname, hh, mm in SHAPES:
    z = ZONES[zname]
    buckets = {}
    for d in wd2026:
        mins, dayoff = chicago_clock(d, z, hh, mm)
        buckets.setdefault((mins, dayoff), 0)
        buckets[(mins, dayoff)] += 1
    parts = ", ".join("%s%s x%d" % (fmt(k[0]), (" d%+d" % k[1]) if k[1] else "", v)
                      for k, v in sorted(buckets.items()))
    print("  %-36s %-16s %02d:%02d -> %s" % (label, zname, hh, mm, parts))
    for (mins, dayoff) in buckets:
        nearest.append((min(mins, 1440 - mins), fmt(mins), label))
print()
print("  total 2026 weekdays:", len(wd2026))

print()
print("== Q4: boundaries ranked by distance from Chicago midnight (wrap-flip margin) ==")
for margin, clock, label in sorted(set(nearest))[:6]:
    print("  %4d min from midnight   %s   %s" % (margin, clock, label))

print()
print("== misalignment windows US vs UK, 2010-2030 (calendar days per year) ==")
for year in range(2010, 2031):
    ds = [dt.date(year,1,1) + dt.timedelta(days=i) for i in range(366 if year%4==0 and (year%100!=0 or year%400==0) else 365)]
    mis = [d for d in ds if delta_h(d, ZONES["Europe/London"]) != 6.0]
    runs = []
    start = None
    prev = None
    for d in mis:
        if start is None:
            start = d
        elif (d - prev).days != 1:
            runs.append((start, prev)); start = d
        prev = d
    if start: runs.append((start, prev))
    print("  %d: %2d days  %s" % (year, len(mis), "  ".join("%s..%s (%dd)" % (a, b, (b-a).days+1) for a, b in runs)))

print()
print("== do any of these DST transitions fall inside a running 17:00 CT -> next-morning session? ==")
for year in (2026, 2027):
    for z, name in ((CHI, "US"), (ZONES["Europe/London"], "UK")):
        # find transitions by scanning hourly across the year
        prev = None
        for i in range(0, 366*24):
            t = dt.datetime(year,1,1,tzinfo=dt.timezone.utc) + dt.timedelta(hours=i)
            off = t.astimezone(z).utcoffset()
            if prev is not None and off != prev[1]:
                inst = prev[0]
                chi_local = inst.astimezone(CHI)
                print("  %s %s transition ~%s UTC = %s Chicago (%s)" % (
                    year, name, inst.strftime("%Y-%m-%d %H:%M"),
                    chi_local.strftime("%Y-%m-%d %H:%M %Z"), chi_local.strftime("%a")))
            prev = (t, off)
