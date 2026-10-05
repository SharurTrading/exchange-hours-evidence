# lse evidence thread — #218 (2015-2019 and 2020-Jan-Aug capture gaps)

Hunt pass: 2026-10-02 UTC. Evidence file: `docs/evidence/lse.md`. Issue:
SharurTrading/exchange-hours-rs#218.

## What this pass added

1. **The three-times-504'd domain-wide sweep is now DONE, unfiltered.**
   `url=londonstockexchange.com&matchType=domain&from=2015&to=2020&collapse=urlkey&filter=statuscode:200`
   returned **124 892 urlkeys** (17.8 MB; `cdx_lse_domain_2015-2020_all200_collapsed_urlkey.txt`
   here). Local greps over it:
   - `holiday|business day`: only 4 rows — an SVG asset, an external
     business-research PDF, a market-news meter link, and
     `.../technical-library/service-announcements/2005/live7005-publicholidaysandactivityschedule2006doc.doc`.
     **No business-days page state and no holiday document inside 2015-2019.**
   - The **service-announcements tree** (16 rows total, listed below) proves
     the operator published an annual **"Public holidays and activity
     schedule"** document per year on this tree (the 2006 edition was
     captured 2015-09-07), but the per-year index pages survive only for
     2003, 2004, 2005, 2006, 2009, 2010 and 2011 — **none in 2015-2019** —
     and no holiday-schedule document of any 2015-2019 year was ever
     crawled.
   - `calendar` rows: only UI SVGs, an EDX Russia trading-calendar page and
     a 2015 `exchange/ajax/calendar-highlights.html` (2 bytes, empty).
2. **The exchange-events AJAX feed was captured inside the gap and is
   empty of holidays.** All 23 status-200 captures of
   `londonstockexchange.com/exchange/ajax/calendar-events.html?day=..&month=..&year=..`
   (2015-08 through 2018-08 plus 2020-04-13; all 23 files here) replay to
   `{}` — an events feed with no holiday/closure content.
   The `calendar-events.html` capture of 2013-2014 dates are 301s.
3. **The 2019 service announcement** that is captured
   (`live-001-09-09-2019.pdf`, here) is a MiFIR volume-cap notice — not a
   holiday document. Negative.
4. **archive.today**: no snapshots of either `.htm` business-days form, the
   `/trade/trading-access/business-days` page, or an
   `/equities-trading/business-days` variant (404s on `newest`, checked
   2026-10-02 UTC).
5. **`lse.co.uk`** swept 2015-2020 (20 000-row CDX dump): it is a
   third-party share-prices/news portal (news-headline "calendars" only),
   not an operator channel — nothing admissible.

## Where this leaves #218

The 2015-01-02..2019-12-31 gap has now survived: per-directory CDX sweeps
(2026-09-29), the unfiltered domain-wide dump (this pass), archive.today,
Memento (2026-09-29), and CC prefix queries (pending in the background
batch). The most promising untried artifact class is the operator's own
annual **"Public holidays and activity schedule"** document series on the
technical-library service-announcements tree — a 2015-2019 edition of that
document (tree pattern
`.../service-announcements/<year>/live<NNNN>-publicholidaysandactivityschedule<year>...`)
or the year index page (`home-<year>.htm`) would key the span at T1, from
the operator's own site. A live retrieval from LSEG's document store or a
human request to the operator's desk are the remaining paths.

## Files here

- `cdx_lse_domain_2015-2020_all200_collapsed_urlkey.txt` — the full
  unfiltered dump (124 892 keys).
- `calevents/<timestamp>.html` — the 23 in-gap AJAX feed replays (all `{}`).
- `live001_2019.pdf` — the captured 2019 service announcement (negative).

## Common Crawl (2026-10-02, `cc-batch-2026-10-02.log` here)

Prefix queries `londonstockexchange.com/products-and-services/trading-services/business*`
in CC-MAIN-2015-48, 2016-47, 2018-47 and `londonstockexchange.com/trade/*`
in CC-MAIN-2019-43: **all zero captures**. CC is a checked negative for the
business-days pages.

## Pass 2 (2026-10-02 UTC): BOTH GAPS CLOSED — the `lseg.com` business-days channel

The 2015-12-03 service announcement (`live001-03122015-xmas-arrangements-2015_capture-20170916002832Z.doc`,
capture `20170916002832` — the class the earlier URL-name greps missed) carries the
operator's own pointer: "Full details of London Stock Exchange trading and EUI
settlement days can be found at: www.lseg.com/businessdays". Following it:
`lseg.com/businessdays` 301s (capture `20160423171007`) to
`lseg.com/areas-expertise/our-markets/london-stock-exchange/equities-markets/trading-services/business-days`
— the operator group's own Business days page — with **155 captures, 200s
continuously 2013-10..2020-07** (`perurl-lseg-busdays.json`). Seventeen captures
retrieved as `id_` replays and saved under `lseg-busdays-captures/` tile both
gaps; parsed rows in `parsed-tables.txt`:

- `LSE-LSEGBUSDAYS-2015-01-03` (20150103045430) prints all 2015 rows.
- `LSE-LSEGBUSDAYS-2015-12-21` (20151221080205) prints all 2016 rows.
- `LSE-LSEGBUSDAYS-2016-11-22` (20161122160354) prints all 2017 rows.
- `LSE-LSEGBUSDAYS-2017-12-02` (20171202110229) prints 2018 rows + 2019-01-01.
- `LSE-LSEGBUSDAYS-2018-10-01` (20181001173859) prints 2019 Good Friday..Spring.
- `LSE-LSEGBUSDAYS-2019-03-26` (20190326054958) prints 2019 Summer..New Year.
- `LSE-LSEGBUSDAYS-2019-12-19` (20191219013737) prints the whole 2020 year
  (2019-06-14 already prints the VE-Day-moved 2020-05-08).
- `LSE-LSEGBUSDAYS-2020-03-17` (20200317072237, gzip saved beside the html) is
  dated **inside 2020-01-01..2020-05-25** and prints 2020-04-10..2020-12-31 —
  the issue's second closing condition is met by the letter.
- Cross-checks: `2015-04-05`, `2016-01-18`, `2016-04-17`, `2017-02-04`,
  `2017-05-05`, `2018-02-03`, `2018-05-03`, `2019-06-14`, `2020-05-11`.

sha256 in `SHA256SUMS-lseg-2026-10-02.txt`. Service-announcements census
negatives kept: `live001-06042016-negative_*` (FTP testing notice),
`serviceann-home-2009/2010/2011/2015_*` index pages (the annual "Public
holidays and activity schedule" document class is absent from every captured
index 2009-2015; the 2009/2010 pages list per-holiday "Trading Schedule"
notices instead). Intermediate-era URL probes (`perurl-tsdir-businessdays.json`
— `products-and-services/trading-services/business-days/business-days.htm`,
65 captures, last 200 2014-02-09; `/equities-trading/business-days` first
capture 2023-09-07; `/securities-trading/...` first 2022-12-18) are recorded
as completed negatives. Heavy all-years CDX regex sweeps (publicholiday /
holiday / service-announcements / uncollapsed) were still queued on the flaky
CDX gateway when the gap closed; the close does not depend on them.
