# INDEX - metals-tas-history

Gate `metals-tas-history` (CME metals TAS: GCT/MGT/QOT/1OT, SIT/MST, HGT/MHT/HG0, PLT, PAT).

Two runs wrote into this directory. Rows below are the artifacts the gate's conclusions rest on.
Capture timestamps date the **observation only**; `artifact date` is the document's own date.
Run A = 2026-09-06T05:14Z-05:45Z (interrupted). Run B = 2026-09-06T06:13Z-06:45Z (this run).
Every Run-A CFTC PDF the conclusions rely on was **re-fetched in Run B and its sha256 matched**.
`.txt` siblings of PDFs are local `pdftotext -layout` renders with no independent URL.

## A. Live CME channels (Run B, 2026-09-06)

CME 403s a bare curl and 403s this host on `/CmeWS/*` even with a full browser header set
(verified again this run: `/CmeWS/mvc/ContractSpecs/List/productId/437` -> HTTP 403).
The public text reader in front of the same CME URL returns the JSON. The **citation is the CME
URL**; `r.jina.ai` is transport, not the source.

| file | sha256 | artifact date | capture (UTC) | CME URL | what it is |
|---|---|---|---|---|---|
| `underlying-437-contractspecs.json` | `2cd3f1e0368651438e66aa5b8e2ba2ba5cdcc1cf00cc299555d459610b6e4fc8` | undated (live) | 2026-09-06T06:13:18Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/437 | Gold Futures. Globex cell: `TAS: Sun-Fri 6:00 p.m. - 1:30 p.m. ET (5:00 - 12:30 CT)`. ProductCode.TAS=GCT, .TAM=GCD |
| `underlying-458-contractspecs.json` | `c2fda2291d73ce502f1cb3f2b4e9be45f42422a60c52d9da84f1ac4a4e9743a3` | undated (live) | 2026-09-06T06:13:21Z | .../productId/458 | Silver. `TAS: Sunday - Friday 6:00 p.m. - 1:25 p.m. (5:00 p.m - 12:25 p.m. CT)` |
| `underlying-438-contractspecs.json` | `289755c2a9fd36dadd04a8bd27bdf7d3e368aaa0503af7e696a4d4628d9f3ad9` | undated (live) | 2026-09-06T06:13:23Z | .../productId/438 | Copper. `TAS: Sunday - Friday 6:00 p.m. - 1:00 p.m. (5:00 p.m. - Noon CT)`. ProductCode.TAS=`"HGT","HG0"` |
| `underlying-445-contractspecs.json` | `24f2cb543c1d6231015bfa41ba4ccfe7c62b7e545ac4eb226a8601968df9ea4c` | undated (live) | 2026-09-06T06:13:26Z | .../productId/445 | Palladium. `TAS:&nbsp;Sunday - Friday 5:00 p.m. - Noon CT` (60-minute-break clause GONE vs 2019) |
| `underlying-446-contractspecs.json` | `57f13e08ffcfdf91e048c5da2fd0fe91bcc9d4840cc328ca582701a8c10772eb` | undated (live) | 2026-09-06T06:13:29Z | .../productId/446 | Platinum. `TAS:&nbsp;Sunday - Friday 6:00 p.m. - 1:05 p.m. (5:00 p.m. - 12:05 p.m. CT)` |
| `gct-4346-contractspecs.json` | (see file) | undated (live) | 2026-09-06T06:13:09Z | .../productId/4346 | GCT has NO spec record of its own: every field `"-"`, `"ProductID":0` |
| `th-gct-4346-2026wk38.json` | `8b8fb7f2b1d9adab2770815a1e759fe72ec4c7b53c99fe87b1b4b9230a0fe3e9` | live | 2026-09-06T06:15Z | /services/trading-hours-by-product?id=4346&fromEventDate=2026-09-13&toEventDate=2026-09-19&pageSize=200 | Gold TAS Futures, prodGroup TG. `"hasEvents":false`, `eventCount 0`, seven empty day arrays |
| `th-sit-4347-2026wk38.json` | `89174d7bbf76866678ac652b8a6cc442848731c79244587cc106a3f7c2f4d6f9` | live | 2026-09-06T06:15Z | ...id=4347... | Silver TAS Futures, MT. Zero events |
| `th-hgt-4803-2026wk38.json` | `917957228467b90917b5a334eaba03dfaff5f11f2ca41f44986903096bab8615` | live | 2026-09-06T06:16Z | ...id=4803... | Copper TAS Futures, HT. Zero events |
| `th-plt-8335-2026wk38.json` | `b6a8befd18ea6edfdd8545a06390e6e6a5b535db91ab1a5b15623dcfe151b4b0` | live | 2026-09-06T06:16Z | ...id=8335... | TAS on Platinum Futures, PE. Zero events |
| `th-pat-8594-2026wk38.json` | `1ee3d114f0b71449dddbbbf036d17b7a0b28f693c9bdf8d183d6632a826d1f03` | live | 2026-09-06T06:16Z | ...id=8594... | Palladium TAS, PX. Zero events |
| `th-GCT-4346-jan.txt` (+ SIT/HGT/PLT/PAT siblings) | `223a8c141ada3f5fdf16cae43fe8c91b3d030c332a9713d0fd7b5e15034ff788` | live | 2026-09-06T05:41Z (Run A) | ...fromEventDate=2027-01-10&toEventDate=2027-01-16 | January-week probe. Same five groups, `"hasEvents":false` |
| `th-probe-gc-437-sep.json` | `e8fc3bba856ccc189a10ed6134fcc9ca39ecb2a7c9189c83e5d3e5b51661cfdc` | live | 2026-09-06T06:14Z | ...id=437... | POSITIVE CONTROL: GC group returns 6 events (preopen 16:00/16:45, open 17:00, closed 16:00) |
| `th-probe-gcd-8407-sep.json` | (see file) | live | 2026-09-06T06:14Z | ...id=8407... | POSITIVE CONTROL: gold **TAM** group GM returns 6 events incl. `closed@09:02` |
| `th-probe-es-133.json` | (see file) | live | 2026-09-06T06:14Z | ...id=133... | POSITIVE CONTROL: ES returns 6 events |
| `wiki-tas-457223974.json` | `318d34739e7f4e2e11fa0b1385ef5273259461e367ffe9f98601aa18591924ee` | v2, 2025-01-13T19:37:27Z | 2026-09-06T06:44Z | https://cmegroupclientsite.atlassian.net/wiki/api/v2/pages/457223974?body-format=storage | CME client wiki "Trade at Settlement - TAS": pause 16:00:00 Sun / 16:45:00 Mon-Thu CT, pre-open randomized within the following minute |

