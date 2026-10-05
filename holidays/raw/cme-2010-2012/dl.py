import json,urllib.request,hashlib,os,time,sys
BASE="https://web.archive.org/web/%sid_/%s"
targets=json.load(open("targets.json"))
os.makedirs("docs",exist_ok=True)
out=[]
for name,ts,url in targets:
    path=os.path.join("docs",name)
    if os.path.exists(path) and os.path.getsize(path)>2000:
        b=open(path,'rb').read()
    else:
        b=None
        for attempt in range(5):
            try:
                req=urllib.request.Request(BASE%(ts,url),headers={'User-Agent':'Mozilla/5.0'})
                b=urllib.request.urlopen(req,timeout=120).read()
                break
            except Exception as e:
                print("retry",name,attempt,e,file=sys.stderr); time.sleep(8)
        if b is None:
            out.append((name,url,ts,"FAILED","")); continue
        open(path,'wb').write(b)
        time.sleep(2)
    out.append((name,url,ts,str(len(b)),hashlib.sha256(b).hexdigest()))
    print("\t".join(out[-1]))
json.dump(out,open("downloaded.json","w"),indent=1)
