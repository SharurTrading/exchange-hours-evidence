# INDEX — `cme-2023-mlk-channel-b-negatives` (the cmegroup.cn / mirror sweep, 2026-10-09 UTC)

Retrieval session: **2026-10-10 00:05–00:40 UTC** (`date -u`). All times UTC (LAW-UTC-DATES).

The fifth wave's Channel B tried the operator channels for the 2023-01-16 (MLK) CME marker that
prior sweeps had not: CME's own Chinese site `cmegroup.cn` (a verbatim mirror on the operator's own
domain would be T1), `cmegroup.fr`, the `cmegroup.com/education/*` and `/advisories/*` paths, and
the remaining archived trading-hours-service captures that query a January 2023 event window.
**Everything closed negative.** The marker stands.

| file | sha256 | bytes | source url | capture (UTC) | what it is |
|---|---|---|---|---|---|
| `cdx-cmegroup-cn-domain-300.json` | `f83166295a53e98b38fe8057bb2b7719f13d566ac1b77df0f0510656a3d767d7` | 38432 | CDX `cmegroup.cn matchType=domain, statuscode:200, collapse=urlkey, limit=300` | live fetch 2026-10-10 00:05 | First 300 archived cmegroup.cn URLs: assets and marketing/product-class pages only. **No URL containing holiday, jieri, hour, notice, schedule or calendar.** |
| `cdx-cmegroup-cn-2022-12_2023-04.json` | `c853ef20c5715c6f077bd229d6209d77b97aeb8a86ed0442503148c10a1fdc78` | 153325 | CDX `cmegroup.cn matchType=domain, 2022-12..2023-04, statuscode:200, collapse=urlkey` (1818 rows) | live fetch 2026-10-10 00:07 | Every archived cmegroup.cn capture across the winter that contains 2023-01-16: nine content pages, all product-class marketing pages (`/trading/`, `/trading-fx/`, `/trading-energy/`, …). No holiday-hours page exists anywhere on the archived domain. |
| `cdx-cmegroup-fr-domain.json` | `c0d437a0b7f4163244e208090d3f2c42556d6cb2904b06d5f43b62cec9ebafbd` | 891 | CDX `cmegroup.fr matchType=domain, statuscode:200, collapse=urlkey` (11 rows) | live fetch 2026-10-10 00:09 | `cmegroup.fr` is not a CME property: its archived captures are a parked EuroDNS landing page and its assets, 2011–2014. No CME content. |
| `cdx-cmegroup-education-prefix.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 3 | CDX `cmegroup.com/education matchType=prefix, mlk/martin/holiday filter, 2022-11..2023-06` | live fetch 2026-10-10 00:12 | Empty result set — no archived education-path URL matches in the window. |
| `cdx-cmegroup-advisories-prefix.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 3 | CDX `cmegroup.com/advisories matchType=prefix` | live fetch 2026-10-10 00:12 | Empty result set — the path has no captures at all. |
| `svc-equities-group-2023-01-15_2023-01-17-capture-20260719102637.json` | `c2300ae6f09ea151c8bc9fa3d345af574084a6d659f865d24e0b8d772bf45afe` | 87 | `https://web.archive.org/web/20260719102637id_/https://www.cmegroup.com/services/trading-hours-by-product?pageNumber=1&pageSize=500&cleared=Futures&group=Equities&fromEventDate=2023-01-15&toEventDate=2023-01-17` | capture 2026-07-19T10:26:37Z, replayed 2026-10-10 00:30 | The one archived service capture besides the known `CME-SVC-2023-01-15` control that queries a January 2023 event window (the `cleared`/`group` URL shape). The operator's own service answered the query with an HTTP 500 — `{ "message": "Error Query data from product slate. Check your parameters are correct."}` — so it carries no events either. |

Also re-fetched and confirmed byte-identical to holdings the store already had: the
`tools-information/holiday-calendar.html` capture of 2023-01-16T03:24:37Z (sha256
`2917984167c5…`, already at `cbot-2023-advisories/holiday-calendar-2023-01-16.html`) and the
`2023-mlk-day-advisory.pdf` (sha256 `2338a383ea4d…`, already at
`cbot-2023-advisories/2023-mlk-day-advisory.pdf`) — the advisory is a CME Clearing memorandum whose
Trading row points at the holiday calendar and states clearing cycles only, no session times.
The domain-wide `filter=original:.*mlk.*` CDX sweep over cmegroup.com timed out three times
(504s, not saved); the education/advisories empties above cover its target surface.
