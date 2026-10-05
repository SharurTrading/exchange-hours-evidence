# Channel: calendar-pdfs-2016-2019

Retrieval log for SGX pre-2020 Derivatives Trading Calendar PDFs and the documents the
2018-07-11 portal capture (and its siblings) link to.

Retrieved 2026-09-06. All sources are SGX-authored (`www.sgx.com` / `sgx.com` WebSphere
portal, `api2.sgx.com`), reached live or via the Wayback Machine `id_` raw-byte replay.

---

## 1. Artifacts saved

### HTML — SGX WebSphere portal ("Trading Hours & Calendar", derivatives)

| File | Capture (UTC) | Original URL | What it contains |
|---|---|---|---|
| `20170705000242_sgxweb_ch_deriv_trading_hours_calendar.html` | 2017-07-05 00:02:42 | `http://sgx.com/wps/portal/sgxweb_ch/home/trading/derivatives/trading_hours_calendar` | **FULL inline trading-hours grid** (88 contract rows) + calendar PDF links (SGX Calendar 2016 / 2015, DTAM 80 of 2016 + 2 appendices) |
| `20170927124017_sgxweb_deriv_trading_hours_calendar.html` | 2017-09-27 12:40:17 | `http://www.sgx.com/wps/portal/sgxweb/home/trading/derivatives/trading_hours_calendar` | **FULL inline trading-hours grid** (88 contract rows, byte-identical to the 2017-07-05 grid) + calendar PDF links (SGX Calendar 2017, DTAM 80 of 2016 + appendices i/ii, DTAM 85 of 2016 full-year calendar + appendix) |
| `20181020041054_sgxweb_deriv_trading_hours_calendar.html` | 2018-10-20 04:10:54 | `http://sgx.com/wps/portal/sgxweb/home/trading/derivatives/trading_hours_calendar` | **NO grid.** Grid replaced by: "For information relating to trading hours, please refer to the SGX calendar 2018 or contract specifications of the applicable product." Links: SGX Calendar 2018, SGX Calendar 2017, DTAM 84 of 2017 Year End Trading Schedule (+ appendix 1) |
| `20181223111840_sgxweb_deriv_trading_hours_calendar.html` | 2018-12-23 11:18:40 | `http://www.sgx.com/wps/portal/sgxweb/home/trading/derivatives/trading_hours_calendar` | **NO grid.** Same wording. Links: SGX Calendar 2018, SGX Calendar 2017, DTAM 84 of 2018 Year End Trading Schedule (+ appendix 1) |
| `20180711020353_portal_trading_hours.html` | 2018-07-11 02:03:53 | `http://www.sgx.com/wps/wcm/connect/mp_en/site/trading_on_sgx/derivatives_market/derivatives_trading_hours_and_calendar/Trading+Hours?...` | The stale WCM "Trading Hours" fragment (already known to the repo). Fetched only to extract link targets — it carries **no** PDF links. |
| `20170606094346_sgxweb_commodities_trading_hours_calender.html` | 2017-06-06 09:43:46 | `http://sgx.com/wps/portal/sgxweb/home/trading/commodities/trading_hours_calender` | Dead end: no grid, no calendar/DTAM PDF links. |
| `20181231112828_sgxweb_trading_hours_calender_toplevel.html` | 2018-12-31 11:28:28 | `http://sgx.com/wps/portal/sgxweb/home/trading_hours_calender/!ut/p/a0/...` | Dead end: no grid, no calendar/DTAM PDF links. |
| `20220811234402_wcm_trading_and_clearing_calendar.html` | 2022-08-11 23:44:02 | `https://www.sgx.com/wps/wcm/connect/mp_en/site/.../Trading+and+Clearing+Calendar` | Dead end: by 2022 this replays only the modern SPA shell — no calendar content. |

### PDF — api2.sgx.com

