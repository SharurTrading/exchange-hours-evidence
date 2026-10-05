#!/bin/zsh
# $1 = url, $2 = outfile
url="$1"; out="$2"
curl -s --max-time 120 "https://r.jina.ai/$url" -o "$out"
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ)  $out  $url  $(shasum -a 256 "$out" | cut -d' ' -f1)  $(wc -c < "$out")"
