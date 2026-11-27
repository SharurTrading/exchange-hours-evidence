# INDEX — cme-forward-2026-11-03 (CME Globex 2028 first windows)

T2 `trading-hours-by-product` service captures retrieved by the ZCode sweep
2026-11-03 (browser relay; cmegroup.com refuses direct curl from this
machine). A-set ids `316,133,425,300,58,437,22,8478,5201,10191`; B-set ids
`168,167,320,323,19,27`. File names carry the document id (window start);
ranges are in each evidence file's Documents row.

| File | Window (eventDates) | sha256 |
|---|---|---|
| `service/CME-SVC-2027-12-26.json` | 2027-12-26..2027-12-30 | see crate Documents rows |
| `service/CME-SVC-2028-01-15.json` | 2028-01-15..2028-01-19 | `f74454cec296f0dd7055091093e7d02fa993bb27963be968dc84082249074d96` |
| `service/CME-SVC-2028-02-18.json` | 2028-02-18..2028-02-23 | `bdd7dd926a84cebd48c702af978b6836b998723f1af86818cc93fc50da557b28` |
| `service/CME-SVC-2028-04-12.json` | 2028-04-12..2028-04-18 | `71a6b95a487deee4fd2ad9fe10853ef2e95230fcd7ffa96e6708b54054939ec3` |
| `service/CME-SVC-2028-05-01.json` | 2028-05-01..2028-05-08 | horizon control only; no rows encoded |
| `service/CME-SVC-B-*.json` | same windows, B set | see crate Documents rows |

Encoded: 2028 MLK (2028-01-17), Presidents' Day (2028-02-21) and Good Friday
(2028-04-14) rows in the eight Globex family tables, inside split coverage
windows. No contiguous Jan–May 2028 audited-normal claim: spans between the
captured windows are unaudited. The Dec 2027 window closes the grains
2027-12-26..29 evidence gap with no row change.
