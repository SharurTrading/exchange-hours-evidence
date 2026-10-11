import pathlib,subprocess,hashlib,datetime,json,concurrent.futures
r=pathlib.Path('/tmp/oanda-four-book-report/evidence')
sources=[('carter-2025.html','https://web.archive.org/web/20250326184653id_/https://www.oanda.com/uk-en/trading/holiday-trading-hours/'),('carter-2026.html','https://web.archive.org/web/20260217213704id_/https://www.oanda.com/uk-en/trading/holiday-trading-hours/'),('hours-2024.html','https://web.archive.org/web/20240221005503id_/https://www.oanda.com/uk-en/trading/hours-of-operation/'),('holiday-current.html','https://www.oanda.com/uk-en/trading/holiday-trading-hours'),('hours-current.html','https://www.oanda.com/uk-en/trading/hours-of-operation/')]
def capture(e):
 f,url=e;x=subprocess.run(['curl','-L','--max-time','40','-sS',url,'-o',str(r/f),'-w','%{http_code}'],capture_output=True,text=True);return {'file':f,'url':url,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':x.stdout,'sha256':hashlib.sha256((r/f).read_bytes()).hexdigest() if (r/f).exists() else None,'error':x.stderr}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:out=list(pool.map(capture,sources))
(r.parent/'retrieval.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
