<!-- SPDX-License-Identifier: MIT-0 -->

# PR 2 result — Metals TAS (five keys)

Completed 2026-09-12 (UTC).

## Identity

| | |
|---|---|
| Branch | `trade-type-metals-tas`, created from `trade-type-fences` |
| Commit | `5530f22` — "Add the five metals TAS keys" |
| Parent | `dd940d7` ("PR 1: CodeRabbit round two"), the tip of `trade-type-fences` |
| PR | <https://github.com/SharurTrading/exchange-hours-rs/pull/83>, base `trade-type-fences` |
| Stacked on | #78 (PR 1). Not merged. The maintainer retargets #83 to `main` after #78 lands. |
| Issues opened | #79, #80, #81, #82 |

## Keys shipped

| Key | Root / group | Launch (local opening day) | Close CT | Eras |
|---|---|---|---|---|
| `globex_gold_tas` | `GCT` / TG | 2010-04-11 (trade date 2010-04-12) | 12:30 | closure, launch, 2011-04-10, 2012-04-15 |
| `globex_silver_tas` | `SIT` / MT | 2010-04-11 (trade date 2010-04-12) | 12:25 | closure, launch, 2011-04-10, 2012-04-15 |
| `globex_copper_tas` | `HGT` / HT | 2011-01-23 (trade date 2011-01-24) | 12:00 | closure, launch, 2011-04-10, 2012-04-15 |
| `globex_platinum_tas` | `PLT` / PE | 2017-05-21 (trade date 2017-05-22) | 12:05 | closure, launch |
| `globex_palladium_tas` | `PAT` / PX | 2018-11-18 (trade date 2018-11-19) | 12:00 | closure, launch |

All five: `tz: US::Central`, `regular: &[]`, `has_daily_close` and
`has_weekend_close` true, Sunday-Thursday 17:00 CT wrapping to the stated close,
no Friday-evening reopen, every inter-trade-date gap over four hours and
therefore `Closed` rather than `Maintenance` (stated in the module comments).
Zero executable revision rows on any key, launch to today. The two dated
revisions are order-entry only and touch the COMEX three alone.

## Files

New:

- `src/calendar/schedules/futures/us/metals_tas.rs` (418 lines) — gold, silver,
  copper; the shared MRAN chain; both order-entry revisions.
- `src/calendar/schedules/futures/us/pgm_tas.rs` (224 lines) — platinum,
  palladium; one era each.
- `tests/futures_family_boundaries/cme_metals_tas.rs` (497 lines) — ten tests.

Modified: `src/calendar/futures_profile.rs` (488 lines after the five variant
docs, inside the 500-line guard), `src/calendar/futures_profile/profiles.rs`,
`src/calendar/schedules/futures/us/mod.rs`,
`tests/futures_family_boundaries/mod.rs`, `tests/schedule_documentation/mod.rs`,
`tests/venue_sessions/named_profiles.rs`,
`tests/unsupported_market_hours_keys.rs`, `tests/golden_grids.rs`,
`tests/golden/normal_week_grids.txt`, `docs/schedules/verification.md`,
`docs/schedules/sources.md`, `docs/schedules/audit-2026-08-22.md`,
`README.md`, `CHANGELOG.md`. Seventeen files, +1411 / −36.

## Registration surface — all thirteen conventions items

1. Enum rows + canonical names + variant docs in `market_hours_keys!`. ✅
2. `hours_for_market_hours_key` arms; the date-aware
   `calendar_for_market_hours_key` surface needs no arm and is exercised on both
   sides of every dated row by the new tests. ✅
3. `session_profile` arms + five `FuturesSessionProfile` statics. ✅
4. `pub(crate) use` re-exports in `schedules/futures/us/mod.rs`. ✅
5. `EXPECTED_MARKET_HOURS_KEY_NAMES` 31 → 36. ✅
6. `EXPECTED_MARKET_HOURS_KEYS`. ✅
7. `SUPPORTED_FAMILY_NAMES`. ✅
8. Five ledger rows, Basis **Partial** / `Gap: executable`, `Reviewed on`
   **2026-09-12** (from `date -u`, not the machine's local day, which runs ten
   hours ahead), six cells each, no `|` inside any cell. ✅
9. `sources.md` — no new source set; `US-CME-GROUP` **Status** counts fourteen →
   nineteen and thirteen → eighteen Partial, plus a paragraph covering the five
   families and their channel provenance. ✅
10. `CHANGELOG.md` `[Unreleased]` / **Added** bullet. ✅
11. README: headline count 30 → 35, `MarketHoursKey has 31 variants—30` → `36
    … 35`, gap-kind split `35 order-entry to 17 executable across the 52 rows`
    → `35 … 22 … 57`, the executable enumeration extended to name all five,
    `30 of 30` → `35 of 35`, `twenty-four are Partial` → `twenty-nine`,
    test-inventory `31 … (30 …)` → `36 … (35 …)`, and the CME Globex coverage
    row's prose. The dated audit report's matching counts too. ✅
12. Golden regenerated; diff is a single `681a682,706` hunk — 25 added lines, no
    existing line changed, **no other key's rows moved**. ✅
13. New submodule `tests/futures_family_boundaries/cme_metals_tas.rs`,
    registered in that directory's `mod.rs`; the root was not fattened. ✅

## Verdict corrections folded in

