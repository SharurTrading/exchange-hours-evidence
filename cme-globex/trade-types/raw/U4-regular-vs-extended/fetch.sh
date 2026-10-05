#!/bin/bash
# $1 = url, $2 = outfile
url="$1"; out="$2"
for i in 1 2 3 4 5 6 7 8; do
  code=$(curl -sS --max-time 180 -o "$out" -w "%{http_code}" "https://r.jina.ai/$url")
  if [ "$code" = "200" ] && ! grep -q "RateLimitTriggeredError" "$out" 2>/dev/null; then
    echo "OK $code $(wc -c < "$out") $url -> $out"; return 0 2>/dev/null || exit 0
  fi
  python3 -c "import time;time.sleep(8)"
done
echo "FAIL $code $url"
