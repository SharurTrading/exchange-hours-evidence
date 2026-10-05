# SGX pre-2020 — channel `contract-sets-and-boundaries`

Retrieved 2026-09-06 (all fetch timestamps in file names are UTC). Question answered:
**for each modelled SGX equity-index family, what is the earliest 2016-2020 SGX-authored
artifact that LISTS that exact contract, and where does each rebrand/launch first appear?**

Only sgx.com / api2.sgx.com / www2.sgx.com and the archived `wps/wcm` + `wps/portal`
portal count as sources. No broker or member material is used here.

---

## 1. Primary artifacts (SGX-authored, in the 2016-2020 window)

| file | what it is | artifact date | capture |
| --- | --- | --- | --- |
| `WB-20170705000242-portal-CH-derivatives-trading_hours_calendar.html` | SGX portal `sgxweb_ch/home/trading/derivatives/trading_hours_calendar`. Carries the full inline **"Trading Hours* for SGX Derivatives Market"** table, 88 coded contracts, English contract names. Also links "SGX Calendar 2016", "SGX Calendar 2015", "SGX Derivatives Trading Calendar 2014". | page, undated | wayback 20170705000242 |
| `WB-20170927124017-portal-trading_hours_calendar.html` | Same page, English portal (`sgxweb/...`). **Its hours table is byte-identical to the 2017-07-05 one** (see `*.hours.json`, diff clean). Links the Sep-2017 calendar update + DTAM 80/85 of 2016. | page, undated | wayback 20170927124017 |
| `WB-20170914065739-sgx-newsrelease-NTR-launch.html` | SGX news release **"SGX launches Net Total Return futures for key emerging markets in Asia"**, page-dated **12 Jun 2017**. Names the four launch NTR contracts. | 2017-06-12 | wayback 20170914065739 |
| `WB-20171113181129-sgx-newsrelease-MSCI-EM-derivatives.html` | SGX news release **"SGX leads with new derivatives on MSCI Emerging Markets indices"**, page-dated **13 Nov 2017**. NTR + price-return futures on MSCI EM / EM Asia. | 2017-11-13 | wayback 20171113181129 |
| `LIVE-20260906T012852Z-api2-2018-05-SGX-Derivatives-Trading-Calendar-2018-Apr.pdf` | **SGX Derivatives Trading Calendar 2018 (Apr)**, `api2.sgx.com/sites/default/files/2018-05/...`. STILL LIVE. Cover "Trading Calendar 2018"; p2 "All dates and information are accurate as of 26 December 2017"; PDF `/CreationDate D:20180411152616+08'00'`; monthly pages Jan-Dec 2018; p16 "Legend & Calendar 2019" (next-year look-ahead). p15 = "Trading Hours of SGX Futures and Options Contracts". | 2018-04-11 | LIVE (fetched 2026-09-06) |
| `LIVE-20260906T012852Z-api2-2019-01-2019-DT-Calendar.pdf` | **SGX Derivatives Market Trading Calendar 2019**, `api2.sgx.com/sites/default/files/2019-01/2019 DT Calendar.pdf`. STILL LIVE. p2 "accurate as of 15 January 2019"; `/CreationDate D:20190122175553+08'00'`. Hours table spans pp. 15-16. | 2019-01-22 | LIVE |
| `LIVE-20260906T012852Z-api2-2020-01-SGX-Derivatives-Trading-Calendar-2020.pdf` | **SGX Derivatives Trading Calendar 2020**. p2 "accurate as of 2 January 2020". | 2020-01-02 | LIVE |
| `LIVE-20260906T014748Z-api2-2021-01-SGX-Derivatives-Trading-Calendar-2021.pdf` | **SGX Derivatives Trading Calendar 2021** — fetched only to date the FTSE Taiwan / FTSE Singapore boundary. | 2021 | LIVE |
| `WB-20181030153306-portal-chinaa50-contracts.html` | SGX portal contract-specification page, `.../products/derivatives/financials/equity-index/chinaa50/contracts`. Product Name **"SGX FTSE China A50 Index Futures"**, ticker CN, with full Pre-Opening / Non-Cancel / Opening / Pre-Closing routines for T and T+1. | page, undated | wayback 20181030153306 |
| `WB-20180921013146-SGX-Monthly-Market-Statistics-Feb2017.pdf` | **SGX Monthly Market Statistics Report - February 2017**. Volume tables naming (short forms) "FTSE China A50 Index Futures", "Nikkei 225 Index Futures", "MSCI Singapore Index Futures", "MSCI Taiwan Index Futures". No NTR rows. No hours. | 2017-02 | wayback 20180921013146 |
| `WB-20201030164207-sgx-media-20200701-ftse-taiwan-zh.html` + `LIVE-20260906T014802Z-sgx-media-20200701-ftse-taiwan-EN.html` | SGX media-centre release **"SGX to introduce SGX FTSE Taiwan Index Futures"**, `dateArticle` 1593532800 = **2020-07-01 SGT**. Body (zh) states launch **20 July 2020**. English `metaDescription`: "SGX is launching SGX FTSE Taiwan Index futures…". The EN page is live but serves an empty SPA shell; the zh capture carries the `_sgxComApp_pageData` JSON body. | 2020-07-01 | wayback 20201030164207 / LIVE |
| `WB-20200904174251-sgx-media-20200820-ftse-russell.html` | SGX media-centre release, 2020-08-20, SGX + FTSE Russell partnership; mentions the Aug-2020 plan for "Asia Ex-Japan and Emerging Markets Asia regional and single country futures based on Net Total Return and Price Return indices calculated by FTSE Russell". | 2020-08-20 | wayback 20200904174251 |

