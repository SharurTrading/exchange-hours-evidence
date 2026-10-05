# Dumps every sheet of every xls/*.xls to txt/<name>.txt, cell by cell. xlrd 2.0.2.
import xlrd, os, glob
def fmt(c, bk):
    if c.ctype==0: return ''
    if c.ctype==1: return c.value
    if c.ctype==2:
        v=c.value; return str(int(v)) if v==int(v) else str(v)
    if c.ctype==3:
        try:
            t=xlrd.xldate_as_tuple(c.value, bk.datemode)
            return "%04d-%02d-%02d %02d:%02d:%02d"%t
        except Exception: return str(c.value)
    if c.ctype==4: return 'TRUE' if c.value else 'FALSE'
    if c.ctype==5: return 'ERR%s'%c.value
    return str(c.value)
os.makedirs('txt', exist_ok=True)
for f in sorted(glob.glob('xls/*.xls')):
    bk=xlrd.open_workbook(f, formatting_info=False)
    with open(os.path.join('txt', os.path.basename(f)[:-4]+'.txt'),'w') as o:
        o.write('FILE: %s\nSHEETS: %s\n'%(os.path.basename(f), bk.sheet_names()))
        for sh in bk.sheets():
            o.write('\n===== SHEET %r rows=%d cols=%d =====\n'%(sh.name, sh.nrows, sh.ncols))
            for r in range(sh.nrows):
                vals=[fmt(sh.cell(r,c),bk) for c in range(sh.ncols)]
                while vals and vals[-1]=='': vals.pop()
                if vals: o.write('r%03d | '%r + ' | '.join(vals) + '\n')
