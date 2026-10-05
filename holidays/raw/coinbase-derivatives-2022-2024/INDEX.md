# Evidence index — bounded retrieval attempt for issue #112 (`coinbase-derivatives-2022-2024`)

One bounded attempt (LAW-BOUNDED-WORK), 2026-09-27 11:25–11:33 UTC, at the two defective
Coinbase Derivatives (FairX) holiday-notice sources recorded in
`docs/evidence/coinbase_derivatives.md` under "Gaps and residual risks, 2021-2026" and tracked
as SharurTrading/exchange-hours-rs#112. All times UTC (`date -u`), per LAW-UTC-DATES.
Prior negative evidence in `../cde-2021-2025/` (session 2026-09-19 02:02–02:45 UTC) is reused
and cited, not re-fetched except where noted.

## Verdicts

- **Notice 22-10 (2022 Thanksgiving): still open — proven unreachable through every channel
  tried this session.** No new copy recovered; trade dates 2022-11-24 and 2022-11-25 stay
  `Unsourced`.
- **Notice 24-12 (2024 Juneteenth): still open — the IN DRAFT copy is the only copy the
  operator has ever served.** Its bytes are identical across the 2024-12-25 Wayback capture,
  the 2025-06-20 Wayback capture, the 2026-09-19 live retrieval and today's live retrieval.
  The live listing shows no final revision and no later notice republishing the 2024
  Juneteenth schedule.

## Retrievals

| Artifact | URL | Retrieved (UTC) | sha256 | What it is |
|---|---|---|---|---|
| `pdf/24-12.live-20260927.pdf` | https://assets.ctfassets.net/k3n74unfin40/3qWRHv5qyUppIBwZXGdAAs/108f4e2cb2379887811a5a9dbdbb59ab/Market_Notice_24-12__Juneteenth.pdf | 2026-09-27 11:32 | `fe2a89a8a4aae9372f0d4fd410a62f345d43bfb630abfe931c51b6c858674b20` | **T1.** Live 24-12 asset, 77,019 bytes, headed "Market Notice \| IN DRAFT". Byte-identical to the 2026-09-19 live copy in `../cde-2021-2025/pdf/24-12.pdf`. |
| `pdf/24-12.wayback-20250620163024.pdf` | https://web.archive.org/web/20250620163024id_/https://assets.ctfassets.net/k3n74unfin40/3qWRHv5qyUppIBwZXGdAAs/108f4e2cb2379887811a5a9dbdbb59ab/Market_Notice_24-12__Juneteenth.pdf | 2026-09-27 11:26 | `fe2a89a8a4aae9372f0d4fd410a62f345d43bfb630abfe931c51b6c858674b20` | **T1 through a verbatim public mirror.** Wayback's 2025-06-20 capture, served gzip-wrapped, gunzipped to the same 77,019 bytes as live: same digest. |
| `listing_capture_20221222045732.html` | https://web.archive.org/web/20221222045732id_/https://www.coinbase.com/derivatives/market-notices | 2026-09-27 11:30 | `cdf1d4fd1914ef03cbe9d58f1114abe3083dca629f0967bd71a2464e4a8c12ab` | **T1 through a verbatim public mirror.** Listing capture one week after 22-10's posting: 22-10's "Read More" href is already the dead `info.fairx.com` URL in both the rendered anchor and the embedded Contentful JSON. |
| `listing_capture_20230214212136.html` | https://web.archive.org/web/20230214212136id_/https://www.coinbase.com/derivatives/market-notices | 2026-09-27 11:30 | `8da72603ccd46c19405ed270aa6fa9a4af07748ac07de2bb235e7fe21f2be005` | Same, two months later: identical dead href. The operator's listing never carried a CDN link for 22-10. |
| `listing_live_20260927.html` | https://r.jina.ai/https://www.coinbase.com/derivatives/market-notices | 2026-09-27 11:31 | `358b42dd07998bb2ac04054ea5032da668db56df0524b1adba735dab78fb8f2d` | **T1** (read through the public reader, as in `../cde-2021-2025/`; direct coinbase.com 403s from this machine). The 2026-09-27 listing: 24-12's only document is still asset `3qWRHv5qyUppIBwZXGdAAs/108f4e2c…`; no final 24-12 and no 25-xx republishing the 2024 Juneteenth schedule (25-20 is the separate 2025 schedule; "R2024-12" and "Supplemental 2024-12" are unrelated regulatory/crude-oil documents). |
| `archive_today_22-10.html` | https://archive.ph/newest/https://info.fairx.com/coinbase-derivatives-market-notice-22-10-thanksgiving-holiday-schedule-2022 | 2026-09-27 11:27 | `a59b66d8475a9f523529fb5d65e6435befe68923bbcdee7c0980fcd1dbfe7ab8` | archive.today answer page: "No results" for the exact 22-10 URL. |
| `cdx_info_fairx_notice_prefix.json` | https://web.archive.org/cdx/search/cdx?url=info.fairx.com/coinbase-derivatives-market-notice*&output=json | 2026-09-27 11:26 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | Empty `[]` — no capture under the listing's slug pattern. |
| `cdx_info_fairx_domain.json` | https://web.archive.org/cdx/search/cdx?url=info.fairx.com&matchType=domain&output=json&limit=2000 | 2026-09-27 11:27 | `65b0246325c818fb9c4cdf02c02ca86f9d158e9f1c3b9df95ba3127be9da0142` | The whole info.fairx.com domain holds two rows: a payload-less 2023 revisit of `/` and one 2022-05-21 capture of the 22-01 page. |
| `cdx_info_fairx_notice_prefix2.json` | https://web.archive.org/cdx/search/cdx?url=info.fairx.com/fairx-market-notice*&output=json | 2026-09-27 11:27 | `8ee5a7c88ccc1e6be59b23c886eb89f2b750264c6c82a47879d54757dfb29f2f` | Only the 22-01 page (`fairx-market-notice-22-01-mlk-holiday-schedule`); no 22-10 under the alternate slug pattern. |
| `cdx_fairx_22-10_filter.json` | https://web.archive.org/cdx/search/cdx?url=fairx.com&matchType=domain&filter=original:.*22-10.*&output=json&limit=500 | 2026-09-27 11:29 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | Empty `[]` — no URL containing "22-10" anywhere under the fairx.com domain (www., info., and all subdomains). |
| `cdx_fairx_nov22_feb23.json` | https://web.archive.org/cdx/search/cdx?url=fairx.com&matchType=domain&from=20221101&to=20230228&output=json&fl=timestamp,original,statuscode&limit=300 | 2026-09-27 11:29 | `cab921594173a86914490fbc2cb0a4723b317a7bf32a9c6718184198f4e0be1b` | 13 captures in the window; every www.fairx.com page captured 2022-12-24 is a 301 — the old WordPress site was already redirects-only when 22-10 posted, so no fairx.com-hosted copy of the notice page ever existed to capture. |
| `info_fairx_http_409.txt` | http://info.fairx.com/coinbase-derivatives-market-notice-22-10-thanksgiving-holiday-schedule-2022 | 2026-09-27 11:26 | (16-byte Cloudflare error body, quoted inside the file) | Plain-HTTP probe: Cloudflare edge answers `409 Conflict`, body `error code: 1001` (DNS resolves, origin refused). HTTPS probes the same minute: `curl (35) sslv3 alert handshake failure` (default) and `tlsv1 alert protocol version` (forced TLS 1.2) — same as the recorded 2026-09-19 failure. |

