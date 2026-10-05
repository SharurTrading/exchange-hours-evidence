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
| `docs/2020-holiday-calendars.zip` | https://www.cmegroup.com/tools-information/holiday-calendar/files/2020-holiday-calendars.zip | **2026-07-30 11:18:34** (ts `20260730111834`; the only capture the archive holds) — operator `Last-Modified: Tue, 29 Dec 2020 21:32:10 GMT`; ZIP members dated 2020-12-29 | 5263a4a5e9076bc0e69c7cd0e3fd9f82dc4d80b66f1b56f14070f08c1d762b59 |
| `docs/2021-holiday-calendars.zip` | https://www.cmegroup.com/tools-information/holiday-calendar/files/2021-holiday-calendars.zip | **2026-08-30 10:03:27** (ts `20260830100327`; the only capture the archive holds) — operator `Last-Modified: Mon, 03 Jan 2022 21:29:08 GMT`; ZIP members dated 2022-01-03 | 0ee0860a3a0e035eb9d079419aca3cafcc4256d296fa916647987c396dda8c59 |

Extracted to `zip2019/globex-trading-schedules/`, `zip2020/`, `zip2021/`.
Plain-text dumps of every sheet are in `text/` (produced with `xlrd`; time-typed cells
rendered HH:MM, all other cells verbatim).

## Supplementary artifact — New Year's Day 2019

The 2019 ZIP's "new years" sheet covers **31 Dec 2019 → 2 Jan 2020**. The schedule that
governs **1 Jan 2019** is the December-2018 document:

| Local path | URL | Archive capture (UTC) | sha256 |
|---|---|---|---|
| `docs/2019-new-years-compact-JAN2019.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2019-new-years-holiday-schedule-compact.xls | 2018-01-07 04:13:43 | 2684a5f1b3a9f65802f6911ca6089e2cb68c3cdf2520dfaf3cdcf3105328c188 |
| `docs/2019-new-years-full-JAN2019.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2019-new-years-holiday-schedule.xls | 2018-01-06 22:58:28 | 6eafe7ee71c676299bd612eb3760d23d449c2111be8cee463d24308959e4d170 |

Sheet title, verbatim: "CME Group Globex New Years Holiday Schedule: December 31, 2018 - January 2, 2019".

Individually-captured copies of many 2019-2021 per-holiday sheets were also downloaded to
`docs/` (see `list.txt` for the archive timestamp of each); with the one exception recorded under
"Failed retrievals" below, they are byte-identical in content to the ZIP members and serve as
corroboration.

## Failed retrievals (corrected 2026-09-12 UTC — verifier discrepancy D2)

`docs/2020-good-friday-holiday-compact.xls` is **not a CME document**. It is 4,749 bytes of HTML —
`<!DOCTYPE html> … <title>Wayback Machine</title> … The Wayback Machine has not archived that URL` —
sha256 `2c10f98451635b204f24db82793e079dd4c806568333ff04137f154f6e8db1a2`. A fresh CDX query on that
exact URL returns `[]`, and a 224-row prefix crawl of `…/holiday-calendar/files/` for 2019-2023 shows
no standalone 2020 Good Friday `.xls` under any name (only `2020-good-friday-advisory.pdf`), so the
retrieval could never have succeeded. The file is retained unaltered so that `shasum.txt` still
verifies 86/86; it is a record of a failed fetch and **sources nothing**. The genuine 2020 Good Friday
compact sheet is the ZIP member `zip2020/2020-good-friday-holiday-compact.xls`, sha256
`aa0936e9278904f40bc23abba57c2c379207af49d0cb6971f07289010fe1745e`, which is what every 2020 Good
Friday row in the result cites.

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

**Nikkei (corrected 2026-09-12 UTC — verifier discrepancies D1, D4):** the compact sheets carry no
Nikkei row — the Nikkei 225 futures follow the "Equity" / "Equity Products" line, and that line is
what every `globex_nikkei_225_dollar` row records. **Most** full sheets print a Nikkei line as a BTIC
trade-type exception ("Nikkei/Topix BTIC" or "Nikkei/ TOPIX BTIC"), with 2021 Good Friday splitting it
("Nikkei BTIC" / "TOPIX BTIC") and 2021 Thanksgiving printing "Nikkei & BTIC". **Three sheets print no
Nikkei-labelled row at all** and must not be described as if they did:

- `2019-new-years-holiday-schedule.xls` (the DEC-2018 sheet governing 1 Jan 2019) — no Nikkei row and
  no TOPIX row; its Equity exception rows are US Equity BTIC's & FTSE Emerging BTIC, FTSE Developed
  Euro BTIC, E-mini FTSE China 50 BTIC, E-mini FTSE BTIC, S&P CNX Nifty (Nifty 50).
- `2019-mlk-day-schedule.xls` — the string "Nikkei" does not occur; row 11 is "Topix BTIC".
- `2020-mlk-day-schedule.xls` — the string "Nikkei" does not occur; row 11 is "TOPIX BTIC".

