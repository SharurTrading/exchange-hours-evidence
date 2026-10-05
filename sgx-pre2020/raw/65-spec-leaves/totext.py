import re,html,sys
def totext(p):
    s=open(p,encoding='utf-8',errors='replace').read()
    t=re.sub(r'<script.*?</script>','',s,flags=re.S|re.I)
    t=re.sub(r'<style.*?</style>','',t,flags=re.S|re.I)
    t=re.sub(r'<[^>]+>','\n',t)
    t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t)
    lines=[l.strip() for l in t.split('\n')]
    return '\n'.join(l for l in lines if l)
if __name__=='__main__':
    for p in sys.argv[1:]:
        open(p+'.txt','w').write(totext(p))
        print('wrote',p+'.txt')