## 2. Context / control artifacts (outside the window, or negative evidence)

| file | why it is here |
| --- | --- |
| `WB-20130820090335-portal-trading_hours_calendar.html` | 2013-08-20 capture of the same portal page. Already names **"SGX FTSE China A50 Index Futures"** — so the "FTSE Xinhua China A50" wording on the 2018-07-11 orphan page is pre-2013 content. Its hours table: A50 9.00am-3.55pm / 4.40pm-2.00am, Nikkei 225 7.45am-2.25pm / 3.15pm-2.00am, MSCI Singapore 8.30am-5.10pm / 6.15pm-2.00am, MSCI Taiwan 8.45am-1.45pm / 2.35pm-2.00am. |
| `WB-20180711020353-portal-derivatives-Trading-Hours.html` | The `wps/wcm/.../Trading+Hours` page the issue quotes. **Its contract set proves it is stale**: Euroyen LIBOR, 3-Month Singapore Interest Rate, 5-Year SGS, MSCI Hong Kong+, MSCI Asia Apex 50, SGX EURO STOXX 50, LME-SGX Copper/Aluminium/Zinc, "S&P CNX Nifty", CPO Futures, "FTSE Xinhua China A50". No FX pair, no iron ore, no NTR. This is a ~2012 contract set frozen on an orphaned page; SGX's own live portal page in 2017 and its own 2018 calendar both state a different grid. |
| `WB-20181020041054-portal-trading_hours_calendar.html`, `WB-20181223111840-portal-trading_hours_calendar.html` | Same portal page in Oct/Dec 2018: **the inline hours table has been removed**. The Dec-2018 copy says "For information relating to trading hours, please refer to the SGX calendar 2018 or contract specifications of the applicable product." That is when SGX moved hours publication into the calendar PDFs. |
| `WB-20190116144452-sgx-product-chinaa50.html`, `WB-20190922123749-sgx-product-nikkei225-NK.html`, `WB-20190930120921-sgx-product-sgxsimsci-SGP.html`, `WB-20200924231643-sgx-product-sgxsimsci.html` | New-site (`www.sgx.com/derivatives/products/...`) captures. **All are empty SPA shells** — the content API response was not archived. No evidentiary value; kept so the negative is reproducible. |

