import json, pathlib, hashlib, subprocess, time

idx = {r["id"]: r for r in json.load(open("cde_notices_index.json"))}
fairx = json.load(open("cde_fairx_links_20221215.json"))
cdx = json.load(open("cdx_ctfassets.json"))[1:]
by_name = {}
for ts, orig, status, mime, digest, length in cdx:
    if status == "200" and "Market_Notice" in orig:
        by_name.setdefault(orig.split("/")[-1], []).append((ts, orig))

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def fetch(url, dest):
    for _ in range(3):
        r = subprocess.run(["curl","-sSL","--max-time","120","-o",str(dest),"-w","%{http_code}",url],
                           capture_output=True, text=True)
        if r.stdout.strip() == "200" and pathlib.Path(dest).exists() and pathlib.Path(dest).stat().st_size > 800:
            return True
        time.sleep(2)
    return False

out = {}
tmp = pathlib.Path("tmp"); tmp.mkdir(exist_ok=True)
for ident in sorted(idx):
    r = idx[ident]
    if not ("Holiday" in r["category"] or "Day of Mourning" in r["subject"] or "Early Close" in r["subject"]):
        continue
    pdf = pathlib.Path("pdf")/f"{ident}.pdf"
    if not pdf.exists():
        out[ident] = {"status": "missing"}; continue
    want = sha(pdf)
    cands = [(u, "listing") for u in r["uris"]]
    if ident in fairx:
        u = fairx[ident][1]
        cands.append((("https:"+u if u.startswith("//") else u), "listing-2022-capture"))
    rec = None
    for url, src in cands:
        if fetch(url, tmp/"probe"):
            if sha(tmp/"probe") == want:
                rec = {"status":"ok","url":url,"channel":"live","listed_by":src}; break
    if rec is None:
        names = [c[0].split("/")[-1] for c in cands]
        for name in names:
            for ts, orig in by_name.get(name, []):
                wb = f"https://web.archive.org/web/{ts}id_/{orig}"
                if fetch(wb, tmp/"probe") and sha(tmp/"probe") == want:
                    rec = {"status":"ok","url":wb,"channel":"archive","capture":ts,"original":orig}; break
            if rec: break
    if rec is None:
        rec = {"status":"unresolved","candidates":[u for u,_ in cands]}
    rec["sha256"] = want; rec["bytes"] = pdf.stat().st_size
    out[ident] = rec
    print(f"  {ident:8} {rec['status']:10} {rec.get('channel','-'):8} {rec.get('url','')[:80]}")
pathlib.Path("provenance.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
import collections
print("\n", dict(collections.Counter(v["status"] for v in out.values())),
      dict(collections.Counter(v.get("channel","-") for v in out.values() if v["status"]=="ok")))
