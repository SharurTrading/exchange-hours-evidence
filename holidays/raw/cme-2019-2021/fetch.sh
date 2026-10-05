#!/bin/zsh
# fetch.sh <archive-ts> <url> <outfile>
ts=$1; url=$2; out=$3
for i in 1 2 3 4 5 6 7 8; do
  code=$(curl -s -L -o "$out" -w "%{http_code}" --max-time 180 "https://web.archive.org/web/${ts}id_/${url}")
  if [ "$code" = "200" ] && [ -s "$out" ]; then echo "OK $out $(wc -c <"$out")"; exit 0; fi
  sleep 20
done
echo "FAIL $out ($code)"
