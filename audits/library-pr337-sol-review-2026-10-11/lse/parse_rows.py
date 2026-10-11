import json,re,pathlib
from html.parser import HTMLParser
class Tables(HTMLParser):
 def __init__(self):super().__init__();self.rows=[];self.r=None;self.c=None
 def handle_starttag(self,t,a):
  if t=='tr':self.r=[]
  elif t in ['td','th'] and self.r is not None:self.c=[]
 def handle_data(self,s):
  if self.c is not None:self.c.append(s)
 def handle_endtag(self,t):
  if t in ['td','th'] and self.c is not None:self.r.append(' '.join(''.join(self.c).split()));self.c=None
  elif t=='tr' and self.r is not None:self.rows.append(self.r);self.r=None
x=json.load(open('/tmp/oanda-lse-exact-review-results/row-audit.json'));months='January February March April May June July August September October November December'.split()
def strings(a):
 if isinstance(a,str):yield a
 elif isinstance(a,list):
  for v in a:yield from strings(v)
 elif isinstance(a,dict):
  for v in a.values():yield from strings(v)
for r in x:
 p=pathlib.Path(r['file'])
 if p.suffix=='.pdf':r['method']='visual page14';continue
 s=p.read_text()
 if p.suffix=='.json':s=' '.join(strings(json.loads(s)))
 t=Tables();t.feed(s)
 y,m,d=map(int,r['date'].split('-'));pat=rf'\b0?{d}\s+{months[m-1]}\s+{y}\b'
 matches=[row for row in t.rows if re.search(pat,' '.join(row))]
 r['source_rows']=matches
 r['source_agrees']=any(('12:30' in ' '.join(row) if r['kind'].startswith('early_close') else 'non-trading' in ' '.join(row).lower()) for row in matches)
json.dump(x,open('/tmp/oanda-lse-exact-review-results/row-audit.json','w'),indent=2)
print('Verified',sum(r.get('source_agrees',False) for r in x),'plusvisual',sum(r.get('method')=='visual page14' for r in x));print([(r['date'],r['id'],r.get('source_rows')) for r in x if not r.get('source_agrees') and not r.get('method')])
class Text(HTMLParser):
 def __init__(self):super().__init__();self.a=[]
 def handle_data(self,s):self.a.append(s)
for r in x:
 if r.get('source_agrees') or r.get('method'):continue
 s=pathlib.Path(r['file']).read_text();t=Tables();t.feed(s);v=Text();v.feed(s);text=' '.join(' '.join(v.a).split());y,m,d=map(int,r['date'].split('-'))
 if r['kind']=='Closed':
  year=None
  for row in t.rows:
   if row and re.fullmatch('20[0-9]{2}',row[0]):year=int(row[0])
   if year==y and re.search(rf'\b{d}\s+{months[m-1]}\b',' '.join(row)):
    r['source_rows']=[row];r['source_agrees']=True;r['derivation']='year header carried through operator closure grid; star is reporting availability, not executable trading'
 else:
  pat=rf'On[^.]*\b{d}\s+December[^.]*\b{y}\s+all Exchange markets will close from 12[.:]30 London time onwards'
  hits=re.findall(pat,text);r['source_prose']=hits;r['source_agrees']=bool(hits)
json.dump(x,open('/tmp/oanda-lse-exact-review-results/row-audit.json','w'),indent=2)
print('Final matches',sum(r.get('source_agrees',False) for r in x),'visual',sum(r.get('method')=='visual page14' for r in x),'missing',[(r['date'],r['id']) for r in x if not r.get('source_agrees') and not r.get('method')])
