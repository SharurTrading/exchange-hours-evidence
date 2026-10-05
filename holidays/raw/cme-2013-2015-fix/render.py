import xlrd, sys, re, os
FAM = {
 'cme group equity':'equity_index','equity products':'equity_index',
 'cme group interest rate':'interest_rates','interest rate products':'interest_rates',
 'cme group fx':'fx','fx products':'fx',
 'interest rate & fx products':'interest_rates+fx',
 'nymex, comex, and dme':'energy+metals','nymex, comex & dme':'energy+metals',
 'energy, metals & dme products':'energy+metals','energy, metals and dme products':'energy+metals',
 'grains and oilseeds':'grains_oilseeds','grains and oilseeds (cbot & kcbt)':'grains_oilseeds',
 'livestock':'livestock','lumber':'lumber','dairy':'dairy',
}
def fmt(c,bk):
    if c.ctype==0: return ''
    if c.ctype==1: return c.value.strip()
    if c.ctype==2:
        v=c.value; return str(int(v)) if v==int(v) else str(v)
    if c.ctype==3:
        try:
            t=xlrd.xldate_as_tuple(c.value,bk.datemode)
            return "%02d:%02d"%(t[3],t[4])
        except Exception: return str(c.value)
    if c.ctype==4: return 'TRUE' if c.value else 'FALSE'
    return str(c.value)
def ffill(v):
    out=[];last=''
    for x in v:
        if x.strip(): last=x.strip()
        out.append(last)
    return out
for path in sys.argv[1:]:
    bk=xlrd.open_workbook(path)
    print('#### FILE', os.path.basename(path))
    for sh in bk.sheets():
        # find header rows
        rows=[[fmt(sh.cell(r,c),bk) for c in range(sh.ncols)] for r in range(min(sh.nrows,12))]
        ti=ci=li=None
        for i,r in enumerate(rows):
            a=r[0].lower()
            if a.startswith('trade date'): ti=i
            elif a in ('date','calendar date'): ci=i
            if 'Close' in ' '.join(r) and li is None and i>0: li=i
        cal = ffill(rows[ci]) if ci is not None else ['']*sh.ncols
        trd = ffill(rows[ti]) if ti is not None else ['']*sh.ncols
        lab = rows[li] if li is not None else ['']*sh.ncols
        print('  == SHEET', repr(sh.name), '| title:', rows[0][0] or rows[0][1])
        for r in range(sh.nrows):
            name=fmt(sh.cell(r,0),bk)
            key=re.sub(r'\s+',' ',name).strip().lower()
            if key not in FAM: continue
            parts=[]
            for c in range(1,sh.ncols):
                v=fmt(sh.cell(r,c),bk)
                if not v: continue
                parts.append(f"[{cal[c] if c<len(cal) else ''} | {lab[c] if c<len(lab) else ''}] {v}")
            print(f"   {FAM[key]:<16} ({name.strip()!r}): " + ' ; '.join(parts))
