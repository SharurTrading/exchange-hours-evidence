# Ledger reshape — assembly result

Written 2026-09-12 (UTC). Branch `ledger-reshape`, commit `e1738ae`,
PR <https://github.com/SharurTrading/exchange-hours-rs/pull/87>.

## What shipped

- **132 ledger rows rewritten** in `docs/schedules/verification.md` to the
  eleven-cell shape, both tables sharing one header. 132 rows before, 132 after;
  same identities, same order, none lost or duplicated. No `|` inside any cell
  (enforced by the eleven-cell assertion), every basis note one to three
  sentences.
- **Prose above both tables rewritten** to describe the eleven columns; the
  "row shape changes in a coming reshape" paragraph deleted; the "evidence
  remains beside the owner code until LAW-EVIDENCE-FILES" sentences replaced by
  a pointer to `docs/evidence/`; the `## Basis` vocabulary closed at four values
  with a retired-labels paragraph; the per-row `Systems in scope` clauses gone
  from the table (19 of them now live in evidence files) while the
  system-coverage audit section, its method, discrepancy list and side-lists
  stay.
- **Fences updated and extended.** `tests/schedule_documentation/mod.rs`
  (eleven-cell shape, closed vocabularies for basis / tier / service / cadence,
  horizon format, three-sentence cap, dormant↔on-demand cross-check,
  `owner_targets` for the two-link Owner cell, `basis_of` / `is_partial` /
  `evidence_target`, gap-kind split counted from the Basis cell, four-column
  distribution strings, plus a new
  `readme_states_the_service_tier_split_from_the_ledger`), `databento.rs`,
  `trade_type_keys.rs`, and the new `evidence_files.rs` with eight tests
  including the two the brief required. 32 documentation fences, all green.
- **Other documents:** `docs/schedules/databento-venues.md` (50 basis cells plus
  its explanatory paragraph), `docs/schedules/audit-2026-08-22.md` (four-column
  distribution table, retired-labels sentence), `README.md` (four-value
  vocabulary, service-tier sentence, gap-kind sentence),
  `docs/schedules/updating.md` (records list, basis list, service/cadence/
  horizon paragraph, step 4 declaration rule, step 5 row shape),
  `docs/schedules/sources.md` (intro), `CHANGELOG.md` under
  `[Unreleased]` / **Changed**.

## Gate chain

`bash …/gates.sh` green end to end: fmt, clippy `-D warnings`, nextest
(561 passed), doctests, `RUSTDOCFLAGS="-D warnings" cargo doc`, `cargo deny`,
`cargo +1.95 check`.

`tests/golden_grids.rs` untouched. `git diff -- src/` filtered of comment lines
prints only one rustfmt reflow of a `revisions!` tuple in
`coinbase_derivatives.rs` whose five values are byte-identical before and after;
no rule datum changed anywhere.

## Blocked cells resolved

Ten rows arrived with `?` in the Horizon cell, every one of them a case §1.3
does not enumerate: the baseline below the earliest revision row is attested by
no dated artifact, so it is neither a launch closure (`—`), nor sourced through
the floor (`2010-01-01`), nor carried from a readable day `D`.

**Resolution: the horizon is the effective day of the earliest revision row.**
That is where the row's sourced record starts; everything below it is carried.
It is the same reading already applied by other groups to `nyse_national`
(2010-08-02), `nasdaq` (2013-03-18), `hkex` (2011-03-03), `jse` (2012-05-25) and
`bmv` (2010-02-18), so the column stays internally consistent.

| Row | Horizon | Earliest revision row |
|---|---|---|
| `nyse` | 2018-04-09 | SEC 34-83230, UTP Pillar production |
| `nyse_american` | 2017-07-24 | NYSE American Pillar update 2017-07-21 |
| `asx` | 2025-06-23 | ASX SR15 notice 0473.25.05 |
| `nzx` | 2020-04-06 | NZX announcement 350919 |
| `sgx_securities` | 2011-08-01 | SGX-ST Rules 2011-08-01 |
| `set_thailand` | 2024-03-25 | SET notification 86864800 |
| `pse` | 2011-10-01 | PSE circular CN-2011-0013 |
| `krx` | 2016-08-01 | FSC notice 73613 |
| `borsa_istanbul` | 2012-03-02 | Borsa Istanbul closing_session |
| `tadawul` | 2013-06-29 | SPA news 7e453de27d |

