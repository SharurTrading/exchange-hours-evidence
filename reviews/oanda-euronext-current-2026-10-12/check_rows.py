from html.parser import HTMLParser
from pathlib import Path
import datetime,re,json,hashlib
class Tables(HTMLParser):
 def __init__(self):super().__init__();self.tables=[];self.table=None;self.row=None;self.cell=None
 def handle_starttag(self,tag,attrs):
  if tag=='table':self.table=[]
  elif tag=='tr' and self.table is not None:self.row=[]
  elif tag in ('td','th') and self.row is not None:self.cell=[]
 def handle_data(self,data):
  if self.cell is not None:self.cell.append(data)
 def handle_endtag(self,tag):
  if tag in ('td','th') and self.cell is not None:self.row.append(' '.join(''.join(self.cell).split()));self.cell=None
  elif tag=='tr' and self.row is not None:self.table.append(self.row);self.row=None
  elif tag=='table' and self.table is not None:self.tables.append(self.table);self.table=None
raw=Path('/tmp/oanda-euronext-root-proof/fresh-hours-holidays.html').read_bytes();p=Tables();p.feed(raw.decode());tables=[t for t in p.tables if t and 'Brussels' in t[0] and any('2026' in str(r) for r in t)]
assert len(tables)==1
assert hashlib.sha256(raw).hexdigest()=='f4f3d2ee85e88557db2aa6a29bf9ec23d1d2d82eaaa1a8cca2d91175c94fc831'
t=tables[0];result={}
for city,tree in [('Brussels','/tmp/oanda-brussels-root-review'),('Lisbon','/tmp/oanda-lisbon-root-review')]:
 i=t[0].index(city); expected=[]
 for row in t[1:]:
  if len(row)<=i or not ('Closed' in row[i] or 'Half' in row[i]):continue
  d,m=re.search(r'(\d+) (January|April|May|December)',row[0]).groups()
  date=datetime.datetime.strptime(f'{d} {m} 2026','%d %B %Y').date()
  expected.append((date.isoformat(),'Closed' if row[i]=='Closed' else 'Unsourced'))
 module=(Path(tree)/f'src/calendar/schedules/holidays/euronext_{city.lower()}.rs').read_text()
 actual=[(datetime.date(int(y),int(m),int(d)).isoformat(),kind) for y,m,d,kind in re.findall(r'\((2026), (\d+), (\d+), (Closed|Unsourced)',module)]
 assert sorted(expected)==sorted(actual),(city,expected,actual)
 assert len(actual)==7
 result[city]=actual
print(json.dumps(result,indent=2))
