# Channel: portal-hours-page

Archived SGX derivatives **Trading Hours** page on the retired `wps/wcm` portal.
Retrieval date: 2026-09-06. All bytes fetched via `web.archive.org/web/<ts>id_/<url>` (raw replay).

Scope: only sgx.com-authored artifacts under `/wps/` (the WebSphere Portal `wps/portal/...`
navigational pages and the `wps/wcm/connect/...` Web Content Manager fragments).

---

## 1. CDX enumerations (JSON, as returned by web.archive.org/cdx/search/cdx)

| File | Query |
|---|---|
| `cdx_hours_prefix.json` | prefix `sgx.com/wps/wcm/connect/mp_en/site/trading_on_sgx/derivatives_market/derivatives_trading_hours_and_calendar`, 2016-01-01→2020-06-30, collapse=digest. **1 row.** |
| `cdx_wps_hours.json` | prefix `sgx.com/wps/`, 2016→2020-06, `filter=urlkey:.*hours.*`, collapse=digest. 23 rows — the master list of hours-named URLs under /wps/. |
| `cdx_wps_hours_2016_2020.json` | same as above but collapse=urlkey — **the definitive in-window inventory (14 URLs).** |
| `cdx_deriv_full.json` | prefix `…/sgxweb/home/trading/derivatives/trading_hours_calendar`, 2015→2020, no collapse. 5 rows. |
| `cdx_deriv_alltime.json` | same URL, **all time**, no collapse. 14 rows (2013 → 2026). |
| `cdx_commod_alltime.json` | `…/sgxweb/home/trading/commodities/trading_hours_calender`, all time. 5 rows. |
| `cdx_marketplace_full.json` | prefix `…/marketplace/mp-en/trading_on_sgx/derivatives_market`, all time. 4 rows, **all 302**. |
| `cdx_marketplace_all.json` | prefix `sgx.com/wps/portal/marketplace/`, all time, collapse=digest. 54 rows. |
| `cdx_portal_trading_all.json` | prefix `sgx.com/wps/portal/sgxweb/home/trading/`, 2014→2020, collapse=digest. 93 rows. |
| `cdx_sgxwebch_trading.json` | prefix `sgx.com/wps/portal/sgxweb_ch/home/trading`, all time. 16 rows. |
| `cdx_wcm_mpen_trading.json` | prefix `sgx.com/wps/wcm/connect/mp_en/site/trading_on_sgx`, all time, collapse=urlkey. 31 URLs. |
| `cdx_wcm_sgxen_trading.json` | prefix `sgx.com/wps/wcm/connect/sgx_en/home/trading`, all time, collapse=urlkey. 8 URLs. |
| `cdx_wcm_th_alltime.json` | prefix `…/derivatives_trading_hours_and_calendar/Trading+Hours`, all time. 7 rows. |
| `cdx_domain_tradinghours.json` | domain-wide `sgx.com` sweep with hours filter — **returned `[]` (empty); dead end, superseded by `cdx_wps_hours_2016_2020.json`.** |

---

## 2. Retrieved artifacts — GRID-BEARING (equity index rows present)

### `portal_ch_deriv_20170705000242.html`  — 171,571 bytes
`http://sgx.com/wps/portal/sgxweb_ch/home/trading/derivatives/trading_hours_calendar`
Capture **20170705000242** · origin `Date: Wed, 05 Jul 2017 00:02:43 GMT`
Chinese-portal (`sgxweb_ch`) mirror of the derivatives Trading Hours page. English content.
Heading: `Trading Hours* for SGX Derivatives Market`. Granular code/contract grid.
**T+1 close = 4.45 am.** Earliest in-window capture of this grid state.

### `portal_deriv_20170927124017.html`  — 183,389 bytes
`http://www.sgx.com/wps/portal/sgxweb/home/trading/derivatives/trading_hours_calendar`
Capture **20170927124017** · origin `Date: Wed, 27 Sep 2017 12:40:17 GMT`
English portal. **Equity-index grid content is byte-identical to the 2017-07-05 capture.**
Latest in-window capture of this grid state.

