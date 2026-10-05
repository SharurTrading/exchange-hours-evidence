# Evidence index — `equities/lse/2025-2027`

Primary-source retrieval for the `lse` identity (London Stock Exchange, SETS). The operator's
holiday statement is the "Bank holidays and their impact on our trading services" table on the
SPA page `londonstockexchange.com/equities-trading/business-days`, delivered by its content API
`api.londonstockexchange.com/api/v1/pages?path=equities-trading/business-days`. The table is
**rolling**: the live page lists only business days from today forward (currently
2026-08-31 .. 2029-01-01), so 2025 and the first half of 2026 are re-verifiable only through
archived captures of the same API URL (Wayback `id_` replay returns the raw archived JSON).

Retrieval session: **2026-09-28, 01:06-01:40 UTC** (LAW-UTC-DATES). `curl` with a desktop
browser User-Agent; no access control evaded. `web.archive.org` was intermittently offline
during the session (CDX 504s, "Temporarily Offline" pages); successful queries needed retries.

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `business-days.api.live.json` | `https://api.londonstockexchange.com/api/v1/pages?path=equities-trading/business-days` | 2026-09-28T01:16:12Z | `4f9f6f3aef9ab02874112c05c0c07ac4529e6c38e7ad74d0aa41735853a87a7f` | 41846 | **T1, controlling for 2026-08-31 .. 2027-12-31.** CMS JSON, component `Business days - Table 1`, HTML table titled "Bank holidays and their impact on our trading services". Rows 2026-08-31 .. 2029-01-01: `NON-trading day.` closures and `Christmas/New Year's Holiday half day` rows stating `Markets closing process commences from 12:30 London time.` |
| `business-days.api.wayback-20251218172240id_.json` | `https://web.archive.org/web/20251218172240id_/https://api.londonstockexchange.com/api/v1/pages?path=equities-trading/business-days&parameters=` | 2026-09-28T01:30:43Z (capture 2025-12-18T17:22:40Z) | `e7d81b189bd75137b2e51136b2d6979d780dd3d50b95c111ef5acbdd38d49a11` | 41928 | **T1 verbatim public mirror, controlling for 2025-12-24 .. 2027-12-31.** The same table as served 2025-12-18: 2025 Christmas half day/closures, the whole 2026 set (01-01, 04-03, 04-06, 05-04, 05-25, 08-31, 12-24 half, 12-25, 12-28, 12-31 half) and the whole 2027 set. |
| `business-days.api.wayback-20260617134453id_.json` | `https://web.archive.org/web/20260617134453id_/https://api.londonstockexchange.com/api/v1/pages?path=equities-trading/business-days&parameters=` | 2026-09-28T01:30:44Z (capture 2026-06-17T13:44:53Z) | `1759a375014f079d7725ac0c08293073d9d27c8d9a28e1999d7f611d7145270a` | 42389 | **T1 verbatim public mirror, corroboration.** Table as served 2026-06-17: 2026-05-04 .. 2029-01-01. Agrees row for row with the live JSON and the 2025-12-18 capture on every overlapping row. |
| `business-days.api.wayback-20240207115235id_.json` | `https://web.archive.org/web/20240207115235id_/https://api.londonstockexchange.com/api/v1/pages?path=equities-trading/business-days&parameters=` | 2026-09-28T01:28:15Z (capture 2024-02-07T11:52:35Z) | `4730c509be75be779d106ccad036eae4f515bc6524613951126b33491b40a90b` | 37254 | **T1 verbatim public mirror.** Table as served 2024-02-07 (2024-03-29 .. 2025-01-01). Supplies the single 2025 row this crate encodes from it: `Wednesday 1 January 2025 - New Year Day - NON-trading day.` |
| `business-days.api.wayback-20240308200156id_.json` | `https://web.archive.org/web/20240308200156id_/https://api.londonstockexchange.com/api/v1/pages?path=equities-trading/business-days&parameters=` | 2026-09-28T01:36:09Z (capture 2024-03-08T20:01:56Z) | `dbcdccd7ef5bae333856d86819ad9f1908df3b5bab4fa6354e891d3ce99300db` | 37225 | **T1 verbatim public mirror, corroboration only** (same horizon as the February capture; confirms 2025-01-01 and no further 2025 rows were listed). |

## Retrieval findings

- The Wayback CDX index holds **exactly four** captures of the business-days API URL
  (`filter=original:.*business-days.*` over `api.londonstockexchange.com/api/v1/pages*`,
  queried 2026-09-28 ~01:25 UTC): 2024-02-07, 2024-03-08, 2025-12-18, 2026-06-17. The gap
  2025-01-02 .. 2025-12-17 has no capture, so the 2025-04-18, 2025-04-21, 2025-05-05,
  2025-05-26 and 2025-08-25 rows of the operator's rolling table are **not re-verifiable
  from any archived or live artifact** today — they left the live page as it rolled forward.
  T3 restatements (mrtopstep.com, ebc.com, apricotcapital.am, found by web search) exist but
  cannot key rows (LAW-PRIMARY-SOURCES). Those five dates ship as `Unsourced`.
- archive.today holds no snapshot of the page ("No results", checked 2026-09-28T01:40Z).
- The SPA HTML shell is useless for evidence (content is client-rendered from the API);
  no shell was archived here deliberately.
- `docs.londonstockexchange.com` "Millennium Exchange and TRADEcho Business Parameters"
  XLSX (2026-07-27, v10.0) was checked for a business-days sheet: it has none
  (sheets: Summary, Trading Service Breakdown, ... Trading Cycles, Price Format, ...).
