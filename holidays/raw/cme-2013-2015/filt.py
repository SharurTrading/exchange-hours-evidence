import sys,re
skip=False
for line in open(sys.argv[1],encoding='utf-8',errors='replace'):
    s=line.rstrip()
    if re.search(r'Korea Exchange|KOSPI|Bursa Malaysia|BMD\)', s): skip=True
    if re.search(r'Holiday Schedule\s*$', s) and 'Globex' in s: skip=False
    if re.match(r'^\s*(CME|CBOT|NYMEX|Other|CME Group|Globex)', s) and 'Bursa' not in s and 'Korea' not in s: skip=False
    if skip: continue
    if re.search(r'subject to change|call the CME|44\.207|Session orders entered', s): continue
    if not s.strip(): continue
    print(s)
