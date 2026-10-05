import json, pathlib, subprocess, time, re
best = json.load(open("hours_pages/index.json"))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
out = pathlib.Path("hours_pages"); out.mkdir(exist_ok=True)
for y, (ts, orig) in sorted(best.items()):
    dest = out/f"hours_{y}_{ts}.html"
    if dest.exists() and dest.stat().st_size > 5000: print("cached", y); continue
    for _ in range(3):
        r = subprocess.run(["curl","-sSL","--max-time","120","-A",UA,"-o",str(dest),"-w","%{http_code}",
                            f"https://web.archive.org/web/{ts}id_/{orig}"],capture_output=True,text=True)
        if r.stdout.strip()=="200" and dest.exists() and dest.stat().st_size>5000:
            print("ok", y, dest.stat().st_size); break
        time.sleep(3)
    else: print("FAIL", y)
