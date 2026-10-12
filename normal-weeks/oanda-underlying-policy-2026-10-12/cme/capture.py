import pathlib,re,json,hashlib,urllib.request,concurrent.futures,datetime,gzip
root=pathlib.Path('/tmp/oanda-public-final-review');out=pathlib.Path('/tmp/oanda-underlying-cme-evidence');doc=pathlib.Path('/tmp/oanda-source-completion/docs/evidence/globex_interest_rates.md').read_text();ids=['new-years-day-2024.pdf @2026-08-11T16:57:16Z','CME-SVC-2024-01-14','CME-SVC-2024-02-18','CME-SVC-2024-12-24','CME-SVC-2026-05-24'];paths=['holidays/raw/cme-2022-2024/new-years-day-2024.pdf','holidays/raw/cme-2022-2024-fix/api_2024-01-14.json','holidays/raw/cme-2022-2024-fix/api_2024-02-18.json','holidays/raw/cme-2022-2024/api_2024-12-24.json','holidays/raw/cme-2025-2027/arc/thbp_2026-05-24_2026-05-26_20260619114105.json']
def capture(item):
 i,p=item;line=next(s for s in doc.splitlines() if s.startswith('| `'+i+'` |') and '<https://' in s);url=re.search(r'<(https://[^>]+)>',line)[1];b=(root/p).read_bytes();saved=out/pathlib.Path(p).name;saved.write_bytes(b);entry={'id':i,'url':url,'saved_path':str(saved),'existing_source':str(root/p),'sha256':hashlib.sha256(b).hexdigest(),'source_table_sha256':re.findall(r'`([a-f0-9]{64})`',line)[0],'copied_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'});fresh=urllib.request.urlopen(req,timeout=35).read();fp=out/('fresh-'+saved.name);fp.write_bytes(fresh);entry.update(fresh_path=str(fp),fresh_sha256=hashlib.sha256(fresh).hexdigest(),retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),fresh_byte_identical=fresh==b)
 except Exception as e:entry['fresh_retrieval_error']=str(e)
 if b[:2]==b'\x1f\x8b':entry['decompressed_sha256']=hashlib.sha256(gzip.decompress(b)).hexdigest()
 return entry
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:results=list(ex.map(capture,zip(ids,paths)))
(out/'retrieval.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
