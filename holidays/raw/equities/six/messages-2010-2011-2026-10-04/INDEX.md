# Evidence index — `equities/six/messages-2010-2011-2026-10-04`

The official-messages channel of #212's 2010-2011 hunt, REOPENED and EXAMINED
2026-10-04 UTC (LAW-UTC-DATES) after the #272 review found that the earlier
same-day pass's point 6 ("the individual message PDFs were themselves never
captured ... the dated `swx_message_*.pdf` rows are 302/301s", in the
`edu-2010-2011-2026-10-04/INDEX.md`) misread its own census. The census
(`cdx-swx-messages-prefix.txt`, 844 rows) holds **680 rows at status 200 with
mimetype `application/pdf`**, and 96 of the 156 title-linked message PDFs are
among them — **26 of the 85 title-linked 2010 messages and 70 of the 71
title-linked 2011 messages**.

## What was fetched and read

For each title-linked PDF with a 200 capture: the bytes fetched once from the
Wayback `id_` replay, text extracted with `pdftotext -layout`, sha256 recorded
in `SHA256SUMS.txt`, and **every one of the 96 sha1(base32) digests of the
fetched bytes re-computed equal to the CDX census digest** (capture integrity).
All 96 are the `_en` editions. Retrieval pass 2026-10-04, completed 2026-10-04T01:46:19Z
(per-file instants in `fetch.log`); each PDF fetched exactly once (two files
needed a retry after transient `web.archive.org` connection refusals, recorded
in `fetch.log`).

**VERDICT: NEGATIVE for row data.** No message announces a holiday, a closure,
a special session, or any trading-calendar content with dates. The full text of
all 96 extractions was scanned for holiday/trading-calendar vocabulary
(holiday, Feiertag, Ferien, trading calendar, Handelskalender, market closed,
no trading, keine Handel, Christmas, Weihnacht, New Year, Neujahr, Easter,
Ostern, Ascension, Auffahrt, Whit, Pfingst, National Day, Bundesfeier, 24/25/26
December, 31 December, 1/2/6 January, Good Friday, Easter Monday, Whit Monday)
and for closure/session language (closed, closure, geschlossen, suspension of
trading, not be a trading day, trading hours, Handelszeiten). The only hits are
false positives and these, recorded for completeness:

- **33/2011 (30.06.2011), "Launch of SLS"** — a **pointer**, not a calendar:
  "Trading in SLS will be possible on SIX Swiss Exchange trading days according
  to the SIX Swiss Exchange Trading Calendar whereby trading hours are as
  follows: securities from Swiss market from 09.00 to 17.20 CET". It names the
  separate Trading Calendar without printing any holiday date (corroborates the
  09:00-17:20 shares normal-week bound; keys no row).
- **50/2011 (31.08.2011), "Extension of Fee Holiday for SLS"** — a fee
  instrument ("extending the fee holiday for SLS transactions until
  30.9.2011"), not a market holiday.
- All remaining extractions: member commencements/name changes, index
  adjustments, bond price-step and stop-trading-range changes, directive/fee
  changes, SWXess maintenance releases, the MF Global suspension — the
  membership/rules shape the title list showed; no holiday content in any body
  text.

The negative now stands on the full bytes of 96 of the 156 title-linked
messages (the other 60 have no Wayback capture and remain unread) and does not
change the closing condition in `edu-2010-2011-2026-10-04/INDEX.md`: the
2010-2011 half of #212 still closes exactly when the operator's Trading
Calendar bytes for those years surface (the stable `trading_calendar_en.pdf` as
served 2010-2011, or the 11 January 2010 Trading Guide edition). A message
announcing holiday trading hours with dates would also key rows (it is the
operator's own session language on an unconditional day); none exists among
these 96, and the title list of the other 60 (all 156 titles in
`titles.json`) names no calendar-bearing message either.

## Files

- `titles.json` — all 156 title-page rows (number, date, title, href) parsed
  from `witness-ssemsg-2010-en-20110108.html` and
  `witness-ssemsg-2011-en-20120610.html` (in `../edu-2010-2011-2026-10-04/`),
  annotated with the matched 200 capture where one exists.
- `fetchlist.json` — the 96 retrievable PDFs with their capture instants,
  original URLs and CDX digests.
- `retrievals.json` — per-PDF retrieval record (url, capture instant, sha256,
  size, pages).
- `pdf/` — the 96 fetched PDFs (byte-verified against the CDX sha1 digests).
- `txt/` — the 96 `pdftotext -layout` extractions.
- `subjects.json` — per-file page count and parsed header where recoverable.
- `SHA256SUMS.txt` — sha256 of every PDF and extraction.
- `fetch.log` — per-file retrieval instants and outcomes.
