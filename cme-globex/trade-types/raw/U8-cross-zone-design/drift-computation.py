# SPDX-License-Identifier: MIT-0
# Reproduces drift-computation-2026-09-06.txt. Pure tz-database arithmetic, no network.
# Run: python3 drift-computation.py
import datetime as dt, zoneinfo, collections
CHI = zoneinfo.ZoneInfo("America/Chicago")
shapes = [
 ("TAM London CLL/BZL/HOL/RBL close", "Europe/London", (16,30)),
 ("TAM Gold GCD close",               "Europe/London", (15, 2)),
 ("TAM Copper HGF close",             "Europe/London", (12,35)),
 ("BTIC Europe DVT/E3T close",        "Europe/London", (16,30)),
 ("BTIC crypto London stop start",    "Europe/London", (16, 0)),
 ("FX BTIC 6EB halt start",           "Europe/London", (15,40)),
 ("FX BTIC 6EB halt end",             "Europe/London", (16,30)),
 ("TAM Singapore CLS/BZS close",      "Asia/Singapore",(16,30)),
 ("TAM Shanghai CLC close",           "Asia/Shanghai", (15, 0)),
 ("BTIC FTSE China 50 FTC close",     "Asia/Hong_Kong",(16, 0)),
 ("BTIC crypto APAC stop start",      "Asia/Hong_Kong",(16, 0)),
 ("BTIC Nikkei/TOPIX close",          "Asia/Tokyo",    (15,30)),
]
for name, zname, hm in shapes:
    counts = collections.Counter()
    for n in range(365):
        d = dt.date(2026,1,1)+dt.timedelta(days=n)
        if d.weekday() > 4: continue
        local = dt.datetime(d.year,d.month,d.day,hm[0],hm[1],tzinfo=zoneinfo.ZoneInfo(zname))
        c = local.astimezone(CHI)
        counts[(c.strftime("%H:%M"), (c.date()-d).days)] += 1
    print(f"{name:38s} anchor {hm[0]:02d}:{hm[1]:02d} {zname}")
    for k,v in sorted(counts.items()):
        print(f"      Chicago {k[0]} (day offset {k[1]:+d})  on {v} weekdays of 2026")
    print()
print("=== US/UK DST misalignment windows ===")
def transitions(zname, year):
    z = zoneinfo.ZoneInfo(zname); out=[]; prev=None
    t=dt.datetime(year,1,1,tzinfo=dt.timezone.utc)
    while t.year==year:
        off = t.astimezone(z).utcoffset()
        if prev is not None and off!=prev: out.append((t, prev, off))
        prev=off; t+=dt.timedelta(hours=1)
    return out
for year in range(2010,2031):
    us = transitions("America/Chicago", year); uk = transitions("Europe/London", year)
    spring = (us[0][0], uk[0][0]); autumn = (uk[1][0], us[1][0])
    sd = (spring[1]-spring[0]).days; ad = (autumn[1]-autumn[0]).days
    print(f"{year}: spring misaligned {spring[0].date()} -> {spring[1].date()} ({sd}d); "
          f"autumn misaligned {autumn[0].date()} -> {autumn[1].date()} ({ad}d); total {sd+ad}d")
