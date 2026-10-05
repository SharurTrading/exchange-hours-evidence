<!-- SPDX-License-Identifier: MIT-0 -->

# Gate U4-regular-vs-extended — retrieved artifacts

All captures made 2026-09-06 (UTC) from this machine.
`cmegroup.com` refuses this machine at IP level (403 with a full browser header set —
verified again this session), so live CME URLs were retrieved through the public text
reader `https://r.jina.ai/<url>`, which returns the same bytes as text. Archived PDFs
were retrieved as raw bytes via `id_` replay on web.archive.org and converted with
`pdftotext -layout` (both the `.pdf` and the `.txt` are kept).

**Capture date is not artifact date.** Each Daily Bulletin states its own trade date and
bulletin number in its page header; that is the artifact date recorded below.

| File | URL | Capture (UTC) | Artifact date | sha256 |
|---|---|---|---|---|
| `RA2302-5_wayback_20251020.pdf` | https://web.archive.org/web/20251020113006id_/https://www.cmegroup.com/rulebook/files/cme-group-Rule-524.pdf | 2026-09-06T05:15:01Z | Advisory Date July 13, 2023 / Effective Date July 31, 2023 | `d7032a32734db371b1558000fb00a0903a2ccd00e7527aaaef3f7c30da4d2ce1` |
| `RA2302-5.txt` | (pdftotext -layout of the above) | 2026-09-06T05:15:10Z | same | `fc4c00602f7a7eecffff666f89f37d4126e48e9f9faf9d6c392316124a3f6c20` |
| `db_landing.txt` | https://www.cmegroup.com/market-data/daily-bulletin.html | 2026-09-06T05:16:40Z | live page, section index | `7c0cc9cad62a543b3cf19a57ed225a0ad9ea84e39650d0091d667367ffe5318e` |
| `db_sec00_index.txt` | https://www.cmegroup.com/daily_bulletin/current/Section00_Daily_Bulletin_Product_Index_Futures_And_Options.pdf | 2026-09-06T05:17:58Z | Fri, Sep 04, 2026 — BULLETIN # 171@ PRELIMINARY | `9ec77dca593064279c5a8bfbb1f3caa3417e3c892f1c83a3d49cf36e5e32768e` |
| `db_sec11_equity.txt` | https://www.cmegroup.com/daily_bulletin/current/Section11_Equity_And_Index_Futures.pdf | 2026-09-06T05:17:43Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `30cb669f4fbbb9509d9833206da2ee0196967cfabe61ad18afaaad9fda424962` |
| `db_sec12_equity_cont.txt` | https://www.cmegroup.com/daily_bulletin/current/Section12_Equity_And_Index_Futures_Continued.pdf | 2026-09-06T05:20:11Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `8560e769de8323fb0c3a7366ddb8b0262677f3aebecc8982049954f58e41f88d` |
| `db_sec62_metals.txt` | https://www.cmegroup.com/daily_bulletin/current/Section62_Metals_Futures_Products.pdf | 2026-09-06T05:17:28Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `f26d7f4440415837996b9856f1c503b1b337825296f6222ceb5d47b511e1b9e7` |
| `db_Section61_Energy_Futures_Products.txt` | https://www.cmegroup.com/daily_bulletin/current/Section61_Energy_Futures_Products.pdf | 2026-09-06T05:18:19Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `db8ffe83591474b9d692eae5d01b41c04115c64f2359ff358a0cde4e6bb19806` |
| `db_Section03_Agricultural_Futures.txt` | https://www.cmegroup.com/daily_bulletin/current/Section03_Agricultural_Futures.pdf | 2026-09-06T05:18:19Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `2310c46d261f79055507b75d935fb699072ce39e59b63a035cf6d3a6c75ed94d` |
| `db_sec04_ag_soft.txt` | https://www.cmegroup.com/daily_bulletin/current/Section04_Agricultural_Soft_AltInvestment_Futures.pdf | 2026-09-06T05:20:11Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `ec875e7e7157f51b94162229a4ada60f228b0ad39b1877858dd89d6427855f7b` |
| `db_Section09_Interest_Rate_Futures.txt` | https://www.cmegroup.com/daily_bulletin/current/Section09_Interest_Rate_Futures.pdf | 2026-09-06T05:18:19Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `184d4a0f83425e75a3b24ae2e934671706d46957e6fec477218e67f2e847aaa6` |
| `db_Section10_Interest_Rate_Futures_Continued.txt` | https://www.cmegroup.com/daily_bulletin/current/Section10_Interest_Rate_Futures_Continued.pdf | 2026-09-06T05:27:24Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `78231525024129f839365cff6242610d2674da608382cfa409a3d2c0b75f6022` |
| `db_Section06_Currency_Futures.txt` | https://www.cmegroup.com/daily_bulletin/current/Section06_Currency_Futures.pdf | 2026-09-06T05:27:24Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `67c471d9353a2b0931e3c0373f09e3e6946fcb3285a7af3564fce4bea2201bde` |
| `db_Section08_Currency_Futures_Continued.txt` | https://www.cmegroup.com/daily_bulletin/current/Section08_Currency_Futures_Continued.pdf | 2026-09-06T05:27:24Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `e0802e69e963d29387f16d1ccfcbea390524b5e2e94c6f83e960bf1827253ef7` |
| `db_Section74_Cryptocurrency.txt` | https://www.cmegroup.com/daily_bulletin/current/Section74_Cryptocurrency.pdf | 2026-09-06T05:18:19Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `73b0586c804738271fac6938299a2f523cf3e93532bcda97665102b5abf0f972` |
| `db_sec24_weather.txt` | https://www.cmegroup.com/daily_bulletin/current/Section24_Weather_Futures_And_Options.pdf | 2026-09-06T05:16:56Z | Fri, Sep 04, 2026 — BULLETIN # 171@ | `fe7c7b5fd304478f665a8b8598f49433d354c8d895d7e84b399788bbf436f1c3` |
| `db_sec12_wb20260821.pdf` | https://web.archive.org/web/20260821212613id_/https://www.cmegroup.com/daily_bulletin/current/Section12_Equity_And_Index_Futures_Continued.pdf | 2026-09-06T05:20:44Z | Thu, Aug 20, 2026 — BULLETIN # 160@ FINAL | `27f29d2c00d2088ff13fdbf7c764ba2c494306f192c1ecca5541a57b21f9da20` |
| `db_sec12_wb20260821.txt` | (pdftotext -layout of the above) | 2026-09-06T05:20:50Z | same | `49d560c7d3f979cd50593acad595a45c8cd920d21b7ca8c0dd902ac3cc326506` |
| `db_sec61_wb20260324.pdf` | https://web.archive.org/web/20260324085750id_/https://www.cmegroup.com/daily_bulletin/current/Section61_Energy_Futures_Products.pdf | 2026-09-06T05:19:46Z | Mon, Mar 23, 2026 — BULLETIN # 55@ PRELIMINARY | `a43bf7ee5f9594a9775ff1a74df42a488f6445b48d93387ca2acac059e5279cd` |
| `db_sec61_wb20260324.txt` | (pdftotext -layout of the above) | 2026-09-06T05:19:52Z | same | `49313a1e15028157f2be3fc020621ed35192931f674a47b9fb99867f69dba007` |
| `db_sec03_wb20150322.pdf` | https://web.archive.org/web/20150322100952id_/http://www.cmegroup.com/daily_bulletin/current/Section03_Agricultural_Futures.pdf | 2026-09-06T05:25:51Z | Fri, Mar 20, 2015 — BULLETIN # 54@ (CBOT grain pit still open) | `f794fe41c1b9d6044f750e9e4ec3cd107c550a7ff2fb5f73c35447fe4bc61c53` |
| `db_sec03_wb20150322.txt` | (pdftotext -layout of the above) | 2026-09-06T05:25:57Z | same | `46bf98c1322d509db9bafbcfbc0e4ed2c0085996de1eba691aa7bf5b371cf752` |
| `db_sec12_wb20180121.pdf` | https://web.archive.org/web/20180121083353id_/https://www.cmegroup.com/daily_bulletin/current/Section12_Equity_And_Index_Futures_Continued.pdf | 2026-09-06T05:26:57Z | Fri, Jan 19, 2018 — BULLETIN # 13@ | `0408b3e300e633af4d4df623b499f91e0a77f4d3beb3fd37e8b0d109b0877e89` |
| `db_sec12_wb20180121.txt` | (pdftotext -layout of the above) | 2026-09-06T05:27:00Z | same | `ac422af4a581443dc041507a91829d62912748ed87b66fa2633cfc3158a3bcad` |
| `db_sec12_wb20200423060628.pdf` | https://web.archive.org/web/20200423060628id_/https://www.cmegroup.com/daily_bulletin/current/Section12_Equity_And_Index_Futures_Continued.pdf | 2026-09-06T05:27:10Z | Wed, Apr 22, 2020 — BULLETIN # 77@ | `a2277c43d856d77c7506bdf8b934278179f22751cfbbc7917132864a728f6454` |
| `db_sec12_wb20210309204159.pdf` | https://web.archive.org/web/20210309204159id_/https://www.cmegroup.com/daily_bulletin/current/Section12_Equity_And_Index_Futures_Continued.pdf | 2026-09-06T05:27:12Z | Mon, Mar 08, 2021 — BULLETIN # 44@ | `f67bebb9d68822e6f4f2896a2b44859bab77755d706d1f24eaa3f4437737625c` |
| `cs_133_es.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/133 | 2026-09-06T05:21:15Z | live (E-mini S&P 500; BTIC EST / TACO ESQ / TMAC ESX) | `556324d02d0087e6e1c8b9cbfe528deebb2164e67abb6e0a1858873c4708f252` |
| `cs_437.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/437 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Gold; TAS GCT / TAM GCD) | `2cd3f1e0368651438e66aa5b8e2ba2ba5cdcc1cf00cc299555d459610b6e4fc8` |
| `cs_438.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/438 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Copper; TAS HGT,HG0 / TAM HGF) | `289755c2a9fd36dadd04a8bd27bdf7d3e368aaa0503af7e696a4d4628d9f3ad9` |
| `cs_445.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/445 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Palladium; TAS PAT) | `24f2cb543c1d6231015bfa41ba4ccfe7c62b7e545ac4eb226a8601968df9ea4c` |
| `cs_446.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/446 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Platinum; TAS PLT) | `57f13e08ffcfdf91e048c5da2fd0fe91bcc9d4840cc328ca582701a8c10772eb` |
| `cs_458.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/458 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Silver; TAS SIT) | `c2fda2291d73ce502f1cb3f2b4e9be45f42422a60c52d9da84f1ac4a4e9743a3` |
| `cs_425.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/425 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Light Sweet Crude; TAS CLT / TAM CLS,CLC,CLL) | `8428766bbd463afc39776783ab115f5691f704108d3204f156758a2445330ed7` |
| `cs_300.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/300 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Corn; TAS ZCT) | `6d3f699113c90fbe2e2d769ede8351466dae40ffa0165a0a55c096bd4182723c` |
| `cs_22.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/22 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Live Cattle; TAS LET) | `e9e6fcd826fd3e2846e5fbf5b2048d95baeb3c78e6a41ed24dcd7d805551c2b1` |
| `cs_8478.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8478 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Bitcoin; TAS TBT / BTIC BNB,BTB,ABB) | `a170b561e5c4233e68f946ff71d642b18c26a688ad8c651142c383ee4f8c5508` |
| `cs_168.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/168 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (Nikkei USD; BTIC NKT) | `00134d159e495c3283997eb4458d489c73f04979ae758e75dd1210430dc2e330` |
| `cs_8491.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8491 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (TOPIX JPY; BTIC TPB) | `c816531d07dab497ae65047af6ad5be82c438b134ff5a4596d835c5ba3474040` |
| `cs_58.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/58 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (EUR/USD; BTIC 6EB) | `4fce3ee21f2bd30f8a60f07133818100d3c417b59b4fa69b86d10345d93f1bfb` |
| `cs_33.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/33 | 2026-09-06T05:21:22Z-05:23:59Z (batch window) | live (S&P GSCI; BTIC GDT) | `3881dce066c2d4363acdab31f6004bbe8a211eb724fceb21a207cc078806158d` |
| `wiki_tas_457223974.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/457223974?expand=body.storage,version | 2026-09-06T05:24:29Z | page v2, 2025-01-13T19:37:27Z | `7d4e17652f95497ececded635203d9e6480da170f11a334a8a26fdab2c5ed687` |
| `wiki_457224081.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/457224081?expand=body.storage,version | 2026-09-06T05:25:00Z-05:25:10Z (batch window) | page v1, 2024-12-21T17:06:00Z | `278fc94844b7b90a6431614148000316cce4ea7e874dc65b259a40257935e203` |
| `wiki_457092968.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/457092968?expand=body.storage,version | 2026-09-06T05:25:00Z-05:25:10Z (batch window) | page v2, 2025-01-13T19:46:14Z | `1715a5f1e97916fccaee44ba900736cb2bb5483655bf1bb0c85e8afdf1303ae0` |
| `wiki_457086960.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/457086960?expand=body.storage,version | 2026-09-06T05:25:00Z-05:25:10Z (batch window) | page v3, 2025-02-11T20:49:05Z | `8622f00d9b807cdf31aa0259d12ba59d1e056ab0002a8ac0f4c29615cd173b47` |
| `cdx61.json` | https://web.archive.org/cdx/search/cdx?url=...Section61...&output=json | 2026-09-06T05:19 (approx, same minute as the request logged in-session) | CDX listing | `18852dc7ef598f143763c7444f1d04af21738bfb831b3c5f6775fb1b32cca770` |
| `cdx12.json` | https://web.archive.org/cdx/search/cdx?url=...Section12...&limit=-8 | 2026-09-06T05:20 (approx, same minute as the request logged in-session) | CDX listing | `71f0ab3c3a490e1191f7fa0d5f9cbe8de57951aeb972f4173833e6c48766bb05` |
| `cdx12b.json` | https://web.archive.org/cdx/search/cdx?url=...Section12...&from=2014&to=2021 | 2026-09-06T05:26 (approx, same minute as the request logged in-session) | CDX listing | `724387d710c3474272ce464ee450f9eb2bca095e1d8763e504fc2137d877cefd` |
| `cdx03.json` | https://web.archive.org/cdx/search/cdx?url=...Section03...&from=2010&to=2015 | 2026-09-06T05:25 (approx, same minute as the request logged in-session) | CDX listing | `09c26c4bf73efe006a2be38ca8463283062e931349f887bb27f6692397693b8d` |
| `fetch.sh` | (local helper: retry wrapper around r.jina.ai) | 2026-09-06T05:16:30Z | n/a | `dd7467d4660040f3a755b33c69b2aad06e545406d96e68695e7f70dfd5e631c5` |

