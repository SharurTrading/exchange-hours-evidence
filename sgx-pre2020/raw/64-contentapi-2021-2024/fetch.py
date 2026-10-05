import json, time, subprocess, os, sys, gzip, io, zlib
rows=json.load(open('targets.json'))
log=[]
for r in rows:
    ts=r['ts']
    out=f"raw_{ts}.bin"
    if os.path.exists(out) and os.path.getsize(out)>0:
        continue
    url=f"https://web.archive.org/web/{ts}id_/{r['url']}"
    ok=False
    for attempt in range(6):
        p=subprocess.run(['curl','-sS','-m','120','-D',f'hdr_{ts}.txt','-o',out,
                          '-A','Mozilla/5.0 (research; exchange-hours-rs evidence)',url],
                         capture_output=True, text=True)
        if p.returncode==0 and os.path.exists(out) and os.path.getsize(out)>0:
            ok=True; break
        time.sleep(5*(attempt+1)*2)
    print(ts, 'OK' if ok else 'FAIL', os.path.getsize(out) if os.path.exists(out) else 0, flush=True)
    time.sleep(3)
