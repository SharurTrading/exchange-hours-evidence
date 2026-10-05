# Stage 3 handoff — built-in special sessions (#93)

Written **2026-09-24** (UTC) at the end of the Stage 2 session. Read this, then
`docs/plans/2026-09-12-path-to-release.md` §7 (the authoritative task) and issue
**#93** (the design detail). This note is orientation and state, not a
replacement for either.

## Start here

`main` is `d5cf64f` — Stage 2B merged. It is **green**: fmt, `clippy --all-targets
-D warnings` (0 findings), **990/990** tests, doctests, `doc -D warnings`, MSRV
(`cargo +1.95 check --all-targets`), `cargo deny`. **#115 is closed**; Stage 2 is
complete.

Work in a worktree, never the primary checkout:
`git worktree add -b stage-3-blocks <path> main`.

Check `git worktree list` first — two worktrees exist today
(`exchange-hours-rs` on `main`, `exchange-hours-rs-2b` on the merged
`stage-2b-query-migration`, which can be removed).

## The task in one paragraph

`HolidayKind` is the scalar vocabulary of `DayPolicy`: closed, early close at an
instant, late open at an instant, or both. A special day whose **internal phase
topology** changes is not representable in it, so those days ship today as
declared coverage gaps on **served** identities. Stage 3 adds a fifth kind that
carries a static replacement block instead, reusing the existing replacement
resolver and validation rather than inventing a parallel mechanism. **Fixtures
only — no invented exchange data.** Operator rows land in Stage 4 (#116) with
their evidence.

## Files the engine work touches (~1,355 lines total, all small)

| file | lines | role |
|---|---|---|
| `src/calendar/exceptions.rs` | 264 | the exception vocabulary |
| `src/calendar/exceptions/static_table.rs` | 443 | `StaticSessionExceptions`, validation, coverage window |
| `src/calendar/query/replacement.rs` | 258 | the replacement resolver Stage 3 must reuse |
| `src/calendar/schedules/holidays/mod.rs` | 390 | `HolidayKind`, the `holidays!` macro and its const fences |

Precedence the plan fixes, and it is easy to get wrong: a built-in block replaces
the **complete trade date**; an explicit caller `Closed`/`ReplaceSessions` wins
over that arrangement; then `DayPolicy` clips the chosen result. Never apply a
scalar row a second time to an already replaced date. `without_holidays`
detaches **all** built-in date exceptions.

"An unstated halt instant remains a source gap even when the new representation
could encode a hypothetical value" — encode only what the operator states.

## What is now known about the gaps Stage 3 is for

`docs/schedules/coverage-2025.md` is the inventory (Stage 1) and has the exact
rows; #93 has the design detail. The declared phase-level gaps already ship as
`CoverageGapReason::NormalWeekPhaseWithheld` and
`SpecialSessionUnrepresentable` in `src/calendar/schedules/sourcing.rs`, with
closing conditions naming **#79** and **#93**. Stage 3 is what discharges the
`SpecialSessionUnrepresentable` ones. The inventory rows say which scopes carry
them (`globex_fx`, `globex_cryptocurrency`, and the CME venues whose Saturday
sessions and merged trade dates the scalar layer cannot state).

## Four things Stage 2 learned that Stage 3 will need

1. **`is_open` is the hot path and is already 3–5× slower than before Stage 2B**
   (measured; #125, filed, not a release blocker). Stage 3 adds a kind to the
   same path, so benchmark before and after and do not make it worse. If #125 is
   fixed first, rebase — the estimate is that resolving the instant's venue-local
   day once per query recovers it.
2. **A declared phase gap does not make a whole date unanswerable.** Stage 2B's
   gate reads only date-level facts (`CalendarCoverage::date_level_gap_on`) for
   session queries, and asks `require_phase_coverage` only for the order-entry
   scans. Read `QueryContext::require_answerable` and its two siblings in
   `src/calendar/query/schedule.rs` before touching coverage behaviour.
3. **The gate's floor check and the phase check have a fixed order**: floor
   first. Changing that order silently invalidated twelve baselined tests in
   Stage 2B. If you change gate ordering, expect a re-baseline across the suite.
4. **Detached `MarketHours` snapshots claim no coverage.** Every gate early-returns
   for them, and the tests rely on that: a snapshot keeps the schedule *and* the
   `Halt`/`Maintenance` classification its own rules derive, including below the
   floor. Do not add a built-in exception that a detached snapshot would observe.

## Open questions left by Stage 2, both files as issues

- **#127** — an empty `SessionExceptions` provider changes an answer on a withheld
  date (bare answers; overlaid refuses `UnresolvedGap`). An empty provider must
  not change an answer, which makes the **bare** path the suspect. Stage 3 touches
  exactly this derivation, so it is worth settling first.
- **#128** — the gate reports `UnresolvedGap` where `coverage_on` reports
  `OutsideCoveredRange` for a date both withheld and inside a phase-gap span.
  Stage 3 may remove the case by representing the day.
- **#86** — partially closed. The dated-constant fence now reads all 15 shipped
  constants across `## Revision rows` and `## Dated selectors`, mutation-checked.
  A cutover written as a comparison inside a selector is still not collected;
  that belongs to Stage 5's retained-boundary audit.

## Acceptance, from the plan

Public `session_exceptions` and holiday/policy suites must cover pause/reopen,
regular-only closure, added Saturday sessions, multi-day and reassigned trade
dates, order-entry changes, DST and precedence. Validate block ordering, bounds,
scope and citations. **Every query family must observe the same replacement** —
Stage 2B put the gate in one place (`find_occurrence`), so a block that is visible
to `is_open` but not to `candle_end` is the failure mode to test for. Full gates
and the benchmark comparison pass.

## Process lessons from Stage 2 that cost whole rounds

- **Commit early and often.** Stage 2 spent 70 files uncommitted for most of its
  run, so `git checkout` on a corrupted file silently reverted it to its
  *pre-migration* state — twice.
- **Never bulk-edit with a regex over assertion macros.** Three scripted
  conversions produced malformed code; the per-file, per-shape,
  compiler-after-each-file loop worked first time on the modules where it was
  used. If you write a script anyway, expect it to fail and verify its output
  compiles before trusting it.
- **Re-derive every count and every "every" before prose claims it.** Stage 2's
  review found a fence claiming "every" while seeing 3 of 15 constants, and a PR
  body claiming 17 assertions where the file had 16. Both were `grep -c`.
- **A fence that cannot fail is not a fence.** Mutation-check each one by flipping
  a shipped value and confirming a test goes red.

## Housekeeping

- `AGENTS.md` is the charter; it names the laws and the verification commands.
  Run the whole chain before claiming anything is done.
- `docs/plans/2026-09-12-path-to-release.md` is the stage plan; §7 is this stage.
- The research store is `/Users/agedvagabond/Developer/exchange-hours-research`.
  `STAGE-2B-HANDOFF.md` there holds the full Stage 2 record (rounds 1–17) if you
  need the reasoning behind any of the above.