Each of the ten evidence files' gap bullet was rewritten from "horizon
undetermined / unresolved" to "horizon carried below the first dated row",
stating the resolved date and keeping its closing condition, which would move
the horizon earlier (to the floor where a floor-era artifact exists). Three
basis notes that said "the horizon is not yet fixed / unresolved" (`pse`,
`borsa_istanbul`, `tadawul`) were corrected in the same edit.

## Migrator flags, adjudicated

1. **`globex_nikkei_225_dollar` horizon outside §1.3's three cases — accepted as
   `—`.** The column's own definition governs: nothing is carried below
   2011-01-12 (`nkd_profile_at` returns `NKD_CLOSED`), so no date is owed. A
   fourth case is not needed; the same reading already produced `—` for
   `sgx_equity_index_taiwan` and `sgx_equity_index_ntr_usd`.
2. **`globex_nikkei_225_dollar`'s stale Notes sentence — left verbatim in
   `## Ledger basis`, contradiction recorded.** The section is the audit trail
   for the distillation, so it is copied without editing; the contradiction and
   which statement is authoritative are recorded under `## Gaps and residual
   risks`, and the new Basis note follows the module. Rewriting the verbatim
   copy would destroy the only record of what the row used to claim.
3. **`cbot` / `globex_grains` at 2010-03-15 and `comex` / `nymex` /
   `globex_energy` at 2012-05-11 — accepted.** The horizon describes the row,
   not one phase of it: below the latest carry-start some part of the served
   baseline is carried rather than sourced, and a reader who needs the matching
   grid's own earlier sourcing finds it in the evidence file.
4. **`cargo fmt --all` run by the group-A agent — no residue.** The full chain
   is green and the only formatting change surviving in `src/` is the
   `coinbase_derivatives.rs` tuple reflow described above.
5. **Dated cutovers encoded outside `revisions!` (`europe.rs`,
   `coinbase_derivatives.rs`, and also `vienna.rs`, `binance.rs`,
   `ice_abu_dhabi.rs`, `ice_endex.rs`, `ice_europe.rs`) — accepted as a real
   fence limit and opened as issue #86.** `assert_revision_bullet` checks those
   files' bullets for grammar and leaves attribution unclaimed rather than
   pretending to cover them, and the fence's doc comment says so and cites the
   issue.

## Follow-ups opened (LAW-FOLLOW-UPS-ARE-ISSUES)

- **#85** — drain `NARRATIVE_DEBT`: 41 schedule modules still carry plain-comment
  runs over six lines, the heaviest being
  `futures/international/sgx_equity_index/history.rs` (310 lines). The list only
  shrinks; `modules_carry_no_narrative` asserts every unlisted module.
- **#86** — dated cutovers encoded as `NaiveDate` constants or selector
  comparisons are invisible to the day fence.

## Issues the PR closes

Both are dormant identities, so LAW-FOLLOW-UPS-ARE-ISSUES is discharged by
recording the gap and its closing condition in the evidence file — which is now
the case:

- **#66** — `docs/evidence/sgx_equity_index_japan.md`, restated in
  `sgx_equity_index_china.md` and `sgx_equity_index_singapore.md`: the 2016 move
  to the 04:45 T+1 grid is bracketed to (2015-12-24, 2017-07-05) with the change
  log's two undated 2016 entries quoted; closing condition is a reachable copy
  of DT/AM 80 of 2016 or another SGX artifact stating the day.
- **#80** — `docs/evidence/globex_copper_tas.md`: `HG0`'s listing day is undated
  with an upper bound of 2018-08-10 only, the Product Code cell demonstrably
  drops TAS codes that exist, and all seventy archived weekly Globex notices
  from 2017-06-05 to 2018-08-27 are silent. The closing condition was **added in
  this change** (it was in the issue body but not the file): a COMEX rule filing
  or a CME Globex notice naming `HG0` on a stated day, with the CFTC
  rule-filing channel and the pre-2017 Globex notice archive named as where to
  look next.

## Counts, before and after

