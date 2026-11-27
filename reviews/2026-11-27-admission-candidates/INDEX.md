# Admission review for four futures candidates

The November 27, 2026 UTC review checked the authored futures root, venue
and calendar mappings in both consumers. The only matching family mapping
is for outright Nikkei `NKD`. There is no exact family mapping for the
other candidates or for the Nikkei TACO codes. This review covers authored
routes. Providers can discover other instrument definitions at runtime.

| Candidate | Operator evidence and current route |
|---|---|
| CME FSPI, channel 335 | [CME's product launch notice](https://www.cmegroup.com/notices/electronic-trading/2026/10/20261026.html) and the [archived product list](../../cme-forward-2026-11-03/notices/fspi_products.md) identify the scope. No mapped sports-index product root was found. |
| Nikkei TACO | [SER-9832RR](https://www.cmegroup.com/notices/ser/2026/10/ser-9832rr.html) names `NKQ` and `NIQ` as transactions on the existing Nikkei futures. The outright `NKD` family mapping applies to `NKD` itself. The two variant codes lack an authored mapping. |
| Bloomberg Commodity Index, channel 340 | [CME's October 5 notice](https://www.cmegroup.com/notices/electronic-trading/2026/10/20261005.html) identifies `AW`, the affected subindices and related transaction codes. No exact mapping was found for the products in the notice. |
| ICE Municipal AAA 10-Year Futures | ICE's specification identifies `M10` and its 18:00–16:00 ET trading window. Submission 26-159 gives December 7, 2026 as the expected listing date and reserves the exchange's ability to select a different date. No exact mapping was found for `M10`. |

| Artifact | Source | Retrieved UTC | SHA-256 |
|---|---|---|---|
| `ice-m10-spec.pdf` | <https://www.ice.com/api/productguide/spec/83050106/pdf> | 2026-11-27 05:53:20 | `89cc531fe0b2a0305abdbf66641e16c9e6d29d698a5c1f6a926432c831b330c1` |
| `ice-m10-certification-26-159.pdf` | [ICE filing mirrored by the CFTC](https://www.cftc.gov/filings/ptc/ptc11192656228.pdf) | 2026-11-27 05:53:20 | `9e4612139fa6c80ebd28e47e23fdfc4235d0c86387cdfe472e5a571d7e7d0ca0` |

Reassess an identity when an exact consumer route is added or the market is
named in the product plan. For a Nikkei TACO route, start with the existing
policy for transaction variants and assess an independent key only if the
consumer needs one. The evidence here supports a future admission review.

[Exchange-hours-rs #386](https://github.com/SharurTrading/exchange-hours-rs/issues/386)
tracks this review.
