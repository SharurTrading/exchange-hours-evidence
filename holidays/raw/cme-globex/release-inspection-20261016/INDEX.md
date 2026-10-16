# INDEX — October-2026 Saturday-extension confirmations (release-month follow-up)

Retrieval session: **2026-10-16 02:4x UTC** (`date -u`), one targeted pass (LAW-BOUNDED-WORK).
`cmegroup.com` 403s this machine (proved negative, prior waves), so the live read went through the
public reader `https://r.jina.ai/<url>`; the digest is of the saved file.

## Artifacts

| file | query | purpose |
|---|---|---|
| `thbp_oct2026_sat.raw` | `[THBP-A]` with `&fromEventDate=2026-10-03&toEventDate=2026-10-05` | post-effective-day confirmation of the 2026-10-03 Saturday maintenance-window extension (Globex notice 20260921) |

`[THBP-A]` = `https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true`
(same ten product groups and parameter shape as the stored waves).

## Reading

`hasEvents: true`. **Bitcoin Futures (`BTC`, id 8478), event date 2026-10-03**: `02:00 closed`,
`04:45 preopen`, `05:00 open`, all three carrying trade date 2026-10-05 — the Saturday maintenance
window closed at its standard 02:00 CT boundary and the market reopened at **05:00 CT**, exactly the
extension window notice 20260921 states (02:00–05:00 CT), with the 04:45 pre-open the same notice
class implies. This confirms the 2026-10-03 forward-dated row **effective** for `globex_cryptocurrency`
and `globex_silver_100oz`, discharging each row's confirm-by obligation (LAW-WATCH) — the same shape
that discharged the 2026-09-19 row in `release-inspection-20260928/thbp_sep2026_sat.raw`.

The other nine product groups answer their ordinary grids for the window (no Saturday events — the
extension is the 24/7 class's alone), and the Sunday/Monday events on 2026-10-04/05 match the served
weeks (BTC 16:00 closed / 16:01 preopen / 16:02 open on the 24/7 grid; ZC's Sunday 19:00 open and
weekday queues unchanged).
