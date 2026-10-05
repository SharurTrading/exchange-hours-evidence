import json, re, sys
from html.parser import HTMLParser

class R(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out=[]; self.buf=[]; self.stack=[]
        self.cells=[]; self.row=[]; self.intable=0
    def flush_para(self, tag=None):
        t=' '.join(''.join(self.buf).split())
        self.buf=[]
        return t
    def handle_starttag(self, tag, attrs):
        if tag in ('p','h1','h2','h3','h4','h5','h6','li','br','td','th','tr','table'):
            t=self.flush_para()
            if t:
                if self.intable and self.row is not None:
                    self.row.append(t)
                else:
                    self.out.append(t)
        if tag=='table':
            self.intable+=1; self.out.append('<<TABLE START>>')
        if tag=='tr': self.row=[]
        self.stack.append(tag)
    def handle_endtag(self, tag):
        t=self.flush_para()
        if tag in ('td','th'):
            if t: self.row.append(t)
            if not t: self.row.append('')
        elif tag=='tr':
            if t: self.row.append(t)
            self.out.append('ROW: ' + ' | '.join(self.row)); self.row=[]
        elif tag=='table':
            if t: self.out.append(t)
            self.intable-=1; self.out.append('<<TABLE END>>')
        elif tag in ('h1','h2','h3','h4','h5','h6'):
            if t: self.out.append('### ' + t)
        else:
            if t:
                if self.intable: self.row.append(t)
                else: self.out.append(t)
        if self.stack and tag in self.stack:
            # pop to tag
            while self.stack:
                x=self.stack.pop()
                if x==tag: break
    def handle_data(self, data):
        self.buf.append(data)

src=sys.argv[1]; dst=sys.argv[2]
d=json.load(open(src))
try:
    body=d['body']['storage']['value']
except KeyError:
    body=d['body']['storage']['value']
p=R(); p.feed(body)
t=p.flush_para()
if t: p.out.append(t)
open(dst,'w').write('\n'.join(x for x in p.out if x.strip()))
