#!/bin/bash
D=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/btic-non-equity-groups
TS_ARC=$1; OUT=$2; ORIG=$3
U="https://web.archive.org/web/${TS_ARC}id_/${ORIG}"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
code=$(curl -sL --max-time 120 -o "$D/$OUT" -w "%{http_code}" "$U")
if [ -f "$D/$OUT" ]; then sz=$(wc -c <"$D/$OUT"|tr -d ' '); sha=$(shasum -a 256 "$D/$OUT"|cut -d' ' -f1); else sz=0; sha=-; fi
echo "| $OUT | $U | $NOW | $code | $sz | $sha |" >> "$D/INDEX.md"
echo "$OUT http=$code bytes=$sz"
