#!/bin/bash
D=/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/raw/btic-non-equity-groups
TS_ARC=$1; ID=$2; LAB=$3
OUT="wbspec-$ID-$LAB-$TS_ARC.json"
U="https://web.archive.org/web/${TS_ARC}id_/https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/$ID"
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
code=$(curl -sL --max-time 120 -o "$D/$OUT" -w "%{http_code}" "$U")
sz=$(wc -c <"$D/$OUT"|tr -d ' '); sha=$(shasum -a 256 "$D/$OUT"|cut -d' ' -f1)
echo "| $OUT | $U | $NOW | $code | $sz | $sha |" >> "$D/INDEX.md"
echo "$OUT http=$code bytes=$sz"
