# Regulatory-channel sweep for #112 — CFTC filings, standing documents, NFA — 2026-10-05 UTC

One bounded attempt (LAW-BOUNDED-WORK), 2026-10-05 05:44–06:01 UTC, at the channels the
notice waves had not tried: the exchange's **regulatory filings and standing documents**.
Coinbase Derivatives Exchange LLC is LMX Labs, LLC d/b/a FairX then Coinbase Derivatives,
CFTC DCM record 43304. The task's four angles and what each produced. Verdict up front:
**no operator bytes stating 2022-11-24/25's hours exist on any regulatory or standing
channel; nothing admissible was found and nothing was encoded.** Trade dates 2022-11-24
and 2022-11-25 stay `Unsourced`; issue #112 stays open and its terminal state is the desk
ask. All times UTC (`date -u`), per LAW-UTC-DATES. Digests in `SHA256SUMS.txt`.

## 1. CFTC rule filings — NEGATIVE, and the channel is structurally incapable of the row

The commission's DCM rule-filings database (`cftc_trading_org_rules.html` is the form page;
POSTed queries saved as `cftc_rules_COIN_*.html`) was enumerated for the exchange's own
organization code **`COIN`** over receipt dates 2021-06-01..2023-03-31 (one broad window and
two disjoint narrow windows, `Show_All=1`). The organization code `CDE` in the same database
is **Cboe Digital Exchange** (formerly Eris), not Coinbase Derivatives —
`cftc_rules_CDE_202106_202303.html` is that disambiguation, kept so the code is not
re-confused.

Findings, in date order around the gap:

