# ag-crypto-tas-history — pass 2 capture index

Gate: `ag-crypto-tas-history` (U-13 / U-14 / U-15).
Pass-2 capture window: 2026-09-06T06:58:55Z – 2026-09-06T07:2x Z (see `CAPTURE-START.txt`).
Per-file sha256 in `SHA256SUMS.txt`. Capture timestamps date the observation, never the state.

Retrieval routes used: (a) the public text reader in front of cmegroup.com
(`https://r.jina.ai/<url>`) — cmegroup.com is 403 direct from this machine; (b) the web archive
CDX + `id_` replay. Archived `/CmeWS/` replies come back gzip-encoded; each `*.json` is the raw
archived body and each `*.json.txt` is the gunzipped bytes actually quoted.

## New channel opened on this pass: the TAS products exist in CME's own product slate

| file | URL | notes |
|---|---|---|
| `slate-ag-group2.txt` | `/CmeWS/mvc/ProductSlate/V2/List?...&group=2` | Agriculture. Yields the nine ag TAS productIds: 7891 ZCT, 7892 SBT, 7893 ZWT, 7894 KET, 7897 ZLT, 7898 ZMT, 7900 LET, 7901 GFT, 7902 HET |
| `slate-crypto-group16.txt` | `...&group=16` | Cryptocurrencies. Eight crypto TAS productIds: 10319 TBT, 10320 TBM, 11069 TET, 11070 TEM, 11382 TSL, 11383 TMS, 11419 TXP, 11420 TMX |

## CME trading-hours service — resolves every TAS product, publishes no events for any of them

| file | URL | result |
|---|---|---|
| `th-all-tas-thx.txt` | `/services/trading-hours-by-product?id=<17 TAS ids>&...&fromEventDate=2026-11-25&toEventDate=2026-11-27` | All 17 resolve with `globex` + `prodGroup`: ZCT/TP, SBT/TA, ZLT/TA, ZMT/TA, ZWT/TW, KET/TW; LET/TH, GFT/TH, HET/TH; TBT/CI, TBM/CI, TET/CM, TEM/CM, TSL/LT, TMS/LT, TXP/XQ, TMX/XQ. `"hasEvents":false`, `eventCount:0` for every one |
| `th-control-thx.txt` | same window, `id=133,300,8478` | CONTROL: ZC returns `paused@07:45 preopen@08:00 open@08:30 paused@13:20 closed@13:30 pcp@14:30 closed@16:00 preopen@16:45`; BTC returns `closed@16:00 preopen@16:01 open@16:02`. The endpoint works; the TAS ids are simply empty |
| `th-7891-sep.txt`, `th-7900-sep.txt`, `th-10319-sep.txt` | current week | empty |
| `th-10319-cutover.txt` | `id=10319`, 2026-05-24…2026-06-02 | empty — the service keeps no history, so it cannot witness the crypto TAS book on cutover day |
| `cs-7891.txt`, `cs-7900.txt`, `cs-10319.txt` | `/CmeWS/mvc/ContractSpecs/List/productId/<TAS id>` | all-`"-"` skeletons: the TAS books have no ContractSpecs page of their own; the slate points them at the underlying's page |

## The underlying's ContractSpecs page prints the TAS window — a dated series

