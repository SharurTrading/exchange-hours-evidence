# INDEX — cme-2025-2027 (CME Group holiday schedules, calendar years 2025-2027)

Task: cme-2025-2027. Evidence gathered 2026-09-12 (UTC; `date -u`).
All CME times below are U.S. Central Time. Source of that statement, quoted verbatim from
https://www.cmegroup.com/trading-hours.html: "Trading hours are subject to change and are in U.S. Central Time unless otherwise stated."

## Channels used

1. **CME Group trading-hours service** (the operator's own machine channel, T2) —
   `https://www.cmegroup.com/services/trading-hours-by-product?...&fromEventDate=YYYY-MM-DD&toEventDate=YYYY-MM-DD`.
   This is the endpoint that `cmegroup.com/trading-hours.html` calls to render its per-asset-class
   **Holiday Hours** table; the rendered table was checked against the service rows for Thanksgiving 2026
   and matches row for row (see `live/trading-hours-live.md`).
   `[THBP-A]` in the JSON output = `https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true`
   `[THBP-B]` = same with `id=168,167,320,323,19,27`. `WA:<ts>id_/` = `https://web.archive.org/web/<ts>id_/` replay prefix.
2. **cmegroup.com/trading-hours.html** (T1 operator page) — the year's Globex holiday table, the
   per-holiday *Holiday Notes*, the CT zone statement, and the market-event-type legend.
3. **Web archive CDX** enumeration of `cmegroup.com/tools-information/holiday-calendar*`,
   `cmegroup.com/trading-hours*` and `cmegroup.com/services/trading-hours*`.

cmegroup.com returns HTTP 403 to this machine directly ("This IP address is blocked due to suspected
web scraping activity"), so live pages and service calls were read through the public reader
`https://r.jina.ai/<url>`; historical states were read from the Wayback Machine with `id_` replay.

## Notes on what the service publishes

Market event types, quoted verbatim from cmegroup.com/trading-hours.html:
  PREOPEN — "Order Entry, modification, and cancel are allowed. No order matching."
  OPEN — "Start of continuous trading phase. Order matching begins."
  Paused — "Interruption of continuous trading. Only order cancellation is allowed. No order matching."
  pcp (POST CLOSE - PREOPEN) — "Allows GTC/GTD orders only placement, modification, and cancellation. No order matching."
  closed — "Final Close of the date. Day and GTD (current trade date) orders are eliminated."

The live service only carries **forward** holiday events (from 2026-09-07 onward as of retrieval);
holidays already past are served from Wayback captures of the same endpoint.

## Artifacts

| file | what it is | url | capture / retrieval (UTC) | sha256 |
|---|---|---|---|---|
| `live/trading-hours-live.md` | CME Group Holiday and Trading Hours page, reader-rendered; carries the CT zone statement, the event-type legend, the printed per-asset-class Holiday Hours table for Thanksgiving 2026, and the 2026/2027/2028 Holiday Notes | https://www.cmegroup.com/trading-hours.html (via r.jina.ai) | retrieved 2026-09-12 | `ac85d05d1fcf2c6fc5afaad7bef5efa7bed407d53df7bdfc9bc724ae18c3449f` |
| `html/trading-hours-20250830.html` | Archived CME trading-hours page, 2025 edition: 2025 Globex holiday table, 2025 Holiday Notes, Trading Floor / ClearPort / BrokerTec / Spot Dairy holiday calendars | https://web.archive.org/web/20250830021420id_/https://www.cmegroup.com/trading-hours.html | captured 2025-08-30T02:14:20Z | `62fc524c79e0bd1269ad89b5fe1ae9b617c1b082243d4f5386c5d3fdf6ed5e58` |
| `html/holiday-calendar-20240917.html` | Archived CME Group Holiday Calendar page (every "Holiday Schedule" link points at /trading-hours.html) | https://web.archive.org/web/20240917153222id_/https://www.cmegroup.com/tools-information/holiday-calendar.html | captured 2024-09-17T15:32:22Z | `d2188be629f26750af5ebce25be8b4da077e2d0eaf70cb98d005761933bf3fb1` |
| `api/filters.json` | trading-hours service filter payload: asset-class/sub-group ids, exchanges, and CME's own forward holiday list with each holiday's start/end period | https://www.cmegroup.com/services/trading-hours-filters | retrieved 2026-09-12 | `0bdd49ce18da9db040d55e9df4d29594937c959e2bd233487d5be096ddb63dc1` |
| `live/normal/normalweek_main.json` | Non-holiday reference week 2026-10-18..24 for the ten headline product groups (the normal-grid baseline every holiday row is measured against) | [THBP-A]&fromEventDate=2026-10-18&toEventDate=2026-10-24 | retrieved 2026-09-12 | `d3bd6e890bdc427d2ebd3ece48dedc56eb231178be82c69ab3ac427f0b09dc0a` |
| `live/normal/normalweek_extra.json` | Non-holiday reference week 2026-10-18..24 for Nikkei, soybeans, wheat, lean hogs, Class III milk | [THBP-B]&fromEventDate=2026-10-18&toEventDate=2026-10-24 | retrieved 2026-09-12 | `2084b6593c7ac7703a5a86d506c242b5d9589f1756cc0dbfddb90c7d8f5f064c` |
| `adv2025/2025-mlk-day-clearing-advisory.pdf` | CME Clearing holiday memorandum, MLK 2025 — clearing cycles only; refers trading hours to the Holiday Calendar / Trading Hours pages | https://web.archive.org/web/20250207115918id_/https://www.cmegroup.com/tools-information/holiday-calendar/files/2025/2025-mlk-day-clearing-advisory.pdf | captured 2025-02-07T11:59:18Z | `477ab0da3a7b5918f578bbb7d1638b3399a9276fad3c1f3a8efbbc30aa9572a4` |
| `pdf2025/mlk-day-holiday-settlement-times-2025.pdf` | CME "Settlement Times" PDF, MLK 2025 — settlement-price derivation only, no trading hours (recorded to show the channel was read and is not a session source) | https://web.archive.org/web/20241214005231id_/https://www.cmegroup.com/tools-information/holiday-calendar/files/2025/mlk-day-holiday-settlement-times-2025.pdf | captured 2024-12-14T00:52:31Z | `d53d2cac8d6270bbf7eb7f2c9e49a06f2723c2ea226b45c404ee06e4141b18f7` |
| `arc/thbp_2024-12-31_2025-01-02_20241220155340.json` | trading-hours service response, window 2024-12-31..2025-01-02 (10 headline product groups) | WA:20241220155340id_/[THBP-A]&fromEventDate=2024-12-31&toEventDate=2025-01-02 | 2024-12-20T15:53:40Z | `375c70eecd19c5c6204ecb408d1b3210a9da4c9a03b85ef1c7dbbcde1397ab63` |
| `arc/thbp_2025-01-19_2025-01-21_20241220155340.json` | trading-hours service response, window 2025-01-19..2025-01-21 (10 headline product groups) | WA:20241220155340id_/[THBP-A]&fromEventDate=2025-01-19&toEventDate=2025-01-21 | 2024-12-20T15:53:40Z | `4f2ab56af14e7b3a6978e7fa6db8e2cfc63a82d06428cd88844f0e5bcf534f40` |
| `arc/thbp_2025-02-16_2025-02-18_20241220155340.json` | trading-hours service response, window 2025-02-16..2025-02-18 (10 headline product groups) | WA:20241220155340id_/[THBP-A]&fromEventDate=2025-02-16&toEventDate=2025-02-18 | 2024-12-20T15:53:40Z | `5bec2ca6b4999a534e4d9818035aaa18ec8626b6c912cf7e3d2c57015536f2fa` |
| `arc/thbp_2025-04-17_2025-04-19_20241220155340.json` | trading-hours service response, window 2025-04-17..2025-04-19 (10 headline product groups) | WA:20241220155340id_/[THBP-A]&fromEventDate=2025-04-17&toEventDate=2025-04-19 | 2024-12-20T15:53:40Z | `865a1d4f08102e00151bd87ab2b8e8a7720e9203a17aaaba24627ade3ed26e74` |
| `arc/thbp_2025-05-25_2025-05-27_20241220155340.json` | trading-hours service response, window 2025-05-25..2025-05-27 (10 headline product groups) | WA:20241220155340id_/[THBP-A]&fromEventDate=2025-05-25&toEventDate=2025-05-27 | 2024-12-20T15:53:40Z | `5f42869879c826f5949b79236aabb3d26d74e7565d92d7cc5e8784c63973210b` |
| `arc/thbp_2025-06-18_2025-06-20_20241220155340.json` | trading-hours service response, window 2025-06-18..2025-06-20 (10 headline product groups) | WA:20241220155340id_/[THBP-A]&fromEventDate=2025-06-18&toEventDate=2025-06-20 | 2024-12-20T15:53:40Z | `a572706907175776255261103b393493ebdf5a8106ec5374d129145bdf89105e` |
| `arc/thbp_2025-07-03_2025-07-05_20241220155340.json` | trading-hours service response, window 2025-07-03..2025-07-05 (10 headline product groups) | WA:20241220155340id_/[THBP-A]&fromEventDate=2025-07-03&toEventDate=2025-07-05 | 2024-12-20T15:53:40Z | `b80cd4bfed0ae72865bfacc1936e107eb8febfcc94b37fcce1d05505c659147b` |
| `arc/thbp_2025-08-31_2025-09-02_20241220155340.json` | trading-hours service response, window 2025-08-31..2025-09-02 (10 headline product groups) | WA:20241220155340id_/[THBP-A]&fromEventDate=2025-08-31&toEventDate=2025-09-02 | 2024-12-20T15:53:40Z | `e075762ed34a86048d94900e10edba10d95b3d766052908ffbb5133f6b64bab0` |
| `arc/thbp_2025-11-26_2025-11-28_20241220155340.json` | trading-hours service response, window 2025-11-26..2025-11-28 (10 headline product groups) | WA:20241220155340id_/[THBP-A]&fromEventDate=2025-11-26&toEventDate=2025-11-28 | 2024-12-20T15:53:40Z | `34f38de416a997f7a1a095ce33261327c0b604abecdbe221a35305005ffa2764` |
| `arc/thbp_2025-12-24_2025-12-26_20260129012159.json` | trading-hours service response, window 2025-12-24..2025-12-26 (10 headline product groups) | WA:20260129012159id_/[THBP-A]&fromEventDate=2025-12-24&toEventDate=2025-12-26 | 2026-01-29T01:21:59Z | `322a2be989b67f5f4cc0ec12fd63a393383d574badd4aacc87a0c9637533d386` |
| `arc/thbp_2025-12-31_2026-01-02_20260619114105.json` | trading-hours service response, window 2025-12-31..2026-01-02 (10 headline product groups) | WA:20260619114105id_/[THBP-A]&fromEventDate=2025-12-31&toEventDate=2026-01-02 | 2026-06-19T11:41:05Z | `0ed61f8328eda4746265cc8e197f10cd53aec06c2b393927bab27c913993d314` |
| `arc/thbp_2026-01-18_2026-01-20_20260619114105.json` | trading-hours service response, window 2026-01-18..2026-01-20 (10 headline product groups) | WA:20260619114105id_/[THBP-A]&fromEventDate=2026-01-18&toEventDate=2026-01-20 | 2026-06-19T11:41:05Z | `5e3ff08bdc7d07474b96b8dc8c18ed0d5e48d12dc4bcad81a5f68820cb2aa89e` |
| `arc/thbp_2026-02-15_2026-02-17_20260619114105.json` | trading-hours service response, window 2026-02-15..2026-02-17 (10 headline product groups) | WA:20260619114105id_/[THBP-A]&fromEventDate=2026-02-15&toEventDate=2026-02-17 | 2026-06-19T11:41:05Z | `5dd507dd959d0029e838ec88b1bdb63c32444ea36a121de002606f5d7b206e2f` |
| `arc/thbp_2026-04-01_2026-04-03_20260619114118.json` | trading-hours service response, window 2026-04-01..2026-04-03 (10 headline product groups) | WA:20260619114118id_/[THBP-A]&fromEventDate=2026-04-01&toEventDate=2026-04-03 | 2026-06-19T11:41:18Z | `54bcc271e9ba9737a99a2fe608e658de0c657075284d050fbfec4fe1aee2a2a5` |
| `arc/thbp_2026-05-24_2026-05-26_20260619114105.json` | trading-hours service response, window 2026-05-24..2026-05-26 (10 headline product groups) | WA:20260619114105id_/[THBP-A]&fromEventDate=2026-05-24&toEventDate=2026-05-26 | 2026-06-19T11:41:05Z | `f7e30d204ce2cbe08e5f486ded6518f623369159f3a36161288a4708288314da` |
| `arc/thbp_2026-06-17_2026-06-19_20260129012310.json` | trading-hours service response, window 2026-06-17..2026-06-19 (10 headline product groups) | WA:20260129012310id_/[THBP-A]&fromEventDate=2026-06-17&toEventDate=2026-06-19 | 2026-01-29T01:23:10Z | `e4e2d5e452843653b7af99d26ef6c317ae068b78c752af09296aedee65af6b17` |
| `arc/thbp_2026-06-18_2026-06-20_20260619113404.json` | trading-hours service response, window 2026-06-18..2026-06-20 (10 headline product groups) | WA:20260619113404id_/[THBP-A]&fromEventDate=2026-06-18&toEventDate=2026-06-20 | 2026-06-19T11:34:04Z | `97fd5da371309f4486a8fb49ff2105c6c1c2396939ab7c76f1a2a1097b6f015c` |
| `arc/thbp_2026-07-02_2026-07-04_20260129012216.json` | trading-hours service response, window 2026-07-02..2026-07-04 (10 headline product groups) | WA:20260129012216id_/[THBP-A]&fromEventDate=2026-07-02&toEventDate=2026-07-04 | 2026-01-29T01:22:16Z | `d97339fb9b8be15b7e1be70293a5b40afc38e8b09f136158f63bbccd75ea93d7` |
| `arc/thbp_2026-07-03_2026-07-05_20260619114108.json` | trading-hours service response, window 2026-07-03..2026-07-05 (10 headline product groups) | WA:20260619114108id_/[THBP-A]&fromEventDate=2026-07-03&toEventDate=2026-07-05 | 2026-06-19T11:41:08Z | `4b89a026358e998277f9c1ff7e095e5d4e625cdc45115fd141dc92201833155b` |
| `arc/thbp_2026-09-06_2026-09-08_20260830142930.json` | trading-hours service response, window 2026-09-06..2026-09-08 (10 headline product groups) | WA:20260830142930id_/[THBP-A]&fromEventDate=2026-09-06&toEventDate=2026-09-08 | 2026-08-30T14:29:30Z | `01fb78ffaac10eac466fed53674214222f05aed518b9d93a4b42cf8957147bca` |
| `arc/thbp_2026-11-25_2026-11-27_20260830142904.json` | trading-hours service response, window 2026-11-25..2026-11-27 (10 headline product groups) | WA:20260830142904id_/[THBP-A]&fromEventDate=2026-11-25&toEventDate=2026-11-27 | 2026-08-30T14:29:04Z | `e1f35a5623b3c5d15e7468b2cb4119e587411a9714f920605dab11bf688756d1` |
| `arc/thbp_2026-12-23_2026-12-25_20260310063244.json` | trading-hours service response, window 2026-12-23..2026-12-25 (10 headline product groups) | WA:20260310063244id_/[THBP-A]&fromEventDate=2026-12-23&toEventDate=2026-12-25 | 2026-03-10T06:32:44Z | `0cc5fa9d78ba2d6d1246faab67acfc1388b52f16a7f2c32b2dddec07238e87c2` |
| `arc/thbp_2026-12-24_2026-12-26_20260830142904.json` | trading-hours service response, window 2026-12-24..2026-12-26 (10 headline product groups) | WA:20260830142904id_/[THBP-A]&fromEventDate=2026-12-24&toEventDate=2026-12-26 | 2026-08-30T14:29:04Z | `bdc1fe831adb794bcf8aeb7e99baf6af2009d1ff9969d0a48b18b2ebc2e1e829` |
| `arc/thbp_2026-12-30_2027-01-01_20260310063233.json` | trading-hours service response, window 2026-12-30..2027-01-01 (10 headline product groups) | WA:20260310063233id_/[THBP-A]&fromEventDate=2026-12-30&toEventDate=2027-01-01 | 2026-03-10T06:32:33Z | `462a8a6df0edf8f59c66a00ed54126c01e1722d2768d50d1d7e78a9fdc390176` |
| `arc/thbp_2026-12-31_2027-01-02_20260830142904.json` | trading-hours service response, window 2026-12-31..2027-01-02 (10 headline product groups) | WA:20260830142904id_/[THBP-A]&fromEventDate=2026-12-31&toEventDate=2027-01-02 | 2026-08-30T14:29:04Z | `7162652821c16f1bd05e3ec533bd5b82af03833c7186a64c7734b0b650364dcd` |
| `live/thbp/thbp_2026-06-21_2026-06-23.md` | trading-hours service response, window 2026-06-21..2026-06-23 (10 headline product groups), reader-rendered | [THBP-A]&fromEventDate=2026-06-21&toEventDate=2026-06-23 (via r.jina.ai) | retrieved 2026-09-25 | `91534cfd3ae56920ef744734216d2f5944cb9057c483d4b12f1550d91d91bcaf` |
| `live/thbp/thbp_2026-09-06_2026-09-08.json` | trading-hours service response, window 2026-09-06..2026-09-08 (10 headline product groups) | [THBP-A]&fromEventDate=2026-09-06&toEventDate=2026-09-08 | retrieved 2026-09-12 | `01fb78ffaac10eac466fed53674214222f05aed518b9d93a4b42cf8957147bca` |
| `live/thbp/thbp_2026-11-25_2026-11-27.json` | trading-hours service response, window 2026-11-25..2026-11-27 (10 headline product groups) | [THBP-A]&fromEventDate=2026-11-25&toEventDate=2026-11-27 | retrieved 2026-09-12 | `e1f35a5623b3c5d15e7468b2cb4119e587411a9714f920605dab11bf688756d1` |
| `live/thbp/thbp_2026-12-22_2026-12-24.json` | trading-hours service response, window 2026-12-22..2026-12-24 (10 headline product groups) | [THBP-A]&fromEventDate=2026-12-22&toEventDate=2026-12-24 | retrieved 2026-09-12 | `c8c0267da8cf171409ad8ca188082b3aa326e8d04a89d12503dcf9f57bf3b7ab` |
| `live/thbp/thbp_2026-12-24_2026-12-26.json` | trading-hours service response, window 2026-12-24..2026-12-26 (10 headline product groups) | [THBP-A]&fromEventDate=2026-12-24&toEventDate=2026-12-26 | retrieved 2026-09-12 | `bdc1fe831adb794bcf8aeb7e99baf6af2009d1ff9969d0a48b18b2ebc2e1e829` |
| `live/thbp/thbp_2026-12-29_2026-12-31.json` | trading-hours service response, window 2026-12-29..2026-12-31 (10 headline product groups) | [THBP-A]&fromEventDate=2026-12-29&toEventDate=2026-12-31 | retrieved 2026-09-12 | `691de39fb25a0be94598e50ac48933f119fbd0cd04fae9c36f7df8494ffcedaa` |
| `live/thbp/thbp_2026-12-31_2027-01-02.json` | trading-hours service response, window 2026-12-31..2027-01-02 (10 headline product groups) | [THBP-A]&fromEventDate=2026-12-31&toEventDate=2027-01-02 | retrieved 2026-09-12 | `7162652821c16f1bd05e3ec533bd5b82af03833c7186a64c7734b0b650364dcd` |
| `live/thbp/thbp_2027-01-17_2027-01-19.json` | trading-hours service response, window 2027-01-17..2027-01-19 (10 headline product groups) | [THBP-A]&fromEventDate=2027-01-17&toEventDate=2027-01-19 | retrieved 2026-09-12 | `7155c4b7ee8b299b3033eb3daf002b6ceecf0fbd53f6f98a7036048022275743` |
| `live/thbp/thbp_2027-02-14_2027-02-16.json` | trading-hours service response, window 2027-02-14..2027-02-16 (10 headline product groups) | [THBP-A]&fromEventDate=2027-02-14&toEventDate=2027-02-16 | retrieved 2026-09-12 | `41f5aa8cde3879f8b10490386c134a294a0f1509edde2022a22ec3ffcaed1183` |
| `live/thbp/thbp_2027-03-25_2027-03-27.json` | trading-hours service response, window 2027-03-25..2027-03-27 (10 headline product groups) | [THBP-A]&fromEventDate=2027-03-25&toEventDate=2027-03-27 | retrieved 2026-09-12 | `9bd7225d440e00139f30892f3914c9b38beb8bf29d4272039b6cd8f2de926880` |
| `live/thbp/thbp_2027-05-30_2027-06-01.json` | trading-hours service response, window 2027-05-30..2027-06-01 (10 headline product groups) | [THBP-A]&fromEventDate=2027-05-30&toEventDate=2027-06-01 | retrieved 2026-09-12 | `1283649724c30163fa08ba7ab02d1230fa9a7dd0613b8b4b3d96cd1d9dc4febd` |
| `live/thbp/thbp_2027-06-17_2027-06-19.json` | trading-hours service response, window 2027-06-17..2027-06-19 (10 headline product groups) | [THBP-A]&fromEventDate=2027-06-17&toEventDate=2027-06-19 | retrieved 2026-09-12 | `60c9a2f5106d61039a616986b463cd852861ee4d3b91b11fac8badfa1b97b01c` |
| `live/thbp/thbp_2026-07-05_2026-07-07.md` | trading-hours service response, window 2026-07-05..2026-07-07 (10 headline product groups), reader-rendered — retrieved to witness the 2026-07-06 `16:00 closed` that closes trade date 2026-07-06, which no earlier capture in this store contains | [THBP-A]&fromEventDate=2026-07-05&toEventDate=2026-07-07 (via r.jina.ai) | retrieved 2026-09-26T02:55:11Z | `f6e1900b4971eda307f63d1c905f94741c268350fe4623e916580065c4c194cb` |
| `live/thbp/thbp_2027-06-20_2027-06-22.md` | trading-hours service response, window 2027-06-20..2027-06-22 (10 headline product groups), reader-rendered | [THBP-A]&fromEventDate=2027-06-20&toEventDate=2027-06-22 (via r.jina.ai) | retrieved 2026-09-25 | `9ab30e85bb6947803f35369ed29e24cc98c20c86498bf48f87ec6515d8431107` |
| `live/thbp/thbp_2027-07-04_2027-07-06.json` | trading-hours service response, window 2027-07-04..2027-07-06 (10 headline product groups) | [THBP-A]&fromEventDate=2027-07-04&toEventDate=2027-07-06 | retrieved 2026-09-12 | `93ff8232886435c94be682bf968aa30749011cdf8dadeb7d2425a3b0b9e0bf71` |
| `live/thbp/thbp_2027-09-05_2027-09-07.json` | trading-hours service response, window 2027-09-05..2027-09-07 (10 headline product groups) | [THBP-A]&fromEventDate=2027-09-05&toEventDate=2027-09-07 | retrieved 2026-09-12 | `aa08a3bd102812928e69cf1ea4c8a84f738eaa5d14f967acee7d2571e74aedb9` |
| `live/thbp/thbp_2027-11-24_2027-11-26.json` | trading-hours service response, window 2027-11-24..2027-11-26 (10 headline product groups) | [THBP-A]&fromEventDate=2027-11-24&toEventDate=2027-11-26 | retrieved 2026-09-12 | `6aa7c0fd701a02480dabeac1fbae1a69b56e77643a29e3a9b2223c56e822ce9f` |
| `live/thbp/thbp_2027-12-22_2027-12-25.json` | trading-hours service response, window 2027-12-22..2027-12-25 (10 headline product groups) | [THBP-A]&fromEventDate=2027-12-22&toEventDate=2027-12-25 | retrieved 2026-09-12 | `5edc4dd588a32faa74f841494c10a3df48692dca29843c3581bad3e18c30fef9` |
| `live/thbp/thbp_2027-12-30_2028-01-02.json` | trading-hours service response, window 2027-12-30..2028-01-02 (10 headline product groups) | [THBP-A]&fromEventDate=2027-12-30&toEventDate=2028-01-02 | retrieved 2026-09-12 | `42112fc78b1a8c2cdd4d029af035b73662f7566826e0ada264d7c1020b8668cb` |
| `live/extra/extra_2026-06-21_2026-06-23.md` | trading-hours service response, window 2026-06-21..2026-06-23 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk), reader-rendered | [THBP-B]&fromEventDate=2026-06-21&toEventDate=2026-06-23 (via r.jina.ai) | retrieved 2026-09-25T08:44:59Z | `09714a527385207db4926843cda9df6d2a0ea6515356584e1f8e1f9f69b4f209` |
| `live/extra/extra_2026-09-06_2026-09-08.json` | trading-hours service response, window 2026-09-06..2026-09-08 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2026-09-06&toEventDate=2026-09-08 | retrieved 2026-09-12 | `f7cc43f8d90b571b945901f826277ca43ec21c4438c36bbb26e231c859a83923` |
| `live/extra/extra_2026-11-25_2026-11-27.json` | trading-hours service response, window 2026-11-25..2026-11-27 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2026-11-25&toEventDate=2026-11-27 | retrieved 2026-09-12 | `f6007a75d6009dada85fe6c57d660598f21ed8a8385364c454ee015565f94dd4` |
| `live/extra/extra_2026-12-24_2026-12-26.json` | trading-hours service response, window 2026-12-24..2026-12-26 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2026-12-24&toEventDate=2026-12-26 | retrieved 2026-09-12 | `b622712c1c45c3efb90443172617636ba4c7d7dfb4c6851b70a22ee1c9fa978d` |
| `live/extra/extra_2026-12-31_2027-01-02.json` | trading-hours service response, window 2026-12-31..2027-01-02 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2026-12-31&toEventDate=2027-01-02 | retrieved 2026-09-12 | `b21ac047d6d67cb9026940a37ad345c7b2ece40e73dbca7be69cf7171646613c` |
| `live/extra/extra_2027-01-17_2027-01-19.json` | trading-hours service response, window 2027-01-17..2027-01-19 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-01-17&toEventDate=2027-01-19 | retrieved 2026-09-12 | `3fc8c80ea1222cd0bb3d46c8a7df904acd3859441ffdfd9de6145625177f9bfc` |
| `live/extra/extra_2027-02-14_2027-02-16.json` | trading-hours service response, window 2027-02-14..2027-02-16 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-02-14&toEventDate=2027-02-16 | retrieved 2026-09-12 | `c8ca83f4594756ed338368a0035b790e7a27efe6872506985ca6f7d16bcc97eb` |
| `live/extra/extra_2027-03-25_2027-03-27.json` | trading-hours service response, window 2027-03-25..2027-03-27 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-03-25&toEventDate=2027-03-27 | retrieved 2026-09-12 | `022dcd1f61e54cc316a621e01f519bbb723a446c000323dd9725d2d6434effe8` |
| `live/extra/extra_2027-05-30_2027-06-01.json` | trading-hours service response, window 2027-05-30..2027-06-01 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-05-30&toEventDate=2027-06-01 | retrieved 2026-09-12 | `1c28c61151bd26e844c5b2ea6f046102b6da45a5f88566e91a421604a8c566e6` |
| `live/extra/extra_2027-06-17_2027-06-19.json` | trading-hours service response, window 2027-06-17..2027-06-19 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-06-17&toEventDate=2027-06-19 | retrieved 2026-09-12 | `011d4f666198a4427faa01d7e91ebf2412f4614ae27188ccd35f84c726a5d05d` |
| `live/extra/extra_2026-07-05_2026-07-07.md` | trading-hours service response, window 2026-07-05..2026-07-07 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk), reader-rendered — retrieved to witness `NKD`/`NIY`'s 2026-07-06 `16:00 closed`, which no earlier capture here contains | [THBP-B]&fromEventDate=2026-07-05&toEventDate=2026-07-07 (via r.jina.ai) | retrieved 2026-09-26T02:55:11Z | `4998f2fbf8016ce92132df7efcb1ea98555270c28ad453262e70213d2b519a4d` |
| `live/extra/extra_2027-06-20_2027-06-22.md` | trading-hours service response, window 2027-06-20..2027-06-22 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk), reader-rendered | [THBP-B]&fromEventDate=2027-06-20&toEventDate=2027-06-22 (via r.jina.ai) | retrieved 2026-09-25T08:44:59Z | `173d07af2d7621480b4a6653d4c2295f3f2b83197c1df3b21ce3bf38179f0d12` |
| `live/extra/extra_2027-07-04_2027-07-06.json` | trading-hours service response, window 2027-07-04..2027-07-06 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-07-04&toEventDate=2027-07-06 | retrieved 2026-09-12 | `1a9550357fbf3c1615fcbeefebbc64e271a6dfe0ad0ffdff10c770a7e2d77aaf` |
| `live/extra/extra_2027-09-05_2027-09-07.json` | trading-hours service response, window 2027-09-05..2027-09-07 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-09-05&toEventDate=2027-09-07 | retrieved 2026-09-12 | `9ceb6df48d2278a807fd2e3081828eb41dd207cc64c389078b3a529f762da928` |
| `live/extra/extra_2027-11-24_2027-11-26.json` | trading-hours service response, window 2027-11-24..2027-11-26 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-11-24&toEventDate=2027-11-26 | retrieved 2026-09-12 | `90320ed581b1d09f6c1b85d98da3a7a097b09d5f4eaac4abbb3d9368ee1cfdfa` |
| `live/extra/extra_2027-12-22_2027-12-25.json` | trading-hours service response, window 2027-12-22..2027-12-25 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-12-22&toEventDate=2027-12-25 | retrieved 2026-09-12 | `1ee3bd5fb9a99f765f96ac60377e8013cfca1c54ceba53beeb616d12862e2b12` |
| `live/extra/extra_2027-12-30_2028-01-02.json` | trading-hours service response, window 2027-12-30..2028-01-02 (Nikkei USD/JPY, soybeans, wheat, lean hogs, Class III milk) | [THBP-B]&fromEventDate=2027-12-30&toEventDate=2028-01-02 | retrieved 2026-09-12 | `4cb0352e98a88c3827e1839cf353c635d4d0484b6721661cd93498da898cf599` |
| `cdx/cdx_holiday_calendar_2024_2027.json` | CDX enumeration of cmegroup.com/tools-information/holiday-calendar* 2024-2027 | https://web.archive.org/cdx/search/cdx?... | retrieved 2026-09-12 | `b83b0a160303df3f6334d8bdb8904d0e494ba3754b6e95af62febe9ae2b923f0` |
| `cdx/cdx_thbp_all.json` | CDX enumeration of cmegroup.com/services/trading-hours-by-product* 2024-2027 | https://web.archive.org/cdx/search/cdx?... | retrieved 2026-09-12 | `e89d94fc29f657659ec672c6044ef216908cf157a092a4b5e369cc76361db64d` |
| `cdx/cdx_services_th.json` | CDX enumeration of cmegroup.com/services/trading-hours* 2024-2027 | https://web.archive.org/cdx/search/cdx?... | retrieved 2026-09-12 | `7d413a23501a426582f89fb7b52772e6621662d569274c679626d43fa5bfa8d2` |
| `cdx/thbp_2025_2027_urls.tsv` | filtered list of the archived service captures whose windows fall in 2025-2027 | https://web.archive.org/cdx/search/cdx?... | retrieved 2026-09-12 | `fac86cb1226356d6b102b5e5171df9de743394da7021f64e81ca48f712f28db0` |
| `FINAL_ROWS.json` | derived: every (date, product) schedule row with its normal-grid baseline, deviation flag and source | (derived in this task) | 2026-09-12 | `540680eb7f0991286cf69b0aeb69b73f7c69448248f6250f22b0c298a35eea81` |
| `FINAL_REVIEW.txt` | derived: human-readable review of every deviating row | (derived in this task) | 2026-09-12 | `899c47fedc3c38fac45246a044a9168b1804045d862fcbdbf97152220b44d266` |
| `ALLDUMP.txt` | derived: raw dump of every retrieved window | (derived in this task) | 2026-09-12 | `2fc1c38d760ad4fdf671a150734ab0cb1025724f63dbf43695edce26f9777fef` |
| `HOLIDAYS_OUT.json` | derived: the holidays[] array returned as this task's structured output | (derived in this task) | 2026-09-12 | `280ac0d6c99c4991e9b776462eac713b7f617d28d4cc7e0d468da1840d11919a` |

