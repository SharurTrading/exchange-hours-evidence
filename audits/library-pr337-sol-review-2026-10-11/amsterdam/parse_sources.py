from html.parser import HTMLParser
from pathlib import Path
import json,subprocess,zipfile,xml.etree.ElementTree as E
class Tables(HTMLParser):
 def __init__(self): super().__init__(); self.tables=[]; self.t=None; self.r=None; self.c=None
 def handle_starttag(self,tag,attrs):
  if tag=='table': self.t=[]
  elif tag=='tr' and self.t is not None:self.r=[]
  elif tag in ('td','th') and self.r is not None:self.c=[]
 def handle_data(self,s):
  if self.c is not None:self.c.append(s)
 def handle_endtag(self,tag):
  if tag in ('td','th') and self.c is not None:self.r.append(' '.join(''.join(self.c).split()));self.c=None
  elif tag=='tr' and self.r is not None:self.t.append(self.r);self.r=None
  elif tag=='table' and self.t is not None:self.tables.append(self.t);self.t=None
out={}
for r in json.load(open('/tmp/oanda-amsterdam-exact-review-results/source-manifest.json')):
 p=Path(r['source_file'])
 if p.suffix=='.html':
  t=Tables();t.feed(p.read_text());out[r['id']]=t.tables
 elif p.suffix=='.pdf':
  out[r['id']]=subprocess.check_output(['pdftotext','-layout',str(p),'-'],text=True)
 elif p.suffix=='.xlsx':
  z=zipfile.ZipFile(p); ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
  ss=E.fromstring(z.read('xl/sharedStrings.xml'));strings=[''.join(x.itertext()) for x in ss]
  sheets={}
  for fn in z.namelist():
   if fn.startswith('xl/worksheets/sheet') and fn.endswith('.xml'):
    a=E.fromstring(z.read(fn)); rows=[]
    for row in a.findall('.//s:row',ns):
     cells=[]
     for c in row.findall('s:c',ns):
      v=c.find('s:v',ns)
      if v is not None:cells.append((c.attrib['r'],strings[int(v.text)] if c.attrib.get('t')=='s' else v.text))
     rows.append(cells)
    sheets[fn]=rows
  out[r['id']]=sheets
json.dump(out,open('/tmp/oanda-amsterdam-exact-review-results/independent-source-tables.json','w'),indent=2)
for k,v in out.items():
 if isinstance(v,list):
  print(k)
  for t in v:
   if any('Trading' in ' '.join(row) or 'Closed' in ' '.join(row) for row in t):print(json.dumps(t))
 else: print(k, str(v)[:180])
