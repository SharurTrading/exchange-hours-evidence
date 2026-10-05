<!-- SPDX-License-Identifier: MIT-0 -->

# ASSEMBLE — result

**Assembled:** 2026-09-12 (UTC, `date -u`, LAW-UTC-DATES)
**Branch:** `holiday-tables` in `/Users/agedvagabond/Developer/exchange-hours-rs`
**Commits:** `b870f1b` (the engine, replayed) and `ff7c0c0` (the tables)
**PR:** <https://github.com/SharurTrading/exchange-hours-rs/pull/96> — base `main`, +10,975 / −239 across 74 files
**Gates:** green, twice (before and after the rebase)
**Golden file:** `tests/golden/normal_week_grids.txt` is byte-identical to `main`

---

## 1. What shipped

**427 holiday rows across 17 `holidays!` blocks, serving 22 of the 132 ledger identities.** Every row is sourced; there is not one `Unsourced` row in the wave.

| Block | Identities served | Coverage (trade dates) | Rows | Tier |
|---|---|---|---|---|
| `globex_equity_index::TABLE` | `globex_equity_index` | 2025-01-01 .. 2027-12-31 | 36 | T2 |
| `globex_interest_rates::TABLE` | `globex_interest_rates` | 2025-01-01 .. 2027-12-31 | 36 | T2 |
| `globex_nikkei_225_dollar::TABLE` | `globex_nikkei_225_dollar` | 2025-01-01 .. 2027-12-31 | 36 | T2 |
| `globex_energy::TABLE` | `globex_energy` | 2025-01-01 .. 2027-12-31 | 36 | T2 |
| `globex_livestock::TABLE` | `globex_livestock` | 2025-01-01 .. 2027-12-31 | 36 | T2 |
| `globex_grains::TABLE` | `globex_grains` | 2025-01-01 .. 2027-12-31 | 40 | T2 |
| `globex_cryptocurrency::TABLE` | `globex_cryptocurrency` | 2025-01-01 .. 2027-12-31 | 32 | T2 |
| `globex_fx::TABLE` | `globex_fx` | 2025-01-01 .. 2027-12-31 | 19 | T2 |
| `cfe::TABLE` | `cfe`, `cfe_vix` | 2026-01-01 .. 2026-12-31 | 12 | T1 |
| `eurex::TABLE` | `eurex` (venue), `eurex`, `eurex_fixed_income` | 2026-01-01 .. 2026-12-31 | 7 | T1 |
| `ice_us::VENUE` | `iceus` | 2026-01-01 .. 2028-01-03 | 24 | T1 |
| `ice_us::FANG` | `ice_us` | 2026-01-01 .. 2028-01-03 | 22 | T1 |
| `ice_us::SUGAR_COFFEE_COCOA` | `ice_us_sugar`, `ice_us_coffee`, `ice_us_cocoa` | 2026-01-01 .. 2028-01-03 | 21 | T1 |
| `ice_us::COTTON` | `ice_us_cotton` | 2026-01-01 .. 2028-01-03 | 21 | T1 |
| `ice_us::DOLLAR_INDEX` | `ice_us_dollar_index` | 2026-01-01 .. 2028-01-03 | 21 | T1 |
| `ice_us::ORANGE_JUICE` | `ice_us_orange_juice` | 2026-01-01 .. 2028-01-03 | 20 | T1 |
| `coinbase_derivatives::TABLE` | `coinbase_derivatives` | 2026-01-01 .. 2026-09-07 | 8 | T1 |

Eurex 2027 does **not** ship: Eurex publishes it "on a preliminary and indicative basis", which LAW-NO-FABRICATED-DATES does not admit.

Largest production file is `holidays/ice_us.rs` at 366 lines; every other holiday module is 50–192. Nothing is near the 500-line guard, so the memo's "no need to fragment by decade" sizing holds with room for Waves 2–6.

---

## 2. Wiring (brief step 1)

Six modules were left undeclared by the encoders and are now wired: `globex_cryptocurrency`, `globex_equity_index`, `globex_fx`, `globex_grains`, `globex_interest_rates`, `globex_nikkei_225_dollar`. Six routing arms added to `for_market_hours_key`. The other six modules (`cfe`, `coinbase_derivatives`, `eurex`, `globex_energy`, `globex_livestock`, `ice_us`) were already wired and were left alone.

Every module uses the reference form `pub(crate) static TABLE: &HolidayTable`, so the routing arms are `Some(super::<module>::TABLE)` with no `&`. Three encoders flagged this as a departure from the task brief's shorthand; they agree with each other, with W0-3 and with the arms already in the tree, so the brief's `pub(crate) static TABLE: HolidayTable` is the odd one out and no module was changed.

