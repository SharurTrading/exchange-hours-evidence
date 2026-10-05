# INDEX - adversarial verification of gate btic-non-equity-groups

All fetches via the public text reader in front of cmegroup.com (https://r.jina.ai/<url>).
Capture date of every row below: 2026-09-11T23:44Z..23:47Z UTC (local date 2026-09-12).

| file | URL | capture_ts (UTC) | bytes | sha256 |
|---|---|---|---|---|
| v-specs-33-GD.txt | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/33 | 2026-09-11T23:44:31Z | 2509 | 3881dce066c2d4363acdab31f6004bbe8a211eb724fceb21a207cc078806158d |
| v-svc-8634-NKT-2025-11-29.json | https://www.cmegroup.com/services/trading-hours-by-product?id=8634&pageSize=500&fromEventDate=2025-11-29&toEventDate=2025-12-13 | 2026-09-11T23:44:45Z | 6337 | 884d14520e981a4f3f7045e66005ad34fce97c48f12281b9a7a5e38fd541f1c8 |
| v-svc-8634-NKT-2026-02-07.json | https://www.cmegroup.com/services/trading-hours-by-product?id=8634&pageSize=500&fromEventDate=2026-02-07&toEventDate=2026-02-21 | 2026-09-11T23:44:51Z | 5656 | b2ca38821269f9340dbf7beda384b02ed7287fe2bf25673f7f8b60026188b090 |
| v-svc-8634-NKT-2026-06-06.json | https://www.cmegroup.com/services/trading-hours-by-product?id=8634&pageSize=500&fromEventDate=2026-06-06&toEventDate=2026-06-20 | 2026-09-11T23:44:58Z | 5883 | 5f3ab0e695bbd403841338168e283ea634e9e54231a345e7bb6785bfb00effad |
| v-svc-10185-BNB-2025oct.json | https://www.cmegroup.com/services/trading-hours-by-product?id=10185&pageSize=500&fromEventDate=2025-10-26&toEventDate=2025-11-07 | 2026-09-11T23:46:29Z | 3504 | d3d73cb0e169658a6f1eaeabf2fe19e397230eae45450dd33e499f1d89369e56 |
| v-svc-8970-BTB-2025oct.json | https://www.cmegroup.com/services/trading-hours-by-product?id=8970&pageSize=500&fromEventDate=2025-10-26&toEventDate=2025-11-07 | 2026-09-11T23:46:35Z | 5919 | 417ceb26544b10028cfeb4f4d652dea01b86f59b51c8b2e392f4d718152c6332 |
| v-svc-10664-ABB-2025oct.json | https://www.cmegroup.com/services/trading-hours-by-product?id=10664&pageSize=500&fromEventDate=2025-10-26&toEventDate=2025-11-07 | 2026-09-11T23:46:41Z | 5965 | d7bb7c9ff74b1bc9b28e21275603f2603cd8b9f45eec7a3d4e176c10db196db2 |

Notes:
- v-specs-33-GD.txt is byte-identical (sha256 3881dce0...) to the researcher's r2-specs-33-GD.txt captured 2026-09-11T23:16:03Z.
- The three v-svc-8634 windows add 9 further Saturdays to the 7 the gate captured; all carry open@05:00 / closed@17:00 with a forward trade date.
- v-svc-8970 / v-svc-10664 (2025-10-26..2025-11-07) are PRE-cutover (era 2) and show a Saturday 05:00->17:00 CT block on 2025-11-01 for BTB and ABB; v-svc-10185 (BNB) has no Saturday events in the same window.
