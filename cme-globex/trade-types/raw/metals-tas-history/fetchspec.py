import subprocess,os,gzip,re,html,time,sys
BASE={'gold':'http://www.cmegroup.com/trading/metals/precious/gold_contract_specifications.html',
 'silver':'http://www.cmegroup.com/trading/metals/precious/silver_contract_specifications.html',
 'copper':'http://www.cmegroup.com/trading/metals/base/copper_contract_specifications.html',
 'palladium':'http://www.cmegroup.com/trading/metals/precious/palladium_contract_specifications.html',
 'platinum':'http://www.cmegroup.com/trading/metals/precious/platinum_contract_specifications.html'}
def get(metal,ts):
    fn=f'wb-{metal}-spec-{ts}.html'
    for _ in range(4):
        if os.path.exists(fn) and os.path.getsize(fn)>5000: break
        subprocess.run(['curl','-s','-m','120','--compressed','-o',fn,f'https://web.archive.org/web/{ts}id_/{BASE[metal]}'],check=False)
        time.sleep(5)
    if not os.path.exists(fn) or os.path.getsize(fn)<5000: return None,fn
    b=open(fn,'rb').read()
    if b[:2]==b'\x1f\x8b': b=gzip.decompress(b)
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',b.decode('utf-8','replace')))),fn
def report(metal,ts):
    txt,fn=get(metal,ts)
    print(f'### {metal} {ts}')
    if txt is None: print('  FETCH FAIL'); return
    i=txt.find('Trading Hours')
    print('  HOURS:', txt[i:i+520].strip() if i>=0 else 'ABSENT')
    j=txt.find('Trade At Marker Or Trade At Settlement Rules')
    if j<0: j=txt.find('Trade At Settlement Rules')
    seg=txt[j:j+520] if j>=0 else 'ABSENT'
    print('  TASRULE:', seg.strip())
    print()
if __name__=='__main__':
    for a in sys.argv[1:]:
        m,t=a.split(':'); report(m,t)