## What these artifacts establish (gate U-4)

1. **Rule 524 enumerates the execution routes and the pit is not one of them.** RA2302-5
   §6 reproduces CME/CBOT and NYMEX/COMEX Rule 524: each of 524.A (TAS), 524.B
   (BTIC / TAM), 524.C (TACO) and 524.D (TMAC) permits entry "on Globex", plus block
   trades under Rule 526 and EFP/EFR under Rule 538. There is no open-outcry route for
   any of the five shapes in the rule that creates them.
2. **RA2302-5 §3 makes each shape's own Pre-Open an order-entry window** — quoted in full
   in the result JSON.
3. **The Daily Bulletin never lists any of the five shapes on an RTH/ETH price page.**
   TAS is a volume column inside the EX-PIT breakdowns; BTIC has its own price-less
   "BTIC PRODUCTS VOLUME REPORT"; TAM has its own price-less "TRADE AT MARKER PRODUCTS"
   page; TACO and TMAC do not appear at all, and the Section 00 product index lists no
   page for any of them. This holds on the 2015-03-20 pit-era edition (CBOT grain pit
   open, CORN FUT carrying a live RTH VOLUME column) and on the 2018-01-19 edition
   (CME S&P 500 pit still open, RTH VOLUME column present, no BTIC row).
