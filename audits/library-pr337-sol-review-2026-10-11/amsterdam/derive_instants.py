import pathlib,json,re
x=json.load(open('/tmp/oanda-amsterdam-exact-review-results/independent-source-tables.json'))
r=json.load(open('/tmp/oanda-amsterdam-exact-review-results/row-audit.json'))
for row in r:
 doc=row['document'];a=x[doc]
 if row['kind'].startswith('early_close'):
  if doc=='EURONEXT-EOY-2010':
   source=next(l for l in a.splitlines() if re.match(r'\s*J0\s+Equities AEX',l)); clock=re.findall(r'\b(\d\d):(\d\d)\b',source)[-1]
  elif doc=='EURONEXT-PR-2011':
   source=re.search(r'at (\d+)\.(\d+) pm CET',a).group(0);h,m=map(int,re.search(r'(\d+)\.(\d+)',source).groups());clock=(h+12,m)
  elif doc.startswith('EURONEXT-EOY-202'):
   line=next(v for cells in a['xl/worksheets/sheet1.xml'] for col,v in cells if col.startswith('L') and any(v2=='J0' for c2,v2 in cells));source=line;clock=re.findall(r'\b(\d\d):(\d\d)\b',line)[-1]
  else:
   text=' '.join(a.split()) if isinstance(a,str) else pathlib.Path('/tmp/oanda-amsterdam-exact-review-results/'+doc+'.txt').read_text()
   source=re.search(r'(?:will close at|closing by|close by)\s+(\d\d):(\d\d)\s*CET',text).group(0);clock=re.findall(r'(\d\d):(\d\d)',source)[-1]
  h,m=map(int,clock);derived=h*3600+m*60;expected=int(re.search(r'(\d[\d_]*)',row['kind']).group(1).replace('_',''));row['instant_source']=source;row['derived_close_ssm']=derived;row['instant_agrees']=derived==expected
json.dump(r,open('/tmp/oanda-amsterdam-exact-review-results/row-audit.json','w'),indent=2)
print('Derived23clocks',sum('derived_close_ssm' in a for a in r),'mismatches',[(a['date'],a['derived_close_ssm'],a['kind']) for a in r if a.get('instant_agrees')==False])