| file | artifact date | quoted line |
|---|---|---|
| `cs-300-live.txt` | live, captured 2026-09-06 | Corn, `"venue":"CME Globex:"` → `Monday - Friday, 8:30 a.m. - 1:20 p.m. CT` … `TAS: Sunday - Friday 7:00 p.m. - 7:45 a.m. and Monday - Friday 8:30 a.m. - 1:15 p.m. CT`; `"ProductCode":{... "TAS":"ZCT","CmeGlobex":"ZC"}` |
| `cs-300-20210710.json(.txt)` | capture 2021-07-10 | same two lines |
| `cs-300-20240612.json(.txt)` | capture 2024-06-12 | same (byte-identical to the 2026-08-10 body) |
| `cs-300-20260810.json(.txt)` | capture 2026-08-10 | same |
| `cs-22-live.txt` | live, captured 2026-09-06 | Live Cattle Globex → `Monday - Friday: 8:30 a.m. - 1:05 p.m. CT` … `TAS: Monday - Friday 8:30 a.m. - 1:00 p.m. CT (9:30 a.m - 2:00 p.m. ET)`; `"TAS":"LET"` |
| `cs-22-20210710.json(.txt)` | capture 2021-07-10 | same |
| `cs-22-20260810.json(.txt)` | capture 2026-08-10 | same |
| `cs-8478-20210710091124.json(.txt)` | capture 2021-07-10 | Bitcoin: **no `TAS` key in ProductCode and no TAS hours line** (pre-launch) |
| `cs-8478-20220921051159.json(.txt)` | capture 2022-09-21 | BTIC present, **still no TAS** (pre-launch) |
| `cs-8478-20231208215151.json(.txt)` | capture 2023-12-08 | `"TAS":"TBT"`; Globex → `TAS: Sunday - Friday 5:00 p.m. - 3:00 p.m. CT` |
| `cs-8478-20240929143511.json(.txt)` | capture 2024-09-29 | same TAS line |
| `cs-8478-20250221153030.json(.txt)` | capture 2025-02-21 | same TAS line |
| `cs-8478-20251028222508.json(.txt)` | capture 2025-10-28 | same TAS line |
| `cs-8478-live.txt` | live, captured 2026-09-06 | Globex → outright `24/7 … Saturday 2:00 a.m. to 4:00 a.m. CT & Monday-Friday 4:00 p.m. to 4:02 p.m. CT`; `TAS: 24/7 with the exception of the following maintenance windows: Saturday 2:00 a.m. to 4:00 a.m. CT & Monday-Friday from 3:00 p.m. to 3:05 p.m. CT` (plus separate BTIC APAC/London/NY lines) |

## Legacy server-rendered spec pages — the family-level TAS session statements

| file | capture | quoted line |
|---|---|---|
| `corn-legacy-20141102022432.html` | 2014-11-02 | pre-launch: `Monday – Friday, 8:30 a.m. – 1:15 p.m. CT`, **zero** occurrences of `TAS` |
| `corn-legacy-20150522230148.html` | 2015-05-22 | pre-launch (17 days before the 2015-06-08 TAS launch): **zero** occurrences of `TAS` |
| `corn-legacy-20150905110358.html` | 2015-09-05 | `Trading Hours … Monday – Friday, 8:30 a.m. – 1:20 p.m. CT` and, in the same page, `Trading in all CBOT Grain TAS products will be 19:00-07:45 and 08:30-13:15 Chicago time. All resting TAS orders at 07:45 will remain in the book for the 08:30 opening, unless cancelled.` |
| `corn-legacy-20151009144314.html` | 2015-10-09 | identical pair |
| `corn-legacy-20160310222501.html` | 2016-03-10 | identical pair |
| `corn-legacy-20170520112704.html` | 2017-05-20 | identical pair |
| `corn-legacy-20190717062118.html` | 2019-07-17 | identical pair |
| `sb-legacy-20150905.html` | 2015-09-05 | Soybean: outright `8:30 a.m. – 1:20 p.m. CT`, `Product Code … TAS: SBT`; carries no TAS hours sentence of its own |
| `lc-legacy-20150905.html` | 2015-09-05 | `Trading in all CME Livestock TAS products will be 9:05-13:00 Chicago time on Mondays or on the Tuesdays that follow a Monday holiday, and Tuesday through Friday 8:00-13:00, Chicago time.` |
| `lc-legacy-20151127.html` | 2015-11-27 | identical era-1 sentence |
| `lc-legacy-20160311.html` | 2016-03-11 | `Trading in all CME Livestock TAS products will be 8:30 am -1:00 pm Chicago time Monday - Friday.`; outright `Monday - Friday: 8:30 a.m. - 1:05 p.m. CT` |
| `lc-legacy-20171211.html` | 2017-12-11 | identical era-2 sentence |
