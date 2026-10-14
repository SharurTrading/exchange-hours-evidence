# CME Group forward-monitoring diff report — 2026-10-13 UTC

Comparison of the operator's live publications (retrieved 2026-10-13T23:29Z..
23:38Z, this machine, direct browser session) against exchange-hours-rs
branch `close_gaps` at `908b7f3` (the 1.1.0 release). Crate files read
read-only; nothing in the crate was modified.

## 1. Per-family status

Every CME-family holiday table in the crate — the four venue mirrors
(`cme`, `cbot`, `nymex`, `comex`) and the eight globex families
(`globex_equity_index`, `globex_energy`, `globex_fx`, `globex_grains`,
`globex_interest_rates`, `globex_livestock`, `globex_cryptocurrency`,
`globex_nikkei_225_dollar`) — declares six audited eras with the last window
**2025-01-01 .. 2027-12-31** (`globex_cryptocurrency` starts 2019). The
2025–2027 rows cite the `CME-SVC-*` captures retrieved live from the
operator's `trading-hours-by-product` service on 2026-09-12 (T2), recorded in
`docs/evidence/cme.md` rows `CME-SVC-2026-09-06` through `CME-SVC-2027-12-22`.

**New publication exists: YES — the 2027 calendar is published.** The
operator's holiday & trading hours calendar page
(`cmegroup.com/tools-information/holiday-calendar.html`, redirecting to
`/trading-hours.html`) carries:

- Holiday Notes accordions for every 2027 holiday: New Year's Day, Martin
  Luther King Day, President's Day, Good Friday, Memorial Day, Juneteenth
  Day, Independence Day, Labor Day, Thanksgiving Day, Christmas Day — plus
  **2028 New Year's Day Notes** (first 2028 statement, see §4).
- The "2026 CME Globex Trading Schedule" annual table (New Year's
  31 Dec 2025 – 2 Jan 2026 through New Year's 31 Dec 2026 – 1 Jan 2027, one
  date span per holiday) — corroborates every remaining-2026 window the crate
  ships; no date-span differs.
- The interactive per-date holiday table, fed by the same T2 service the
  crate cites (the page's own XHR calls are the `CME-SVC-*` URLs).
- The statement: "with the 2026 and 2027 calendar year the CME Group will be
  providing downloadable holiday calendars for Globex and incorporating with
  Regular Trading hours into one location." No per-holiday Globex
  trading-hours PDF ships on the page: the 35 PDFs under
  `/tools-information/holiday-calendar/files/2026/` are clearing advisories,
  settlement-time tables and OTC files (clearing scope). The page adds the
  operator's caveat: "This schedule is subject to change. Trading hours are
  usually finalized approximately two weeks prior to the holiday."

## 2. T2 service re-pull: zero 2026 errata, zero 2027 changes

All fourteen crate-recorded windows re-pulled 2026-10-13T23:31Z reproduce the
2026-09-12 bytes exactly (sha256 match, column in `INDEX.md`). Row-by-row:
**no diff in any window, for any family.** Representative verbatim content
read from the re-pulls and compared against the shipped tables:

- `CME-SVC-2027-06-17` (Juneteenth 2027): ZN/ES/CL/6E/GC print
  `2027-06-18: 2027-06-21 12:00 closed` (Friday 12:00 CT early close) and
  `2027-06-19: 2027-06-21 05:00 open; 2027-06-21 17:00 closed` (Saturday
  session carrying trade date Monday 2027-06-21); Corn prints no events
  6/18–6/19. Matches the shipped `early_close(12:00)` +
  `ReplacementBlocks(&SATURDAY_SESSION_BLOCKS)` rows keyed 2027-06-18/06-21 in
  `cme.rs`/`nymex.rs`/`comex.rs` and the grains `Closed` 2027-06-18 +
  `CLOSURE_EVE_BLOCKS` 2027-06-17 in `cbot.rs`.
- `CME-SVC-2027-12-22` (Christmas 2027): 2027-12-24 prints **no events** for
  every representative product (full Globex closure — Christmas falls
  Saturday, the closure keyed to Friday 12-24); 2027-12-23 prints the normal
  Wednesday grid (16:00 close; grains full day with the 13:20 pause / 13:30
  pit close); BTC continues with only the standard weekend maintenance
  (02:00–04:00 Sat). Matches the shipped `Closed` 2027-12-24 rows and
  `cbot.rs`' `CLOSURE_EVE_BLOCKS` on 2027-12-23, and the T1 "2027 Christmas
  Day Notes" (day orders from the Wednesday 12-22 pre-open roll to trade date
  Thursday 12-23; TAS early closes per product: Copper 11:00, Silver 11:25,
  Gold 11:30, Platinum 11:05, Palladium 11:00, Crude/HO/RBOB/NG 12:30,
  Grain/Oilseed/Livestock 12:00, Bitcoin 12:00 CT).