## B. CFTC-hosted NYMEX/COMEX rule filings (Run B; sha256 identical to the U-6 gate's copies)

Base: `https://www.cftc.gov/sites/default/files/stellent/groups/public/@rulesandproducts/documents/ifdocs/<file>`

| file | sha256 | artifact date | capture (UTC) | what it is |
|---|---|---|---|---|
| `rul083109nymexandcomex001.pdf` | `a5693b21c1e57d54b043968a5066afee3556d5758c047435fcfc59a10e2111f1` | 2009-08-31 | 2026-09-06T06:29Z | NYMEX Sub 09-189 / MRAN RA0907-4 (adv. 2009-09-01, rule eff. 2009-09-14). Rule 524.A.2 floor text; TAS-eligible list contains **no gold, silver or copper** |
| `rul020210nymexandcomex001.pdf` | `982b4026770c2180c191b8d72b6cfb95742bfd1bd16dac1817daeddacd3665b8` | 2010-02-02 | 2026-09-06T06:29Z | NYMEX/COMEX Sub 10-036R / RA1001-4, RA1002-4 (eff. 2010-02-07). Reprinted TAS list still has **no gold or silver** |
| `rul031110nymexandcomex001.pdf` | `5d343544cce771d79412e2d0c28a3ac60aea0b2dceeda5d22657aa19743f0c75` | 2010-03-11 | 2026-09-06T05:23Z (Run A) | **NYMEX/COMEX Sub 10-070 + SER S-5166.** COMEX self-certifies the gold/silver TAS launch: Globex **April 11**, trade date **April 12, 2010** |
| `rul100710nymexandcomex001.pdf` | `089a1416d33151fc78e1f502072691b61e761cec016b3d14e09bb16d0e59012b` | 2010-10-07 | 2026-09-06T06:29Z | Sub 10-284 / RA1005-4 (adv. 2010-10-11). GCT `12:30 p.m.-4:45 p.m. (ET)`, SIT `12:25 p.m.-4:45 p.m. (ET)` - the mislabelled-Central table |
| `rul102110nymexandcomex001.pdf` | `f694b26fd6f94577ea78777780b26110a59dccf0de906fbb1b155a3ac5707d88` | 2010-10-21 | 2026-09-06T06:29Z | Sub 10-306 / RA1006-4 (adv. 2010-10-22; TAS rule eff. 2010-11-01). Same table as **No-Activity Periods**, one hour later, correctly ET. GCT `1:30 p.m. - 5:45 p.m. (ET) Monday- Thursday / 1:30 p.m. (ET) Friday- 5:15 p.m. (ET) Sunday`; SIT `1:25 p.m.` |
| `rul010311nymexandcomex001.pdf` | `c0b7238dc5314cc77ffc57ff29b0bb47d29e79fbd77117a01d93cae6244d1fdd` | 2011-01-03 | 2026-09-06T06:29Z | Sub 10-391R / RA1101-4 (adv. 2011-01-05, eff. 2011-01-23). **First appearance of HGT**: `1:00 p.m.- 5:45 p.m. (ET) Monday- Thursday / 1:00 p.m. (ET) Friday-5:15p.m. (ET) Sunday` |
| `rul010611nymexandcomex001.pdf` | `a71fb96d6821ed4396be3c726c42beb9e299b55ae3f9e1de2a2b2706df193607` | 2011-01-06 | 2026-09-06T06:29Z | Sub 11-010 / RA1102-4 (adv. 2011-01-07, eff. 2011-01-23). Same three rows |
| `rul033111nymexandcomex001.pdf` | `afb98d313e603dae45aae0d47cb5463dfb395bbf849e88519dc8c0f32bbca84d` | 2011-03-31 | 2026-09-06T06:29Z | Sub 11-131 / RA1104-4 (adv. 2011-04-04, eff. **Sunday 2011-04-10 / trade date 2011-04-11**). Staggered TAS pre-opens: Gold 5:48 p.m./5:18 p.m. ET, Silver 5:49/5:19, Copper 5:50/5:20 |
| `rul062811nymexandcomex001.pdf` | `d4904557a0c1584789075d8266337e4c6758d6a3fc752dad5a6ddd4d467cfc5c` | 2011-06-28 | 2026-09-06T06:29Z | RA1106-4 (eff. 2011-07-11). Clock table **gone**; security-status-message definition only |
| `rul101811nymexandcomex001.pdf` | `dc2101966eb44469f1dc763f6528959b1f5a7d4a6bb4b9565ef936de1cd13c7f` | 2011-10-18 | 2026-09-06T06:29Z | Sub 11-381 / RA1107-4 (dated 2011-11-02 in-page). "the end of a TAS **trading session**..."; "TAS transactions are not allowed in any pit-traded Copper futures contract month"; MO copper pit RTH `8:10 a.m. until 1:00 p.m. ET` |

