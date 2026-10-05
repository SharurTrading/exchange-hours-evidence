#!/bin/bash
while IFS=$'\t' read -r name ts url; do
  [ -z "$name" ] && continue
  f="docs/$name"
  if [ -s "$f" ] && [ "$(stat -f%z "$f")" -gt 2000 ]; then echo "HAVE $name $(stat -f%z "$f")"; continue; fi
  for a in 1 2 3 4 5; do
    curl -sL --max-time 150 -A "Mozilla/5.0" "https://web.archive.org/web/${ts}id_/${url}" -o "$f"
    sz=$(stat -f%z "$f" 2>/dev/null || echo 0)
    if [ "$sz" -gt 2000 ]; then break; fi
    sleep 6
  done
  echo -e "$name\t$ts\t$(stat -f%z "$f" 2>/dev/null || echo 0)\t$(shasum -a 256 "$f" 2>/dev/null | cut -d' ' -f1)"
  sleep 2
done < list.tsv
