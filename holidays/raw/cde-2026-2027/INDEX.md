# Evidence index — task `cde-2026-2027`

Coinbase Derivatives (CDE) published-future refresh. Retrieval session **2026-09-26 07:14–07:21 UTC**.
All retrieval times are UTC (`date -u`), per LAW-UTC-DATES. Supersedes nothing: the earlier capture set
lives in `../cde-2021-2025/` (2026-09-19) and is untouched by this directory.

Purpose: the crate's `coinbase_derivatives` identity covers `2021-06-28..2026-09-07`. Its stored notice
index stops at **26-36** (the 2026-09-07 Labor Day notice). This directory adds the notices the store
explicitly recorded as *not retrieved* (26-25, 26-33, 26-33.1, 26-33.2) and a fresh capture of the
operator's notices listing, and records what is still absent.

Direct `www.coinbase.com` requests return 403 (Cloudflare) from this host; the store's recorded workaround
(reader with HTML response mode) could not be used this session — see **Access** below.

---

## Documents

| Document | URL | Retrieved (UTC) | sha256 | Bytes | What it is |
|---|---|---|---|---|---|
| `pdf/CDE_Market_Notice_26-25_Removal_of_Weekly_1-Hour_Friday_Maintenance_Window.pdf` | https://assets.ctfassets.net/k3n74unfin40/ck3V0pTQinM2mDaj0V2vm/9d0ce9bcf938c0d298fd0fa5cd23bcab/CDE_Market_Notice_26-25_Removal_of_Weekly_1-Hour_Friday_Maintenance_Window.pdf | 2026-09-26 07:18:28 | `5f71cb0add14003d45bbea8824960c9ae27f80626bf2144775c55a803dbceb2e` | 96,133 | **T1.** 26-25, Removal of Weekly 1-Hour Friday Maintenance Window, dated 05/20/2026. |
| `pdf/CDE_Market_Notice_26-33_24x7_Transition__Rolling_Gateway_Deploys_and_Final_Friday_Maintenance_Windows.pdf` | https://assets.ctfassets.net/k3n74unfin40/2SQkz152vmsnsSRoKTA4Ij/df5806d1dcfedbc8e6910d1f6c1a3581/CDE_Market_Notice_26-33_24x7_Transition__Rolling_Gateway_Deploys_and_Final_Friday_Maintenance_Windows.pdf | 2026-09-26 07:18:30 | `b105299592c8a9d570c42dd36ff391b510da18919fbaf3c275d2905d3c89c4a7` | 217,412 | **T1.** 26-33, 24x7 Transition, dated 07/13/2026. Supersedes 26-13, revises 26-25. |
| `pdf/CDE_Market_Notice_26-33.1_Updated_Dates_on_24x7_Transition__Rolling_Gateway_Deploys_and_Final_Friday_Maintenance_Windows.pdf` | https://assets.ctfassets.net/k3n74unfin40/6FyHssn288V4WK5thCVJgP/3ea97c2589858dd8e11d5ab28cec5bc3/CDE_Market_Notice_26-33.1_Updated_Dates_on_24x7_Transition__Rolling_Gateway_Deploys_and_Final_Friday_Maintenance_Windows.pdf | 2026-09-26 07:18:32 | `39b891e391edf14c470fba8f49008b8a548241f1299ef5719171332e3384f5fa` | 224,576 | **T1.** 26-33.1, dated 08/05/2026. Moves the final window to "October 2026 (date to be announced)". |
| `pdf/CDE_Market_Notice_26-33.2_Updated_Dates_on_24x7_Transition_-_Rolling_Gateway_Deploys_and_Final_Friday_Maintenance_Windows.pdf` | https://assets.ctfassets.net/k3n74unfin40/7e6O4DoAtbFNnhaShiFs7q/201c834c6d3d66ea494596d8876ae1a3/CDE_Market_Notice_26-33.2_Updated_Dates_on_24x7_Transition_-_Rolling_Gateway_Deploys_and_Final_Friday_Maintenance_Windows.pdf | 2026-09-26 07:18:33 | `887c5daa3f61c6b653e0d85bf66fbe32603ec187d15ec32c250f004fafc48512` | 198,203 | **T1.** 26-33.2, dated 09/10/2026. Current rolling-deploy schedule; GoLive still undated. |
| `txt/*.txt` (4 files) | — (derived) | 2026-09-26 07:19 | see below | — | `pdftotext -layout` dumps of the four PDFs; the source of every verbatim in `cde-late-2026-notices.md`. |
| `cde_market_notices_20260926.md` | https://r.jina.ai/https://www.coinbase.com/derivatives/market-notices | 2026-09-26 ~07:15 (bracketed 07:14:40–07:16:39) | *(authored file; not a byte copy)* | 4,161 | **T1 listing.** Reader-rendered markdown of the notices listing: every row published on/after 2026-08-25 transcribed, newest first. See the caveat in that file. |
| `cdp_derivatives_market_hours_20260926.html` | https://docs.cdp.coinbase.com/derivatives/introduction/market-hours | 2026-09-26 07:16:40 | `327928ff63bf4abb51990ca94b25647e3fa221e4fd12a8accfbb941f84f13829` | 1,040,125 | **T1.** The operator's baseline market-hours page, byte-exact (re-fetched at 07:21:29, identical sha256). |
| `cdp_derivatives_market_hours_20260926.txt` | — (derived) | 2026-09-26 07:21:02 | `6507e87f50c2b3f34a1959f09767df907f85f95a97dab0c45483d1a92e96a3b1` | 12,383 | Tag-stripped text of the page, used for the sentence-level comparison against the 2026-09-12 capture. |
| `refused_r-jina-ai-cloudflare-403_20260926.html` | https://r.jina.ai/https://www.coinbase.com/derivatives/market-notices (with `x-respond-with: html`) | 2026-09-26 07:14:40 | `4f68008d91677fdb711bb610bb2117cceb555785df4fcc8ce70236f36fca7c55` | 5,851 | **Refusal evidence.** Cloudflare "Just a moment..." interstitial returned by the reader to `curl`. Kept so the block is auditable. |
| `cde_status_page_20260926.html` | https://status.cde.coinbase.com/ | 2026-09-26 07:23:32 | `a536a8fd7f2254a1f6cea0b35a06dd120384e70054f3d0701523b57649679802` | 109,449 | **T2 (supplementary).** The operator's own status feed. Past-incident list proves the weekly Friday maintenance window still ran on **2026-09-25** ("Friday Maintenance Window 260925", in progress 21:05 UTC, completed 22:00 UTC) and quotes its own duration as "1-hour … 17:00 to 18:00 ET". Locates notice 26-33.2's PDF. Fetchable directly; no block. |
| `cde_status_page_20260926.txt` | — (derived) | 2026-09-26 | `fa2885b40782e2bd905168e44b1ff006d9bb369c70efc69928db2232b5c4d34a` | 1,869 | Text of the past-incident list. |
| `cde-late-2026-notices.md` | — (authored) | 2026-09-26 | `9c8cff5cc117672ed6779ae0cae41ac2525d21c837973d43098a702388c67670` | 13,848 | Verbatim operative lines for 26-25 / 26-33 / 26-33.1 / 26-33.2, the listed-only 26-33.3 and 26-37, the holiday-notice status, and the status-feed corroboration. |
| `INDEX.md` | — (this file) | 2026-09-26 | — | — | Register and access log. |

