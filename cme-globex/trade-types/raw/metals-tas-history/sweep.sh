#!/bin/zsh
while IFS=$'\t' read d ts url; do
  [ -s "notices1718/$d.html" ] && continue
  curl -s --max-time 45 -A 'Mozilla/5.0' "https://web.archive.org/web/${ts}id_/$url" -o "notices1718/$d.html"
done