The 2027 T1 notes otherwise corroborate the shipped 2027 rows date for date:
MLK (Sunday 1-17 pre-open, trade date Tuesday 1-19, Friday 1-15 TAM/TAS
regular close), Presidents (Sunday 2-14 → Tuesday 2-16; Friday 2-12), Good
Friday ("Thursday March 25th all markets have a regular close. No trading for
Friday March 26th trade date"), Memorial (Sunday 5-30 → Tuesday 6-1; Friday
5-28), Juneteenth (Thursday 6-17 pre-open, Friday 6-18), Independence (Sunday
7-4 → Tuesday 7-6; "Friday July 2nd: Regular CME Group Globex close for all
products"), Labor (Sunday 9-5 → Tuesday 9-7; Friday 9-3), Thanksgiving
(Wednesday 11-24 pre-open → Friday 11-26; Tuesday 11-23 TAM/TAS regular;
Wednesday 11-24 TAS per-product shapes).

## 3. Row-by-row diffs — served families

**Holiday tables (all twelve): no diff.** No shipped 2026 or 2027 row changes;
no missing row; the operator publishes nothing for 2026/2027 that the tables
do not already hold.

**24/7 Saturday maintenance extensions (revision-row families): one missing
arrangement.** The crate models CME's one-day Saturday-window extensions for
the 24/7 markets as dated revision rows in three families:
`globex_cryptocurrency` (channels 326/327), `globex_event_contracts_btc`
(channel 329), `globex_silver_100oz` (24/7 since 2026-09-12, notice
20260907). Shipped vs published:

| Saturday | Operator statement | shipped in crate? |
|---|---|---|
| 2026-08-01 → 09:00 CT | notice 20260727 | yes (all three families, where governed) |
| 2026-08-29 → 06:00 CT | notice 20260824 | yes |
| 2026-09-19 → 08:00 CT | notice 20260824, restated 20260831 | yes |
| 2026-10-03 → 05:00 CT | notice 20260921 (restated 20260928) | yes (`cryptocurrency.rs`, `silver_100oz.rs`); **absent from `bitcoin_event_contracts.rs`** (its rows stop at Sep 19/20) |
| 2026-10-24 → 15:30 CT (FIA industry disaster-recovery exercise) | notice 20260921 (restated 20260928) | yes (`cryptocurrency.rs`, `silver_100oz.rs`); **absent from `bitcoin_event_contracts.rs`** |
| **2026-10-31 → 05:00 CT** | **notice 20261005 (NEW)** | **absent from all three families** |

The new operator statement, verbatim (Globex notice 20261005, published
October 5, 2026, saved as `notices/globex-notice-20261005-full.html`):
"On Saturday, October 31, CME Group will temporarily extend the Saturday
maintenance window schedule for 24/7 markets from 2:00 a.m. – 5:00 a.m.
Central Time (CT). Following the extension, the Saturday maintenance window
will revert to its 2:00 a.m. – 4:00 a.m. CT standard schedule."

This is the wave's one actionable crate diff: a forward-dated
2026-10-31 extension row + 2026-11-01 revert row per family, keyed to the
Saturday, following exactly the shipped 20260921 pattern (the crate's own
comment convention: "Forward-dated on the operator's statement; confirm
before the day"). `globex_event_contracts_btc` is dormant, so its Oct 3/24
omission is recorded per LAW-SERVICE-TIERS rather than raised as a served
defect; the two October rows of notice 20260921 postdate that family's last
review.

## 4. First 2028 statement (beyond every shipped horizon)

- **T2** `service/CME-SVC-2027-12-31.json` (window 2027-12-31..2028-01-02,
  sha256 `d5a7c430…`): Friday 2027-12-31 normal 16:00 CT final close; Saturday
  2028-01-01 no session; Sunday 2028-01-02 normal reopen (16:45 preopen /
  17:00 open carrying trade date Monday 2028-01-03). No holiday disturbance.
- **T1** "2028 New Year's Day Notes" (page): "Day orders entered after a
  product's Pre-opening(s) on Thursday , December 30th are for trade date
  Friday, December 31st and can continue working until their Friday,
  December 31st Globex close. December 29th TAS: Regular close per each
  product schedule."

One window does not make a calendar; recorded as the first 2028 witness for
the future 2028 sweep, not encoded.

## 5. Hours changes for unserved product sets (watch items)

- **Bloomberg Commodity Index and Subindex futures/options** — SER-9808
  ("Expansion of the CME Globex Electronic Trading Hours and the CME Globex
  Pre-Open Hours for Nine (9) Bloomberg Commodity Index and Subindex Futures
  and Option Contracts"), announced in Globex notices 20260928 and 20261005:
  "Effective this Sunday, October 11 (trade date Monday, October 12), pending
  completion of all regulatory review periods", from the day-session grid
  (Pre-Open Sunday 16:00–Monday 08:15 and Mon–Thu 16:45–08:15 CT; open
  Monday–Friday 08:15–13:30 CT) to the standard Globex grid (Pre-Open Sunday
  16:00–17:00 and Mon–Thu 16:45–17:00 CT; open Sunday 17:00 – Friday 16:00 CT
  with a daily maintenance period 16:00–17:00 CT). No `MarketHoursKey` routes
  BCOM; recorded so the change is not rediscovered as a CME-family drift.
- All other notices 2026-09-01..2026-10-13 (90 indexed results, pages 1–3)
  are margin, position limit, delivery, listing/catalog or regulation
  business; none touches a served family's session grid. Catalog items
  noted for awareness only: Wind Power options launch moved to 2026-10-11,
  Compute futures postponed (was 2026-10-04), Soybean oil/meal listing-cycle
  amendment + temporary suspensions (2026-09-28), Micro WTI weekly option
  rename/listing expansion, UNI/BCH futures 2026-10-18, IDR/USD termination
  time 2026-10-12 (instrument lifecycle, LAW-SESSION-NOT-EXPIRY scope).

## 6. Channel intel

cmegroup.com's Akamai block still refuses curl from this machine (HTTP 403 on
page and service URLs alike), but a real browser session passes and can fetch
both pages and same-origin service JSON. The "re-verify from a direct
retrieval when one becomes possible" caveats recorded in the crate's
`docs/schedules/sources.md` (US-CME-GROUP status note) are now dischargeable
from this machine; the reader-extracted-text caveat can be retired for any
document this channel re-fetches. The notice-search JSON endpoint used here
(`.../search_sort_filter_d.ssfajax.<page>.0.<from>.<to>.json`) is public and
unauthenticated behind the same gate.
