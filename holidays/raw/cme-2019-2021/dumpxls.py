import sys, xlrd
b=xlrd.open_workbook(sys.argv[1])
def fmt(sh,r,c):
    t=sh.cell_type(r,c); v=sh.cell_value(r,c)
    if t==xlrd.XL_CELL_DATE:
        try:
            y,mo,d,h,mi,s=xlrd.xldate_as_tuple(v, b.datemode)
            if y==0 and mo==0 and d==0: return f"{h:02d}:{mi:02d}"
            return f"{y:04d}-{mo:02d}-{d:02d} {h:02d}:{mi:02d}"
        except Exception: return str(v)
    if t==xlrd.XL_CELL_NUMBER:
        if 0<=v<1:
            tot=round(v*24*60); return f"{tot//60:02d}:{tot%60:02d}"
        if v==int(v): return str(int(v))
        return str(v)
    return str(v).strip()
for sh in b.sheets():
    print("=== SHEET:", sh.name, sh.nrows, "x", sh.ncols)
    for r in range(sh.nrows):
        vals=[fmt(sh,r,c) for c in range(sh.ncols)]
        line=" | ".join(vals)
        while line.endswith(" | ") or line.endswith("|"): line=line[:-1].rstrip()
        if line.strip(): print(f"[{r}] {line}")
