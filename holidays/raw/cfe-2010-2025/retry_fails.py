import json, pathlib, re, subprocess, time
rec = json.load(open("notices_index.json"))
rows = {(re.search(r'/schedule_update/(\d{4})/', r[1]).group(1), r[1]) for r in json.load(open("cdx_schedule_update.json"))[1] if re.search(r'/schedule_update/(\d{4})/', r[1])}
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
fails = [(y,n) for y,n,_,s in rec if s=="fail"]
fixed = 0
for year, name in fails:
    # map the saved name back to the original URL
    orig = next((o for (yy,o) in rows if yy==year and re.sub(r'[^A-Za-z0-9._-]','_',o.split('/')[-1]) == name[len(year)+1:]), None)
    if not orig:
        print(f"  {name[:60]}: no source url"); continue
    q = f"https://web.archive.org/cdx/search/cdx?url={orig}&output=json&fl=timestamp,statuscode&limit=50"
    try:
        raw = subprocess.run(["curl","-sS","--max-time","60",q],capture_output=True,text=True).stdout
        caps = json.loads(raw)[1:] if raw.strip().startswith("[") else []
    except Exception:
        caps = []
    good = [ts for ts, st in caps if st == "200"]
    dest = pathlib.Path("notices")/name
    ok = False
    for ts in reversed(good):
        for _ in range(2):
            r = subprocess.run(["curl","-sSL","--max-time","90","-A",UA,"-o",str(dest),"-w","%{http_code}",
                                f"https://web.archive.org/web/{ts}id_/{orig}"],capture_output=True,text=True)
            if r.stdout.strip()=="200" and dest.exists() and dest.stat().st_size>500:
                ok = True; break
            time.sleep(2)
        if ok: break
    if ok: fixed += 1; print(f"  {name[:62]:64} FIXED via {good[-1][:8]}")
    else:  print(f"  {name[:62]:64} still missing ({len(good)} status-200 captures)")
print(f"\nrecovered {fixed} of {len(fails)}")
