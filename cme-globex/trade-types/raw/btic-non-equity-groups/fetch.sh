#!/bin/bash
# usage: fetch.sh <outfile> <url>
D=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/btic-non-equity-groups
OUT="$1"; URL="$2"
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
code=$(curl -s --max-time 120 -o "$D/$OUT" -w "%{http_code}" "https://r.jina.ai/$URL")
sz=$(wc -c < "$D/$OUT" | tr -d ' ')
sha=$(shasum -a 256 "$D/$OUT" | cut -d' ' -f1)
echo "| $OUT | $URL | $TS | $code | $sz | $sha |" >> "$D/INDEX.md"
echo "$OUT http=$code bytes=$sz"