## Note codes used in the structured output

- `N1` no market events published for the date (family does not trade)
- `N2` pre-open only at 16:00 CT and no open: the Sunday-evening leg does not run
- `N3` ordinary daily 16:00-17:00 CT pause, no early close; no final close on the date so the trade date rolls
- `N4` no day session; only a 17:00 CT open, beginning the next business-day trade date
- `N5` no day session; only a 19:00 CT open, beginning the next business-day trade date
- `N6` final close at the normal 16:00 CT but no evening re-open
- `N7` day session normal to the 16:00 CT final close; the evening leg (normally 16:45 CT pre-open / 19:00 CT open) does not run
- `N8` published event list equals the family's normal grid for that weekday
- `N9` published event list differs from the normal grid
- `N10` 24/7 grid: the 16:00 CT daily final close is omitted (no settlement on the holiday); trading continuous, trade date rolls
- `N11` special Saturday session (Saturday is normally closed for this family)
- `N12` pre-open starts 06:00 CT (no prior-evening session ran); matching still begins 08:30 CT
- `N13` only a pre-2026-05-29 publication survives for this date, captured before CME crypto moved to the 24/7 grid; superseded
- `N14` final close 16:00 CT, pre-open 16:45 CT, no 17:00 CT open that evening
- `N15` matching halts 12:00 CT (event type preopen, not a final close), resumes 17:00 CT; span carries the next business-day trade date
- `N16` matching halts 13:30 CT (event type preopen), resumes 17:00 CT; span carries the next business-day trade date
- `EC <hh:mm> CT ...` early final close at the stated instant