**`MarketHoursKey::GlobexMiniGrains` stays `None`** — dormant, and the grains module says mini grains are a separate key and a separate table. **`Exchange::Cme`, `Cbot`, `Comex`, `Nymex` stay `None`** — see §4.

The `mod.rs` and `routing.rs` module docs, which both said "no table ships in this wave", were rewritten to state what actually ships and what deliberately does not.

---

## 3. The four test failures, and what each one was (brief step 2)

Wiring the tables broke exactly four tests. None was a defect in an encoder's work.

| Test | Cause | Fix |
|---|---|---|
| `without_holidays_changes_no_answer_while_no_table_ships` | the name is the claim, and the claim is now false | renamed to `without_holidays_is_the_identity_without_a_table_and_a_detachment_with_one`; the identity-function claim survives for tableless identities, and an identity **with** a table must now diverge somewhere in the Christmas probe window |
| `policy_calendar_mirrors_the_builtin_accessors` | its caller overrides sat on 2025-12-24 and 2025-12-25, both now built-in rows | overrides moved to 2025-12-23 / 2025-12-26; the test additionally asserts the crate's own Christmas row and its coverage window **do** come through the `PolicyCalendar` wrapper |
| `an_out_of_range_boundary_is_unavailable_and_never_rolls_a_trade_date` | probed Friday 2026-06-19, now a built-in crypto `Closed` row, so the built-in layer was rolling the trade date before the caller's layer was reached | moved to Friday 2026-08-21, which carries no row; the test now asserts `holiday_on` is `None` there rather than trusting the date |
| `cme_mini_grains::mini_grains_and_the_standard_grain_grid_disagree_outside_the_converged_eras` | the converged-week probe contains Juneteenth 2026-06-19; `globex_grains` is served and has a table, `globex_mini_grains` is dormant and does not | the `session_state` comparison detaches the holiday layer on both sides, with the reason in a comment. The two keys agree on the **grid**, which is what the test's name claims; they differ on the layer, which is a service-tier fact |

After the fixes: **749 tests, 749 passed.** The suite grew from 629 (the state one encoder measured in isolation) to 749 because every encoder's test module now compiles and runs, plus two new benchmark classes and two new documentation fences.

---

## 4. The four CME venue calendars ship no table

`cme`, `cbot`, `comex`, `nymex` answer `None` to `holiday_coverage()` even though every family that routes to them now has a table. A venue's table is the **intersection** of those families (memo D17): full closures agree, most early closes do not, and a date where two disagree can ship no venue row at all. Publishing one family's early close as the venue's would be a fabrication; dropping the disagreements silently would make the coverage window a lie.

Each of the four evidence files gains a `holidays, no table` bullet under `## Gaps and residual risks`, naming D17, Wave 7 and **#95** as the closing condition, and saying what a consumer should do meanwhile: route through the product-family key rather than the venue. Recorded as **W1-ASM-2**.

---

## 5. The ledger (brief step 4)

**A twelfth column, `Holidays`, between `Horizon` and `Reviewed on`.** `LEDGER_CELLS` moves 11 → 12 and all 132 rows carry the cell: `first..last` for the 22 identities with a table, an em dash for the other 110.

The brief allowed the coverage window in the Basis note *or* a Horizon-adjacent column with the fences updated. The note was not viable: LAW-EVIDENCE-FILES caps it at three sentences and every row that gained a table was already at three, so the window could only have gone there by deleting something a reader needs more. The charter's consumer contract already says the ledger states "each identity's horizon and holiday coverage", so the column is what that sentence was describing.

**It is a record, not a claim.** `shipped_holiday_window` in `tests/schedule_documentation/mod.rs` resolves the row's wire name to its `Exchange` or `MarketHoursKey`, calls the crate's own `holiday_coverage()`, and asserts the cell equals it. A table that lands, moves its window or is withdrawn fails the ledger until the cell is corrected, and no cell can name a window the crate does not answer over. Recorded as **W1-ASM-1**.

`LEDGER_CELLS - 1` already indexed the evidence cell, so that fence followed the column automatically; the two hand-written indices that did not (`cells[7]` for a review date, and the Basis-note position) were moved.

---

## 6. Documentation (brief step 5)

