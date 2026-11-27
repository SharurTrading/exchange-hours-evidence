# CME Globex direct captures for the November 3 horizon sweep

The public CME calendar's `trading-hours-by-product` service returned
HTTP 200 with JSON for all ten GETs in the original sweep. Chrome's
Network panel exported the response bodies. The payloads below retain
CME's original UTF-8 bytes after HTTP content decompression.

| Artifact | Retrieved UTC | Bytes | SHA-256 |
|---|---|---:|---|
| [`service/CME-SVC-2027-12-26.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2027-12-26&toEventDate=2027-12-30) | 2026-11-27T04:53:00.765Z | 17490 | `71c831516474d8c7e01bed54d6a2953ea4f95f6e0eeb438f9a6ee5dc0ac347e4` |
| [`service/CME-SVC-2028-01-15.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2028-01-15&toEventDate=2028-01-19) | 2026-11-27T05:01:11.695Z | 12892 | `08fbfea910fb210cc8b24c3da1e6a5d507f42f454be7774404a459843efb0ed1` |
| [`service/CME-SVC-2028-02-18.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2028-02-18&toEventDate=2028-02-23) | 2026-11-27T04:59:07.201Z | 15256 | `319ad5f7f606d928ac4750ab0eae7404e0a649f23875626f88bb0975cdc2bf98` |
| [`service/CME-SVC-2028-04-12.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2028-04-12&toEventDate=2028-04-18) | 2026-11-27T04:59:14.452Z | 18005 | `3447a4581e561780fc35336004f0fc7e37132205c80add47ebac3f31b6a2192c` |
| [`service/CME-SVC-2028-05-01.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2028-05-01&toEventDate=2028-05-08) | 2026-11-27T04:59:21.705Z | 20376 | `8939d6863ad0b5ebab87ae5ee8528feee8a835beda111bf555fedf0068cf9a96` |
| [`service/CME-SVC-B-2027-12-26.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2027-12-26&toEventDate=2027-12-30) | 2026-11-27T04:53:03.610Z | 13470 | `8f906ce7103af248d2cca1b0a57d1de66d87ab075e46472a68f88956f109d217` |
| [`service/CME-SVC-B-2028-01-15.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2028-01-15&toEventDate=2028-01-19) | 2026-11-27T04:59:05.087Z | 8949 | `51c27d2af8649b51aa369124fe1d85a6e4b3b6a0aa303495865c30376bb791cf` |
| [`service/CME-SVC-B-2028-02-18.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2028-02-18&toEventDate=2028-02-23) | 2026-11-27T04:59:12.365Z | 10939 | `0e05007d7a2c5fe87e83ebf879cf51278179775c8d7ea64f09b2f834102fea78` |
| [`service/CME-SVC-B-2028-04-12.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2028-04-12&toEventDate=2028-04-18) | 2026-11-27T04:59:19.606Z | 13387 | `feeb43bdfdf6b297f1c2a00dc214989ee6f4318a272556d02e1967a299bc7d06` |
| [`service/CME-SVC-B-2028-05-01.json`](https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2028-05-01&toEventDate=2028-05-08) | 2026-11-27T04:59:28.020Z | 15382 | `888222a6a1ae274c6c2f5c702a0908a9469feb35e2517d0a0173e221d8da3f34` |

The five B-set bodies match the earlier relay captures byte for byte.
For each A-set body, reordering only the products to the order in the
relay capture reproduces its bytes. Across all ten windows, the records
contain the same 80 product-window entries, 496 product-day records and
1,334 session events, including each event's trade date, time and type.
The [November 3 captures](../cme-forward-2026-11-03/INDEX.md) preserve the
original retrieval record.

Tracks [exchange-hours-rs #385](https://github.com/SharurTrading/exchange-hours-rs/issues/385).
