# APAC / broker-book / crypto / CFE forward watch — findings, 2026-10-13 UTC

Monitoring pass over six operators' live schedule channels, diffed against the
store's banked captures. Retrieval session 2026-10-13 23:27–23:39 UTC
(`date -u`). **Every diff is a clean negative: no operator published anything
new for late 2026 or 2027 since the store's previous captures.** Method note:
byte hashes of live pages differ trivially (dynamic tokens, regenerated
timestamps), so every comparison below is content-level — normalized text,
table rows, or header sets — between the fresh bytes saved in this directory
and the named banked capture.

## 1. HKEX (`hkex`, served, holiday window 2025-01-01..2027-12-31)

- **2027 table: already published and already banked.** The live
  `Trading-Calendar-and-Holiday-Schedule` page edition `Updated 31 Jul 2026`
  (`HKEX-TC-2026-2027`) prints 2026 and 2027 complete; the crate's window end
  2027-12-31 is the operator's own publication horizon.
- **Diff:** all 27 `<tr>` rows naming 2026/2027 content-identical to
  `equities/hkex/forward-2028/hkex_holiday_schedule.live-20261002T235917Z.html`;
  footer still `Updated 31 Jul 2026`; `2028` appears zero times (no 2028
  edition yet).
- **Errata:** none — no holiday-trading-arrangement change is visible in any
  channel pulled (the page's holiday table is the arrangement channel; it is
  unchanged since the banked 2026-09-28 digest `c460176b…`).

## 2. ASX (`asx`, served, holiday window 2010-01-01..2027-12-31)

- **2027 table: already published and already banked** (cash sheet on the live
  trading-calendar page; ASX 24 tables on `markets/market-resources/asx-24-trading-calendar`).
- **Cash-market sheet diff:** the fresh `Dates for 2026` / `Dates for 2027`
  sheets state exactly the shipped rows in
  `src/calendar/schedules/holidays/asx.rs` (2026: 1 Jan, 26 Jan, 3 Apr, 6 Apr,
  25 Apr, 8 Jun CLOSED; 24 Dec and 31 Dec CLOSE EARLY 14:10; 25 Dec, 28 Dec
  CLOSED; 2027: 1 Jan, 26 Jan, 26 Mar, 29 Mar, 14 Jun CLOSED; 24 Dec, 31 Dec
  CLOSE EARLY; 27 Dec, 28 Dec CLOSED; footnotes `[3]`/`[5]`/`[6]`/`[7]`
  unchanged). No new row, no changed row.
- **ASX 24 diff:** 32/32 dated rows content-identical to
  `asx24-2010-2027/live_asx24_trading_calendar.html` (fetched 2026-10-11);
  ONO footnote dates identical (`Friday 23 January 2026`, `Friday 5 June 2026`,
  `Monday 8 June 2026`, `Friday 11 June 2027`, `Monday 14 June 2027`); `2028`
  appears zero times.

## 3. SGX (`sgx_securities` served; `sgx_equity_index*` dormant, no holiday tables)

- **2027 calendar: not published by the operator.** The T2 content-API feed
  (`SGX-ST-SCHED` queryId) still scopes its eve/half-day statement to
  `The Eve of Chinese New Year, Eve of Christmas and Eve of New Year in 2025
  &amp; 2026` and names no 2027 holiday or half-day treatment. The recorded
  gap (`sgx_securities.md`, closing condition "SGX's next annual securities
  schedule naming the 2027 half days") stays open.
- **Diff:** holiday-related content identical to the banked 2026-09-28 JSON
  (`45dbdc61…`); the only content delta anywhere in the payload is a
  Market Maker and Active Trader Programmes (MMAT) blurb module — not
  schedule data.
- **MOM (designated calendar, T1):** year tabs 2025/2026/2027 all
  content-identical to the banked page (page last updated 19 June 2026);
  no 2026 errata; 2027 gazetted dates unchanged; no 2028 tab.
- **Errata:** none.

## 4. OANDA UK books (nine served keys, holiday window …2026-10-30)

- **Post-2026-10-30 publication: does not exist yet.** The holiday page's
  newest dated section is still `Friday, 30 Oct 2026 – All Saint Day (SE)`;
  no November 2026, December 2026 or 2027 section has been printed. 104/104
  dated section headers are content-identical to
  `oanda-uk-holiday-hours-2026-10-10/oanda-uk-holiday-trading-hours.html`.
- **Normal week:** the hours-of-operation page's 25 time-grid tokens
  (`17:05 - 16:59` family) are identical to the 2026-10-10 capture.
- **Watch cadence:** the ledger's "Check OANDA publication again before the
  2026-10-30 native holiday boundary" note stands; per the 2025 page pattern
  the Thanksgiving and Christmas rows appear close to the dates, so the next
  re-pull should land in early-to-mid November 2026.

## 5. Coinbase Derivatives (`coinbase_derivatives`, served, holiday window 2021-06-28..2026-09-07)

- **Remaining-2026/2027 holiday notices: none published yet.** The live
  listing (reader render; direct fetch 403 — see `cde_direct_20261013.html`)
  stops at `26-37` (published 09/24/2026, effective 10/24/2026, Q4 quarterly
  maintenance window) and `26-33.3` (published 09/24/2026, gateway-deploy
  amendment) — both already recorded listed-only in `../cde-2026-2027/`.
  Nothing numbered above 26-37; the only later row is `R2026-56`
  (10/07/2026, Rule Filing, MMP supplemental — not a schedule document).
- **Negative hunt:** the Wayback CDX over
  `assets.ctfassets.net/k3n74unfin40/*` for 2026-09-19..2026-10-15 holds only
  crawls of already-known notice PDFs — no new notice file exists.
- **Errata:** none. Per the 2025 pattern (the 2026 New Year's Day notice
  25-42 was published 2025-11-25), the Thanksgiving-2026 and Christmas-2026
  notices are expected in the next few weeks; the holiday horizon stays
  2026-09-07 until one lands.

## 6. CFE (`cfe`, served, holiday window 2017-04-10..2026-12-31; `cfe_vix` dormant, same windows)

- **2027 calendar: not published.** The operator CSV export regenerated its
  `# Generated:` header to `2026:10:13 16:26:54` but still carries exactly the
  thirteen 2026 rows; the Hours & Holidays page has only a `2026 Futures
  Holiday Schedule` section (its two `2027` strings are conference nav
  links); the circulars list's latest holiday circular remains CFERG26-004
  (2026-03-31). No 2027 holiday notice or calendar exists in any channel
  pulled.
- **2026 errata: none** — the CSV rows are byte-identical (Generated header
  excluded) to the 2026-09-12 capture.
