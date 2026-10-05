# Evidence index — `equities/euronext_paris/2025-2027`

Primary-source retrieval for the `euronext_paris` identity (Euronext Paris cash equities).
Euronext publishes one holiday calendar covering its cash markets with a per-market column
(Paris is the last column) on `live.euronext.com/en/resources/trading-hours-holidays`, plus a
per-year INFO-FLASH PDF, plus a **separate end-of-year appendix** to the Euronext Instructions
4-01/4-03 Trading Manuals that alone states the December half-day hours. The live page keeps
only the latest two years (2026 and 2025 today); 2027 is not published anywhere.

Retrieval session: **2026-09-28, 01:06-01:55 UTC** (LAW-UTC-DATES). `curl` with a desktop
browser User-Agent; no access control evaded; `connect2.euronext.com` file and
`www.euronext.com/media/...` fetched anonymously. `www.euronext.com` non-`/media` routes
returned a maintenance page during the session (recorded because it blocked two media links;
`/en/media/14656/download` was unaffected and served the XLSX directly).

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `trading-hours-holidays.live.html` | `https://live.euronext.com/en/resources/trading-hours-holidays` | 2026-09-28T01:07:28Z | `5a1165a52361a81350fa69401910c76f046f28e16f757dadb6d33d68ccb6e5e3` | 331382 | **T1, controlling for 2026 and corroboration for 2025.** Raw HTML of "Trading hours & Holidays". Carries the 2026 table ("2026 Holiday Calendar for Euronext's Cash and Derivatives markets", Paris column) and the rolling "Calendar of business days 2025" table; footnotes state that half-day hours are announced in an end-of-year appendix and that "2026 end of year Trading hours: To be announced". |
| `trading-hours-holidays.wayback-20251206154319id_.html` | `https://web.archive.org/web/20251206154319id_/https://live.euronext.com/en/resources/trading-hours-holidays` | 2026-09-28T01:50:03Z (capture 2025-12-06T15:43:19Z) | `dc96c4f7f1e6a51cd2e6743385faa5cbc4156623ec45499c89e2ec3871398a18` | 325268 | **T1 verbatim public mirror, controlling for 2025.** The page as served 2025-12-06: the 2025 table with the Paris column, plus the then-current "2025 end of year Trading hours" callout linking `www.euronext.com/media/14656/download` for the cash-markets end-of-year appendix. |
| `euronext_2025-end-of-year-appendix-instructions-4-01.live.xlsx` | `https://www.euronext.com/media/14656/download` (attachment name "Appendix...") | 2026-09-28T01:50:36Z | `5850b4b4f5a031e637a0c44a0c7c1388ddc638c652133e66636c674af19bb6b9` | 394852 | **T1, controlling for the 2025 half-day instants.** XLSX, "Appendix of Trading Manual 4-01", sheet 1 header: `24th and 31st of December 2025`, `Amsterdam, Brussels, Dublin, Lisbon, Milan, Oslo & Paris`. Paris `Equities`/CAC segments: OU `09:00 Random`, Trading `09:00 Random - 13:55`, CU `14:00 Random`, TAL `14:00 - 14:05` — i.e. the Paris availability envelope ends at CET 14:05:00. |
| `euronext_if251107_2026-holiday-calendar-cash-derivatives.live.pdf` | `https://connect2.euronext.com/sites/default/files/2025-11/IF251107CADE%202026%20Holiday%20Calendar%20for%20Euronexts%20Cash%20and%20Derivatives%20markets_1.pdf?VersionId=3ehe2.c9cMxv1K36.i6o4tz.5CAJmuw2` | 2026-09-28T01:09:41Z | `617bc559510ef3a3d86d4a8b804422d0ba4c4dae43782a0a728d57a23fc4b1c5` | 243065 | **T1, corroboration for 2026** (the live HTML page states the same rows). INFO-FLASH "2026 Holiday Calendar for Euronext's Cash and Derivatives markets", 3 pages, Paris column: 01-01 Closed, 04-03 Closed, 04-06 Closed, 05-01 Closed, 12-24 `**Half Trading Day`, 12-25 Closed, 12-31 `**Half Trading Day`; its footnote repeats that end-of-year hours "will be announced in an end of year appendix". Printed header date reads `07 November 2026` while the publishing path and file name say 2025-11-07; recorded as printed, cited only for the table cells. |

## Retrieval findings

- **2027 is not published.** The live page's newest calendar is the 2026 one; the INFO-FLASH
  PDF covers 2026; no 2027 edition exists on live.euronext.com (sitemap grep
  `holiday|calendar|trading-hours`, queried 2026-09-28T01:03Z). Coverage therefore stops at
  2026-12-31 for this identity.
- **2026-12-24 and 2026-12-31 are announced half days whose instants are not published.**
  Both the 2026 INFO-FLASH (`**Half Trading Day`) and the live page ("2026 end of year Trading
  hours: To be announced") withhold the hours. The 2025 appendix is the operator's own
  precedent, not evidence of 2026; nothing is inferred. Both dates ship as `Unsourced`, with
  the closing condition "the 2026 end-of-year appendix to the Euronext Instructions 4-01/4-03".
- The December half-day rows in the year tables are `**Half Trading Day` for **Paris** on
  2025-12-24, 2025-12-31 and 2026-12-24, 2026-12-31; the "Wednesday before Easter" half-day
  row is **Oslo only** and Paris prints `Full Trading Day` in both years.
- Dublin-only rows (Irish May Bank Holiday, St Stephen's Day substitute) print
  `Full Trading Day` for Paris; Milan/Oslo rows likewise do not touch Paris.
