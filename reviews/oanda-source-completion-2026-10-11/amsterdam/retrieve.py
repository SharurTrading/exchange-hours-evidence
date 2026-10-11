from pathlib import Path
import subprocess,hashlib,json,datetime,concurrent.futures
root=Path('/tmp/oanda-amsterdam-exact-review-results');(root/'retrieved').mkdir(exist_ok=True)
rows=json.loads((root/'source-manifest.json').read_text())
def retrieve(row):
 row=row.copy();suffix=Path(row['source_file']).suffix;out=root/'retrieved'/(row['id']+suffix);run=subprocess.run(['curl','-L','--fail','--max-time','25','-o',str(out),row['url']],capture_output=True,text=True)
 row['retrieval_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();row['exit_code']=run.returncode
 if run.returncode:row['error']=run.stderr[-500:]
 else:row['retrieved_file']=str(out);row['retrieved_sha256']=hashlib.sha256(out.read_bytes()).hexdigest();row['digest_matches']=row['retrieved_sha256']==row['expected_sha256']
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(retrieve,rows))
(root/'second-retrieval.json').write_text(json.dumps(results,indent=2));print('retrieved',sum(r['exit_code']==0 for r in results),'of',len(results),'byte-identical',sum(r.get('digest_matches',False) for r in results));print([(r['id'],r['exit_code']) for r in results if r['exit_code']])