## C. CME notices and SERs

| file | sha256 | artifact date | capture (UTC) | URL | what it is |
|---|---|---|---|---|---|
| `SER-5542.pdf` | `afb408ac9d594f4724e4691948b5a0686a36af993699ed65037db030e10830b9` | 2010-12-22 | 2026-09-06T05:44Z (Run A) | https://web.archive.org/web/20120512095523id_/http://www.cmegroup.com/rulebook/files/SER-5542__10-12-22__TAS_COMEX.pdf | Copper TAS: "effective Sunday, January 23, 2011 for trade date Monday, January 24, 2011"; "TAS transactions are not allowed in any pit-traded Copper futures contract month" |
| `notice-20170508.html` | `dc9d9ed7594fc85541edb146471a59fb66cf15099d02d50e4547c05d761f2ef1` | 2017-05-08 | 2026-09-06T06:39Z | https://web.archive.org/web/20260214165515id_/https://www.cmegroup.com/notices/electronic-trading/2017/05/20170508.html | PLT listing: "Effective Sunday, May 21 (trade date Monday, May 22)". **Unconditional** |
| `notice-20180903.html` | `e59d77b3925953381f02cbf3c6c0b9add352a603ffe4a09b6acdf5ace45de0e0` | 2018-09-03 | 2026-09-06T06:39Z | .../web/20260214052421id_/.../2018/09/20180903.html | MGT listing: "Effective Sunday, September 23 (trade date Monday, September 24)". Unconditional - while the SONIA item in the same notice says "pending completion of all regulatory review periods" |
| `notice-20181112.html` | `200a14015c5c51c7f062f063ba956dfeb8e6113bb95d6ec1ee06f1ac410326bf` | 2018-11-12 | 2026-09-06T06:39Z | .../web/20260218023215id_/.../2018/11/20181112.html | PAT listing: "Effective this Sunday, November 18 (trade date Monday, November 19)". Unconditional |
| `notice-20250721.txt` | `500073fda485222046afb663cbec1aec89e395da794f4e8996b9f4a4c2fa4bc4` | 2025-07-21 | 2026-09-06T05:44Z (Run A) | https://www.cmegroup.com/notices/electronic-trading/2025/07/20250721.html | QOT/1OT/MHT/MST listing + MGT month expansion: "Effective this Sunday, July 27 (trade date Monday, July 28)". Group codes TG/TG/HT/MT |
| `notice-20150817.txt` | `4e9795989c02c2ce3da406ab96fbf425f726bb31ee8005f0b284f9b31fba7692` | 2015-08-17 | 2026-09-06T06:24Z | https://www.cmegroup.com/tools-information/lookups/advisories/electronic-trading/20150817.html | The DCM-wide 15-minute move: "Effective Monday, September 21 ... the closing times for the following markets will now occur 15 minutes earlier Monday through Friday **at 16:00 CT**: CME Equity / CBOT Equity / COMEX / NYMEX / DME. All other CME Globex markets trading hours remain unchanged." |
| `comex-25-240.txt` | `0b2060f40e1481f13345d66164e21a9392cf1c74032420051f8bf42d8a34573a` | 2025-07-02 | 2026-09-06T05:45Z (Run A) | https://www.cmegroup.com/content/dam/cmegroup/market-regulation/rule-filings/2025/7/25-240.pdf | COMEX Sub 25-240, TAS eligibility for QO/1OZ/MHG/SIL "effective on Sunday, July 27, 2025, for trade date Monday, July 28, 2025". No hours row |