### `wcm_tradinghours_20180711020353.html`  — 11,046 bytes
`http://www.sgx.com/wps/wcm/connect/mp_en/site/trading_on_sgx/derivatives_market/derivatives_trading_hours_and_calendar/Trading+Hours?%20noCache=1531274630984.837727.133108399`
Capture **20180711020353** · origin `Date: Wed, 11 Jul 2018 02:03:53 GMT`, `ETag: "561385584"`
Legacy WCM fragment on the older `mp_en` content tree. Heading: `Trading Hours* for SGX Derivatives Market`.
**T+1 close = 2.00 am (following day).** Content is the OLDER regime although captured LATER
than the two 4.45 am captures above. Uses superseded contract names (`FTSE Xinhua China A50`,
`MSCI S'pore`, `S&P CNX Nifty`, `MSCI Asia Apex 50`). Only in-window capture of this URL.

---

## 3. Retrieved artifacts — NO GRID (page had dropped the hours table)

| File | URL / capture | Content |
|---|---|---|
| `portal_deriv_20181020041054.html` | `sgx.com/wps/portal/sgxweb/home/trading/derivatives/trading_hours_calendar` @ **20181020041054** | No hours table. Only: *"For information relating to trading hours, please refer to the SGX calendar 2018 or contract specifications of the applicable product."* + calendar/DTAM PDF links. |
| `portal_deriv_20181223111840.html` | same URL @ **20181223111840** | Same — no table (DTAM 84 of 2018 links). |
| `portal_deriv_20181231134425.html` | same page, `!ut/p/a0/…` portal-state URL @ **20181231134425** | Same digest as 20181223111840. |
| `portal_home_hours_20181231112828.html` | `sgx.com/wps/portal/sgxweb/home/trading_hours_calender/!ut/p/a0/…` @ **20181231112828** | No sessions table. |

---

## 4. Retrieved artifacts — CONTEXT / NOT EQUITY-INDEX

| File | URL / capture | Note |
|---|---|---|
| `portal_commod_20170606094346.html` | `sgx.com/wps/portal/sgxweb/home/trading/commodities/trading_hours_calender` @ **20170606094346** | Commodities-only grid, still on the **2.00 am** T+1 regime. No equity-index rows. |
| `portal_commod_20170927133020.html` | same URL @ **20170927133020** | Same commodities grid, still 2.00 am — i.e. stale alongside the 4.45 am derivatives page captured the same day. |
| `portal_commod_20171005123310.html` | `!ut/p/a0/…` variant @ **20171005123310** | Different digest from the two above; commodities only. |
| `portal_deriv_20130820090335_OUTOFWINDOW.html` | derivatives hours page @ **20130820090335** | **Out of window (2013).** Page at that time carried a *holiday* trading schedule, not the standard grid. |
| `wcm_tradinghours_printerfriendly_20210925205725_OUTOFWINDOW.html` | `…/Trading+Hours?presentationtemplate=design_lib/PT_Printer_Friendly` @ **20210925205725** | **Out of window (2021).** No content — modern-site "unsupported browser" shell. All post-2020 captures of this URL are the same shell, so 20180711 is the last content-bearing capture. |

`archive_headers.txt` — origin (`x-archive-orig-*`) headers for the three grid-bearing captures.
No `Last-Modified` was returned by SGX for any of them; the portal pages send
`Cache-Control: no-cache, no-store, must-revalidate`, so no artifact self-dates its content.

---

## 5. Findings summary

- **Two distinct grid states** appear on this channel inside 2016-01-01 → 2020-06-30.
- State **G1** (granular, T+1 → 4.45 am): captured 2017-07-05 and 2017-09-27, identical.
- State **G2** (legacy, T+1 → 2.00 am): captured 2018-07-11 on the `wps/wcm` fragment.
- The captures are **out of content order**: G2 (older content) was captured a year after G1.
  The two pages coexisted on sgx.com; the `mp_en` WCM fragment was never refreshed.
  **No effective date can be read off either artifact.**
- The **05:15** T+1 close appears **nowhere** on this channel. The portal page stopped
  publishing a grid by 2018-10-20 and 301'd away from 2019-04-19.
- **No NTR / Net Total Return (USD) contract is listed on any capture in this channel.**
