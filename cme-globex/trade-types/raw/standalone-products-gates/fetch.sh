#!/bin/zsh
# usage: fetch.sh <outfile> <url>
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:/Library/Frameworks/Python.framework/Versions/3.14/bin:$PATH
RAW=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/standalone-products-gates
OUT="$RAW/$1"; URL="$2"
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
python3 -c "import time;time.sleep(8)"
CODE=$(curl -sL --max-time 120 -o "$OUT" -w "%{http_code}" "$URL")
SZ=$(wc -c < "$OUT" | tr -d ' ')
SHA=$(shasum -a 256 "$OUT" | awk '{print $1}')
echo "$1|$URL|$TS|$CODE|$SZ|$SHA" >> "$RAW/index.psv"
echo "code=$CODE size=$SZ sha=$SHA ts=$TS file=$1"
