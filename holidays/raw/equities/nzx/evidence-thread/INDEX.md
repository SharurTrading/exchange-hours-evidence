# NZX evidence thread — #209 (2016-04-26..2017-04-13 capture gap)

Hunt pass: 2026-10-02 UTC (agent sweep; retrievals by curl live + Wayback CDX + archive.today
existence probes + web search). Evidence file: `docs/evidence/nzx.md`. Issue:
SharurTrading/exchange-hours-rs#209.

## FINDING — an operator artifact covering the gap exists and is live

**NZX Announcement 294559 — "NZX Market Holidays – 2016/2017"** — a MEMO from
NZX Client and Data Services to all NZX Market Participants, release date
2016-12-19 (NZ local; page stamp 15:15 Sun 18 Dec 2016), retrieved **live**
from `https://www.nzx.com/announcements/294559` on 2026-10-02 UTC.

Its holiday table, in session language, prints per date:

- 23 December 2016 — Abbreviated Trading
- 26 December 2016 — Boxing Day - Closed
- 27 December 2016 — Christmas Day Observed - Closed
- 30 December 2016 — Abbreviated Trading
- 2 January 2017 — New Year's Day Observed - Closed
- 3 January 2017 — Day after New Year's Day Observed - Closed
- **6 February 2017 — Waitangi Day - Closed** ← the one date inside the
  current recorded gap (2016-04-26..2017-04-13)
- 14 April 2017 — Good Friday - Closed
- 17 April 2017 — Easter Monday - Closed
- 25 April 2017 — ANZAC Day - Closed
- 5 June 2017 — Queen's Birthday - Closed
- 23 October 2017 — Labour Day - Closed

The memo is a **complete 2016/2017 list**, so combined with the
2017-07-18 Derivatives trading-hours page (reaches back to Good Friday
2017-04-14) it re-joins the windows from 2016-12-23 onward. It leaves only
**2016-04-26..2016-12-22** of the old gap unaudited (the memo starts at
23 December 2016).

