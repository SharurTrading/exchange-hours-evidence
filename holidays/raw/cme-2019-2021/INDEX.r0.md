# cme-2019-2021 — evidence index

Task: CME Group holiday schedules for calendar years 2019, 2020, 2021, per product group.
Charter: exchange-hours-rs AGENTS.md (2026-09-12 UTC). Retrieval performed 2026-09-12 UTC.
All artifacts are CME Group's own published Globex holiday schedules — **tier T1**
(operator statement), read from the Internet Archive's verbatim replay (`id_` raw mode)
of `cmegroup.com`. cmegroup.com returns 403 to this machine directly.

Times are recorded exactly as CME prints them. These sheets print **CT with UTC**
(header: "All times are Central Time   ET +1  UTC +5/+6"); the ET column appears only in
the TAS notes, where CME prints "CT / ET". Both are kept verbatim.

## Enumeration (CDX) — what exists

| File | What |
|---|---|
| `cdx-hc.json` | CDX `cmegroup.com/tools-information/holiday-calendar*`, 2017-2023, collapse=digest |
| `cdx-files.json` | CDX prefix `…/holiday-calendar/files/`, 2018-2023, statuscode 200 |
| `cdx-tradinghours.json` | CDX `cmegroup.com/trading-hours*`, 2017-2023 (no 2019-2021 holiday PDFs; the `/trading-hours/files/` holiday PDFs begin in 2023) |
| `cdx-hcpage.json` | CDX snapshots of `holiday-calendar.html`, 2019-2022 |
| `page-20191206230021.html`, `page-20200611060720.html`, `page-20200420113115.html`, `page-20200326083500.html` | archived `holiday-calendar.html` — the operator's own index of which holiday documents existed each year |

The enumeration showed CME published, for each year, one **annual consolidated ZIP**
(`<year>-holiday-calendars.zip`) plus per-holiday `.xls` schedules (a full sheet and a
"compact" sheet) and per-holiday settlement-time / OTC advisory PDFs. The three ZIPs below
source every holiday in their year.

## Primary artifacts (consolidated, one per year)

| Local path | URL | Archive capture (UTC) | sha256 |
|---|---|---|---|
| `2019-holiday-calendars.zip` | https://www.cmegroup.com/tools-information/holiday-calendar/files/2019-holiday-calendars.zip | 2021-01-26 09:48:37 | 1e861e355238903b013c1288f4eb9e8026e6ddd5fc1001dfd2acdbfcc1832e05 |
| `docs/2020-holiday-calendars.zip` | https://www.cmegroup.com/tools-information/holiday-calendar/files/2020-holiday-calendars.zip | nearest-2021 replay; ZIP members dated 2020-12-29 | 5263a4a5e9076bc0e69c7cd0e3fd9f82dc4d80b66f1b56f14070f08c1d762b59 |
| `docs/2021-holiday-calendars.zip` | https://www.cmegroup.com/tools-information/holiday-calendar/files/2021-holiday-calendars.zip | nearest-2022 replay; ZIP members dated 2022-01-03 | 0ee0860a3a0e035eb9d079419aca3cafcc4256d296fa916647987c396dda8c59 |

Extracted to `zip2019/globex-trading-schedules/`, `zip2020/`, `zip2021/`.
Plain-text dumps of every sheet are in `text/` (produced with `xlrd`; time-typed cells
rendered HH:MM, all other cells verbatim).

## Supplementary artifact — New Year's Day 2019

The 2019 ZIP's "new years" sheet covers **31 Dec 2019 → 2 Jan 2020**. The schedule that
governs **1 Jan 2019** is the December-2018 document:

| Local path | URL | Archive capture (UTC) | sha256 |
|---|---|---|---|
| `docs/2019-new-years-compact-JAN2019.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2019-new-years-holiday-schedule-compact.xls | 2018-01-07 04:13:43 | 2684a5f1b3a9f65802f6911ca6089e2cb68c3cdf2520dfaf3cdcf3105328c188 |
| `docs/2019-new-years-full-JAN2019.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2019-new-years-holiday-schedule.xls | 2018-01-06 22:58:28 | 2684…(see shasum.txt) |