- RA0907-4's complete Globex TAS list quoted as its **eleven** real codes
  (`WST RTI BHT HPT HHT BBT CLT HOT NGT RBT RET`); `BZT` is not among them and
  is not quoted.
- RA1102-4 cited with its sha256
  `a71fb96d6821ed4396be3c726c42beb9e299b55ae3f9e1de2a2b2706df193607`.
- The 2012-09-14 and 2013-09-02 hours-page captures cited, so the staleness of
  the 2012-06-16 weekday cell is *evidenced* rather than asserted over a later
  observation.
- Observation gaps named beside the rows: 2015-03-22 → 2019-11-18 for the COMEX
  three (channel exhaustion, stated as such), platinum 2021-04-11 → 2026-03-10,
  palladium 2021-05-13 → 2026-05-27.
- productId **445 = palladium, 446 = platinum**, recorded in `pgm_tas.rs`.
- The 2015-08-17 notice's own stated day is **Monday 2015-09-21**, not
  "trade date 2015-09-20".
- The handoff's "unsourced 2021-07 → today" and "MST … presumably 2023+" both
  corrected implicitly by the citations used (the archived ContractSpecs API
  channel; `MST` listed 2025-07-27).
- The handoff's characterisation of the palladium specification as the strongest
  document in the group is corrected in the module comment: the strongest are
  RA1006-4 and RA1107-4.

## "Do not" items written into the module comments

- Copper ≠ palladium on their coincident 12:00 CT close (COMEX vs NYMEX, HT vs
  PX, seven years apart, different settlement determination ranges); the
  `globex_mini_grains` precedent cited.
- No 16:00-17:00 CT daily break on palladium TAS; the clause is inherited
  boilerplate CME deleted by 2020-11-26 with the instants untouched.
- No pit or open-outcry window on any of the five, with the full pit-era history
  (gold and silver only, never copper; no window of its own; CME's own pit
  column wrong for copper and empty for silver).
- Member listings — `MGT`, `QOT`, `1OT`, `MHT`, `MST`, `HG0` — are caller
  catalog data and date no revision row.

## Withheld

- Sunday **16:00-16:15 CT** on gold, silver and copper: the sourced
  intersection under "a knowledge boundary may only widen", cross-referenced to
  `globex_equity_index`'s identical withholding and to issue #79. Platinum and
  palladium launched after the undated move and withhold nothing.

## Tests and mutation checks

Ten new tests. **Test count 544 before, 554 after**; doctests 3, unchanged.

Every one of the **eleven** dated revision rows was mutated one day, confirmed
red, restored, confirmed green. No mutation survived:

gold 2010-04-11, gold 2011-04-10, gold 2012-04-15, silver 2010-04-11, silver
2011-04-10, silver 2012-04-15, copper 2011-01-23, copper 2011-04-10, copper
2012-04-15, platinum 2017-05-21, palladium 2018-11-18.

## Gates

`cargo fmt --all --check`, `cargo clippy --all-targets -- -D warnings`,
`cargo nextest run --all-targets` (554/554), `cargo test --doc` (3/3),
`RUSTDOCFLAGS="-D warnings" cargo doc --no-deps`, `cargo deny check`, and
`cargo +1.95 check --all-targets` — all pass, run after the mutation checks were
restored.

One clippy fix was needed along the way: `type_complexity` on the test module's
`KEYS` table, resolved with two local `type` aliases (`Ymd`, `Hm`).

## Issues opened (before the text citing them was written)

| # | Title |
|---|---|
| [#79](https://github.com/SharurTrading/exchange-hours-rs/issues/79) | CME's undated 2012 Sunday Pre-Open move 16:15→16:00 CT: `globex_equity_index` and the five metals TAS keys are the same open question |
| [#80](https://github.com/SharurTrading/exchange-hours-rs/issues/80) | Copper Spot TAS (`HG0`): the listing day is undated, with an upper bound of 2018-08-10 only |
| [#81](https://github.com/SharurTrading/exchange-hours-rs/issues/81) | Metals TAM product codes are not monotone across captures: gold `GC7`→`GCD` and copper `HGK`/`HGF` |
| [#82](https://github.com/SharurTrading/exchange-hours-rs/issues/82) | NYMEX softs TAS (`KTT`, `CJT`, `TTT`, `YOT`) plus `XKT`/`XCT` and `RET`: sourced daily closes the MRAN chain states and no key holds |

**Deviation from the spec, stated:** the spec said to cross-reference "the
existing `globex_equity_index` issue rather than opening a duplicate" for the
undated Sunday move. **No such issue existed** — a search of all open and closed
issues found none tracking that bracket, though `globex_equity_index`'s ledger
row records it. So #79 was opened to cover both families as one question, and it
names `globex_equity_index` explicitly. That is the smallest change consistent
with LAW-FOLLOW-UPS-ARE-ISSUES; if the maintainer knows of a pre-existing issue
elsewhere, #79 should be closed as a duplicate of it.

## Nothing else skipped

Every item of the PR 2 specification was implemented. The PR was **not** merged,
as instructed.

## One thing that happened mid-flight

`trade-type-fences` gained `dd940d7` ("PR 1: CodeRabbit round two") while this
branch was open, which among other things sharpened the plan's date-aware-surface
convention to require registration, history, cutover **and boundary** tests on
both sides of the opening day. This branch was already based on that tip, the
new tests satisfy the sharpened convention, and the commit here does not touch
that plan file.
