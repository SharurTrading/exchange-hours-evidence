import xlrd, re, os, glob, json, sys, datetime
FAM = {
 'cme group equity':'equity_index','equity products':'equity_index',
 'cme group interest rate':'interest_rates','interest rate products':'interest_rates',
 'cme group fx':'fx','fx products':'fx',
 'nymex, comex, and dme':'energy+metals','nymex, comex & dme':'energy+metals',
 'nymex, comex, and dubai mercantile (dme)':'energy+metals',
 'energy, metals & dme products':'energy+metals',
 'grains and oilseeds':'grains_oilseeds','grains and oilseeds (cbot & kcbt)':'grains_oilseeds',
 'livestock':'livestock','lumber':'lumber','dairy':'dairy',
}
MON='january february march april may june july august september october november december'.split()
def fmt(c,bk):
    if c.ctype==0: return ''
    if c.ctype==1: return c.value.strip()
    if c.ctype==2:
        v=c.value; return str(int(v)) if v==int(v) else str(v)
    if c.ctype==3:
        try:
            t=xlrd.xldate_as_tuple(c.value,bk.datemode); return "%02d:%02d"%(t[3],t[4])
        except Exception: return str(c.value)
    if c.ctype==4: return 'TRUE' if c.value else 'FALSE'
    return str(c.value)
def ffill(v):
    out=[];last=''
    for x in v:
        if x.strip(): last=x.strip()
        out.append(last)
    return out
recs=[]
for path in sorted(glob.glob('xls/*.xls')):
    bk=xlrd.open_workbook(path)
    for sh in bk.sheets():
        head=[[fmt(sh.cell(r,c),bk) for c in range(sh.ncols)] for r in range(min(sh.nrows,12))]
        title=' '.join(x for x in head[0] if x)
        ymap={}
        for m,d,y in re.findall(r'(%s)\s+(\d{1,2}),?\s*(\d{4})'%'|'.join(MON), title, re.I):
            ymap[m.lower()]=int(y)
        if not ymap: continue
        ti=ci=li=None
        for i,r in enumerate(head):
            a=r[0].strip().lower()
            if a.startswith('trade date'): ti=i
            elif a in ('date','calendar date'): ci=i
            if li is None and i>0 and any('close' in (x or '').lower() for x in r): li=i
        if ci is None: continue
        cal=ffill(head[ci]); lab=head[li] if li is not None else ['']*sh.ncols
        for r in range(sh.nrows):
            key=re.sub(r'\s+',' ',fmt(sh.cell(r,0),bk)).strip().lower()
            if key not in FAM: continue
            fam=FAM[key]
            for c in range(1,sh.ncols):
                v=fmt(sh.cell(r,c),bk)
                if not v: continue
                cd=cal[c] if c<len(cal) else ''
                m=re.search(r'(%s)\s*,?\s*(\d{1,2})'%'|'.join(MON), cd, re.I)
                if not m: continue
                mon=m.group(1).lower(); day=int(m.group(2))
                y=ymap.get(mon)
                if y is None: continue
                try: dt=datetime.date(y, MON.index(mon)+1, day).isoformat()
                except ValueError: continue
                recs.append(dict(file=os.path.basename(path), sheet=sh.name, fam=fam, orig=re.sub(r'\s+',' ',fmt(sh.cell(r,0),bk)).strip(),
                                 date=dt, label=(lab[c] if c<len(lab) else '').strip(), value=v, caldate=cd.strip()))
json.dump(recs, open('xls_records.json','w'), indent=0)
print('records', len(recs), 'dates', len(set(r['date'] for r in recs)))