## Per-channel outcomes (two refusals end a channel)

1. **(a) `info.fairx.com` direct — refused.** HTTPS listing href: handshake failure (11:26:38);
   HTTPS host root with forced TLS 1.2 + HTTP/1.1 + browser UA: protocol-version alert
   (11:26:38); plain HTTP: 409 `error code: 1001` (11:26:38). Channel ended.
   The `assets.ctfassets.net` URL pattern is not inferable for 22-10: each sibling URL embeds a
   random Contentful entry id and content hash (e.g. 22-11's
   `1bcPFyFDQbRNqR6RhKwdX3/744286f7…`), and the full CDX enumeration of the space
   (`../cde-2021-2025/cdx_ctfassets.json`, 818 artifacts incl. 144 Market_Notice PDFs 21-01..26-13)
   holds no 22-10 row under either `assets.` or `images.` — so there is nothing to guess from.
2. **(b) Wayback CDX alternate forms + aggregators — exhausted, negative.** Prefix queries over
   both `info.fairx.com` slug families: no 22-10 (only sibling 22-01). Domain-wide filter
   `.*22-10.*` over fairx.com: empty. Three listing captures (2022-12-15 prior session,
   2022-12-22 and 2023-02-14 this session): the 22-10 href is the same dead `info.fairx.com`
   URL in all three. archive.today: "No results". timetravel.mementoweb.org: DNS unresolved on
   both attempts (http and https), 11:27 — refused.
3. **(c) Search-engine caches — refused.** Google cache endpoint returns only the Google search
   shell (cache discontinued); `cc.bingj.com` does not resolve. Channel ended at two refusals.
   Web search (3 query shapes: exact subject, "22-10" + FairX, Coinbase Derivatives + holiday
   schedule) found no copy of the notice.
4. **(d) Verbatim public mirrors — none found.** The only Thanksgiving-2022 schedule pages the
   search surfaced are CME-member FCM pages (ampfutures.com) about CME products, not mirrors of
   a FairX/CDE notice. No site reprinting notice 22-10 was found.

## 24-12 finalisation check

The listing rows after 24-12 (24-13 Independence Day, 24-16 Labor Day, 24-21 Thanksgiving,
24-23 Christmas, 24-25 New Year's, 24-26 early-close incident, 24-27 Day of Mourning) contain
no revised Juneteenth notice, and the 2025-06-20 Wayback capture proves the asset was not
replaced in the year after posting. The IN DRAFT watermark has now been observed in the
operator's own served bytes at four instants spanning 2024-12-25 to 2026-09-27, all one
byte-string (`fe2a89a8…`). Closing condition unchanged: a non-draft copy, if the operator ever
issues one.
