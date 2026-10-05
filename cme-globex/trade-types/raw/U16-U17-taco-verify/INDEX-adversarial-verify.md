# U16-U17-taco — ADVERSARIAL VERIFIER capture index

Verification run 2026-09-11T23:17Z – 23:27Z (UTC). Capture timestamps date the
observation only; artifact dates are separate and given per row.
Files dated 2026-09-06 17:27/17:28 in this directory pre-date this run and are
not mine.

| File | URL | Artifact date | capture_ts (UTC) | sha256 | bytes |
|---|---|---|---|---|---|
| cs-133-verify.txt | r.jina.ai → https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/133 | live, undated by CME | 2026-09-11T23:17:49Z | 556324d02d0087e6e1c8b9cbfe528deebb2164e67abb6e0a1858873c4708f252 | 4504 |
| cs-146-verify.txt | same, productId/146 | live, undated | 2026-09-11T23:18:35Z | 10c5a7ae591bcb20c701fbcf0d3a0bfe63ffde2eacff37173e0d236dba9943dc | 4203 |
| cs-8314-verify.txt | same, productId/8314 | live, undated | 2026-09-11T23:18:36Z | 90b2b39b749ba6069d3aaa46a7b9526bfed1ff6d0a5cc66f8affd2f613b1b754 | 4281 |
| cs-8528.txt | same, productId/8528 (ESQ) | live, undated | 2026-09-11T23:26Z | 38f4136254005f95447df94f356f6c9c72154bae9eb9a8b4b0826ce2be91ef63 | 831 |
| cdx133-verify.json | web.archive.org CDX, ContractSpecs/List/productId/133* | 23 captures 2021-07-03→2026-04-05 | 2026-09-11T23:19Z | 0c09177137a103b4af5057cc575116605c5a83d955c2113016ec47aeef0ca4d4 | 3899 |
| wb-20210703123524.json | web.archive.org id_ replay of ContractSpecs 133 | wayback ts 2021-07-03 | 2026-09-11T23:19Z | ff1ac332c4b78d66320ca43b799ef0c06d06c2c62da30bed1b86548183f9f984 | 3206 |
| wb-20220908122619.json | same | wayback ts 2022-09-08 | 2026-09-11T23:19Z | 4fa6538b307b89bf04b5fd9c958556bf53d8c0110c9bea3bbf0315a7b314abbc | 3211 |
| epic-verify.txt | CDX prefix sweep cmegroup.com/confluence/display/EPICSANDBOX* (fl=original, collapse=urlkey) | 2333 rows | 2026-09-11T23:21Z | d9bb335bda99676819d739de3fa13927d6c29eb25b61f6b8a6e5d8c4ffff2a97 | 226265 |
| conf-457092968-verify.json | https://cmegroupclientsite.atlassian.net/wiki/rest/api/content/457092968?expand=body.view,version,history.lastUpdated | migrated page v2, 2025-01-13T19:46:14.571Z | 2026-09-11T23:21Z | b690cd5cf7ce4c76422374cbdf74ae170c74ea38b575cf07cc317b9c8149f2fd | 8685 |
| conf-457418067.json | same API, page 457418067 "E-Mini Standard and Poors 500 Futures" | v4, 2026-08-20T17:21:45Z | 2026-09-11T23:26Z | da0910ac85c8542b539b76dd8c9df733befcd26ab25640e4cd7cf52cf9a4098b | 16413 |
| cql-friday.json / cql-sat.json / cql-taco.json | Confluence CQL title~"Friday Trading Schedule" / text~"TACO" and text~"Saturday" / text~"TACO" | live | 2026-09-11T23:26Z | 0292ba2c… / 0523cb63… / a4d76753… | 247 / 829 / 6658 |
| **tacopage-20260213.html** | https://web.archive.org/web/20260213214836id_/https://www.cmegroup.com/trading/equity-index/trade-at-cash-open.html | wayback ts **2026-02-13** | 2026-09-11T23:24Z | e6bf2315c562493ec3b2d14fffbd114b5362a1d5158a005aca3b65e34d7b0109 | 207685 |
| **chadv21-234-verify.txt** | r.jina.ai → https://www.cmegroup.com/notices/clearing/2021/06/Chadv21-234.pdf | **CME Clearing Advisory 21-234, DATE July 1, 2021; Effective Date 27 September 2021** | 2026-09-11T23:26:01Z | 59ecd6e4d66ff938aa884afaceb1bbcf93e3c24e239a28a9f496a36ea6ec64ea | 2236 |
| chadv21-223.txt | r.jina.ai → .../notices/clearing/2021/06/Chadv21-223.pdf | Clearing Advisory 21-223, DATE June 28, 2021 (listing cycle only, no hours) | 2026-09-11T23:26Z | 49c737e1037812fb575a8fe959e516929afb564ebc63f9b6669004187e340f13 | 1576 |
| svc-hist.txt | r.jina.ai → /services/trading-hours-by-product?id=8528&…fromEventDate=2021-10-01&toEventDate=2021-12-31 | live feed, hasEvents:false | 2026-09-11T23:26Z | 73e3fdbdb8b97c0cc6e7ec1cdbeaa90cfeb0e0afc57ad9a7b703315c606b0032 | 5680 |

`chadv21-234-verify.txt` differs from the researcher's own
`../U16-U17-taco/Chadv21-234-pdf.txt` only in the text reader's
`Published Time:` header line; the document body is byte-identical.

Direct (non-reader) GETs to www.cmegroup.com returned http=000 from this
machine, consistent with the gate's note.