A TOPIX BTIC row is not a Nikkei row. These BTIC lines are trade-type variants, not the outright future.

## Not used to key any row

`settlement-notices/*settlement-times*.pdf` and `*-otc-advisory.pdf`: settlement / OTC
clearing times, not session language (LAW-SESSION-NOT-EXPIRY). Retained inside the ZIPs.

## Fetch tooling

`fetch.sh <archive-ts> <url> <out>` — `https://web.archive.org/web/<ts>id_/<url>` with retry.
`list.txt` — the per-file fetch manifest (archive timestamp | url | local name).
`/tmp/dumpxls.py` — the xlrd dumper (copy in `dumpxls.py`).

## Addendum, 2026-09-12 UTC — supplementary hash manifest (verifier discrepancy D8)

`shasum.txt` covers the 86 CME documents and ZIP extractions. These files were relied on for
enumeration and tooling but were not hashed or tabulated in the first round. Hashes re-computed
by the fixer on 2026-09-12 UTC:

| File | What it is | sha256 |
|---|---|---|
| `page-20191206230021.html` | archived `holiday-calendar.html`, capture 2019-12-06 23:00:21 UTC | 0e35326340d7d1328f69c040a3ac0d8014f19b0a1016607246a9c9973905f77c |
| `page-20200326083500.html` | archived `holiday-calendar.html`, capture 2020-03-26 08:35:00 UTC | d8af4d6ebd0ee9e54302e4097b27d9d08653f9470686020c176d644caf12009c |
| `page-20200420113115.html` | archived `holiday-calendar.html`, capture 2020-04-20 11:31:15 UTC | 2f204a3104be3bb98e76914e16962c8494fc475305b99eb07b8a8951ef524a85 |
| `page-20200611060720.html` | archived `holiday-calendar.html`, capture 2020-06-11 06:07:20 UTC | 53d488146a44308cfe9bfefbfa54c43b5e0564d635e3db84250a7b3864715f41 |
| `cdx-hc.json` | CDX, `holiday-calendar*` | d86ed55dac9fe280f0f2c137180bebf6052f179affa25ba38277459224d84bf1 |
| `cdx-files.json` | CDX, `…/holiday-calendar/files/` prefix | 15442d051e6fccb25583f388665a8643f0a54052e216a03845f5c4bce2e93baa |
| `cdx-tradinghours.json` | CDX, `trading-hours*` | 25ecc8f8f0fe8c9eca6f4482a43651a80254abb065b6486009eea8882ad67685 |
| `cdx-hcpage.json` | CDX, `holiday-calendar.html` snapshots | d8170b888770f8d0606113165b2f5bd25383dc737b4b5789926587e521c1a66c |
| `cdx-holiday-calendar.json` | CDX, `holiday-calendar` exact | e084d527921708642a79724e9f0210da659bbc0905c6ce9a3a1f416e4628091c |
| `cdx-faac8fd6.json` | CDX, empty result (`[]`, 3 bytes) | 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 |
| `t1.xls` | **a scratch duplicate**, byte-identical to `docs/2021-presidents-compact.xls`; sources nothing | 7a8d5ce35c639998abf64723de2cc2d649dc015b1aa6cfc3bc326ab5cdfd0c4f |
| `list.txt` | per-file fetch manifest for `docs/` | 7dcbcc13c235133624dbde5387c5cdd2db5e60f8a429fdf5c427d36f43d19803 |
| `dumpxls.py` | the xlrd dumper | f7a1a60d30903fac482c7e5b06f2bc0adab33c44a0fb578a82f7009aa097f209 |
| `fetch.sh` | the id_-replay fetch wrapper | fc13110c3c4f298fc91be58c6c30b92e847652ab1728c1063304908c7b01758f |

`list.txt` omitted three `docs/` files. Their capture times, from fresh per-URL CDX queries saved in
`../cme-2019-2021-fix/cdx/`:

| File | Capture (UTC) | Note |
|---|---|---|
| `docs/2020-mlk-day-schedule.xls` | 2026-08-15 19:42:02 (ts `20260815194202`, the only capture) | byte-identical to `zip2020/2020-mlk-day-schedule.xls` (`51ab36645ea68133de299f9c849f1361521399eb1334d55cc1a6d28de0faeb5b`) |
| `docs/2020-martin-luther-king-holiday-schedule-compact.xls` | 2025-08-27 08:21:54 (ts `20250827082154`, the only capture) | byte-identical to `zip2020/2020-martin-luther-king-holiday-schedule-compact.xls` (`bacf30ad37e6843f7162a6457e17dec7e0024474e9b8e0d35f9ef12fc9671d25`) |
| `docs/2020-good-friday-holiday-compact.xls` | — no capture exists | failed retrieval; see "Failed retrievals" above |

The round-1 copy of this file, before these corrections, is preserved as `INDEX.r0.md`.