`txt/` dump hashes (sha256): 26-25 `5f45d9bb2e81a436ba1c758ac6ddb006c812e6549cdaf56bb628a0ab9f32168e`;
26-33 `302bf25367f9305a67e6224a875bfd14df5d03d7dfc714a5be733f1d07d75434`;
26-33.1 `739412a471be7d88bf44dfc8449a515babb4902de36e829946169aedaa3e6214`;
26-33.2 `f922a5454989d87f0d04e444cd21a9faf67e134436c75c1b584a05915767a369`.

**Where the four PDF URLs came from.** Not from this session's listing capture (which renders text only),
but from the store's own 2026-09-19 capture, `../cde-2021-2025/cde_notices_index.json`, whose `uris` field
records them. The addresses were re-resolved live: all four returned HTTP 200 on 2026-09-26.

---

## Enumeration — every notice above / issued after 26-36

| ID | Type | Published | Effective | Title | Category | PDF |
|---|---|---|---|---|---|---|
| 26-33.3 | Market | 2026-09-24 | 2026-09-25 | Amendment to 26-33.2 and 26-25: Rolling Gateway Deploys Postponed and Upcoming Maintenance Windows | Maintenance | **not retrieved** |
| 26-37 | Market | 2026-09-24 | 2026-10-24 | CDE Q4 Quarterly Maintenance Window & FIA DR Testing - Details | Maintenance | **not retrieved** |

