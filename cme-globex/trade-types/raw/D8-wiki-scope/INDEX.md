<!-- D-8 — wiki-page scope capture. Dates in this file are UTC (LAW-UTC-DATES). -->

# D-8 — Does the CME client-systems wiki migration page's effective-day statement scope the BTIC tables?

Target: CME Group Client Systems Wiki (Confluence, public, no authentication),
page id `1283194884`, title **"Cryptocurrency Futures and Options Migration to 24-7 Trading"**,
space `EPICSANDBOX`.

All retrievals on **2026-09-12**, between `01:32:41Z` (CAPTURE-START.txt) and `01:32:51Z`.
Every byte below came back over plain HTTPS with no credentials.

## What was retrieved and why

| Version | Created (UTC, from the version API) | Why this version |
|---|---|---|
| v39 | 2026-05-19T19:47:16.357Z | the version live for most of 2026-05-22 (until 18:58:57Z) |
| **v40** | **2026-05-22T18:58:57.710Z** | **the version created on 2026-05-22 — the one the ag/crypto gate saved** |
| **v41** | **2026-06-01T15:34:49.610Z** | **first version created after the 2026-05-29 migration** |
| v42 | 2026-06-01T16:05:58.830Z | same-day successor to v41, held as a check |
| **v46** | **2026-08-14T17:35:29.637Z** | **the CURRENT version** (`status: current`; `wiki-current-v1.json` is byte-identical to `wiki-v46.json`) |

There is no version between 2026-05-22T18:58Z and 2026-06-01T15:34Z: v40 was live across the
whole 2026-05-29 cutover.

## Files

| File | sha256 | URL |
|---|---|---|
| `versions-v2.json` | `1542ce7ebf62e689582bf61e21fd3bc4aa675d7ffe67f95a46ae1cc62e338b2c` | `https://cmegroupclientsite.atlassian.net/wiki/api/v2/pages/1283194884/versions?limit=100` |
| `wiki-current-v2.json` | `1e6f42d0c93648ebee969763cccb1f481d310ddd9885395cf9eb5224d2ea6c15` | `https://cmegroupclientsite.atlassian.net/wiki/api/v2/pages/1283194884?body-format=storage` |
| `wiki-current-v1.json` | `fd92e538a387a5c7d4378a3dcf57910e940b7eae69d8d3efccc4dc2d23208c47` | `https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/1283194884?expand=body.storage,version,history` |
| `wiki-v39.json` | `62ab41d8ada9a3c7c5c855b337a03eed951e3ca6c592435fe812c1004727d87e` | same v1 endpoint + `?status=historical&version=39&expand=body.storage,version,history` |
| `wiki-v40.json` | `8b229384404618672819d75768b4282e3ebb3cc18f2236a702a006678b47bbaa` | ditto, `version=40` |
| `wiki-v41.json` | `a320033cd9b9c86550f7a556e68f9847082d33e41633f314da5f70373fbb0503` | ditto, `version=41` |
| `wiki-v42.json` | `24e8eb693e0a834617e876377fb64c9d34e72ce38bb18c392da35d9a214efd4c` | ditto, `version=42` |
| `wiki-v46.json` | `fd92e538a387a5c7d4378a3dcf57910e940b7eae69d8d3efccc4dc2d23208c47` | ditto, `version=46` (== current) |

Derived, from those bytes only (no network):

| File | sha256 | What it is |
|---|---|---|
| `storage-v39.html` | `b19ae66148e905cec93e8d34bbcb27e00b04835595a2033fe70efe3c82983186` | `body.storage.value` extracted verbatim |
| `storage-v40.html` | `2d4f9b339e49e1de1ce86aedcb3696714fe0d0a8e32ebe40e2ab1b101a0e0599` | " |
| `storage-v41.html` | `8edcdcac30fef952cc1313dc434167d8b7a9c4d9a2f8c988611623557e55906e` | " |
| `storage-v42.html` | `04dd80e1bdd6b2416eca2354c0f82c978c26c3e8dc43d7615ec096b0c849e3b8` | " |
| `storage-v46.html` | `90bab57bf2c715c1e7f6fca3dc98c16acf2651dbdb1622118f92a04ff5578425` | " |
| `schedule-section-v{39,40,41,42,46}.txt` | all five identical, 6124 bytes | page intro + the whole `h1 24/7 Trading` / `h2 CME Globex Maintenance Windows and Market Hours` block containing all seven schedule tables |
| `body-v*.txt`, `body-current-v1.txt` | see `SHA256SUMS.txt` | whole-page text renders |
| `render.py`, `slice.py`, `sect.py` | see `SHA256SUMS.txt` | the render/slice helpers used |

`SHA256SUMS.txt` holds the full list.

## Heading structure (identical in v39, v40, v41, v42 and current v46)

```
h1  24/7 Trading
 h2  CME Globex Maintenance Windows and Market Hours
  h3  Current Cryptocurrency Futures and Options Schedule
  h3  Future Cryptocurrency Futures and Options Schedule
  h3  Day One Extended Maintenance
  h3  Future Cryptocurrency Futures and Options Schedule - 24/7 Crypto Trade at Settlement (TAS)
  h3  24/7 Basis Trade at Index Close (BTIC) Crypto Asia-Pacific (APAC)
  h3  24/7 BTIC Crypto London Session (LDN)
  h3  24/7 BTIC Crypto New York (NY)
  h3  Saturday Maintenance Window Processing Overview
 h2  24/7 Maintenance and Trading Schedule Examples
 h2  Products Not In Scope        (titled "Product Scope" in v39/v40, "Product Not In Scope" in v41)
```

The three BTIC tables are **h3 siblings of the TAS table and of the futures/options tables**,
inside one h2 section. No BTIC table is nested under any futures/options heading, and no
futures/options heading is a parent of any other schedule table.

## Where the day is stated

The string `effective` does not occur anywhere on the page, in any captured version.
`May 29` occurs exactly four times, in three places — **none of them inside any of the
seven schedule tables**:

1. the page's opening sentence, above every heading;
2. the `Key Events and Dates` table (h1-level, far above the schedule section): the
   `Friday, May 29, 2026, starting at 4:00 p.m. CT` / `Production Launch` row;
3. the `h3 Day One Extended Maintenance` paragraph and its own one-row table.

The `h3 Future Cryptocurrency Futures and Options Schedule` table itself carries **no date at all**.

## Byte-stability across the cutover

The four schedule sections (TAS, BTIC APAC, BTIC LDN, BTIC NY) are byte-identical in
v39, v40, v41, v42 and v46 — i.e. unchanged from ten days before the migration to the current
version eleven weeks after it. `schedule-section-v*.txt` are all 6124 bytes and share one digest.
The `Current …` / `Future …` labels were never swapped after the event; the page was not
re-labelled, so the label words carry no information about which state is now live.

## Scope-restricting statements on the page

Only two, and neither mentions BTIC:

- `h2 CME Globex Maintenance Windows and Market Hours` opens
  "This section outlines schedule impacts for all clients trading cryptocurrency futures and
  options." — this sentence sits above **all seven** h3 tables.
- The section's own contents panel ends "Cryptocurrency Spot Quoted Futures (SQF) will remain
  on a 5 day schedule.", and `h2 Products Not In Scope` enumerates exactly twelve spot-quoted
  futures (QBTC QEF QEM QETH QOF QOM QSOL QTF QTM QXF QXM QXRP). No BTIC product appears there.
