#!/bin/bash
# re-verification pass 2026-09-12
IDX=INDEX-20260912.md
fetch() {  # fetch <outfile> <url>
  local out="$1"; shift; local url="$1"
  local ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  local code=$(curl -sS -L -o "$out" -w "%{http_code}" --max-time 120 "$url")
  local sz=$(wc -c < "$out" | tr -d ' ')
  local sha=$(shasum -a 256 "$out" | cut -d' ' -f1)
  echo "| \`$out\` | $url | $ts | $code | $sz | \`$sha\` |" >> "$IDX"
  echo "$out $code $sz"
}
