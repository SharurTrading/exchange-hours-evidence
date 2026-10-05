#!/bin/zsh
# usage: fetch.sh <outfile> <url>
out="$1"; url="$2"
for i in 1 2 3 4 5 6; do
  code=$(curl -s -o "$out" -w "%{http_code}" --max-time 150 "https://r.jina.ai/$url")
  sz=$(wc -c < "$out")
  echo "[$i] $code $sz  $url"
  if [ "$code" = "200" ]; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ)  $out  $url  sha256=$(shasum -a 256 "$out" | cut -d' ' -f1)  bytes=$sz" >> CAPTURES.log
    break
  fi
  python3 -c "import time;time.sleep(20)"
done
