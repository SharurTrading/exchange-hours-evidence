from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,re,subprocess
root=Path('/workspace/exchange-hours-rs')
out=Path(__file__).resolve().parent
notice=(out/'final-trading-session-2026.txt').read_text()
assert 'Wednesday, 30 December' in notice and '2026.' in notice
section=notice.split('2. Market Deutsche Börse Xetra',1)[1].split('3. Availability',1)[0]
for literal in ['from 7.00 a.m.', 'from 8.00 a.m.', 'from 8.55 a.m.', 'from 1.00 p.m.', 'from 2.00 p.m.', 'from 3.00 p.m.', 'no earlier than 2.05 p.m.', 'at 2.10 p.m.']:
 assert literal in section,literal
rel='src/calendar/schedules/holidays/xetra.rs'
s=(root/rel).read_text()
block=re.search(r'static FINAL_SESSION_2026:.*?= \[(.*?)\n\];',s,re.S).group(1)
(out/'merged-final-session-block.txt').write_text(block+'\n')
def number(src):
 def n(x):
  if isinstance(x,ast.Constant) and isinstance(x.value,int):return x.value
  if isinstance(x,ast.BinOp) and isinstance(x.op,ast.Add):return n(x.left)+n(x.right)
  if isinstance(x,ast.BinOp) and isinstance(x.op,ast.Mult):return n(x.left)*n(x.right)
  raise ValueError(ast.dump(x))
 return n(ast.parse(src.strip(),mode='eval').body)
rows=[]
for kind,offset,start,end in re.findall(r'ExceptionBlock::(\w+)\(([^,]+),([^,]+),([^\)]+)\)',block):
 rows.append({'kind':kind,'day_offset':number(offset),'start_ssm':number(start),'end_ssm':number(end)})
expected=[('order_entry',25200,28800),('extended',28800,32430),('regular',32430,46800),('extended',46800,46950),('regular',46950,50400),('extended',50400,51000),('order_entry',51000,54000)]
assert [(r['kind'],r['start_ssm'],r['end_ssm']) for r in rows]==expected
assert all(r['day_offset']==0 for r in rows)
assert '(2026, 12, 30, ReplacementBlocks(&FINAL_SESSION_2026), T1, "DB-FINAL-SESSION-2026")' in s
capture=next(r for r in json.loads((out/'captures.json').read_text()) if r['file']=='final-trading-session-2026.pdf')
assert capture['sha256']=='d3618ef9738a3cae92909d11d4eaf820ab7b71d1e723c1fa04a21062e9738115'
assert hashlib.sha256((out/capture['file']).read_bytes()).hexdigest()==capture['sha256']
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
baseline='d3f6b21db8f4f7523f0c79b786c16c6852c4678c'
baseline_source=subprocess.check_output(['git','show',baseline+':'+rel],cwd=root,text=True)
assert baseline_source==s,'runtime data changed since merged baseline'
doc='docs/evidence/xetra.md'
baseline_doc=subprocess.check_output(['git','show',baseline+':'+doc],cwd=root,text=True)
current_doc=(root/doc).read_text()
def documents_section(t):return t.split('### Documents',1)[1].split('## Sources',1)[0]
assert documents_section(baseline_doc)==documents_section(current_doc),'Documents table changed from runtime sourcing baseline'
j={'checked_utc':datetime.now(timezone.utc).isoformat(),'crate_head':head,'module':rel,'module_sha256':hashlib.sha256(s.encode()).hexdigest(),'runtime_module_unchanged_from_merged_baseline':True,'documents_table_unchanged_from_merged_baseline':True,'confirmation_metadata_location':'captures.json and channel-checks.json; no new Documents rows','source_pdf_sha256':capture['sha256'],'source_bytes_identical_to_merged_document':True,'trade_date':'2026-12-30','timezone':'Europe/Berlin','same_day_blocks':rows,'source_literal_checks':8,'comparison':'matches merged 7-block replacement; no runtime discrepancy','interpretation_limits':['The final-session notice fixes the special-date phase starts, closing auction earliest price time, DAX/MDAX/SDAX Trade-at-Close end, and post-trading end.','The 09:00:30 opening and 13:02:30 intraday conservative uncross boundaries are retained normal-profile conventions, not new literal final-notice times.','Pre-trading and post-trading classification and the combined extended auction/TAC block preserve the existing documented XETR DAX-share scope.']}
(out/'runtime-comparison.json').write_text(json.dumps(j,indent=2)+'\n')
print(json.dumps(j,indent=2))