| File | Source | Status |
|---|---|---|
| `LIVE20260906_api2_2020-01_SGX_Derivatives_Trading_Calendar_2020.pdf` | live `https://api2.sgx.com/sites/default/files/2020-01/SGX%20Derivatives%20Trading%20Calendar%202020.pdf`, fetched 2026-09-06 | **Readable.** 16 pp. `/CreationDate D:20200102181432+08'00'`. Front-matter states: "All dates and information are accurate as of 2 January 2020." Carries the "Trading Hours of SGX Futures and Options Contracts" grid. This is the **2020 boundary edition**. |
| `20211216195137_api2_2018-12_Titan_DTDC_Change_of_Trading_Hours.pdf` | wayback `20211216195137id_` of `api2.sgx.com/sites/default/files/2018-12/Titan%20DTDC%20Newsletter%20-%20Change%20of%20Trading%20Hours.pdf` | **PASSWORD-PROTECTED — not opened.** |
| `20211128115601_api2_2018-12_Titan_DTDC_Extended_Trading_Hours_PriceLimits_TAS.pdf` | wayback `20211128115601id_` of `.../2018-12/Titan%20DTDC%20Newsletter%20-%20Extended%20Trading%20Hours%2C%20Price%20Limits%20and%20Trade%20at%20Settlement.pdf` | **PASSWORD-PROTECTED — not opened.** |
| `20211125035043_api2_2019-07_Titan_DTDC_Extension_of_T+1_Trading_Hours.pdf` | wayback `20211125035043id_` of `.../2019-07/Titan%20DTDC%20Newsletter%20-%20Extension%20of%20T%2B1%20Trading%20Hours_0.pdf` | **PASSWORD-PROTECTED — not opened.** |
| `20211216195121_api2_2019-10_Titan_DTDC_Ext_of_T+1_Trading_Hours_Go_Live_Schedule.pdf` | wayback `20211216195121id_` of `.../2019-10/Titan%20DTDC%20Newsletter%20-%20Ext%20of%20T%2B1%20Trading%20Hours%20Go%20Live%20Schedule.pdf` | **PASSWORD-PROTECTED — not opened.** |

Encryption detail for the four Titan DTDC newsletters (identical across all four):
`/Filter /Standard, /V 4, /R 4, /Length 128, /CF /StdCF {/CFM /V2}, /P -1028`.
Empty-password check performed with `pypdf` (`decrypt("") -> 0`), `pikepdf`
(`PasswordError: invalid password`) and `pdftotext -opw "" -upw ""`
(`Command Line Error: Incorrect password`). No further attempt made.
Archived bytes are byte-identical in size to the live files, so the archive replay is not
the problem — the documents themselves are member-gated.

### Derived (my extractions, not primary sources)

| File | Content |
|---|---|
| `DERIVED_20170927124017_grid.tsv` | The 88 grid rows from the 2017-09-27 capture, verbatim: `code / contract / T Session / T+1 Session` |
| `DERIVED_LIVE20260906_SGX_Derivatives_Trading_Calendar_2020_pdftotext.txt` | `pdftotext -layout` of the 2020 calendar PDF |

---

## 2. The one distinct pre-2020 grid state found in this channel

Source: SGX portal page "Trading Hours & Calendar" (derivatives), **captured 2017-07-05 and
again 2017-09-27**. The two captures carry a byte-identical 88-row table — one grid state,
not two. Table title on the page: **"Trading Hours* for SGX Derivatives Market"**.

Rows for the five families in scope (verbatim, including SGX's own inconsistent spacing and
its mixed use of `:` and `.` as the time separator):

| Code | Contracts | T Session | T+1 Session |
|---|---|---|---|
| NK | SGX Nikkei 225 Index Futures | `7.30 am to 2.25 pm` | `2.55 pm to 4.45 am` |
| NKO | SGX Nikkei 225 Index Options | `7.30 am to 2.30 pm` | `2.55 pm to 4.45 am` |
| NS | SGX Mini Nikkei 225 Index Futures | `7.30 am to 2.25 pm` | `2.55 pm to 4.45 am` |
| NU | SGX USD Nikkei 225 Index Futures | `7.30 am to 2.25 pm` | `2.55 pm to 4.45 am` |
| ND | SGX Nikkei Stock Average Dividend Point Index Futures | `7.30 am to 5.55 pm` | `6.25 pm to 4.45 am` |
| CN | FTSE China A50 Index Futures | `9:00 am to 4:30 pm` | `5.00 pm to 4.45 am` |
| SGP | SGX MSCI Singapore Index Futures | `8.30am to 5.10 pm` | `5.40 pm to 4.45 am` |
| SGPO | SGX MSCI Singapore Index Options | `8.30 am to 5.15 pm` | `5.40 pm to 4.45 am` |
| TW | SGX MSCI Taiwan Index Futures | `8.45 am to 1.45 pm` | `2.15 pm to 4.45 am` |
| TWO | SGX MSCI Taiwan Index Options | `8.45 am to 1.50 pm` | `2.15 pm to 4.45 am` |

**No NTR (USD) contract appears anywhere on this page.** The NTR suite is absent from the
2017 grid entirely.

Session-state footnote, verbatim:

