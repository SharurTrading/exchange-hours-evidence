#!/bin/zsh
# fetch.sh <url> <outfile>  -- retry with backoff
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
url="$1"; out="$2"
for i in 1 2 3 4 5 6 7 8; do
  code=$(curl -sS -g -L -A "$UA" --max-time 180 -o "$out.tmp" -w "%{http_code}" "$url" 2>/dev/null) || code="ERR"
  sz=$(wc -c < "$out.tmp" 2>/dev/null || echo 0)
  if [ "$code" = "200" ] && [ "$sz" -gt 0 ]; then mv "$out.tmp" "$out"; echo "OK $code $sz $out"; exit 0; fi
  echo "  retry $i: http=$code size=$sz"
  sleep $((3 + i))
done
echo "FAIL $url"; rm -f "$out.tmp"; exit 1