- **README** — five passages rewritten. The three that said holiday tables "land in a separate change" now state what ships; the overlay passage names the three API items; the design bullet distinguishes the normal-week tables from the holiday tables. A new fence, `readme_states_the_holiday_coverage_count_from_the_ledger`, derives the "22 of the 132 ledger rows" count from the ledger's `Holidays` column and requires it **twice**, so neither mention can drift.
- **`docs/schedules/updating.md`** — a new `### Adding a holiday year` subsection under §4, in five steps: retrieve the operator calendar at T1/T2 over a continuous range; convert to the crate's trade date (with the holiday-eve rule that a withheld evening leg ships no row); encode through `holidays!` and wire the module and the routing arm; write the `## Holidays` evidence section with its `Documents` table; test the seven required cases and fence the absences, then the ledger cell, the README count and the CHANGELOG. §3's one-off-holiday bullet now routes to the built-in table first and `DayPolicy` second. §5's "eleven cells" is now twelve.
- **`docs/schedules/date-exceptions.md`** — the overlay contract is unchanged and now says so explicitly, with the tightening rule (`OR` / `min` / `max`), a pointer to the ledger's `Holidays` column for which identities carry a table, and the three accessors.
- **`CHANGELOG.md`** — a new `[Unreleased]` / **Added** entry naming every identity and its years, the three API items, the T1/T2 split, the venue exclusion, and the measured numbers. The wave-0 entry was reconciled: it no longer claims "no family table ships in this version".
- **`AGENTS.md`** — three factual sentences updated, no law's intent changed. LAW-HOLIDAY-SCOPE's "**No table ships yet**" is replaced by a pointer to the ledger's `Holidays` column plus the audited-normal-vs-no-answer distinction; the Purpose section's "will also answer … once the tables ship" becomes the present tense; "They will live in per-family date tables" becomes "They live in".

---

## 7. Bench (brief step 6)

`BENCH-wave1.md`, written beside Wave 0's file rather than over it, as that file's §7 asked. Apple M2 Max, `rustc 1.97.1`, 2026-09-12 UTC; the `globex_equity_index` group is the **median of three clean runs**, because the first pass of that group overlapped a `cargo nextest` run and its figures were 20–50 % high.

| §6.3 measurement | Target | Wave 0 | Wave 1 | Verdict |
|---|---|---|---|---|
| `is_open`, regular, far from a holiday | ≤ +15 % | 236.1 ns | **240.9 ns** | **Met** (+1.7 %) |
| `is_open`, closed weekend, far from a holiday | ≤ +16 % | 482.3 ns | **481.0 ns** | **Met** — Wave 0's +20 % *Watch* clears, for the reason it predicted |
| `is_open`, on or adjacent to a holiday | ≤ 3 µs | 3.81 µs (proxy) | 5.40 / 5.99 µs | **Watch** — ~13 dates a year plus neighbours; §2.3 reduction 2 is the lever |
| cold frame, 4,999 `is_open` + 1 close | ≤ 1.3× | 3.103 ms | **2.962 ms** | **Met** (0.94×) |
| daily trading-day derivation | ≤ 30 µs | 12.42 µs | **12.41 µs** | **Met** |
| `StaticDayPolicy`, date not covered | ≤ 2× once `may_affect` ships | 15.8× | 15.6× | **Deferred to #94** |

`holiday_on` went from 310 ps to **5.04 ns** — the 310 ps was `table_for` answering `None` and the compiler folding the call away; 5.04 ns is the real binary search over a 36-row static slice.

**D19's merge precondition holds with real data.** The two far-from-a-holiday `is_open` rows are met, and the one Wave-0 *Watch* that was an artifact of measuring through `&dyn SessionExceptionSource` is now met on the built-in path, which has no virtual call in it.

The harness gained the two date classes §6.2 asks for (**W1-ASM-5**), both regular-session minutes so the only variable against `regular` is the date class. A first run used a *closed* minute on Good Friday 2026 and measured 19.0 µs; that is reported as the closed-instant observation it is, with its probe named, and not as the date-class figure.

---

## 8. Follow-ups opened (brief step 7)

Eight issues, each cited where the follow-up is named (LAW-FOLLOW-UPS-ARE-ISSUES). Memo §7 items 1 and 2 were already closed by the 2026-09-12 repair round, which is why no row in this wave is `Unsourced`.

