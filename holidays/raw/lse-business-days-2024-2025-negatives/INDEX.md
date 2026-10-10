# INDEX — `lse-business-days-2024-2025-negatives` (Channel D, 2026-10-10 UTC)

Retrieval session: **2026-10-10 01:25–02:00 UTC** (`date -u`). All times UTC (LAW-UTC-DATES).

Question: does any 2024-2025 capture of the LSEG business-days page (the page whose 2013-2020
captures tiled the `lse` history, #218) fall inside 2025-01-02..2025-12-17 and list the five
missing 2025 dates (2025-04-18, 2025-04-21, 2025-05-05, 2025-05-26, 2025-08-25)?

**Answer: no. The channel closes negative.**

1. The `lseg.com/areas-expertise/.../business-days` URL answers **301** from 2021 onward — the last
   200s of the page itself are the 2013-2020 era the #218 close already tiled
   (`cdx-lseg.com-business-days-first100.json` holds the first 100 captures, 2013-10..2020;
   `cdx-lseg.com-business-days-2021-2026.json` shows the five 2021-2024 captures are all 301s).
2. The 301 target, `londonstockexchange.com/securities-trading/trading-access/business-days`, has
   exactly two 200 captures inside 2024-2025: **2024-05-19T07:20:53Z** and
   **2025-08-07T20:17:52Z** (re-crawled unchanged 2025-08-09, same digest
   `BK42SPDMFQEZON7XDSIEHEVR6MNRBAR3`) — `cdx-londonstockexchange.com-business-days-2023-2026.json`.
3. Both page captures are **client-side application shells that state no dates**. The 2025-08-07
   capture (34178 bytes, LSEG web release 1.113.0) is an Angular bootstrap with no holiday text —
   no "Good Friday", no "bank holiday", no 2025 dates anywhere in its bytes; the 2024-05-19 capture
   (3867 bytes, an earlier shell of the same app) likewise. The page renders its table from a
   runtime API the archive never captured, so no archived byte of this page lists any 2025 holiday.

The five 2025 markers in `lse.rs` / `docs/evidence/lse.md` stand. Common Crawl index queries for the
target URL (CC-MAIN-2025-05/30/47) timed out repeatedly (504) and are not saved; the Wayback shell
evidence above answers the question those queries would have asked, since a Common Crawl capture of
the same URL would carry the same runtime-empty shell.

| file | sha256 | bytes | source url | capture (UTC) | what it is |
|---|---|---|---|---|---|
| `cdx-lseg.com-business-days-first100.json` | `8d211835d1241a823f0268f2c7154c1a830c659ac2afe8d7042019cf65c21dbf` | 19537 | CDX exact-URL query, limit 100 | live fetch 2026-10-10 01:26 | First 100 captures of the #218 URL: 200s from 2013-10-04 onward. |
| `cdx-lseg.com-business-days-2021-2026.json` | `c4c6b9b0c1ad0a0d0f34dbadb1b16a1bc93c48dd13aabd8d4554c6bdfcc5fdc8` | 772 | CDX exact-URL query 2021-2026 | live fetch 2026-10-10 01:28 | Five captures, all 301 — the page moved. |
| `cdx-londonstockexchange.com-business-days-2023-2026.json` | `d80944e49d5ce5b28f9b3322c0a51ae5fa6b61d53ac91715492c9021b47b5a7b` | 1333 | CDX exact-URL query of the redirect target, 2023-2026 | live fetch 2026-10-10 01:32 | Seven captures; the two 2024-2025 200s are the shells below (one digest each, the 2025-08-09 re-crawl identical). |
| `business-days-2024-05-19.html` | `62ce31df0eff551efa09c1f9f3a59012ab1d27e73264125551bef248f3e3a55c` | 3867 | https://web.archive.org/web/20240519072053id_/https://www.londonstockexchange.com/securities-trading/trading-access/business-days | 2024-05-19T07:20:53Z, replayed 2026-10-10 01:36 | Client-side shell; no holiday content. |
| `business-days-2025-08-07.html` | `55313f292f475940c4e4ab65dc8f66c02d365ab3f7b912ccbe42d72d2a993088` | 34178 | https://web.archive.org/web/20250807201752id_/https://www.londonstockexchange.com/securities-trading/trading-access/business-days | 2025-08-07T20:17:52Z, replayed 2026-10-10 01:34 | Client-side shell (release 1.113.0); no holiday content, no dates. |