## D. CME `/trading_hours/metals-hours.html` (retired; archive only)

URL for all four: `http://www.cmegroup.com/trading_hours/metals-hours.html`, replayed `https://web.archive.org/web/<ts>id_/<url>`.

| file | sha256 | artifact date | capture (UTC) |
|---|---|---|---|
| `metals-hours-20111029.html` | `2f7b312f8f705bb0504d8d5781c9a3b597b0d06ea14e1ef73c4c5df909d7c967` | 2011-10-29 | 2026-09-06T06:25Z |
| `metals-hours-20120501182431.html` | `feb67d4b9b8194c3ef65cc4f1a0ba903223b3e3347c635a7d44c10c791ed4d66` | 2012-05-01 | 2026-09-06T06:31Z |
| `metals-hours-20120616193920.html` | `9ceec3d4da4175fd7cf7bd22de7eb20e3e1d143ded6e1dbb19d98827d09fe936` | 2012-06-16 | 2026-09-06T06:31Z |
| `metals-hours-20150322121442.html` | `46170e4659dc7e94483c8c21931fdb54757cc5fcb3468c37115f2deb87443eda` | 2015-03-22 | 2026-09-06T06:31Z |

## E. CME server-rendered contract-specification pages (archive only)

Gold `http://www.cmegroup.com/trading/metals/precious/gold_contract_specifications.html`;
silver `.../silver_contract_specifications.html`; platinum `.../platinum_contract_specifications.html`;
palladium `.../palladium_contract_specifications.html`; copper `http://www.cmegroup.com/trading/metals/base/copper_contract_specifications.html`.

