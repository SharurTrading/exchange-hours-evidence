import sys, xlrd
b = xlrd.open_workbook(sys.argv[1], formatting_info=False)
for sh in b.sheets():
    print("=== SHEET: %s (%d x %d) ===" % (sh.name, sh.nrows, sh.ncols))
    for r in range(sh.nrows):
        vals=[]
        for c in range(sh.ncols):
            v = sh.cell_value(r,c)
            if isinstance(v,float) and v==int(v): v=int(v)
            vals.append(str(v).replace("\n"," | ").strip())
        line=" \t| ".join(vals).rstrip(" \t|")
        if line.strip(): print("%3d: %s" % (r,line))
