#!/bin/bash
set -u
BASE="https://web.archive.org/web"
dl(){ ts="$1"; url="$2"; out="pdf/$3"
  if [ -s "$out" ] && head -c4 "$out" | grep -q PDF; then echo "SKIP $out"; return 0; fi
  for i in 1 2 3 4 5 6 7 8; do
    code=$(curl -sL --max-time 90 -w "%{http_code}" -o "$out" "$BASE/${ts}id_/$url" 2>/dev/null)
    sz=$(stat -f%z "$out" 2>/dev/null || echo 0)
    if [ "$code" = "200" ] && [ "$sz" -gt 1000 ]; then echo "OK $sz $out"; sleep 1; return 0; fi
    sleep 4
  done
  echo "FAIL($code/$sz) $out"
}