26-37 is the only notice numbered above 26-36. 26-33.3 carries a lower number but was issued after 26-36
and amends it in effect. Twelve regulatory (R2026-50…R2026-64) notices also postdate the 2026-09-19
capture; none is a holiday or session-hours notice, and they are enumerated in
`cde_market_notices_20260926.md`.

## Holiday notices after 26-36

None. The newest Holiday-category row on the operator's listing is **26-36 (2026 Labor Day, effective
2026-09-07)**, published 2026-08-25. No Thanksgiving 2026, Christmas 2026 or 2027 holiday notice exists
as of 2026-09-26.

---

## Access

Every channel tried for `https://www.coinbase.com/derivatives/market-notices` and its PDF addresses:

| # | Channel | Outcome |
|---|---|---|
| 1 | `curl` → `https://www.coinbase.com/derivatives/market-notices` | **403** (Cloudflare interstitial). Matches the store's recorded experience; not retried. |
| 2 | harness fetch tool → same URL | **403** (same interstitial). |
| 3 | `curl` → `https://r.jina.ai/<url>` with `x-respond-with: html` — the store's recorded method | **403**, Cloudflare on the reader itself (saved as `refused_r-jina-ai-cloudflare-403_20260926.html`). Not retried with altered headers. |
| 4 | harness fetch tool → `https://r.jina.ai/<url>` (reader default mode) | **200.** Full listing text retrieved; the reader drops `href`s inside the notices table (verified — the same reader preserves links on ordinary pages), so no `assets.ctfassets.net` address could be recovered. |
| 5 | Wayback CDX for the listing page | **141 captures**, first 2022-06-18 (404), last **2025-09-28**; **none in 2026**. (The store's `../cde-2021-2025/INDEX.md` records "133 captures … through 2026-09-28"; the fresh query shows the last capture is 2025-09-28, so that line overstates the archive's reach.) |
| 6 | Wayback Save Page Now (`/save`, GET and POST SPN2) | **"Job failed"** (HTTP 520). The Internet Archive was also briefly "Temporarily Offline" mid-session. No capture created. |
| 7 | Common Crawl index, `CC-MAIN-2026-39 / -34 / -30` | "No Captures found". |
| 8 | archive.today `newest/` lookup | **404** — no capture. |
| 9 | Wayback CDX for `assets.ctfassets.net/k3n74unfin40*` from 2026-04-01 | 29 artifacts, none a notice PDF newer than 26-13. |
| 10 | `docs.cdp.coinbase.com` baseline | **200**, directly fetchable — saved above. |
| 11 | `curl` → `https://status.cde.coinbase.com/` | **200**, directly fetchable — saved above; links 26-33.2's PDF, does not link 26-33.3 or 26-37. |
| 12 | Web search for the `26-33.3` / `26-37` titles and for `assets.ctfassets.net` `Market_Notice_26-*` filenames | No indexed copy of either PDF surfaced (see the report's search log). |

No proxy, credential or header-rotation workaround was attempted; with `#1`–`#3` refused, the reader's
text mode (`#4`) and the sanctioned archives (`#5`–`#8`) were used instead.

## Still missing, and what closes it

| Gap | Closing condition |
|---|---|
| PDFs of **26-33.3** and **26-37** | One capture of the listing page that preserves its `href`s — an `x-respond-with: html` read of `https://www.coinbase.com/derivatives/market-notices` from a host the reader does not challenge, or a Wayback capture of that page after 2026-09-24. Then fetch the `assets.ctfassets.net/.../CDE_Market_Notice_26-33.3_*.pdf` and `.../CDE_Market_Notice_26-37_*.pdf` addresses it carries. |
| Thanksgiving 2026 / Christmas 2026 / 2027 CDE holiday notices | Not yet published by the operator (2025 pattern: Thanksgiving notice 10/30, Christmas notice 11/25). Re-check the same listing monthly per LAW-WATCH. |
| Date for the removal of the weekly Friday maintenance window | Currently "October 2026 (date to be announced)" in 26-33.1 / 26-33.2; no encodable date until the operator names one. |
