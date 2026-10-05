#!/bin/zsh
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$PATH
RAW=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/standalone-products-gates
OUT="$RAW/$1"; TS=$2; URL=$3
CAP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
CODE=$(curl -sL --max-time 120 -A 'Mozilla/5.0' -o "$OUT" -w "%{http_code}" "https://web.archive.org/web/${TS}id_/${URL}")
echo "$1|https://web.archive.org/web/${TS}id_/${URL}|$CAP|$CODE|$(wc -c <"$OUT"|tr -d ' ')|$(shasum -a 256 "$OUT"|awk '{print $1}')" >> "$RAW/index.psv"
echo "code=$CODE size=$(wc -c <"$OUT"|tr -d ' ') file=$1"
python3 -c "import time;time.sleep(2)"
