# Evidence index — `normal-weeks/nyse-american-options-eth-2026-11-14`

Normal-week captures for NYSE American Options **Extended Trading Hours (ETH)**,
which went live 2026-10-19 and changes the dormant `nyse_american_options`
identity's session shape for all dates from then on.

Retrieval session: **2026-11-14 07:12–07:14 UTC** (LAW-UTC-DATES). `curl` with a
desktop browser User-Agent; no access control evaded.

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `NYSE_American_Options_Extended_Trading_Hours_Fact_Sheet.pdf` | `https://www.ice.com/publicdocs/nyse/notifications/trader-update/110000958754/NYSE_American_Options__Extended_Trading_Hours_Fact_Sheet.pdf` | 2026-11-14T07:12:11Z | `5041066e0cac0ffd3ef3dbdf1c25cb8cb8b086741de33eae66ac7026269b2354` | 199233 | **T1, controlling.** "NYSE American Options Extended Trading Hours Fact Sheet", v 1.3, October 2026. Adds "an Early Trading Session from 7:30 AM to 9:25 AM and a Late Trading Session from 4:00 PM to 4:15 PM. The Core Trading Session will remain unchanged"; session overview prints "Pre-Open - 6:00 AM to 7:30 AM - Open for connectivity and order entry", the Early and Late sessions marked `*New*`, Core 9:30 AM–4:00 PM (4:15 PM eligible); Implementation Schedule line "Production Symbols: Monday, October 19, 2026"; "Holidays: No trading sessions on holidays"; shortened-day rows Core 9:30 a.m.–1:00 p.m. (1:15 p.m.) and Late 1:00–1:15 p.m. |
| `nyse-trader-updates-api-110000960906.json` | `https://www.nyse.com/api/notifications/public/system/1/summaries/filter?pageSize=100&pageNumber=1&sortKey=publishedDate&sortOrder=desc` | 2026-11-14T07:14:22Z | `a05beb48380b5c037ac5c1f2a43337f9584048f9206f3241abe83efa734971ad` | 166207 | **T2, the operator's own notification feed.** Page 1 (newest 100) carries notice id `110000960209`, published 2026-09-18T21:22:04Z, "NYSE American Options: Extended Trading Hours Updates", whose body states "Effective Monday, October 19, 2026, NYSE American Options will introduce Extended Trading Hours ("ETH") for eligible Production symbols, pending regulatory effectiveness" and names the fact sheet. The earlier go-live trader update (id `110000960906`, "Go-Live October 19 | Final Test October 17") published 2026-10-14T18:52:10Z and observed in the 2026-11-12 sweep, does not sit inside the API's newest-100 window at this retrieval; the addressable page is `https://www.nyse.com/trader-update/history#110000960906` and a re-capture is the closing condition for citing it directly. |

## Retrieval findings

- The unconditional production day (2026-10-19) is stated by the banked fact
  sheet itself ("Production Symbols: Monday, October 19, 2026"); the 2026-09-18
  alert's "pending regulatory effectiveness" clause is discharged by the fact
  sheet's later October 2026 publication describing the live sessions.
- The 6:00 a.m. pre-open queue is unchanged; what is new is the queue draining
  into the 7:30 Early session for eligible symbols, plus the 4:00–4:15 p.m. Late
  session.
