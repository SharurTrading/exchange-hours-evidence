# ag-crypto-tas-history — adversarial verification pass capture index

Verifier re-fetches, 2026-09-12. Capture timestamps date the observation, never the state.
Per-file sha256 in `SHA256SUMS.txt`.

| file | URL | capture ts (UTC) | result |
|---|---|---|---|
| `v_corn2015.html` | `https://web.archive.org/web/20150905110358id_/http://www.cmegroup.com/trading/agricultural/grain-and-oilseed/corn_contract_specifications.html` | 2026-09-12 | byte-identical to `pass2/corn-legacy-20150905110358.html` (sha256 e9b9e69a…) |
| `v_corn20150522.html` | `https://web.archive.org/web/20150522230148id_/…/corn_contract_specifications.html` | 2026-09-12 | **NOT identical** to `pass2/corn-legacy-20150522230148.html`. The stored file is Internet Archive chrome; this is the real CME capture (83,721 bytes, sha256 fd5f67b3…), 0 case-sensitive `TAS`, outright `Monday – Friday, 8:30 a.m. – 1:15 p.m. CT` |
| `v_lc2015.html` | `https://web.archive.org/web/20150905203207id_/…/live-cattle_contract_specifications.html` | 2026-09-12 | byte-identical to `pass2/lc-legacy-20150905.html` (sha256 83c49520…) |
| `v_23017.pdf` | `https://web.archive.org/web/2026id_/https://www.cmegroup.com/content/dam/cmegroup/market-regulation/rule-filings/2023/1/23-017.pdf` | 2026-09-12 | byte-identical to `filings2023/23-017.pdf` (sha256 fe356694…) |
| `v_cs300.txt` | `https://r.jina.ai/https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/300` | 2026-09-12 | byte-identical to `pass2/cs-300-live.txt`; TAS line `Sunday - Friday 7:00 p.m. - 7:45 a.m. and Monday - Friday 8:30 a.m. - 1:15 p.m. CT` |
| `v_cs8478.txt` | `…/ContractSpecs/List/productId/8478` | 2026-09-12 | byte-identical to `pass2/cs-8478-live.txt`; TAS line `24/7 … Saturday 2:00 a.m. to 4:00 a.m. CT & Monday-Friday from 3:00 p.m. to 3:05 p.m. CT` |
| `v_ser9740r.txt` | `https://r.jina.ai/https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2026/05/ser-9740r.pdf` | 2026-09-12 | independently re-fetched; 0 case-insensitive `TAS` |
| `v_ch5.txt` | `https://r.jina.ai/https://www.cmegroup.com/rulebook/CME/I/5/5.pdf` | 2026-09-12 | CME Rulebook Chapter 5 (51pp). Rule 524.A.1: "A TAS order may be entered on Globex at any time the applicable contract is available for TAS trading on Globex and during such TAS-eligible contract's prescribed pre-open time period." No clock time; the TAS/BTIC/TACO/TMAC Table is an external XLS. Channel not listed in the researcher's dead_ends; it does NOT close the grain-TAS Pre-Open residual |

CDX re-runs (not saved as files):
- fact-card PDF: exactly three distinct 200 digests (YOU6E…@20150616, 5VD5F…@20200608/20200929/20210507, GTCPA…@20231118) — but with a five-year archive hole 2015-06-16 → 2020-06-08.
- `tas-on-cryptocurrency-futures.html` with `collapse=digest`: exactly 16 rows; last pre-cutover 20260209183250, first post-cutover 20260610025555.
- corn spec page 2015 range: `20150522230148 200 6HB5XFH6EGKXEU62EAUJXJ4SLMQ26J2Z 14806` — a real capture exists at the timestamp the researcher cited.