4. **CME's live ContractSpecs API prints exactly two venues** — "CME Globex:" and
   "CME ClearPort:" (or a single "Default:") — with every TAS/BTIC/TAM/TACO/TMAC hours
   line nested inside them. No product carries an Open Outcry / Trading Floor venue.
5. **The client-systems wiki** files TAS, TAM, BTIC and TACO as "Instrument Types
   Available on CME Globex", and its per-shape pages state the TAS and TMAC pre-open
   market-state sequence and the whole TACO grid including its three Pre-Opens.

## Pass 2 — 2026-09-06 (second, independent run of gate U4-regular-vs-extended)

All Pass-2 files are prefixed `p2_`. Captures made 2026-09-06 (UTC) from this machine.
`cmegroup.com` still refuses this machine at IP level, so live CME URLs went through the public
text reader `https://r.jina.ai/<url>`; archived rulebook PDFs came from `id_` replay on
web.archive.org and were converted with `pdftotext -layout` (both `.pdf` and `.txt` kept).
The reader returns HTTP 429 `RateLimitTriggeredError` under load; two files below are that error
body rather than an artifact and are labelled as such.

**Capture date is not artifact date.** The Daily Bulletin states its own trade date and bulletin
number in its page header; archived rulebook chapters are dated by their Wayback timestamp, which
dates the *observation of that edition*, not the day the rule changed.