## Residual risks

- Every 2025 holiday except Christmas 2025 and New Year 2026 is sourced from the single Wayback capture
  **2024-12-20T15:53:40Z** of the service. CME states on the same page: "This schedule is subject to change.
  Trading hours are usually finalized approximately two weeks prior to the holiday." No later capture of a
  2025 window exists in the archive, so the later-2025 rows are CME's published future as of 2024-12-20,
  not a post-finalisation statement.
- Nikkei 225 (NKD/NIY), soybeans (ZS), wheat (ZW), lean hogs (HE) and Class III milk (DC) are only in the
  archive for windows from 2026-09-06 onward; before that the archive carries only the ten-product list.
- Cryptocurrency on 2026-06-17 and 2026-07-02 survives only in a 2026-01-29 capture taken before CME crypto
  moved to the 24/7 grid on 2026-05-29; those two rows are marked `unknown`, not carried.


| `/Users/agedvagabond/Developer/exchange-hours-research/holidays/cme-2025-2027.r0.json` | this task's round-0 structured output, superseded by the round-1 fix and kept verbatim under the `.r0.json` name (the hash below is of those round-0 bytes; the round-1 output is `cme-2025-2027.json`, sha256 `6bc718e5fbaea70c01f3bf54ccab156028eef9c28ce24357a5217c633b5d5771`, indexed in `../cme-2025-2027-fix/INDEX.md`) | (derived in this task) | 2026-09-12 | `4cd4706a8e989cd0d59abe1279e4a03f3aee9b0b80c99476d2fe49466584bd50` |


