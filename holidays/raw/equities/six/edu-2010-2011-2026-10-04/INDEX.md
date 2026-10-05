# Evidence index — `equities/six/edu-2010-2011-2026-10-04`

Fourth hunt pass on issue #212's 2010-2011 half, run 2026-10-04 00:08-00:50
UTC (LAW-UTC-DATES), after the 28 May 2018 education-path guide closed the
2018-2019 half (hunt-3). **Verdict: NEGATIVE for row data — no 2010 or 2011
operator document printing the year's holiday grid survives on any
machine-reachable channel — but the witness chain for the unarchived
documents is now exact.** Digests in `SHA256SUMS.txt`.

## What the pass established

1. **The 2010/2011 calendars were published under the stable name
   `trading_calendar_en.pdf`** (updated in place each year), NOT per-year
   names. Witnessed three ways, all saved here and in the 09-30 store:
   - `witness-tg-de-20100203.html` (capture `20100203141257`),
     `witness-tg-en-20100525.html` (`20100525145312`) and
     `witness-tg-fr-20100525.html` (`20100525144834`) — the operators' own
     Trading Guides index pages of February and May 2010, each linking
     `/download/participants/regulation/trading_guides/trading_calendar_en.pdf`
     alongside the part-guide family (`trading_guide_en.pdf`,
     `business_day_en.pdf`, `trading_period_en.pdf`, ...).
   - The 2010-01-31 and 2010-11-15 Trading-and-Settlement-Calendar pages
     (already in `cdx-retry-2026-09-30/` as `six-grid-2010/2011`) both link
     the same stable path with the sentence "trading calendar [pdf] shows on
     which days there is no trading". The per-year rename
     (`trading_calendar_2012.pdf`, capture 2011-12-10) happened between May
     2010 and December 2011.
   - CDX uncollapsed all-URL-forms (`cdx-uncollapsed-tc-en.txt`): the stable
     URL's captures are exactly four 2022 redirect records (302/301, empty).
     **No 2010 or 2011 capture exists on Wayback.**
2. **The Trading Guide edition of 11 January 2010 existed.** The May-2010
   guides page's archive section lists the dated part editions
   `trading_guide_2010_01_11_en.pdf`, `business_day_2010_01_11_en.pdf`,
   `market_model_2010_01_11_en.pdf`, ... under
   `download/participants/regulation/archive/trading_guides/` (witness:
   `witness-tg-archive-en-20100525.html`, `witness-tg-archive-de-20120105.html`).
   By the proven edition pattern (the 2015-12-16 guide prints 2015 AND 2016;
   the 2016-09-07 guide prints 2016 AND 2017 — hunt-3 re-reads), a January
   2010 guide edition would print the 2010 and 2011 grids. **The whole
   archive path holds exactly one Wayback capture**
   (`cdx-uncollapsed-archive-tg-all.txt`, `cdx-sixswiss-archive-prefix.txt`):
   `on_order_book_2010_01_11_en.pdf` at `20250528090810`, status 301, empty
   body. The six-group `/exchanges/` mirror of the archive path: one 301
   (`cdx-sixgroup-exchanges-archive.txt`). Live 2026-10-04: both the
   six-swiss archive/trading_guides URLs and the six-group /exchanges/ forms
   301 to the products home page (`live-probe.log`).
3. **No capture of either target on the non-Wayback archives.** archive.today
   `newest`: "No results" for `trading_guide_2010_01_11_en.pdf`,
   `business_day_2010_01_11_en.pdf` and `trading_calendar_en.pdf`
   (`at-*.html`). arquivo.pt: empty timemap for the stable URL, zero
   text-search hits for "trading calendar"+six-swiss-exchange and
   "Handelskalender"+"SIX" (`arquivo-*`). Memento aggregator stays dead (DNS
   parked; recorded 2026-10-02).
4. **Common Crawl early indices remain outage-blocked (re-runnable).**
   CC-MAIN-2010, 2011, 2012, 2013-20, 2013-48, 2014-10, 2014-15 prefix
   queries for `six-swiss-exchange.com/download/participants/regulation/*`:
   504 on every attempt across three retry rounds 00:28-00:42 UTC
   (`cc-*.txt` are the 504 bodies, `cc-sweep.log` the record; the index host
   also 504s on `coll-info.json`). The same outage pattern was recorded
   2026-10-02; the hunt-3 pass (2026-10-03) got through for 2018-2019
   indices, so this remains the one re-runnable machine channel.
5. **Web search: only another operator's calendar.** The 2011 hits are
   Eurex's own "Trading Calendar 2011"/"Handelskalender 2011" (whose Swiss
   line concerns Eurex-listed Swiss products/LEPOs) — not the SIX cash-market
   calendar, not an operator document for our rows, recorded as
   considered-and-rejected (the 2026-10-02 pass had already found the Eurex
   document class for the per-year names).