| Issue | Memo §7 | Blocks |
|---|---|---|
| [#88](https://github.com/SharurTrading/exchange-hours-rs/issues/88) | 3 | Wave 5 — and it changes a recorded status, so it blocks rows, not just prose |
| [#89](https://github.com/SharurTrading/exchange-hours-rs/issues/89) | 4 | Wave 4 |
| [#90](https://github.com/SharurTrading/exchange-hours-rs/issues/90) | 5 | Wave 2 |
| [#91](https://github.com/SharurTrading/exchange-hours-rs/issues/91) | 6 | Wave 3 |
| [#92](https://github.com/SharurTrading/exchange-hours-rs/issues/92) | 7 | Wave 6, and the January-2010 floor |
| [#93](https://github.com/SharurTrading/exchange-hours-rs/issues/93) | 8 | the declared topology gaps; needs a LAW-HOLIDAY-SCOPE amendment, so maintainer's call |
| [#94](https://github.com/SharurTrading/exchange-hours-rs/issues/94) | 9 | `DayPolicy::may_affect` |
| [#95](https://github.com/SharurTrading/exchange-hours-rs/issues/95) | 10 | Wave 7 venue tables and the D17 audit |

`#93` and `#95` are cited in 12 evidence files (16 citations) at every point a gap names the block-row or venue-intersection follow-up.

---

## 9. Decisions recorded

Five assembly-level entries appended to `DECISIONS.md` under **Assembly**: W1-ASM-1 (the ledger column), W1-ASM-2 (the venue `None` arms), W1-ASM-3 (mini grains stays tableless, and the convergence test detaches the layer rather than dodging the holiday), W1-ASM-4 (the three reframed wave-0 assertions), W1-ASM-5 (the benchmark's date-class split). The per-family entries W1-CRYPTO-*, W1-FX-*, W1-ENERGY-*, W1-LIVESTOCK-*, W1-IR-*, W1-NKD-*, W1-EQUITY-*, W1-GRAINS-* and W8-* were written by the encoders and were not touched.

---

## 10. Deviations from the brief

1. **PR base is `main`, not `ledger-reshape`.** #87 squash-merged to `main` at 2026-09-12T08:58:20Z, before assembly. Its tree is byte-identical to the branch tip (`git diff origin/main 97bbbcd` is empty), so the branch was rebased `--onto origin/main` and the PR's diff is the holiday work alone. Targeting a merged branch would have produced a PR whose diff replayed the whole ledger reshape.
2. **A twelfth ledger column rather than a Basis-note sentence.** The brief permitted either; the note's three-sentence cap made it the wrong half of the choice. The fences are updated with it, as the brief required.
3. **The benchmark harness was extended**, which the brief did not ask for. `BENCH-wave0.md` §7 named the date-class split as the first thing Wave 1 should do, and measuring "on a holiday" through a caller's `DayPolicy` proxy when a real table now exists would have been reporting the wrong path.

## 11. Unrelated observations, and their disposition

One encoder flagged three tree-wide problems seen from an isolated copy. All three are clean in the assembled tree: `tests/schedule_documentation` passes all 38 fences including the comment-run guard on `globex_interest_rates.rs` and the `## Holidays` section fence on `globex_cryptocurrency.md`, and no `tests/zz_probe_livestock.rs` exists — whoever left it removed it before assembly.

---

# Review fixes — 2026-09-12 (UTC), commit `c9a48cd`

Thirteen confirmed findings from the branch review, all applied on
`holiday-tables` and pushed. PR #96's body gains a `## Review` section stating
each one. Decisions recorded as `W1-ASM-6` .. `W1-ASM-11` in `DECISIONS.md`;
the design memo's own corrections in its new §8.4.

## 1. Blocking

**Gate window** (`src/calendar/query/identity.rs`). `resolve_rule_bounds` dates
an occurrence by the local date of the **trading day's** final close, not of the
rule's own close, so an occurrence opening after its own trading day has closed
is dated by the next trading day — `D + 3` or more over a weekend. The gate's
`[D, D + 1]` was not a superset of that, and on six shipped families
(`globex_grains`, `globex_livestock`, `ice_us_sugar`, `ice_us_coffee`,
`ice_us_cocoa`, `ice_us_orange_juice`) the built-in table silently failed to
apply to the post-close order-entry windows, with the same query flipping when an
unrelated *empty* caller layer was attached. Replaced with the derivation's own
reach, `[D - 1, D + 19]`, widened per identity convention. `is_open` never
diverged; every diverging instant was order-entry-only.

**Gate-soundness fence** (`tests/holiday_tables.rs`). The old test could not
fail — one April-2026 fortnight over six classes, four of which ship no table
and two of which have no row within their gate reach.
`the_coverage_gate_is_sound_for_every_shipped_row` runs memo §4.2 to spec and
fails on `globex_grains` at 2025-01-17 20:47 UTC with the old arm restored. Old
test kept as `attaching_an_irrelevant_exception_provider_changes_no_answer`, plus
the named regression
`a_friday_order_entry_window_answers_the_same_with_and_without_an_empty_layer`.

**Not done, tracked as #97.** The sound window opens the gate on nearly every day
within 19 of a row, so §6's ~97 % exit rate and D19's precondition are not met by
this branch. The narrowing needs a proof from the static profile, not the identity
table's assumption; #97 carries it and the §6 re-measurement. It is also why the
new fence costs ~7 minutes in a debug build.

**`globex_cryptocurrency`'s nine five-day-era `[N3]` rows withdrawn.** Each
deleted 1380 minutes of published matching. No `[N6]` predecessor exists on the
preceding evenings, so the prior open was normal and only the trade-date label
moved; 16:00 CT is this family's own normal close. Declared trade-date-merge gaps
(#93), as `globex_fx` already reads the same records. 32 → 24 rows. Two family
tests inverted. With the rows gone the 24/7-era roll test still passes, which
disproves `W1-CRYPTO-6`'s second justification.

**Document-id collisions.** Two incompatible slug rules in one namespace. Three
ids resolved to two artifacts each, two artifacts carried two ids each. Every CME
service-window id is now `CME-SVC-<first eventDate>` with `-SAT`/`-PRE`: 111 ids
renamed across 8 evidence files, 8 modules, 3 test files. Every CME evidence file
normalized to one `### Documents` table in the fixed shape;
`globex_interest_rates.md` gains the sha256 column §3.2 requires. Three new
fences. Extending the shape to CFE/Eurex/ICE US/Coinbase is #98.

## 2. Should fix

- Saturday 2025-11-29 rows added to `globex_equity_index`,
  `globex_cryptocurrency` and `globex_nikkei_225_dollar`, so one operator closure
  is one uniform input to the D17 intersection (#95). Seven per-family records
  collapse into `W1-ASM-8`.
- Five public doc blocks that still asserted no table ships, rewritten.
- LAW-HOLIDAY-SCOPE's T1-only sourcing sentence corrected in `AGENTS.md` and
  `docs/schedules/sources.md`; the CME entry point now says the *service* behind
  the page is the T2 channel.
- `every_evidence_holiday_line_exists_in_its_module` closes the reverse direction
  of the holiday evidence fence.
- Six served rows move `quarterly` → `monthly`, held by a new `assert_row_shape`
  assertion.
- `holidays_eurex.rs` gains §4.1 case 6; it is the only test in the suite that
  fails under a one-arm gate-window mutation on `EurexFixedIncome`.
- `docs/schedules/updating.md`'s cell enumeration gains `holiday coverage window`.

## 3. Nits

- `globex_nikkei_225_dollar`: nine rows inferred from the Equity Index line, not
  eight, in both the module header and the evidence file.
- `docs/evidence/ice_us_cotton.md`: the conversion *justification* replaced; the
  identity conversion it concludes with was already correct, and the four sibling
  files' copies of the sentence are true as written and untouched.

## 4. Detail corrections to the findings as filed

- The grains divergence count is grid-dependent; the six-family set and the four
  `ice_us` counts reproduce.
- The finding on the gate window proposed `(0, 3)` as "the narrowest fix" while
  the same finding's own analysis gives `[D - 1, D + 19]` as the sound bound and
  says to land the sound window first. The sound window is what shipped; the
  narrowing is #97.
- `globex_cryptocurrency` ends at **24** rows (20 `closed`, 4 `early close`), not
  the 23 the finding states — the finding was written before the 2025-11-29
  addition, which is a `closed` row.
- `CME-SVC-2025-11-29` and `CME-SVC-B-2025-11-29`, the ids the 2025-11-29 finding
  proposed, do not exist under the id rule the collision finding mandates. The
  rows cite `CME-SVC-2025-11-26-SAT` and `CME-SVC-B-2025-11-26`, the artifacts
  whose windows actually reach the Saturday.
- `every_cited_document_id_is_resolved_exactly_once` is scoped to evidence files
  carrying the fixed `### Documents` table. Extending the shape to the non-CME
  families — whose ids are not date-slugged and cannot collide — is #98 rather
  than an unrecorded gap.

## 5. Verification

`tests/golden/normal_week_grids.txt` unchanged. Full gate chain green: fmt,
`clippy --all-targets -D warnings`, `nextest run --all-targets` (756 tests, 0
failed), doctests, `RUSTDOCFLAGS="-D warnings" cargo doc`, `cargo deny check`,
`cargo +1.95 check --all-targets`. Every new fence was mutation-checked against
the defect it guards.

## 6. Follow-ups opened

| Issue | Why |
|---|---|
| #97 | Prove the `[D, D + 1]` narrowing and re-measure the D19 overlay targets |
| #98 | Extend the fixed `### Documents` shape to CFE, Eurex, ICE US and Coinbase |