## 3. Derived files

- `*.hours.json` — the parsed 2017-07-05 and 2017-09-27 hours tables (code / contract / T / T+1). The two are identical.
- `*.layout.txt`, `cal2019.txt`, `cal2020.txt`, `cal2021.txt` — `pdftotext -layout` dumps of the calendars.
- `cdx_*.json` — every CDX enumeration run, kept so the negatives below are reproducible.
- `products_list.txt` — filtered CDX listing of SGX product pages.
- `fetch.sh` — retry-with-backoff fetch helper (Wayback was intermittently refusing connections).

---

## 4. Hard negatives (verified, not assumed)

1. **No SGX derivatives trading-hours page is archived for any date in 2016.** `cdx_th_2015_2019.json`
   enumerates every `sgx.com` URL matching `trading.hours` captured 2015-2019: the derivatives page
   appears at 2013-08-20, then not again until 2017-07-05 (zh) / 2017-09-27 (en).
2. **The 2016 and 2017 calendar PDFs are unreachable.** The 2017-07-05 portal page links
   `SGX+Derivatives+Trading+Calendar+2016_Oct+end+Update_FA.PDF`,
   `SGX+Derivatives+Trading+Calendar+2015_Aug+Update_FA.PDF`, `DTAM+80+of+2016+*`,
   `DTAM+85+of+2016+Full+Year+Calendar_2017_v05.pdf` and
   `SGX_Derivatives+Trading+Calendar+Update+(Sep+2017).PDF`. **None is in the Wayback Machine**
   (per-URL CDX: zero rows each) and all `www.sgx.com/wps/wcm/connect/...` paths now return the
   11,792-byte SPA shell. Guessed `api2.sgx.com/sites/default/files/<YYYY-MM>/` paths for them all 404.
3. **The 2018 and 2019 calendar editions ARE live on api2.sgx.com but are NOT in the Wayback Machine.**
   `cdx_api2_cal2.json` (api2 domain, filename matching `calendar`) returns 2020, 2021-01, 2021-07,
   2022-06, 2024, 2025-07 only. This reconciles the earlier "earliest archived edition is 2020"
   negative with the "a 2019-01 calendar exists" claim: both are true, of different channels.
4. **`SGX Monthly Market Statistics Report - Mar 2016.pdf` is listed in CDX but its only capture
   (2022-01-20) returns the SPA shell**, not the PDF. The Feb-2017 report (captured 2018-09-21,
   while the wcm path still worked) is the earliest monthly report that actually replays.
5. **No SGX news release announcing the Japan / Singapore / Australia NTR (USD) contracts is archived.**
   `cdx_newsreleases.json` (411 rows) contains only the 2017-06-12 and 2017-11-13 NTR releases.
6. **No `SGX FTSE Taiwan Index Futures` product page is archived** — `cdx_ftsetaiwan_prod.json`
   returns only media-centre and market-update articles.

---

## 5. Findings, in one page

### 5.1 The 2018-07-11 portal capture cannot be read as a 2018 grid state
Its contract set is a ~2012 one (see §2). Two SGX artifacts contradict it from inside the window:
the SGX portal's own `trading_hours_calendar` page on **2017-07-05** and the **2018 (Apr) calendar**
both state Nikkei 225 T 7.30am-2.25pm and a T+1 close of **4.45am** — not 7.45am-2.25pm / 2.00am.
The `wps/wcm/.../Trading+Hours` URL is an orphan leaf of the retired portal; the live page the
navigation actually pointed at is `wps/portal/sgxweb/home/trading/derivatives/trading_hours_calendar`.

### 5.2 Per-family knowledge boundary (earliest in-window SGX artifact LISTING the contract)

