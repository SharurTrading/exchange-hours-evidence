import json, pathlib, subprocess, time, hashlib, re
idx = json.load(open("listing_index.json"))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
out = pathlib.Path("live"); out.mkdir(exist_ok=True)
recs = []
for year in sorted(idx):
    for url in idx[year]:
        if "schedule_update" not in url: continue
        if not re.search(r'(CFE|Cboe).*(Holiday|holiday|Christmas|Thanksgiving|Memorial|Labor|Independence|Juneteenth|Presidents|Martin|New.Year|Good.Friday|MLK)', url, re.I): continue
        name = f"{year}__{re.sub(r'[^A-Za-z0-9._-]','_',url.split('/')[-1])}"
        dest = out/name
        st = "cached"
        if not (dest.exists() and dest.stat().st_size > 500):
            st = "fail"
            for _ in range(3):
                r = subprocess.run(["curl","-sSL","--max-time","90","-A",UA,"-o",str(dest),"-w","%{http_code}",url],
                                   capture_output=True, text=True)
                if r.stdout.strip() == "200" and dest.exists() and dest.stat().st_size > 500:
                    st = "ok"; break
                time.sleep(2)
        if dest.exists() and dest.stat().st_size > 500:
            recs.append({"listing_year": year, "url": url, "file": name,
                         "sha256": hashlib.sha256(dest.read_bytes()).hexdigest(),
                         "bytes": dest.stat().st_size, "status": st})
json.dump(recs, open("live_index.json","w"), indent=1)
print("fetched:", sum(1 for r in recs if r['status'] in ('ok','cached')), "of", len(recs))
