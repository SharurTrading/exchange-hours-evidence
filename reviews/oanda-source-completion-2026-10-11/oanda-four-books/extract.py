from html.parser import HTMLParser
import pathlib,json,re
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
  if self.skip:return
  if t in ['div','p','li','tr','h1','h2','h3','h4','h5','br']:self.out.append('\n')
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
  if self.skip:return
  if t in ['div','p','li','tr','h1','h2','h3','h4','h5']:self.out.append('\n')
 def handle_data(self,d):
  if not self.skip:self.out.append(d)
r=pathlib.Path('/tmp/oanda-four-book-report/evidence')
for path in r.glob('*.html'):
 p=Text();p.feed(path.read_text());text='\n'.join(x.strip() for x in ''.join(p.out).splitlines() if x.strip());path.with_suffix('.txt').write_text(text)
