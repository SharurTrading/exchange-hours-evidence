#!/bin/zsh
# CDX sweeps for the edu-2010-2011 hunt. Each line: outfile|params
q() {
  local out="$1"; shift
  echo "== $(date -u +%FT%TZ) $out" >> cdx-sweep.log
  curl -sS --max-time 240 "https://web.archive.org/cdx/search/cdx?$*" -o "$out" 2>>cdx-sweep.log
  echo "   -> $(date -u +%FT%TZ) $(wc -c < "$out" | tr -d ' ') bytes" >> cdx-sweep.log
  sleep 2
}
# Angle 1: education/training/documentation trees of the era
q cdx-edu-sixswiss-educ.json       "url=six-swiss-exchange.com&matchType=domain&filter=original:.*educat.*&from=2008&to=2013&collapse=urlkey"
q cdx-edu-sixswiss-training.json   "url=six-swiss-exchange.com&matchType=domain&filter=original:.*training.*&from=2008&to=2013&collapse=urlkey"
q cdx-edu-sixswiss-ausbildung.json "url=six-swiss-exchange.com&matchType=domain&filter=original:.*ausbildung.*&from=2008&to=2013&collapse=urlkey"
q cdx-edu-sixswiss-dokumentation.json "url=six-swiss-exchange.com&matchType=domain&filter=original:.*dokument.*&from=2008&to=2013&collapse=urlkey"
q cdx-edu-swiss-training-prefix.json "url=six-swiss-exchange.com/download/trading/training/*&collapse=urlkey"
q cdx-edu-sixgroup-educ.json       "url=six-group.com&matchType=domain&filter=original:.*educat.*&from=2008&to=2013&collapse=urlkey"
q cdx-edu-sixgroup-training.json   "url=six-group.com&matchType=domain&filter=original:.*training.*&from=2008&to=2013&collapse=urlkey"
q cdx-edu-swx-educ.json            "url=swx.com&matchType=domain&filter=original:.*(educat|training|ausbildung).*&from=2006&to=2013&collapse=urlkey"
