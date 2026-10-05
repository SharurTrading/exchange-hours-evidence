<!-- SPDX-License-Identifier: MIT-0 -->
# Verifier evidence — gate U8-cross-zone-design

Two verification passes have written into this directory. The 2026-09-06 **second** pass
(adversarial re-verification of the researcher's second-pass result) added the rows below;
earlier rows from the first pass are retained.

| file | URL | capture (UTC) | artifact date | note |
|---|---|---|---|---|
| `hgf-oct.txt` | https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=8652&fromEventDate=2026-10-26&toEventDate=2026-10-30&pageSize=100 | 2026-09-06 | CME published calendar, trade dates 2026-10-26..30 | **NEW first-hand measurement.** `globex":"HGF","prodGroup":"TR","name":"Copper London TAM"`, 5x `closed@07:35`, 4x `preopen@16:50`, 4x `open@17:00`. Closes the researcher's second-hand HGF row on the misaligned side. |
| `hgf-dec.txt` | same service, id=8652, 2026-12-07..2026-12-11 | 2026-09-06 | CME published calendar, trade dates 2026-12-07..11 | 5x `closed@06:35`. The aligned side. Together these measure HGF's 06:35/07:35 pair first-hand. |
| `verify_u8.py` / `verify_u8.out.txt` | local, no network (IANA tz database via CPython `zoneinfo`) | 2026-09-06 | derived | Third independent re-derivation, written without reference to either `drift-computation.py` or `recheck-2026-09-06b.py`, and using **absolute-instant conversion** rather than delta arithmetic. Reproduces: two offset states per zone pair 2010–2030; every Chicago clock pair; the 241/20 and 170/91 weekday splits over 261 weekdays; 28 calendar / 20 weekdays of 2026 misalignment; `America/New_York` constant at 1.0. Also **bisects the DST transition instants to the minute**, correcting the tilde-approximations both prior scripts printed: UK 2026-10-25 01:00 UTC = **2026-10-24 20:00 CDT** (not 19:00), US 2026-03-08 08:00 UTC = 03:00 CDT. |
| `svc-8407-dec.refetch.txt`, `faq.refetch.txt`, `svc-7956-oct.refetch.txt` | the researcher's own three URLs, re-fetched live | 2026-09-06 | as stored | **Byte-identical** to the stored artifacts: `0917c5f9…`, `5b623062…`, `b86f4f02…`. |

Verdict: `../../U8-cross-zone-design.verify.json` (matches=false; evidence base clean, two
load-bearing defects in the encodable/structural claims — see D1 and D2 there).
