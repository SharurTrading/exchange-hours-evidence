#!/bin/bash
D=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/btic-non-equity-groups
TS_ARC=$1; OUT=$2; PATHPART=$3
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
code=0
for sch in https http; do
  U="https://web.archive.org/web/${TS_ARC}id_/${sch}://www.cmegroup.com${PATHPART}"
  code=$(curl -sL --max-time 120 -o "$D/$OUT" -w "%{http_code}" "$U")
  if [ "$code" = "200" ] && [ -s "$D/$OUT" ]; then break; fi
done
if [ -f "$D/$OUT" ]; then sz=$(wc -c <"$D/$OUT"|tr -d ' '); sha=$(shasum -a 256 "$D/$OUT"|cut -d' ' -f1); else sz=0; sha=-; fi
echo "| $OUT | $U | $NOW | $code | $sz | $sha |" >> "$D/INDEX.md"
echo -n "$OUT http=$code bytes=$sz :: "
python3 - "$D/$OUT" <<'PY'
import sys,re,html,gzip
p=sys.argv[1]
try: b=open(p,'rb').read()
except: print('MISSING'); raise SystemExit
if b[:2]==b'\x1f\x8b':
    try: b=gzip.decompress(b)
    except: pass
t=b.decode('utf-8',errors='replace')
i=t.lower().find('trading hours')
if i<0: print('NO TRADING HOURS'); raise SystemExit
s=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',t[i:i+1100])))
print(s[:1000])
PY