Sheet title, verbatim: "CME Group Globex New Years Holiday Schedule: December 31, 2018 - January 2, 2019".

Individually-captured copies of many 2019-2021 per-holiday sheets were also downloaded to
`docs/` (see `list.txt` for the archive timestamp of each); they are byte-identical in
content to the ZIP members and serve as corroboration.

## Per-year member map

`zip2019/globex-trading-schedules/`: 2019-mlk-day-schedule.xls + …-martin-luther-king-holiday-schedule-compact.xls,
2019-presidents-day-schedule.xls + …-compact.xls, 2019-good-friday-schedule.xls + 2019-good-friday-holiday-compact.xls,
2019-memorial-day-schedule.xls + …-compact.xls, 2019-independence-day-schedule.xls + 2019-4th-of-july-holiday-schedule-compact.xls,
2019-labor-day-schedule.xls + …-compact.xls, 2019-thanksgiving-schedule.xls + …-compact.xls,
2019-christmas-holiday-schedule.xls + …-compact.xls, 2019-2020-new-years-holiday-schedule.xls + 2019-new-years-holiday-schedule-compact.xls,
plus `settlement-notices/` PDFs (settlement times — NOT session language; not used to key any row).

`zip2020/`: 2020-mlk-day-schedule.xls + 2020-martin-luther-king-holiday-schedule-compact.xls,
2020-presidents-day-schedule.xls + …-compact.xls, 2020-good-friday-schedule.xls + 2020-good-friday-holiday-compact.xls,
2020-memorial-day-schedule.xls + …-compact.xls, 2020-independence-day-schedule.xls + 2020-4th-of-july-holiday-schedule-compact.xls,
2020-labor-day-schedule.xls + …-compact.xls, 2020-thanksgiving-schedule.xls + …-compact.xls,
2020-christmas-holiday-schedule.xls + …-compact.xls, 2021-new-years-holiday-schedule.xls + …-compact.xls.

`zip2021/`: 2021-mlk-day-holiday-schedule.xls + 2021-mlk-day-schedule-compact.xls,
2021-presidents-day-holiday-schedule.xls + …-compact.xls, 2021-good-friday-holiday-schedule.xls + …-compact.xls,
2021-memorial-day-holiday-schedule.xls + …-compact.xls, 2021-independence-day-holiday-schedule.xls + …-compact.xls,
2021-labor-day-holiday-schedule.xls + …-compact.xls, 2021-thanksgiving-holiday-schedule.xls + …-compact.xls,
2021-christmas-holiday-schedule.xls + …-compact.xls, 2022-new-years-holiday-schedule.xls + …-compact.xls.

## Group naming as CME prints it

Compact sheets use these row labels: **Equity**, **Bitcoin** (renamed **Cryptocurrency** in
the 2021 full sheets), **Interest Rate**, **FX**, **Energy, Metals & DME**,
**Grain & Oilseed**, **Mini-Grain**, **MGEX Wheat / MGEX Indices**, **Dairy**,
**Lumber (Futures&Options)**, **Livestock**. Full sheets add
**Energy, Metals, Softs & DME Products** and per-product exception rows.

**Nikkei:** the compact sheets carry no Nikkei row — the Nikkei 225 futures follow the
"Equity" / "Equity Products" line. The full sheets print a Nikkei line only as a BTIC
trade-type exception ("Nikkei/TOPIX BTIC"), except 2021 Good Friday ("Nikkei BTIC" /
"TOPIX BTIC" split) and 2021 Thanksgiving ("Nikkei & BTIC"). Those verbatim lines are
recorded in the JSON under family `globex_nikkei_225_dollar` and flagged as BTIC-variant
rows, not the outright future.

## Not used to key any row

`settlement-notices/*settlement-times*.pdf` and `*-otc-advisory.pdf`: settlement / OTC
clearing times, not session language (LAW-SESSION-NOT-EXPIRY). Retained inside the ZIPs.

## Fetch tooling

`fetch.sh <archive-ts> <url> <out>` — `https://web.archive.org/web/<ts>id_/<url>` with retry.
`list.txt` — the per-file fetch manifest (archive timestamp | url | local name).
`/tmp/dumpxls.py` — the xlrd dumper (copy in `dumpxls.py`).
