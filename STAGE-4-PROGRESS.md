# Stage 4 — progress note

**2026-09-25 (UTC).** A consolidated state note for whoever picks this up. It
supersedes the per-round entries in `STATUS.md` for orientation; `STATUS.md`
remains the running record and `STAGE-4-HANDOFF.md` (written at the end of
Stage 3) is still the entry point for the stage as a whole. The plan's §8 and
#116 are the authority.

## Where it stands in one line

**Five PRs, all CI-green, all unreviewed.** No maintainer review has been posted
on any of them across this session, and `main` has not moved from `4066bfd`.

| PR | Branch | Head | Content |
|---|---|---|---|
| [#131](https://github.com/SharurTrading/exchange-hours-rs/pull/131) | `stage-4-130-overlap` | `4677e9d` | **Engine**: settles #130 — a replacement block that meets the next trade date's open takes its place, so `session_bounds` and `trade_date` describe one session |
| [#133](https://github.com/SharurTrading/exchange-hours-rs/pull/133) | `stage-4-energy` | `1074de2` | **Data**: `globex_energy`'s three Saturday-session trade dates |
| [#134](https://github.com/SharurTrading/exchange-hours-rs/pull/134) | `stage-4-equity-index` | `d0fa12e` | **Data**: `globex_equity_index`'s same three dates; carries #133's reconciliation |
| [#136](https://github.com/SharurTrading/exchange-hours-rs/pull/136) | `stage-4-rates-fx` | `2da8f14` | **Data**: `globex_interest_rates` + `globex_fx`, shared-operator PR |
| [#137](https://github.com/SharurTrading/exchange-hours-rs/pull/137) | `stage-4-nikkei` | `7a0ec34` | **Data**: `globex_nikkei_225_dollar`'s same three dates |
| [#135](https://github.com/SharurTrading/exchange-hours-rs/pull/135) | `stage-4-stack` | `ec3a383` | **Integration only, draft, do not merge**: `main` + #131/#133/#134/#136, verified at **1006/1006**. Does **not** include #137 yet |

**Merge order: #131 → #133 → #134 → #136 → #137.** #134 already contains #133, so
those two do not conflict; **#136 conflicts with both** in five files
(`CHANGELOG.md`, `docs/schedules/coverage-2025.md`,
`src/calendar/schedules/holidays/venues/cme.rs`, `docs/evidence/cme.md`,
`tests/venue_sessions/holidays_cme_venues.rs`) — all the same collision shape, a
row or counter an earlier PR already moved. #136's resolution can be taken from
`stage-4-stack` rather than reproduced.

**Reviewer caveat.** #134's diff against `main` shows **six** `ReplacementBlocks`
rows and two CHANGELOG entries, not three and one, because it carries #133's
reconciliation. Read it as *stacked on #133*, not as claiming those rows.

## What each PR was checked against

Every PR ran the full chain at its head (fmt, `clippy --all-targets -D warnings`,
`nextest --all-targets`, doctests, `doc -D warnings`, `cargo deny`,
`cargo +1.95 check --all-targets`). Every shipped row was re-derived from the
operator bytes by `STAGE-4-AUDIT-rows.py`, and all six rows resolve with no cited
window silent for its trade date. Every family's rows were mutation-checked.

**#131 also has a benchmark comparison** against a same-machine `main`→`main`
control (branch median 0.991×, control spread 1.012× median with a 1.390× max
row); the four criterion runs are `STAGE-4-BENCH-*.txt` here.

## What remains

| Item | State |
|---|---|
| `globex_nikkei_225_dollar` Saturday-session rows | **Authorable now.** Retrieval done and shape verified (round 11): same three blocks as `globex_energy`, artifacts `live/extra/extra_2026-06-18_2026-06-20.md` (`d7ed6858…`) and `live/extra/extra_2026-07-03_2026-07-05.md` (`7839fef6…`) |
| `globex_fx` + `globex_cryptocurrency` **merged trade dates** | **Stateable, but deliberately not written — a design decision, not a data gap.** Measured in round 16: the merge changes only which trade date owns Sunday evening through Monday 16:00, with `is_open` agreeing at every instant. Stating it would reassign two dates' worth of `trade_date` answers on the strength of a label the operator prints and the crate's convention contradicts. In scope under LAW-HOLIDAY-SCOPE, but it needs an explicit acceptance. Analysis in `STAGE-4-BLOCK-ROW-RECIPE.md` shape 3 |
| **#132** — order-entry queries on dates with a withheld phase | **Withdrawn as a defect (round 19); it is documented policy.** `require_phase_coverage` refuses the order-entry API for any date a declared phase-level gap applies to, which for the CME families is every date before the #79 bound. `is_open` still answers. Both halves are fenced by `tests/coverage_query_errors.rs::a_withheld_phase_refuses_the_order_entry_query_but_not_the_session_query`. What remains is a **design question for the maintainer**: the refusal is by whole date, so a fully-sourced instant inside the Monday-Thursday `16:45-17:00` queue is refused along with the withheld quarter-hour |
| ~~`globex_grains`, `globex_livestock` residual scalar work~~ | **Not Stage 4 work — struck in round 20.** Both ship `complete to 2027-12-31` with no `Unsourced` 2025+ dates. Their remaining gaps are historical (the 2012-2013 grains queue regime, the 2016-2020 livestock PCP) and lie **below the 2025 floor**, so they are out of Stage 4's interval and the plan supersedes further retrieval on them; Stage 5 owns the affected eras |
| `globex_equity_index`, `globex_energy`, `globex_interest_rates`, `globex_fx` completeness | All four still withhold the Sunday 16:00-16:15 CT quarter-hour (#79) |

`STAGE-4-BLOCK-ROW-RECIPE.md` (this directory) has the block geometries, the
rules a row author trips over, and the probe procedure. Read it before writing a
row; it exists so the remaining families are bounded work rather than a repeat of
the survey.

## Two process lessons that cost real time here

1. **A hand-resolved merge conflict can parse, look plausible, and have silently
   lost content.** Twice in the #135 stack a conflict resolution dropped an
   inventory row while leaving a valid-looking table. A row-counting fence caught
   both (`inventory_sample_date_is_inside_every_scopes_audit`,
   `the_coverage_inventory_repeats_the_ledger_horizons`). Verify a resolution by
   whether the structure is still whole, not by whether it compiles.
2. **Check a fixture's dates against the coverage window, not just the acceptance
   list.** Two of this session's blocked queries were correct refusals for dates
   outside an identity's published range, and I twice mistook them for defects
   before probing `main`.

## Environment state owed

Five worktrees exist (`eh-wt-130`, `eh-wt-energy`, `eh-wt-equity`,
`eh-wt-ratesfx`, `eh-wt-stack`) against the convention of one. They should be
removed and their branches deleted once the PRs land, and #135 closed. Each
branch is in sync with its remote at the heads above; every tree is clean.

Two live-retrieval sets were added to the store this session and are recorded in
the evidence files they belong to: the energy/equity Sunday windows, and the
Nikkei `THBP-B` windows.
