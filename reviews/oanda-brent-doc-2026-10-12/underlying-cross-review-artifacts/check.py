import json,pathlib,hashlib,datetime,subprocess
from zoneinfo import ZoneInfo
bundle=pathlib.Path('/tmp/oanda-public-final-review/normal-weeks/oanda-underlying-policy-2026-10-12');r=json.loads(pathlib.Path('/tmp/oanda-underlying-brent-resolution.json').read_text());rows=r['rows'];g=json.loads(pathlib.Path('/tmp/oanda-unresolved-holidays-26.json').read_text());expected={x['date'] for x in g if x['book']=='oanda_brent'}
assert len(rows)==17 and {x['trade_date'] for x in rows}==expected
assert sum(x['policy_kind']=='inherit_normal' for x in rows)==13
assert sum(x['policy_kind']=='inherit_reopen' for x in rows)==4
proof=[];blocks=0
for x in rows:
 d=datetime.date.fromisoformat(x['trade_date']);bs=x['proposed_executable_blocks'];assert len(bs)==(1 if d.weekday()==4 else 2)
 for j,b in enumerate(bs):
  o=datetime.datetime.fromisoformat(b['open_local']);c=datetime.datetime.fromisoformat(b['close_local']);ou=datetime.datetime.fromisoformat(b['open_utc']);cu=datetime.datetime.fromisoformat(b['close_utc']);assert o.astimezone(datetime.timezone.utc)==ou and c.astimezone(datetime.timezone.utc)==cu
  assert o.utcoffset()==o.replace(tzinfo=ZoneInfo('Europe/London')).utcoffset();assert c.utcoffset()==c.replace(tzinfo=ZoneInfo('Europe/London')).utcoffset();assert c>o
  if j==0:
   assert c.time().isoformat()=='21:59:00';assert c.date()==d
   if x['policy_kind']=='inherit_reopen':assert o.date()==d and o.time().isoformat()=='01:00:00'
   elif d.weekday()==0:assert o.date()==d-datetime.timedelta(days=1) and o.time().isoformat()=='23:01:00'
   else:assert o.date()==d and o.time().isoformat()=='01:01:00'
  else:assert o.date()==c.date()==d and o.time().isoformat()=='22:05:00' and c.time().isoformat()=='22:59:00'
  blocks+=1
 assert 'no operator-proof claim' in x['classification']
 proof.append({'date':str(d),'weekday':d.strftime('%A'),'policy':x['policy_kind'],'checked_blocks':len(bs),'UTC_verified':True})
manifest=json.loads((bundle/'brent/source-manifest.json').read_text());checks=[]
for s in manifest:
 p=bundle/'brent'/pathlib.Path(s['file']).name;assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256'];checks.append({'file':str(p),'sha256':s['sha256'],'url':s['url']})
 if p.suffix=='.pdf':subprocess.run(['pdftotext','-layout',str(p),'/tmp/oanda-brent-cross-review/'+p.stem+'.txt'],check=True)
for x in rows:
 for s in x['sources']:assert hashlib.sha256((bundle/'brent'/pathlib.Path(s['file']).name).read_bytes()).hexdigest()==s['sha256']
reportpaths=['/tmp/oanda-underlying-brent-resolution.md','/tmp/oanda-underlying-brent-resolution.json']
json.dump({'reviewed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'artifact_hashes':{p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest() for p in reportpaths},'row_proofs':proof,'block_count':blocks,'source_checks':checks},open('/tmp/oanda-brent-cross-review/check-results.json','w'),indent=2)
print('PASS:',len(rows),'rows,',blocks,'blocks,',len(checks),'manifest source digests; all embedded source digests match')
