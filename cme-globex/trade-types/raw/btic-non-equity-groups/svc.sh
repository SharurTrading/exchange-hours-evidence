#!/bin/bash
D=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/btic-non-equity-groups
# svc.sh <id> <label> <tag> <from> <to>
ID=$1; LAB=$2; TAG=$3; FROM=$4; TO=$5
OUT="svc-$ID-$LAB-$TAG.json"
URL="https://www.cmegroup.com/services/trading-hours-by-product?id=$ID&pageSize=100&fromEventDate=$FROM&toEventDate=$TO"
for try in 1 2 3; do
  TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  code=$(curl -s --max-time 120 -o "$D/$OUT" -w "%{http_code}" "https://r.jina.ai/$URL")
  if [ "$code" = "200" ]; then break; fi
done
sz=$(wc -c < "$D/$OUT" | tr -d ' '); sha=$(shasum -a 256 "$D/$OUT" | cut -d' ' -f1)
echo "| $OUT | $URL | $TS | $code | $sz | $sha |" >> "$D/INDEX.md"
echo "$OUT http=$code bytes=$sz"
