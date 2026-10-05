import json, pathlib, subprocess, time, re, hashlib
rows = json.load(open("cdx_cfe_infocirc.json"))[1:]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
out = pathlib.Path("infocirc")
rec = []
for ts, orig, status in sorted(rows, key=lambda r: r[1]):
    name = re.sub(r'[^A-Za-z0-9._-]', '_', orig.split("/")[-1])
    dest = out / name
    if dest.exists() and dest.stat().st_size > 500:
        rec.append((name, ts, "cached")); continue
    url = f"https://web.archive.org/web/{ts}id_/{orig}"
    ok = False
    for _ in range(3):
        r = subprocess.run(["curl","-sSL","--max-time","90","-A",UA,"-o",str(dest),"-w","%{http_code}",url],
                           capture_output=True, text=True)
        if r.stdout.strip() == "200" and dest.exists() and dest.stat().st_size > 500:
            ok = True; break
        time.sleep(2)
    rec.append((name, ts, "ok" if ok else "fail"))
    print(f"  {name[:44]:46} {ts[:8]} {'ok' if ok else 'FAIL'}")
pathlib.Path("infocirc_index.json").write_text(json.dumps(rec, indent=1))
print("fetched:", sum(1 for _,_,s in rec if s in ("ok","cached")), "of", len(rec))
