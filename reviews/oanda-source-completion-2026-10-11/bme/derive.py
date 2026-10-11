import pathlib,re,json,datetime,hashlib
root=pathlib.Path('/tmp/bme-independent-review'); ev=root/'evidence'
months={'enero':1,'abril':4,'marzo':3,'mayo':5,'diciembre':12}
closures=[]
for year in range(2010,2027):
 text=(ev/f'{year}-calendar.txt').read_text()
 for line in text.splitlines():
  if not re.match(r'^\s*[−–-]',line): continue
  m=re.search(r'(\d{1,2})\s+(?:de\s+)?(Enero|Abril|Marzo|Mayo|Diciembre)',line,re.I)
  if m: closures.append((year,months[m[2].lower()],int(m[1]),f'BME-CAL-{year}'))
source=pathlib.Path('/tmp/bme-independent-build/src/calendar/schedules/holidays/bme.rs').read_text()
actual=[(int(y),int(m),int(d),doc) for y,m,d,doc in re.findall(r'\((\d+), (\d+), (\d+), Closed, T1, "([^"]+)"\)',source)]
assert actual==closures,(set(actual)-set(closures),set(closures)-set(actual)); assert len(closures)==86
replacements=[]
for path in sorted(ev.glob('*-eves.txt')):
 text=path.read_text();year=int(path.name[:4]); assert re.search(r'24\s+y\s+31\s+de\s+diciembre',text,re.I) and re.search(r'(?:año|diciembre de)\s+'+str(year),text,re.I),path
 assert '8:30' in text and '9:00' in text and '13:55' in text and '14:00' in text
 tal='Fin fase TAL' in text
 if tal: assert '14:10' in text
 for d in (24,31):replacements.append((year,12,d,'HALF_DAY_TAL' if tal else 'HALF_DAY_PRE_TAL',f'BME-EVES-{year}'))
actualrepl=[(int(y),int(m),int(d),block,doc) for y,m,d,block,doc in re.findall(r'\((\d+), (\d+), (\d+), ReplacementBlocks\(&([^)]+)\), T1, "([^"]+)"\)',source)]
assert actualrepl==replacements;assert len(replacements)==18
withheld=re.findall(r'\((2026), (12), (24|31), Unsourced, T1, "(BME-CAL-2026)"\)',source);assert len(withheld)==2
idx=json.loads((ev/'operator-regulation-index.json').read_text()); rs=idx['results']; absent=[r for r in rs if 'sociedad-de-bolsas' in r['url'] and ('horarios-24-y-31' in r['url'].lower() or 'calendario' in r['url'].lower()) and ('2027' in r['title'] or ('2026' in r['title'] and ('24' in r['title'] or '31' in r['title'])))];assert not absent,absent
report={'closure_count':len(closures),'source_derived_closures':closures,'reviewer_every_fifth_closure':closures[::5],'replacement_count':len(replacements),'replacements':replacements,'withheld':withheld,'operator_index_result_count':len(rs),'missing_2026_eves_or_2027_calendar':absent,'index_sha256':hashlib.sha256((ev/'operator-regulation-index.json').read_bytes()).hexdigest()}
(root/'source-validation.json').write_text(json.dumps(report,indent=2)+'\n');print('Independently parsed all86closed rows; all18replacement dates and2withheld match. Reviewer18samples. Index4580records no2026eves/2027calendar.')
