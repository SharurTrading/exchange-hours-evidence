from pathlib import Path
from subprocess import run
import hashlib,json
repo=Path('/workspace/exchange-hours-review-20261031')
outdir=Path('/workspace/exchange-hours-evidence/reviews/2026-10-31-future-update/independent-final-review')
cases=[
 ('nse', 'src/calendar/schedules/holidays/nse_india.rs',
  'ExceptionBlock::order_entry(0, 14 * 3_600 + 5 * 60, 14 * 3_600 + 13 * 60)',
  'ExceptionBlock::order_entry(0, 14 * 3_600 + 5 * 60, 14 * 3_600 + 12 * 60)',
  'venue_sessions','nse_muhurat_2026_preserves_published_phases_and_weekend_trade_date'),
 ('xetra','src/calendar/schedules/holidays/xetra.rs',
  'ExceptionBlock::order_entry(0, 14 * 3_600 + 10 * 60, 15 * 3_600)',
  'ExceptionBlock::order_entry(0, 14 * 3_600 + 10 * 60, 14 * 3_600 + 59 * 60)',
  'equities_holidays','the_2026_final_session_replaces_retail_late_with_shortened_post_trading')]
results=[]
for name,rel,old,new,target,test in cases:
 p=repo/rel; original=p.read_bytes();txt=original.decode();assert txt.count(old)==1
 cmd=['cargo','nextest','run','--test',target,test,'--failure-output','immediate-final','--status-level','fail']
 try:
  p.write_text(txt.replace(old,new));
  with (outdir/(name+'-mutation.log')).open('w') as log:r=run(cmd,cwd=repo,stdout=log,stderr=log)
 finally:p.write_bytes(original)
 assert r.returncode!=0,(name,'mutation unexpectedly passed')
 with (outdir/(name+'-restored.log')).open('w') as log:rr=run(cmd,cwd=repo,stdout=log,stderr=log)
 assert rr.returncode==0,(name,'restored test failed')
 item={'case':name,'file':rel,'original_sha256':hashlib.sha256(original).hexdigest(),'mutation':{'from':old,'to':new},'mutant_exit':r.returncode,'restored_exit':rr.returncode,'restored_exact_bytes':p.read_bytes()==original}
 results.append(item);print(json.dumps(item),flush=True)
(outdir/'mutation-results.json').write_text(json.dumps(results,indent=2))