| Measure | Before | After |
|---|---:|---:|
| Ledger rows | 132 | 132 |
| `Exchange` Primary / executable / order-entry / synthetic | 67 / 3 / 25 / 1 | unchanged |
| `MarketHoursKey` Primary / executable / order-entry / synthetic | 6 / 19 / 10 / 1 | unchanged |
| Gap-kind split | 35 order-entry to 22 executable | unchanged |
| Repository cutoff | 2026-08-22 | 2026-08-22 |
| Evidence files | 0 | 132 |
| Documentation fences | 24 | 32 |
| Comment lines in `src/` | — | 3,820 removed, 850 added |

## Review fixes (2026-09-12 UTC, commit 715e515)

Seven confirmed review findings applied on branch `ledger-reshape`, committed as
`Ledger reshape: review fixes` and pushed; PR #87's body gained a `## Review`
section stating the same seven.

| # | Where | Fix |
|---|---|---|
| 1 | `verification.md` :185, :454, :458 | `cme`, `globex_equity_index`, `globex_fx` horizon `2010-01-01` → **`2012-05-03`** (SPEC §1.3 case 3; the 2012-05-03 equities/FX-hours captures are these families' earliest artifacts, not the 2012-05-11 index capture the energy rows key to). `globex_interest_rates` deliberately left at `2010-01-01` — Globex notice 20090326 is a pre-floor T1 table, so case 2 holds. `cme.md`, `globex_equity_index.md`, `globex_fx.md` order-entry gap bullets each gained the carry-start sentence. |
| 2 | `verification.md` :222–:225 | The four Euronext legacy rows `2010-01-01` → **`2010-12-24`**; the conditional horizon bullet at :37 of all four evidence files discharged into the resolved horizon plus its closing condition (Lisbon keyed to its own 06:15/08:00/16:30/16:40 grid). |
| 3 | `verification.md` :212 | `idx` `2010-01-01` → **`2010-08-31`** (capture date of the archived IDX trading-hours page). Basis note and `idx.md` unchanged — the residual risk was already recorded at `idx.md:31`. |
| 4 | `verification.md` :216 | `szse` `2010-01-01` → **`2016-05-09`**; third basis sentence replaced so the three-sentence cap holds (the dropped ChiNext / 2026-07-06 sentence survives at `szse.md:12` and `:29`); `szse.md` gap bullet restated with the resolved horizon and its closing condition. |
| 5 | `tests/schedule_documentation/evidence_files.rs` `comment_run` | Upward walk no longer skips arbitrary non-blank, non-comment lines; only the binding line and attributes stacked on it are stepped over. **Mutation-checked both ways**: an undeclared second `revisions!` block glued to `tse.rs` passes the pre-fix fence and fails the post-fix one (`every revisions! block needs exactly one // Evidence: line above it`, `left: 0 right: 1`), failing both `every_revisions_block_declares_its_evidence_files` and `every_evidence_revision_line_exists_in_source`. Probe reverted; `src/` is clean. |
| 6 | `verification.md` :59–:61, `updating.md` :26–:31, `CHANGELOG.md` | Both user-facing records stopped claiming the narrative move is complete. Each now names the 41 modules in `NARRATIVE_DEBT` and issue #85, which until now was cited only inside the test file. |
| 7 | Twelve evidence files, `## Revision rows` line | The seven US options files scope "single static profile" to the identity and say `options/history.rs`'s blocks belong to post-floor launches; `eurex`, `eurex_key`, `eex` name the `eurex_profile_at` / `eex_profile_at` comparisons carrying 2018-12-10 and 2024-03-25; `always_open` and `unknown` (found in the same pass) now name `ALWAYS_OPEN_PROFILE` in `schedules` instead of modules that define no profile. `bursa_malaysia.md` and `tsx.md` left alone — already true. Every line still opens `None.`, so the section fence stays green. |

No rule datum changed; no `src/` file was modified by these fixes.

Gate chain re-run green after the fixes: `cargo fmt --all --check`,
`cargo clippy --all-targets -- -D warnings`, `cargo nextest run --all-targets`
(561 passed, 0 failed), `cargo test --doc` (3 passed),
`RUSTDOCFLAGS="-D warnings" cargo doc --no-deps`, `cargo deny check`,
`cargo +1.95 check --all-targets`.
