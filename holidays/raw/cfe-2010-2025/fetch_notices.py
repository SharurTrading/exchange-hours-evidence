import json, pathlib, re, subprocess, time, collections
rows = json.load(open("cdx_schedule_update.json"))[1:]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
HOL = re.compile(r'(holiday|christmas|thanksgiving|memorial|labor.day|independence|juneteenth|president|martin.luther|new.year|good.friday|mlk)', re.I)
out = pathlib.Path("notices"); out.mkdir(exist_ok=True)
by_year = collections.defaultdict(list)
for ts, orig, status, mime in rows:
    m = re.search(r'/schedule_update/(\d{4})/', orig)
    if m and HOL.search(orig):
        by_year[m.group(1)].append((ts, orig))
rec = []
for year in sorted(by_year):
    for ts, orig in sorted(by_year[year]):
        name = f"{year}_{re.sub(r'[^A-Za-z0-9._-]', '_', orig.split('/')[-1])}"
        dest = out / name
        if dest.exists() and dest.stat().st_size > 500:
            rec.append((year, name, ts, "cached")); continue
        url = f"https://web.archive.org/web/{ts}id_/{orig}"
        ok = False
        for _ in range(3):
            r = subprocess.run(["curl","-sSL","--max-time","90","-A",UA,"-o",str(dest),"-w","%{http_code}",url],
                               capture_output=True, text=True)
            if r.stdout.strip() == "200" and dest.exists() and dest.stat().st_size > 500:
                ok = True; break
            time.sleep(2)
        rec.append((year, name, ts, "ok" if ok else "fail"))
json.dump(rec, open("notices_index.json","w"), indent=1)
print("year  fetched/total")
for year in sorted(by_year):
    got = sum(1 for y,_,_,s in rec if y==year and s in ("ok","cached"))
    print(f"  {year}  {got}/{len(by_year[year])}")
