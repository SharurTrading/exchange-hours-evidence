# cme-bracket-rereads — the 2026-10-03 UTC byte-level re-read of the #79 / #123 / #259 bracket-era artifacts

A second retrieval over the artifacts the three open CME gap issues hang on,
plus the fresh archived retrievals the earlier passes could not finish (the
Internet Archive was offline during parts of 2026-10-02). All retrievals below
were made 2026-10-03T09:14-09:18Z through web.archive.org raw replays. No
candidate closed its issue: every statement quoted is a matching-grid or
listing statement, none states a queue or Pre-Open onset in session language.

## Artifacts

| File | What it is | Retrieved from | Retrieval, UTC | sha256 |
|---|---|---|---|---|
| `SER-8051R.pdf` | CME Special Executive Report 8051R, 2017-12-14, "Initial Listing of the Bitcoin Futures Contract" — the `globex_cryptocurrency` 2017-12-17 launch row's cited document, now saved | `https://web.archive.org/web/20180106225141id_/http://www.cmegroup.com:80/notices/ser/2017/12/SER-8051R.pdf` (capture 2018-01-06T22:51:41Z, status 200) | 2026-10-03T09:14Z | `9ca9f103c271221a1b06478580dcfc73df92b947b5f41fcfa514701011b4d402` |
| `SER-8051R.txt` | pdftotext extraction of the above | local | 2026-10-03T09:14Z | (derived) |
| `wb_20120528102754_trading_hours_index.html` | CME trading-hours index, capture 2012-05-28T10:27:54Z — the last state printing Sunday Pre-Open 16:15 platform-wide; the #79 bracket's left endpoint, previously uncaptured in the store | `https://web.archive.org/web/20120528102754id_/http://www.cmegroup.com/trading_hours/index.html` | 2026-10-03T09:17Z | `32b05ccd1128638ce89a20d9760c321159c83e41995e8fd5438e292769260baa` |
| `wb_20120607015831_trading_hours_index.html` | CME trading-hours index, capture 2012-06-07T01:58:31Z — the first state printing Sunday Pre-Open 16:00 platform-wide; the #79 bracket's right endpoint, previously uncaptured in the store | `https://web.archive.org/web/20120607015831id_/http://www.cmegroup.com/trading_hours/` | 2026-10-03T09:17Z | `845a2d8278fdd3a29f79ed77091380dca6fed92b5b3e80a5cf7b9babf37a64a7` |
| `wb_20181017135528_globex-product-reference-sheet.xls` | CME Globex Product Reference Sheet, file's own create/save dates 2018-10-01 — inside the five-day crypto era; lists `Bitcoin Futures BTC BTC-BTC$` and carries **no hours and no Pre-Open columns at all** | `https://web.archive.org/web/20181017135528id_/https://www.cmegroup.com/globex/files/globex-product-reference-sheet.xls` (capture 2018-10-17T13:55:28Z, status 200) | 2026-10-03T09:18Z | `d88ed886b185e3628777cf1540747ffb8b22e695eacd3204702156ff22c906e6` |
| `cdx_newtradinghours_2026-10-03.json` | CDX for `cmegroup.com/globex/files/newtradinghours.pdf` (exact; the prefix form returns the same single row): exactly one capture, `20260829064641`, status 404 — the advisory-20120518 detail document was never archived while live | web.archive.org CDX | 2026-10-03T09:18Z | `d0cf900e787b7fab4a037e88b1343f988267bf499079bdf5cf99277025d93046` |
| `cdx_advisories_2012-05_2012-06.json` | CDX of every `cmegroup.com/tools-information/lookups/advisories/` URL captured 2012-05-01..2012-06-30 (56 captures): clearing-house advisories, market-regulation SERs, and the already-read electronic-trading/market-data pages — nothing new inside the #79 bracket | web.archive.org CDX | 2026-10-03T09:18Z | `565255824201baf03f674f901628d0000e55f54bef0c0579643251cd6e16245a` |
| `cdx_globex_files_2017-2019.json` | CDX of `cmegroup.com/globex/files/` captures 2017-2019 (urlkey-collapsed): no Bitcoin/cryptocurrency artifact exists in the directory in the launch era | web.archive.org CDX | 2026-10-03T09:18Z | `7751aff3a39a2550458dd6995ae978eead1f2f286662c9fe52e8a8ef4dbf1b10` |
| `cdx_bitcoin_paths_2017-2019.json` | CDX for `cmegroup.com/bitcoin*` 2017-2019: two 301 redirects only; `/cryptocurrency*` returned an empty set | web.archive.org CDX | 2026-10-03T09:18Z | `799a386d8c3babe647002a77543d206f0fb1b7907ed753a2a28661a4a258749d` |