| File | URL | Capture (UTC) | Artifact date / what it is | sha256 |
|---|---|---|---|---|
| `p2_cbot_ch5_20141116071003.pdf` | https://web.archive.org/web/20141116071003id_/http://www.cmegroup.com/rulebook/CBOT/I/5/5.pdf | 2026-09-06T06:20:18Z (batch) | CBOT Rulebook Chapter 5, capture 2014-11-16: "524.-525. [RESERVED]" | `05a0bd7cfd543eed517f4ace9d254cbfb600fadf80c8407e004dd1246cb2ad4a` |
| `p2_cbot_ch5_20141116071003.txt` | https://web.archive.org/web/20141116071003id_/http://www.cmegroup.com/rulebook/CBOT/I/5/5.pdf (pdftotext -layout) | 2026-09-06T06:20:18Z (batch) | CBOT Rulebook Chapter 5, capture 2014-11-16: "524.-525. [RESERVED]" | `038a569fef74ca1124080be98a59f671d0f140885c5d0c135decf06ebba0170b` |
| `p2_cbot_ch5_20150915054703.pdf` | https://web.archive.org/web/20150915054703id_/http://www.cmegroup.com/rulebook/CBOT/I/5/5.pdf | 2026-09-06T06:20:18Z (batch) | CBOT Rulebook Chapter 5, capture 2015-09-15: Rule 524 TAS, Globex-only | `f27d342eee6b80ad9e5572191af40ee7a3975b76367331559a6b3866406c53e3` |
| `p2_cbot_ch5_20150915054703.txt` | https://web.archive.org/web/20150915054703id_/http://www.cmegroup.com/rulebook/CBOT/I/5/5.pdf (pdftotext -layout) | 2026-09-06T06:20:18Z (batch) | CBOT Rulebook Chapter 5, capture 2015-09-15: Rule 524 TAS, Globex-only | `cb690e4618b5542443229ef6d6c79259623eefa986b7565ddf0613f9b1a1efaf` |
| `p2_cme_ch5_20120512.pdf` | https://web.archive.org/web/20120512064547id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2012-05-12: Rule 524 [RESERVED] | `91966b68db5d7d92cdc1b5ffc4f247b1efbd42ec726b4f30237216b7aa5c728b` |
| `p2_cme_ch5_20120512.txt` | https://web.archive.org/web/20120512064547id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf (pdftotext -layout) | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2012-05-12: Rule 524 [RESERVED] | `d0b820da222b0036fa3125a92f9e7d5278c48f78339993fb2f69712ccc377625` |
| `p2_cme_ch5_20150319015903.pdf` | https://web.archive.org/web/20150319015903id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2015-03-19: Rule 524 [RESERVED], no "Trading at Settlement" anywhere | `07a3ee1a548213661de2e6cbddff538f1ffaee55138cb75f27f065dacf0da516` |
| `p2_cme_ch5_20150319015903.txt` | https://web.archive.org/web/20150319015903id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf (pdftotext -layout) | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2015-03-19: Rule 524 [RESERVED], no "Trading at Settlement" anywhere | `49495175e1ca02c6583b0e62a965dadd6969efe2b3a6e9c04f5496ccac652a82` |
| `p2_cme_ch5_20150905223702.pdf` | https://web.archive.org/web/20150905223702id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2015-09-05: Rule 524 TAS, Globex-only | `cfb03f513b703cbf4c569c37cfd2e62af7560b3730daf19393c8fc153c4821e4` |
| `p2_cme_ch5_20150905223702.txt` | https://web.archive.org/web/20150905223702id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf (pdftotext -layout) | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2015-09-05: Rule 524 TAS, Globex-only | `4beda39f26d240e961bc58ca04ac39b50b376a69a7634ae186a70ef4b336d5fa` |
| `p2_cme_ch5_20151014210844.pdf` | https://web.archive.org/web/20151014210844id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2015-10-14 | `aa4e1c30d0d083e3fb67d15c77d17a62344a4e2c4f66447e3c2df1c6cd5cae99` |
| `p2_cme_ch5_20151014210844.txt` | https://web.archive.org/web/20151014210844id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf (pdftotext -layout) | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2015-10-14 | `e0b0fb98759e023f689141e46a8ec0d025ef8c536ea1d9b6f8dbc63054db534e` |
| `p2_cme_ch5_20161122210636.pdf` | https://web.archive.org/web/20161122210636id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2016-11-22: Rule 524 TAS + BTIC, Globex-only | `b3adebef1fff1eda026d28f580e0fbd23ca6adbb1120995cae0aebe25ee26a13` |
| `p2_cme_ch5_20161122210636.txt` | https://web.archive.org/web/20161122210636id_/http://www.cmegroup.com/rulebook/CME/I/5/5.pdf (pdftotext -layout) | 2026-09-06T06:18:27Z-06:19:13Z (batch) | CME Rulebook Chapter 5, capture 2016-11-22: Rule 524 TAS + BTIC, Globex-only | `4f7cd928595fb0154dac27df246f16519b416159afba9edbfdd8153925156e0a` |
| `p2_cs_10205.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/10205 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | Micro Crude Oil TAS (empty record) | `1da1242f6e81e4dfa56db23939ef2b4a92e5d86b037a0f7d2633fd27cc2f076a` |
| `p2_cs_10319.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/10319 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | TAS on Bitcoin Futures (empty record) | `de4ba6ffaf1d55187f8c5d22db8af4b9ad5edde4251f65b2662cdf55d9844274` |
| `p2_cs_10508.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/10508 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | TMAC on E-mini S&P 500 (record present, TradingHours "-") | `612ca589a2a0421d5ecda30742823af83272ce26a8c81854a6a4d0d2e81f06d0` |
| `p2_cs_431.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/431 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | HTTP 429 from the reader - not an artifact | `6765be4aa63862f1fbee5af698c15c7878632d0610be96be86b9791238dc6d78` |
| `p2_cs_4346.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/4346 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | Gold TAS (empty record) | `a7882eb72c1715d99bdb624bcce52c6abc887a549926aeca8df1b23a12d78ab0` |
| `p2_cs_6266.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/6266 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | WTI Crude Oil London TAM (empty record) | `72bb63234220ef4ac26bccbdf739fe21840467b62be29f92f9c32919bfab4ab7` |
| `p2_cs_7891.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/7891 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | Corn TAS (empty record) | `642053c12244bd85f185f536846015aff76244640d6490b6c291ad43c3adfe52` |
| `p2_cs_7968_est.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/7968 (via r.jina.ai) | 2026-09-06T06:14:16Z | live (BTIC E-mini S&P 500, EST) | `f4346fdbcd246ca748a17e2277277a628d12d58510777db4e2d7f0c0ef68da26` |
| `p2_cs_8407.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8407 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | Gold London TAM (empty record) | `49ef09a49342be58ae880011e4eebe18b00c439ce25078eebaa51042eb8e9ce7` |
| `p2_cs_8462.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8462 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | Three-Month SOFR Futures - Globex+ClearPort only | `f2a0f402874559508dd3a84fb60db9ee75024e726811a953b3cbb6158959d776` |
| `p2_cs_8528.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8528 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | TACO on E-mini S&P 500 (empty record) | `38f4136254005f95447df94f356f6c9c72154bae9eb9a8b4b0826ce2be91ef63` |
| `p2_cs_8633.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8633 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | BTIC on Nikkei (JPY) (record present, TradingHours "-") | `9394b954c1558223aa15c2e851ce003c12b02453731ca44390df9fe712004016` |
| `p2_cs_8849.txt` | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8849 (via r.jina.ai) | 2026-09-06T06:23:20Z-06:24:48Z (batch) | Options on Three-Month SOFR Futures - THE CONTRAST CASE: prints a third venue block "Open Outcry:" "MON - FRI: 7:20 a.m. - 2:00 p.m." | `c8b6a22ab54665fe2401586d1bba290e8a4d41427a240d2cfd246655ed534d6f` |
| `p2_db_Section00_Daily_Bulletin_Product_Index_Futures_And_Options.txt` | https://www.cmegroup.com/daily_bulletin/current/Section00_Daily_Bulletin_Product_Index_Futures_And_Options.pdf (via r.jina.ai) | 2026-09-06T06:21:38Z-06:21:43Z (batch) | CME Daily Information Bulletin, Fri, Sep 04, 2026 - BULLETIN # 171@ PRELIMINARY | `9ec77dca593064279c5a8bfbb1f3caa3417e3c892f1c83a3d49cf36e5e32768e` |
| `p2_db_Section03_Agricultural_Futures.txt` | https://www.cmegroup.com/daily_bulletin/current/Section03_Agricultural_Futures.pdf (via r.jina.ai) | 2026-09-06T06:21:54Z-06:22:07Z (batch, after 429 backoff) | CME Daily Information Bulletin, Fri, Sep 04, 2026 - BULLETIN # 171@ PRELIMINARY | `2310c46d261f79055507b75d935fb699072ce39e59b63a035cf6d3a6c75ed94d` |
| `p2_db_Section09_Interest_Rate_Futures.txt` | https://www.cmegroup.com/daily_bulletin/current/Section09_Interest_Rate_Futures.pdf (via r.jina.ai) | 2026-09-06T06:21:38Z-06:21:43Z (batch) | CME Daily Information Bulletin, Fri, Sep 04, 2026 - BULLETIN # 171@ PRELIMINARY | `184d4a0f83425e75a3b24ae2e934671706d46957e6fec477218e67f2e847aaa6` |
| `p2_db_Section10_Interest_Rate_Futures_Continued.txt` | https://www.cmegroup.com/daily_bulletin/current/Section10_Interest_Rate_Futures_Continued.pdf (via r.jina.ai) | 2026-09-06T06:21:54Z-06:22:07Z (batch, after 429 backoff) | CME Daily Information Bulletin, Fri, Sep 04, 2026 - BULLETIN # 171@ PRELIMINARY | `78231525024129f839365cff6242610d2674da608382cfa409a3d2c0b75f6022` |
| `p2_db_Section11_Equity_And_Index_Futures.txt` | https://www.cmegroup.com/daily_bulletin/current/Section11_Equity_And_Index_Futures.pdf (via r.jina.ai) | 2026-09-06T06:21:38Z-06:21:43Z (batch) | CME Daily Information Bulletin, Fri, Sep 04, 2026 - BULLETIN # 171@ PRELIMINARY | `30cb669f4fbbb9509d9833206da2ee0196967cfabe61ad18afaaad9fda424962` |
| `p2_db_Section12_Equity_And_Index_Futures_Continued.txt` | https://www.cmegroup.com/daily_bulletin/current/Section12_Equity_And_Index_Futures_Continued.pdf (via r.jina.ai) | 2026-09-06T06:21:54Z-06:22:07Z (batch, after 429 backoff) | CME Daily Information Bulletin, Fri, Sep 04, 2026 - BULLETIN # 171@ PRELIMINARY | `8560e769de8323fb0c3a7366ddb8b0262677f3aebecc8982049954f58e41f88d` |
| `p2_db_Section61_Energy_Futures_Products.txt` | https://www.cmegroup.com/daily_bulletin/current/Section61_Energy_Futures_Products.pdf (via r.jina.ai) | 2026-09-06T06:21:54Z-06:22:07Z (batch, after 429 backoff) | CME Daily Information Bulletin, Fri, Sep 04, 2026 - BULLETIN # 171@ PRELIMINARY | `db8ffe83591474b9d692eae5d01b41c04115c64f2359ff358a0cde4e6bb19806` |
| `p2_db_Section62_Metals_Futures_Products.txt` | https://www.cmegroup.com/daily_bulletin/current/Section62_Metals_Futures_Products.pdf (via r.jina.ai) | 2026-09-06T06:21:54Z-06:22:07Z (batch, after 429 backoff) | CME Daily Information Bulletin, Fri, Sep 04, 2026 - BULLETIN # 171@ PRELIMINARY | `f26d7f4440415837996b9856f1c503b1b337825296f6222ceb5d47b511e1b9e7` |
| `p2_nymex_ch5_20150306113807.pdf` | https://web.archive.org/web/20150306113807id_/http://www.cmegroup.com/rulebook/NYMEX/1/5.pdf | 2026-09-06T06:20:54Z (batch) | NYMEX Rulebook Chapter 5, capture 2015-03-06: Rule 524.A.1 STILL carries the pit clause; 524.B (TAM) does not; 524.C is MO ("open outcry trades") | `426b1b4378ba32adc6ec5f6ddf74c4c0bb38cd264e721de8f1a080468b906149` |
| `p2_nymex_ch5_20150306113807.txt` | https://web.archive.org/web/20150306113807id_/http://www.cmegroup.com/rulebook/NYMEX/1/5.pdf (pdftotext -layout) | 2026-09-06T06:20:54Z (batch) | NYMEX Rulebook Chapter 5, capture 2015-03-06: Rule 524.A.1 STILL carries the pit clause; 524.B (TAM) does not; 524.C is MO ("open outcry trades") | `7742d2c991c594b3a71b5f3930749ee3f61f8ad89ca3f2a827f95a85ab6a9f49` |
| `p2_nymex_ch5_20160809000829.pdf` | https://web.archive.org/web/20160809000829id_/http://www.cmegroup.com/rulebook/NYMEX/1/5.pdf | 2026-09-06T06:20:54Z (batch) | NYMEX Rulebook Chapter 5, capture 2016-08-09: pit clause GONE, MO gone, title now "TAS AND TAM" | `8f2fbec14facc51323aafcc12b569076a7053bd871bec43b6d588d2783a38281` |
| `p2_nymex_ch5_20160809000829.txt` | https://web.archive.org/web/20160809000829id_/http://www.cmegroup.com/rulebook/NYMEX/1/5.pdf (pdftotext -layout) | 2026-09-06T06:20:54Z (batch) | NYMEX Rulebook Chapter 5, capture 2016-08-09: pit clause GONE, MO gone, title now "TAS AND TAM" | `f620104c69ed7552fc34da397e3b88d2710e01ba513a91d8ae77be8c1e3d16ab` |
| `p2_nymex_ch5_20180205015718.pdf` | https://web.archive.org/web/20180205015718id_/http://www.cmegroup.com/rulebook/NYMEX/1/5.pdf | 2026-09-06T06:20:54Z (batch) | NYMEX Rulebook Chapter 5, capture 2018-02-05: same as 2016 | `f3feb375e5041463bdc41d0bcafb3c6503b3690d5f8443992cc63a30e4f82c02` |
| `p2_nymex_ch5_20180205015718.txt` | https://web.archive.org/web/20180205015718id_/http://www.cmegroup.com/rulebook/NYMEX/1/5.pdf (pdftotext -layout) | 2026-09-06T06:20:54Z (batch) | NYMEX Rulebook Chapter 5, capture 2018-02-05: same as 2016 | `1fce5cccf64a786ea565789bfb40ba1b8ec6dbeae151a6c6cd736e4a02680af3` |
| `p2_slate_p1.txt` | https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=1&sortAsc=true&sortField=id&pageSize=2000 (via r.jina.ai) | 2026-09-06T06:15:01Z-06:15:28Z (batch) | live; props.voi.tradeDate = 04 Sep 2026 | `c443e2e0d19e07511c7dfae02a2e437a21607efa884ccf68aa645fcd1631d49f` |
| `p2_slate_p2.txt` | https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=2&sortAsc=true&sortField=id&pageSize=2000 (via r.jina.ai) | 2026-09-06T06:15:01Z-06:15:28Z (batch) | live; props.voi.tradeDate = 04 Sep 2026 | `76a824a77b66cc2cef09648698f3e4c9118566247c71ba1161fd4f28ce9d1be6` |
| `p2_slate_p3.txt` | https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=3&sortAsc=true&sortField=id&pageSize=2000 (via r.jina.ai) | 2026-09-06T06:15:01Z-06:15:28Z (batch) | live; props.voi.tradeDate = 04 Sep 2026 | `76b5d33e07fd1242bf2802d33de49c1bfa9cb8e44d76138ae73417d976ccd7d1` |
| `p2_slate_p4.txt` | https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=4&sortAsc=true&sortField=id&pageSize=500 (via r.jina.ai) | 2026-09-06T06:15:01Z-06:15:28Z (batch) | live; props.voi.tradeDate = 04 Sep 2026 | `91cb756b86d77330ee0f57b7967461a06ce825c1e28375b0881b8f23b5cd1b1d` |
| `p2_slate_p5.txt` | https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=5&sortAsc=true&sortField=id&pageSize=500 (via r.jina.ai) | 2026-09-06T06:15:01Z-06:15:28Z (batch) | live; props.voi.tradeDate = 04 Sep 2026 | `93031581631fa0e4cd264b6d36d5525ccb0dbd5d815a5b69ce580f79ad66cfc7` |
| `p2_slate_p6.txt` | https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=6&sortAsc=true&sortField=id&pageSize=500 (via r.jina.ai) | 2026-09-06T06:15:01Z-06:15:28Z (batch) | live; props.voi.tradeDate = 04 Sep 2026 | `7a4592505845e67dfe47f2ec1df168c08864ec3d062a57cfbde756e5c751a9f9` |
| `p2_slate_p7.txt` | https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=7&sortAsc=true&sortField=id&pageSize=500 (via r.jina.ai) | 2026-09-06T06:15:01Z-06:15:28Z (batch) | live; props.voi.tradeDate = 04 Sep 2026 | `23b1edc4f862643bb53d7838605f76ceb7808cb24814c11daa6fea5184bb9e07` |
| `p2_slate_probe.txt` | https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=1&sortAsc=false&sortField=oi&pageSize=5 (via https://r.jina.ai/) | 2026-09-06T06:14:50Z | live; props.voi.tradeDate = 04 Sep 2026, PRELIMINARY | `1089cd7dd23c9aaf61d823bbf9847fe335ff199348d8296bc097592b2fdb2b41` |
| `p2_th_10251.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=10251&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | HTTP 400 - missing pageSize; not an artifact | `a3c9806d2a937ee677f64b8a8e184126fbae4afdfdd18fcf5db46881cbc976de` |
| `p2_th_10319.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=10319&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | TBT/group CI: hasEvents false, zero events | `f3283346153032ba357307bd238516263595a2054577372339109b4ba0591029` |
| `p2_th_10508.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=10508&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | ESX/group E2: closed@15:00, paused@16:45, preopen@16:45, open@17:00 | `8d74f277cd31908075d0c25db743dedda4c51fdf774a4ab7a7cc5c273d077b84` |
| `p2_th_431.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=431&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | CLT/group CT: hasEvents false, zero events | `c0973595491852cc0e789599691e91a0a26dd55fc59565b75f34b95e8ead5602` |
| `p2_th_4346.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=4346&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | GCT/group TG: hasEvents false, zero events | `9e48233750d9d18b83f9eeba358d8b1fc1f9bb7b99144023a89a34ac17896e2a` |
| `p2_th_7968.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=7968&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | EST/group SB: preopen@16:45, open@17:00, closed@15:00 | `d29d523a572577282d94c93069c4eaab5fb3c8a849549537b6374eb178169a7c` |
| `p2_th_8407.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=8407&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | GCD/group GM: closed@09:02 daily, preopen@16:50, open@17:00 | `21c94cdf71c38acce3e9d65f736057060d56faa0f0fdeeafcccc51426051a0a6` |
| `p2_th_8528.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=8528&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | ESQ/group 3T: preopen@09:30, open@10:00, paused@16:00, preopen@16:45, open@17:00, closed@08:30 | `1e94a3cf154cab24d44c19ed475d50c9d4a21259ceb3b6a3c814c245fe186f67` |
| `p2_th_8610.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=8610&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | HTTP 400 - missing pageSize; not an artifact | `db68f07006bd54cfffef6b29634e1042227d086c485c5aca32a6faaba9551972` |
| `p2_th_8652.txt` | https://www.cmegroup.com/services/trading-hours-by-product?id=8652&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 (via r.jina.ai) | 2026-09-06T06:28:00Z-06:32:30Z (batch) | HTTP 400 - missing pageSize; not an artifact | `bace8d659d9d0ae45b92ca29e4fcf4b709b45811b9759e41d51e104803d54524` |
| `p2_wiki_children_457086960.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/457086960/child/page?limit=50 | 2026-09-06T06:26:20Z | children of 'Instrument Types Available on CME Globex' | `6d7a4b6e5bf59f2c80b048464e40494bd8d68d4cda42ebd041ea840b19e7e94f` |
| `p2_wiki_q_73c45051ec5d242125206ef375d8e84b.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/search?cql=... (title~BTIC / text~'BTIC groups' / text~'pre-open state is randomized') | 2026-09-06T06:26:00Z-06:26:40Z | Confluence CQL search results | `e6d0ffcbef559c4b01ee47dbc475b104e6416401ce62deecb7b9ffe310e12f06` |
| `p2_wiki_q_769977d83b028c2abc32c47b00e51f27.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/search?cql=... (title~BTIC / text~'BTIC groups' / text~'pre-open state is randomized') | 2026-09-06T06:26:00Z-06:26:40Z | Confluence CQL search results | `598d467a370c7ba0776b570701b6faf04b24d88ce1283685d5b00e3d80cad464` |
| `p2_wiki_q_c6d15a64c92e0c573fbdab3758f5dc1a.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/search?cql=... (title~BTIC / text~'BTIC groups' / text~'pre-open state is randomized') | 2026-09-06T06:26:00Z-06:26:40Z | Confluence CQL search results | `efb21f0b5cdf3bd25d4493021aa11b7f36157c485e5bc5732d940d0861667ace` |
| `p2_wiki_search_btic_title.json` | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/search?cql=title~%22Basis%20Trade%20at%20Index%20Close%22&limit=20 | 2026-09-06T06:25:49Z | Confluence search: size 0 - no such page | `67dc413582ecbd74485b34f5627de035acdc6d15e1f129186eaf93f580289eef` |

### What Pass 2 adds, and where it corrects Pass 1

1. **A structured, per-root, affirmative channel Pass 1 did not use: CME's own ProductSlate.**
   `/CmeWS/mvc/ProductSlate/V2/List` returns, for every listed product, a `floor` code, a
   `floorTraded` flag, a `floorVol` and a `venues` string. Merging all 7 pages gives 3,248 unique
   products, of which **234 are trade-type products** (name matches BTIC / TAS / Trade at
   Settlement / TAM / Trade at Marker / TACO / TMAC). **All 234 carry `floor: "-"` and
   `floorVol: "0"`; 231 carry `venues: "Globex ClearPort "` and 3 carry `venues: "ClearPort "`.**
   None carries a "Floor" component. The three ClearPort-only records are `IBB`, `DGT` and `SET`
   (globex code `-`, `globexTraded: false`) - a non-Globex BTIC and two BTIC-on-swaps, i.e. not
   order books at all and out of this crate's scope.
   **Data-quality caveat that must travel with this channel:** `floorTraded` is unreliable. It
   reads `true` on `NQQ` (8914) and `RTQ` (8915) while the same records read `floor: "-"`,
   `floorVol: "0"` and `venues: "Globex ClearPort "`. The flag reads `true` across a contiguous id
   band (8914-8927) that also contains `HDG`, `BEF`, `BEB`, `TEF` and `T7C` - products with no
   floor either. The substantive fields are `venues`, `floor` and `floorVol`; do not cite
   `floorTraded`.

2. **A contrast test that converts silence into an affirmative.** CME's ContractSpecs API prints
   one `venue`-labelled hours block per market. For **Options on Three-Month SOFR Futures**
   (productId 8849 - the one CME family that still has a pit) it prints a third block:
   `"venue": "Open Outcry:"`, `"hours": "MON - FRI: 7:20 a.m. - 2:00 p.m."`. Across 27 captured
   contract-specification records, 16 hours blocks carry a `TAS:` / `BTIC:` / `TACO:` / `TMAC:`
   line and **every one of them sits inside `CME Globex:`** (or its `CME ClearPort:` duplicate, or
   a single-venue `Default:` page). Not one appears under `Open Outcry:`. The label exists in the
   same API and is never used for these shapes - which is stronger than the four *silent* channels
   `globex_spot_quoted` rests on.

3. **A correction to Pass 1's central claim.** Pass 1's INDEX said "There is no open-outcry route
   for any of the five shapes in the rule that creates them." That is **false for NYMEX/COMEX TAS
   in the pit era**. NYMEX & COMEX Rule 524.A.1, as issued with MRAN RA0907-4 (2009-09-01,
   effective 2009-09-14) and still present in the NYMEX rulebook captured 2015-03-06, reads:
   *"TAS transactions executed in the pit must be made open and competitively pursuant to the
   requirements of Rule 521 during the hours designated for pit trading in the particular contract
   and must be identified as such on the member's trading records."* The clause is gone by the
   2016-08-09 capture. It never applied to TAM (NYMEX 524.B was Globex-only from the start), and
   it never applied on the CME/CBOT side at all, because CME and CBOT Rule 524 was `[RESERVED]`
   until after the 2015-07-02 futures-floor closure.
   Why the conclusion nevertheless stands: the advisory's own eligibility tables separate
   **"Pit-Traded Contracts"** - listed by the *underlying's* code (`CL`, `HO`, `NG`, `RB`, `BZ`,
   `7F`, `GC`, `SI`) with no TAS code - from **"CME Globex Contracts"**, listed by the TAS root's
   own Globex commodity code (`CLT`, `BZT`, `BBT`, `HOT`, `RBT`, `NGT`, ...). The pit route was a
   pricing convention available in the *underlying's* pit, not a session of the Globex TAS
   instrument this crate keys.

4. **Two more recent Daily Bulletin editions read from the bytes**, plus the pit-era contrast:
   Fri Sep 04 2026 (BULLETIN # 171@, seven sections, captured independently this pass and
   byte-identical to Pass 1's capture of the same edition), Mon Mar 08 2021 (BULLETIN # 44@,
   Section 12 - carries the `Open Outcry(RTH)` legend *and* a separate BTIC report page in the same
   edition), and Fri Mar 20 2015 (BULLETIN # 54@, Section 03 - live `RTH VOLUME` figures against
   CBOT grain rows while TAS appears only as a `TAS DAILY TOTALS` column under
   `EX-PIT & OTHER BREAKDOWN`).