| file | sha256 | artifact date | capture |
|---|---|---|---|
| `wb-gold-spec-20150906022503.html` | `4a5aabb36c75467df83b32d5733d062c9bda8c0fa9fbaf6cf618be2a3e06672c` | 2015-09-06 | Run A | 
| `wb-gold-spec-20151009145054.html` | `118cff9844d9488fb17b1bc795cb7350d7dce9d3c4336ea9ec6554c574771278` | 2015-10-09 | Run A |
| `wb-gold-spec-20191118131805.html` | `b1f6141c42b0508641d535d13312f4f34b01150c089bdbfbee543bbd8e898b44` | 2019-11-18 | Run A |
| `wb-pl-spec-20170610040445.html` | `f780dc25aea53937723da0112be8374e678c6e8c3a3ceab4b0bb502a02746f2f` | 2017-06-10 | Run A |
| `wb-pl-spec-20170802234329.html` | `7c2284e75c148661b5955863c208d65ab0f91e1810c5868e655834f166ef9f4a` | 2017-08-02 | Run A |
| `wb-pl-spec-20190717122952.html` | `b9bbf1eb7df62566317afa616107207c44bdea33a4ce92986067817b6b4815a8` | 2019-07-17 | Run A |
| `wb-pl-spec-20210411151252.html` | `62df5ac7fd9939c04b3e6f0d5772f18ffe73241d14532332ae5a4aeb1de5e064` | 2021-04-11 | Run A |
| `wb-palladium-spec-20190717064606.html` | `4bd2d7deae495f0bea992f58fb6696d2b5ad50c7522b9e820f4cc2b7e6d69104` | 2019-07-17 | Run A |
| `wb-copper-spec-20170613052441.html` | `11ce3c33b18b5183bcd6f96139819d3526cffd7f9f257f3c63ef4ff64c8c8afe` | 2017-06-13 | 2026-09-06T06:35Z |
| `wb-copper-spec-20180810034204.html` | `041d56cc9b61190f9a7769087969f4f230036a56b6b48b7d3b27ad8076ccb816` | 2018-08-10 | 2026-09-06T06:35Z |
| `wb-copper-spec-20191220234431.html` | `c6a67b23a33a7f7bc645c04f1c98a3e06cc1abb4e751a404e9360ee2fc4c4191` | 2019-12-20 | 2026-09-06T06:35Z |
| `wb-copper-spec-20210621090253.html` | `254d4c07203216c8bcaf6d4970833e8311642b8e8b0401b3305417f13f351f1d` | 2021-06-21 | Run A |

## F. Archived `/CmeWS/mvc/ContractSpecs/List/productId/N` (this is what closes 2021-07 -> today)

Replayed `https://web.archive.org/web/<ts>id_/https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/<N>?isProtected&_t=<...>`.
All fetched 2026-09-06T06:19Z-06:22Z (Run B).

