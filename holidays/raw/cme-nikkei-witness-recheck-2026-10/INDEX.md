# INDEX — Nikkei witness re-check (`#162`), 2026-10-03 (UTC)

Targeted live re-check of the CME trading-hours service (T2) for the five 2025 merged
trade dates `globex_nikkei_225_dollar` ships no witness for: 2025-01-21, 2025-02-18,
2025-05-27, 2025-06-20, 2025-09-02. This round tries only what the 2026-09-12 repair
round's targeted `THBP-B` captures (`../cme-2025-2027-repair/`, windows exactly
Sunday..Tuesday over the id set `168,167,320,323,19,27`) did **not**: unfiltered
queries, the alternate product set, a single-product query, and wider windows running
from the Friday (or Wednesday, for Juneteenth) before each holiday through the day
after the merged date.

Channel: `https://www.cmegroup.com/services/trading-hours-by-product?...` read live
through the public reader `https://r.jina.ai/<url>` — the store's sanctioned path for
this endpoint since cmegroup.com refuses this machine directly (re-confirmed below).
Every `.md` file is the retrieved reader envelope (URL Source + `Markdown Content`
JSON body) and is what its sha256 hashes.

## Attempts

| # | Variant | Window(s) | Result |
|---|---|---|---|
| 0 | direct `curl` (browser UA) | 2025-01-19..2025-01-21 | **Refused** — HTTP 403, "This IP address is blocked due to suspected web scraping activity" (`direct_probe.html`). One attempt; not retried. |
| 1 | unfiltered (no `id=`), all products | 2025-01-17..2025-01-22 | **Rejected by the service itself** — HTTP 500 `{"message": "Error Query data from product slate. Check your parameters are correct."}` (`unfiltered_2025-01-17_2025-01-22.md`). The endpoint requires the `id` parameter; there is no all-products query shape. One attempt; not retried. |
| 2 | `[THBP-A]` set `id=316,133,425,300,58,437,22,8478,5201,10191` | 2025-01-17..2025-01-22 | All ten products enumerated over the six event dates with **zero events**, `hasEvents:false` (`thbpA_2025-01-17_2025-01-22.md`). The retention edge is not id-set-dependent. |
| 3 | single-product `id=168` (NKD alone) | 2025-01-17..2025-01-22 | The service knows the product (`"globex":"NKD","prodGroup":"NK","name":"Nikkei (USD) Futures"`) and enumerates every event date with `"events":[]`, `eventCount:0` (`nikkei_single168_2025-01-17_2025-01-22.md`). Not a product-resolution failure; the data is absent. |
| 4 | `[THBP-B]` set, wider windows | 2025-02-13..2025-02-19, 2025-05-23..2025-05-28, 2025-06-18..2025-06-21, 2025-08-29..2025-09-03 | Each returns all six products with zero events, `hasEvents:false` (`thbpB_2025-*.md`). The MLK date's wider window is attempt 3's neighbours plus `thbpA` above. |
| 5 | positive control, `[THBP-B]`, 2025-11-26..2025-11-29 | — | `hasEvents:true`, full schedules for all six products including `NKD` and `NIY` (`thbpB_positive_control_2025-11-26_2025-11-29.md`). The channel and service work today; the empties are retention, not an outage. |

## Conclusion

The service carries **no events for any product** in any window before Thanksgiving
2025, under every query shape available to it: the six-product set (2026-09-12 round),
the ten-product set, a single-product query, and wider Friday-to-Wednesday windows
(this round); the unfiltered shape does not exist (the service rejects it), and the
direct channel refuses this machine. The retention edge stands where the 2026-09-12
round placed it: between Labor Day 2025 and Thanksgiving 2025. No `NKD`/`NIY` witness
for 2025-01-21, 2025-02-18, 2025-05-27, 2025-06-20 or 2025-09-02 can come from this
channel, and #162 stays open on its desk-thread closing condition. The positive
control's bytes differ from the 2026-09-12 capture `D54` of the same window only in
the order of the `products` array; every event, count and instant is identical.

## Artifacts

| File | URL (via `https://r.jina.ai/`) | Retrieved (UTC) | sha256 |
|---|---|---|---|
| `live/direct_probe.html` | <https://www.cmegroup.com/services/trading-hours-by-product?pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-01-19&toEventDate=2025-01-21> (direct; refused) | 2026-10-03 09:16 | `eecde3fafbde4090c30e610a7ed4b8d877f8351c0490e4189574890e8a5a4f7e` |
| `live/unfiltered_2025-01-17_2025-01-22.md` | <https://www.cmegroup.com/services/trading-hours-by-product?pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-01-17&toEventDate=2025-01-22> (no `id`) | 2026-10-03 09:18 | `a3d2e7c6339eb27ea2b4529191f844b40adc4acec803c8bf7d717e7b7eee2acd` |
| `live/thbpA_2025-01-17_2025-01-22.md` | <https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-01-17&toEventDate=2025-01-22> | 2026-10-03 09:19 | `6edecaea11098cbc06be84bac3f70a2b25fcdc9de4c2f7866c91872ff625a49a` |
| `live/nikkei_single168_2025-01-17_2025-01-22.md` | <https://www.cmegroup.com/services/trading-hours-by-product?id=168&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-01-17&toEventDate=2025-01-22> | 2026-10-03 09:19 | `b2d0518a59473e29cb3b1be32738adff4424c3e28b1fbaf3283da8808e1e08d4` |
| `live/thbpB_2025-02-13_2025-02-19.md` | <https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-02-13&toEventDate=2025-02-19> | 2026-10-03 09:21 | `2956c3f4effde81acb570c27382ae2401a3caf12d48e45f938f1b8be637543c1` |
| `live/thbpB_2025-05-23_2025-05-28.md` | <https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-05-23&toEventDate=2025-05-28> | 2026-10-03 09:21 | `a62332bb287a109a560e313063d20fff5a996acabe36363b3539e3631b6f401e` |
| `live/thbpB_2025-06-18_2025-06-21.md` | <https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-06-18&toEventDate=2025-06-21> | 2026-10-03 09:21 | `1db4e3a0953846b0624e476b11eb6e8f1da1c8e438765099ffe57ea5fcae9ae2` |
| `live/thbpB_2025-08-29_2025-09-03.md` | <https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-08-29&toEventDate=2025-09-03> | 2026-10-03 09:21 | `e8293e1abc640eb5fdad89a19213ba5365dc1641755bc3dff1f534196e676e81` |
| `live/thbpB_positive_control_2025-11-26_2025-11-29.md` | <https://www.cmegroup.com/services/trading-hours-by-product?id=168,167,320,323,19,27&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-11-26&toEventDate=2025-11-29> | 2026-10-03 09:22 | `1961a417c16c7c8219a01d21805a0cad3ac7487bc035962c633d02ce75bcd61c` |

`SHA256SUMS.txt` beside this file lists the same digests. The `direct_probe.html`
digest above is recorded in this INDEX only (it is not a service answer; it is the
Cloudflare/IP-block refusal evidence).
