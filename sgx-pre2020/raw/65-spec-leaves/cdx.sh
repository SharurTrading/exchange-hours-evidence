#!/bin/zsh
# cdx.sh <cdx-query-url-suffix> <outfile>  -- retry with backoff
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
q="$1"; out="$2"
for i in 1 2 3 4 5 6 7 8; do
  code=$(curl -sS -g -L -A "$UA" --max-time 240 -o "$out.tmp" -w "%{http_code}" "$q" 2>/dev/null) || code="ERR"
  sz=$(wc -c < "$out.tmp" 2>/dev/null || echo 0)
  if [ "$code" = "200" ]; then mv "$out.tmp" "$out"; echo "OK $code $sz $out"; exit 0; fi
  echo "  retry $i: http=$code size=$sz"
  sleep $((3 + i*2))
done
echo "FAIL $q"; rm -f "$out.tmp"; exit 1