| file | sha256 | productId | artifact date |
|---|---|---|---|
| `wb-437-20210710.json` | `018f81ef2bf19e21b113614d1d82b59fa813793b650e117c062fe83b1bff24db` | 437 | 2021-07-10 |
| `wb-437-20230617.json` | `725b81b65b7ee124c4e257a8ac9d72a32be17216eb9bbbbf1b387589f2b684de` | 437 | 2023-06-17 |
| `wb-437-20250604.json` | `3673e5c5c2cfb7fd526f3260bf716ac8966a4246fb7d641d01fa72a6570bbc05` | 437 | 2025-06-04 |
| `wb-437-20260527.json` | `79158cb94dad425681cffc447eaf551c1a136e1782b710badcd548b1feb46a2d` | 437 | 2026-05-27 |
| `wb-458-20210710.json` | `109a909504e652ef4a1f13db4629f9cfcf7966981fd2c2478a7fc976eb5a9db7` | 458 | 2021-07-10 |
| `wb-458-20221003.json` | `109a909504e652ef4a1f13db4629f9cfcf7966981fd2c2478a7fc976eb5a9db7` | 458 | 2022-10-03 (byte-identical to 2021-07-10) |
| `wb-458-20230713.json` | `cc2737927e168e981fb1a79d4d712d52d4b22ffc4723b14adff58005ae04ae8a` | 458 | 2023-07-13 |
| `wb-458-20231219.json` | `ae41102be58ffa22b6462434650ac9d8aeffbfb0be7e6db2339aa94a7c61650d` | 458 | 2023-12-19 |
| `wb-458-20240208.json` | `ae41102be58ffa22b6462434650ac9d8aeffbfb0be7e6db2339aa94a7c61650d` | 458 | 2024-02-08 |
| `wb-458-20260227a.json` | `3590fb07383e195aa3f1a831863f66a4a25f60da17ad7a98f2b1fa5aa5d302fc` | 458 | 2026-02-27 |
| `wb-458-20260527.json` | `a3bac3a790af91df409f2e4bd352ba752089f2077e6d4e7815e6357cf5d8b1b8` | 458 | 2026-05-27 |
| `wb-438-20210710.json` | `cdddfa19e16667c929bc498b77f91000be1ad60e8f95cd3c15f05cd130b2b00e` | 438 | 2021-07-10 |
| `wb-438-20240802.json` | `da8c41e1098170c54b271b28be84e5b948c7488812ffaae21f847f59a4dc1cea` | 438 | 2024-08-02 (digest repeats at 2026-02-04 and 2026-02-09) |
| `wb-445-20260527.json` | `ab2483236f40c92d4af2594073b3273e6d00638713d743394bfab64e61490e36` | 445 | 2026-05-27 |
| `wb-446-20260310.json` | `1cc08c19e00f6004155eb0c7b640a0974d233754724f44e2f0be06d485e6f01c` | 446 | 2026-03-10 (digest repeats at 2026-04-10) |

CDX index of that channel (Run B, no digest collapse) is reproduced in the gate JSON's `dead_ends`.

---

## Run C — 2026-09-06T06:55Z-07:17Z (verification + two closures)

Run C re-verified every load-bearing Run-A/Run-B artifact **from the bytes** (each CFTC PDF
re-fetched from cftc.gov and its sha256 matched; each archived capture re-parsed and its quote
re-read) and then closed two of the gate's open items. `.txt` siblings of PDFs are local
`pdftotext -layout` renders with no independent URL.

### C.1 Live CME channels re-verified (via the public text reader in front of the CME URL; bare curl and full-browser-header curl both still 403 from this host)

