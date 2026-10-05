import sys, xlrd
WANT=['Equity Products','Nikkei','Cryptocurrency','Interest Rate Products','FX Products','Energy','Grain','Livestock','Dairy','Lumber','Softs']
def fmt(v):
    if isinstance(v,float):
        if 0.0<=v<=1.0:
            t=round(v*24*60); return "%02d:%02d"%(t//60%24,t%60)
        if v==int(v): return str(int(v))
        return str(v)
    return str(v).replace("\n"," ").strip()
for fn in sys.argv[1:]:
    b=xlrd.open_workbook(fn); sh=b.sheets()[0]
    g=lambda r,c: fmt(sh.cell_value(r,c))
    # locate rows
    hdr=None; caldates=None
    for r in range(min(12,sh.nrows)):
        if g(r,0).startswith('Calendar Date') and caldates is None: caldates=r
        if 'Products on CME Group Globex' in g(r,0): hdr=r
    print("#### FILE %s | sheet '%s' | title: %s | %s" % (fn, sh.name, g(0,1) or g(1,1), g(0,0)))
    print("#### zone-note: %s" % g(hdr,0)[-90:] if hdr is not None else "")
    # build col->(caldate, header)
    cal={}
    cur=""
    for c in range(sh.ncols):
        v=g(caldates,c) if caldates is not None else ""
        if v and c>0: cur=v
        cal[c]=cur
    for r in range(sh.nrows):
        name=g(r,0)
        if not name: continue
        if any(name.startswith(w) for w in WANT):
            cells=[]
            for c in range(1,sh.ncols):
                v=g(r,c)
                if v: cells.append("%s / %s = %s" % (cal.get(c,''), g(hdr,c) if hdr is not None else '?', v))
            print("ROW[%s]: %s" % (name, " ;; ".join(cells)))
    print()
