# INDEX — Coinbase Derivatives re-check, 2026-10-03 (UTC)

Third forward re-check wave (after the 2026-09-26 `cde-2026-2027/` round and the
2026-10-02 `cde/INDEX-recheck-2026-10-02.md`). Two outcomes, both new:

1. **The listing's hrefs are captured.** The reader's HTML mode — refused with
   Cloudflare 403 on 2026-09-26 (`../cde-2026-2027/refused_r-jina-ai-cloudflare-403_20260926.html`,
   Access row #3) — answered HTTP 200 on 2026-10-03, so the live listing page is held
   byte-exact including its embedded Contentful rich-text table, which carries an
   `assets.ctfassets.net` PDF address for **every** notice except 22-10 (see the #112
   section of `docs/evidence/coinbase_derivatives.md`). The page's own link table is
   extracted to `ctfassets_notice_urls_from_live_listing_20261003.txt` (437 addresses).
2. **The two listed-only notices are retrieved.** `CDE_Market_Notice_26-33.3` and
   `CDE_Market_Notice_26-37`, whose addresses the 2026-09-26 wave could not read out of
   the text-mode render, are saved below from the addresses this capture carries, with
   text extracts. Notice 22-11's PDF is saved from the same table (its address was
   already known to the archive; this is the operator's own serving copy).

## Documents

| File | URL | Retrieved (UTC) | sha256 |
|---|---|---|---|
| `cde_market_notices.reader-20261003T091031Z.md` | <https://www.coinbase.com/derivatives/market-notices> via the public reader (text mode) | 2026-10-03 09:10 | `0bdf9fb716ab1a5de14fae8be8125cd996b093862b39c5f21e5de7f2863c1ace` |
| `cde_market_notices.reader_html-20261003T091118Z.html` | same URL, reader HTML mode (`x-respond-with: html`) | 2026-10-03 09:11 | `41cac699afa5856413a951bc66a65167657971ca5218ee2b5f769142a6b313cc` |
| `ctfassets_notice_urls_from_live_listing_20261003.txt` | derived from the HTML capture | 2026-10-03 | *(derived; header carries the count)* |
| `pdf/CDE_Market_Notice_26-33.3_Rolling_Gateway_Deploys_Postponed_and_Upcoming_Maintenance_Windows.pdf` | <https://assets.ctfassets.net/k3n74unfin40/J6XHQuLLScfNJF7gwzCEC/60a4d7965f8eb030e198ddbb05b7f222/CDE_Market_Notice_26-33.3_Rolling_Gateway_Deploys_Postponed_and_Upcoming_Maintenance_Windows.pdf> | 2026-10-03 09:12 | `ac4f9f5da7d7174fa787834ad286575e3eeae5c7af1af08d0d34f46174763858` |
| `pdf/CDE_Market_Notice_26-37_Q4_2026_Quarterly_Maintenance_Window___FIA_DR_Testing.pdf` | <https://assets.ctfassets.net/k3n74unfin40/6cvYvCxcHFMAGEjOM1Cfoy/3830c45e49154425f5c14ffc1b24c0bb/CDE_Market_Notice_26-37_Q4_2026_Quarterly_Maintenance_Window___FIA_DR_Testing.pdf> | 2026-10-03 09:12 | `97f2d841c43239aba313f7a4c594381767ffb759ee0a2bcc869c1de80f869754` |
| `pdf/Market_Notice__22-11.pdf` | <https://assets.ctfassets.net/k3n74unfin40/1bcPFyFDQbRNqR6RhKwdX3/744286f7573b8b1b043a919670d70641/Market_Notice__22-11.pdf> | 2026-10-03 09:12 | `b4981e4fe3c6d388612716b1c72721ff5870825f867b67e75d8f3c9e036f8927` |
| `txt/*.txt` (3 files) | derived | 2026-10-03 | `pdftotext -layout` dumps |
| `../coinbase-derivatives-2022-2024/cdx_ctfassets_thanksgiving-20261003T092039Z.txt` | Wayback CDX, `assets.ctfassets.net/k3n74unfin40/*` filtered `.*[Tt]hanksgiving.*` | 2026-10-03 09:20 | `e1306da89924331363878f38758f1809bf984e759aff93ea47711295ace9d5d3` |
| `../coinbase-derivatives-2022-2024/cdx_ctfassets_22-10-20261003T092039Z.txt` | Wayback CDX, same space filtered `.*22-10.*` | 2026-10-03 09:20 | `30fce02c80b847a588286321860fff57ec835e4c011fab19d2c874dfd6ee5705` |
| `../coinbase-derivatives-2022-2024/cdx_trade_ledgerx_2022-2023-20261003T092400Z.txt` | Wayback CDX, `trade.ledgerx.com` domain, 2022-2023 | 2026-10-03 09:24 | `1dda07958d83c61df1d78082762cc80cddd6006c6c8a5083b6241de6b303a137` |

## What the two notices state

- **26-33.3** (dated 09/24/2026, amends 26-33.2 and 26-25): the weekly 1-hour Friday
  maintenance window `(16:00 to 17:00 CT) remains in effect`; the rolling Friday deploys
  are cancelled "through GoLive"; the TradingSessionID "will not change to TRUE_24X7
  until the transition is rescheduled" — the 24x7 transition is deferred **without a
  date**, so its closing condition becomes the operator's rescheduling notice. Q4
  quarterly maintenance: "Saturday, October 24, 2026 (aligned with FIA DR test). See
  Market Notice 26-37 for details."
- **26-37** (dated 09/24/2026): Saturday, October 24, 2026 — `24x7 Products Transition
  to CLOSE / Start of Maintenance` at 5:00 AM CT, `Transition into DR` 9:00 AM, back to
  production 12:00 PM, `24x7 Products Transition to PRE-OPEN` 1:50 PM, `24x7 Products
  Transition to OPEN / End of Maintenance` 2:00 PM CT. A 24x7-tier arrangement; that
  tier claims no key and adds no row in this crate, so neither notice changes the
  built-in table and the holiday horizon stays 2026-09-07.
- **22-11** (dated 12/12/2022): Christmas 2022 schedule only. It restates no
  Thanksgiving date, so it cannot close notice 22-10 by the restatement route; its rows
  (2022-12-26 `Closed`) already ship from the archived copy.

`SHA256SUMS.txt` beside this file lists every artifact's digest.

## 2026-10-05 (UTC) — the sibling full-text read closes the bridging route (#112)

Task angle for issue #112: read the retrieved siblings' full texts completely for bridging
language — a sentence carrying a default schedule 22-10 could composite against, or a
cross-reference witnessing 22-10's contents. Negative on both, corpus-wide:

- Full reads: 22-11, 26-33.3, 26-37 (this directory's `txt/`), and from `../../cde-2021-2025/txt/`
  the holiday family 21-06, 22-07, 22-08, 23-16, 24-21, 25-37 plus 26-27.1. A phrase scan over all
  56 stored text dumps (53 + these 3) for `except as`, `all other hours/dates`, `unchanged`,
  `standard schedule`, `supersed*`, `amend(s) notice`, `see also`, `previously issued/published`,
  `regular hours apply`, `default schedule` finds no other candidate sentence: the only
  cross-references in the whole corpus are 26-27.1's "Amendment: This notice supersedes Market
  Notice 26-27 …" and 26-33.3's "This notice amends Market Notice 26-33.2 and Market Notice
  26-25 (published 05/20/2026)." — the operator states amendment lineages explicitly, and 22-11
  carries no such sentence toward 22-10.
- The nearest things to bridging sentences point inside the same notice or at the separate 24x7
  listing: 23-16 "Please see below description of Coinbase Derivatives hours of operations and
  settlement information.", 24-21 "Please see the table below for the detailed Coinbase
  Derivatives hours of operation and settlement information around the holiday schedule.",
  25-37 "Additional details on 24x7 hours can be found here." Every holiday notice is a
  self-contained three-trade-date grid; none references a standard hours document.
- No other 2022-11-era item exists: the live listing's posted dates carry no row between 22-08
  (11/10/2022) and the 12/12/2022 trio 22-07/22-10/22-11.
- Template note (predictable, NOT evidence): the shared template makes 22-10's missing section
  predictable in form — three trade dates, "Closed for holiday" on Thursday 11/24, and in all four
  observed Thanksgiving years the same notice also states the Friday-after early close (21-06
  Equity 12:15 CT / Energy 12:45 CT; 23-16 Equity 12:15 CT / Crypto+Energy 12:45 CT; 24-21 all
  groups 13:45 CT; 25-37 Energy & Metal 13:45 CT / Equity 12:15 CT). The desk ask therefore
  requests the Friday 11/25 close cell too, not the Thursday closure alone.

Recorded in the repo's `docs/evidence/coinbase_derivatives.md` #112 bullet the same date.
