# six evidence thread — #212 (2010-2011 and 2018-2019 Trading Calendar gap)

Hunt pass: 2026-10-02 UTC. Evidence file: `docs/evidence/six.md`. Issue:
SharurTrading/exchange-hours-rs#212.

## What this pass added

1. **The exact witnessed href is now proven and enumerated.** The 2019-04-11
   witness page (already in the store at
   `holidays/raw/equities/six/2010-2024/extra_six-shares-calendar-page-2019_capture-20190411184205Z.html`)
   links the 2019 calendar as
   `/exchanges/download/participants/regulation/trading_guides/trading_calendar_2019.pdf`
   on `www.six-group.com`. Probes 2026-10-02 UTC:
   - Wayback CDX exact on the `/exchanges/`-prefixed URL (2019 and 2018) and
     on `six-group.com/exchanges/...trading_calendar_2019.pdf`: **no captures**.
   - archive.today `newest`: 404 (no snapshot).
   - Memento TimeTravel aggregator (`timetravel.mementoweb.org/api/json/2019/...`):
     empty for the witnessed URL and both six-swiss-exchange.com forms.
   - Live: `six-group.com/exchanges/download/...` 301s to the products home
     page; `six-swiss-exchange.com/exchanges/...` 301s to a doubled prefix
     (`/exchanges/exchanges/...`) — both dead ends.
2. **The `/exchanges/download/` tree was crawled 2018-2020** — 254 captured
   files (`cdx_sixgroup_exchanges_download.txt` here), of which exactly three
   are `trading_guides` files (smr7 participant readiness, best execution,
   swissatmid factsheet). **No trading calendar in the crawled tree.** This
   closes the "was the /exchanges/ path ever checked?" question: it was
   crawled and is empty of calendars.
3. **`business_day.pdf`** (Trading Guide part, same directory) — captures
   only 2016-09-05 and 2017-11-15; both re-read here: it is a daily phase
   overview ("06:00 Start of Business Day ... 08:55 Start of Trading") and
   carries **no annual holiday grid** (both PDFs here). Negative.
4. **Web search for verbatim mirrors** of `trading_calendar_2019.pdf` /
   2010 / 2011: nothing; the only similarly-named document is **Eurex's own**
   `tradingcalendar_2019_en.pdf` (a Eurex document that merely references
   SIX trademarks — not the SIX trading calendar, not admissible).
5. Stable-URL verification: `trading_calendar_en.pdf` captures remain only
   the four 2022 redirect records (302/301); the six-group `dam/...trading-calendar-en.pdf`
   path has zero captures.

## Where this leaves #212

The 2026-09-30 search record in the evidence file was already complete for
Wayback; this pass adds the non-Wayback channels (archive.today, Memento
aggregation, Common Crawl on the per-year paths — the 2018-2020 CC index
queries returned empty for the `trading_guides` prefixes across seven
indexes, checked 2026-10-02 UTC with several gateway failures; the failed
ones are re-runnable) and proves the witnessed 2019 href itself was never
captured. The closing conditions stand as written in the issue: SIX's own
channels (download centre, publications archive) or a human request to the
operator's desk. The `extra_*` settlement/currency documents remain the
proof that the 2010-2011 grids archived are NOT trading calendars.

## Files here

- `cdx_sixgroup_exchanges_download.txt` — the 254-key tree enumeration.
- `business_day_20160905150205.pdf`, `business_day_20171115003322.pdf` —
  the Trading Guide part, both captures (negatives).

## Pass 3 (2026-10-02 UTC): completed negatives — the guide-generation channels

All probes under `probes-2026-10-02/` (sha256 in that directory's
`SHA256SUMS.txt`). Nothing survives; every lead of the hunt brief is now a
recorded negative:

1. **The exact witnessed URLs are capture-empty.** Wayback CDX exact:
   `six-group.com/exchanges/download/participants/regulation/trading_guides/trading_calendar_2019.pdf`
   and `..._2018.pdf` — zero captures of any status (`cdx-perurl-tc2018-exch.json`,
   `cdx-perurl-tc2019-exch.json`). archive.today `newest`: 404 for 2018/2019/`trading_guide.pdf`
   (`at-*.html`). arquivo.pt timemap: empty for all four per-year and guide URLs.
   Memento TimeTravel: the aggregator host no longer resolves to its API (DNS
   lands on GitHub-pages parking), so it contributes nothing new; the earlier
   pass had it working and empty.
2. **The Trading Guide mechanism is proven and is a dead end for the gap
   years.** `six-swiss-exchange.com/.../trading_guides/trading_guide.pdf` has
   exactly three PDF captures — 2015-12-16 ("valid as of 26 October 2015",
   prints Trading Calendar 2015 AND 2016), 2016-05-27 and 2016-09-07 ("valid
   as of 1 March 2016", prints 2016 AND 2017) — all years already sourced
   (`tg-20151216.pdf`, `tg-20160907.pdf`). The `dam/.../trading-guides/trading-guide.pdf`
   full-guide captures begin 2020-10-24 (would print 2020+2021). The
   operators' own guides pages of 2019-11-19
   (`witness-pguides-{trading,reg}-en-20191119.html`) list the complete
   trading_guides file set — `trading_calendar_2019.pdf`,
   `trading_calendar_2020.pdf`, `trading_guide.pdf` and the part documents —
   so no additional calendar-bearing filename existed there unprobed.
3. **No hidden calendar file class.** Full `trading_guides/` directory
   enumeration all-years (`cdx-prefix-sixswiss-trading_guides-all.json`, 47
   urlkeys), the 263-urlkey `/exchanges/download/` crawl census 2018-2021,
   the domain-wide six-group `trading_guide` sweep 2018-2021 (23 rows — only
   200s are the guides HTML pages and three unrelated PDFs), the uncollapsed
   `trading_calendar` sweep (21 rows — only the witness pages and the
   currency-holiday grids), the `participation/calendar/` prefix
   (Trading_Hours_Membertest.pdf, 30x only) and the `exchanges/ajax/` prefix
   2018-2020 (zero captures).
4. **2010-2011 era**: the full six-swiss-exchange.com `/download/` tree
   2008-2012 (268 urlkeys) holds no calendar-named artifact beyond
   `trading_calendar_2012.pdf`; `guide_ttc.pdf` (2008-11-22) is the Trade
   Type Code overview and `guide_order_book_trading_en.pdf` (2008-11-22)
   carries no calendar section (both re-read here). The live download centre
   carries no historical trading calendar (its 2012-2019 documents are ETP
   guides and fees).
5. **Common Crawl**: service-wide outage during this pass (the index host
   504s on every endpoint including `coll-info.json`, then began 307-redirecting
   to trailing-slash forms that 404/reset — checked 07:37-08:45 UTC). The
   earlier pass's CC queries for the `trading_guides` prefixes across seven
   indexes (recorded above, 2026-10-02) remain the completed CC record; this
   pass's wider queries (six-swiss 2017-2018 crawls for a late-2017
   `trading_calendar_2018.pdf`, the `/exchanges/download/` prefix) are
   re-runnable when the service recovers.
