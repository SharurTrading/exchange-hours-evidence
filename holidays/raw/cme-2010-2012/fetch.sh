#!/bin/bash
BASE="https://web.archive.org"
fetch_one() {
  local url="$1"; local out="$2"
  # get CDX entries for exact url
  local enc=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1],safe=''))" "$url")
  local cdx=$(curl -s --max-time 90 "$BASE/cdx/search/cdx?url=$enc&output=json&fl=timestamp,statuscode,length&filter=statuscode:200&limit=10")
  local ts=$(echo "$cdx" | jq -r '.[1:][0][0] // empty')
  if [ -z "$ts" ]; then echo "NOSNAP $url"; return 1; fi
  curl -sL --max-time 120 "$BASE/web/${ts}id_/$url" -o "docs/$out"
  local sz=$(stat -f%z "docs/$out" 2>/dev/null || echo 0)
  echo -e "$out\t$url\t$ts\t$sz\t$(shasum -a 256 "docs/$out" | cut -d' ' -f1)"
}