- **No COIN rule filing was received between 2022-09-02 and 2022-12-13.** The filings on
  either side: `Weekly Rule Notification - New Fee Schedule` received 09/02/2022 (record
  49310) and the Lead Market Maker / Broker Rebate renewals received 12/13/2022 (records
  49872, 49873). The commission's PDF namespace corroborates independently: of the 53
  `rule*lmxdcm*.pdf` files the Wayback CDX has captured under `cftc.gov/filings/orgrules/`
  (`cdx_cftc_orgrules_lmx.json`), none is dated between `rule090622lmxdcm*` (the 09/02
  filing) and `rule121422lmxdcm*` (the 12/13 filings). Market notices are not rule filings —
  the 40.6(d) weekly notifications enumerate only that week's rule amendments
  (`weekly_notification_2022-08-29.pdf`: "hereby submits this Weekly Notification of the
  following rule amendment issued during the week of August 29, 2022"), and no weekly
  notification exists for any week of the Thanksgiving window.
- **The rulebook edition in force at Thanksgiving 2022 defers holidays to the lost channel.**
  The last edition filed before the holiday is submission #2022-18E, received 08/25/2022
  (record 49084; `cftc_filing_49084.html`); its cover letter
  (`rule082522lmxdcm001.pdf`, saved as `weekly_notification_2022-08-22.pdf`, sha256
  `56f3d7b6e70cf385e130722db5d91959d2daec7c57c3aaec08bd9a6a66d547f9`) names only the Nano
  Ether addition and the Rule 1106 hard-fork provision as that edition's changes, and its
  clean rulebook copy `rule082522lmxdcm002.pdf` is
  saved as `rulebook_2022-08-25.pdf` (sha256 `06e0193913695a18ee45798590ab8188501b056291a
  fd30d55a3370a5d535d88`, text `rulebook_2022-08-25.txt`). Rule 503 reads: "Except as
  provided in Rule 212 with respect to Emergencies, the Exchange shall determine and publish
  a Notice to Participants listing the Business Days and Holidays of the Exchange and the
  Trading Hours for each Contract." Chapter 1's definition: "`Trading Hours` means, for any
  Business Day, the hours as may be published by the Exchange". A text search over the whole
  edition for `thanksgiving|holiday|hours of operation` finds only that deferral — no
  holiday exhibit, no per-product hours table, nothing dated.
- **The 2020 designation rulebook is the same.** DCM record 43304's Exhibit M-1
  (`cftc_orgdcmlmxexhibitm1ruleb200420.pdf`, `LMX-DCM000909`, text `lmx_rulebook_2020.txt`)
  carries the identical Rule 503 deferral. The record page itself
  (`cftc_dcm_43304.html`) lists only the five designation-era documents (AR agreement,
  Delaware good standing, the rulebook, Form DCM, the designation order) — nothing dated
  after designation.
- **The fee schedule in force at Thanksgiving carries no hours.** The edition filed with the
  09/02/2022 notification (`rule090622lmxdcm002.pdf`, "Fee Schedule as of August 23, 2022",
  `fee_schedule_2022-08-23.pdf` + `.txt`) lists per-side fees and the trader definitions
  only — the string `hour` does not occur. The last web-hosted edition before it
  (`media.fairx.com/wp-content/uploads/2022/03/30092305/Fee-Schedule-04_01_22-1.pdf`,
  Wayback 2022-05-28 id_ replay, `fee_schedule_web_2022-04-01.pdf`) likewise: zero `hour`
  strings.
- **The 12/13/2022 filings are program renewals.** `filing_121422_001.pdf` is submission
  #2022-20E (LMM renewal effective 2023-01-01) and `filing_121422_003.pdf` is #2022-21E
  (nano crypto broker-rebate renewal, same effective day). No holiday content; both
  postdate the event anyway.
- **Product certifications in the window state recurring hours only.** The products database
  (`cftc_products_COIN_2022-08_2023-03.html`) holds exactly one COIN certification in
  2022-08..2023-03: Nano Ether Futures, received 08/25/2022 — a contract listing, not a
  holiday arrangement.

## 2. Archived rulebook / operator standing pages — NEGATIVE

- Rulebook editions: 2020 designation exhibit, May/Sep/Oct 2021 fairx.com WordPress
  editions (already enumerated in `../cde-2021-2025/cdx_fairx.json`), and the Aug 2022 CFTC
  edition above. Every edition defers via Rule 503; none prints a holiday schedule. The
  successor-site pages (`coinbase.com/derivatives*`) were enumerated in the earlier wave's
  `cdx_cde_pages.json`; the `derivatives-exchange/market-notices` and `/filings` pages first
  answer 200 in 2023-05 captures, postdating the event and linking the same CFTC documents.
- `help.coinbase.com/derivatives*`: earliest Wayback capture **2024-09-14**, and every early
  row is a 307 redirect (`cdx_help_coinbase_derivatives.json`) — no 2022-era help-center
  carrier exists.
- `coinbasederivatives.com`: a 2021 parked domain (1,344-byte page, markmonitor tagline
  logo; `cdx_coinbasederivatives_domain.json`) — never an operator content site.
- `fairx.io`: a 2017-2020 static landing page, 404 since 2020 (`cdx_fairx_io_domain.json`).
- The DCM-archive page (`cftc_subdcmsarchives.html`) carries no Coinbase/LMX/FairX entry.

## 3. Fee-schedule / hours-of-operation pages — NEGATIVE

Covered under 1: the CFTC-filed fee schedule in force (as of 2022-08-23) and the web edition
(as of 2022-04-01) both carry fees only. The operator's hours-of-operation prose lived in
the market notices (lost) and, from 2025, in the CDP market-hours page (postdates the
event; already in evidence).

## 4. NFA BASIC — REFUSED twice, and incapable of the row in any case

`basic.nfa.org` does not resolve from this machine (DNS failure). The reachable
`www.nfa.futures.org/basicnet/` surface twice refused a real query: the landing form
(`nfa_basic_search_landing.html`) exposes no working target and both direct probes
(`nfa_probe1.html`, `nfa_probe2.html`) return the same session-gated 21 KB shell with no
result set. Two refusals end the channel per the sweep brief — and NFA BASIC is a
registration/disciplinary database; it carries no DCM holiday schedules, so a successful
query could not have keyed the dates either. The exchange itself is CFTC-designated, not
NFA-registered (the NFA registrations in the lineage are the FCM's, Coinbase Financial
Markets).

## Extra angle (not in the brief, closed while open): CDN document twins

Google indexes `.docx`-titled twins of some notices on `assets.ctfassets.net`
("Market Notice 22-08.docx", "Market Notice 22-09.docx") that the Wayback CDX has never
captured — proof the Contentful space holds more assets than the archive sees. Three
searches for a 22-10 twin (exact notice number + subject; CDN-domain-restricted; the
subject phrase alone) surfaced no 22-10 asset. DuckDuckGo's HTML endpoint answered a
challenge page (`ddg_22-10_subject.html`, HTTP 202, no results) and Bing ignored the exact
phrase (`bing_22-10.html`, generic Coinbase pages) — two refusals, channel closed. The
notices page's own JS bundle (read from the 2026-10-03 reader capture in
`../recheck-2026-10-03/`) embeds only placeholder Contentful tokens
(`BG19dk9-thisisdummytoken-...`) for unrelated spaces, so the space's asset list is not
enumerable through the delivery API.

## Verdict

Nothing admissible. The regulatory channel is now exhausted beside the notice, archive and
bridging channels: the rule filings database holds no filing from the window, the rulebook
in force at the date defers holidays to "a Notice to Participants" by its own Rule 503 (in
both the 2020 and 2022-08 editions), the fee schedules carry no hours, product
certifications state recurring hours only, and the standing pages either predate the event
or never existed. Closing condition unchanged: **any surviving copy of notice 22-10, or a
later operator document that restates the outgoing 2022 Thanksgiving schedule.** Until
then #112 stays open; the two trade dates ship `Unsourced`; the desk ask (a copy of the
notice, ideally carrying both the Thursday closure cell and the Friday 11/25 early-close
instants per product group) is the terminal state.
