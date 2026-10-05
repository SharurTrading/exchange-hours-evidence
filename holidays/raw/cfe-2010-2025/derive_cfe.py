"""Derive the crate rows from the CFE production holiday notices."""
import json, pathlib, re, subprocess, collections
exec(open("parse_cfe.py").read().split("recs = json.load")[0])

MON = {m: i for i, m in enumerate(
    ["january","february","march","april","may","june","july","august","september",
     "october","november","december"], 1)}

def is_production(t):
    return "Cboe Futures Exchange" in t and "modified trading hours" in t.lower()

def derive(d):
    """(iso trade date, kind, close minutes) for the notice's holiday day."""
    txt = d["holiday_text"]
    wk, mo, dy, yr = txt.split()[0].upper(), txt.split()[1].lower(), txt.split()[2].rstrip(','), int(txt.split()[3])
    iso = f"{yr}-{MON[mo]:02d}-{int(dy):02d}"
    g = d["grid"].get(wk, {})
    def mins(s):
        m = re.match(r'(\d{1,2}):(\d{2})\s*(AM|PM)', s or "", re.I)
        if not m: return None
        h, mi, ap = int(m.group(1)), int(m.group(2)), m.group(3).upper()
        if ap == "PM" and h != 12: h += 12
        if ap == "AM" and h == 12: h = 0
        return h*60+mi
    if g.get("RTH Close"):   return iso, "early_close", mins(g["RTH Close"])
    if g.get("ETH Close"):   return iso, "early_close", mins(g["ETH Close"])
    if g:                    return iso, "closed", None
    return iso, "closed", None

recs = json.load(open("live_index.json"))
rows, skipped = [], []
for r in recs:
    p = pathlib.Path("live")/r["file"]
    ws = words(p)
    text = " ".join(w["t"] for w in ws)
    if not is_production(text):
        skipped.append(r["file"]); continue
    d = parse(p)
    if not d:
        skipped.append(r["file"] + "  [UNPARSED]"); continue
    iso, kind, m = derive(d)
    rows.append({"date": iso, "kind": kind, "close_min": m, "file": r["file"],
                 "url": r["url"], "sha256": r["sha256"], "holiday": d["holiday_text"],
                 "weekday": d["observed_weekday"]})
rows.sort(key=lambda r: r["date"])
json.dump({"rows": rows, "skipped": skipped}, open("derived_rows.json","w"), indent=1)
print(f"production notices: {len(rows)} derived, {len(skipped)} skipped (non-CFE or unparsed)\n")
by = collections.defaultdict(list)
for r in rows: by[r["date"][:4]].append(r)
FULL = ["New Year","MLK","Presidents","Good Friday","Memorial","Juneteenth","Independence","Labor","Thanksgiving","Christmas"]
for y in sorted(by):
    print(f"=== {y}: {len(by[y])} rows")
    for r in sorted(by[y], key=lambda r: r["date"]):
        print(f"    {r['date']}  {r['kind']:12} {str(r['close_min']):>5}  {r['file'].split('__')[1][:58]}")
print("\nskipped:")
for s in skipped[:8]: print("   ", s[:95])
print(f"   ... {len(skipped)} total")
