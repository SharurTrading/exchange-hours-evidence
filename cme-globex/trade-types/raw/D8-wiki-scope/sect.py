import re,sys,html as H
v=sys.argv[1]
s=open(f'storage-v{v}.html').read()
hs=[(m.start(),m.group(1),' '.join(re.sub(r'<[^>]+>','',m.group(2)).split())) for m in re.finditer(r'<h([1-6])[^>]*>(.*?)</h\1>',s,re.S)]
want=sys.argv[2]
for i,(pos,lvl,txt) in enumerate(hs):
    if want in txt:
        end = hs[i+1][0] if i+1<len(hs) else len(s)
        t=re.sub(r'<[^>]+>',' ',s[pos:end]); t=H.unescape(t); t=re.sub(r'\s+',' ',t).strip()
        print(t)
        break
