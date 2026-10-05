"""Derive each CFE holiday notice's effect on the VX (volatility-index) clock.

Reads exact word bounding boxes (`pdftotext -bbox`). The notices print day
headers over a set of ETH/RTH sub-columns; a sub-column belongs to the day
header nearest its x-centre. The VX row's printed times are matched to
sub-columns the same way, so a day with no printed time is a day with no
session in that phase.
"""
import json, pathlib, re, subprocess, collections

WEEK = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
MONTHS = "january|february|march|april|may|june|july|august|september|october|november|december"
TIME = re.compile(r'^\d{1,2}:\d{2}$', re.I)
MERO = re.compile(r'^(AM|PM)$', re.I)

def words(pdf):
    xml = subprocess.run(["pdftotext","-bbox",str(pdf),"-"],capture_output=True,text=True).stdout
    out = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', xml):
        x0,y0,x1,y1,txt = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5)
        out.append({"x": (x0+x1)/2, "y": (y0+y1)/2, "t": txt.strip()})
    return out

def lines(ws, tol=3.0):
    ls = collections.defaultdict(list)
    for w in ws:
        key = next((k for k in ls if abs(k - w["y"]) <= tol), None)
        ls[key if key is not None else w["y"]].append(w)
    return [sorted(v, key=lambda w: w["x"]) for _, v in sorted(ls.items())]

def parse(pdf):
    ws = words(pdf)
    if not ws: return None
    text = " ".join(w["t"] for w in ws)
    obs = re.search(r'observed on\s+(\w+day),?\s+([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})', text, re.I)
    if not obs: return None
    ls = lines(ws)
    dayline = next((l for l in ls if sum(1 for d in WEEK if any(w["t"].upper().rstrip(',') == d for w in l)) >= 2), None)
    def phase_words(line):
        return [i for i, w in enumerate(line) if w["t"] in ("ETH", "RTH")]
    subline = max(ls, key=lambda l: len(phase_words(l)), default=None)
    if subline is None or len(phase_words(subline)) < 3: return None
    if dayline is None or subline is None: return None
    days = [(w["t"].upper().rstrip(','), w["x"]) for w in dayline if w["t"].upper().rstrip(',') in WEEK]
    if len(days) < 2: return None
    subs = []
    for i in phase_words(subline):
        nxt = next((w for w in subline[i+1:] if w["t"] in ("Start", "Close")), None)
        if nxt is None: continue
        subs.append((f"{subline[i]['t']} {nxt['t']}", (subline[i]["x"] + nxt["x"]) / 2))
    subs.sort(key=lambda s: s[1])
    if len(subs) < 3: return None
    def owner(x):
        return min(days, key=lambda d: abs(d[1]-x))[0]
    # the VX product row: the line whose first word starts "Volatility"
    vx = next((l for l in ls if l and l[0]["t"].startswith("Volatility") and any(TIME.match(w["t"]) for w in l)), None)
    if vx is None: return None
    grid = collections.defaultdict(dict)
    k = 0
    while k < len(vx):
        w = vx[k]
        if TIME.match(w["t"]):
            val = w["t"] + ((" " + vx[k+1]["t"]) if k+1 < len(vx) and MERO.match(vx[k+1]["t"]) else "")
            name = min(subs, key=lambda s: abs(s[1]-w["x"]))[0]
            grid[owner(w["x"])].setdefault(name, val)
            k += 2 if k+1 < len(vx) and MERO.match(vx[k+1]["t"]) else 1
        else:
            k += 1
    hol = f"{obs.group(1)} {obs.group(2)} {obs.group(3)}, {obs.group(4)}"
    return {"holiday_text": hol, "observed_weekday": obs.group(1).capitalize(),
            "days": [d for d, _ in days], "grid": {k: dict(v) for k, v in grid.items()},
            "subs": [s for s, _ in subs]}

recs = json.load(open("live_index.json"))
out = []
for r in recs:
    d = parse(pathlib.Path("live")/r["file"])
    if d:
        d.update({"file": r["file"], "listing_year": r["listing_year"], "url": r["url"], "sha256": r["sha256"]})
    else:
        d = {"file": r["file"], "listing_year": r["listing_year"], "unparsed": True}
    out.append(d)
json.dump(out, open("parsed.json","w"), indent=1)
print("parsed", sum(1 for d in out if not d.get("unparsed")), "of", len(out))
for d in [x for x in out if not x.get("unparsed")][:2]:
    print(json.dumps({k: d[k] for k in ("file","holiday_text","days","subs","grid")}, indent=1)[:900])
