# U16-U17-taco — evidence index

Gate: **U-16 (TACO Saturday events) / U-17 (TACO Monday–Friday day leg)**.
Capture session: 2026-09-06 (UTC). Two capture runs live in this directory:

* files at the top level and in `notices/ sers/ wiki/ tacopage/ cftc/` — captured
  2026-09-06 **05:16Z–06:47Z** (the run that produced `CAPTURES.log`; that log
  stops at 05:42Z and does not cover the later files in that run).
* files under `u16u17/` — captured 2026-09-06 **07:00Z–07:10Z**, fully logged with
  URL, UTC capture timestamp, sha256 and byte count in `u16u17/INDEX.tsv`.

Capture timestamp dates the observation only. Artifact dates are given separately below.

## Load-bearing artifacts (the ones quoted in the result)

| File | URL | Artifact date (stated in the document) | sha256 | bytes |
|---|---|---|---|---|
| `u16u17/notice-2018_05_20180507.txt` | https://www.cmegroup.com/notices/electronic-trading/2018/05/20180507.html | Weekly CME Globex Notice **2018-05-07** | 589d0b260d7140a7c92d7aec2aa932678386f825d3326a8da7759bf74e34907a | 17430 |
| `SER-8124R-pdf.txt` | https://www.cmegroup.com/notices/ser/2018/04/SER-8124R.pdf | SER date **2018-04-26**; header Effective Date 13 May 2018 | e04bfc5b58cf7c7c8321331eaf516236de326c92d21d077d6676d30d61b0771a | 7464 |
| `SER-8124R.txt` | https://www.cmegroup.com/notices/ser/2018/04/SER-8124R.html | Notice Date 26 April 2018 / Effective Date 13 May 2018 | 109dff0ea43d28931dc4fd68bf5adae97bd292a08f75da98c0d58c85a2e16a4b | 9888 |
| `Chadv20-061-pdf.txt` | https://www.cmegroup.com/notices/clearing/2020/02/Chadv20-061.pdf | Clearing advisory 20-061, notice date **2020-02-26**, listing/trade date Mon 2020-03-23 | a791f4718f60ada0fb10c91d45a0e0c64113c56f54f094d3d00709f2357cab79 | 2544 |
| `Chadv20-061.txt` | https://www.cmegroup.com/notices/clearing/2020/02/Chadv20-061.html | same | 142b8594c9aa1efd35ce19dcb809d74e6a67c29d76988192fcd14582f81552a2 | 10236 |
| `notices/bodies/notices_electronic-trading_2020_03_20200316.html` | https://www.cmegroup.com/notices/electronic-trading/2020/03/20200316.html | Weekly CME Globex Notice **2020-03-16** | b788461bf90ac5a28263b806e4837a1d9f7cd5c5babc2086cb89dcee3ca001b0 | 41611 |
| `u16u17/notice-2021_09_20210906.txt` | https://www.cmegroup.com/notices/electronic-trading/2021/09/20210906.html | Weekly CME Globex Notice **2021-09-06** | 010d3816a0ae2ce6f4a1b87ac010af54b499e0000e797b0b1da1e8136b825366 | 35362 |
| `u16u17/notice-2021_09_20210913.txt` | https://www.cmegroup.com/notices/electronic-trading/2021/09/20210913.html | Weekly CME Globex Notice **2021-09-13** | a4e7b28be0a21d8f42bb9d0895f27cbb0df5f72384e3f72fd2605e178b7834cf | 36073 |
| `notices/bodies/notices_electronic-trading_2021_09_20210920.html` | https://www.cmegroup.com/notices/electronic-trading/2021/09/20210920.html | Weekly CME Globex Notice **2021-09-20** | 3bb171e22765f1be4503f876d5899cd4dc00de922b6b126a4eb45c1ccf1b7184 | 32804 |
| `u16u17/notice-2021_09_20210927.txt` | .../2021/09/20210927.html | Weekly notice 2021-09-27 — **no TACO item** (no postponement) | 9f19020ad64ef86519ff054b27988b74513df52c6b08c8fb7d501607eb296c7d | 28574 |
| `u16u17/notice-2021_10_20211004.txt` | .../2021/10/20211004.html | 2021-10-04 — no TACO item | 8c0a53edf569991a3370c6046d80c1293462a53cf3d270d8d3cc3bcb5b7f4d9c | 16473 |
| `u16u17/notice-2021_10_20211011.txt` | .../2021/10/20211011.html | 2021-10-11 — no TACO item | ba4bc9fdb932fff18a528f8f2a43ca042f4eabdd24c08a74b8221889fff12b26 | 21870 |
| `notices/bodies/notices_electronic-trading_2021_06_20210621.html` | .../2021/06/20210621.html | 2021-06-21 — "all BTIC and TACO products will not be impacted" | f299aa894083a41cc4af59084ba990a466f7a1456ed20d59992b20ac0304837b | 23688 |
| `u16u17/notice-2019_08_20190826.txt` | .../2019/08/20190826.html | 2019-08-26 BTIC+/TACO+ listing — **states no hours** | a65726fcf6c29dc3456501f50481c42f8a22f8084671168aadd06c90e08c153a | 32624 |
| `wiki/confluence-taco-20200701111011.html` | https://www.cmegroup.com/confluence/display/EPICSANDBOX/Basis+Trade+at+Cash+Open | wayback ts 20200701111011; page last-modified stamp **Feb 26, 2020** (v12→13) | b90ad0af2e6a9806fd7a929de7bb19030dda5db31e8c2d7e4b274154141f87dc | 48938 |
| `wiki/confluence-taco-20210611132316.html` | same | wayback ts 20210611132316; last-modified **Feb 26, 2020** | 7daf4cbf5610dd25ad0100ac01a5c3db2ea994121b07872d3aae5353c3ead0d9 | 47663 |
| `wiki/confluence-taco-20210621203030.html` | same | wayback ts 20210621203030; last-modified **Feb 26, 2020** | 3614fd253490c45a6833510b759d15a15b6011e0e0f3f70a67eb6175c6ae0ad6 | 47662 |
| `wiki/confluence-taco-20211026124959.html` | same | wayback ts 20211026124959; last-modified **Oct 11, 2021** (v13→14) | bae3fe0172489bdb1a988db7d861bad9252c460e12093a34f76317212c8e8cdb | 48381 |
| `wiki/confluence-taco-20220528113732.html` | same | wayback ts 20220528113732; last-modified **Oct 11, 2021** | f522864f229e3a8df2789f12888f4b44cc7587c326990b22e3e898e110f85a35 | 48373 |
| `u16u17/conf-457092968-body.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/457092968?expand=body.view,version | migrated page, version 2 of 2, **2025-01-13T19:46:14.571Z** (v1 2024-12-21, "Space Sync for Confluence") | b690cd5cf7ce4c76422374cbdf74ae170c74ea38b575cf07cc317b9c8149f2fd | 8685 |
| `taco_friday_scenario.png` | Confluence attachment `Taco-Friday-Scenario.png` on page 457092968 | attachment version date 2024-12-21 (migration) | 1270ed97ee5042051d67697b2863ef2d5692df2b2d1eef20b6524c713bbc5b22 | 66952 |
| `u16u17/cs-133-live.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/133 | live, undated by CME | 556324d02d0087e6e1c8b9cbfe528deebb2164e67abb6e0a1858873c4708f252 | 4504 |
| `u16u17/cs-146-live.txt` | .../productId/146 (E-mini Nasdaq-100) | live, undated | 10c5a7ae591bcb20c701fbcf0d3a0bfe63ffde2eacff37173e0d236dba9943dc | 4203 |
| `u16u17/cs-8314-live.txt` | .../productId/8314 (E-mini Russell 2000) | live, undated | 90b2b39b749ba6069d3aaa46a7b9526bfed1ff6d0a5cc66f8affd2f613b1b754 | 4281 |
| `specs133-20210703123524.decoded.json` | wayback id_ replay of ContractSpecs 133 | wayback ts **2021-07-03** | ff1ac332c4b78d66320ca43b799ef0c06d06c2c62da30bed1b86548183f9f984 | 3206 |
| `specs133-20220908122619.decoded.json` | same | wayback ts **2022-09-08** | 4fa6538b307b89bf04b5fd9c958556bf53d8c0110c9bea3bbf0315a7b314abbc | 3211 |
| `specs133-20260405234659.decoded.json` | same | wayback ts **2026-04-05** | 511fb8fa542f2bdd11897f111731a391f5facc03c79c8de77ab288b97948678c | 4395 |
| `cdx-133-full.json` | web.archive.org CDX for `.../ContractSpecs/List/productId/133*` | 23 captures, 2021-07-03 → 2026-04-05 | 0c09177137a103b4af5057cc575116605c5a83d955c2113016ec47aeef0ca4d4 | 3899 |
| `th_8528_aug29.txt` | `/services/trading-hours-by-product?id=8528&…fromEventDate=2026-08-24&toEventDate=2026-09-13` | live feed | e35069803ecdc0005d67d5d2b664c51d4c4acd7e0a177829d1ee7d2e012226d7 | 8640 |
| `u16u17/svc8528-2026-10-19_2026-11-16.txt` | same, 2026-10-19→2026-11-16 (spans US DST end 2026-11-01) | live feed | 79fdfa4f098194a0c545d931bf8d8b2d8515cb005cf2d97f69b5cb1b4ec20259 | 12257 |
| `u16u17/svc8528-2026-11-20_2026-12-07.txt` | same, Thanksgiving week | live feed | fd2b84fbf90c3cdc7da15e42b00413c6da586014c8e5799195b9ea50d72d572a | 7113 |
| `u16u17/svc8528-2026-12-20_2027-01-10.txt` | same, Christmas / New Year | live feed | 1a3c83e9ab152def7f4a4d9fdbc84d9c08c0a2a6c49ba15ebe720deff23613ee | 8243 |
| `thallB_p1.txt` … `thallB_p17.txt` | `/services/trading-hours-by-product?pageNumber=N&pageSize=200&fromEventDate=2026-09-04&toEventDate=2026-09-07` | live feed; **3,243 products** — the Saturday census | see `CAPTURES.log` lines 27-43 | ~175 KB each |
| `th_8914.txt` / `th_8915.txt` | service id=8914 (NQQ) / id=8915 (RTQ) | live feed | 595040733d8bc24519cc41e61dd058cccb2377a73ad34c96fc60df2ee0d643a1 / e3148744f7b96635538745e7817f51f37d1b728f82de5203083d3c74b457263d | 8649 / 8653 |
| `th_8633.txt` / `th_8634.txt` | service id=8633 (NIT) / id=8634 (NKT) | live feed — same Saturday block | a2d6c40cc02c2bc34febb0d13e2507505f05e1f2d035fd8aa00202699ba57e4e / 04ef776f47752c1c5abc4361b5db757c6eea8990c6df9fee9de7b84e378e12dc | 8732 / 8735 |
| `th_7968.txt` / `th_8689.txt` / `th_133_w1.txt` / `th_10508.txt` / `th_8407.txt` | service EST / ES1 / ES / ESX / GCD | live feed — **empty** Saturday blocks | 430468fd… / 3cbc2acd… / 0621ac4e… / 75ab37e5… / 2811db6e… | 4862 / 5091 / 2919 / 5931 / 4863 |
| `u16u17/conf-search-taco.json` | Confluence CQL `text~"TACO"` | live | 1ea7988c40809997e4fc946bf02997b2c5ed3dd297dcf91dde5f0e66e6149eeb | 23610 |
| `u16u17/conf-search-sat.json` | Confluence CQL `text~"TACO" and text~"Saturday"` | live — 1 hit, an RDW API doc, no hours | 82bd46272e1281a8d3efcbde824d600d043d6747e0830a30b9049f63c2b9d0c7 | 833 |
| `u16u17/wiki-friday-live.txt` | .../confluence/display/EPICSANDBOX/TACO+and+BTIC+Friday+Trading+Schedule | **404** — the Client Impact Assessment the 2021 notice links to is gone | 0af36cf9e2177be9dfa221d4510082f88bcaf163fc2aa66c98347ab93f1286b0 | 624 |
| `u16u17/cdx-wiki-friday.json` | CDX for that URL | **empty** — never archived | 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 | 3 |
| `u16u17/nidx-2021sep-p0…p12.json` | CME notices index, 2021-09-01→2021-10-31, 163 notices | no SER or clearing advisory for the TACO/BTIC Friday schedule | see `u16u17/INDEX.tsv` | — |
| `u16u17/SER-8853.txt` `SER-8854R.txt` `SER-8856.txt` `SER-8859.txt` `SER-8869.txt` | the five Sep/Oct-2021 Equity-Index SERs | none concerns TACO hours | see `u16u17/INDEX.tsv` | — |
| `u16u17/Chadv21-305-pdf.txt` | https://www.cmegroup.com/notices/clearing/2021/09/Chadv21-305.pdf | crypto BTIC launch, trade date **2021-09-27** (same day) — no TACO grid | ebf4d0800e654a0891ef69289e1beab8e8d40557115ce62378d70b8c39741c50 | 2961 |
| `cme21-236.pdf` → `u16u17/cme21-236.txt` | URL not recorded by the earlier run (file present) | CME Submission 21-236, cover sheet Filing Date **07/19/21** — Rule 524 BTIC price-assignment amendments effective 2021-08-08/09; **states no trading hours** | 288554-byte PDF, text extracted with pdftotext -layout | — |

Full per-file log of the 07:00Z–07:10Z run: `u16u17/INDEX.tsv`.
