import re, sys, html as H
src=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
s=open(src).read()[a:b]
# mark block boundaries
s=re.sub(r'<h([1-6])[^>]*>', r'\n@@H\1 ', s)
s=re.sub(r'</h[1-6]>', r'\n', s)
s=re.sub(r'<table[^>]*>', r'\n@@TABLE\n', s)
s=re.sub(r'</table>', r'\n@@ENDTABLE\n', s)
s=re.sub(r'<tr[^>]*>', r'\n@@ROW ', s)
s=re.sub(r'<t[hd][^>]*>', r' ||| ', s)
s=re.sub(r'<p[^>]*>', r'\n', s)
s=re.sub(r'<li[^>]*>', r'\n  - ', s)
s=re.sub(r'<br\s*/?>', r' / ', s)
s=re.sub(r'<[^>]+>', '', s)
s=H.unescape(s)
s=s.replace(' ',' ')
out=[]
for line in s.split('\n'):
    line=' '.join(line.split())
    if line: out.append(line)
print('\n'.join(out))