| file | sha256 | capture (UTC) | CME URL | note |
|---|---|---|---|---|
| `gc-437-contractspecs.txt` | `2cd3f1e0368651438e66aa5b8e2ba2ba5cdcc1cf00cc299555d459610b6e4fc8` | 2026-09-06T06:55Z | .../CmeWS/mvc/ContractSpecs/List/productId/437 | byte-identical to Run B's `underlying-437-contractspecs.json` |
| `cs-458.txt` | `c2fda2291d73ce502f1cb3f2b4e9be45f42422a60c52d9da84f1ac4a4e9743a3` | 2026-09-06T06:55Z | .../productId/458 | identical to Run B |
| `cs-438.txt` | `289755c2a9fd36dadd04a8bd27bdf7d3e368aaa0503af7e696a4d4628d9f3ad9` | 2026-09-06T06:55Z | .../productId/438 | identical to Run B |
| `cs-445.txt` | `24f2cb543c1d6231015bfa41ba4ccfe7c62b7e545ac4eb226a8601968df9ea4c` | 2026-09-06T06:55Z | .../productId/445 | **Palladium** (ProductName "Palladium Futures", ProductCode.TAS "PAT"). The gate brief's product-id labelling (PL=445, PA=446) is inverted |
| `cs-446.txt` | `57f13e08ffcfdf91e048c5da2fd0fe91bcc9d4840cc328ca582701a8c10772eb` | 2026-09-06T06:55Z | .../productId/446 | **Platinum** (ProductCode.TAS "PLT") |
| `cs-4346.txt` | `a7882eb72c1715d99bdb624bcce52c6abc887a549926aeca8df1b23a12d78ab0` | 2026-09-06T06:56Z | .../productId/4346 | GCT: every field `"-"`, `"ProductID":0` (same for 4347/4803/8335/8594/8585/11176/11178/11179/7909) |
| `slate-8.txt` | `f709b8532f7b8193ed27a2bac5f69b1494b08cd84ad3228e28e5b9d7e3bf0438` | 2026-09-06T06:56Z | .../CmeWS/mvc/ProductSlate/V2/List?...&group=8 | the metals slate: GCT 4346, SIT 4347, HGT 4803, HG0 7909, PLT 8335, PAT 8594, MGT 8585, QOT 11176, MHT 11178, MST 11179, GCD 8407, HGF 8652. **1OT has no slate row of its own** |
| `th-437-sep.txt` | `61b2d3e2f0ceae3e046e851bf4b7235d8d3a23557db5473c292eb480f69d013a` | 2026-09-06T06:56Z | /services/trading-hours-by-product?id=437&fromEventDate=2026-09-06&toEventDate=2026-09-12&pageSize=100 | POSITIVE CONTROL, group GC, 6 events |
| `th-8652-sep.txt` | `c6b39cf763aa6a12345fca6263b616a325d50920df2eee99403e25e8f197cdde` | 2026-09-06T06:57Z | ...id=8652... | POSITIVE CONTROL, copper TAM group TR, `closed@06:35` |
| `th-4346-sep.txt` / `th-4347-sep.txt` / `th-4803-sep.txt` / `th-8335-sep.txt` / `th-8594-sep.txt` | `9e48233750d9d18b…` / `e51dca5716b4b45f…` / `7c96c742c5075fab…` / `206abf37ff5e7425…` / `3cf822fdca469b0f…` | 2026-09-06T06:56-06:57Z | ...id=4346/4347/4803/8335/8594... | September-week repeat of the Run-B negative: `eventCount 0` for TG, MT, HT, PE, PX |

The `pageSize` parameter is REQUIRED on `/services/trading-hours-by-product`; without it the
endpoint returns HTTP 400 `Requiered Parameters Missing`.

### C.2 CFTC PDFs re-fetched and hash-matched (2026-09-06T07:00-07:02Z)

`rul100710` `089a1416d33151fc78e1f502072691b61e761cec016b3d14e09bb16d0e59012b`,
`rul031110` `5d343544cce771d79412e2d0c28a3ac60aea0b2dceeda5d22657aa19743f0c75`,
`rul102110` `f694b26fd6f94577ea78777780b26110a59dccf0de906fbb1b155a3ac5707d88`,
`rul010311` `c0b7238dc5314cc77ffc57ff29b0bb47d29e79fbd77117a01d93cae6244d1fdd`,
`rul033111` `afb98d313e603dae45aae0d47cb5463dfb395bbf849e88519dc8c0f32bbca84d`,
`rul083109` `a5693b21c1e57d54b043968a5066afee3556d5758c047435fcfc59a10e2111f1`,
`rul020210` `982b4026770c2180c191b8d72b6cfb95742bfd1bd16dac1817daeddacd3665b8`,
`rul101811` `dc2101966eb44469f1dc763f6528959b1f5a7d4a6bb4b9565ef936de1cd13c7f`.
All eight quotes re-read from the `pdftotext -layout` render this run.