6. **The official-messages channel (Angle 4) is exhausted — negative.**
   Complete title lists extracted from the archived year pages (saved):
   - `witness-ssemsg-2010-en-20110108.html`: all 85 messages of 2010
     (01/2010 04.01. - 85/2010 07.12.), NO calendar/holiday/trading-days
     announcement.
   - `witness-ssemsg-2011-en-20120610.html`: all 71 messages of 2011
     (01/2011 03.01. - 71/2011 22.12.), same negative.
   - `witness-ssemsg-2012-en-20120611.html` (29 messages, H1 2012) and
     `witness-ssemsg-2011-de-20110207.html` (DE partial): same negative.
   The individual message PDFs were themselves never captured (`cdx-swx-messages-prefix.txt`:
   844 rows over the whole `swx_messages*` prefix, of which only two
   non-message urlkeys resolve to 200 PDFs — `list_chf_bonds_stoptrading.pdf`,
   `spiextra_en.pdf` — the dated `swx_message_*.pdf` rows are 302/301s).
7. **Education/training/documentation trees of the era (Angle 1) — negative.**
   Domain-wide `educat|training|ausbildung|dokument` filters 2008-2013
   (`cdx-edu-*.json`): six-swiss carries careers/trader-education HTML pages
   and five course PDFs (`download/trading/training/education/preparation/1_1_new_issues_de.pdf`,
   `1_2_dept_sec_de.pdf`, 2009 captures; `education/material/1_3_equity_sec_fr.pdf`
   2013; `2_4_supervis_authorit_and_penalt_{de,en}.pdf` 2022/2024) — course
   material, no calendar section class; the only `ausbildung` hit is one
   navigation GIF. six-group.com 2008-2013: only `about/jobs/further_education_*.html`
   (2009). swx.com (predecessor, 2006-2013): the SWX training-module family
   `download/trading/training/1_*..3_*_{de,en,fr}.pdf` and `tmup_3_match_*` —
   all captured 2006-03/07, SWX-branded course PDFs predating the gap years;
   its later captures (2011-2024, e.g. `3_handel_de.pdf` 2024) are the same
   SWX-era documents. Nothing in this family is a calendar carrier.
8. **DE/FR guide-name variants (Angle 2) — negative.** Domain-wide `kalender`,
   `calendrier`, `feiertag` on six-swiss-exchange.com: zero rows.
   `holiday` on six-swiss: only the 2012 fee-holiday news pages (a fee
   instrument). six-group `kalender|calendrier`: only SIX SIS settlement
   kalenders (xls, 2022+) and an SVG icon. swx.com
   `calendar|kalender|holiday|feiertag` 2007-2013: only the settlement/currency
   grid pages 2006-2009 (the ruled-out instrument) and dojo UI assets.
   `swx.ch`/`six-swiss-exchange.ch` aliases: nothing calendar-bearing
   (`cdx-swxch-calendar.txt`, `cdx-sixswissch.txt`).
9. **News-announcement pages 2009-2012 — negative.** The 182 captured
   `news/overview*.html?id=` ids (`cdx-news-overview-ids.txt`) contain no
   calendar/holiday/trading-days announcement id.
10. **The guides-revisions pages of 2012 have no surviving capture content**
    (`witness-revisions-tg-de-20120104.html` is a Wayback error page; the
    `revisions/until_2010_03_31/trading_guides_en.html` fetch returned 0 bytes).

## Closing condition (narrowed to named bytes)

The 2010-2011 half of #212 closes exactly when bytes surface of either:
(a) `six-swiss-exchange.com/download/participants/regulation/trading_guides/trading_calendar_en.pdf`
as served between January 2010 and the 2012-edition rename (witnessed live
2010-01-31 through 2010-11-15), whichever year edition that bite holds; or
(b) the Trading Guide edition of 11 January 2010
(`trading_guide_2010_01_11_en.pdf`), whose calendar section would print the
2010-2011 grids under the proven two-year pattern. No Wayback, archive.today,
arquivo.pt or live capture exists; Common Crawl's early indices are the only
re-runnable machine channel (queries recorded above), else a human request to
the operator's desk.

## Files

- `witness-tg-{en,de,fr}-2010*.html` — the Feb/May 2010 Trading Guides index
  pages (Wayback `id_` replays; sha256 in `SHA256SUMS.txt`).
- `witness-tg-archive-{en,de}-*.html` — the until-2010-03-31 archive guides
  pages naming the 11 January 2010 editions.
- `witness-ssemsg-*.html` — the official-messages year pages (title lists
  extracted for the record above).
- `cdx-*.txt|json` — verbatim CDX sweep outputs (see `cdx-sweep.log` for
  query instants).
- `cc-*.txt`, `cc-sweep.log` — the outage-blocked Common Crawl attempts.
- `at-*.html`, `at-sweep.log` — archive.today probes.
- `arquivo-*`, `arquivo-sweep.log` — arquivo.pt probes.
- `live-probe.log` — live redirect checks (00:31 UTC).
- `fetch.log` — per-artifact retrieval instants.
