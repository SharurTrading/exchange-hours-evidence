<!-- SPDX-License-Identifier: MIT-0 -->

# Implementation plan — CME trade-type and standalone-product keys (issue #58)

Planned 2026-09-12 (UTC) against `main` @ `687e562`. Input: the eight research gates and
their nine adversarial verdicts in
`exchange-hours-research/cme-globex/trade-types/`. **Where a verdict reports a
discrepancy, the verdict wins** — every correction below is already folded in and marked
`[verdict Dn]`.

Work item 5 of [the coverage plan](2026-09-05-cme-globex-family-coverage.md) delivered
[the handoff](2026-09-05-cme-trade-type-handoff.md). This plan authors it: **13 PRs, 32
new `MarketHoursKey` rows, 6 keys deliberately blocked, 2 rejections recorded on
evidence.** One fence PR lands first because every later PR touches the same ledger.

---

## 0. What the gates changed since the handoff was written

Read this before opening any PR; four of the handoff's own blockers are gone and two of
its dates are wrong.

| Handoff said | Now |
|---|---|
| U-4 (regular vs extended) blocks every shape | **RESOLVED.** `regular: &[]` for every BTIC, TAS, TAM, TACO and TMAC key in every era. Three affirmative channels (Rule 524's positive route enumeration; ProductSlate's 234 trade-type records at `floor "-"` / `floorVol "0"` / no Floor venue component, against SOFR options' `floor "S3O"` / `floorVol "449,759"` in the same file; ContractSpecs' `"Open Outcry:"` venue label, used for SOFR options and never for a trade-type hours line) plus one contrastive (NYMEX Rule 524.C naming MO as "open outcry trades" in the same rule that names none of the five). This **exceeds** the `globex_spot_quoted` sourced-absence precedent, which rests on four silent channels. Every Pre-Open is `order_entry` (RA2302-5 §3: "Rule 524 permits the initiation of TAS, TAM, BTIC, TACO, and TMAC orders into CME Globex only subsequent to the beginning of each group's pre-open state"). |
| U-8 (cross-zone) blocks eight shapes | **PREMISE FALSIFIED.** A `StaticHoursProfile` carries one `tz`, but a *key* is not limited to one profile: four genuine cross-zone selectors already ship (`ice_endex.rs:150`, `ice_abu_dhabi.rs:103`, `b3.rs:201`, `bmv.rs:235`) plus two self-DST season selectors (`europe.rs:120`, `eurex_fixed_income.rs:287`). `MarketHoursKey::EurexFixedIncome` is the key-side precedent. Twelve shapes are affected, not eight — `6EB` was missing from the handoff's list. |
| U-1 (EST/IPT/RVT contradiction) unadjudicated | **RESOLVED.** The 17:00 ET cells are the generic **ClearPort** envelope with its venue label dropped [verdict D4 — not "the ClearPort BTIC window"]. Seven venue-labelled live records and eleven dated archived states of productId 133 say 16:00 ET. |
| TACO era 2 has "No notice found" | **WRONG.** Clearing Advisory **21-234** (notice date 2021-07-01, effective 2021-09-27) tabulates both grids side by side and names the product codes [verdict D1]; the weekly Globex notice carried the item in **13 consecutive issues**, 2021-06-28 through 2021-09-20, never naming a different day [verdict D3]. |
| TAM launch rows at trade dates 2011-06-13 / 2011-07-11 / 2024-06-17 / 2017-10-23 / 2019-02-25 | **ALL FIVE ARE ONE DAY LATE** [U-8 verdict D4]. These grids open 17:00 CT the previous evening, so LAW-NO-FABRICATED-DATES keys them to the local opening day: **2011-06-12, 2011-07-10, 2024-06-16, 2017-10-22, 2019-02-24**. |
| Gasoil "current close 10:30 CT is undated" | **WRONG.** 11:30 a.m. ET *is* 10:30 CT; the 2016-12-19 notice is the cutover. |
| RA1005-4's "(ET)" must be adjudicated | **RESOLVED as a typographic error**: RA1006-4 reprints the same table with every row exactly +1h under the same "(ET)" label across 15 common product rows [verdict D6 — 15/16 rows, not "ten"], and relabels the column from "Globex Pre-Open Time Period" to "No-Activity Period". The energy-TAS effective day is **2010-11-01, not 2010-10-25** — and no 2010 revision row should be opened at all (see PR 5). |

---

## 1. PR sequence

Each PR is independently mergeable and independently revertible. **Every PR touches
`docs/schedules/verification.md`, `README.md`, `CHANGELOG.md` and
`docs/schedules/sources.md`, so each merge breaks the next one's mergeability. That is
expected: land one, rebase the rest, and re-derive every tally from the *merged* ledger
rather than resolving the conflict by picking a side** (coverage plan, "Traps already
paid for").

| # | PR | Keys | Ready? | Blocked on |
|---|---|---|---|---|
| 1 | Fences before the families | 0 | **yes** | — |
| 2 | Metals TAS | 5 | **yes** | — |
| 3 | Grain and livestock TAS | 2 | **yes** | — |
| 4 | Cryptocurrency TAS | 1 | **yes** | — |
| 5 | Energy and gasoil TAS | 2 | yes | decision **D-5** (minor), **D-6** (doc text only) |
| 6 | Commodity-index cash families | 3 | yes | decision **D-7c** (minor) |
| 7 | Dairy, lumber, southern yellow pine | 3 | yes | — |
| 8 | Santos soybeans, urea, Black Sea wheat | 3 | yes | decision **D-7a**, **D-7b** (minor) |
| 9 | Equity, commodity-index and credit BTIC | 3 | yes | — |
| 10 | TACO and TMAC | 2 | no | decision **D-3** |
| 11 | Energy TAM — the first cross-zone key set | 3 | no | decision **D-1**, **D-2** |
| 12 | Metals TAM | 2 | no | decision **D-1**, **D-4** |
| 13 | TOPIX BTIC, Nikkei BTIC, FX BTIC | 3 | no | decision **D-1**, **D-3** |
| — | Rejections recorded, no key | 0 | with PR 1 | — |

PRs 1–4 need no decision from the maintainer. PRs 5–9 need only the four minor calls in
§4. PRs 10–13 need D-1 through D-4.

---

## 2. Per-PR specifications

### Conventions that apply to every PR below

- **Registration surface** (the deliberate coverage fences; do all of these by hand —
  AGENTS.md forbids generating them from `ALL`):
  1. enum row + canonical `snake_case` name + variant doc in the `market_hours_keys!`
     table, `src/calendar/futures_profile.rs`
  2. `hours_for_market_hours_key` arm (same file) → the module's `profile_at`; and the
     date-aware `calendar_for_market_hours_key` surface (AGENTS.md item 3) — no arm to
     add, since it reselects `hours_for_market_hours_key` per opening day, but the key's
     registration, history, cutover and boundary tests (open, close and the instants either
     side) must exercise it through that surface on both sides of the opening day
  3. `session_profile` arm + a `FuturesSessionProfile` static in
     `src/calendar/futures_profile/profiles.rs`
  4. the module's `pub(crate) use` re-exports in
     `src/calendar/schedules/futures/us/mod.rs`
  5. `EXPECTED_MARKET_HOURS_KEY_NAMES` (bump the array length) in
     `tests/schedule_documentation/mod.rs`
  6. `EXPECTED_MARKET_HOURS_KEYS` in `tests/venue_sessions/named_profiles.rs`
  7. `SUPPORTED_FAMILY_NAMES` in `tests/unsupported_market_hours_keys.rs`
  8. the `MarketHoursKey` row in `docs/schedules/verification.md`, **with a Basis and a
     `Reviewed on` date ≥ the repository cutoff `2026-08-22`, and with no `|` anywhere
     inside a cell** — `row_cells` splits on `|`, and the row must have exactly 6 cells.
     The `Reviewed on` date is the **UTC** calendar date the evidence was checked
     (LAW-UTC-DATES, on `main` since `687e562`): take it from `date -u`, never from the
     machine's local day, which runs ten hours ahead of UTC on the maintainer's clock
  9. `docs/schedules/sources.md` — `US-CME-GROUP` already covers every key in this plan,
     so no new source set is needed; the **Status** paragraph's prose counts change (PR 1
     fences them)
  10. `CHANGELOG.md` under `[Unreleased]` / **Added**
  11. README: the fenced counts (see PR 1) and the coverage/limitations prose
  12. `UPDATE_GOLDEN=1 cargo test --test golden_grids`, then **confirm no other key's rows
      moved**
  13. tests in a **new submodule** of `tests/futures_family_boundaries/`, registered in
      that directory's `mod.rs` — never fatten the root
- **Test content** (AGENTS.md item 6): published open and the instant before it;
  `regular`/`extended`/`order_entry` classification; every gap, with its
  `session_state` kind asserted; the end-exclusive close; the weekend boundary; the
  serde round-trip; **both sides of every cutover at venue-local midnight**; and a
  **separation test** against the key this one is most likely to be confused with, on an
  instant where the two disagree.
- **Mutation-check every cutover fence** — move the revision one day, confirm failure,
  restore, and **say in the PR that you did it**.
- **Every probe instant is stated in `America/Chicago` wall clock and converted**, as
  `tests/futures_family_boundaries/cme_bitcoin_event_contracts.rs` does, so a DST slip
  in either direction fails rather than passing on a coincidence.
- **Date keying.** A row on a grid that wraps from a 17:00 (or 19:00) CT evening open is
  keyed to the **local opening day** — for a Monday trade date, the preceding Sunday. A
  row on a non-wrapping day session is keyed to the day the grid first governs. This is
  where the U-8 gate got five rows wrong; check every date below against its quoted
  source.
- **Production files stay at or below 500 lines** and functions at or below 100. Each PR
  below names its module split accordingly.
- **`regular: &[]`** for every trade-type key (U-4). Each module comment must name **the
  channels its own empty `regular` rests on** — they differ per shape — and the energy
  and metals TAS modules must additionally record the 2009-2015 NYMEX/COMEX pit clause
  and why it does not create a regular session (see PR 2 and PR 5).
- **LAW-FOLLOW-UPS-ARE-ISSUES.** Each PR opens the issues listed in its "Follow-ups"
  block **before it merges**, and cites the issue number where the follow-up is named.
- **LAW-UTC-DATES** (added to `AGENTS.md` on 2026-09-12 UTC, after the gates ran). Every
  date a PR records about the repository's own work — ledger `Reviewed on`, a
  knowledge-bound row's date label and citation label, audit or ledger amendment notes,
  a CHANGELOG release date, a plan's "planned on" date — is the UTC calendar date of that
  work. Exchange effective days stay venue-local civil dates keyed to the opening day.
  Wayback capture timestamps are already UTC; a `capture 2026-09-06` label is fine as
  long as it is the UTC stamp, not the local one.

---

### PR 1 — Fences before the families

**Keys: none.** This PR exists because the coverage plan requires it ("put a PR that adds
a fence *before* the PRs it protects") and because issue #58 asks what fence the repo
lacks. Five fences and one capacity fix, each justified by something the last two
key-adding PRs actually missed.

**F1 — `ledger_covers_every_market_hours_key_variant`. The ledger is not tied to the
enum at all.** `tests/schedule_documentation/mod.rs` does not so much as import
`MarketHoursKey`: `verification_ledger_has_every_market_hours_key_once_and_in_order`
compares the ledger to the handwritten `EXPECTED_MARKET_HOURS_KEY_NAMES` and nothing
compares that array to `MarketHoursKey::ALL`. A key added to the enum,
`named_profiles.rs`, `unsupported_market_hours_keys.rs` and the golden file, but
forgotten in the ledger *and* in `EXPECTED_MARKET_HOURS_KEY_NAMES`, ships green — with no
Basis, no `Reviewed on`, no owner link and no source set, which is the one thing
LAW-PRIMARY-SOURCES exists to prevent. Add:

```rust
assert_eq!(
    EXPECTED_MARKET_HOURS_KEY_NAMES.as_slice(),
    MarketHoursKey::ALL.iter().map(|key| key.as_str()).collect::<Vec<_>>().as_slice(),
);
```

This *compares* two independently maintained artifacts rather than generating either from
the other, exactly as `named_profiles.rs:79` already does with
`assert_eq!(MarketHoursKey::ALL, expected_keys)`, so it is in-pattern under AGENTS.md's
"never generate those independent fences from `ALL`". **This is the fence the whole
sequence most needs: thirty-two additions each pass through that hole.**

**F2 — `handoff_keys_are_registered_or_rejected`.** The fence issue #58 names. `include_str!`
`docs/plans/2026-09-05-cme-trade-type-handoff.md`; walk its backticked spans; keep every
span matching `globex_[a-z0-9_]+`; for each, require **either** that it parses as a
`MarketHoursKey` **or** that `docs/schedules/unsupported-families.md` contains it. Extract
from backticks, **not** from the table structure — the handoff's rows are `|`-delimited
and a table parser would be brittle and would tempt someone to put a `|` in a ledger
cell. Add the mirror assertion for roots: every root the handoff marks `**UNMAPPED**`
must be named in `unsupported-families.md`. Effect: the handoff's 23 proposed key names
become a checklist the suite enforces, and a key that is neither authored nor
*explicitly* rejected cannot be quietly dropped between PRs.

**F3 — `cme_source_set_prose_counts_match_the_ledger`.** `docs/schedules/sources.md`'s
`US-CME-GROUP` **Status** paragraph hand-writes "All **fourteen** fixed-current CME-family
profiles…" and "**Thirteen** of the fourteen are Partial…". Nothing derives either; the
only fence on `sources.md` today is anchor resolution (`validated_source_link_count`) and
`every_source_set_is_referenced_by_a_ledger_row`. Every one of PRs 2–13 changes both
numbers. Derive them: count ledger key rows whose Source-sets cell contains
`sources.md#us-cme-group`, and the Partial subset, and assert the spelled-out claims via
`number_words`.

**F4 — `every_executable_gap_row_is_named_in_the_prose`.** The gap-kind *counts* are
fenced (`the_gap_kind_split_is_quoted_consistently_everywhere`); the *enumerations* are
not. README:304 reads "The executable seventeen — the ICE Futures U.S. keys, CME Nikkei
225 Dollar, the SGX equity-index keys, `nyse` and `nyse_american`, … — are each served
conservatively", and `verification.md:56` reads "The executable seventeen are …". Both
name rows by hand. Assert that every wire name whose ledger row contains `Gap:
executable` appears inside those two enumerations. Without this, a PR can bump the count
word and leave its own key out of the sentence the count refers to — which is the same
defect class as the two the last PRs fixed, one level down.

**F5 — `variant_arithmetic_prose_matches_the_ledger`.** Two more unfenced hand-written
counts that every PR here changes: README:178, "`MarketHoursKey` has **31** variants—**30**
operator-derived product-family keys plus the synthetic `AlwaysOpen` key" (the *fenced*
claim is the different sentence at README:40), and `tests/golden_grids.rs`'s module doc,
"it covers all **96** exchanges and all **31** keys at once". Derive both from the ledger;
reach the golden header with `include_str!("../golden_grids.rs")`, the same technique
already used for the README and the audit.

