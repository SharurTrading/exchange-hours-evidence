#!/usr/bin/env bash
# fetch.sh — retrieval helper for the iceus-2025-2027 evidence round.
# usage: ./fetch.sh <url> <outfile>   (globoff, 3 attempts, 120s each, browser UA)
set -u
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
url="$1"; out="$2"
for i in 1 2 3 4; do
  code=$(curl -g -sS -L --max-time 120 -A "$UA" -o "$out" -w '%{http_code}' "$url" 2>>fetch_err.txt) && {
    printf 'HTTP %s  bytes=%s  %s  -> %s\n' "$code" "$(wc -c <"$out" | tr -d ' ')" "$url" "$out"
    exit 0
  }
  printf 'attempt %s failed (rc=%s) %s\n' "$i" "$?" "$url" >>fetch_err.txt
  sleep 3
done
printf 'FAILED %s\n' "$url"
exit 1
