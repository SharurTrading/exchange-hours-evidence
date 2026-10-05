#!/bin/zsh
# r2fetch.sh <outfile> <url>   -- fetch through the public text reader, record bytes + sha
RAW=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/btic-non-equity-groups
out="$RAW/$1"; url="$2"
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
code=$(curl -s -o "$out" -w '%{http_code}' --max-time 180 "https://r.jina.ai/$url")
b=$(wc -c < "$out" | tr -d ' ')
s=$(shasum -a 256 "$out" | awk '{print $1}')
printf '| %s | %s | %s | %s | %s | %s |\n' "$1" "$url" "$ts" "$code" "$b" "$s" >> "$RAW/INDEX.md"
echo "$1 http=$code bytes=$b ts=$ts"
