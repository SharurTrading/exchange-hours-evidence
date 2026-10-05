<!-- SPDX-License-Identifier: MIT-0 -->

# U1-btic-equity-conflict — retrieved artifacts

Gate: **U-1** (EST / NQT / YMT / IPT / RVT equity-index BTIC). Capture window: 2026-09-06T05:14Z - 2026-09-06T05:45Z.
Retrieval channels: (1) public text reader `https://r.jina.ai/<cmegroup.com URL>` - cmegroup.com returns HTTP 403 to this host at IP level, confirmed again today on `/content/dam/...`; (2) web.archive.org `id_` replay; (3) direct GET to cftc.gov (works).
`capture_ts` below is the observation time on this machine, not the artifact's own date.

| file | bytes | sha256 | capture_ts (UTC) | source URL |
|---|---|---|---|---|
| `cdx-cs-7968.json` | 3 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 2026-09-06T05:18:05Z | web.archive.org CDX prefix search for ContractSpecs productId 7968 — EMPTY (no captures) |
| `cdx-cs-7969.json` | 3 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 2026-09-06T05:18:17Z | CDX prefix search, productId 7969 — EMPTY |
| `cdx-cs-8027.json` | 3 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 2026-09-06T05:18:19Z | CDX prefix search, productId 8027 — EMPTY |
| `cme-equity-index-futures-options-2021.md` | 5964 | `5b4d9fda2e0b69eb1e39bf6250e7ab7b637d1dbc9c0a114a0d678113d745ed6f` | 2026-09-06T05:26:29Z | https://www.cmegroup.com/content/dam/cmegroup/notices/electronic-trading/2021/06/cme-equity-index-futures-options.pdf (via r.jina.ai) |
| `cs-133-live.txt` | 4504 | `556324d02d0087e6e1c8b9cbfe528deebb2164e67abb6e0a1858873c4708f252` | 2026-09-06T05:15:06Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/133 (via r.jina.ai) |
| `cs-166-live.txt` | 2826 | `abbfcc7a278b56628b1baeec25db6c4f68660cb33203ff0b857041fcdec94da7` | 2026-09-06T05:37:56Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/166 (via r.jina.ai) |
| `cs-170-live.txt` | 2750 | `56ea67101164fd74412b8328884ff11398a7c1168c91eaee7caffd9d3512793d` | 2026-09-06T05:37:55Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/170 (via r.jina.ai) |
| `cs-7945-live.txt` | 2713 | `c363f8f2197aa1544a98216891e3eaee3bd16a67d096e26f64f4205f2c38478f` | 2026-09-06T05:37:55Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/7945 (via r.jina.ai) |
| `cs-7948-live.txt` | 2730 | `2aa822aac734450ebc2b811fb3b892b64fe7615a9b630618ca6e7b61ae2a342d` | 2026-09-06T05:15:06Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/7948 (via r.jina.ai) |
| `cs-7949-live.txt` | 831 | `45316ca4c9bca98f9ef4a24684f6eb2352749d61c30d13e239e64f0ebdf3fc81` | 2026-09-06T05:22:18Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/7949 (via r.jina.ai) — returns "-" (no spec record for RVT) |
| `cs-7968-live.txt` | 1906 | `f4346fdbcd246ca748a17e2277277a628d12d58510777db4e2d7f0c0ef68da26` | 2026-09-06T05:14:57Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/7968 (via https://r.jina.ai/) |
| `cs-7969-live.txt` | 2222 | `03efe114faaad6108b706c1bc7a818a33e226cf58cdcd5b0b5b58512c7c25444` | 2026-09-06T05:15:07Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/7969 (via r.jina.ai) |
| `cs-7970-live.txt` | 831 | `0a201be89ec2a48dafc108c5fd51ebcc029695928d5e66f30805e37c8e8b662e` | 2026-09-06T05:22:43Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/7970 (via r.jina.ai) — returns "-" (no spec record for YMT) |
| `cs-8026-live.txt` | 2666 | `83d1ab60aba9cfdac0f4de93e3ef53e7049d9a59fc6740fa3f2e98a28b84c052` | 2026-09-06T05:37:42Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8026 (via r.jina.ai) |
| `cs-8027-live.txt` | 2134 | `806de9ce226e6c68793b01906d3fb63218ec5d225ca5a6a19920e583582da380` | 2026-09-06T05:15:05Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8027 (via r.jina.ai) |
| `cs-8314-live.txt` | 4281 | `90b2b39b749ba6069d3aaa46a7b9526bfed1ff6d0a5cc66f8affd2f613b1b754` | 2026-09-06T05:37:56Z | https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/8314 (via r.jina.ai) |
| `es-spec-20151115083010.html` | 81090 | `cf2178f1c23bc714c74f0d433e9220fd088146ec089d57068f7aac9772e24a1f` | 2026-09-06T05:38:51Z | https://web.archive.org/web/20151115083010id_/http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500_contract_specifications.html |
| `es-spec-20160201022054.html` | 96650 | `fc53b6b90d3554a8e16cbf13d310d8287316e3c4811c9ad6cfd0901aca9f02a7` | 2026-09-06T05:38:52Z | https://web.archive.org/web/20160201022054id_/http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500_contract_specifications.html |
| `es-spec-20180419185207.html` | 128680 | `31dff59831ef7093e1fa457e848f13db031f9abcc11f62328a2adc422a0c3404` | 2026-09-06T05:39:26Z | https://web.archive.org/web/20180419185207id_/https://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500_contract_specifications.html |
| `es-spec-20190130110517.html` | 124199 | `436f1da44fa79cb29da72c7a27bad95d605d5e3133275a4aac3b8fcce2c6b7c2` | 2026-09-06T05:39:27Z | https://web.archive.org/web/20190130110517id_/https://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500_contract_specifications.html |
| `es-spec-20210610062512.html` | 14322 | `2c3de7a76bc345e3bf2458dc83ec948d7c3143d20e0c2bc1db4c21f30063adb1` | 2026-09-06T05:42:53Z | https://web.archive.org/web/20210610062512id_/... — JS shell, no server-rendered hours (negative) |
| `es-spec-20210703123520.html` | 28997 | `2881dae967bbd1da7e25f18da9fba3c5c3cd79d2ce4a42a79b5ee4d87092c97b` | 2026-09-06T05:42:54Z | https://web.archive.org/web/20210703123520id_/https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html — JS shell (negative) |
| `globex-notice-20210621.md` | 23688 | `f299aa894083a41cc4af59084ba990a466f7a1456ed20d59992b20ac0304837b` | 2026-09-06T05:26:04Z | https://www.cmegroup.com/notices/electronic-trading/2021/06/20210621.html (via r.jina.ai) |
| `npsummary-btic-es-nq-2015.pdf` | 53072 | `0aa4b0e8968535e7f915f6cbee3ca4810cc86666d67343b24bd969f180f13ecf` | 2026-09-06T05:20:02Z | https://www.cmegroup.com/tools-information/lookups/advisories/electronic-trading/files/btice-minisp_nq.pdf via https://web.archive.org/web/20210116202108id_/ |
| `npsummary-btic-es-nq-2015.txt` | 4506 | `4d7695a821e78640e54a3cb0e13b440828d964320d4f33220261e9c4b8d297f8` | 2026-09-06T05:20:39Z | pdftotext -layout of the above |
| `npsummary-btic-ym-2015.pdf` | 52095 | `9457184ee5f67c9e49d907c3e40165408dc2a545a43d1db99d9c6cfbada805cd` | 2026-09-06T05:20:32Z | https://www.cmegroup.com/tools-information/lookups/advisories/electronic-trading/files/btice-minidowfutures.pdf via https://web.archive.org/web/20151112131859id_/ |
| `npsummary-btic-ym-2015.txt` | 3662 | `f9d0bf98c70744aa87e2b5b46e75f24b4d0d6007a2af737c382aa938077536d3` | 2026-09-06T05:20:39Z | pdftotext -layout of the above |
| `ser-8788.md` | 36829 | `044020951d735ddaf432f98df03b2d8ad5fe4379188ebf94755136e98ac1df24` | 2026-09-06T05:25:43Z | https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2021/06/SER-8788.pdf (via r.jina.ai) |
| `slate-equities.txt` | 152553 | `480fa58fc1c0415148f352edddcecd8081e8d33863a5be32931707620051809c` | 2026-09-06T05:21:20Z | https://www.cmegroup.com/services/product-slate?sortField=globexCode&sortAsc=true&pageSize=500&pageNumber=1&cleared=Futures&group=4 (via r.jina.ai) — CME equities futures slate, 285 rows; source of productId 7949=RVT, 7970=YMT, 8026=IPO |
| `slate-equity.txt` | 260 | `ebed373e3732b47086f075aec436c9830f69f19dfda57ef794b9ecdf30738dda` | 2026-09-06T05:17:19Z | same service with group=Equity%20Index — 502, kept as channel note |
| `th-133-sep.txt` | 1936 | `f125e6b7e5a4ecb8278765d42e4b710cea09c553abf0f29211926e6b2b7a1b9b` | 2026-09-06T05:16:32Z | single-id probe, id=133, 2026-09-06..2026-09-12 |
| `th-7948-sep.txt` | 1977 | `e98b1352d98403dbcfd46eeee90b8d2d7c7967fdfeb70ddb3cf1776cc698a14b` | 2026-09-06T05:16:19Z | single-id probe, id=7948, 2026-09-06..2026-09-12 |
| `th-7968-sep.txt` | 1794 | `9bcf3cb7154d24b5b4b57140df8b6c4d1a7f8effc8d9d2317d1fb88ff0e619e5` | 2026-09-06T05:15:54Z | single-id probe, id=7968, 2026-09-06..2026-09-12 |
| `th-7969-sep.txt` | 337 | `c408437c8efd760d198b947f250a3c025ec6d05ed8da92f093e58bf0c46a81b6` | 2026-09-06T05:15:34Z | single-id probe without pageSize — 400 Bad Request, kept as channel note |
| `th-8027-sep.txt` | 1824 | `2e334fec71135b3df8eaea72adda55c5d52cfc627f2685133c142e7823ec90b4` | 2026-09-06T05:16:07Z | single-id probe, id=8027, 2026-09-06..2026-09-12 |
| `th-more-normal.txt` | 9144 | `60dfac8b202a230bed2b1c6bf91934eb162b03bc60e0872f85a983baac69a8ae` | 2026-09-06T05:38:12Z | same service, id=7596,7946,7947,8315,8026, 2026-09-13..2026-09-19 |
| `th-multi-dec.txt` | 10825 | `9affd5967fd4fc42e7f2bfbb099665073ca45cd1e5f47bede05316d7edbc6354` | 2026-09-06T05:24:25Z | same service, fromEventDate=2026-12-06&toEventDate=2026-12-12 (DST probe) |
| `th-multi-normal.txt` | 10825 | `812f64e6c2aa16e8ab1bb4981894a85a2b4b10de55b196cdfe26a1546c1129b3` | 2026-09-06T05:24:16Z | https://www.cmegroup.com/services/trading-hours-by-product?id=7968,7969,7970,7949,8027,133&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-09-13&toEventDate=2026-09-19 (via r.jina.ai) |
| `th-multi-sep.txt` | 9619 | `f8aa567b7b495b10c752a80c95d4ff1ec7eb768932be91bbf6ce507c435edecf` | 2026-09-06T05:24:03Z | same service, fromEventDate=2026-09-06&toEventDate=2026-09-12 (US Labor Day week) |
| `cftc/ptc030918cmedcm001.pdf` | 549026 | `b51df55f3b007a2625130954be60b40d3d5aa33629c0f864784f88473f3466f9` | 2026-09-06T05:32:48Z | https://www.cftc.gov/filings/ptc/ptc030918cmedcm001.pdf — CME Submission 18-070 (2 of 2), sector BTIC listing, states BTIC Globex hours |
| `cftc/ptc030918cmedcm001.txt` | 18398 | `80702cf8a4041b2b13ab24803aa8879ced5a827be06028f3ae314f2f5824c8de` | 2026-09-06T05:32:48Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc0409261062.pdf` | 567355 | `5c5db31ecbe0c527334de65bc2478d3bd254625744801fce4807da3275466740` | 2026-09-06T05:37:30Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc0409261062.txt` | 67568 | `4f22bac0a7fb1679eec7c8657539e113a2bfcb261bdc5239e81a6827e2b33a1e` | 2026-09-06T05:37:30Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc092515cmedcm001.pdf` | 281225 | `3bf2327c1577ad8c57d743c934a3e06d95ce606ad9e60e2a2c06f86bd73780f6` | 2026-09-06T05:35:14Z | https://www.cftc.gov/sites/default/files/filings/ptc/15/09/ptc092515cmedcm001.pdf — CME 15-410, FTSE 100 / FTSE China 50 initial listing (lead for the FTC gate, not U-1) |
| `cftc/ptc092515cmedcm001.txt` | 80065 | `121f445a8f9c82ec9ebc559dba811f6e4c2b2e45c98a73540a3742283c6bc144` | 2026-09-06T05:35:15Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc100615cbotdcm001.pdf` | 415790 | `86f8b6976161ea2003f45440fa7e4f0fa60898dcf5b3ebf7ca550c3f9d5bb2b5` | 2026-09-06T05:33:57Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc100615cbotdcm001.txt` | 12075 | `3e1817adb7639c0bf2f380f404cba34edfcb95092c585207fc09e2c573c35f58` | 2026-09-06T05:33:57Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc100815cbotdcm001.pdf` | 560741 | `d40d9deb5a71210f6ed3c461d5e77d240c5919cad7759ef98a2df5073b2889b0` | 2026-09-06T05:33:57Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc100815cbotdcm001.txt` | 30874 | `a648576bdaea917987e2afb70a3c8e9702482705797701a77a96d409f33270e8` | 2026-09-06T05:33:57Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc100915cmedcm001.pdf` | 444702 | `c31e6ce53da1806310753846259c17066441e420972370beddfaf84e0dc3116e` | 2026-09-06T05:33:58Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc100915cmedcm001.txt` | 59949 | `4740ff9406e25d9d4f88efff27a64fcd66851cbb1df697c57b1cb2b5d8c1ee50` | 2026-09-06T05:33:58Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc101615cbotdcm001.pdf` | 695363 | `b387cb9e094f5cc554cf9d4d1525f6b911a2ae59dbce585c06da21a592925b1f` | 2026-09-06T05:33:58Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc101615cbotdcm001.txt` | 41800 | `5da28905468aa0d2523c2ce164fbf08382f4f66ab782905f7aa1cc2538ce430c` | 2026-09-06T05:33:58Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc102215cmedcm001.pdf` | 459751 | `f46b8a1214bca117f2559e464135f20799e0d034007cfb24d09dde892214422b` | 2026-09-06T05:33:58Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc102215cmedcm001.txt` | 8160 | `e3b23cd53e4b2f56efc1de188f16b50dc4eb4e379d6da0e420c4b76ec8dac18f` | 2026-09-06T05:33:58Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc102615cmedcm001.pdf` | 449474 | `9773d305868b982d09b66b6158786bd12743bc7bf221e3a319450f1cfaf47e0b` | 2026-09-06T05:33:58Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc102615cmedcm001.txt` | 25124 | `8cc2bf9c1d4733733ddd9d1e5876ba7fc1ecb25fb9ecf1a25a06dbbf771edd50` | 2026-09-06T05:33:58Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc102915cbotdcm001.pdf` | 491911 | `97ad25d6f652992cff135189a85cd369e689dd2c87aaa732c5e615617d58a521` | 2026-09-06T05:36:43Z | https://www.cftc.gov/sites/default/files/filings/ptc/15/10/ptc102915cbotdcm001.pdf — CBOT Submission 15-437, the YMT BTIC launch certification |
| `cftc/ptc102915cbotdcm001.txt` | 13591 | `edb59d9bead2d98021120a9033cc10a75021e2442066dc33685913a488cbfd98` | 2026-09-06T05:36:43Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc102915cmedcm001.pdf` | 499411 | `f207101167091f35406dceb4fd0c7bf2e4d9290b169ef3f57ba74a3fd0077938` | 2026-09-06T05:36:43Z | https://www.cftc.gov/sites/default/files/filings/ptc/15/10/ptc102915cmedcm001.pdf — CME Submission 15-438, the EST/NQT BTIC launch certification |
| `cftc/ptc102915cmedcm001.txt` | 17598 | `c787fa0441a627050d0cf70399bf662ed0c573a660f59227af2f8cfbea0765d1` | 2026-09-06T05:36:43Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc102915cmedcm002.pdf` | 689142 | `6748a83009c8b4f92763d1c752df145ef65beb17cbbf22fa2986d2e12eb72223` | 2026-09-06T05:36:43Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc102915cmedcm002.txt` | 52207 | `377f355e7b0cb6307022c929a0e48c701a7569b12e711e5fb5d1dfdf5e663ac6` | 2026-09-06T05:36:43Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc103015cmedcm001.pdf` | 685390 | `1f6a3f4242d1ca9ef1e8c7ab57355503a417140b50b3ce9e9046d78d331d07a3` | 2026-09-06T05:36:43Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc103015cmedcm001.txt` | 53765 | `a84c8cd58643d41bed2262455b277b1c2e4bd9ff9812323881e5ae35aa97af10` | 2026-09-06T05:36:43Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc103015cmedcm002.pdf` | 685377 | `edc48dc861b4e2f2621e9c7bffbd689402ac54d4496d42d0cade5c3c0ccc35b4` | 2026-09-06T05:36:44Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc103015cmedcm002.txt` | 53765 | `11fd4d05a5bfaac028cf097c8417e1b0e932c2d1f3542a813f7b2eacdf229e7d` | 2026-09-06T05:36:44Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc111415cbotdcm001.pdf` | 634839 | `877d55d70bba2861f9459b0b4692b642eee5b02f9f2968e2a0d754c50e4dc530` | 2026-09-06T05:36:44Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc111415cbotdcm001.txt` | 47265 | `322a632364f83ced2ee8aed7f5534fc5838a37010572cc4c98187ee8bcaaab3c` | 2026-09-06T05:36:44Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc111815cmedcm001.pdf` | 461868 | `942b0fcb1365ae7e984c804afb46e0515e445dfedd1c065ea85389f18985d5be` | 2026-09-06T05:33:59Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc111815cmedcm001.txt` | 8249 | `68714984718f3942e39d441b17d7580613b9e4fc314c1aa6c6080079889cdb7c` | 2026-09-06T05:33:59Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc111915cbotdcm001.pdf` | 469729 | `95e3d3a350c93b00dce90c0fef9d12bed2c46b9c4f3dc69c7312e748796e801c` | 2026-09-06T05:33:59Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc111915cbotdcm001.txt` | 9000 | `dde2b4b02daceba5efdefd87cd54afced29da0231991b836674edd8f617c6a43` | 2026-09-06T05:33:59Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc111915cmedcm001.pdf` | 466871 | `ecaddf138c69ccca619d9489512e4410fe32a9b45cc2983e87205f223d7b9b50` | 2026-09-06T05:33:59Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/ptc111915cmedcm001.txt` | 8703 | `b993e4810aa63de4940c8b43121f961c93834892822c95dea86bcd3a457f65bc` | 2026-09-06T05:33:59Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/rules09032529907.pdf` | 156731 | `5582da811fed24e0deec900ecf3979056101f9bc5f9c968765e08444f92a7fe1` | 2026-09-06T05:43:33Z | https://www.cftc.gov/sites/default/files/filings/orgrules/25/09/rules09032529907.pdf — CME 25-368, SMET BTIC MM program, 'Designated hours during Regular Trading Hours ("RTH")' |
| `cftc/rules09032529907.txt` | 5865 | `b641db04388986c6d0f05ec2dcff7ae86fcd3b5a69a1a85413097a7c0afd6be7` | 2026-09-06T05:43:33Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |
| `cftc/rules12302535976.pdf` | 161563 | `73048173e85fc3969497967157fdd86c131f55b0809bda9b4f4496c93eda1f9a` | 2026-09-06T05:34:30Z | https://www.cftc.gov/sites/default/files/filings/orgrules/25/12/rules12302535976.pdf — CBOT Submission 25-546 (2 of 2), BTIC Market Maker Program, names RVT and gives the RTH label |
| `cftc/rules12302535976.txt` | 6838 | `2b0024012a23f91f081961cf868806a25804de24368c47d3a8ac6f71a5946f24` | 2026-09-06T05:34:30Z | (search by-product of the CFTC ptc filename probe for Oct-Nov 2015; kept as negative evidence — none mentions BTIC) |

## Second pass — 2026-09-06T06:14Z–06:20Z (verification + archive-history closure)

The first pass's 42 artifacts were re-verified on disk: every sha256 above still matches, and every
verbatim quotation carried into the gate result was re-read from the bytes (not from the earlier
note). Six new artifacts close the archive-history question the gate asked for explicitly.

| file | bytes | sha256 | capture_ts (UTC) | source URL |
|---|---|---|---|---|
| `cdx-cs-7948.json` | 3 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 2026-09-06T06:15:10Z | CDX prefix search, `cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/7948*` — EMPTY (no captures) |
| `cdx-cs-7949.json` | 3 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 2026-09-06T06:15:14Z | CDX prefix search, productId 7949 (RVT) — EMPTY |
| `cdx-cs-8026.json` | 3 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 2026-09-06T06:15:18Z | CDX prefix search, productId 8026 (IPO) — EMPTY |
| `cdx-cs-166.json` | 225 | `e66fa61d27aeca39febfc775a54a6a4681d47765dfc69a72b8a056cb8178d360` | 2026-09-06T06:15:22Z | CDX prefix search, productId 166 — exactly ONE capture, `20210710091114`, status 200 |
| `cs-166-wb-20210710.json` | 1190 (gzip; 2664 uncompressed) | `671a8d251b449b54ea080599f7a642b0705474a9b33a35db6c168cc8387a5a95` | 2026-09-06T06:16:40Z | `https://web.archive.org/web/20210710091114id_/https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/166?isProtected&_t=1625908274614` — the only archived capture of the modern ContractSpecs channel for any product in this gate |
| `cdx-th-service.json` | 170938 | `b6361a5dfa6a8125aa4c5eff9714df55c1ce96bf03514361f1cc4ddbdafd1b28` | 2026-09-06T06:18:05Z | full CDX listing for `cmegroup.com/services/trading-hours-by-product*` — 690 captures, 2022-08-23 … 2026-08-31 |

### What the two CDX sweeps establish (negative results, recorded so they are not re-run)

- **The ContractSpecs channel has no archived history for this gate.** Prefix search returns zero
  captures for productIds 7968 (EST), 7969 (NQT), 8027 (IPT), 7948 (RSV), 7949 (RVT) and 8026 (IPO).
  The disputed "Default:" cells therefore cannot be dated — they can only be observed live. The one
  exception is productId 166 (E-mini S&P MidCap 400), captured once, on 2021-07-10.
- **The session-event channel has no archived history for this gate either.** Of 690 archived
  captures of `/services/trading-hours-by-product`, every id-scoped one carries the CME homepage
  widget's fixed list `316,133,425,300,58,437,22,8478,5201,10191`; the only other id values archived
  anywhere are the singletons `316`, `5224` and `318`. **No BTIC productId appears in a single
  archived capture.** The `closed@15:00` events are a live observation with no datable history.
- Consequence for the adjudication: neither modern channel can be ordered in time against the other.
  The ordering that decides the gate comes instead from the *server-rendered* spec pages
  (2015-11-15 … 2019-01-30, all retrieved above) and from the two CFTC certifications, which are
  dated documents in their own right.

### The 2021-07-10 capture, verbatim (from the decompressed bytes)

```
"TradingHours":{"vandhr":[
 {"hours":"Sunday 6:00 p.m. - Friday 6:45 p.m. ET (Sun 5:00 - Fri 5:45 p.m. CT) with no reporting
   Monday - Thursday&nbsp;6:45 p.m. &ndash; 7:00 p.m. ET (5:45 p.m. &ndash; 6:00 p.m. CT)",
  "venue":"CME ClearPort:"},
 {"hours":"Sunday 6:00 p.m. - Friday - 5:00 p.m. ET (5:00 p.m. - 4:00 p.m. CT) with a daily
   maintenance period from&nbsp;5:00 p.m. &ndash; 6:00 p.m. ET (4:00 p.m. &ndash; 5:00 p.m. CT)<br />
   <br />\nBTIC: Sunday - Friday 6:00 p.m. - 4:00 p.m. ET","venue":"CME Globex:"}]}
ProductCode: {"ClearPort":"ME","BTIC":"EMT","ClearingCode":"ME","CmeGlobex":"EMD"}
```

Two things it settles. (a) The modern ContractSpecs channel already printed the venue-labelled
`CME Globex: … BTIC: … 4:00 p.m. ET` line in July 2021, so the 16:00 ET reading is not a recent
edit. (b) It is dated twelve days after the 2021-06-28 halt removal and its **outright** Globex line
carries no `4:15 p.m. – 4:30 p.m.` halt clause, where the 2019-01-30 server-rendered ES page still
did — the channel tracked that change, which is evidence the cell is maintained rather than frozen.

### Channels tried and closed in this pass

- `https://www.cftc.gov/search?search_api_fulltext=…` returns HTTP 200 but renders the homepage;
  `/search/node?keys=…` is 404 and `/search?keys=…` is 403. CFTC full-text search is not reachable
  from this machine, so the IPT and RVT *listing* certifications were not located. They are not a
  blocker — under `AGENTS.md` ("Adding or revising a product-family key", item 2) a member product
  listing after the family clock began is caller catalog data — but the route is recorded as closed.
