# INDEX — cme-2025-2027 repair round, 2026-09-12 (UTC)

Evidence retrieved to repair the four material findings in
`../../cme-2025-2027.verify.json` (round 2). Every artifact below is CME Group's own
trading-hours service — the endpoint `https://www.cmegroup.com/trading-hours.html` itself
calls to render its per-asset-class Holiday Hours table — read live on 2026-09-12 (UTC)
through the public reader `https://r.jina.ai/<url>` because cmegroup.com refuses this
machine directly (HTTP 403). Tier **T2** under LAW-PRIMARY-SOURCES: the operator's own
machine channel, read as bytes and saved.

**The premise this round refutes.** The task and its round-1 fix asserted that the service
"carries only FORWARD holidays" and that "past holidays are dropped". It does not. CME's
forward holiday *list* (`services/trading-hours-filters`) starts at Labor Day 2026-09-07,
but `services/trading-hours-by-product` still answers for past windows back to Thanksgiving
2025. Every window below was retrieved live on 2026-09-12, and the earliest of them,
`fromEventDate=2025-11-26`, is nine and a half months past. Windows through Labor Day 2025
still return the products with empty schedules, so the retention edge falls between Labor
Day 2025 and Thanksgiving 2025.

**Product id sets.** `[THBP-A]` = `id=316,133,425,300,58,437,22,8478,5201,10191`
(ES, ZN, 6E, CL, GC, ZC, LE, CSC, BTC, LBR — the ten CME's own trading-hours page queries).
`[THBP-B]` = `id=168,167,320,323,19,27` (NKD, NIY, ZS, ZW, HE, DC). Both are queried with
`&pageNumber=1&pageSize=999&sortAsc=true`.

## Artifacts

| Doc | File | Set | Window | Retrieved (UTC) | Bytes | sha256 |
|---|---|---|---|---|---|---|
| `D54` | `live/probeB_2025-11-26_2025-11-29.md` | THBP-B | `2025-11-26..2025-11-29` | 2026-09-12T08:54:32Z | 6500 | `50da5636342b8352826debc016850594cc84bc2d50ac0f3121f1c79843435fa2` |
| `D55` | `live/probeB_2025-12-24_2025-12-26.md` | THBP-B | `2025-12-24..2025-12-26` | 2026-09-12T08:54:56Z | 5631 | `11dc4de5bf662e60d6bf71e37adb6247e217433991e1b29af0cbbf973c9288fd` |
| `D56` | `live/probeB_2025-12-31_2026-01-02.md` | THBP-B | `2025-12-31..2026-01-02` | 2026-09-12T08:54:57Z | 6230 | `c558c9f399eb1b83b55f6dd1c00dac81a8a55e8d25b5eaa9cecd1b6bb229a216` |
| `D57` | `live/probeB_2026-01-18_2026-01-20.md` | THBP-B | `2026-01-18..2026-01-20` | 2026-09-12T08:54:58Z | 6080 | `15f55c10115e7a37cf85f0583e577c2fb7421b08a545ee03f3c0261e46c5d09d` |
| `D58` | `live/probeB_2026-02-15_2026-02-17.md` | THBP-B | `2026-02-15..2026-02-17` | 2026-09-12T08:54:58Z | 6080 | `5bbecf07eecbdb2dbe5325f39f6b464bf817f535d38841fccdafef19103aaef0` |
| `D59` | `live/probeB_2026-04-01_2026-04-03.md` | THBP-B | `2026-04-01..2026-04-03` | 2026-09-12T08:55:08Z | 7139 | `b4569c685450baab17749fbed20c8c0e37c40910b77c411f72b6c596cd3c0567` |
| `D60` | `live/probeB_2026-05-24_2026-05-26.md` | THBP-B | `2026-05-24..2026-05-26` | 2026-09-12T08:55:09Z | 6080 | `3c7628b898d8069067836a36c44769f2f2b76a1dee5edbd48225f76b363881d0` |
| `D61` | `live/probeB_2026-06-17_2026-06-19.md` | THBP-B | `2026-06-17..2026-06-19` | 2026-09-12T08:55:09Z | 7139 | `444abf5a4c5886ff7d853ef513f9953a89ceec3074a65b6c8e35c8680e696a57` |
| `D62` | `live/probeB_2026-06-18_2026-06-20.md` | THBP-B | `2026-06-18..2026-06-20` | 2026-09-12T08:55:10Z | 5028 | `41791460e029bb7db0d280374048c36f015594fb71e9f1aae86a6145429ce2e5` |
| `D63` | `live/probeB_2026-07-02_2026-07-04.md` | THBP-B | `2026-07-02..2026-07-04` | 2026-09-12T08:55:11Z | 5028 | `5b701f1211cc4f86d0bed244d741797e8215ed2f087b993456485669f619e50a` |
| `D64` | `live/probeB_2026-07-03_2026-07-05.md` | THBP-B | `2026-07-03..2026-07-05` | 2026-09-12T08:55:11Z | 3822 | `dfc4aff36f0e44fb8fdb78de59d13bad90707c0d108673094ad0a012cefad898` |
| `D65` | `live/probeA_2025-11-26_2025-11-29.md` | THBP-A | `2025-11-26..2025-11-29` | 2026-09-12T08:55:12Z | 10315 | `2e9f34f20085de3ccbdff1dc29cb7463bcff93713ef0c550740d6f15e0635ab7` |
| `D66` | `live/probeA_2026-06-17_2026-06-19.md` | THBP-A | `2026-06-17..2026-06-19` | 2026-09-12T08:55:13Z | 10129 | `f9ee38678821e32e8f54f8084366024173462b108376658be423581c1ba77e09` |
| `D67` | `live/probeA_2026-07-02_2026-07-04.md` | THBP-A | `2026-07-02..2026-07-04` | 2026-09-12T08:55:14Z | 8239 | `0e8b38b67779644a22d41de94e315e599198d6c8c739ef35196163779aacfd4b` |

## Re-fetch URLs (verbatim, one step)

- `D54` — Thanksgiving 2025 window incl. Saturday 2025-11-29 - NKD, NIY, ZS, ZW, HE, DC
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-11-26&toEventDate=2025-11-29`
- `D55` — Christmas 2025
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-12-24&toEventDate=2025-12-26`
- `D56` — New Year's Day 2026
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-12-31&toEventDate=2026-01-02`
- `D57` — Martin Luther King Jr. Day 2026
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-01-18&toEventDate=2026-01-20`
- `D58` — Presidents' Day 2026
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-02-15&toEventDate=2026-02-17`
- `D59` — Good Friday 2026
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-04-01&toEventDate=2026-04-03`
- `D60` — Memorial Day 2026
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-05-24&toEventDate=2026-05-26`
- `D61` — Juneteenth 2026, eve window
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-06-17&toEventDate=2026-06-19`
- `D62` — Juneteenth 2026, holiday + Saturday window
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-06-18&toEventDate=2026-06-20`
- `D63` — Independence Day 2026, eve window
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-07-02&toEventDate=2026-07-04`
- `D64` — Independence Day 2026, holiday + Saturday window
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-07-03&toEventDate=2026-07-05`
- `D65` — Thanksgiving 2025 window extended to Saturday 2025-11-29 - ten-product set
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-11-26&toEventDate=2025-11-29`
- `D66` — Juneteenth 2026 eve window - post-24/7 Cryptocurrency publication for 2026-06-17
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-06-17&toEventDate=2026-06-19`
- `D67` — Independence Day 2026 eve window - post-24/7 Cryptocurrency publication for 2026-07-02
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-07-02&toEventDate=2026-07-04`

## Derived files

`json/<name>.json` is the JSON body of each reader response, extracted verbatim from the
`Markdown Content:` section of the corresponding `live/<name>.md` and re-serialised with
`indent=1` for readability. The `.md` files are the retrieved bytes and are what the sha256
column above hashes; the `json/` files are derived and are hashed separately below.

## New note code defined in this round

- `N19` — 24/7 Cryptocurrency grid on a **Friday** holiday: the 16:00 CT final-close event
  *is* published, but it carries the **following Monday's** trade date, so the holiday's own
  trade date has no session and no settlement of its own and the whole day rolls into the
  next business date. Distinct from `N10`, where on a Monday or Thursday holiday the 16:00 CT
  event is omitted altogether. Distinct from `N8` (genuinely normal), because on a normal
  Friday the 16:00 CT close carries **that Friday's** trade date — verified against the
  reference week in `../cme-2025-2027/live/normal/normalweek_main.json`, where BTC on Friday
  2026-10-23 prints `16:00 closed /TD 2026-10-23; 16:01 preopen /TD 2026-10-26;
  16:02 open /TD 2026-10-26`.


## Appendix — retention-edge probes (negative results)

These eight windows are the 2025 holidays New Year through Labor Day, queried live with the
`[THBP-B]` id set on 2026-09-12. Each returns all six products with an **empty** `schedules`
event list (6 products, 0 events), which is where the service's retention edge falls: every
window from Thanksgiving 2025 forward returns a full schedule, every window through Labor Day
2025 returns nothing. They key no row; they are the evidence for the re-scoped `missing[]`
entries 0 and 1, and they are why those eight holidays' Nikkei / ZS / ZW / HE / DC lines stay
unsourced.

| File | Window | Retrieved (UTC) | Bytes | sha256 |
|---|---|---|---|---|
| `live/edgeB_2024-12-31_2025-01-02.md` | `2024-12-31..2025-01-02` | 2026-09-12T09:01:07Z | 2625 | `0a60ca31d54ade2c4c428b49b1b38813faefb03356c3691f678ff341341f1710` |
| `live/edgeB_2025-01-19_2025-01-21.md` | `2025-01-19..2025-01-21` | 2026-09-12T09:01:08Z | 2625 | `ab4a3d54197a9a8448e3df7f4de3faa46e2a3dbf45adf8bfceb6e6b4162ae74a` |
| `live/edgeB_2025-02-16_2025-02-18.md` | `2025-02-16..2025-02-18` | 2026-09-12T09:01:09Z | 2625 | `6f453d5a822036c1220f6809221f88cd2e02730dde827887c10ce15fa79e263f` |
| `live/edgeB_2025-04-17_2025-04-19.md` | `2025-04-17..2025-04-19` | 2026-09-12T09:01:10Z | 2625 | `33d94c6688ce0017926747aa4e69136e216cc2eaa2da776ce3e413405f872b9b` |
| `live/edgeB_2025-05-25_2025-05-27.md` | `2025-05-25..2025-05-27` | 2026-09-12T09:01:11Z | 2625 | `4c9a3e73781994fa09ae42b3a967dcc85a93dc26495912332ecd88e5d399031d` |
| `live/edgeB_2025-06-18_2025-06-20.md` | `2025-06-18..2025-06-20` | 2026-09-12T09:01:11Z | 2625 | `ba8e2857b7c71600c2c29e5dd1956489b5bb51df6d67800cf377a08859238e2f` |
| `live/edgeB_2025-07-03_2025-07-05.md` | `2025-07-03..2025-07-05` | 2026-09-12T09:01:12Z | 2625 | `a2147f38ea27284fc1e1418c3f147da75ff65377778fa24be7bf29b415a77409` |
| `live/edgeB_2025-08-31_2025-09-02.md` | `2025-08-31..2025-09-02` | 2026-09-12T09:01:13Z | 2625 | `ba5a1ca356133eecbb3eb826cbb9382d14087d3c884863c3288837b81535ad9e` |

Re-fetch URLs:

- `edgeB_2024-12-31_2025-01-02.md`
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2024-12-31&toEventDate=2025-01-02`
- `edgeB_2025-01-19_2025-01-21.md`
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-01-19&toEventDate=2025-01-21`
- `edgeB_2025-02-16_2025-02-18.md`
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-02-16&toEventDate=2025-02-18`
- `edgeB_2025-04-17_2025-04-19.md`
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-04-17&toEventDate=2025-04-19`
- `edgeB_2025-05-25_2025-05-27.md`
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-05-25&toEventDate=2025-05-27`
- `edgeB_2025-06-18_2025-06-20.md`
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-06-18&toEventDate=2025-06-20`
- `edgeB_2025-07-03_2025-07-05.md`
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-07-03&toEventDate=2025-07-05`
- `edgeB_2025-08-31_2025-09-02.md`
  - `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-08-31&toEventDate=2025-09-02`


## Output of this round

| File | Role | sha256 |
|---|---|---|
| `../../cme-2025-2027.json` | the repaired payload (31 holidays, 367 family rows) | `e4a5b242ee4fac2eff162c366f348ea52a168c9a06cde5e500f8f5a2a36ea91e` |
| `../../cme-2025-2027.r2.json` | the payload this round supersedes, kept verbatim; byte-identical to what `cme-2025-2027.verify.json` verified | `6bc718e5fbaea70c01f3bf54ccab156028eef9c28ce24357a5217c633b5d5771` |
| `../../../holiday-tables/DECISIONS.md` | the implementation choices this round made where DESIGN-holiday-tables.md left a detail open (entries R1-R7) | (see file) |

**Rows changed.** 54 rows added (the `THBP-B` lines for nine holidays, plus the two
Saturday 2025-11-29 rows), 8 rows changed (the two formerly `unknown` Cryptocurrency eve
rows, and the six Friday Cryptocurrency rows relabelled to `closed` [N19]). Two
`missing[]` entries deleted (Cryptocurrency 2026-06-17/2026-07-02; Saturday 2025-11-29),
two re-scoped to the eight remaining 2025 windows (Nikkei; ZS/ZW/HE/DC), one corrected in
its channel statement. Every (product, date) pair named by a new or changed row -- 158 of
them -- was re-parsed from the bytes in this directory and matches event for event,
including per-event trading dates.
