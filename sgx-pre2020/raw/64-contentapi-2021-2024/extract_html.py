import re,json,glob,sys
def contracts(t):
    out=[]
    for m in re.finditer(r'"title"\s*:\s*"((?:[^"\\]|\\.)*)"', t):
        seg=t[m.end():m.end()+6000]
        mm=re.search(r'"tradingHours"\s*:\s*', seg)
        if not mm: continue
        if '"title"' in seg[:mm.start()]: continue
        dec=json.JSONDecoder()
        try: val,_=dec.raw_decode(seg, mm.end())
        except Exception: continue
        title=json.loads('"'+m.group(1)+'"')
        p = val.get('processed') if isinstance(val,dict) else val
        out.append((title,p))
    return out
res={}
for f in sorted(glob.glob('raw_html_*.html')):
    ts=f[9:-5]
    t=open(f,encoding='utf8',errors='replace').read()
    seen={}
    for title,p in contracts(t):
        seen.setdefault(title,p)
    res[ts]=seen
json.dump(res,open('extracted_ssr_tradinghours.json','w'),indent=1,ensure_ascii=False)
TARGET=['SGX Nikkei 225 Index Futures','SGX Nikkei 225 Index Options','SGX FTSE China A50 Index Futures','SGX MSCI Singapore Index Futures','SGX FTSE Taiwan Index Futures','SGX MSCI Singapore Free NTR (USD) Index Futures']
for ts in sorted(res):
    for t in TARGET:
        if t in res[ts]:
            print(ts,'|',t,'|',repr(res[ts][t]))