> `* All trading hours shown are in Singapore Time (GMT +8) and exclude the pre-opening,
> pre-closing and respective non-cancel session states. Please refer to the full contract
> specifications for details on these session states.`

Full 88-row table is in `DERIVED_20170927124017_grid.tsv`; primary bytes in the two HTML files.

### Why this matters

The T+1 close is already **4.45 am** on 2017-07-05 — i.e. the 02:00 T+1 close on the stale
WCM fragment captured 2018-07-11 was **already superseded by July 2017**. Two SGX-published
states coexisted on sgx.com through 2018: the live portal page (4.45 am) and an orphaned WCM
fragment (2.00 am). The repo's "by 2019-05-31 the T+1 close was already 04:45" is consistent
with, and now pushed back nearly two years by, this evidence.

Between 2017-09-27 and 2018-10-20 SGX **deleted** the grid from the portal page and pointed
readers at the calendar PDF instead. That PDF is the artifact that is now unreachable
(section 4).

---

## 3. The 2020 boundary edition (for comparison, from the readable PDF)

`SGX Derivatives Trading Calendar 2020`, "accurate as of 2 January 2020", page titled
**"Trading Hours of SGX Futures and Options Contracts"**, columns `T SESSION #ˆ` / `T+1 SESSION # ˆ`:

| Contract | T | T+1 |
|---|---|---|
| SGX Nikkei 225 Index Futures | `7.30am to 2.25pm` | `2.55pm to 5.15am` |
| SGX Nikkei 225 Index Options | `7.30am to 2.30pm` | `2.55pm to 5.15am` |
| SGX Mini Nikkei 225 Index Futures | `7.30am to 2.25pm` | `2.55pm to 5.15am` |
| SGX USD Nikkei 225 Index Futures | `7.30am to 2.25pm` | `2.55pm to 5.15am` |
| SGX Nikkei 225 Index Total Return Futures | `7.30am to 2.25pm` | `2.55pm to 5.15am` |
| SGX Nikkei Stock Average Dividend Point Index Futures | `7.30am to 2.25pm` | `2.55pm to 5.15am` |
| SGX FTSE China A50 Index Futures | `9.00am to 4.30pm` | `5.00pm to 5.15am` |
| SGX MSCI Singapore Index Futures | `8.30am to 5.20pm` | `5.50pm to 5.15am` |
| SGX MSCI Singapore Index Options | `8.30am to 5.25pm` | `5.50pm to 5.15am` |
| SGX MSCI Taiwan Index Futures | `8.45am to 1.45pm` | `2.15pm to 5.15am` |
| SGX MSCI Taiwan Index Options | `8.45am to 1.50pm` | `2.15pm to 5.15am` |
| every `... NTR (USD/JPY) Index Futures` row | `7.25am to 6.30pm` | `7.00pm to 5.15am` |

Footnotes, verbatim:

> `# Timings exclude pre-opening and pre-closing routines, the respective non-cancel periods
> as well as the respective order-cancellation session states where applicable. For detailed
> timings, visit https://www2.sgx.com/derivatives/trading.`
>
> `^ NLT registration for all products commence at 7.10am.`
>
> `* Trade registration hours for SGX FlexC FX Futures. After the close of T session, there
> will be a 30-minute grace period for participants to continue registering T session trades.`

---

## 4. Link targets extracted, and their retrieval status (all DEAD)

Every calendar/DTAM PDF linked from the portal captures lives under the retired WebSphere
WCM content store `.../wps/wcm/connect/<uuid>/<filename>?MOD=AJPERES`. **None of them is in
the Wayback Machine and none of them is live.**

From the 2017-09-27 capture:

| Filename as linked | UUID |
|---|---|
| `SGX_Derivatives Trading Calendar Update (Sep 2017).PDF` | `298856d8-0671-438e-8e73-c0d7a2a50d4c` |
| `DTAM 80 of 2016 Year End Trading Schedule_v06.pdf` | `9e0bc7d0-1c90-4a39-a5db-c2e2c08ca7f0` |
| `DTAM 80 of 2016 Trading Calendar_Appendix 1_v07_AK (1).pdf` | `620b6dca-1cb5-4102-92b3-2b1bfcd97f16` |
| `DTAM 80 of 2016 Trading Calendar_Appendix 2_v07_AK.pdf` | `71c3c9b6-5b50-48b7-8a6b-fb690486e743` |
| `DTAM 85 of 2016 Full Year Calendar_2017_v05.pdf` | `1b90517a-09f3-4af2-a1cc-1501d6725a8c` |
| `DTAM 85 of 2016 Full year calendar_Appendix 1_v05.pdf` | `05a51d36-0cc1-4eaa-aba4-bfddd7a14866` |