Also retrieved live (corroborates the series and 2017-10-23's row):
**NZX Announcement 312156 — "NZX Market Holidays – 2017/2018"** (19 Dec 2017),
`https://www.nzx.com/announcements/312156`.

Files: `nzx-announcement-294559.html`, `nzx-announcement-312156.html` (raw
saved pages), `nzx-memo-2016-2017-text.txt`, `nzx-memo-2017-2018-text.txt`
(extracted MEMO bodies). No sha256 taken on the HTML (live dynamic page);
the extracted text files are stable.

## The remaining hole: 2016-04-26..2016-12-22 (Queen's Birthday 2016-06-06, Labour Day 2016-10-24)

The closing artifact would be the series' prior edition, **"NZX Market
Holidays – 2015/2016"** (published ~18-19 December 2015). What this pass
established about it:

- **NZX's own announcement system purges pre-December-2016
  announcements.** The Next.js data endpoint
  `/​_next/data/_cQa9-axa-UXU_AB-C7AS/announcements/<id>.json` answers
  404-notFound for 275000, 280000, 285000 and 290000; 294000 (2016-12-09)
  and 294559 answer. The purge boundary sits between 290000 and 294000
  (checked 2026-10-02 UTC).
- Wayback CDX of `nzx.com/announcements/*` 2015-2017 holds exactly six
  captures, all Nov-Dec 2017, none the holiday memo
  (`cdx_nzx_announcements_2015-2017.txt` in the hunt scratch; query kept:
  `url=nzx.com/announcements/*&from=2015&to=2017&collapse=urlkey`).
- archive.today has no snapshot of either announcement URL (404 on
  `archive.ph/newest/...` for 294559 and 312156, checked 2026-10-02 UTC).
- The annual MEMO's ID would be ≈276900±500 by the series' ID slope
  (~17.6k IDs/year); unguessable and unarchived, so ID probing cannot find
  it. A vendor mirror, an email copy in a participant's archive, or the
  operator's desk remain the closing paths.

## Other checked negatives this pass (2026-10-02 UTC)

- `/nzxmarket/holidays` Wayback captures 2010-2019: only 302s at
  2017-02-05 and 2017-04-22 (both INSIDE the gap) plus a 2011 404; the 302s'
  original redirect target is not recoverable (Wayback falls back to the
  2011 capture; no `x-archive-orig-location` exposed) and both URLs 404 live
  today.
- `nzx.com/docs*` 2016-2017 CDX: zero captures (annual PDF calendars never
  crawled).
- archive.today: no snapshots of `nzx.com/trading-hours`, `/regulation/key-dates`,
  `/key-dates`, `/services/trading-services/trading-hours`.
- Common Crawl domain queries for nzx.com 2016-2017 (`filter=url:.*holiday.*`):
  results pending in the background batch (CC index heavily 504-degraded
  2026-10-02); to be appended when the batch settles.

## Encoding notes for the user

- The memo's `Closed` rows are T1 session language keyed to venue-local
  trade dates; `Abbreviated Trading` rows need the half-day grid from the
  trading-hours page (the memo links `nzx.com/markets/NZSX/trading_hours`).
- Watch the memo's own reference URLs — they witness the December-2016
  location of the rolling tables.
- After encoding Waitangi 2017-02-06, the gap narrows to
  2016-04-26..2016-12-22 and the ledger/evidence windows move with it;
  update `tests/global_equities/holidays.rs` tallies per the issue's
  acceptance list.

## Common Crawl (2026-10-02, `cc-batch-2026-10-02.log` here)

Domain queries `nzx.com` with `filter=url:.*holiday.*` in CC-MAIN-2016-43
and CC-MAIN-2017-13, and `.*holiday|calendar.*` in CC-MAIN-2017-22: **all
zero captures**. CC is a checked negative for 2016-2017 holiday-bearing NZX
URLs (the announcement URLs carry no title in their path, so a capture of
the Dec-2015 memo, if any existed, would not match this filter — but the
trading-hours pages would, and none was crawled).

## Hunt pass 2, 2026-10-02 UTC — completed negatives; CC pending

**Purge boundary completed (live GET probes, `purge-boundary-2026-10-02.txt`
here):** 292000 → 404, 292500 → 200 — the operator's announcement system
purges everything below ≈292000-292500 (tighter than pass 1's 290000-294000
bracket). The 2015/2016 memo (id ≈276900 by the series slope) is
definitively purged; the sequential-ID brute force channel is CLOSED (no
retained straggler exists anywhere in the probed 275000-294001 range).

**A second announcement URL family exists:** `nzx.com/companies/<TICKER>/
announcements/<id>` (Wayback holds 2015-era captures; see
`cdx-nzx-notices-2015-2017.txt`). The market-memo URL form `nzx.com/
announcements/<id>` is unchanged since 2016 (the 294559 live URL, and the
2017-02-05 302 fallback in pass 1), so the pass-1 `announcements/*` sweep
covered the right family; the companies family carries company announcements
only.

**Wayback Dec-2015 census (`cdx-nzx-domain-dec2015-apr2016.txt`):** 733
captures Dec 2015-Apr 2016 domain-wide; the only Dec 14-31 hits are
subpage/asset fetches — Wayback was not crawling nzx.com when the memo
published. Completed negative for Wayback, consistent with pass 1's
six-capture record.

**The 2015-era announcement UI is a server-rendered table** (the
`assets/announcement-filter/*.js` assets are client-side filters —
`nzx-announcement-filter-market.js.wayback-20150113155240id_.js` here); no
data API exists to query around the purge.

**Not found (search pass):** no live index holds "NZX Market Holidays –
2015/2016" (the series ids found: 294559 = 2016/2017, 364227 = 2020/2022,
383874 = 2021/2023, 463713 = 2025/2027). The memo's closing paths remain a
vendor/participant mirror or the operator's desk. The Common Crawl batch
(announcements/* and trading-hours-family prefix queries across the
CC-MAIN-2016-07..2016-50 crawls, `cc2-batch-2026-10-02.log` here) was still
Common Crawl batch 2 (`cc2-batch-2026-10-02.log` here): the CC index gateway
answered one settled real query at ~08:19 UTC — **CC-MAIN-2016-50 holds zero
`nzx.com/announcements/*` captures** ("No Captures found") — and then
degraded to persistent 504s on every collection (probes 09:1x-09:2x UTC;
even one-row example.com queries time out). The announcements and
trading-hours-family sweeps across CC-MAIN-2016-07..2017-22 therefore remain
**re-runnable, not settled**; the query lists and runner are preserved at
`/private/tmp/hunt-tsx-nzx/{nzx,tsx}-queries.txt, cc-batch.sh`. Note the
pass-1 combined-filter result for CC-MAIN-2017-22 (`.*(holiday|calendar).*`)
is unreliable — the pipe in the regex collided with the batch runner's field
parsing — so that collection needs the pipe-free `.*calendar.*` re-run queued
above. No NZX row changed this pass; the 2016-04-26..2016-12-22 gap stands
with its recorded closing conditions.

## Hunt pass 3, 2026-10-03 UTC — THE GAP CLOSED: the series' 2015/2016 edition found on the operator's derivatives site

**FINDING — `NZX-DD-2015-11-20`.** The download system of the operator's own
derivatives site `nzxfutures.com` — a host no earlier pass had swept — holds
the holiday-memo series as PDFs. Wayback capture `20170520051811` replays
`http://www.nzxfutures.com:80/system/downloads/15/Market_Holidays_Memo.pdf?1464052847`
verbatim: *"NZX Dairy Derivatives Market Holidays – 2015/2016"*, NZX Client
and Market Services, 20 November 2015 — the 2015/2016 edition the
announcement-system hunt had been seeking. Its complete season table prints,
in session language, **`6 June 2016 Queen's Birthday Closed`** and
**`24 October 2016 Labour Day Closed`** (plus 13 more rows from 24 December
2015 to 27 December 2016), so the two rows key to it and its completeness
audits the span's ordinary days. #209 closes; the windows re-join into one
2010-01-01..2027-01-04 span. Encoded in the round-2 branch
`evidence-hunt-round2-nzx`.

The slot's three captures are all in this directory (`nzxfutures-*.pdf` +
extracted texts; sha256 in `SHA256SUMS.txt`): the 2013-09-17 derivatives
edition (capture `20140331113945`), the 2015-01-16 dairy edition (capture
`20160208055659`) and the 2015-11-20 dairy 2015/2016 edition. The two
earlier editions corroborate the market-scope step (see
`docs/evidence/nzx.md`): every date they share with a Main Board sheet
agrees. The slot inventory comes from `cdx-nzxfutures-domain-2014-2018.txt`
(541 rows; `/system/downloads/15/` has exactly these three 200-captures).

**Settled negatives this pass (probe artifacts here):**

- Wayback domain sweep 2016-04-26..2016-12-31
  (`cdx-nzx-domain-apr-dec-2016.txt`, 266 captures): assets, one securities
  page and the `companyresearch.nzx.com` subdomain only — no nzx.com page
  that could print the span was captured mid-2016.
- Uncollapsed trading-hours sweeps 2014-06..2018-06 (`cdx-sx-th-unc*.txt`,
  `cdx-nzdx-th.txt`, `cdx-dx-th*.txt`): the three pages' 200-captures run
  ...2015-04-27/28 then 2017-06/07 — no rolling-table state ever printed the
  span (one 302 at 2016-03-05).
- `companyresearch.nzx.com` (`cdx-companyresearch-nzx-alltime.txt`, 981
  rows): an NZX research/announcement mirror Wayback crawled 2008-2010; its
  announcement views answer **410 Gone** live and the rest sits behind the
  `crust` login — a dead end for 2015.
- `announcements.nzx.com` (live probe, `announcements-nzx-com-root.html`):
  a real, live "NZX Market Announcements" platform — but recent-window only
  (old ids, 294559 included, 404; id space matches the CA family at ~480.9k).
- The operator's static S3 export
  `nzx-prod-s7fsd7f98s.s3-website-ap-southeast-2.amazonaws.com` (search-index
  lead): a 2019-era prerender; REST listing AccessDenied; every announcement
  path shape 403 — a 2015 memo is not in it.
- Mondo Visione news index, full scan of 2015-12-15..2015-12-31 and
  2016-12-14..2016-12-23 (pages 10973-11011, 9950-10009): NZX's same-day
  media releases are carried ("NZX Market Activity Remains Strong In 2015"
  on 2015-12-18; "NZX Employee Share Plan" on 2016-12-30) — **no NZX holiday
  memorandum was ever carried, in either year**, while a dozen other
  exchanges' holiday notices appear.
- ShareChat (`cdx-sharechat-*.txt`, `sc-ann-20160123.html`,
  `sc-nzxo-2015.live-shell.html`): alive through 2015-2016 and mirroring the
  same CA id family (`/announcement/NZX/<TICKER>/<id>/...`), but only one
  announcement page was ever captured; the 2012-era page 500s live and the
  NZXO yearly listings serve an empty JS shell.
- Common Crawl: the index gateway 504-degraded all day again (even
  example.com queries time out); the batch-2 prefix sweeps across
  CC-MAIN-2016-07..2017-22 remain **re-runnable, not settled** — moot now
  that the rows are sourced and encoded.
- NZX annual report FY2016 / adviser portal / T4 news: not reached — the
  hunt closed with the memo found before those angles were spent.