## What the bytes say (verbatim)

- `SER-8051R.txt`: "Effective Sunday, December 17, 2017, for trade date Monday,
  December 18, 2017, and pending all relevant CFTC regulatory review periods,
  Chicago Mercantile Exchange Inc. ("CME" or "Exchange") will list the Bitcoin
  Futures contract (commodity code: BTC; rulebook chapter: 350) for trading on
  the CME Globex electronic trading platform" — and, under "Trading Hours And
  Commodity Code": "CME Globex and CME ClearPort: 5:00 p.m. to 4:00 p.m.,
  Sun-Fri. (Central Time)". No Pre-Open, no order-entry text anywhere in the
  document.
- `wb_20120528102754_trading_hours_index.html`: "E-mini S&P 500 Futures &
  Options 16:15 17:00-15:15 15:25, 16:45 15:30-16:30, 17:00-15:15"; "Gold
  Futures & Options 17:15 ET (16:15 CT)"; "Light Sweet Crude Oil (WTI) Futures
  & Options 17:15 ET (16:15 CT)"; already the new grain regime: "Corn Futures
  & Options 16:00 17:00-14:00 14:30- 16:00, 16:45 – 17:00 17:00-14:00
  09:30-13:15". No "Effective" dating text anywhere on the page.
- `wb_20120607015831_trading_hours_index.html`: "E-mini S&P 500 Futures &
  Options 16:00 17:00-15:15 15:25, 16:45 15:30-16:30, 17:00-15:15"; "Gold
  Futures & Options 17:00 ET (16:00 CT)"; WTI likewise 17:00 ET (16:00 CT);
  Corn unchanged. No dating text.
- Advisory 20120518 (already in the store at
  `cme-globex/trade-types/raw/metals-tas-history/wb-notice-20120518.html`,
  re-read in full this pass): "Effective this Sunday, May 20 (trade date
  Monday, May 21), the electronic trading hours on CME Globex for all CBOT
  Commodity, KCBT, and MGEX Grain and Oilseed futures and options will be
  expanded to the following: · Sunday to Friday: 17:00 CT to 14:00 Central
  Time (CT)" — the matching hours only; no Pre-Open, no pause, no 16:00/16:15.
- `operatorsreleaseschedule.pdf` (the one loose end of the 2026-10-02 pass,
  saved at `../cme-globex/evidence-thread/retry-2026-10-02/`): its extracted
  text (`ops.txt` there, re-derived this pass from the saved PDF) is the
  "FIX/FAST Operators Release Schedule" — market-data channel release dates
  for July 1 - November 18, 2012. No session or pre-open content.

## Verdicts

- **#79** (undated 2012 Sunday Pre-Open move 16:15→16:00 CT): definitive
  negative. The bracket (2012-05-28, 2012-06-07] re-verified from the saved
  endpoints; the candidate dating document (advisory 20120518) states matching
  hours only; its detail PDF was never archived; the advisory area holds no
  unread in-bracket capture; the FIX/FAST schedule resolves the last loose end
  negative. The maintainer's CME desk ask remains the sanctioned closer.
- **#123** (five-day-era Pre-Open onset undated): definitive negative. The
  launch SER dates the listing and states matching hours only; the launch-week
  Globex notices (in the store at
  `cme-globex/trade-types/raw/metals-tas-history/notices1718/`) date the
  listing and state no hours at all; the 2018-2021 spec captures state
  matching hours only; the 2018-10-01 reference sheet has no hours columns;
  the archive holds no other crypto schedule artifact.
- **#259** (2012-05-20..2013-04-06 regime queue onset undated): definitive
  negative. Advisory 20120518 (the regime's own dated row) states the matching
  hours only; the detail document it links is unrecoverable; the queue states
  re-verified as states on the saved 2012-05-28/06-07 captures.
