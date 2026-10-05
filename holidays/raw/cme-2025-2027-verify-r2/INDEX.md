# INDEX — cme-2025-2027-verify-r2 (adversarial verifier, round 2)

Verifies `/Users/agedvagabond/Developer/exchange-hours-research/holidays/cme-2025-2027.json`
(round-1 output, sha256 `6bc718e5fbaea70c01f3bf54ccab156028eef9c28ce24357a5217c633b5d5771`) against
`../cme-2025-2027/` and `../cme-2025-2027-fix/`.

Evidence gathered **2026-09-12 (UTC; `date -u`)**. `MANIFEST.sha256` carries the sha256 of every file
in this directory. Every sha256 below is of the bytes as saved here.

cmegroup.com returns HTTP 403 to this machine directly. Live service calls were read through the public
reader `https://r.jina.ai/<url>`; history through the Wayback Machine with `id_` replay. Wayback `id_`
replay of this endpoint returns gzip-compressed original bytes; the `.json` files here are the
decompressions, which is what was parsed and compared.

## A. Re-fetches of documents the task cites (byte comparison)

Expand `[THBP-A]` to `https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true`
and `[THBP-B]` to the same with `id=168,167,320,323,19,27`.

| file | doc | url | capture / retrieval (UTC) | result |
|---|---|---|---|---|
| `arc/thbp_2025-01-19_2025-01-21_20241220155340.json` | D02 | `https://web.archive.org/web/20241220155340id_/[THBP-A]&fromEventDate=2025-01-19&toEventDate=2025-01-21&isProtected&_t=1734710019539` | captured 2024-12-20T15:53:40Z | **byte-identical** to saved (`4f2ab56a…`) |
| `arc/thbp_2025-07-03_2025-07-05_20241220155340.json` | D07 | same pattern, `&_t=1734710019545` | captured 2024-12-20T15:53:40Z | **byte-identical** (`b80cd4bf…`) |
| `arc/thbp_2025-11-26_2025-11-28_20260129012309.json` | D09 | `…/20260129012309id_/[THBP-A]&fromEventDate=2025-11-26&toEventDate=2025-11-28&isProtected&_t=1769649789739` | captured 2026-01-29T01:23:09Z | **byte-identical** (`6c4c5987…`) |
| `arc/thbp_2025-12-24_2025-12-26_20260129012159.json` | D10 | `…&_t=1769649719078` | captured 2026-01-29T01:21:59Z | **byte-identical** (`322a2be9…`) |
| `arc/thbp_2026-04-01_2026-04-03_20260619114118.json` | D14 | `…&_t=1749141516011` | captured 2026-06-19T11:41:18Z | **byte-identical** (`54bcc271…`) |
| `arc/thbp_2026-06-17_2026-06-19_20260129012310.json` | D16 | `…&_t=1769649789748` | captured 2026-01-29T01:23:10Z | **byte-identical** (`e4e2d5e4…`) |
| `live/D44.md` | D44 | `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?[THBP-A]&fromEventDate=2027-11-24&toEventDate=2027-11-26` | retrieved 2026-09-12T18:07Z | JSON body **byte-identical** (`6aa7c0fd…`) |
| `live/D46.md` | D46 | same, `2027-12-22..2027-12-25` | retrieved 2026-09-12T18:07Z | **byte-identical** (`5edc4dd5…`) |
| `live/D41.md` | D41 | `[THBP-B]&fromEventDate=2027-07-04&toEventDate=2027-07-06` | retrieved 2026-09-12T18:07Z | **byte-identical** (`1a955035…`) |
| `live/D52.md` | D52 | `[THBP-A]&fromEventDate=2026-11-27&toEventDate=2026-11-29` | retrieved 2026-09-12T18:08Z | **byte-identical** (`31c724b0…`) |

Ten documents re-fetched; ten byte-identical.

## B. Latest-capture check for the eight documents not taken from the latest capture

Each fetched at its window's latest capture and compared schedule-for-schedule over all 30
(product, eventDate) pairs.

| file | doc | latest capture | diffs vs the capture the task cites |
|---|---|---|---|
| `arc/latest/D11.20260722114222.json` | D11 | 2026-07-22T11:42:22Z | 0 |
| `arc/latest/D12.20260812185118.json` | D12 | 2026-08-12T18:51:18Z | 0 |
| `arc/latest/D13.20260812185118.json` | D13 | 2026-08-12T18:51:18Z | 0 |
| `arc/latest/D14.20260722114222.json` | D14 | 2026-07-22T11:42:22Z | 0 |
| `arc/latest/D15.20260722114222.json` | D15 | 2026-07-22T11:42:22Z | 0 |
| `arc/latest/D17.20260722114222.json` | D17 | 2026-07-22T11:42:22Z | 0 |
| `arc/latest/D18.20260129012310.json` | D18 | 2026-01-29T01:23:10Z | 0 |
| `arc/latest/D19.20260722114223.json` | D19 | 2026-07-22T11:42:23Z | 0 |

