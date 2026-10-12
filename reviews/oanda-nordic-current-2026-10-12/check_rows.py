import re,datetime,pathlib,json,hashlib
store=pathlib.Path('/tmp/oanda-public-final-review/captures/nasdaq-current-2026-10-12')
s=(store/'nasdaq-trading-hours.web-extract.txt').read_text()
assert hashlib.sha256((store/'nasdaq-trading-hours.web-extract.txt').read_bytes()).hexdigest()=='9f8fe49d65db294d48e7bd94e7b4b6b098dac44f102ad74dd71c89b5aa9bff4c'
lines={int(n):t for n,t in re.findall(r'^L(\d+): (.*)$',s,re.M)}
selected={'copenhagen':[(74,'Closed'),(100,'Closed')],'helsinki':[(84,'Closed'),(110,'Closed')],'stockholm':[(77,'Closed'),(79,'ReplacementBlocks'),(103,'Closed'),(105,'ReplacementBlocks')]}
result={}
for city, selections in selected.items():
 expected=[]
 for line,kind in selections:
  text=lines[line].split('|')[0]
  for month,day,year in re.findall(r'([A-Za-z]+) (\d+), (202[67])',text):
   date=datetime.datetime.strptime(f'{month[:3]} {day} {year}','%b %d %Y').date()
   expected.append((date.isoformat(),kind))
 module=pathlib.Path('src/calendar/schedules/holidays/nasdaq_'+city+'.rs').read_text()
 actual=[(datetime.date(int(y),int(m),int(d)).isoformat(),kind) for y,m,d,kind in re.findall(r'\((202[67]), (\d+), (\d+), (Closed|ReplacementBlocks)',module)]
 assert sorted(expected)==sorted(actual),(city,expected,actual)
 assert len(expected)==len(set(expected))
 result[city]={'rows':len(actual),'half_days':sum(k=='ReplacementBlocks' for _,k in actual),'source_lines':[n for n,_ in selections]}
print(json.dumps(result,indent=2))
