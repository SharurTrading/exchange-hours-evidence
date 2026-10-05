import sys, xlrd
def fmt(v):
    if isinstance(v,float):
        if 0.0 <= v <= 1.0:
            t = round(v*24*60)
            return "%02d:%02d" % (t//60 % 24, t%60)
        if v==int(v): return str(int(v))
        return str(v)
    return str(v).replace("\n"," ").strip()
b = xlrd.open_workbook(sys.argv[1])
only = sys.argv[2] if len(sys.argv)>2 else None
for sh in b.sheets():
    if only and only.lower() not in sh.name.lower(): continue
    print("=== SHEET: %s (%d rows x %d cols) ===" % (sh.name, sh.nrows, sh.ncols))
    for r in range(sh.nrows):
        cells=[]
        for c in range(sh.ncols):
            v=fmt(sh.cell_value(r,c))
            if v: cells.append("[%d]%s" % (c,v))
        if cells: print("r%-3d %s" % (r, "  ".join(cells)))
