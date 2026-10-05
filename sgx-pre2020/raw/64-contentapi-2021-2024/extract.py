import json,glob,os,re,collections
TARGETS=[
 'SGX Nikkei 225 Index Futures',
 'SGX FTSE China A50 Index Futures',
 'SGX MSCI Singapore Index Futures',
 'SGX FTSE Taiwan Index Futures',
 'SGX MSCI Singapore Free NTR (USD) Index Futures',
 'SGX MSCI Singapore NTR (USD) Index Futures',
]
out=collections.OrderedDict()
for f in sorted(glob.glob('dec_*.json')):
    ts=f[4:-5]
    try: j=json.load(open(f))
    except Exception: continue
    res=((j.get('data') or {}).get('list') or {}).get('results') or []
    if not res: continue
    per={}
    for p in res:
        for c in (p['data'].get('contracts') or []):
            d=c['data']; t=(d.get('title') or '').strip()
            if t in TARGETS:
                th=(d.get('tradingHours') or {})
                per[t]={'contractCode':d.get('contractCode'),
                        'tradingHours_processed': th.get('processed') if isinstance(th,dict) else th,
                        'tradingHoursOnLastDay': d.get('tradingHoursOnLastDay')}
    out[ts]=per
json.dump(out, open('extracted_tradinghours.json','w'), indent=1, ensure_ascii=False)

def norm(s):
    return s if s is not None else '(ABSENT)'

prev={}
for ts,per in out.items():
    changed=[]
    for t in TARGETS:
        cur=norm((per.get(t) or {}).get('tradingHours_processed'))
        if t not in prev:
            changed.append((t,'FIRST-SEEN',None,cur))
        elif prev[t]!=cur:
            changed.append((t,'CHANGED',prev[t],cur))
        prev[t]=cur
    if changed:
        print('='*100)
        print('CAPTURE', ts)
        for t,kind,old,new in changed:
            print('-'*80)
            print(f'  {t}  [{kind}]')
            if old is not None:
                print('   PREV:', repr(old))
            print('   NOW :', repr(new))
