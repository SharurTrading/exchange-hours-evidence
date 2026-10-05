import subprocess,os,gzip,re,html,time,sys
BASE={'gold':'http://www.cmegroup.com/trading/metals/precious/gold_contract_specifications.html',
 'silver':'http://www.cmegroup.com/trading/metals/precious/silver_contract_specifications.html',
 'copper':'http://www.cmegroup.com/trading/metals/base/copper_contract_specifications.html',
 'palladium':'http://www.cmegroup.com/trading/metals/precious/palladium_contract_specifications.html',
 'platinum':'http://www.cmegroup.com/trading/metals/precious/platinum_contract_specifications.html'}
def txt_of(metal,ts):
    fn=f'wb-{metal}-spec-{ts}.html'
    for _ in range(4):
        if os.path.exists(fn) and os.path.getsize(fn)>5000: break
        subprocess.run(['curl','-s','-m','120','--compressed','-o',fn,f'https://web.archive.org/web/{ts}id_/{BASE[metal]}'],check=False)
        time.sleep(4)
    if not os.path.exists(fn) or os.path.getsize(fn)<5000: return None
    b=open(fn,'rb').read()
    if b[:2]==b'\x1f\x8b': b=gzip.decompress(b)
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',b.decode('utf-8','replace'))))
for a in sys.argv[1:]:
    m,ts=a.split(':')
    t=txt_of(m,ts)
    if t is None: print(m,ts,'FAIL'); continue
    i=t.find('Trading Hours')
    hours=t[i:i+400] if i>=0 else 'ABSENT'
    tas='TAS:' in hours
    ceases='ceases daily' in t
    cm=re.search(r'ceases daily at [^.]*\.',t)
    print(f'{m} {ts} TASinHours={tas} ceases={ceases} {cm.group(0) if cm else ""}')
    if tas:
        j=hours.find('TAS:'); print('    ', hours[j:j+160])
