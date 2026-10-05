import sys,subprocess,re
GROUPS=['INTEREST RATE','EQUITIES','ENERGY','GRAINS','FX','METALS','LIVESTOCK','CRYPTOCURRENCIES','DAIRY','LUMBER','SOFTS','NIKKEI']
for fn in sys.argv[1:]:
    txt=subprocess.run(['pdftotext','-layout',fn,'-'],capture_output=True,text=True).stdout
    lines=txt.split('\n')
    hdr=None
    for l in lines:
        if 'PRODUCT NAME' in l: hdr=l; break
    starts=[m.start() for m in re.finditer(r'\S',hdr)]
    # column boundaries: find token starts of day headers
    cols=[]
    for m in re.finditer(r'(?:MON|TUE|WED|THU|FRI|SAT|SUN)[A-Z]*DAY,', hdr):
        cols.append(m.start())
    bounds=[0]+cols+[10**6]
    labels=['PRODUCT']+[hdr[cols[i]:cols[i+1] if i+1<len(cols) else len(hdr)].strip() for i in range(len(cols))]
    print("##### %s" % fn)
    print("HEADER: %s" % " | ".join(labels))
    cur=None; buckets=None
    out=[]
    started=False
    for l in lines:
        if 'PRODUCT NAME' in l: started=True; continue
        if not started: continue
        if 'Trading hours are subject to change' in l: break
        name=l[:bounds[1]].strip()
        if name and name.upper() in GROUPS:
            if cur: out.append((cur,buckets))
            cur=name.upper(); buckets=[[] for _ in cols]
        if cur:
            for i in range(len(cols)):
                seg=l[bounds[i+1]:bounds[i+2]].strip()
                if seg: buckets[i].append(seg)
    if cur: out.append((cur,buckets))
    for name,bs in out:
        print(" %-18s || %s" % (name, " || ".join(" / ".join(b) for b in bs)))
    print()
