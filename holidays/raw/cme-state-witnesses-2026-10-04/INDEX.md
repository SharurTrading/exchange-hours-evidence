# cme-state-witnesses-2026-10-04 — the archived state-witness hunt for #123 and #79

The 2026-10-04 UTC pass hunted for a dated archived capture of the operator's
own pages that shows a state the crate's two open CME declarations need:
the `globex_cryptocurrency` five-day-era Pre-Open (#123, any in-era capture of
a crypto page printing the queue in session language) and the 2012 Sunday
Pre-Open switch 16:15→16:00 CT (#79, any capture from inside the
2012-05-28..2012-06-07 bracket). **Every angle closed negative: no witness
exists in Wayback, Common Crawl or the alternate archives, so no row is keyed,
no declaration moves, and both gaps stay desk-thread-dependent.** All
retrievals below were made 2026-10-04T00:20-12:10Z unless stated. cmegroup.com
was never touched live; every route was web.archive.org, index.commoncrawl.org
or the alternate archives named below.

## Verdicts

- **#123** (five-day-era Pre-Open onset): **negative.** The operator's bitcoin
  product page carries no hours content in its HTML at all — neither on the
  era's first day (Wayback capture 2017-12-17) nor in the January-February
  2019 window the ask names (Common Crawl's 2019-02-16 fetch, byte-verified) —
  so neither capture can print the queue; the landing page is likewise
  silent; the FAQ's only pre-open sentence is the price-limit halt state, not
  the daily queue; the contractSpecs-futures page prints the matching grid
  only; the 2019 holiday workbooks print no `(PREOPEN)` token in any Bitcoin
  row; the trading-hours service's era captures (2022-08-23, 2023-09-07) hold
  no cryptocurrency rows; the crypto landing/markets pages have no era captures
  at all (earliest 2021-03-31); and the domain-wide bitcoin/crypto CDX sweeps
  surface only the already-read page classes. The onset remains undated and
  #123 stands.
- **#79** (2012 Sunday Pre-Open switch): **negative — the bracket cannot be
  narrowed from any archive.** The complete CDX enumeration of every
  `cmegroup.com/trading_hours/*` capture across 2012-04-01..2012-07-15 (58
  rows, uncollapsed) holds exactly two captures inside the
  2012-05-28..2012-06-07 bracket — the two bracket endpoints the store already
  holds (`cme-bracket-rereads/`). Common Crawl's 2012 crawl fetched the
  trading-hours pages only in February 2012. The 2012-era product
  specification pages print the matching grid only and never a pre-open value,
  so that channel cannot witness the queue regardless of capture dates.
  archive.today refused (HTTP 429, twice), arquivo.pt returned nothing, and
  both Memento aggregator hosts are unresolvable. The client-systems wiki's
  TAS page was created 2024-12-21, so its revision history cannot reach 2012.
  The bracket 2012-05-28..2012-06-07 and the desk ask stand exactly as
  recorded in the evidence file.

## Artifacts (`artifacts/`)

| File | What it is | Retrieved from | Capture / fetch, UTC | sha256 |
|---|---|---|---|---|
| `wb_20171217225155_bitcoin.html` | The operator's bitcoin product page on the five-day era's first day (capture 2017-12-17T22:51:55Z): no `Trading Hours` content in the HTML at all — the tab renders client-side; no pre-open text anywhere | `https://web.archive.org/web/20171217225155id_/http://www.cmegroup.com:80/trading/equity-index/us-index/bitcoin.html` | archive capture 2017-12-17T22:51:55Z | `6d84efbb15b873b7334a9419ebc8d991985b6cb37db95adeeca3e73d0a0eaf04` |
| `wb_20171217104134_trading-bitcoin-futures.html` | The `/trading/bitcoin-futures.html` landing page, capture 2017-12-17T10:41:34Z (era's first day): no pre-open text | `https://web.archive.org/web/20171217104134id_/http://www.cmegroup.com:80/trading/bitcoin-futures.html` | archive capture 2017-12-17T10:41:34Z | `fc2087e205b639ec04fff1591d9f5f1149b6f353542befbf3da42629d2a80958` |
| `wb_20190121042903_trading-bitcoin-futures.html` | The same landing page, capture 2019-01-21T04:29:03Z (the January-2019 window the #123 ask names): no pre-open text | `https://web.archive.org/web/20190121042903id_/https://www.cmegroup.com/trading/bitcoin-futures.html` | archive capture 2019-01-21T04:29:03Z | `5bcf6faf8a81df098413c5d70a92ed3e711610e0703655cebe2983fdd67f5c62` |
| `wb_20171223060541_btc-faq.html` | The operator's bitcoin futures FAQ, capture 2017-12-23T06:05:41Z. Its only pre-open language: a contract at its price limit "will enter into “a pre-open” market state. During the pre-open market state, trade matching does not occur but orders can be entered, modified or cancelled" — the halt mechanism, not the daily queue | `https://web.archive.org/web/20171223060541id_/https://www.cmegroup.com/education/cme-bitcoin-futures-frequently-asked-questions.html` | archive capture 2017-12-23T06:05:41Z | `75b5fdf8e3b39afd55f1dbba06401a56aaa213f828c35f79bd97ff15b4438857` |
| `wb_20180121044846_btc-contractspecs-futures.html` | The `bitcoin_contractSpecs_futures.html` page, capture 2018-01-21T04:48:46Z (in-era): hours row prints the matching grid only — "Sunday - Friday 6:00 p.m. - 5:00 p.m. (5:00 p.m. - 4:00 p.m. CT) with a 60-minute break each day beginning at 5:00 p.m. (4:00 p.m. CT)" — and zero pre-open text | `https://web.archive.org/web/20180121044846id_/http://www.cmegroup.com:80/trading/equity-index/us-index/bitcoin_contractSpecs_futures.html` | archive capture 2018-01-21T04:48:46Z | `8c364e697d8c616d3390df516605538680c6223af2afa321960053c05d22dd19` |
| `wb_20120507084420_gold_spec.html` | The 2012-era gold product specification page, capture 2012-05-07T08:44:20Z: the `Hours (All Times are New York Time/ET)` rows print the matching grid only ("Sunday – Friday 6:00 p.m. – 5:15 p.m. (5:00 p.m. – 4:15 p.m. Chicago Time/CT) with a 45-minute break each day...") — no pre-open value anywhere. Establishes that the 2012 specification channel structurally cannot witness the Sunday Pre-Open, so no in-bracket spec capture could narrow #79 | `https://web.archive.org/web/20120507084420id_/http://www.cmegroup.com/trading/metals/precious/gold_contract_specifications.html` | archive capture 2012-05-07T08:44:20Z | `b2259d439eb84378b331c9e6e3fc665812eb5d3c306c3538c99c1e4f4ca437cc` |
| `thbp_2022-08-22_2022-08-24_20220823173514.json` (+ `.dec.json` derived) | The operator's trading-hours service, archive capture 2022-08-23T17:35:14Z, window eventDate 2022-08-22..24 (five-day era): page 1 of the most-active sort holds seven products (Eurodollar, SOFR, ZF, ZN, ES, ZT, ZQ) — no cryptocurrency row; ES/GE print `16:45 preopen; 17:00 open` | `https://web.archive.org/web/20220823173514id_/https://www.cmegroup.com/services/trading-hours-by-product?pageNumber=1&pageSize=7&exch=&cleared=Futures&group=&subGroup=&sortField=most-active&sortAsc=true&fromEventDate=2022-08-22&toEventDate=2022-08-24&isProtected&_t=1661276114342` | archive capture 2022-08-23T17:35:14Z | `b20a0e57cba00a12cf338006ad4577f07e2cda8b0fdfb2665b860ee4b29e8edb` |
| `thbp_2022-08-22_2022-08-24_20230907123824.json` (+ `.dec.json` derived) | The same service and window re-fetched at capture 2023-09-07T12:38:24Z: `hasEvents: false`, all schedules empty — the era's service captures carry no crypto rows | `https://web.archive.org/web/20230907123824id_/https://www.cmegroup.com/services/trading-hours-by-product?...&fromEventDate=2022-08-22&toEventDate=2022-08-24&isProtected&_t=1661276127946` | archive capture 2023-09-07T12:38:24Z | `ee2db084a9d940695bfd5c8e6fae5b2e40229ca38b6bb23b909220f13a27cd0b` |
| `archiveph-20120603-th-index.html` | archive.today's HTTP 429 rate-limit response to the in-bracket query for the trading-hours index (twice, 45 s apart) — refusal recorded, not a snapshot | `https://archive.li/20120603/http://www.cmegroup.com/trading_hours/index.html` | fetch 2026-10-04T00:52Z and 11:54Z | `6b18ebdc0d774de49eacfc4f6389386a8835f4acad0c328c1c539b7e4b25e952` |
| `cc_20190216200839_bitcoin.html` (+ `.warc.gz` raw range fetch) | The bitcoin product page as Common Crawl fetched it on 2019-02-16T20:08:39Z — the January-February 2019 window the #123 ask names: zero `pre-open` mentions and no `Trading Hours` content at all, byte-verified against the WARC record (digest `WCEERRNEUO5NQNJF6NLGEYXZCYYCR3GS`) | `https://data.commoncrawl.org/crawl-data/CC-MAIN-2019-09/segments/1550247481111.41/warc/CC-MAIN-20190216190407-20190216212407-00001.warc.gz` (HTTP range 802781547-802802331) | CC fetch 2019-02-16T20:08:39Z; retrieval 2026-10-04T01:14Z | `.warc.gz` `3b0c8ba52410c0f83d578ad8de49cd3f1b0b5bb459fdcab60278f6042332d367`; extracted `.html` `27a03ccdb325ebea017911a3e2beaca9f6601fcf4ba818785441b0d8ad4e2f9f` |

## CDX / index dumps (`cdx/`, `cdx/cc2012/`)

| File | Query | Result, UTC |
|---|---|---|
| `cdx-bitcoin-product-prefix-2017-2019.json` | Wayback CDX `cmegroup.com/trading/equity-index/us-index/bitcoin*`, 2017-12..2019-12 | 490 rows; `bitcoin.html` 93 captures (200s from 2017-12-04 on, incl. era-first-day 2017-12-17); spec page 50 captures (incl. the already-read 2017-12-14/22, 2018-01-04, 2019-06-03); all other paths quotes/margins/calendar pages |
| `cdx-domain-bitcoin-2017-2019.json` | Wayback CDX domain-wide `filter=original:.*bitcoin.*`, 2017-12..2019-07 | 553 urlkeys; only index/reference-rate, education, press-release and the already-read trading pages — no new hours carrier |
| `cdx-domain-crypto-2017-2019.json` | Wayback CDX domain-wide `filter=original:.*cryptocur.*`, 2017-12..2019-07 | 43 urlkeys; index/reference pages only |
| `cdx-markets-cryptocurrencies-2017-2019-empty.json` | Wayback CDX `cmegroup.com/markets/cryptocurrencies*`, 2017..2019 | empty — the current crypto landing URL has no era captures (its earliest is 2021-03-31, `cdx-markets-cryptocurrencies-all.json`) |
| `cdx-tradinghours-2012-04.json`, `cdx-tradinghours-2012-05_07-all.json` | Wayback CDX `cmegroup.com/trading_hours*`, 2012-04-01..05-01 and 2012-05..07-15, uncollapsed | 58 rows total; exactly two captures inside the #79 bracket (2012-05-28 index, 2012-06-07 `/` — both already in `cme-bracket-rereads/`); the 2012-ten 05-05 rows and the 05-11 pair sit between 05-05 and 05-28 |
| `cdx-tradinghours-2016-2019.json` | Wayback CDX `cmegroup.com/trading_hours*`, 2016..2019, urlkey-collapsed | 10 rows: 4×301, 4×dash, 1×404 and one 200 (2016-08-10, `trading_hours.html` at 10,835 bytes, the dead pre-crypto shell) — the trading-hours pages were gone before the crypto era |
| `cc-CC-MAIN-2018-51/2019-09/2019-18/2019-30/2019-43.json` | Common Crawl per-crawl indexes, `url=cmegroup.com/trading/equity-index/us-index/bitcoin*` | 39 records, all of the already-read page classes; the January-February 2019 fetches are `bitcoin.html` (2019-02-16) and `bitcoin_product_calendar_futures.html` — no hours carriers |
| `cc-2019-09-bitcoin-full.json` | full CC-MAIN-2019-09 index records for `bitcoin.html` | one 200 record: fetch 2019-02-16T20:08:39Z, WARC `CC-MAIN-20190216190407-20190216212407-00001.warc.gz`, offset 802781547, length 20784 |
| `cc2012/{index,energy,equities,metals}-hours.html.json` | Common Crawl `CC-MAIN-2012` exact-URL indexes for the trading-hours pages | four records, fetch timestamps 2012-02-04, 02-10, 02-12 — all before the bracket |
| `cc2012/{commodities,fx,interest-rates,real-estate,weather}-hours.html.504-refusal.txt` | same queries | index.commoncrawl.org 504 Gateway Time-out, four attempts each — refusals recorded (these sections are not load-bearing for #79's families; equities/metals/energy all answered) |
| `cc-2012-tradinghours.json` | `CC-MAIN-2012-26` (nonexistent collection) and the prefix-form `CC-MAIN-2012` query | "No index found" / 504s; the exact-URL form above is what answered |

## Reads against artifacts already in the store (no new bytes)

- **2019 holiday workbooks.** All 18 `.xls` members of
  `holidays/raw/cme-2019-2021/2019-holiday-calendars.zip` (pinned there,
  sha256 `1e861e355238903b013c1288f4eb9e8026e6ddd5fc1001dfd2acdbfcc1832e05`)
  were re-dumped with that directory's `dumpxls.py` on 2026-10-04: every sheet
  carries one `Bitcoin` row (e.g. the MLK sheet's
  `Bitcoin | Regular @ 1600 CT / 2200 UTC | Regular @ 1700 CT / 2300 UTC |
  1200 CT / 1800 UTC | Regular @ 1700 CT / 2300 UTC`) and **no sheet contains
  the token `preopen`/`PRE-OPEN` anywhere** — the workbooks print closures and
  matching-grid deviations only, so they cannot witness the queue.
- **Launch-era Globex notices.** All 70 notice pages in
  `cme-globex/trade-types/raw/metals-tas-history/notices1718/` re-scanned: the
  only `pre-open` hits (2018-04-23, 2018-04-30, 2018-05-07) are the TACO
  E-mini S&P sections ("Sunday Pre-Open 4:00 pm Central Time (CT)"), not
  cryptocurrency.
- **Client-systems wiki.** `wiki-tas-457223974.json` (same directory): the TAS
  page's `createdAt` is 2024-12-21T17:05:53Z with version 2 on 2025-01-13 —
  the page did not exist before December 2024, so no revision of it can state
  the 2012 change.
- **Wayback CDX exact queries (no dumps, read inline):** the ES spec page URL
  form `e-mini-sandp-500*` has no captures at all in 2012-05..07;
  `crude-oil_contract_specifications.html` none in the window;
  `e-mini-nasdaq-100_contract_specifications.html` captures 2012-04-12,
  05-07, 05-09, 05-10, then 2012-06-16 — none inside the bracket (and the
  channel cannot carry the witness regardless, per the saved gold-spec bytes);
  the crypto FAQ page has no 2017-2019 Wayback captures other than the ones
  listed above.
- **Memento aggregators.** `timetravel.mementoweb.org` and
  `api.mementoweb.org` both fail DNS resolution (2026-10-04T00:56Z).
  `arquivo.pt/wayback/timemap` returned an empty body for the trading-hours
  index.