No superseded publication remains quoted.

## C. Fresh CDX enumeration

| file | url | retrieved (UTC) |
|---|---|---|
| `cdx/cdx_r2.json` | `https://web.archive.org/cdx/search/cdx?url=cmegroup.com/services/trading-hours-by-product*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&collapse=digest&limit=100000` | 2026-09-12T18:09Z |

688 rows, 56 distinct `fromEventDate/toEventDate` windows. Id sets seen: the ten-product THBP-A set (669),
no-id filter queries (16), and three singletons (`id=316`, `id=5224`, `id=318`). The THBP-B id set
(`168,167,320,323,19,27`) appears nowhere — the task's claim about the archive is correct.

Captures covering each 2025 holiday (independently reproduced, matching `../cme-2025-2027-fix/INDEX.md`):

| holiday | covering captures | latest |
|---|---|---|
| New Year 2025 | 2 | 2024-12-20T15:53:40Z |
| MLK / Presidents' / Good Friday / Memorial / Juneteenth / Independence / Labor 2025 | 1 each | 2024-12-20T15:53:40Z |
| Thanksgiving 2025 | 45 | 2026-01-29T01:23:09Z |
| Christmas 2025 | 45 | 2026-01-29T01:23:09Z |
| New Year 2026 | 51 | 2026-07-22T11:42:22Z |
| **Saturday 2025-11-29** | **0 — no archived window covers it** | — |

`arc/w7_20260711.json` is the one later (2026-07-11) capture touching Good Friday 2026, a single-product
(`id=5224`, Micro Gold) query over 2026-04-01..2026-04-07. It shows MGC with no events on Saturday
2026-04-04, corroborating the task's "no Saturday session after Good Friday 2026".

## D. Live-service probes — the channel-availability claims

All read through `r.jina.ai` on **2026-09-12T18:10–18:14Z**. "events" is the total event count returned.

| file | window | id set | events |
|---|---|---|---|
| `live/probeA_2024-12-31_2025-01-02.md` | New Year 2025 | A | **0** |
| `live/probeA_2025-01-19_2025-01-21.md` | MLK 2025 | A | **0** |
| `live/probeA_2025-02-16_2025-02-18.md` | Presidents' 2025 | A | **0** |
| `live/probeA_2025-04-17_2025-04-19.md` | Good Friday 2025 | A | **0** |
| `live/probeA_2025-05-25_2025-05-27.md` | Memorial 2025 | A | **0** |
| `live/probeA_2025-06-18_2025-06-20.md` | Juneteenth 2025 | A | **0** |
| `live/probeA_2025-07-03_2025-07-05.md` | Independence 2025 | A | **0** |
| `live/probeA_2025-08-31_2025-09-02.md` | Labor 2025 | A | **0** |
| `live/probeA_2025-11-26_2025-11-29.md` | Thanksgiving 2025 **incl. Sat 29 Nov** | A | **75** |
| `live/probeA_2025-12-24_2025-12-26.md` | Christmas 2025 | A | **52** |
| `live/probeA_2026-04-02_2026-04-04.md` | Good Friday 2026 + Saturday | A | 34 |
| `live/probeA_2026-06-17_2026-06-19.md` | Juneteenth 2026 | A | **80** |
| `live/probeA_2026-07-02_2026-07-04.md` | Independence 2026 | A | **55** |
| `live/probeB_2025-07-03_2025-07-05.md` | Independence 2025 | B | **0** |
| `live/probeB_2025-11-26_2025-11-29.md` | Thanksgiving 2025 | B | **47** |
| `live/probeB_2025-12-24_2025-12-26.md` | Christmas 2025 | B | **40** |
| `live/probeB_2025-12-31_2026-01-02.md` | New Year 2026 | B | **48** |
| `live/probeB_2026-01-18_2026-01-20.md` | MLK 2026 | B | **46** |
| `live/probeB_2026-02-15_2026-02-17.md` | Presidents' 2026 | B | **46** |
| `live/probeB_2026-04-01_2026-04-03.md` | Good Friday 2026 | B | **60** |
| `live/probeB_2026-05-24_2026-05-26.md` | Memorial 2026 | B | **46** |
| `live/probeB_2026-06-17_2026-06-19.md` | Juneteenth 2026 | B | **60** |
| `live/probeB_2026-06-18_2026-06-20.md` | Juneteenth 2026 (eve window) | B | **32** |
| `live/probeB_2026-07-02_2026-07-04.md` | Independence 2026 | B | **32** |
| `live/probeB_2026-07-03_2026-07-05.md` | Independence 2026 | B | **16** |
| `live/filters_r2.md` | `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-filters` | — | 14 forward holidays, 2026-09-07 .. 2028-01-01 |

The task states repeatedly that "the live service carries only FORWARD holidays" and that "past holidays
are dropped". That is true only back to Labor Day 2025. From Thanksgiving 2025 forward the service still
serves the window, for **both** id sets. Discrepancies 1, 2 and 3 in the verdict rest on these bytes.