| modelled family | exact name as SGX prints it | earliest in-window artifact naming it | earliest in-window artifact naming it **with hours** |
| --- | --- | --- | --- |
| Japan / Nikkei 225 | `SGX Nikkei 225 Index Futures` (NK) | SGX Monthly Market Statistics Report Feb 2017 (as "Nikkei 225 Index Futures") | **portal capture 2017-07-05** — `7.30 am to 2.25 pm` / `2.55 pm to 4.45 am` |
| China / FTSE China A50 | `SGX FTSE China A50 Index Futures` (CN) | Feb 2017 stats report (as "FTSE China A50 Index Futures") | **portal capture 2017-07-05**, printed there without the SGX prefix as `FTSE China A50 Index Futures` — `9:00 am to 4:30 pm` / `5.00 pm to 4.45 am`. First in-window artifact using the full modelled name `SGX FTSE China A50 Index Futures`: the **2018 (Apr) calendar**; the 2018-10-30 contract-spec page repeats it. |
| Singapore / SiMSCI | `SGX MSCI Singapore Index Futures` (SGP) | Feb 2017 stats report | **portal capture 2017-07-05** — `8.30am to 5.10 pm` / `5.40 pm to 4.45 am` |
| Taiwan — MSCI predecessor | `SGX MSCI Taiwan Index Futures` (TW) | Feb 2017 stats report | **portal capture 2017-07-05** — `8.45 am to 1.45 pm` / `2.15 pm to 4.45 am` |
| Taiwan — FTSE successor (the modelled family) | `SGX FTSE Taiwan Index Futures` (TWN) | **SGX media release 2020-07-01**, launch stated as 20 July 2020 | **2021 calendar** — `8.45am to 1.45pm` / `2.15pm to 5.15am`. Absent from the 2020 calendar (published 2020-01-02, six months before launch). |
| NTR (USD) suite | `SGX MSCI <country> NTR (USD) Index Futures` | **SGX news release 2017-06-12** — four contracts, no hours | **2018 (Apr) calendar** — every NTR row `7.25am to 6.30pm` / `7.00pm to 4.45am`. The suite is **absent from both 2017 portal captures**, which list 88 contracts and no NTR row at all, even though four NTR contracts had launched on 12 Jun 2017. |

### 5.3 Rebrands and launches, first appearance

- **FTSE Xinhua China A50 -> FTSE China A50**: already "SGX FTSE China A50 Index Futures" in the
  2013-08-20 portal capture. The rebrand is **pre-window**; "FTSE Xinhua" survives only on the
  orphaned `Trading+Hours` page.
- **"SGX MSCI Singapore Index Futures" <-> "SGX MSCI Singapore Free Index Futures"**: SGX oscillated.
  2017 portal = `SGX MSCI Singapore Index Futures`; 2018 (Apr) and 2019 calendars =
  `SGX MSCI Singapore Free Index Futures`; 2020 and 2021 calendars = `SGX MSCI Singapore Index Futures`.
  Code SGP throughout. **This is a naming change only, not a contract change.**
- **There is no FTSE successor to SiMSCI.** The 2021 calendar — the first edition after the MSCI
  licence expiry that removed every other MSCI-branded SGX index contract — still lists
  `SGP SGX MSCI Singapore Index Futures`, `SGPO SGX MSCI Singapore Index Options` and
  `NSP SGX MSCI Singapore NTR (USD) Index Futures`, while the Taiwan slot has become
  `TWN SGX FTSE Taiwan Index Futures` / `FNTW SGX FTSE Taiwan NTR (USD) Index Futures` and MSCI Taiwan
  is gone entirely. The premise "MSCI Singapore -> FTSE successor" is false; the Singapore family
  kept MSCI branding.
