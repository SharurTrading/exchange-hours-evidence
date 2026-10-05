import json, re, pathlib, hashlib, subprocess, time, sys

OUT = pathlib.Path("pdf"); OUT.mkdir(exist_ok=True)
idx = {r["id"]: r for r in json.load(open("cde_notices_index.json"))}
fairx = json.load(open("cde_fairx_links_20221215.json"))
cdx = json.load(open("cdx_ctfassets.json"))[1:]
# best archive capture per original URL (status 200, latest)
arch = {}
for ts, orig, status, mime, digest, length in cdx:
    if status == "200" and "Market_Notice" in orig:
        arch.setdefault(orig, (ts, orig))

def run(url, dest, extra=None):
    cmd = ["curl", "-sSL", "--max-time", "180", "-o", str(dest), "-w", "%{http_code}", url]
    if extra: cmd[1:1] = extra
    for attempt in range(4):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True)
            code = r.stdout.strip()
            if code == "200" and dest.exists() and dest.stat().st_size > 800:
                return code, "live" if not extra else "archive"
        except Exception:
            pass
        time.sleep(3)
    return code, "fail"

results = {}
for ident in sorted(idx):
    r = idx[ident]
    if not ("Holiday" in r["category"] or "Day of Mourning" in r["subject"] or "Early Close" in r["subject"]):
        continue
    # candidate URLs: live listing href, then fairx/ctfassets from the 2022 capture
    cands = []
    for u in r["uris"]:
        cands.append(("live", u))
    if ident in fairx:
        u = fairx[ident][1]
        if u.startswith("//"): u = "https:" + u
        cands.append(("live-listing-2022", u))
    dest = OUT / f"{ident}.pdf"
    if dest.exists() and dest.stat().st_size > 800:
        results[ident] = ("cached", str(dest)); continue
    got = None
    for label, u in cands:
        code, how = run(u, dest)
        if code == "200":
            got = (label, u, "live"); break
    if not got:
        # archive replay of the same originals
        for label, u in cands:
            base = u
            for orig, (ts, o) in arch.items():
                if o.endswith(base.split("/")[-1]) or base.split("/")[-1] in o:
                    code, how = run(f"https://web.archive.org/web/{ts}id_/{o}", dest)
                    if code == "200":
                        got = (label, f"https://web.archive.org/web/{ts}id_/{o}", "archive"); break
            if got: break
    if got:
        sha = hashlib.sha256(dest.read_bytes()).hexdigest()
        results[ident] = ("ok", got[1], got[2], sha, dest.stat().st_size)
        print(f"  {ident:8} {got[2]:8} {dest.stat().st_size:>8}b  {got[1][:88]}")
    else:
        results[ident] = ("MISSING", [u for _, u in cands])
        print(f"  {ident:8} MISSING")
pathlib.Path("fetch_results.json").write_text(json.dumps(results, ensure_ascii=False, indent=1))
print("\ndownloaded:", sum(1 for v in results.values() if v[0] in ("ok","cached")), "of", len(results))