From the 2017-07-05 (Chinese) capture — three earlier editions not previously known:

| Filename as linked | UUID |
|---|---|
| `SGX Derivatives Trading Calendar 2016_Oct end Update_FA.PDF` | `bce57650-845d-4680-b286-691d46e4efa1` |
| `SGX Derivatives Trading Calendar 2015_Aug Update_FA.PDF` | `5da48629-63a4-41ee-8fa9-b208bfdfe961` |
| `SGX Derivatives Trading Calendar 2014 - Oct 2014 update_D1.pdf` | `e036cd33-309f-4dec-b753-3a18ac6aeaf9` |

From the 2018-10-20 capture:

| Filename as linked | UUID |
|---|---|
| `SGX Derivatives Trading Calendar 2018  (Apr Update).pdf` (two spaces before `(Apr`) | `52f39ede-508b-47dc-9a43-19b8f2748fc4` |
| `DTAM 84 Year End Trading Schedule.pdf` | `ff6ee815-3526-4d1d-9a34-50bf35905c69` |
| `DTAM 84 2017 Trading Calendar - Appendix 1 .pdf` | `0e34f180-31c0-4064-b1c5-cc559d14effa` |

From the 2018-12-23 capture:

| Filename as linked | UUID |
|---|---|
| `DTAM 84 of 2018 - Trading Schedules for Year End 2018_New Year Day 2019.pdf` | `2edf7596-b337-4d2d-ab19-eabf72240661` |
| `DTAM 84 of 2018 Trading Calendar Appendix 1.pdf` | `5422f1b5-328a-4549-a6d7-62085e40435c` |

### Evidence that these are dead

- CDX `url=sgx.com/wps/wcm/connect/<uuid>&matchType=prefix` → `[]` for all 13 UUIDs.
- CDX `url=sgx.com/wps/wcm/connect/&matchType=prefix&from=2014&to=2022&filter=urlkey:.*pdf.*`
  returns 373 archived WCM PDFs; **none** matches `calendar|dtam|circular|trading.?hour|schedule|holiday`.
- CDX `url=sgx.com&matchType=domain&from=2016&to=2020&filter=urlkey:.*calendar.*` → 16 rows,
  no calendar PDF.
- Live probe of the WCM URLs returns HTTP 200 `text/html` 11 792 bytes (the modern SPA 404
  shell), not a PDF.
- `api2.sgx.com` CDX (2016-2025) `filter=urlkey:.*calendar.*` → 7 rows, earliest `2020-01`.
  No 2016/2017/2018/2019 edition was ever re-hosted on api2 under a name containing "calendar".
- Live brute-probe of plausible api2 paths for a 2019 edition
  (`2018-12|2019-01|…|2020-01` × `SGX Derivatives Trading Calendar 2019.pdf`,
  `SGX_Derivatives Trading Calendar 2019.pdf`, `DT Trading Calendar 2019.pdf`,
  `SGX Derivatives Trading Calendar 2019 (Final).pdf`) → all 404.
- `infopub.sgx.com` CDX filtered for `dtam|calendar|trading.?hour` → only listed-company
  financial calendars, no DTAM.
- `sgx.com/wps/wcm/myconnect/` prefix → 5 rows, all images.

### DTAM circulars found in the archive, all POST-window

Only these DTAM circulars survive on api2, and every one is 2022 or later, so none of them
bears on 2016-2019 trading hours:
`DTAM 67 of 2022`, `DTAM 64 of 2023`, `DTAM 93 of 2023`, `DTAM 6 of 2024 Appendix1`,
`DTAM 87 of 2024`, `DTAM 24 of 2025` (+ Appendix A), `DTAM 25 of 2024 Appendix A`,
`DTAM 36 of 2024 Appendix A`. **No pre-2020 DTAM circular is retrievable from any SGX host.**

---

## 5. Method / reproducibility

Helpers used (in `/tmp`, recreate as needed):

- `wbfetch.sh <url> <out> [tries]` — curl with retry/backoff, requires HTTP 200 and >500 bytes.
- `cdxq.sh "<cdx query string>"` — CDX with retry; treats the Internet Archive
  "Temporarily Offline" HTML page as a retryable failure (it fired repeatedly on 2026-09-06).
- Raw bytes always via the `…/web/<timestamp>id_/<url>` replay form.

PDF handling: `pdftotext -layout` first, then `pypdf`, then `pikepdf`. Empty-password check
only; no password cracking attempted.
