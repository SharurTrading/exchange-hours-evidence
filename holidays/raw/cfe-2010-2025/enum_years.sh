#!/bin/bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for y in $(seq 2010 2027); do
  out="listing/su_$y.html"
  [ -s "$out" ] && continue
  "$CHROME" --headless=new --disable-gpu --no-sandbox --virtual-time-budget=20000 --dump-dom \
    "https://www.cboe.com/markets/us/futures/notices/schedule-update/$y" > "$out" 2>/dev/null
  echo "$y $(wc -c < "$out")b"
done