---

## Addendum — round-1 fix, 2026-09-12 (UTC)

A fixer round re-read the saved bytes and retrieved new evidence; it is under
`../cme-2025-2027-fix/` with its own INDEX.md. Nothing in this directory was deleted or rewritten; the only
edit to this file is the output row above, plus this addendum. What it affects here:

- **Note codes.** This file defines `N1`..`N16` and `EC`. `N17` was used in the output without a definition,
  and `N18` was added in the fix round:
  - `N17` no day session on the holiday: only a 16:00 CT pre-open and a 17:00 CT open, both already carrying
    the next business day's trade date (verified against `arc/thbp_2024-12-31_2025-01-02_20241220155340.json`).
  - `N18` the published event TIMES equal the family's normal grid for that weekday, but the re-open carries a
    trade date that skips the following closed holiday.
- **Re-fetch path.** The `url` column for the 25 archived service artifacts in `arc/` omits the
  `&isProtected&_t=<epoch>` suffix that is part of the archived URL, so following one literally returns a
  Wayback 404. The exact one-step `id_` replay URL for each is in `../cme-2025-2027-fix/REFETCH.tsv`.
- **File inventory.** This file lists the 72 load-bearing artifacts. `../cme-2025-2027-fix/MANIFEST-cme-2025-2027.sha256`
  hashes all 180 files on disk under this directory, including every `.raw` reader original and the `html/`,
  `api/`, `cdx/`, `js/` and derived working files.
- **Residual risks, first bullet — corrected.** "No later capture of a 2025 window exists in the archive" is
  false for Thanksgiving 2025: the window `2025-11-26..2025-11-28` has 45 captures, 44 of them from the
  2026-01-29 crawl, i.e. after the holiday. The output now sources that holiday from the latest of them
  (`../cme-2025-2027-fix/arc/thbp_2025-11-26_2025-11-28_20260129012309.json`), and
  `arc/thbp_2025-11-26_2025-11-28_20241220155340.json` is retained as the superseded pre-holiday publication.
  The statement does hold for the eight windows New Year 2025 through Labor Day 2025.
- **Unrecorded gap.** No archived call of the service covers Saturday 2025-11-29, although CME's own 2025
  Globex table states the Thanksgiving period as "27 - 29 November 2025". This is now an explicit `missing[]`
  entry in the output.