### C.3 NEW — the TAS pre-open randomization is DATED (closes most of Run B's open item 9)

| file | sha256 | artifact date | capture (UTC) | URL |
|---|---|---|---|---|
| `wb-notice-20120409.html` | `2aaa54eb1113266d4ffae4bf1bc7445d31396c0c1ee26eda785968f7cb5a4f49` | 2012-04-09 | 2026-09-06T07:09Z | https://web.archive.org/web/20190716…id_/https://www.cmegroup.com/tools-information/lookups/advisories/electronic-trading/20120409.html |
| `wb-notice-20120402.html` | `1c63399d159d79c9afaba13e0d8263219ff9f52a50b5c9ccdb92723a4ad60797` | 2012-04-02 | 2026-09-06T07:09Z | …/20120402.html (same item, announced a week earlier) |

Verbatim: *"Trading At Settlement (TAS) Pre-Open Timing Changes — On **Sunday, April 15** (trade
date Monday, April 16), in order to ensure appropriate and efficient messaging practices for TAS
orders into CME Globex, CME Group will randomize the timing of each TAS groups' pre-open state.
With this change, the market states sequence will change. There will be a market pause,
communicated via the FIX/FAST Security Status message (tag 35-MsgType=f),
tag 326-SecurityTradingStatus=2 at 16:15:00 on Sunday and 16:45:00 Monday through Thursday. TAS
groups will then go into pre-open on Sundays between 16:15:00 and 16:16:00 Central time (CT), and
Mondays through Thursdays between 16:45:00 and 16:46:00 CT."* No conditional clause.

Negatives bounding it: `wb-notice-20120416/0423/0430/0507/0514/0518/0521/0528/0604/0611/0618/0625.html`
carry no TAS pre-open item (2012-04-16 and 2012-04-23 mention TAS only in a NYMEX B/C-Index
delisting item).

### C.4 NEW — palladium TAS at the 2020/2021 boundary

| file | sha256 | artifact date | capture (UTC) |
|---|---|---|---|
| `wb-palladium-spec-20201126020132.html` | `e9b983dbe0d269bd5b34a869913a5d7609586dcaee037dbca95063a7f4b76473` | 2020-11-26 | 2026-09-06T07:07Z |
| `wb-palladium-spec-20210513093821.html` | `00a735dbc7f2809c053fb196935103a6e719e2a8432f67c6efb886bbcd6b96eb` | 2021-05-13 | 2026-09-06T07:07Z |

Both: *"TAS: Sunday - Friday 6:00 p.m. - 1:00 p.m. (5:00 p.m. - Noon CT)"* — same instants as
2019-07-17, and the inherited "60-minute break" clause is already gone by 2020-11-26.

### C.5 NEW — HG0 notice sweep (bounded negative)

`notices1718/<YYYYMMDD>.html`, 70 files, aggregate sha256 of `cat notices1718/*.html` =
`f0aa0d6bed7ad1dd2513f2e8ef0b0091a0485149ad19b2ee93a8dc6d5c792282`. Every archived weekly CME
Globex notice from 2017-06-05 to 2018-08-27 inclusive (70 of 70), replayed
`https://web.archive.org/web/<ts>id_/<notice url>`; index and timestamps in `win.tsv`
(from `cdx-notices-2017.json` / `cdx-notices-2018.json`). None contains `HG0`, `Spot TAS`,
`TAS zero` or `TAS flat`.

### C.6 NEW — archive bounds for platinum/palladium ContractSpecs

`cdx2-445.json` (1 row, 20260527221952) and `cdx2-446.json` (2 rows, 20260310171835 and
20260410064201) — CDX prefix, `filter=statuscode:200`. Those are the only archived captures of
that API path for the two PGM ids.
