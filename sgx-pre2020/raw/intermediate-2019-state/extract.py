import json,sys,re,html
TARGETS=["SGX Nikkei 225 Index Futures","SGX FTSE China A50 Index Futures",
         "SGX MSCI Singapore Free Index Futures","SGX MSCI Taiwan Index Futures",
         "SGX MSCI Singapore Free NTR (USD) Index Futures","SGX FTSE Taiwan Index Futures",
         "SGX MSCI Singapore Index Futures","SGX MSCI Taiwan NTR (USD) Index Futures"]
def walk(o):
    if isinstance(o,dict):
        if 'tradingHours' in o: yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
def clean(th):
    if isinstance(th,dict): th=th.get('processed') or ''
    t=re.sub(r'<br\s*/?>','\n',th or ''); t=re.sub(r'</p>','\n',t); t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t)
    return '\n'.join(x.strip() for x in t.split('\n') if x.strip())
for f in sys.argv[1:]:
    d=json.loads(open(f).read())
    print("##########",f)
    names={}
    for n in walk(d):
        nm=(n.get('title') or n.get('name') or '').strip()
        names[nm]=n
    for t in TARGETS:
        if t in names:
            print("---",t); print(clean(names[t].get('tradingHours')))
        else:
            print("--- ",t,": NOT PRESENT")
