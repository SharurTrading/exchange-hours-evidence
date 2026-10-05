import os,sys,time,subprocess
rows=[l.rstrip('\n').split('\t') for l in open('dl_list.txt')]
os.makedirs('docs',exist_ok=True)
log=open('dl.log','a')
for f,ts,orig in rows:
    p=os.path.join('docs',f)
    if os.path.exists(p) and os.path.getsize(p)>1000: continue
    url=f"https://web.archive.org/web/{ts}id_/{orig}"
    for attempt in range(6):
        r=subprocess.run(['curl','-sL','--max-time','180','-w','%{http_code}','-o',p,url],capture_output=True,text=True)
        code=r.stdout.strip()
        sz=os.path.getsize(p) if os.path.exists(p) else 0
        if code=='200' and sz>1000:
            print(f,code,sz,file=log,flush=True); break
        print('retry',f,code,sz,file=log,flush=True)
        time.sleep(10+attempt*15)
    else:
        print('FAIL',f,file=log,flush=True)
    time.sleep(2)
print('DONE',file=log,flush=True)
