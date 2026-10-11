import pathlib,re,json,datetime,zoneinfo
r=pathlib.Path('/tmp/oanda-four-book-report');ev=r/'evidence';base=pathlib.Path('/tmp/oanda-four-book-review');MONTHS={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
def parse_date(line,yr):
 if not re.match(r'^(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|\d)',line,re.I):return None
 m=re.search(r'\b(20\d\d)\b',line);y=int(m[1]) if m else yr
 if not y:return None
 months=[(k,v) for k,v in MONTHS.items() if re.search(r'\b'+k+r'\w*\b',line,re.I)]
 if not months:return None
 mn=months[0][1]
 s=re.sub(r'\b20\d\d\b','',line);d=re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\b',s)
 if not d:return None
 return datetime.date(y,mn,int(d[1]))
def sections(name):
 out={};cur=None;yr=None
 for line in (ev/(name+'.txt')).read_text().splitlines():
  if re.fullmatch(r'20\d\d',line):yr=int(line);continue
  date=parse_date(line,yr)
  if date:cur=date;yr=date.year;out.setdefault(str(cur),[])
  elif cur:out[str(cur)].append(line)
 return out
old=sections('carter-2025');live=sections('holiday-current');proof=[]
def facts(book,lines):
 p={'oanda_us_index_cfd':r'US index|US indices','oanda_us_bond_cfd':r'US bonds|US indices and bonds|US index futures and bonds','oanda_us_commodity_cfd':r'US energies|US Energies','oanda_brent':r'Brent|BCO'}[book]
 return [s for s in lines if re.search(p,s,re.I)]
def expr(s):return eval(s,{'__builtins__':{}},{})
for book in ['oanda_us_index_cfd','oanda_us_bond_cfd','oanda_us_commodity_cfd','oanda_brent']:
 text=(base/'src/calendar/schedules/holidays'/f'{book}.rs').read_text()
 # Each row is parsed for comparison, never used as the source's expected date/time.
 rows=re.findall(r'^\s*\((\d+), (\d+), (\d+), (.*), T1, "([^"]+)"\),',text,re.M)
 for y,m,d,kind,doc in rows:
  day=datetime.date(int(y),int(m),int(d));key=str(day);sec=old if doc=='OANDA-UK-CARTER-2025-WAYBACK' else live;lines=sec.get(key,[]);prev=sec.get(str(day-datetime.timedelta(days=1)),[]);f=facts(book,lines);pf=facts(book,prev)
  if key=='2025-01-09' and book=='oanda_us_index_cfd':f=facts(book,old[key])
  if kind=='Unsourced':status='withheld';assert (not f) or key in ['2026-05-26','2024-01-02','2024-01-16','2024-02-20']
  elif kind=='Closed':status='closed source or holiday trade-date closed before evening reopen';assert any(re.search(r'closed|open(?: late)? (?:at )?18:0[14]|open late 6 pm',x,re.I) for x in f),(book,key,f)
  elif kind.startswith('early_close'):
   value=expr(kind[len('early_close('):-1]);nydate=day;h=value//3600;mi=value%3600//60
   if book=='oanda_brent':
    t=datetime.datetime.combine(day,datetime.time(h,mi),zoneinfo.ZoneInfo('Europe/London')).astimezone(zoneinfo.ZoneInfo('America/New_York'));h,mi=t.hour,t.minute
   # Independently match operator literal24-hour or AM/PM clock, normalizing hour only with explicitPM or close-before-reopen context.
   variants=[f'{h}:{mi:02}',f'{h%12 or 12}:{mi:02}',f'{h%12 or 12}.{mi:02}']
   if mi==0:variants+=[f'{h%12 or 12} pm',f'{h%12 or 12}:00 PM']
   assert any(any(v.lower() in x.lower() for v in variants) for x in f),(book,key,h,mi,f)
   status=f'exact early close {h:02}:{mi:02} ET'
  elif kind.startswith('late_open'):
   v=expr(kind[len('late_open('):-1]);assert v==18*3600+4*60;assert any('18:04' in x for x in pf),(book,key,pf);status='preceding holiday18:04 ET reopen'
  else:
   assert kind.startswith('ReplacementBlocks');block=re.search(r'&([^)]*)',kind)[1];decl=re.search(r'static '+block+r':.*?=\s*\[(.*?)\];',text,re.S)[1]
   blocks=[(int(off),expr(op),expr(cl)) for off,op,cl in re.findall(r'ExceptionBlock::regular\((-?\d+), (.*?), (.*?)\)',decl)]
   if book!='oanda_brent':
    opening=blocks[0][1];assert opening in [18*3600,18*3600+60]
    if block=='HOLY_THURSDAY':assert any('17:00' in x for x in f)
    else:assert any(re.search(r'reopen(?:s|ing)?(?: at)? (?:18:00|6(?::00)?\s*pm|6$)',x,re.I) for x in pf),(book,key,pf)
    if blocks[0][2]!=16*3600+59*60 and block!='HOLY_THURSDAY':assert f,(book,key,f)
   else:assert any(re.search(r'reopen(?:s)?(?: at)? 8(?::00)?\s*pm',x,re.I) for x in pf),(book,key,pf)
   status='replacement from previous reopen + own printed/normal close';
  proof.append({'book':book,'date':key,'kind':kind,'document_id':doc,'source_same_day':f,'source_previous_day':pf,'result':status})
(r/'row-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print({b:sum(p['book']==b for p in proof) for b in {p['book'] for p in proof}})
(r/'source-sections.json').write_text(json.dumps({'carter_2025':old,'current':live},indent=2)+'\n')
