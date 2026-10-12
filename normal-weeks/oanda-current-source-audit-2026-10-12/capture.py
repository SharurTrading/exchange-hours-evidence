import subprocess,pathlib,json,hashlib,datetime,concurrent.futures
out=pathlib.Path('/tmp/oanda-current-source-audit-2026-10-12');urls={'uk-hours':'https://www.oanda.com/uk-en/trading/hours-of-operation/','uk-holidays':'https://www.oanda.com/uk-en/trading/holiday-trading-hours/','help-uk-hours':'https://help.oanda.com/uk/en/faqs/hours-of-operation.htm'}
def get(item):
 name,url=item;p=out/(name+'.html');h=out/(name+'.headers');r=subprocess.run(['curl','-L','--fail','--max-time','35','--silent','--show-error','-D',str(h),url,'-o',str(p)],capture_output=True,text=True);x={'name':name,'url':url,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':r.returncode,'error':r.stderr,'path':str(p)}
 if p.exists():x['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
 return x
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:a=list(ex.map(get,urls.items()))
(out/'retrieval.json').write_text(json.dumps(a,indent=2));print(json.dumps(a,indent=2))
