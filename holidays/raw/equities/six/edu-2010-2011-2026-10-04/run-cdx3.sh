#!/bin/zsh
q() {
  local out="$1"; shift
  echo "== $(date -u +%FT%TZ) $out" >> cdx-sweep.log
  curl -sS --max-time 240 "https://web.archive.org/cdx/search/cdx?$*" -o "$out" 2>>cdx-sweep.log
  echo "   -> $(date -u +%FT%TZ) $(wc -c < "$out" | tr -d ' ') bytes" >> cdx-sweep.log
  sleep 2
}
q cdx-uncollapsed-tg-20100111.txt "url=six-swiss-exchange.com/download/participants/regulation/archive/trading_guides/trading_guide_2010_01_11_en.pdf"
q cdx-uncollapsed-archive-tg-all.txt "url=six-swiss-exchange.com/download/participants/regulation/archive/trading_guides*&limit=3000"
q cdx-uncollapsed-tc-en.txt "url=six-swiss-exchange.com/download/participants/regulation/trading_guides/trading_calendar_en.pdf&limit=1000"
q cdx-sixgroup-exchanges-archive.txt "url=six-group.com/exchanges/download/participants/regulation/archive*&limit=2000"
q cdx-swissguide-2010-variants.txt "url=six-swiss-exchange.com/download/participants/regulation/archive/trading_guides/trading_guide_2010_01_11_en.pdf&matchType=exact"
