#!/bin/bash
# notsearch.sh <out> <page> <from> <to>
D=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/btic-non-equity-groups
OUT="$1"; P="$2"; F="$3"; T="$4"
URL="https://www.cmegroup.com/content/cmegroup/en/notices/jcr:content/main-content-section/section/section-elements/search_sort_filter_d.ssfajax.$P.0.$F.$T.json"
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
code=$(curl -s --max-time 150 -o "$D/$OUT" -w "%{http_code}" "https://r.jina.ai/$URL")
sz=$(wc -c < "$D/$OUT" | tr -d ' '); sha=$(shasum -a 256 "$D/$OUT" | cut -d' ' -f1)
echo "| $OUT | $URL | $TS | $code | $sz | $sha |" >> "$D/INDEX.md"
echo "$OUT http=$code bytes=$sz"