- **NTR (USD) suite launch**: SGX news release 12 Jun 2017 names, verbatim and numbered,
  "1. SGX MSCI Taiwan Net Total Return (USD) Index Futures; 2. SGX MSCI China Free Net Total Return
  (USD) Index Futures; 3. SGX MSCI India Net Total Return (USD) Index Futures; and 4. SGX MSCI
  Indonesia Net Total Return (USD) Index Futures." The 13 Nov 2017 release adds MSCI EM and MSCI EM Asia.
  `NSG SGX MSCI Singapore Free NTR (USD) Index Futures` — one of the two codes the crate's NTR key
  names — first appears in the **2018 (Apr) calendar**; `NSP SGX MSCI Singapore NTR (USD) Index Futures`
  first appears in the **2020** calendar.
- **FTSE-branded NTR**: `FNTW SGX FTSE Taiwan NTR (USD) Index Futures` and `FAXJ SGX FTSE Asia ex Japan
  Index Futures` first appear in the **2021** calendar; the 2020-08-20 media release foreshadows them.

### 5.4 Grid states this channel incidentally pinned (for the hours channels)

Four distinct states appear across the artifacts read here:

| state | artifacts | Japan T / T+1 | China T / T+1 | SiMSCI T / T+1 | Taiwan T / T+1 | NTR T / T+1 |
| --- | --- | --- | --- | --- | --- | --- |
| pre-window | 2013-08-20 portal | 7.45am-2.25pm / 3.15pm-2.00am | 9.00am-3.55pm / 4.40pm-2.00am | 8.30am-5.10pm / 6.15pm-2.00am | 8.45am-1.45pm / 2.35pm-2.00am | (none) |
| A | portal 2017-07-05 **and** 2017-09-27 (byte-identical tables) | 7.30 am to 2.25 pm / 2.55 pm to 4.45 am | 9:00 am to 4:30 pm / 5.00 pm to 4.45 am | 8.30am to 5.10 pm / 5.40 pm to 4.45 am | 8.45 am to 1.45 pm / 2.15 pm to 4.45 am | (not listed) |
| B | calendar 2018 (Apr); calendar 2019 | 7.30am to 2.25pm / 2.55pm to 4.45am | 9.00am to 4.30pm / 5.00pm to 4.45am | 8.30am to 5.10pm / 5.40pm to 4.45am | 8.45am to 1.45pm / 2.15pm to 4.45am | 7.25am to 6.30pm / 7.00pm to 4.45am |
| C | calendar 2020 | 7.30am to 2.25pm / 2.55pm to 5.15am | 9.00am to 4.30pm / 5.00pm to 5.15am | 8.30am to 5.20pm / 5.50pm to 5.15am | 8.45am to 1.45pm / 2.15pm to 5.15am | 7.25am to 6.30pm / 7.00pm to 5.15am |

State A and state B agree on every modelled bound. So **between 2017-07-05 and the 2019 edition
(2019-01-22) SGX published one and only one grid for these four families** — which means the
sourced intersection over that whole stretch is that grid, not a degraded one. The only two moves
between state A and state C are the SiMSCI T-close 5.10pm->5.20pm with its T+1 open 5.40pm->5.50pm,
and the universal T+1 close 4.45am->5.15am.

Footnote convention, verbatim, on the 2018/2019/2020 calendars:
"# Timings exclude pre-opening and pre-closing routines, the respective non-cancel periods as well
as the respective order-cancellation session states where applicable. For detailed timings, visit
https://www2.sgx.com/derivatives/trading." (the 2018 edition ends "visit
sgx.com/derivativestradingcalendar" instead).
On both 2017 portal captures: "* All trading hours shown are in Singapore Time (GMT +8) and exclude
the pre-opening, pre-closing and respective non-cancel session states. Please refer to the full
contract specifications for details on these session states."

Caveat: the 2019 edition marks its columns "T SESSION #ˆ" / "T+1 SESSION # ˆ" but **prints no `ˆ`
footnote anywhere in the document** — a dangling reference. Only the `#` note exists.
