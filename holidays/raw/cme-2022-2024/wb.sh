#!/bin/bash
# wb.sh <outfile> <timestamp> <url>
D=/Users/agedvagabond/Developer/exchange-hours-research/holidays/raw/cme-2022-2024
out="$D/$1"; ts="$2"; url="$3"
[ -s "$out" ] && { echo "SKIP $1"; exit 0; }
for i in 1 2 3 4 5 6; do
  code=$(curl -sSL --max-time 180 -w "%{http_code}" "https://web.archive.org/web/${ts}id_/${url}" -o "$out" 2>/dev/null)
  if [ "$code" = "200" ] && [ -s "$out" ]; then
    echo "OK $1 ts=$ts sha256=$(shasum -a 256 "$out"|cut -d' ' -f1) bytes=$(stat -f%z "$out")"; exit 0
  fi
  sleep 12
done
rm -f "$out"; echo "FAIL $1 ts=$ts $url"
