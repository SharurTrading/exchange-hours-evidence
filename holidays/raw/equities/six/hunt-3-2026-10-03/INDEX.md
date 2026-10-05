# six hunt 3 — 2026-10-03 UTC — 2018-2019 CLOSED AS DATA (corrected after review)

Third retrieval pass on #212 (the 2010-2011 and 2018-2019 Trading Calendar
gap). Retrieval instant for all fetches: 2026-10-03 09:03-09:40 UTC. Digests
in `SHA256SUMS.txt`.

**CORRECTION, 2026-10-03 UTC (PR #270 review).** The original "completed
negative" verdict below was wrong for the live education-path
`trading-guide.pdf`: the PR #270 second-retrieval review re-read the saved
bytes (`six-edu-trading-guide.live-20261003.pdf`, sha256 `f459e1fb…`) and
found **`Trading Calendar 2018` and `Trading Calendar 2019` sections on its
pages 25-26** — twelve-month weekday grids per year, legend `Saturday —
Market Closed / Sunday — Market Closed / Market Holiday — Market Closed`,
operator footer "© SIX Swiss Exchange Ltd, 2018 … CH-8021 Zurich" — exactly
the closing condition's named document class. The 24 dark cells (12 per year,
all weekdays) key the 2018-2019 `Closed` rows that close #212's 2018-2019
half as data; the cell derivation is recorded in
`guide-calendar-cells-20261003.txt`. The first read of this artifact ("no
trading-calendar section at all") was an incomplete read and the item-1
sentence below is wrong on that point; it stands only for the module-1
negative, restated below.

## Angles swept this pass

1. **The education channel (the one untried operator-document family that
   could have carried the grids).** The preparatory-documentation path
   `six-group.com/dam/download/sites/education/preparatory-documentation/
   trading-module/` WAS archived (full CDX in this pass's session log; 13
   urlkeys): `trading-on-ssx-module-1-trading-en.pdf` (April 2019 edition,
   capture 20191119233413), `...-de.pdf` (20210921173701), the rules-modules,
   and the live `trading-guide.pdf` compilation. Retrieved this pass:
   - `six-edu-module1-trading.wayback-20191119233413id_.pdf` — truncated at
     exactly 1 048 576 bytes **by the original server** (its
     `x-archive-orig-content-length: 1048576` against the crawler-recorded
     2 813 845), so the archive itself holds a 1 MiB cut; the same is true of
     the 2021 DE module (crawler length 2 740 654). **Restated 2026-10-03 UTC
     to what the saved bytes support:** no text extraction recovers from the
     saved bytes — `pdftotext` cannot read the xref and PyMuPDF refuses the
     file (probe: `module1-extraction-attempt-20261003.txt`) — so the module
     keys nothing from saved evidence; the first pass's interactive reads
     (the complete-table-of-contents claim, the pointer sentence, the
     crawler-recorded lengths) were session observations, not archived
     artifacts, and are not relied on.
   - `six-edu-trading-guide.live-20261003.pdf` — the live education-path
     Trading Guide (the parts compilation cited in the evidence file's
     Sources for the 2018-05-28 grid): a compilation of guide parts
     ("Valid as of" 2014/2017/2018). **Corrected 2026-10-03 UTC: this
     document DOES carry `Trading Calendar 2018` and `Trading Calendar 2019`
     sections (pages 25-26) and closes the 2018-2019 gap as data** — the
     original "no trading-calendar section at all" reading was incomplete.
     See the correction note above and `guide-calendar-cells-20261003.txt`.
2. **German-language per-year names.** CDX exact on
   `trading_calendar_2018_de.pdf` and `trading_calendar_2019_de.pdf` under
   both the six-swiss-exchange.com per-year path and the six-group.com
   `/exchanges/` path: **zero captures** (session record — these two query
   outputs were not saved as dumps; the saved CDX artifacts of this pass are
   items 3-4); and no witness page names a German per-year file (the
   2019-04-11 shares page and the 2019-10-18 landing page link only the
   `grid_en.pdf` currency/settlement grids and `trading_calendar_2019.pdf`).
3. **The doubled-prefix host form.** The six-swiss-exchange.com
   `/exchanges/download/participants/regulation/trading_guides*` tree (the
   form the site's own mailto links print): **zero captures** across the
   whole prefix (`cdx_sixswiss_exchanges_tg.txt`).
4. **Media-release announcements.** Domain-wide six-group.com filter
   `(media|news|press).*(calendar|holiday)` 2017-2020
   (`cdx_sixgroup_media_calendar_2017-2020.txt`, 12 rows): three
   `trading-currency-holiday-calendar` pages, four `environment-calendar`
   pages plus the `swxess-availability-factsheet`, one teaser image, and
   three `interbank-clearing/{de,en,fr}/shared/news/2016/bankholidays.html`
   pages (2016 news posts, captured 2019) — three different instruments,
   none the exchange's trading calendar, and no announcement of a trading
   calendar exists. (Corrected 2026-10-03 UTC: the original item named only
   the currency-holiday and environment-calendar instruments and missed the
   interbank-clearing rows.)
5. **Operator annual reports.** The 2008-2019 annual-report editions are
   archived (`cdx_sixgroup_annual_2018-2020.txt`); the 2019 EN report
   (capture 20200422192452) was retrieved whole (44 711 words) and contains
   **zero occurrences of "holiday"** and no trading-calendar section — the
   corporate-report channel cannot key closures (a "trading days" count
   could not key dates under LAW-NO-FABRICATED-DATES in any case, which is
   also why the Facts & Figures statistics brochures are recorded here as
   considered-and-skipped rather than fetched).
6. **Common Crawl re-runs** (the queries the 2026-10-02 outage left
   re-runnable): CC-MAIN-2018-13 and CC-MAIN-2018-30 prefix queries for
   `six-swiss-exchange.com/download/participants/regulation/trading_guides/*`
   return **no captures**; CC-MAIN-2019-09 returns only the 301-redirect
   record for `smr7_participant_readiness.pdf`; CC-MAIN-2019-35 timed out
   once (504) — re-runnable, low expectation given 2018/2019-09.
7. **Web search for verbatim mirrors**, re-run with the literal per-year
   filenames: only other exchanges' same-named documents (HKEX Northbound,
   ASX 24 `trading-calendar-2019.pdf`, Malta SE) — no SIX document; matches
   the 2026-10-02 search's Eurex-only result.

## Net (restated 2026-10-03 UTC after review)

The 2018-2019 gap half is **closed as data**: the operator's own Trading
Guide of 28 May 2018 prints both years' grids (see the correction note), and
its 24 dark cells key the `SIX-TG-2018` rows in
`src/calendar/schedules/holidays/six.rs`. The 2010-2011 half remains negative
on every machine-reachable channel: the per-year PDF series (both hosts, EN
and DE names, both path forms), the guide editions (the full-guide editions
print 2015-2017 or 2020+ grids; the education modules yield no extraction),
the settlement/currency grids (proven different instruments), media releases,
annual reports, Wayback (complete domain filters), Common Crawl (through
2019-09), the non-Wayback archives (2026-10-02 pass), and web search.
Closing condition narrowed accordingly: a captured copy of the operator's own
Trading Calendar for **2010 or 2011** — from SIX's own channels or a human
request to the operator's desk (issue #212, whose 2018-2019 half this
closes; evidence file `docs/evidence/six.md`).
