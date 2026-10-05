#!/bin/bash
# usage: fetch.sh <outname> <url>
D=/Users/agedvagabond/Developer/exchange-hours-research/holidays/raw/cme-2022-2024
out="$D/$1"; url="$2"
if [ -s "$out" ]; then echo "SKIP-exists $1"; exit 0; fi
# find best timestamp
for i in 1 2 3 4; do
  cdx=$(curl -sS --max-time 120 "https://web.archive.org/cdx/search/cdx?url=${url#https://}&output=json&fl=timestamp,statuscode&limit=20" 2>/dev/null)
  case "$cdx" in "<html"*|"") sleep 10;; *) break;; esac
done
ts=$(echo "$cdx" | jq -r '.[1:][] | select(.[1]=="200") | .[0]' 2>/dev/null | head -1)
if [ -z "$ts" ]; then echo "NOARCHIVE $1 $url"; exit 1; fi
for i in 1 2 3 4; do
  code=$(curl -sSL --max-time 180 -w "%{http_code}" "https://web.archive.org/web/${ts}id_/${url}" -o "$out" 2>/dev/null)
  if [ "$code" = "200" ] && [ -s "$out" ]; then break; fi
  sleep 10
done
if [ -s "$out" ]; then
  echo "OK $1 ts=$ts sha256=$(shasum -a 256 "$out" | cut -d' ' -f1) bytes=$(stat -f%z "$out") url=$url"
else
  echo "FAIL $1 ts=$ts $url"; rm -f "$out"
fi
