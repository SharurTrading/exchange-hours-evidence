#!/bin/bash
# usage: fetch2.sh <outfile> <url> [reader]
OUT="$1"; URL="$2"; MODE="${3:-jina}"
D=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/U16-U17-taco/u16u17
mkdir -p "$D"
if [ "$MODE" = "direct" ]; then
  curl -sSL --max-time 90 -A "Mozilla/5.0" "$URL" -o "$D/$OUT"
else
  curl -sSL --max-time 120 "https://r.jina.ai/$URL" -o "$D/$OUT"
fi
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
SHA=$(shasum -a 256 "$D/$OUT" | awk '{print $1}')
BY=$(wc -c < "$D/$OUT" | tr -d ' ')
printf '%s\t%s\t%s\tsha256=%s\tbytes=%s\n' "$TS" "$OUT" "$URL" "$SHA" "$BY" >> "$D/INDEX.tsv"
echo "$OUT  bytes=$BY  sha=$SHA"