**F6 — capacity, and it is load-bearing for PR 2.**
`the_gap_kind_split_is_quoted_consistently_everywhere` carries a local `words` array
ending at `"twenty-five"` and **panics** (`"extend the number words past {partial_keys}"`)
the instant the ledger holds 26 Partial keys. It holds **24 today**; PR 2 alone adds five.
`assert_key_basis_prose_matches_the_ledger`'s local `spelled` stops at 20 and silently
falls back to digits, which is why the README currently reads "Six key rows are
**Primary** and 24 are **Partial**". Reconcile both against the module's existing
`number_words` (valid below 100), raise its own `assert!(n < 100)` bound or pin the prose
style, and rewrite that README sentence to spelled form ("…and twenty-four are
**Partial**") so the style does not flip mid-sequence.

**Also in PR 1 — the rejections on evidence, and the six blocked keys**, so F2 is green
from the start. F2 requires every `globex_*` name the handoff proposes to be either a
registered key or named in `docs/schedules/unsupported-families.md`; the six keys §3
blocks are neither, so PR 1 must also add a **"Blocked, not rejected"** block to
`unsupported-families.md` naming each of them, what blocks it (from §3) and the issue
number that tracks it — a blocked key is a follow-up, and LAW-FOLLOW-UPS-ARE-ISSUES wants
the issue open before the PR merges. Then add the rejections on evidence rather than on
effort:

- **Treasury TAS — `TNT`, `UBT`, `ZBT`, `ZFT`, `ZNS`, `ZTT`.** Launch dated (SER-8863;
  Globex Notice 2021-10-18, trade date 2021-11-15) but **no CME document states the
  hours**. The 14:00 CT close is feed-only and equals the stated Treasuries settlement
  range end 13:59:30–14:00:00 CT, which under LAW-SESSION-NOT-EXPIRY proves nothing.
  Record that SER-8863 was retrieved (294,279 bytes) and states no hours anywhere — **do
  not re-fetch it** — that its body is conditional ("pending all relevant CFTC regulatory
  review periods"), and that its own summary table prints `ZNT` where its Exhibit 1 and
  the Product Reference Sheet say `TNT`. Name what would close it: a CFTC 40.2/40.6
  certification for the CBOT Oct–Nov 2021 Treasury TAS listing whose appendix carries a
  Trading Hours row. Note also that `GlobexInterestRates`' doc says only "Excludes options
  and separately specified interest-rate product families" — it does **not** name TAS, so
  the non-reuse argument must rest on the two-hour close difference, not on a borrowed
  citation from `GlobexEnergy`.
- **Dutch TTF TAS — `TAS`, `TTS`.** Absent from RA1005-4/RA1006-4 and from every retrieved
  CME hours statement; the zone anchor is undecided, because one summer week cannot
  separate a 10:05 CT close from 16:05 London or 17:05 CET, and CME demonstrably *does*
  express settlement ranges in London time when a product is London-anchored ("Aluminum |
  16:25:00-16:30:00 London") while listing no row for Dutch gas at all. **Never infer the
  anchor from the TAM note.**
- **Commodity-index BTIC — `AWT`, `BAT`, `BET`, `BGT`, `BLT`, `BMT`, `BPT`, `BST`, `CCT`.**
  Measured on their own Globex groups (B7, 8G, 8R, 8S, 8U, 8T, 8Q, 8X, FX) at
  `open@08:15` / `closed@13:30` CT — feed-only, with no CME prose, and the one CME document
  that tabulates a BTIC window for them (SER-9138 / Submission 23-074) is demonstrably
  defective twice over. They must **not** ride `globex_bloomberg_commodity_index`: merging
  would import AW's history and report BTIC BCOM closed 17:00–08:15 CT, a **15h15m**
  executable-hours gap asserted with full confidence. Record [verdict D5] that no `17:00`
  boundary of any kind exists on group B7 — the queue starts at Sunday 16:00 / weekday
  16:45 and runs overnight to the 08:15 open — so 23-074's "5:00 pm" is not even a queue
  start.

**Tests:** the five fences above plus the capacity fix. **Mutation check:** for each
fence, stale the artifact it guards (drop a key from
`EXPECTED_MARKET_HOURS_KEY_NAMES` and leave the ledger row; add a `globex_*` name to the
handoff that resolves nowhere; change "fourteen" to "fifteen" in `sources.md`; delete one
name from the README's executable enumeration; change `31` in the golden header), confirm
red, restore, confirm green. Say so in the PR.

**Residual risk:** F2 reads a `docs/plans/` file, which the repository otherwise treats as
a historical record. That is deliberate — the handoff *is* the work list for #58 — but it
means a future edit to the handoff can fail the suite. State that in the test's doc
comment, and say that the correct response to a red F2 is to author or reject the key,
never to edit the handoff.

---

### PR 2 — Metals TAS

**Keys (5):** `globex_gold_tas`, `globex_silver_tas`, `globex_copper_tas`,
`globex_platinum_tas`, `globex_palladium_tas`.
**Modules:** `src/calendar/schedules/futures/us/metals_tas.rs` (gold, silver, copper —
they share the MRAN chain and both order-entry revisions) and
`src/calendar/schedules/futures/us/pgm_tas.rs` (platinum, palladium — one era each, later
launches, different exchange lineage). Two modules because the citation blocks are long
and `mini_grains.rs` reached 448 lines for one key with seven revisions.

**Why first:** every launch day is unconditional, there is not one cross-zone endpoint,
there is not one executable revision in sixteen years, and no maintainer decision is
involved.

`tz: US::Central`. `regular: &[]`. `has_daily_close: true`, `has_weekend_close: true`.
Sunday–Thursday opens at 17:00 CT wrapping to the stated close; **no Friday-evening
reopen** (RA1006-4: "1:30 p.m. (ET) Friday- 5:15 p.m. (ET) Sunday"). Every
inter-trade-date gap exceeds four hours (gold 4h30m, silver 4h35m, platinum 4h55m, copper
and palladium 5h), so it is **`Closed`, not `Maintenance`** — state that in the comment so
nobody "fixes" it later.

| Key | Pre-launch | Launch row (local opening day) | Close | Effective-date source |
|---|---|---|---|---|
| `globex_gold_tas` | closure | **2010-04-11** (Sun; trade date Mon 2010-04-12) | 12:30 CT | NYMEX/COMEX Submission 10-070 with SER S-5166 attached, 40.6 self-certification: "the launch of TAS pricing for the active month in each of Gold Futures (Chapter 113) and Silver Futures (Chapter 112) on Globex on April 11 (for trade date April 12)" |
| `globex_silver_tas` | closure | **2010-04-11** (same document) | 12:25 CT | as above |
| `globex_copper_tas` | closure | **2011-01-23** (Sun; trade date Mon 2011-01-24) | 12:00 CT | COMEX SER-5542 (2010-12-22), "on CME Globex only"; RA1101-4, whose own Effective Date is that same day, prints HGT's window on the day it starts |
| `globex_platinum_tas` | closure | **2017-05-21** (Sun; trade date Mon 2017-05-22) | 12:05 CT | CME Globex Notice 2017-05-08, unconditional |
| `globex_palladium_tas` | closure | **2018-11-18** (Sun; trade date Mon 2018-11-19) | 12:00 CT | CME Globex Notice 2018-11-12, unconditional |

**The pre-launch closure is sourced, not assumed.** RA0907-4 (2009-08-31) and
RA1001-4/RA1002-4 (2010-02-02) each print CME's *complete* TAS-eligible product list and
none contains gold, silver or copper; RA1005-4 and RA1006-4 carry GCT and SIT rows and no
HGT row; the platinum spec capture of 2017-03-03 contains the string "TAS" zero times
while 2017-05-23 carries "TAS: PLT". So the pre-2010-11-01 Rule 524.A.2 sentence that
supplies the energy-TAS floor era ("TAS transactions on Globex may take place at any time
the applicable contracts are available for trading on Globex") is **inapplicable here** —
gold was not an applicable contract. **Do not carry any grid back to the January-2010
floor on these five keys.**

**Order-entry rows — two, both on gold/silver/copper only, neither touching an executable
boundary:**

- **2011-04-10** (Sun opening day; trade date Mon 2011-04-11) — MRAN **RA1104-4** staggers
  the TAS queue onset per product: gold Sunday 16:18 / Mon–Thu 16:48; silver 16:19 /
  16:49; copper 16:20 / 16:50. The same table leaves every close unchanged.
- **2012-04-15** (Sun opening day; trade date Mon 2012-04-16) — CME Globex Notice
  2012-04-02 / 2012-04-09 ends the stagger and moves every TAS group to one randomised
  one-minute window: "a market pause … at 16:15:00 on Sunday and 16:45:00 Monday through
  Thursday. TAS groups will then go into pre-open on Sundays between 16:15:00 and
  16:16:00 Central time (CT), and Mondays through Thursdays between 16:45:00 and 16:46:00
  CT." Unconditional.

**Order-entry window served (the sourced intersection, and this is the crate's existing
worked example).** For gold/silver/copper the Sunday onset is sourced at 16:15
(RA1006-4 / RA1101-4 / RA1102-4), then 16:18/16:19/16:20 (RA1104-4), then 16:15 again
(2012-04-09 notice), then 16:00 — undated, bracketed to (2012-04-15, 2012-06-16] and
stated by CME's client-systems wiki in 2025. **A knowledge boundary may only widen**, so
serve `order_entry` from 16:15 (16:18/16:19/16:20 inside the 2011-04-10..2012-04-14 row)
to 17:00 across the whole span and **withhold 16:00–16:15**, exactly as
`globex_equity_index`'s Sunday Pre-Open already does; cross-reference that row in the
comment. The weekday onset needs no withholding: 16:45 → 16:48/16:49/16:50 → 16:45, all
three states dated. Platinum and palladium launched *after* the undated Sunday move, so
their earliest sourced Sunday onset is 16:00 and nothing is withheld — serve Sunday
16:00–17:00 / Mon–Thu 16:45–17:00.

**Executable boundaries: zero revision rows on any of the five, launch to today.** Say so
explicitly beside the table — a reader who sees no revisions must be told this is a
*sourced constancy* across sixteen years and a dozen dated observations, not an unworked
row. Gold's 12:30 close is observed at RA1006-4, RA1101-4, RA1102-4, RA1104-4; the metals
hours page at 2011-10-29 / 2012-05-01 / 2012-06-16 / **2012-09-14 / 2013-09-02 /
2014-07-07 / 2014-11-04** / 2015-03-22 [verdict D3/D4 added four of those]; the spec page
2019-11-18 → 2021-06-21; the ContractSpecs API 2021-07-10, 2022-08-26, 2023-06-17,
2025-06-04, 2025-10-16, 2026-05-27, 2026-08-27; and live.

**The 2015-09-20 DCM-wide move did not reach metals TAS**, on two independent arguments.
Scope, in the notice's own words — CME Globex Notice **2015-08-17** says the maintenance
period starts fifteen minutes earlier and "the closing times for the following markets
will now occur 15 minutes earlier Monday through Friday at 16:00 CT" for CME Equity, CBOT
Equity, COMEX, NYMEX and DME; a 12:30 / 12:25 / 12:00 CT close is not a 16:15 CT close and
cannot move to 16:00. And direct observation: the last statement before (2015-03-22) and
the first after (2019-11-18) are the same values. **The notice's own stated day is Monday
2015-09-21, not "trade date 2015-09-20"** — 2015-09-20 was a Sunday [U-6 verdict D4]. The
control that makes these separate keys: the same notice demonstrably *did* move the metals
outrights (gold's spec goes from "5:15 p.m. … 45-minute break" on 2015-09-06 to "5:00
p.m. … 60-minute break" on 2015-10-09).

**Do not:**
- merge copper and palladium on their coincident 12:00 close — different exchange (COMEX
  vs NYMEX), different security group (HT vs PX), launches seven years apart, different
  settlement determination ranges. The `globex_mini_grains` precedent (three keys, one
  envelope, three histories) applies directly.
- encode any 16:00–17:00 CT daily break on palladium TAS. The spec's "60-minute break each
  day beginning at 4:00 p.m.(CT)" clause is **inherited boilerplate from the outright row**
  — a book closed at 12:00 CT cannot break at 16:00 — and CME had deleted it from the TAS
  line by 2020-11-26 while leaving the instants unchanged. The handoff calls that spec "the
  strongest document in the group"; it is not. **The strongest are RA1006-4 and RA1107-4**,
  which call it "a TAS trading session" with a stated end and pre-date the spec channel by
  nine years. Correct the handoff's characterisation in the module comment.
- encode any pit or open-outcry window. There *was* a pit-era COMEX TAS, for gold and
  silver only, beginning one day *after* the electronic one (SER S-5166 heads its sections
  "A. Gold Futures (GC) (CME Globex TAS code GCT) Traded on CME Globex and COMEX Pit" and
  the cover letter dates the floor launch "on the COMEX trading floor on April 12");
  RA1107-4 confirms and adds that copper TAS was never pit-eligible. Pit TAS had **no
  window of its own** — Rule 524.A.1 ties it to "the hours designated for pit trading in
  the particular contract". CME's metals hours page gives Gold TAS an Open Outcry cell of
  "08:20-13:30 ET (07:20-12:30 CT)" in every capture 2011-10-29 → 2015-03-22, gives Silver
  TAS none, and its Copper TAS cell "08:10-13:00 ET" is CME's own error (that is the copper
  pit *matched-order* window, as RA1005-4, RA1006-4 and RA1107-4 all state) and is empty
  from 2012-05-01 on. **Write this into the module comment so the next reader does not
  "discover" the pit clause and conclude the key is wrong.**
- treat any member listing as a revision: MGT 2018-09-23; QOT, 1OT, MHT and MST all
  2025-07-27 (Globex Notice 2025-07-21; COMEX Submission 25-240); HG0 undated with an
  upper bound of 2018-08-10 only. All caller catalog data.

**Corrections to fold in from the verdict, before anything reaches a source comment:**

- **[verdict D1]** The result's `verbatim` for RA0907-4's Globex TAS list is **partly
  fabricated** — the document's complete list is eleven codes, `WST RTI BHT HPT HHT BBT
  CLT HOT NGT RBT RET`; `BZT` occurs **zero** times in it and five real codes were
  dropped. Quote the eleven, or do not quote the document.
- **[verdict D2]** RA1102-4 is cited but has no evidence row. It is saved at
  `raw/metals-tas-history/rul010611nymexandcomex001.pdf`, sha256
  `a71fb96d6821ed4396be3c726c42beb9e299b55ae3f9e1de2a2b2706df193607`, header "Advisory
  Date January 7, 2011 | Advisory Number NYMEX & COMEX RA1102-4 | Effective Date January
  23, 2011". Cite it with its hash.
- **[verdict D3]** Do **not** write that the 2012-06-16 hours page is "simply a stale
  page". The 2012-09-14 and 2013-09-02 captures of the same URL print
  "Pre-Open Electronic Trading (Weekday) 17:45-17:46 ET (16:45-16:46 CT)" for all three
  metals — the 2012-04-09 notice's uniform randomised minute — so the notice's adoption is
  *observed*, not asserted over a later capture.
- **[verdict D4/residuals]** Record the observation gaps beside the rows: gold/silver/copper
  close 2015-03-22 → 2019-11-18 (channel exhaustion, not a sampling choice —
  `metals-hours.html` has no 200-status capture after 2015-03-22 and the spec channel
  carried no TAS hours line until autumn 2019); platinum 2021-04-11 → 2026-03-10;
  palladium 2021-05-13 → 2026-05-27.
- Correct the handoff's "unsourced 2021-07 → today (CME retired the server-rendered
  pages)" — false; Wayback archives `/CmeWS/mvc/ContractSpecs/List/productId/N` and the
  reader route returns it today. And its "MST … presumably 2023+" — MST listed 2025-07-27.
- Note in the module comment that productId **445 is palladium and 446 is platinum**, the
  reverse of the gate brief, so the next reader does not re-derive it backwards.

**Ledger:** five rows, Basis **Partial / `Gap: executable`** — each row's executable close
is carried across a multi-year observation gap with no cutover asserted, which is the same
reason `globex_event_contracts` is Partial/executable. Name each gap in the row.

**Follow-ups to open as issues:** HG0's undated listing day; the undated Sunday
16:15→16:00 CT move inside (2012-04-15, 2012-06-16] (cross-reference the existing
`globex_equity_index` issue rather than opening a duplicate); the gold TAM code drift
GC7→GCD and copper HGK/HGF; and the four NYMEX **softs TAS** rows the MRAN chain sources
and nothing keys — `KTT` NYMEX Coffee (12:30 p.m. ET), `CJT` NYMEX Cocoa (11:50 a.m. ET),
`TTT` NYMEX Cotton (2:15 p.m. ET), `YOT` NYMEX No. 11 Sugar (12:30 p.m. ET) — plus
`XKT`/`XCT` and `RET` [U-6 verdict D7].

---

### PR 3 — Grain and livestock TAS

**Keys (2):** `globex_grains_tas`, `globex_livestock_tas`.
**Module:** `src/calendar/schedules/futures/us/ag_tas.rs`.

Both launch on one unconditional day: **RA1503-3** — CME and CBOT adopted Rule 524
effective Sunday 2015-06-07 for trade date Monday 2015-06-08, and the string "pending"
does not occur in the document. Pre-launch is a **positively witnessed** closure: the corn
and live-cattle spec pages carry zero occurrences of "TAS" at 2014-11-02 and 2015-05-22
[replace the stored 2015-05-22 artifact first — **verdict D1**: the saved file is Internet
Archive chrome, not a CME page; the real capture is 83,721 bytes at
`web.archive.org/web/20150522230148id_/…`, sha256
`fd5f67b3a740beeff5e98028cfa5ac7de244189d12ac90589cac850de8520ba3`, and does carry the
claim].

**`globex_grains_tas`** — roots ZCT, SBT, ZMT, ZLT, ZWT, KET. Globex groups TA (SBT, ZLT,
ZMT), TP (ZCT), TW (ZWT, KET): **the key is a family claim spanning three groups**, and the
warrant is textual, not structural — CME states one hours cell for "all CBOT Grain TAS
products" on the corn spec page and one cell for all six on the fact card. **Say that
beside the table** [verified residual]. Note also that only the *corn* page carries the
family sentence; the soybean page captured the same day prints "TAS: SBT" in Product Code
and no TAS hours sentence at all.

- **One era, keyed 2015-06-07** (local opening day — the grid wraps from a Sunday 19:00 CT
  open). `extended`: Sunday–Friday 19:00–07:45 CT (wrapping) **and** Monday–Friday
  08:30–13:15 CT. `regular: &[]`. **`order_entry: &[]`** — ship the key with no queue
  rules rather than copying `globex_grains`'; CME's only statement about the 07:45
  boundary is about order persistence, not a queue window ("All resting TAS orders at
  07:45 will remain in the book for the 08:30 opening, unless cancelled"). Say that the
  omission is deliberate.
- **Assert no row at 2015-07-05/06**, and say why positively as well as negatively.
  Negatively: SER-7395R's Appendix 1 is the complete affected-product list for the CBOT
  grain move (95 product rows ending with Black Sea Wheat, exactly as its supersession
  note says) and the string "TAS" does not occur once in its fifteen pages. Positively:
  CME's own corn spec page prints, at family scope and in session language, "Trading in
  all CBOT Grain TAS products will be 19:00-07:45 and 08:30-13:15 Chicago time" at
  2015-09-05, 2015-10-09, 2016-03-10, 2017-05-20 and 2019-07-17, and the ContractSpecs API
  carries the identical pair at 2021-07-10, 2024-06-12, 2026-08-10 and live. **Do not
  write "no gap wide enough to hide a revision"** — that is rhetoric, not a measurement
  [verified residual]; write the observation gap (2019-07-17 → 2021-07-10) and say the
  state is identical at both ends.
- **Do not reuse `globex_grains`**: it steps to 13:20 CT on 2015-07-05 and this key does
  not.

**`globex_livestock_tas`** — roots LET, GFT, HET, Globex group TH. Non-wrapping day
sessions in every era.

- **Row 1, keyed 2015-06-08**: Monday 09:05–13:00 CT, Tuesday–Friday 08:00–13:00 CT. Grid
  sourced twice — the 2015-06-10 fact card and CME's live-cattle spec page at 2015-09-05
  and 2015-11-27. **Cite the spec page, not the fact card, for the zone** — the fact
  card's cell carries no zone label; "Chicago time" is the spec page's word [verified
  residual]. No Pre-Open sourced for this era.
  **Date exception, sourced verbatim, belonging to `DayPolicy` and
  `docs/schedules/date-exceptions.md` and *not* to the template (LAW-HOLIDAY-SCOPE):** the
  09:05 open also governs "the Tuesdays that follow a Monday holiday".
- **Row 2, keyed 2016-02-29**: Monday–Friday 08:30–13:00 CT, plus `order_entry`
  06:00–08:30 CT. Source **SER-7591**, in session language and naming all three Globex
  codes: "Trading of Live Cattle TAS Futures, Feeder Cattle TAS Futures, and Lean Hog TAS
  Futures will be 8:30 am – 1:00pm (Central Time) Monday – Friday." Its "pending CFTC
  review" clause is discharged by the fact card created 2016-03-03 and by the spec page at
  2016-03-11 — **record the discharge beside the row**, do not assume it. Restated at
  2017-12-11, 2021-07-10, 2026-08-10 and live. The 06:00 queue is carried back exactly as
  `livestock.rs` carries the underlying's, because SER-8599R states the outgoing 06:00
  value and 2016-02-29 is the day the 08:30 open it queues into was established.
- **Row 3, keyed 2020-05-31**: `order_entry` narrows to 08:00–08:30 CT; the executable
  window is unchanged. Source **SER-8599R**, naming LET/GFT/HET with both values.
  **[verdict D5]** SER-8599R is *also* conditional ("Effective Sunday, May 31, 2020 for
  trade date Monday, June 1, 2020, and pending all relevant regulatory CFTC review
  periods") and no post-effective artifact was retrieved. Its warrant is that `livestock.rs`
  already keys 2020-05-31 to it — **record that as the discharge** rather than leaving it
  implicit, and note it is the weakest of the three rows.
- **[verdict D8]** Rows 1 and 3 use two different keying rules (trade date vs effective
  Sunday) and both cannot follow from one convention; the grid has no Sunday session in
  either era, so they are observationally identical. **Mirror `livestock.rs` row for row**
  so the TAS key's dates line up with the underlying's, state the convention beside the
  table, and open an issue if the two rows in `livestock.rs` itself are inconsistent.
- **Never add a Post-Close.** Globex Notice 20160530's product table names only LE/GF/HE,
  so the 14:30–16:00 CT PCP that `livestock.rs` adds on 2016-06-06 does not exist here.
  **Sourced absence, not an unknown** — say so.
- **Do not reuse `globex_livestock`**: 13:00 vs 13:05 today, a completely different era-1
  shape, and a different order-entry history from 2016-06-06.

**Documentation debt this PR must clear** (handoff §5, final paragraph): `GlobexGrains`
mentions TAS in neither `futures_profile.rs` nor `verification.md`, unlike `GlobexEnergy`,
`GlobexFx`, `GlobexLivestock` and `GlobexRoughRice`. Add the exclusion to both, naming the
new key.

**Ledger:** `globex_grains_tas` — Partial, `Gap: order-entry` (the queue onset for
TA/TP/TW is unsourced and deliberately unmodelled). `globex_livestock_tas` — Partial,
`Gap: order-entry` (era 1 has no sourced queue).

**Follow-ups:** the grain TAS Pre-Open onset (channels already exhausted: the fact-card
CDX has three digests with a five-year archive hole; the trading-hours service is empty
for TG/CT/CI; CME Rulebook Chapter 5 / Rule 524.A.1 confirms a "prescribed pre-open time
period" exists but states no clock and serves its TAS/BTIC/TACO/TMAC table as an external
XLS); the pre-2016 livestock TAS Pre-Open; the `livestock.rs` keying inconsistency.

---

### PR 4 — Cryptocurrency TAS

**Key (1):** `globex_cryptocurrency_tas` — roots TBT, TBM, TET, TEM, TSL, TMS, TXP, TMX;
Globex groups CI (TBT/TBM), CM (TET/TEM), LT (TSL/TMS), XQ (TXP/TMX).
**Module:** `src/calendar/schedules/futures/us/cryptocurrency_tas.rs`.

Pre-launch closure, positively witnessed: BTC's ContractSpecs object has no TAS key and no
TAS hours line at 2021-07-10 and 2022-09-21.

- **Row 1, keyed 2023-02-05** (local opening day; the grid wraps from a Sunday 17:00 CT
  open and CME Submission **23-017** gives trade date Monday 2023-02-06, unconditional, in
  session language: "CME Globex: Sunday - Friday 5:00 p.m. - 3:00 p.m. CPT"). Sunday–Friday
  17:00→15:00 CT; the 15:00–17:00 CT daily gap is 2h and therefore **`Maintenance`** under
  the crate's inter-trade-date rule. Corroborated on the TAS product page at 2023-03-14,
  2024-04-18, 2025-04-20, 2026-02-09 and on BTC's ContractSpecs at 2023-12-08, 2024-09-29,
  2025-02-21, 2025-10-28.
- **Row 2 — a one-day bridge at 2026-05-29, then the steady state at 2026-05-30**
  [**verdict D3**, and this is the shape the gate got wrong]. A single day-level row at
  2026-05-29 carrying the steady-state 24/7 grid would assert the book was open from
  Friday local midnight and would rewrite the era-1 Thursday-17:00→Friday-15:00 leg as a
  Friday-midnight open — precisely the running session LAW-NO-FABRICATED-DATES says a
  day-level boundary must not split. And LAW-HOLIDAY-SCOPE does **not** cover a migration's
  first day: that is a real, sourced, persistent change to the recurring week that arrives
  mid-day. **Follow `cryptocurrency.rs` exactly**, which carries
  `(2026,5,29,&TRANSITION_2026_05_29,…)` then `(2026,5,30,&CURRENT,…)` with the comment
  "Keeping this one-day bridge prevents the historical Thursday open from being rewritten
  as Friday midnight." The bridge row keeps the Thursday leg and withholds the unsourced
  Friday-afternoon reopen.
- **Steady state from 2026-05-30:** 24/7 with Saturday 02:00–04:00 CT closed and
  Monday–Friday 15:00–15:05 CT closed (Close 15:00, Pause, Pre-open 15:01:30, No-cancel,
  Open 15:05). Sources: client-systems wiki page 1283194884 v40, saved **2026-05-22, before
  the event** (v46 identical); the TAS product page captured 2026-06-10, listing all eight
  roots; BTC's ContractSpecs live.
- **`order_entry` in the steady state is sourced and must not be dropped** [**verdict
  D4**]: the same wiki table states "Pre-open: 3:01:30 p.m. to 3:04:30 p.m. CT / No cancel:
  3:04:30 p.m. to 3:05:00 p.m. CT" on Monday–Friday and "Pre-open: 3:45:30 a.m. to
  3:59:30 a.m. CT / No cancel: 3:59:30 a.m. to 4:00:00 a.m. CT" on Saturday.
  `cryptocurrency.rs` encodes the analogous Saturday 03:45 phase for the futures key from
  the same channel. Encode both, or say explicitly beside the table that they were
  withheld and why — the defect to avoid is the false "nothing sourced" impression.
- **Source conflict — serve the intersection and record it.** The wiki alone adds "Pause:
  4:01:00 p.m. to 4:02:00 p.m. CT"; the product page and ContractSpecs both omit it, so it
  is two silent channels against one. Serve the agreed window — open 15:05 → 15:00 next
  day, closed 15:00–15:05 and Saturday 02:00–04:00 — and **withhold the disputed
  16:01–16:02 minute by serving it closed**. Write the instruction once, in that form; the
  gate's own prose states it twice in a self-contradictory order [verified residual]. Same
  shape as `ECBTC`, so cite `bitcoin_event_contracts.rs`.
- **What U-15 actually established, and it is a negative worth recording:** there is no
  companion filing. CME 26-114 has no "TAS" string; **neither SER-9740 (13 May 2026) nor
  SER-9740R (28 May 2026)** — the SERs 26-114 itself promises — contains "TAS", despite a
  ~70-row Table 1 reaching down to Friday weekly options on Micro XRP; and ten weekly
  Globex notices across the migration never say "TAS" either. The wiki plus the two product
  channels are the operator's only statements. Say so, so nobody re-runs the sweep.
- **Member listings are caller catalog data, not rows:** TET/TEM 2025-03-17; TSL/TMS
  announced for 2025-10-13 then re-announced for 2025-12-15; TXP/TMX 2025-12-15. All but
  one carry a "pending" clause and the one that does not was contradicted by CME twice.
  The knowledge boundary that matters — all eight roots under one hours cell — is closed by
  the 2026-02-09 and 2026-06-10 product-page captures.
- **Do not reuse `globex_cryptocurrency` in either era**: 17:00→15:00 then a 15:00–15:05
  roll, against that key's 17:00→16:00 then a 16:00–16:02 roll.
- **Check whether this key needs `joins_adjacent_same_kind`** in
  `src/calendar/query/identity.rs`. The steady-state weekend block is continuous across
  Saturday and Sunday and is stored as adjacent pieces, exactly as for
  `GlobexCryptocurrency` and `GlobexEventContractsBtc`. If it does, it likely also needs the
  following-open-business-date trade-date branch in `assign_normal`. Decide from the
  weekend probe, and test the joined bounds across **both** DST transitions, as PR #60 was
  amended to do.

**Documentation debt:** `GlobexCryptocurrency` mentions TAS in neither `futures_profile.rs`
nor `verification.md` (handoff §5). Add the exclusion to both.

**Ledger:** Partial, `Gap: executable` — the steady-state weekday window is the sourced
intersection of three CME channels that disagree about one minute, and the era boundary's
first-day reopen is withheld.

---

### PR 5 — Energy and gasoil TAS

**Keys (2):** `globex_energy_tas` (CLT, HOT, RBT, BZT, BBT, NGT, NNT, HHT — and MCT if
D-6 is accepted), `globex_gasoil_tas` (7FT).
**Module:** `src/calendar/schedules/futures/us/energy_tas.rs`.

`tz: US::Central`. Every era is stated by CME in ET and/or CT at a fixed one-hour offset;
there is **no** cross-zone problem in either family.

**`globex_energy_tas`**

- **Era 1 — carried back to the January-2010 audit floor, no cutover asserted.**
  Sunday–Thursday 17:00 CT → next day 13:30 CT; Friday close 13:30 CT; no Friday-evening
  reopen. `order_entry` Sunday 16:15–17:00, Monday–Thursday 16:45–17:00. Sources:
  **RA1006-4** (advisory 2010-10-22) "No-Activity Periods: 2:30 p.m. - 5:45 p.m. (ET)
  Monday-Thursday / 2:30 p.m. (ET) Friday - 5:15 p.m. (ET) Sunday" for CLT, BZT, BBT, HOT,
  NGT, NNT, RBT, reprinted unchanged in RA1101-4 and RA1102-4; the **17:00 CT open** comes
  from CME's own `trading_hours/energy-hours.html` ("18:00-14:30 ET (17:00-13:30 CT)"),
  which no MRAN edition states. Carry-back warrant: AGENTS.md "Carry the earliest sourced
  state back to the audit floor".
- **Do not open a 2010 revision row, and do not use the handoff's 2010-10-25.** RA1006-4
  moves the TAS half to "Effective Date November 1, 2010 (TAS Changes) / The prohibition
  will become effective on Sunday, October 31 for trade date November 1, 2010", and what
  became effective is an **order-entry prohibition** ("Market participants are prohibited
  from initiating the entry of any TAS order into Globex prior to receipt of the security
  status message"), which LAW-SESSION-NOT-EXPIRY expressly excludes from session evidence.
  The No-Activity table is labelled "provided solely for informational purposes" — it
  *states* the session, it does not say the session changed that day. And the
  pre-amendment Rule 524.A.2 permission clause, whose own redline shows CME correcting
  "available for trading" to "available for TAS trading", is a wording clarification;
  reading it as "the TAS session was the full `globex_energy` envelope until 2010-11-01"
  would mint a session change out of a rule-text edit. **Carry the state back and record
  that residual risk beside the table.**
- **Era 2 — keyed 2011-04-10** (Sunday opening day; **RA1104-4**: "Effective on Sunday,
  April 10, 2011, for trade date Monday, April 11, 2011, the pre-opening times for TAS
  trading on CME Globex will be as follows (all times are in Eastern Time)"). Executable
  window **unchanged**. `order_entry` Sunday 16:17–17:00, Monday–Thursday 16:47–17:00 —
  the narrowest value across the whole undated span, because the family splits three ways
  (BZT/BBT/NNT 5:45/5:15 p.m. ET; CLT/HOT/RBT 5:46/5:16; NGT 5:47/5:17) and the reversal to
  a flat 16:45/16:00 CT is **undated** (a 16:45–16:46 range at 2013-01-16, flat at
  2015-03-22 and today, randomised today per RA2302-5). **Withhold Sunday 16:00–16:17**,
  exactly as the metals rows withhold 16:00–16:15. See decision **D-5** for the
  single-era alternative.
- **No further dated change exists.** RA1106-4 (eff. 2011-07-11) is the first edition to
  drop the clock table; RA1107-4/RA1108-4, RA1203-4R, **RA1323-4** (advisory 2013-11-01,
  effective 2013-11-18 — fetched, negative, add it to the exhausted list [U-6 verdict D7])
  , RA1303-4 and RA2302-5 state no per-product times. Globex Notice 2015-08-17 (stated day
  **Monday 2015-09-21** [verdict D4]) moved the energy *outright* close 16:15→16:00 CT and
  did not touch TAS: the 2015-03-22 capture and today's ContractSpecs both read 13:30 CT.

**`globex_gasoil_tas`** — separate key because its close differs from `globex_energy_tas`
in every sourced era.

- **Era 1 — carried back to the floor**: Sunday–Thursday 17:00 CT → next day **11:00 CT**
  (12:00 p.m. ET); Friday close 11:00. `order_entry` Sunday 16:15–17:00, Monday–Thursday
  16:45–17:00. Sources: RA1006-4's "7FT European Gasoil (ICE) … No-Activity Periods: 12:00
  p.m.-5:45 p.m. (ET) Monday-Thursday / 12:00 p.m. (ET) Friday-5:15 p.m. (ET) Sunday",
  unchanged in RA1101-4, RA1102-4 and RA1104-4 (7FT falls under "all other TAS-eligible
  products … will continue to be 5:45 p.m. ET Monday through Thursday and 5:15 p.m. ET on
  Sunday"), independently reconfirmed six years later by the 2016-12-19 notice's
  "Currently, the trading session closes daily at 12:00 p.m. ET".
- **Era 2 — keyed 2017-01-08** (Sunday opening day; CME Globex Notice 2016-12-19:
  "Effective Sunday, January 8 (trade date Monday, January 9), the trading hours for the
  European Low Sulphur Gasoil (100mt) Bullet Futures Trade at Settlement (TAS) cease daily
  at 11:30 a.m. Eastern time (ET)"). Close **10:30 CT**. `order_entry` unchanged — **era 2
  of this key does NOT inherit the 16:17/16:47 intersection**, because RA1104-4 left 7FT on
  the unstaggered value and no source states a gasoil pre-open change. Corroborated on
  CME's own 7F spec page at 2017-03-30 and 2017-11-29 ("Trading in all TAS products will
  cease daily at 11:30 Standard Time (EST)").
- **Source conflict to record beside the table.** From the 2019-11-16 page rebuild onward,
  and on the live ContractSpecs for productId 2912 today, CME prints for 7F "TAS: Sunday -
  Friday 6:00 p.m. - 2:30 p.m. (5:00 p.m. - 1:30 p.m. CT)" — the shared energy-TAS string,
  byte-identical to CL's. Serve the sourced intersection 17:00 → 10:30 CT and withhold
  10:30–13:30 CT. The same page printed a demonstrably wrong generic TAS time *before* the
  change too ("2:30 PM Eastern Time" at 2016-09-25, when both RA1006-4 and the notice say
  12:00 p.m. ET), so the boilerplate is unreliable on both sides and the dated notice
  controls. **[verdict D8]** Both gasoil eras take their 17:00 open from that same rejected
  cell; that is correct under "prefer the sourced intersection to omission", but **say that
  is what you are doing** rather than letting it pass unremarked.

**The `regular: &[]` trap, specific to this PR.** On the archived `energy-hours.html` the
TAS rows carry a "09:00-14:30 ET (08:00-13:30 CT)" column. That is the **open-outcry**
column — TAS was pit-eligible under NYMEX/COMEX Rule 524.A.1 from 2009-09-14 (RA0907-4)
until a 2015-03-06..2016-08-09 bracket — and RA1006-4 separately says "Regular trading
hours for open outcry trading in the Copper futures pit are from 8:10 a.m. until 1:00 p.m.
Eastern Time". It is **not** a Globex RTH. The adjudication that makes `regular: &[]` right
anyway: CME lists the pit route by the **underlying's** product code under "Pit-Traded
Contracts" (CL, HO, NG, RB, BZ, 7F, GC, SI — no TAS code) and the electronic route by the
**TAS root's own** Globex commodity code under "CME Globex Contracts" (CLT, BZT, BBT, HOT,
RBT, NGT, …). The pit route was a pricing convention inside the underlying's pit; this
crate keys the Globex TAS instrument, and `energy_metals.rs` already ships `regular: &[]`
for the NYMEX/COMEX outrights in every era, so no NYMEX pit is modelled as regular
anywhere. **Write this into the module comment.**

**U-0a and U-0b:**

- **`HHT` is closed and joins the key.** CME's ContractSpecs for Henry Hub Look-Alike Last
  Day Financial (productId 2752) names `ProductCode.TAS = "HHT"` and states "TAS: Sunday -
  Friday 6:00 p.m. - 2:30 p.m. (5:00 p.m. - 1:30 p.m. CT)"; HHT also appears as a Globex
  TAS contract in RA0907-4 (2009-08-31), before the floor. **Membership caveat for the
  comment:** HHT is absent from every 2010-2011 MRAN per-root table, so its TAS
  eligibility lapses and returns — catalog data, not a family-schedule fact.
- **`MCT` narrows only.** No CME document states MCT hours; MCL's ContractSpecs (productId
  10037) names MCT as its TAS code but, uniquely among CL/HO/RB/BZ/NG/HH, its Globex hours
  row carries **no** TAS line. CME Globex Notice 2022-07-18 tabulates "Micro Crude Oil TAS
  | MCT | CT | 382" under "iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group",
  placing MCT in group **CT**. **[verdict D5] Source the group-identity argument on `BZT`,
  not `CLT`**: no retrieved artifact states CLT's group (the only CL row held returns
  groupCode "CL", the *outright* group), while Globex Notice 2016-12-19 prints "Brent Last
  Day Financial Futures TAS | BZT | CT" under the identical header, and BZT is a proposed
  root of this key. See decision **D-6**.

**Corrections to fold in [U-6 verdict]:** strike "matches RA1104-4 to the minute" and
record the **BZT/RET pre-open conflict** (RA1104-4 puts both at 5:45/5:15 p.m. ET inside
"all other TAS-eligible products", while CME's own hours page seven months later prints
17:46/17:16 ET for both) beside the table — the zone pillar survives whatever the minutes,
and NGT's 16:47 remains the narrowest value, but the conflict is real and unrecorded [D1].
Correct the `energy-hours.html` CDX record: 60 rows were fetched under `&limit=60`, 74
exist, the last surviving **content** capture is 2015-03-23 (byte-identical to 2015-03-22)
and every later capture is a stub, a 301 or CME's 404 shell [D2]. Record **RA1003-4**
(advisory 2010-04-12, the Rule 524 edition in force through the first nine and a half
months of the floor year) as an **open channel** with the routes already tried, not as
silence — mitigating and worth stating: RA1005-4's own words, "The revisions address 1)
the time period during which TAS orders in TAS-eligible products may be entered on CME
Globex", indicate the prescribed pre-open period was *introduced* by RA1005-4, so RA1003-4
most likely carried no clock table [D3].

**Ledger:** two rows, Partial. `globex_energy_tas` — `Gap: order-entry` (the executable
window is unbroken and sourced from the floor to today; what is intersected is the queue
onset). `globex_gasoil_tas` — `Gap: executable` (the live spec channel disputes the close
and 10:30–13:30 CT is withheld).

---

### PR 6 — Commodity-index cash families

**Keys (3):** `globex_bloomberg_commodity_index`, `globex_ftse_crb_index`,
`globex_housing_index`.
**Module:** `src/calendar/schedules/futures/us/us_index_products.rs`.

These are ordinary outrights, not trade types: following the `globex_livestock`
precedent, **`regular` takes the whole published Globex window, `extended` is empty, and
queues are `order_entry`**.

- **`globex_bloomberg_commodity_index`** — AW (productId 333, group AW) plus BAG (10209/7A),
  BPE (10211/7H), BEN (10213/7E), BGR (10215/7G), BME (10217/7M), BLI (10219/7L), BPR
  (10221/7R). **One era, carried back to the January-2010 floor, no revision row
  anywhere**: `regular` Monday–Friday 08:15–13:30 CT; `order_entry` Sunday 16:15 → Monday
  08:15 and Monday–Thursday 16:45 → next 08:15; **no Friday-evening queue** (CME's feed
  publishes none). The boundary is the floor and **not** the 2015 rename: CME's own
  trading-hours page states the same 08:15–13:30 CT window under the name "Dow Jones-UBS
  Commodity Index" at a capture dated **2010-02-23** — seven weeks after the floor, in
  scope — and the specification page states it with "Symbols Clearing=70 Globex=AW" from
  2010-08-22, so the family appears in an in-scope source under its own Globex code and
  nothing is carried through the rename. The seven subindices join AW's existing grid on
  trade date 2025-03-31 (CBOT 25-093): **member listing, not a revision.**
  **Doc must exclude** AWT/BAT/BET/BGT/BLT/BMT/BPT/BST (see PR 1's rejection) **and DRS**.
  **[verdict D4]** The "Monday - Friday 4:45 p.m." wording belongs to CME 25-215 (the CCI
  filing), not to 25-093, whose pre-open line carries no day range at all — attribute it
  correctly. See decision **D-7c** for the queue end.
- **`globex_ftse_crb_index`** — CCI (11180, group FW), CME Chapter 414. **Separate key from
  BCOM** on identity, not on hours: XCME/CME 414 against XCBT/CBOT 29, and a different
  Globex group, so a divergence is a one-line edit (AGENTS.md: a venue that merely
  coincides still gets its own named profile). Pre-launch closure, then **keyed
  2025-07-21** — CME Submission **25-215**, "effective on Sunday, July 20, 2025, for trade
  date Monday, July 21, 2025"; keyed to the trade date because the first session opens
  Monday morning and there is no Sunday-evening leg to split. `regular` Monday–Friday
  08:15–13:30 CT; `order_entry` Sunday 17:00 → Monday 08:15 and Monday–Thursday 16:45 →
  next 08:15. **[verdict D5]** 25-215's pre-open line says "Monday - Friday 4:45 p.m. -
  8:15 a.m." while CME's own service publishes no Friday-evening pre-open for CCI: add the
  Friday-evening queue to the **withheld** list for this key *and* for BCOM.
- **`globex_housing_index`** — eleven roots on one Globex group HI: CUS 802, BOS 800, CHI
  801, DEN 803, LAV 804, LAX 805, MIA 806, NYM 807, SDG 808, SFR 809, WDC 1213 (CME
  chapters 419/420).
  - **Era A, carried back to the floor**: `regular` Sunday–Thursday 17:00 → 14:00 next day
    (five trade dates Mon–Fri); `order_entry` Sunday 16:15, Monday–Thursday 16:45.
  - **Era B, keyed 2013-09-03**: `regular` Monday–Friday 08:15–15:00 CT; `order_entry`
    Monday–Friday 08:00–08:15. Unchanged to today.
  - **U-9 is resolved:** the issued **SER-6805** (Notice Date 2013-08-27, Effective Date
    2013-09-03) states one unconditional day in session language and settles Submission
    13-344's self-contradiction — the letter body's "trade day, Tuesday, September 3, 2013"
    is right and the embedded appendix's "Monday, September 2, 2013" is a draft
    ("Special Executive Report S-XXX / August XX") that was never issued and named US Labor
    Day. CME's own specification channel brackets it independently (2013-04-12 still Era A,
    2013-09-10 already Era B). The two other leads are non-events and should be recorded as
    such: CME #12-060 (2012-03-08) adds Globex for housing *options* and says the futures
    were "already trading on CME Globex" on an unchanged schedule; Submission 17-001
    (2017-01-20) adds ClearPort only, and its value is the authoritative eleven-code
    membership list.
  - **Keyed 2013-09-03, not 2013-09-02**, because a row that *narrows* an overnight open
    keeps its artifact's own date. **[residual C5]** That leaves Monday 2013-09-02
    17:00–24:00 CT served by Era A as open when no session ran, and a closed date cannot
    remove it (that evening leg carries trade date Tuesday 2013-09-03, which did trade
    under Era B). Label this an **executable-phase residual** — the serious kind — beside
    the row. The alternative key, 2013-09-02, is worse: it would split the genuine
    Sunday-evening→Monday session.
  - **[residual C1]** Era A's Sunday leg has a primary that omits it: `housing-spec`
    2013-04-12 reads "CME Globex (Electronic Platform) Mon/Thurs 5:00 p.m.-2:00 p.m. CT the
    next day" with no Sunday. The Sunday leg is sourced by the 2010-11-10 fact card
    ("Sundays through Thursdays") and, post-floor and decisively, by the 2011-10-29 hours
    page's separate Sunday column (pre-open 16:15, electronic 17:00-14:00). Serving Sun–Thu
    is right; **record the 2013 spec's omission beside the row.** **[residual C2]** The fact
    card is undated and its worked example cites 2006 index values, so its capture dates the
    observation, not the state; for the futures-pit absence use Submission **17-001**
    instead, whose Current-Venues column gives the 419/420 futures rows "CME Globex" and the
    419A/420A options rows "CME Globex …, Trading Floor".
  - **[residual C8]** CME's two channels disagree on productId 802's name — ContractSpecs
    "CME Composite Housing Index Futures", the trading-hours service "CME Metro Area Housing
    Index Futures" — both on group HI with the same grid. One sentence beside the eleven-root
    list.

**Ledger:** BCOM — Partial, `Gap: order-entry` (the weekday queue end is narrowed against
25-093 and the Friday-evening queue is withheld). CCI — Partial, `Gap: order-entry` (same
Friday-evening narrowing). Housing — Partial, `Gap: executable` (the 2013-09-02 evening
residual).

---

### PR 7 — Dairy, lumber, southern yellow pine

**Keys (3):** `globex_dairy`, `globex_lumber`, `globex_southern_yellow_pine`.
**Modules:** `src/calendar/schedules/futures/us/dairy.rs` and
`src/calendar/schedules/futures/us/lumber.rs` (LBR and SYP share one grid and one Globex
group; two keys in one module).

- **`globex_dairy`** — DC 27, CSC 5201, GDK 778 (group DC); CB 26 (group CB); DY 36, GNF
  781 (group DY). Three groups, one grid, day for day. **Excludes JQ (1709) on evidence.**
  U-0c is closed: all six roots re-fetch live, so "only Class III Milk is independently
  confirmed" no longer holds.
  - **One era, carried back to the floor, no revision.** **Five daily sessions, not one
    weekly session with a halt**: Sun 17:00→Mon 16:00, Mon 17:00→Tue 16:00, Tue→Wed,
    Wed→Thu, Thu 17:00→Fri 13:55. Five trade dates. The 16:00→17:00 gaps are one hour and
    therefore **`Maintenance`**; Friday 13:55 → Sunday 17:00 is **`Closed`**. `order_entry`
    Sunday 16:15→17:00 and Monday–Thursday 16:45→17:00. Following `globex_livestock`,
    `regular` takes the whole Globex envelope, `extended` is empty, and the pit is not
    modelled.
  - **The five-closes shape is CME's own distinction, not an inference:** the feed emits
    `closed` at 16:00 carrying that day's trading date and then `preopen`/`open` carrying
    the next one, and the same feed writes `paused` rather than `closed` for SAS and CVB at
    13:20.
  - **The pre-floor notices make the carry-back evidenced rather than assumed:** #09-236
    (effective 2009-11-15) dates the Sunday 17:00 open and names five of the six roots;
    Q2008-215 (effective 2008-10-24) dates the Friday 13:55 close; the 2007-03-07 press
    release is the origin of the 16:00–17:00 daily break.
  - **[verdict D1 — fix before writing any citation]** The claimed **2025-08-11** Wayback
    capture of ContractSpecs productId 27 **does not exist**: that URL 302s to the
    2026-08-10 capture and the CDX lists exactly one capture, `20260810165630`. One capture
    was saved three times under two dates. Strike the 2025-08-11 citation, restate the
    bridge as "archived capture 2026-08-10 plus the live fetch", and **state the real
    carried, unwitnessed span, 2021-04-20 → 2026-08-10 (five years four months)**, beside
    the table. This is the same 2025-08-11 timestamp family the handoff already flagged as
    not resolving (U-11 / U-0c).
  - **[residual C6] Cite the corroboration already on disk and not used**, which makes the
    dairy case markedly stronger and narrows the queue side of that gap:
    `wb_trading_hours_20120511_commodities.html` gives per-product dairy rows "Class III
    Milk Futures | 16:15 | 17:00-16:00 | 16:45 | 17:00-13:55 | 09:05-13:10" (same for Class
    IV/Nonfat, Dry Whey, Cash-Settled Butter and Cheese), and `th_20141030` and
    `th_20150405` give "| 16:00 | 17:00-16:00 | 16:45 | Mon-Thurs: 17:00-16:00 Fri:
    17:00-13:55 | 09:05-13:10". These state the five-daily-session shape, the 16:45 weekday
    queue and the 16:15→16:00 Sunday move explicitly, in scope, for all six roots.
    **[residual D6]** Quote the 2010-02-23 row with its real cell boundaries — the Sunday
    cell is separate from the pre-open cell.
  - **The pit sub-item is answered, not retrieved, and no closure day is needed**: the
    open-outcry row ("MON-FRI: 9:05 a.m. - 1:10 p.m.") is present through the 2015-03-26
    capture and gone by 2015-09-05, and `globex_dairy` is Globex-scoped.
- **`globex_lumber`** — LBR (10191, group LU), CME Chapter 63, `SettlementMethod:
  Deliverable`. Pre-launch closure, then **keyed 2022-08-08** — CME Submission 22-248,
  "effective Sunday, August 7, 2022 for trade date Monday, August 8, 2022"; the grid has no
  Sunday leg, so the trade date is the opening day. `regular` Monday–Friday 09:00–15:05 CT;
  `order_entry` Monday–Friday 06:00–09:00 CT. ContractSpecs 10191 (2026-06-20) still
  identical. **The filing's own reference to "CME's existing lumber futures" forbids
  carrying legacy Random Length Lumber history into this key** — say so.
- **`globex_southern_yellow_pine`** — SYP (11073, group **LU**, the same Globex group as
  LBR), CME Chapter 64, financially settled. Pre-launch closure, then **keyed 2025-03-31**;
  `regular` Monday–Friday 09:00–15:05 CT; `order_entry` Monday–Friday 06:00–09:00 CT
  carried back from the capture.
  - **Two keys on one identical grid, deliberately.** One Globex group cannot run two
    grids, so SYP's grid is LBR's; the family question is the reason for the split — CME 63
    / deliverable against CME 64 / financially settled.
  - **Submission 25-082's hours table is a known-erroneous pasted template, not an open
    conflict**: it prints Sunday 17:00 – Friday 16:00 CT and says "Tuesday – Thursday"
    where CME's window is Mon–Thu. **[residual C4]** The defect is broader than the gate
    states — its ClearPort line reads "Sunday 5:00 p.m. - Friday 4:00 p.m. CT with no
    reporting Tuesday - Thursday from 4:00 p.m. - 5:00 p.m. CT", which also departs from
    CME's ClearPort template, so the **whole cell** is the pasted template. That strengthens
    the known-erroneous verdict; record it that way. The launch day comes from the SYP FAQ,
    which states it in the future tense four days before (capture 2025-03-27) and in the
    past tense a year later (capture 2026-05-21), with 25-082 agreeing.
  - SYP's 06:00–09:00 queue is served where the intersection with 25-082 is **empty**
    (25-082 gives Sunday 16:00–17:00 and "Tuesday – Thursday" 16:45–17:00). Record that in
    the withheld list.

**Ledger:** dairy — Partial, `Gap: executable` (a five-year unwitnessed carried span).
lumber — Primary if nothing is withheld; SYP — Partial, `Gap: order-entry` (the queue is
served against a defective filing).

---

### PR 8 — Santos soybeans, urea, Black Sea wheat

**Keys (3):** `globex_santos_soybeans`, `globex_urea_10_ton`,
`globex_black_sea_wheat_cvb`.
**Module:** `src/calendar/schedules/futures/us/cbot_standalone_ag.rs`.

- **`globex_santos_soybeans`** — SAS (8947, group AS). Pre-launch closure, then **keyed
  2020-09-21** — CBOT Submission 20-347, "effective on Sunday, September 20, 2020 for trade
  date Monday, September 21, 2020". `regular` Monday–Friday 08:30–13:20 CT; `order_entry`
  Monday–Friday 08:00–08:30 and Monday–Friday 14:30–16:00 (the modified pre-open).
  **Not `globex_grains`** — and the discriminator is not the coinciding day session, it is
  that SAS has **no overnight leg at all**. **[verdict D2]** The archived ContractSpecs
  citation must carry its query string
  (`.../productId/8947?isProtected&_t=1716050714530`); without it the URL 404s.
- **`globex_urea_10_ton`** — MFV (11100, group UA), CBOT chapters 48/48A. Pre-launch
  closure, then **keyed 2025-06-02** — CBOT Submission 25-177, "effective Sunday, June 1,
  2025, for trade date Monday, June 2, 2025". `regular` Monday–Friday 08:30–14:30 CT;
  `order_entry` Monday–Friday 08:00–08:30. **Doc must exclude UFV/UFB/UFE**, or a caller
  will mis-map "urea".
  **U-10 is resolved from the bytes on three independent legs and no launch SER is
  needed:** (1) 25-177's own hours cell states a pre-open "Monday through Friday 8:00 a.m.
  - 8:30 a.m. CT", and a daily pre-open presupposes a daily open, so "CME Globex: Monday
  8:30 a.m. – Friday 2:30 p.m. CT" in the line below cannot be a continuous week and is a
  mis-rendering of "Monday - Friday 8:30 a.m. - 2:30 p.m. CT"; (2) CME's live product
  specification reads "Monday - Friday 8:30 a.m. - 2:30 p.m. / Pre-Open 8:00 a.m."; (3)
  CME's session feed publishes five separate `preopen@08:00` / `open@08:30` / `closed@14:30`
  CT days with no overnight or weekend event.
- **`globex_black_sea_wheat_cvb`** — CVB (11102, group BW), CBOT chapters 14Y/14Z. **Two
  fully dated eras.** Cannot reuse `globex_grains`, with which it coincided on the day
  session until it diverged on a dated day.
  - **Era 1, keyed 2025-06-01** (Sunday, the local opening day of the first session it
    governs; CBOT Submission 25-103, effective trade date 2025-06-02): `regular`
    Monday–Friday 08:30–13:20 CT; overnight leg Sunday–Friday 19:00–07:45 CT;
    `order_entry` Sunday 16:00–19:00, Monday–Thursday 16:45–19:00, Monday–Friday
    08:00–08:30. **[residual C7]** The 07:45→08:30 gap is **same-trade-date** and therefore
    **`Halt`** — classify it explicitly.
  - **Era 2, keyed 2026-08-02** (Sunday, same rule — the row *lengthens* a wrapping
    overnight session, so it must not be keyed to the trade date; CBOT Submission 26-234,
    effective trade date 2026-08-03): one continuous leg Sunday–Friday 19:00 → 13:20 CT;
    `order_entry` Sunday 16:00–19:00 and Monday–Thursday 16:45–19:00; the morning queue
    dropped. 26-234's "Current" column independently reproduces Era 1.
  - See decision **D-7a** for era 1's regular/extended split.

**Ledger:** SAS — Primary if nothing is withheld. MFV — Partial or Primary depending on how
the filing's mis-rendering is recorded (the grid itself is triply sourced; recommend
Primary with the mis-rendering recorded as a document defect, not a gap). CVB — Primary,
two dated eras with nothing withheld.

---

### PR 9 — Equity, commodity-index and credit BTIC

**Keys (3):** `globex_equity_index_btic`, `globex_commodity_index_btic`,
`globex_credit_index_btic`. All three are **single-zone `America/Chicago` at both
endpoints — U-8 does not reach them**, because `America/New_York` shares Chicago's DST
calendar, so a constant −1h offset is exactly representable. **Do not spend the
cross-zone mechanism here.**
**Module:** `src/calendar/schedules/futures/us/equity_index_btic.rs` (equity) and
`src/calendar/schedules/futures/us/index_btic.rs` (commodity-index and credit).

- **`globex_equity_index_btic`** — EST, NQT, YMT, EMT, IPT, RVT, R1T, RGT, RLT, ART, plus
  the eleven 18-070 sector roots (XYT, XPT, XET, XFT, XVT, XIT, XBT, XKT, XUT, XRT, BIT)
  and the handoff's remaining row-2 roots on their own citations.
  - **Pre-launch closure, then ONE era keyed 2015-11-15** (Sunday, the local opening day;
    CME Submission 15-438 and CBOT Submission 15-437, both 2015-10-28, each state
    "effective on Sunday, November 15, 2015 for trade date Monday, November 16, 2015" with
    no condition). Before that day the family did not exist: **encode a pre-launch closure,
    do not carry the grid back to the floor.** The 2015 New Product Summary cannot supply
    the day on its own — its footer reads "Pending All Relevant CFTC Regulatory Review
    Periods".
  - **Grid:** Sunday open 17:00 CT wrapping to a 15:00 CT close on Monday's trade date;
    Monday–Thursday reopen 17:00 → 15:00; final weekly close Friday 15:00 CT. The daily
    15:00→17:00 CT gap is two hours and therefore **`Maintenance`**. Weekend Friday 15:00 →
    Sunday 17:00 is **`Closed`**. Note for the comment: CME's prose calls only 16:00–17:00
    CT the "daily maintenance period" — that phrase is the platform-wide window carried into
    the BTIC sentence; the book is simply closed 15:00–16:00 as well, and nothing turns on
    it because the whole gap classifies the same way.
  - **`order_entry`** Sunday 16:00–17:00, Monday–Thursday 16:45–17:00 — **from the session
    service only**, with no archived history and no CME prose, carried back to 2015-11-15
    with no cutover asserted. Permissible, but **the row must say so** [verified residual].
  - **NO 15:15–15:30 CT halt in any era, and NO 2021-06-27/28 revision row.** Structurally,
    the halt ran 15:15–15:30 and the BTIC book closed at 15:00 from its first day — a halt
    cannot fall inside a session that has already ended. Documentarily at launch, the
    2015-11-15 capture attaches the halt clause to the CME Globex **outright** line only and
    the adjacent BTIC sentence carries none (same in 2016-02-01, 2018-04-19, 2019-01-30).
    Documentarily at removal, CME Globex Notice 2021-06-21's linked affected-product list
    enumerates tag-1151 security groups (ES, NQ, YM, IX, RV, ME, XB, XR, …) and contains
    **no** BTIC group — SB, NB, DB, R3, IT, PB, R1, R2 and RT are all absent. SER-8788
    states the change but is conditional and names no product code; it does supply the
    rationale that settles the question — "The halt was initially implemented to account for
    transactions conducted via open outcry in the trading pits and is therefore no longer
    necessary" — and a Globex-only trade type launched in 2015 never had a pit. So "all BTIC
    and TACO products will not be impacted" reads as "BTIC never had it", not "BTIC kept
    it". **The 2021-06-28 revision belongs to `globex_equity_index`, which already holds
    it, and must not be copied here.**
  - **U-1 is adjudicated in writing; carry the adjudication into the module comment.** CME
    publishes the 16:00 ET Globex BTIC close in three independent primary channels: the
    launch New Product Summary under the heading "Trading Hours"; CME's own server-rendered
    ES contract-specification page, captured on the launch Sunday 2015-11-15 and again
    2016-02-01, 2018-04-19 and 2019-01-30 ("For the BTIC, trading hours will be Sunday -
    Friday 6:00 p.m. - 4:00 p.m. New York time/ET (5:00 p.m. - 3:00 p.m. Chicago Time/CT)");
    and a CFTC Regulation 40.6(a) self-certification, CME Submission **18-070** (2 of 2,
    2018-03-08), under the explicit heading "Hours of BTIC trading on CME Globex:", with an
    unconditional day-level effective date (trade date 2018-03-26) and a table of sector
    BTIC codes. The session service (`closed@15:00` for SB, NB, DB, R3, IT, PB, R1, R2, RT
    against `closed@16:00` for ES and IX in the same response) is **corroboration, not the
    basis**. And LAW-SESSION-NOT-EXPIRY is clear: the 2018 page prints "BTIC trading
    terminates at 4:00 p.m. Eastern Time (ET) on the Thursday before the 3rd Friday of
    contract month" as a **separate** Termination-of-Trading row, and that row is not used.
  - **Source-conflict note that must sit beside the table** (the repo requires the conflict
    be recorded, not silently resolved): CME's live ContractSpecs prints, for productId 7968
    (EST) and 8027 (IPT), a single unlabelled `"venue":"Default:"` trading-hours row
    carrying the 18:00–17:00 ET envelope, and for productId 7948 (RSV) a
    `"venue":"CME Globex:"` row reading "BTIC: Sunday - Friday 6:00p.m. - 5:00 p.m. ET".
    The key serves 16:00 ET on the sourced intersection and on the venue-labelled
    statements; these three cells are the disputed remainder. **[verdict D4]** Describe the
    17:00 figure as **the generic ClearPort envelope**, not as "the ClearPort BTIC window" —
    CME's current ES record puts the *ClearPort BTIC* line at 16:00 ET too, and has since at
    least 2022-09-08. **[verdict D2]** The 8027/7969 cells are identical in wording and every
    time but are **not** byte-identical — under whitespace collapse they differ by one
    space. **[verdict D3]** The handoff's "productId 7948 (RSV)" is not an error to correct;
    it labels 7948 as RSV correctly. The genuinely new fact is that **RVT is productId 7949,
    security group R3, and has no ContractSpecs record at all** (as YMT/7970 does not) —
    record it as a fact, not as a correction. **[verdict D5]** 18-070's body says "twelve
    (12) equity index futures contracts" while its table enumerates eleven product rows;
    encode the eleven and record the document's own 12-vs-11 discrepancy so a later reader
    does not read it as a missing root. **[verdict D6]** CBOT Submission 25-546's "Start date
    is November 16, 2015" is the term of the BTIC **Market Maker Program**, not a listing
    date — several of the eleven products it scopes did not exist in 2015 — so it
    corroborates the family clock only by coincidence; the launch day comes from 15-438 /
    15-437.
  - **[verdict D1] Do not write that the modern channels have no archived history.** The
    BTIC *product* records (7968, 7969, 8027, 7949, 7970) and the session service have none
    and cannot be ordered in time; the *underlying* records the ruling relies on do —
    productId **133** is archived 2021-07-03 → 2026-04-05, **23 captures, 11 distinct
    digests**, every one carrying the venue-labelled "CME Globex: … BTIC: Sunday - Friday
    6:00 p.m. - 4:00 p.m. ET" line, and productId 166 once at 2021-07-10. Say it that way;
    AGENTS.md legislates this exact failure.
  - **U-2 and U-3 are closed on hours.** ART is productId 10040, group BV, and the
    time-aligned week puts BV, DH and PB all on this grid; its April-vs-August route drift is
    catalog data and **[verdict D11]** was *not* dated, so keep the undated route change as
    an open catalog note rather than calling U-2 fully resolved. EMT is productId 7596, group
    PB; its underlying EMD (166) prints "BTIC: Sunday - Friday 6:00 p.m. - 4:00 p.m. ET"
    live and in the 2021-07-10 archived capture, and the service returns group PB at
    `closed@15:00`.
  - **[verified residual]** The eleven sector BTIC roots from 18-070 were never probed in
    the session service and rest on the filing's prose alone — sufficient, but one-channel;
    record it.
  - **[verified residual] Channel caveat for the ledger:** the live ContractSpecs,
    product-slate and session-service quotations, the 2021 Globex notice, its
    affected-product PDF and SER-8788 were all read as text extracted by a public reader in
    front of the cited cmegroup.com URLs — the same weaker-channel caveat `sources.md`
    already records for `globex_event_contracts`. The four server-rendered spec captures came
    from `web.archive.org` `id_` replay and the four CFTC filings from a direct GET to
    cftc.gov; those carry no such caveat, and between them they carry the whole ruling.
  - **Do not encode CBOT 25-546's "8:30AM - 3:00PM (CT) (\"RTH\")" as a `regular` phase.**
    It is a market-maker **quoting obligation** inside an incentive program, not a statement
    that the market has an RTH/ETH split. Its coincidence with the family close is
    suggestive and nothing more. `regular: &[]` stands on U-4's channels.
- **`globex_commodity_index_btic`** — DRT (group LH), GDT (group GT), GIT (group GH):
  **three security groups, not one**, all on one identical grid. Pre-launch closure, then
  **one era keyed 2018-12-02** (Sunday, first session; trade date Monday 2018-12-03; CME/CBOT
  18-431 is the eligibility notification and states both the day and the hours, corroborated
  by Chadv18-443R's revised Globex hours, "no 5:00 p.m. session on Friday"). Sunday–Friday
  open 17:00 CT, close 13:30 CT; `order_entry` Sunday 16:00–17:00, Monday–Thursday
  16:45–17:00; **no Friday-evening reopen**.
  - **Assert NO 2023-03-12 revision.** SER-9138 (2023-02-14) and CME/CBOT 23-074 (2023-02-23)
    state a prior 17:00–16:00 CT Globex BTIC window and amend it to 17:00–13:30 CT effective
    trade date 2023-03-13, while **four** other CME documents spanning 2018–2021 say the
    window was already 17:00–13:30 CT. The SER's table has a second demonstrable error (its
    AW row), and the value it prints as "Current" is exactly the **ClearPort** BTIC window
    printed one line below the Globex one on the same spec pages. **[verdict D4]** The GSCI
    spec's bytes are *stronger* than the gate's quote: CME labels the venue inside the BTIC
    line itself — "Globex BTIC: Sunday - Friday 5:00 p.m. - 1:30 p.m. (6:00 p.m. - 2:30 p.m.
    ET)" and "ClearPort BTIC: Sunday - Friday 5:00 p.m. - 4:00 p.m. …" — as two labelled
    lines inside one merged Trading Hours cell. Quote them with their labels. Serve
    17:00→13:30 CT for the family's whole life, record the conflict beside the table, and
    **[verdict D6]** say the withheld span is **13:30–16:00 CT, two and a half hours**, not
    "an hour".
  - **Excludes** AWT/BAT/BET/BGT/BLT/BMT/BPT/BST/CCT (PR 1's rejection).
- **`globex_credit_index_btic`** — IQBT, HYBT, IQLT, IQYT, DLBT, DHBT, DHYT (group CG) and
  IQST (currently routed on the **outright** group CE). **Eight roots, not the handoff's
  six** — DHBT and DHYT are missing from that row. Pre-launch closure, then **one era keyed
  2024-09-15** (Sunday, first session; trade date Monday 2024-09-16; CBOT 24-328 for the
  day, ContractSpecs 10676/10677/11451/11459/11461/11463 for the 15:00 close, the service on
  group CG across a September week, the 2026-10-25..11-07 DST window and a January week).
  Sunday–Friday open 17:00 CT, close 15:00 CT; `order_entry` Sunday 16:00–17:00,
  Monday–Thursday 16:45–17:00; no Friday-evening reopen. **Single-zone — confirmed across
  the DST window.**
  - **Do NOT encode a 16:00–17:00 gap.** The ContractSpecs BTIC sentence "Sunday - Friday
    5:00 p.m. - 3:00 p.m. CT with a 60-minute break each day beginning at 4:00 p.m." is
    internally inconsistent — a book closed at 15:00 cannot break at 16:00 — and the break
    clause is boilerplate inherited from the outright line above it. **[verdict D7]** Only
    10677 (HYB) carries "CT" on the Globex BTIC line; 11459 and 11461 omit it, and the zone
    comes from the sibling line — do not normalise a zone label inside a verbatim.
  - **Conflict:** IQST (11460) sits on group CE, the credit **outright** group (IQB, IQS and
    IQL all sit there), and therefore publishes the outright's `closed@16:00` while its own
    spec says 15:00. Serve the intersection 17:00→15:00 CT, withhold IQST's 15:00–16:00
    hour, and treat its CE routing as per-root catalog data.
  - **Do not merge into `globex_equity_index_btic`** despite the identical envelope: CBOT
    segment-84 Bloomberg credit is a different family with a different launch day. One
    envelope is not one family.
  - Member listings, all caller catalog data: DHBT CBOT 24-423, first session 2024-12-15;
    DLBT CBOT/CME 26-064, first session 2026-03-29; IQST/IQYT/IQLT CBOT 26-087 (2026-02-26)
    — **[verdict D8]** the PDF lives at `/rule-filings/2026/2/26-087.pdf`, and the retrieval
    trap is the **`_N` exhibit-suffix convention** (present on 18-431_1, 19-012_1, 22-220_1,
    23-015_1, 24-080_1 and absent on 24-263, 24-328, 25-061, 26-087), **not** zero-padding;
    record the right trap. DHYT is not separately dated.

**Ledger:** three rows, Partial. Equity BTIC — `Gap: order-entry` (the Pre-Opens are
feed-only and carried back). Commodity-index BTIC — `Gap: executable` (2.5 h withheld
against SER-9138). Credit BTIC — `Gap: executable` (IQST's hour withheld).

**Follow-ups:** the undated ART route change; the equity-BTIC RTH question (`globex_spot_quoted`'s
sourced-absence precedent and the Daily Bulletin RTH/ETH route both remain untried *for
BTIC specifically*, though U-4 answers it at class level); the crypto-BTIC keys this PR
does not author.

---

### PR 10 — TACO and TMAC

**Keys (2):** `globex_equity_index_taco` (ESQ/3T, NQQ/NT, RTQ/RE),
`globex_equity_index_tmac` (ESX/E2, NQX, RTX, YMX).
**Module:** `src/calendar/schedules/futures/us/equity_index_taco_tmac.rs`.
`tz: US::Central` throughout — every published instant is a CT clock time, so a single-tz
profile represents both exactly and **U-8 does not apply**.
**Blocked on decision D-3** (the "pending" clause), which fixes four of these dates.

**`globex_equity_index_taco`**

- **Era 1 — pre-launch closure, then keyed 2018-05-13** (Sunday; trade date Monday
  2018-05-14). Grid from CME Globex Notice 2018-05-07, SER-8124R Exhibit 1 and the
  client-systems wiki page "Basis Trade at Cash Open" v13, all in CT:
  - Sunday 16:00 pre-open (`order_entry`), 17:00 open → Monday 08:30 close; trade date
    Monday.
  - Monday–Thursday: 09:30 pre-open (`order_entry`), 10:00 open → 16:00; **halt**
    16:00–17:00 (CME's own words: "Market Halt … - Globex Maintenance Period"); 16:45
    pre-open (`order_entry`); 17:00 open → 08:30 next business day. Each such span is one
    trade date, the next business day.
  - Friday: **no day session.** Nothing between Friday 08:30 and Sunday 16:00.
  - Trade dates fall out of the generic convention with no exception needed in this era:
    every leg wraps and ends at 08:30 on its own trade date.
- **Era 2 — keyed 2021-09-26** (the stated effective Sunday; trade date Monday 2021-09-27).
  Identical to era 1 plus a Friday day leg: Friday 09:30 pre-open, 10:00 open → 16:00
  close — and the service marks this Friday 16:00 as `closed`, not `paused` as Mon–Thu
  16:00 is. No 16:45 pre-open and no 17:00 reopen on Friday. Weekend closed Friday 16:00 →
  Sunday 16:00 pre-open. **No Saturday phase.** The Monday–Thursday halt and evening leg are
  unchanged — CME expanded only the morning-close, pre-open and day-session lines to
  Monday–Friday. Keying at 2021-09-26 rather than at the first Friday it bites (2021-10-01)
  is unobservable, because the Sunday and weekday grids are unchanged between those dates,
  and the notice's own day should win.
  - **Sources — use 21-234 as the primary, which the gate missed [verdict D1].** CME
    **Clearing Advisory 21-234** (notice date 2021-07-01, effective date 2021-09-27)
    tabulates both grids side by side in one dated document: Current "TACO: Sunday - Friday
    6:00 p.m. - 9:30 a.m. ET. Monday - Thursday 11:00 a.m. - 5:00 p.m. ET." against Expanded
    "… Monday - Friday 11:00 a.m. - 5:00 p.m. ET." It also names the product codes the
    weekly notice does not: TACO ESQ (ch. 358), NQQ (ch. 359), RTQ (ch. 393); BTIC NKT (ch.
    352) and NIT (ch. 352B) **only**. Without it the era-2 grid rests on a wiki page whose
    own stamp (2021-10-11) is *after* the effective day plus the live feed — with it, the
    grid is operator-stated two and a half months before the event.
  - **[verdict D3]** The weekly Globex Notice carried the item "TACO and BTIC Amended
    Trading Schedule- September 26" in **thirteen consecutive issues**, 2021-06-28 through
    2021-09-20, always naming Sunday September 26 / trade date Monday September 27, never a
    different day. State it that way — three months of unchanged announcement with no
    slippage — not as three issues.
  - **[verdict D2]** A third independent channel brackets the change: the TACO marketing
    page's contract-specification block, whose Trading Hours row reads "For each trade day,
    trading starts at 10:00 a.m. CT the previous day, **except for a Monday trade date,
    which starts on Sunday at 5:00 p.m. CT**" in nine captures through 2021-10-22 and drops
    the exception clause from 2021-12-02 onward (still CME's current prose at 2026-02-13).
    This is the only retrieved CME prose that states in words what the change did to the
    **trade date**, and it is exactly the hardest part of encoding TACO. Cite it. Correct the
    gate's dead end, which said this page has no hours prose in any capture and that 13 of
    its 30 captures were the whole channel.
  - **[verdict D4]** The FIXP-postponement contrast is real but mis-cited: the word
    "postponed" appears in the 2021-09-06/13/20 notices (the same issues that carried the
    TACO item), not in the 2021-09-27/10-04/10-11 notices. State it in that corrected form.
- **The trade-date exception — the single hardest part of this PR, and the handoff does not
  flag it.** In era 2, trade date Monday has **two disjoint legs**: Friday 10:00–16:00 CT
  and Sunday 17:00 → Monday 08:30 CT, separated by a ~49-hour weekend. CME states the
  assignment in words ("Any order submitted on Friday after 10:00am (CT) will have a next
  business date of Monday") and in FIX (the Taco-Friday-Scenario diagram's tag
  75-TradeDate = the following Monday). The crate's generic convention — trade date = the
  venue-local date of a containing session's final close — puts the Friday leg on **Friday**,
  which is wrong. This needs a **sourced trade-date exception in
  `src/calendar/query/identity.rs`**, the same mechanism `globex_rough_rice` needed, and it
  is a harder instance: the two legs of one trade date are separated by a gap that is
  `Closed` (>4 h), so they must **not** coalesce into one session. Add the branch to
  `assign_normal`, leave `joins_adjacent_same_kind` alone, and test both legs' trade dates
  and the non-coalescence explicitly. **[verdict D7]** Do not use the diagram to date
  anything — its own labels are internally inconsistent (no year has June 25 on a Friday and
  June 27 on a Monday); use it only for the structure.
- **MUST STAY WITHHELD — 1: any Saturday session or Saturday phase.** The service's Saturday
  rows (`open@05:00`, `closed@17:00`) are withheld as a feed artifact, with the CME prose
  cited beside the table and the anomaly recorded. **State the residual risk plainly:
  nothing found EXPLAINS the 05:00/17:00 pair.** The argument is that it cannot be a
  session — invariant under the 2026-11-01 US DST end; unchanged after the early-close
  Friday 2026-11-27 (12:15 CT); still present after Friday 2026-12-25, a full holiday whose
  event list is empty (an "open" with nothing that opened it, and with no pre-open, unlike
  every other open in the group's week); byte-identical across two differently-anchored
  families; and confined, across 3,243 products, to exactly five roots (ESQ, NQQ, RTQ and
  the two Nikkei BTIC roots) which are precisely the population the 2021-09-26 "the trade
  date will not roll over on the weekend" change created. Against it stand **four** CME prose
  statements that the weekend is shut: SER-8124R Exhibit 1 ("Friday … No day session. Trading
  shall resume on Sunday evening."); the wiki, era 2 and still live ("No TACO orders will be
  persisted over the weekend. Clients must re-enter their Day/session orders for Monday trade
  date when we re-open Sunday for Monday's trade date."); the Taco-Friday-Scenario diagram,
  whose only markers are Friday, "Sunday Start" and Monday; and the marketing page's
  previous-day sentence [verdict D2]. The crypto complex's Saturday shape is a completely
  different, separately sourced triple (02:00 closed, 03:45 preopen, 04:00 open) on 265
  products, so "crypto-style maintenance" is dead.
- **MUST STAY WITHHELD — 2: the CME ClearPort TACO hours.** A distinct venue cell;
  submission-for-clearing rather than an order book; ES's copy still reads Monday–Thursday
  while NQ's and RTY's read Monday–Friday, verified live. One sentence in the doc comment so
  the next reader does not re-litigate it, and do **not** let ES's stale cell be read as a
  live dispute about the Globex grid.
- **MUST STAY WITHHELD — 3: any BTIC-side conclusion from the 2021-09 notice.** With 21-234
  in hand the BTIC half **is** scoped — to NKT and NIT only — which is PR 13's material, not
  this key's.
- **NQQ/RTQ's 2020-03-23 listing is caller catalog data**, not a revision: CME Clearing
  Advisory 20-061 (notice date 2020-02-26, effective 23 March 2020) tabulates "Listing Date
  Trade Date Monday, March 23, 2020" with both roots and the era-1 grid, and a member
  listing after the family clock began adds no row. The future-tense sentence on the 2026
  marketing page never mattered.

**`globex_equity_index_tmac`**

- **Pre-launch closure, then one era keyed 2023-07-30** (Sunday, the local opening day;
  CME Globex Notice 2023-07-10 gives trade date Monday 2023-07-31, with the table `ESX | E2`,
  `NQX | N9`, `RTX | R9`, `YMX | Y9`, ref SER-9210). Sunday–Friday 17:00 → 15:00 CT (CME's
  "6:00 p.m. - 4:00 p.m. ET") with the Globex maintenance gap; `order_entry` Sunday
  16:00–17:00 and Monday–Thursday 16:45–17:00 (wiki: "TMAC groups then go into pre-open on
  Sundays between 16:00:00 and 16:01:00 Central time (CT), and Mondays through Thursdays
  between 16:45:00 and 16:46:00 CT"; service on group E2 returns `closed@15:00`,
  `paused@16:45`, `preopen@16:45`, `open@17:00`). The live service returns byte-identical
  schedules for all four roots → **one key**.
- **The adjacent "TERMINATION OF TRADING … 4:00 P.M. ET on the business day immediately
  preceding the last trade date" is expiry and is deliberately not used.** Say so in the
  comment and cite LAW-SESSION-NOT-EXPIRY.
- `regular: &[]` on Rule 524.D.1 + .2 (Globex plus Rule 526 block or Rule 538 EFP/EFR
  only), the ProductSlate's four TMAC records at `floor "-"`, the ContractSpecs venue label,
  and the wiki's pre-open paragraph with no RTH/ETH split. **TMAC's absence from the Daily
  Bulletin is an ACTIVITY absence (vol 0, oi 0) and is not evidence** — record it as such so
  nobody cites it.
- **[U-4 verdict D6]** Every trading-hours-service capture behind these two keys covers
  2026-09-06..12, whose Monday is **US Labor Day**: group E2 has no events on Sunday
  2026-09-06 and group 3T reads `preopen@12:00` on the Monday. Mark the capture as a holiday
  week and withdraw any Monday or Sunday inference from it. The Sunday 16:00 pre-opens rest
  on the wiki, not on that capture.

**Ledger:** TACO — Partial, `Gap: executable` (the Saturday rows are withheld against the
operator's own feed, and the residual is an unexplained 12-hour block). TMAC — Partial,
`Gap: order-entry` (the Pre-Opens rest on the wiki and the feed; no dated onset).

**Follow-ups (open before merge):** the (05:00, 17:00) Saturday artifact on NIT/N6 and
NKT/ND, for PR 13 to withhold on the same evidence; Clearing Advisory 21-234 as a PR-13
source in its own right (it dates the Nikkei BTIC Mon–Thu → Mon–Fri 12:00–17:00 ET expansion
to trade date 2021-09-27 and names NKT/NIT with rulebook chapters 352 and 352B); the
"pending" adjudication (D-3); the ES ClearPort/Globex TACO cell divergence; and — if D-4
lands the narrowed rule — the AGENTS.md edit recording that **a feed event is session
language except where the operator's own prose contradicts it**, with TACO's Saturday rows
as the worked example. That edit narrows a named law and therefore belongs in its own issue
and its own commit, not in a key's doc comment.

---

### PR 11 — Energy TAM, and the cross-zone pattern

**Keys (3):** `globex_energy_tam_london` (CLL, BZL, HOL, RBL),
`globex_energy_tam_singapore` (CLS, BZS), `globex_energy_tam_shanghai` (CLC).
**Module:** `src/calendar/schedules/futures/us/energy_tam.rs`.
**Blocked on decisions D-1 (Option G) and D-2 (three keys, not one).**

This is the **first cross-zone key set**, so it establishes the pattern and the shared test
template for PRs 12 and 13. Land it before them.

**Representation (Option G).** Keep `tz: US::Central`. Ship **two** `StaticHoursProfile`
values per key — one per relative-offset state — and choose between them in the key's
`profile_at` with `schedules::timeline::reference_delta_seconds`, exactly as
`ice_abu_dhabi.rs:103` does (foreign venue tz, New-York-anchored grid — the exact mirror of
this proposal, and the strongest precedent). Shape:

```rust
const LONDON_ALIGNED_DELTA_SECONDS: i32 = 6 * 3600;

pub(crate) fn energy_tam_london_profile_at(as_of: DateTime<Utc>) -> &'static StaticHoursProfile {
    let day = local_date(as_of, US::Central);
    if day < TAM_LONDON_LAUNCH {
        return &CLOSED_CENTRAL;
    }
    let seasonal = if reference_delta_seconds(as_of, US::Central, Europe::London)
        == LONDON_ALIGNED_DELTA_SECONDS { &ALIGNED } else { &MISALIGNED };
    select_revision(day, seasonal.baseline, seasonal.revisions)
}
```

The seasonal switch **asserts no date** and must **never** enter a `revisions!` table or
`HISTORICAL_CUTOVERS`; the `revisions!` timeline carries only sourced launch days.
`reference_delta_seconds` reads no clock (LAW-DETERMINISM) and resolves through the total
`mk_local_open` (LAW-PANIC). No public type, field, signature or serde form moves; the
golden file gains additive rows only and **no existing key's rows move**.

| Key | Pre-launch | Launch row (local opening day) | Open | Close, aligned / misaligned |
|---|---|---|---|---|
| `globex_energy_tam_london` | closure | **2011-06-12** (Sun; SER-5788, 2011-06-06, "Effective trade date Monday, June 13, 2011 … TAM based on the London market close at 4:30 p.m. London time") | 17:00 CT | 10:30 / 11:30 CT |
| `globex_energy_tam_singapore` | closure | **2011-07-10** (Sun; SER-5794, 2011-06-07, "Effective trade date Monday, July 11, 2011 … the Singapore Trading at Marker (TAM) based on the Singapore market close of 4:30 p.m. Singapore time") | 17:00 CT | 03:30 / 02:30 CT |
| `globex_energy_tam_shanghai` | closure | **2024-06-16** (Sun; SER-9380, 2024-05-23, "Effective Sunday, June 16, 2024, for trade date Monday, June 17, 2024 … TAM (Shanghai Marker) eligibility … Light Sweet Crude Oil Futures \| CL \| CLC \| Front contract month") | 17:00 CT | 02:00 / 01:00 CT |

**All three launch rows were one day late in the U-8 gate [verdict D4]** — SER-9380 states
both days in the handoff's own quote and the gate took the wrong half. Key the Sunday.

**Session language is CME's own, and this is what makes these keys admissible at all.** The
Energy TAM FAQ (published 2024-06-05) says "CLL, RBL, HOL and BZL trading **halts at the
marker time, daily**, at 4:30 p.m. London time", "CLS and BZS trading halts at the marker
time, daily, at 4:30 p.m. Singapore time", and "CLC trading halts at the marker time,
daily, at 3:00 p.m. China time". "Trading halts … daily" is LAW-SESSION-NOT-EXPIRY's own
first listed session phrasing. **CME publishes both Central values itself** for two of the
three — "(2:30/3:30 a.m. Central time)" and "(1:00/2:00 a.m. Central time)" — so the
Singapore and Shanghai pairs are transcription, not inference. Keep the FAQ's §5 marker
**calculation** windows ("the volume weighted average price (VWAP) … for the one-minute
period from 4:29 - 4:30 p.m.") strictly separate; they are not session language.

`regular: &[]`, and TAM is the cleanest of the five trade-type shapes: NYMEX/COMEX Rule
524.B has **never** contained a pit clause — verified on the 2015-03-06 rulebook capture,
i.e. *during* the pit era, where 524.A (TAS) still had one and 524.C defined MO as "open
outcry trades". That is an affirmative negative, not silence. Eight TAM ProductSlate
records read `floor "-"`, `floorVol "0"`, `venues "Globex ClearPort "`. The Daily Bulletin
gives TAM its own page headed "TRADE AT MARKER PRODUCTS" with columns "VOLUME BLOCK VOL
MARKER PRICE" and no RTH/ETH legend — **[U-4 verdict D5]** it is **not** price-less, and
the load-bearing form of the argument is that no trade-type instrument is a row inside the
RTH/ETH apparatus, which a marker price does not make it.

`order_entry` — the TAM group's own Pre-Open, on RA2302-5 §3 and NYMEX/COMEX Rule 524.B.1
("during each TAM contract's prescribed pre-open time period"), present since at least the
2015-03-06 capture. **The onsets have no sourced day** (`preopen@16:50` for groups TM, TS,
WM; `preopen@16:45` for others), so either withhold them or attach them to a knowledge-bound
review row — do not invent an onset date. **ContractSpecs is not a channel for TAM**:
productIds 8407 (GCD) and 6266 (CLL) return empty records and the CL (425) spec's Globex
block carries only a TAS line.

**[U-8 verdict D2] Withdraw the "no product id was located for CLL/CLS/CLC" dead end.** A
single `ProductSlate/V2/List?…&searchString=<root>` call returns CLL=6266, BZL=6268,
HOL=6270, RBL=6273, CLS=6332, BZS=6333, CLC=10725, GCD=8407, HGF=8652, BTB=8970, ABB=10664,
and all four close pairs are now first-hand.

**Tests — the shared cross-zone template.** New file
`tests/futures_family_boundaries/cme_trade_type_cross_zone.rs`, and PRs 12 and 13 extend it
rather than duplicating it. Ten assertions, per the U-8 memo §4:

- **T1 aligned summer** (2026-08-31 week): closed 16:59:59 CT Sunday; open 17:00:00; open
  10:29:59 CT Monday; **closed 10:30:00** (end-exclusive).
- **T2 aligned winter** (2026-12-07 week): the same four Chicago values. This proves the
  aligned state is offset-driven and not a summer accident.
- **T3 autumn misalignment** (2026-10-26 week): open 11:29:59, **closed 11:30:00**, and
  `open@17:00 CT` **unchanged** — assert the open explicitly, because the whole claim is
  that one endpoint moves and the other does not.
- **T4 spring misalignment** (2027-03-15 week): identical to T3. A naive autumn-only
  implementation passes T3 and fails T4.
- **T5 the four transition weekends, date-aware**, via `calendar_for_market_hours_key` (a
  fixed snapshot cannot cross a transition). Copy the shape of
  `tests/seasonal_calendars/international.rs::endex_calendar_scans_reselect_both_mismatch_entries_and_exits`,
  which already uses exactly that four-case table: autumn entry
  `next_session_after(Fri 2026-10-23 10:30 CT) == (Sun 2026-10-25 17:00, Mon 2026-10-26
  11:30)`; autumn exit `(Fri 2026-10-30 11:30) == (Sun 2026-11-01 17:00, Mon 2026-11-02
  10:30)`; spring entry `(Fri 2027-03-12 10:30) == (Sun 2027-03-14 17:00, Mon 2027-03-15
  11:30)`; spring exit `(Fri 2027-03-26 11:30) == (Sun 2027-03-28 17:00, Mon 2027-03-29
  10:30)`. Plus `session_bounds(Mon 2026-10-26 11:00 CT)` returning the **containing**
  session, not the next one — the assertion that catches the false-closed error.
- **T6 no session spans an offset change**: for each of the four transition Sundays in 2026
  and 2027, `is_open` is false at the transition instant itself (US 02:00 local Sunday; UK
  01:00 UTC Sunday = **Saturday 20:00 CDT**, not 19:00 — the memo's returned JSON has that
  wrong [verdict D5]).
- **T7 the two profiles differ only in the SSM**: identical `tz`, rule counts, `days` masks,
  `has_daily_close`/`has_weekend_close` and per-rule wrap; the only difference is
  `close_ssm`, by exactly 3600. Also assert `normal_week_open_seconds()` differs by exactly
  `3600 × <closing days>` — this pins the golden file's blind spot, because
  `UNIX_EPOCH + 1_787_400_000 s` is 2026-08-22 12:00 UTC, an **aligned** day, so the second
  profile never appears in the golden file.
- **T8 trade date is stable across states**: `trade_date(Mon 10:00 CT)` in the T1 week and
  `trade_date(Mon 11:00 CT)` in the T3 week both return the Monday.
- **T9 serde and identity** (standard, listed so it is not forgotten).
- **T10 mutation check**: move a launch revision one day → red; flip the aligned/misaligned
  branch → T3 and T4 red; change one `close_ssm` by 60 s → T1 red. **Say in the PR that you
  did it.**

**Residual risks to record beside the tables:** no both-zones-on-summer-time week was ever
captured, so the aligned summer value is derived (15:02 BST = 14:02 UTC = 09:02 CDT) —
unambiguous but not observed; the Pre-Open onsets are undated; the Singapore and Shanghai
**opens** are stated by no retrieved document in prose and are carried from the family grid.

**Follow-ups (open before merge):** `session_profile`'s doc claims a clock-less current
table equals the timeline's selection at any instant — **already false for
`EurexFixedIncome` half the year** (`profiles.rs:309` against
`eurex_fixed_income.rs`'s "`_CURRENT` is the CEST grid"), and these keys add more of the
same; the near-midnight wrap caveat (nearest miss is 00:30 CT on the Tokyo-anchored shapes,
with CLC at 01:00 second); and `6EB`'s addition to U-8's list.

---

### PR 12 — Metals TAM

**Keys (2):** `globex_gold_tam` (GCD, group GM), `globex_copper_tam` (HGF, group TR).
**Module:** `src/calendar/schedules/futures/us/metals_tam.rs`.
**Blocked on decisions D-1 and D-4.** D-4 is the whole question: CME's prose for these two
gives only a marker **calculation** window, so the close rests solely on the trading-hours
service's labelled `closed@` events. Do not write this PR until D-4 is decided in writing.

| Key | Pre-launch | Launch row (local opening day) | Open | Close, aligned / misaligned |
|---|---|---|---|---|
| `globex_gold_tam` | closure | **2017-10-22** (Sun; CME Globex Notice 20171016, trade date 2017-10-23, "Gold London Trade At Marker First PM \| GCD \| GM"; Clearing advisory 17-356 confirms) | 17:00 CT | 09:02 / 10:02 CT |
| `globex_copper_tam` | closure | **2019-02-24** (Sun; CME Globex Notice 20190211, trade date 2019-02-25, "Copper London TAM \| HGF \| TR") | 17:00 CT | 06:35 / 07:35 CT |

Both dates were a day late in the U-8 gate [verdict D4]. `regular: &[]` and `order_entry`
exactly as PR 11. `/services/trading-hours-by-product?id=8407` publishes labelled session
events — `preopen@16:00`/`open@17:00` Sunday, `closed@09:02` daily,
`preopen@16:50`/`open@17:00` weekdays — measured across three windows (2026-10-26,
2026-12-07, 2027-03-15) with `open@17:00` and `preopen@16:50` identical in every one; `id=8652`
(group TR) returns the same queue shape at `closed@06:35`.

**The handoff's "HGF 78/TR → 78/HT" route drift is an artefact and must be recorded as
one:** HT is the copper **TAS** group (HGT/MHT/HG0), and the same notice prints "Copper TAS
| HGT | HT" a few rows below "Copper London TAM | HGF | TR". The inventory conflated a TAM
root with a TAS group; the row-41 "copper TAM 12:00" figure contradicts its own signature
(11:35Z = 06:35 CT, while 12:00 CT is the copper *TAS* close). **[U-4 verdict D7]** The
"HGF on TR" datum was carried from the handoff, not measured by the U-4 gate whose own probe
returned HTTP 400 — it **is** first-hand in the U-8 verifier's captures; cite those.

CME's eligibility workbook's "Metals TAM" sheet lists exactly two roots, GCD and HGF, so the
gold AM/Asia marker trap is hypothetical and the two-key scope is complete. The COMEX
metals-marker copper London/New-York DST carve-out is second-hand and was never re-fetched;
the first-hand 06:35/07:35 CT measurement is what it predicts. Record both facts.

**Ledger:** two rows, Partial, `Gap: executable` — the close rests on one channel, and its
promotion to a session boundary is the D-4 adjudication, which must be cited in the row.

---

### PR 13 — TOPIX BTIC, Nikkei BTIC, FX BTIC

**Keys (3):** `globex_topix_btic` (TPB, TPT — both group BJ), `globex_nikkei_btic` (NIT/N6,
NKT/ND), `globex_fx_btic_euro` (6EB).
**Modules:** `src/calendar/schedules/futures/us/japan_index_btic.rs` and
`src/calendar/schedules/futures/us/fx_btic.rs`.
**Blocked on D-1 and D-3.** `globex_nikkei_btic` is the hardest shape in the whole plan:
its overnight close is `Asia/Tokyo` while its open **and its entire daytime leg** are
`America/Chicago`.

**`globex_topix_btic`** — separate key from Nikkei, on a primary-sourced difference:
identical published sentence, **different actual grid** (Nikkei carries a second Noon–17:00
ET window, TOPIX demonstrably does not; service id=10251 returns `closed@01:30`,
`preopen@16:45`, `open@17:00` only).

- Pre-launch closure, then **era 1 keyed 2018-02-04** (Sunday; CME 18-007's operative
  cover-letter sentence is itself the self-certification and states the day without
  condition — "…to be listed … on Sunday, February 4, 2018, for trade date of Monday,
  February 5, 2018"; Chadv18-013 gives the same value). 17:00 CT → 15:00 Tokyo
  (00:00/01:00 CT). No daytime leg. `order_entry` Sunday 16:00–17:00, Monday–Thursday
  16:45–17:00 (in session language from 22-413). **[verdict D9] Both 18-007 and Chadv18-013
  also carry the "pending certification … and completion of all regulatory review periods"
  boilerplate the handoff's U-5 uses to disqualify SER-8863's header date. Name the clause
  and say why it does not bite here** (the cover letter states the day unconditionally, the
  day is eight years past, and Chadv18-013 plus contemporaneous spec captures show the
  listing happened) — a gate whose brief is "a conditional launch is not an unconditional
  effective day" cannot pass over it silently. This is decision **D-3**'s first application.
- **Era 2 keyed 2024-11-03** (Sunday, the local opening day; **CME Submission 24-263**,
  2024-08-27, an unconditional 40.6(a) certification: "effective Sunday, November 3, 2024,
  for trade date Tuesday, November 5, 2024", with the blackline "BTIC: Sunday - Friday 6:00
  p.m. ET - [3:00 p.m.] **3:30 p.m.** Tokyo time" for NKT, NIT, TPB and TPT together). The
  trade date named is Tuesday because Monday 2024-11-04 is a Japanese bank holiday. Close
  moves to 15:30 Tokyo = **00:30 / 01:30 CT**. SER-9412 carries the same text conditionally.
  **This closes U-18(a).**
- TPT's 2022-11-20 listing (CME 22-413) is a later member listing on an existing family
  clock — caller catalog data. Group BJ publishes no session for Japanese-holiday trade
  dates (no Sunday 2027-01-10 evening session for the 2027-01-11 Coming-of-Age Day trade
  date) — **DayPolicy input, not template data.**

**`globex_nikkei_btic`**

- Pre-launch closure, then **era 1 keyed 2019-02-18** (CME 19-012: "effective on Monday,
  February 18, 2019, for trade date Tuesday, February 19, 2019" — the evening session opens
  17:00 CT that Monday for Tuesday's trade date, so the Monday is the local opening day even
  though it was US Presidents' Day [verified residual]). Grid, which 19-012 states "For any
  regular week containing no US or Japanese market holidays" — the crate's exact template
  semantics: Sunday 18:00 ET → 15:00 Tokyo; Monday–Thursday Noon–17:00 ET **and** 18:00 ET →
  15:00 Tokyo; Monday–Thursday 17:00–18:00 ET maintenance; **no Friday daytime leg**
  ("Friday: No BTIC trading is permitted after 1:00 a.m. EST (2:00 a.m. EDT)").
- **Era 2 keyed 2021-10-01** (CME 21-294: "commencing on Friday, October 1, 2021 for trade
  date Monday, October 4, 2021"): adds a Friday Noon–17:00 ET daytime leg carrying Monday's
  trade date. Blackline: "Monday - Thursday 12:00 p.m. to 5:00 p.m. ET" → "Monday - **Friday**
  12:00p.m. to 5:00 p.m. ET". **Corroborate with Clearing Advisory 21-234** [PR 10 verdict
  D1], which states the same before/after grid for NKT and NIT with rulebook chapters 352
  and 352B against effective trade date 2021-09-27 — note that 21-234 and 21-294 give
  *different* days for what looks like the same expansion, so establish which took effect
  before keying the row, and record the conflict if it survives.
- **Era 3 keyed 2024-11-03** (CME 24-263, as TOPIX): the overnight close moves 15:00 → 15:30
  Tokyo.
- **U-18(b) is resolved in the negative — there was never an 11:00 a.m. → Noon ET Globex
  change.** 19-012 puts Globex at 12:00 noon ET and CME ClearPort at 11:00 a.m. ET on the
  same page; the conditional clearing advisory Chadv19-025 (2019-01-17) prints the ClearPort
  value in its Globex row; 21-294's 2021 "Current" column already says 12:00 p.m. ET; and the
  live feed opens 11:00 CT = Noon ET. **Serve Noon ET from launch and record Chadv19-025 as
  the outlier.**
- **Withhold the Saturday block.** Groups N6 and ND publish `open@05:00` … `closed@17:00`
  with the following Monday's (or next Japanese business day's) trade date in every retrieved
  week, on the same evidence and for the same reason as TACO's (PR 10). **[verdict D2] Do not
  write that it is "present on every Saturday across the feed's entire retained year"** — the
  gate probed four windows containing seven Saturdays out of roughly seventy, and the
  verifier's three further windows bring it to **16 of 16 Saturdays across 16 months**. State
  the measurement that was actually made.
- **Holiday irregularities in the captures are DayPolicy input, not template data** and the
  gate mentions only two of them: NKT/NIT lose the Friday daytime leg on 2026-09-18 (Japanese
  holiday run 2026-09-21..23); TPB has no close on 2026-11-02 and no open on 2027-01-11;
  NKT closes early at 12:00 on Friday 2026-06-19 (Juneteenth); BTB/NKT roll Friday 2027-01-15
  to trade date 2027-01-19 (MLK Day). 19-012's own note and Chadv19-025's "BTIC trading will
  not be permitted on U.S. Exchange or Japanese Banking Holidays" are the operator's
  statement of the same thing.
- **[verdict, minor]** 24-263's Table 1 mislabels NKD as "Yen Denominated" and NIY as "USD
  Denominated", the reverse of 19-012 — a CME document defect, immaterial because the BTIC
  codes disambiguate. Record it.
- **Do not fold these into `globex_nikkei_225_dollar`**: `cme_nikkei.rs` puts NKD's whole
  envelope in `regular`, so folding an extended-only BTIC key into it would be a semantic
  error.

**`globex_fx_btic_euro`** — the cheapest cross-zone sub-case: the **envelope** is
`America/Chicago` (17:00 open, 16:00 close, 16:00–17:00 maintenance) and only a 50-minute
interior interruption is `Europe/London`-anchored.

- Pre-launch closure, then **one era keyed 2023-02-05** (Sunday; CME 23-015 is the BTIC
  eligibility certification, trade date Monday 2023-02-06; the FX BTIC FAQ dates the launch
  in words: "The first day of trading for BTIC and BTIC+ is Monday February 6, 2023").
  Sunday–Friday 17:00 → 16:00 CT with the 16:00–17:00 CT daily maintenance, plus a daily
  trade-date roll: the book stops at 15:40 London and reopens at 16:30 London =
  **09:40–10:30 CT aligned, 10:40–11:30 CT misaligned**. CME spells both pairs out itself:
  "Trading halt from 3:40 p.m. London time (9:40 a.m./10:40 a.m. CT) to 4:30 p.m. London
  Time (10:30 a.m./11:30 a.m. CT)". `order_entry` Sunday 16:00–17:00, Monday–Thursday
  16:45–17:00.
- **The handoff's "CME uses two different words and two different end times for the same
  interruption" is dissolved, and it was a venue confusion**: the spec's "trading halt 9:40
  a.m. to 11:30 a.m. CT" is the **CME ClearPort** window and the "trading close from 3:40
  p.m. - 4:30 p.m. London time (9:40 a.m. - 10:30 a.m. CT)" is the **CME Globex** window. Two
  venues, two windows, no contradiction; the FAQ prints both consistently. **Record the
  dissolution** — the handoff's row says the wording decides Halt vs Closed and it does not.
- **Classification: `Maintenance`, never `Halt`.** The FAQ: "These trades will be treated as
  trades for the next day's trade date." The 50-minute gap is a **trade-date roll**, so it is
  an inter-trade-date gap under four hours within one ISO week.
- **Scope caveat to record:** 6EB has **no** product-slate row, **no** Globex security group
  of its own and **no** schedule-service entry — the slate carries only 6E (group 6E) and 6EP
  (group 6X), and `"globex":"6EB"` occurs zero times across all seven slate pages (3,248
  records), which is a genuinely exhaustive negative [verdict D12]. So the handoff §3.2
  asymmetry between 6EB (own key) and 6EP (rides `globex_fx`) rests **entirely** on the
  spec/FAQ interruption. Say so, and say that 23-015's Exhibit E stating the plain FX
  envelope with no BTIC interruption is the contract's boilerplate hours block, not a denial.
- 6EB is the one shape never measured first-hand on any pass; its pair is CME's own prose,
  which is a stronger source than a feed decode, but the shape is unmeasured. Record it.

**Tests:** extend `cme_trade_type_cross_zone.rs` with each key's own instants. **For the
Tokyo-anchored pair make T8 (trade-date stability) explicitly on both states** rather than
reusing the London instants — 00:30 CT is the nearest approach to local midnight anywhere in
this plan, and the swap must not flip wrap/no-wrap. For 6EB the moving boundary is an
**interior** gap, so assert both its edges in both states and assert the envelope's
endpoints do **not** move.

**Ledger:** TOPIX BTIC — Partial, `Gap: order-entry`. Nikkei BTIC — Partial, `Gap:
executable` (the Saturday block is withheld and the 21-234/21-294 day conflict may survive).
FX BTIC — Partial, `Gap: order-entry` if the interior roll is encoded; `Gap: executable` if
it is withheld.

---

## 3. Keys that are BLOCKED, and on exactly what

**Never plan a row that lacks an unconditional day.** These six are not in any PR above.

| Key | Blocked on | What closes it |
|---|---|---|
| `globex_cryptocurrency_btic_new_york` (19 roots, 9 groups) | **U-15.** Era 1 is unconditional (22-220, first session 2022-07-24, trade date Monday 2022-07-25) and its grid is sourced on BTC's ContractSpecs at 2024-09-29, 2025-02-21 and 2025-10-28. The **current** grid is a different, 24/7 shape and its cutover day is undated: CME 26-114 and SER-9740R scope "all cryptocurrency futures and options on futures contracts" and neither contains the string "BTIC". Shipping era 1 alone would serve today's market wrongly; shipping era 2 would invent a date. | A CME notice, SER or clearing advisory naming a **BTIC product code** against 2026-05-29. **Or** — and this is the cheap, bounded step, worth one retrieval before anything else — re-read the client-systems wiki migration page and determine whether its own effective-day sentence scopes the BTIC tables the way the ag/crypto gate accepted it scoping the **TAS** table. The two gates treat the same channel differently (see decision **D-8**); one read settles it. Note the 26-114 pre-open times (Mon–Fri 16:01–16:02 CT, Saturday 03:45–04:00 CT) are byte-for-byte the BTIC feed's, but that is inference, not a day. |
| `globex_cryptocurrency_btic_london` (10 roots, 5 groups) | **U-15**, and additionally **U-8 verdict N1**: Option G is *not exact* for this shape. Its 24/7 weekend block is one continuous span from Saturday ~04:00 CT to Monday, and `profile_for_open_day` anchors selection at `OPEN_DAY_ANCHOR_SSM` on the **opening** day (the Saturday, pre-transition) while the close falls on the Monday (post-transition). Measured: BTB autumn 2026 would serve a 10:00 CT close where CME publishes 11:00 — an hour of **false-closed executable** window; spring 2027 the reverse. Also an unrecorded **source conflict**: CME's BTIC-on-Cryptocurrency FAQ states a **30-minute** stop ("4:00 p.m. London time … Monday - Thursday 4:30 p.m. London time … - 5:00 p.m. ET") against the feed's **5-minute** restart, and the 5-minute value is the post-cutover state only. | A dated source for the cutover, **plus** a treatment for the weekend block: a close-day anchor, a split of the block at the transition, or leave it unmapped. Withhold the 25 disputed minutes either way. |
| `globex_cryptocurrency_btic_apac` (5 roots, 2 groups) | Same as London (N1 measured on ABB across the US fall-back too). Also: **SOL, XRP, ADA, LINK, AVAX, SUI and Stellar Lumens have no APAC variant** — only the Bitcoin and Ether complexes plus Bitcoin Friday Futures carry one; the handoff's row-14 caution is upheld and extended. | As London. |
| `globex_europe_index_btic` (DVT, E3T) | **No gate ever covered it** [btic verdict D3]: neither the root codes, the key name, nor productIds 8005/7955/7956 appear anywhere in the non-equity BTIC result. The handoff's own citations are good (ContractSpecs DVT 8005: "Sunday - Friday, 6:00pm New York time - 4:30pm London time (5:00pm - 10:30am Chicago time, as adjusted for DST)"; E3G 9998: "BTIC Hours: Sunday - Friday 5:00 p.m. CT - 4:30 p.m. London Time"; service id=8005 closes 10:30 CT Sep/Dec and 11:30 CT in the 2026-10-27 week — **Europe/London, not CEST**) but no launch day was ever retrieved, and **[U-8 verdict D6]** the retrieved evidence does not fix the zone: the shape queue decoded the same 15:30 UTC close as "17:30 CEST". Immaterial to the Chicago pair (London and the continental zones change offset at the same UTC instant) but LAW-PRIMARY-SOURCES wants the comment to name the anchor the source states. | One gate: the launch certification for the DVT and E3G BTIC listings, plus E3G's unresolved route change 68/EU → 68/EQ. Then it is an ordinary Option G key. |
| `globex_ftse_china_50_btic` (FTC) | Same — no gate covered it. Handoff citations: ContractSpecs FT5 7955, "BTIC: Sunday - Friday 6:00 p.m. - 3:00 a.m./4:00 a.m. ET (16:00 Hong Kong Time)"; service id=7956 closes 03:00 CT Sep/Oct and 02:00 CT Dec → Hong Kong-anchored, re-derived first-hand as 16:00 `Asia/Hong_Kong` in both states. FTC's own page's flat "5:00 p.m. - 3:00 a.m. CT" is **wrong** and must be recorded as a conflict. No launch day retrieved. | One gate: the FT5 BTIC launch certification. |
| `globex_equity_index_btic_plus_taco_plus` (ES1, ES2, EQ1) | **U-19.** Two CME documents give two **conditional** launch days — Globex Notice 2019-08-26 "Effective Sunday, September 8 (trade date Monday, September 9)" against the BTIC+/TACO+ FAQ "CME Group will launch BTIC+ and TACO+ on E-mini S&P 500 futures on October 7", both carrying "pending". This is a *conflict*, not merely a condition, so decision D-3 does not rescue it. The executable window **is** sourced (FAQ, capture 2026-06-06: "Sunday – Friday 6:00 p.m. - 5:00 p.m. ET, 5:00 p.m. - 4:00 p.m. CT", with the 5:00 p.m. ET / 9:30 a.m. ET instants separately labelled "Termination of trading" — deliberately not used). Carrying that grid back to the floor would say the product traded in 2010; a knowledge-bound row would say it did not trade in 2019. Neither is acceptable. | The SER confirming which day took effect. **[U-4 verdict D1]** When it is written: Rule 524 is **not** a channel for this key — CME's own FAQ says "Unlike BTIC and TACO transactions, BTIC+ and TACO+ are not governed by Rule 524" — so its `regular: &[]` rests on the ProductSlate (ES1 8689, ES2 8690, EQ1 8691 each `floor "-"`, `floorVol "0"`), the ContractSpecs venue label and the Daily Bulletin only. Say which channels reach it and which do not. It is excluded by name from `globex_equity_index`, and CME Globex Notice 2021-06-21's "all BTIC and TACO products will not be impacted" means its halt history diverges — same envelope, different history, own key. |

**Also blocked, and correctly recorded as rejections rather than as keys** (PR 1): Treasury
TAS (U-5), Dutch TTF TAS (U-7), commodity-index BTIC AWT…CCT. `MCT` (U-0a) is a membership
question, not a key — see D-6.

---

## 4. Decisions the maintainer must make before certain waves

Each is stated as a question with a recommendation. **D-1 through D-4 gate PRs 10–13;
D-5 through D-8 are minor and gate only their own PR.** Every one of them should be opened
as a GitHub issue and cited where it is relied on (LAW-FOLLOW-UPS-ARE-ISSUES).

**Decisions taken 2026-09-12 UTC** (under the maintainer's standing delegation of
correctness and architectural calls, logged here and in the repo plan doc PR 1 adds):
D-1 **adopted** (Option G, scoped to the ten weekly-close shapes); D-2 **adopted** (ten
TAS keys, five TAM keys; rows 10/22 stay one key); D-5 **adopted** (two energy-TAS eras);
D-6 **adopted** (map `MCT` on published-group identity, sourced on `BZT`); D-7 (a), (b),
(c) **adopted** as recommended. **D-3 and D-4 are law edits to `AGENTS.md` and are
referred to the maintainer as GitHub issues** — the repository's instruction is to keep
to its law even where a case argues for changing it — so PRs 10, 12 and 13 wait on those
issues; D-8 was run alongside PR 1 and returned **PAGE_WIDE** (`D8-wiki-scope.json`): PR 4 stands as written; the crypto BTIC keys' *date* blocker clears on the TAS key's warrant, leaving the exact-instant bridge, the membership channel, the 16:01–16:02 conflict and — for London/APAC — N1 (tracked on #73).

### D-1 — U-8: how are cross-zone grids represented? *(gates PRs 11, 12, 13)*

**Question.** A `StaticHoursProfile` carries one `tz` and seconds-since-local-midnight
rules. Ten shapes here open at 17:00 `America/Chicago` and close at a fixed wall-clock
instant in London, Singapore, Shanghai, Hong Kong or Tokyo. How is that represented?

**Recommendation: adopt Option G** — keep `tz: America::Chicago`, ship two
`StaticHoursProfile` values per key, select with `reference_delta_seconds`. U-8's premise
that "neither endpoint is expressible without the other drifting" is **false**: four
genuine cross-zone selectors already ship, `ice_abu_dhabi.rs` is the exact mirror of this
proposal, and `MarketHoursKey::EurexFixedIncome` is the key-side precedent, whose module
already writes down this memo's central argument ("A single fixed-local-wall-clock profile
would therefore be wrong for roughly half of every year"). Zero API change, zero serde
change, no migration, no existing key's golden rows move, and AGENTS.md already anticipates
it ("A cross-zone or otherwise recurring selector also needs date-aware `ExchangeCalendar`
transition coverage"). The cost of the single-grid alternative is measured: 20 hours a year
of false-closed or false-open **executable** window for the London-anchored shapes, and an
hour wrong on 35–65% of weekdays for the Asian anchors — and AGENTS.md ranks
executable-window gaps highest.

**Scope the answer to the ten shapes that carry CME's Friday-16:00 / Sunday-17:00 CT weekly
close.** It is **not** exact for the two 24/7 crypto BTIC shapes (verdict N1), which are
blocked on U-15 anyway. Do not spend the mechanism on `America/New_York`-anchored shapes —
TMAC, TACO, equity/sector/AIR BTIC, credit BTIC, crypto BTIC New York and commodity-index
BTIC are all exactly representable in Chicago local seconds.

### D-2 — TAS and TAM granularity *(gates PR 11; informs PRs 2–5)*

**Question.** CME's own TAS eligibility workbook has exactly six tabs — Cryptocurrency,
Energy, Grain and Oilseed, Livestock, Metals, Treasury — and its single "Energy TAS" sheet
covers CLT, MCT, NGT, HHT, 7FT, TAS and TTS together. This plan proposes **ten** TAS keys
and **five** TAM keys. Is that right?

**Recommendation: keep the ten TAS keys and the five TAM keys, decided on family semantics
and history rather than on the envelope**, which is what handoff §3.3 asks for.
- Metals TAS splits five ways because the closes differ (12:30 / 12:25 / 12:05 / 12:00 /
  12:00), the launches are 2010, 2010, 2011, 2017 and 2018, and copper's and palladium's
  coincident 12:00 sits on different exchanges and different security groups. The
  `globex_mini_grains` precedent (three keys, one envelope, three histories) governs.
- Energy TAS and gasoil TAS split because 7FT's close differs from CLT's in **every**
  sourced era (11:00 then 10:30 against a constant 13:30).
- **Do NOT split rows 10/22** (CLT/HOT/RBT/BZT/BBT against NGT/NNT). They differ only by a
  Pre-Open second the crate does not encode today, and by a one-to-two-minute Pre-Open
  stagger in 2011–2012 — never by an executable boundary. One key.
- Three energy TAM keys, not one: they differ by exactly one constant each, so Option G
  makes the three-key answer nearly free, and AGENTS.md's "a venue that merely coincides
  with another still gets its own named profile so a future divergence is a one-line edit"
  applies directly to three different city closes.

### D-3 — Does "pending all relevant CFTC regulatory review periods" defeat an effective day? *(gates PRs 10, 13)*

**Question.** The handoff rates TACO's 2018 launch **High** while U-19 rejects two 2019 days
**partly because they carry "pending"**. Those cannot both stand. The clause appears on
Globex Notice 2018-05-07, SER-8124R, Clearing Advisory 20-061, Clearing Advisory 21-234,
Globex Notice 2021-09-06/13/20, the TMAC launch notice, CME 18-007, Chadv18-013, SER-8599R,
SER-8788, SER-9412 and RA2302-5 — i.e. most CME launch and eligibility documents in this
handoff.

**Recommendation: a conditional clause on a day that is now in the past, whose occurrence is
independently witnessed by a post-effective artifact in the operator's own channel, is
DISCHARGED, and the row is encodable — with the discharge recorded beside the row.** The
crate already does exactly this: `livestock.rs` keys 2016-02-29 to SER-7591 despite its
"pending CFTC review" clause, discharged by a fact card created 2016-03-03 and a spec page at
2016-03-11. Two facts support the narrow form. First, CME publishes **unconditional** days in
the same weekly channel — the 2021-06-21 halt-removal item reads "Effective this Sunday, June
27 (trade date Monday, June 28), CME Group will eliminate…" with no clause — so the clause is
applied *selectively*, to product listings and eligibility changes that are CFTC
self-certified, and is not universal boilerplate to be read past. Second, LAW-NO-FABRICATED-DATES
forbids encoding a **future** date contingent on a readiness filing; it does not say a past,
witnessed day is unsourced. **U-19 stays rejected for a different reason** — two documents
name two different days, which is a conflict, not a condition, and the sourced-intersection
convention has nothing to intersect when the disputed thing is a launch day.

Write the adjudication **once**, in AGENTS.md beside LAW-NO-FABRICATED-DATES, and cite it
from every row that relies on it. That is a law edit and belongs in its own PR — put it in PR
1 if the maintainer decides before PR 1 lands, otherwise in its own PR before PR 10.

### D-4 — Does a labelled `closed@` event promote a marker instant to a session close? *(gates PR 12)*

**Question.** `globex_gold_tam` (GCD) and `globex_copper_tam` (HGF) rest **solely** on
CME's `/services/trading-hours-by-product` publishing `closed@09:02` and `closed@06:35`;
CME's prose for both gives only a marker **calculation** window. Meanwhile U-16 narrowed the
rule in the opposite direction, because TACO's Saturday feed rows are contradicted by four
CME prose statements.

**Recommendation: yes for GCD and HGF, on a narrowed rule that resolves both cases
consistently — a venue feed's own labelled close/halt event is session language EXCEPT where
the operator's own prose contradicts it.** A marker *calculation* window is **silent** about
the session, not contrary to it; the same feed vocabulary is accepted without argument for
the five TAM shapes whose FAQ states the close in session language; and withholding would
leave two families unmapped on a distinction the operator itself does not draw (its
eligibility workbook's "Metals TAM" sheet lists exactly these two roots beside the energy
ones). LAW-SESSION-NOT-EXPIRY's own text already admits "a venue feed's own close/halt
event"; the narrowing only adds the contradiction carve-out, and TACO's Saturday rows are its
worked example — note they are a full open+close **pair**, not the close/halt event the law
names, which is an independent reason to reject them. **Record the narrowing in AGENTS.md in
its own commit** [U-16 verdict D6]: narrowing a named law does not belong in a key's doc
comment.

If the maintainer decides **no**, PR 12 is dropped and GCD/HGF are recorded in
`unsupported-families.md` as rejections on evidence, naming the two `closed@` values so the
next reader does not re-derive them.

### D-5 — Energy TAS: one era or two? *(minor; gates PR 5)*

**Question.** RA1104-4 (unconditional, dated, session language) splits the energy TAS
**Pre-Open** three ways at minute resolution on 2011-04-10 and the reversal is undated. Encode
two eras with the 16:17/16:47 intersection, or one era from the floor at 16:15/16:45 with the
stagger recorded beside the table?

**Recommendation: two eras.** RA1104-4 is an unconditional dated primary and the crate's
convention is to encode a dated row even when it touches only order-entry (both metals TAS
order-entry rows do exactly that). Either way, **do not split the key** — the executable
window is identical for every root in every sourced era.

### D-6 — `MCT`: map on published-group identity, or leave unmapped? *(minor; gates PR 5)*

**Question.** No CME document states MCT's hours, and MCL's spec uniquely carries no TAS
line. Globex Notice 2022-07-18 places "Micro Crude Oil TAS | MCT | CT | 382" in Globex
security group **CT**, and Globex Notice 2016-12-19 places BZT — a proposed root of this key
— in the same group.

**Recommendation: map it, with the reasoning written down.** The crate already accepted the
identical published-group-identity argument for SYP/LBR ("one group cannot run two grids"),
this is documentation text rather than a grid, and the notice's own effective day is
conditional so it dates nothing — a member listing after the family clock began is caller
catalog data in any case. Source the argument on **BZT** [U-6 verdict D5], not CLT.

### D-7 — Three standalone-cash ratifications *(minor; gate PRs 6 and 8)*

- **(a) CVB era-1 regular/extended split.** CVB era 1 has two executable legs (overnight
  19:00–07:45 and day 08:30–13:20). Neither 25-103 nor 26-234 uses an "Extended Trading
  Hours" heading for CVB, so the split is a **convention** choice, not a sourced one.
  **Recommendation:** day leg `regular`, overnight leg `extended`, matching `grains.rs`'s
  treatment of the same shape under CBOT's own Submission 18-001 heading — and record beside
  the table that the classification is a convention, not a source.
- **(b) SAS and MFV trade-date convention.** Both are non-wrapping day sessions, the shape the
  coverage plan flags as having needed a sourced exception for Rough Rice.
  **Recommendation: check, then do nothing.** Rough Rice needed the exception because it has a
  non-wrapping **evening** leg; SAS and MFV have no evening leg at all, so the close-date
  default already names the right day. Assert it in a test rather than adding a branch.
- **(c) BCOM/CCI weekday queue end.** Served as 16:45 → 08:15 above; the strict intersection
  against 25-093's "4:45 p.m. - 5:00 p.m." is 16:45 → 17:00. **Recommendation: serve 16:45 →
  08:15** — CME's own feed for AW publishes `preopen@16:45` with no intervening event before
  `open@08:15`, and the same filing cell demonstrably carries a ClearPort clause inside the
  Globex row — and record the narrowing in the withheld list. It is an `order_entry` window,
  the lesser kind. Add the **Friday-evening** queue to the withheld list for both keys
  [verdict D5].

### D-8 — The wiki-channel asymmetry between crypto TAS and crypto BTIC *(gates the crypto BTIC keys)*

**Question.** The ag/crypto gate keys crypto **TAS** era 2 to 2026-05-29 on the strength of
the client-systems wiki migration page (saved 2026-05-22, before the event) plus two product
channels, and its verifier accepted the era boundary as firm. The non-equity BTIC gate treats
the **BTIC** tables on what appears to be the same migration page as undated ("those are
page-revision dates, not effective days") and withholds three keys. One of the two readings is
wrong.

**Recommendation: settle it with one retrieval, before deciding anything else about the crypto
BTIC keys.** Re-read the wiki page and determine whether its own effective-day statement
scopes the whole page (in which case the BTIC tables are as dated as the TAS table and the
three crypto BTIC keys move from blocked to writable, subject to N1 for London and APAC) or
only the futures-and-options tables (in which case the crypto TAS row-2 date needs the same
scrutiny the BTIC rows got, and PR 4 must be re-examined before it merges). **Do this before
PR 4 lands**, because the answer can cut either way.

---

## 5. The two repo-side edits from handoff §5 — already landed; the residual is not

- **`futures_profile.rs` `globex_fx` doc — DONE** in commit `e1dc255`. The current text
  reads: "Excludes plain BTIC (`6EB`), which CME's FX BTIC FAQ trades 'up to 3:40 p.m.
  London time (typically 9:40 a.m. CT)' — a different window. The same FAQ puts BTIC+
  (`6EP`) on this clock … so the exclusion is of the trade type's plain flavour, not of the
  ticker family." **PR 13 must keep it coherent** by naming `globex_fx_btic_euro` in that
  clause, and must record the scope caveat that `6EB` has no security group of its own.
- **`cme_nikkei.rs` BTIC sentence — DONE** in the same commit. It now reads "BTIC … is
  separately scheduled, **on its own published hours**, so it is not a phase of this outright
  order book … That is a statement about scope, not about tradability". **PR 13 must add the
  cross-reference** from that sentence to the new `globex_nikkei_btic` and
  `globex_topix_btic` keys, so a reader of `cme_nikkei.rs` is sent to the key that answers
  the BTIC question rather than left with an exclusion.
- **The residual from §5's final paragraph is NOT done, and lands with the TAS PRs**:
  `GlobexGrains` and `GlobexCryptocurrency` mention TAS in **neither** `futures_profile.rs`
  nor `verification.md`, unlike `GlobexEnergy`, `GlobexFx`, `GlobexLivestock` and
  `GlobexRoughRice`. **PR 3** adds the `GlobexGrains` exclusion; **PR 4** adds the
  `GlobexCryptocurrency` one. And `GlobexInterestRates`' doc says only "Excludes options and
  separately specified interest-rate product families" — it does **not** name TAS — so
  **PR 1**'s Treasury-TAS rejection must rest on the two-hour close difference and must not
  borrow a citation from `GlobexEnergy`.

---

## 6. Verification, for every PR

```bash
cargo fmt --all --check \
  && cargo clippy --all-targets -- -D warnings \
  && cargo nextest run --all-targets \
  && cargo test --doc \
  && RUSTDOCFLAGS="-D warnings" cargo doc --no-deps \
  && cargo deny check
cargo +1.95 check --all-targets
UPDATE_GOLDEN=1 cargo test --test golden_grids   # then read the diff line by line
```

Then, before claiming the PR is done: state the test count before and after; state that the
golden diff added only the new keys' rows and **moved no other key's rows**; state the
mutation check you ran on each cutover fence and that restoring it went green; and confirm
every follow-up named anywhere in the PR has an issue number cited where it is named.

---

## 7. Residual risks that span the whole sequence

- **Every PR restates the same ledger tallies.** Two PRs can move the counts along different
  axes so that neither branch's figures survive the merge — it happened with #51 and #49.
  **Re-derive every tally from the merged ledger; never resolve a count conflict by picking a
  side.** The PR-1 fences turn that from a review habit into a red test.
- **The `Partial` key count crosses the fence's hard ceiling on the first family PR.** 24
  today; the array stops at 25. If PR 1 is skipped or trimmed, PR 2 fails with a panic whose
  message ("extend the number words past 29") names the fix but not the cause.
- **`session_profile`'s "equals the timeline's selection at any instant" claim is already
  false** for `EurexFixedIncome` half the year, and PRs 11–13 add ten more seasonal keys.
  Open the issue with PR 11 and fix the doc, or the claim becomes ten times wronger.
- **The golden file renders only the aligned state of every seasonal key** (its instant,
  2026-08-22 12:00 UTC, is an aligned day), so a wrong misaligned `close_ssm` is invisible
  there. T7's handwritten `normal_week_open_seconds()` expectation is the only thing that
  catches it. Do not let it be dropped as redundant.
- **Feed-sourced phases carried back to launch.** Equity BTIC's Pre-Opens, the TAM onsets,
  and the crypto BTIC grids are all carried from 2025–2026 observations to launch days in
  2011–2024. That is the carry-back convention working as designed, but the residual belongs
  beside **each** table, not stated once in this plan.
- **The unexplained Saturday (05:00, 17:00) CT block is a cross-family CME pattern**, not a
  TACO quirk: it appears on ESQ/NQQ/RTQ, on NIT/NKT in both eras, and — **[btic verdict D1]**
  — on crypto BTIC London and APAC in their pre-2026 era, which the gate characterised as
  five-day because its capture window started on a Sunday. One issue must cover all of them.
- **Channel fragility.** `cmegroup.com` returns 403 at IP level to this machine, so much of
  the evidence behind these keys was read as **extracted text** through a public reader in
  front of the cited URLs. `sources.md` already records that caveat for
  `globex_event_contracts` and `globex_event_contracts_btc`; every PR here extends it, and
  each ledger row should say which of its citations came through that channel and which came
  from `web.archive.org` `id_` replay or a direct `cftc.gov` GET (those two carry no caveat).
  Do not advance a review date on the weaker channel alone.
