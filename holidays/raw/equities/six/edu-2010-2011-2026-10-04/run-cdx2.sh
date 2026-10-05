#!/bin/zsh
q() {
  local out="$1"; shift
  echo "== $(date -u +%FT%TZ) $out" >> cdx-sweep.log
  curl -sS --max-time 240 "https://web.archive.org/cdx/search/cdx?$*" -o "$out" 2>>cdx-sweep.log
  echo "   -> $(date -u +%FT%TZ) $(wc -c < "$out" | tr -d ' ') bytes" >> cdx-sweep.log
  sleep 2
}
q cdx-sixswiss-kalender.txt    "url=six-swiss-exchange.com&matchType=domain&filter=original:.*kalender.*&collapse=urlkey"
q cdx-sixswiss-calendrier.txt  "url=six-swiss-exchange.com&matchType=domain&filter=original:.*calendrier.*&collapse=urlkey"
q cdx-sixswiss-feiertag.txt    "url=six-swiss-exchange.com&matchType=domain&filter=original:.*feiertag.*&collapse=urlkey"
q cdx-sixswiss-holiday.txt     "url=six-swiss-exchange.com&matchType=domain&filter=original:.*holiday.*&collapse=urlkey"
q cdx-sixswiss-publication.txt "url=six-swiss-exchange.com&matchType=domain&filter=original:.*publication.*&from=2009&to=2013&collapse=urlkey"
q cdx-sixswiss-regulation-html.txt "url=six-swiss-exchange.com/participants/regulation*&filter=mimetype:text/html&from=2009&to=2013&collapse=urlkey"
q cdx-swx-calendar.txt         "url=swx.com&matchType=domain&filter=original:.*(calendar|kalender|holiday|feiertag).*&from=2007&to=2013&collapse=urlkey"
q cdx-sixgroup-kalender.txt    "url=six-group.com&matchType=domain&filter=original:.*(kalender|calendrier).*&collapse=urlkey"
q cdx-sixgroup-hyphen-guides.txt "url=six-group.com&matchType=domain&filter=original:.*trading-guide.*&collapse=urlkey"
q cdx-sixgroup-notices.txt     "url=six-group.com&matchType=domain&filter=original:.*(official_notice|circular).*&from=2009&to=2013&collapse=urlkey"
q cdx-sixswiss-notices.txt     "url=six-swiss-exchange.com&matchType=domain&filter=original:.*(official_notice|notices).*&from=2009&to=2013&collapse=urlkey"
