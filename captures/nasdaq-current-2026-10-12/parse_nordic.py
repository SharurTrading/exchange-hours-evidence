import pathlib,re,json
p=pathlib.Path(__file__).parent
text=(p/"nasdaq-trading-hours.web-extract.txt").read_text()
lines={int(n):s for n,s in re.findall(r"^L(\d+): (.*)$",text,re.M)}
selectors={'copenhagen':[(100,'Closed'),(74,'Closed')],'helsinki':[(110,'Closed'),(84,'Closed')],'stockholm':[(103,'Closed'),(105,'ReplacementBlocks(&HALF_DAY)'),(77,'Closed'),(79,'ReplacementBlocks(&HALF_DAY)')]}
months={'Jan':1,'Apr':4,'May':5,'Jun':6,'Mar':3,'March':3,'Dec':12,'Oct':10,'Nov':11}
parsed={}
for identity,parts in selectors.items():
 rows=[]
 for line,kind in parts:
  for month,day,year in re.findall(r"([A-Z][a-z]+) (\d+), (202[67])",lines[line].split("|")[0]):
   rows.append((int(year),months[month],int(day),kind))
 parsed[identity]=sorted(rows)
(p/"nasdaq-parsed-rows.json").write_text(json.dumps(parsed,indent=2)+"\n")
print({k:len(v) for k,v in parsed.items()})
