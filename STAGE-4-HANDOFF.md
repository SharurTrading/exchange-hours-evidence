# Stage 4 handoff — complete served calendars (#116)

Written **2026-09-25** (UTC) at the end of the Stage 3 session. Read this, then
`docs/plans/2026-09-12-path-to-release.md` §8 (the authoritative task) and issue
**#116** (the tracker). This note is orientation and state, not a replacement for
either.

## Start here

`main` is **`4066bfd`** — Stage 3 squash-merged. It is **green**, verified on the
primary checkout at that exact commit: fmt, `clippy --all-targets -D warnings`
(0 findings), **998/998** tests, doctests, `doc -D warnings`, `cargo deny`, MSRV.

Work in a worktree, never the primary checkout:
`git worktree add -b stage-4-<scope> <path> main`

`git worktree list` shows exactly one worktree and `git branch` exactly one
branch right now. Keep it that way; Stage 3's branch was deleted after merge.

Issue state at handoff: **#93 open** (the engine half is done and merged; this
stage owns the rows), **#116 open** (this stage), #130/#125/#127/#128/#86/#79/#123
open, #77 closed.

## What Stage 3 changed for you

The headline: **`HolidayKind::ReplacementBlocks(&'static [ExceptionBlock])` now
exists.** A built-in holiday row can state a complete ordered block set, served
by the same resolver a caller's `SessionExceptions` record drives. The shapes
that #93 recorded as unstateable are stateable now:

- CME's Saturday sessions carrying the following Monday's trade date.
- Merged trade dates where only the label moves.
- Restated order-entry onsets (`16:00 preopen` instead of `16:45`).
- A trade date that pauses and reopens, or whose blocks begin several local days
  before it.

Three things you must carry as acceptance, because Stage 3 could not fence them
with zero shipped rows. They are recorded in a
[#116 comment](https://github.com/SharurTrading/exchange-hours-rs/issues/116#issuecomment-5826709572)
so they are obligations rather than trivia:

1. **The composition arm is unfenced.** Two reviewers independently confirmed:
   deleting `exception_on`'s `ReplacementBlocks` arm leaves the suite green. The
   first shipped block row must come with a test that fails when the arm is
   removed.
2. **`fences::assert_blocks` has never actually failed a build.** The first row
   exercises it; show a deliberately malformed row failing the build, or the
   fence is decorative.
3. **`without_holidays` detaching a block row** is untestable without a row.

## Settle #130 before the first block row

**#130** is open and pre-existing (byte-identical on `main` at `d5cf64f`): a
replacement block opening on an instant the **next** trade date's normal session
also opens on makes `session_bounds` and `trade_date` describe different
sessions. A row keyed to a trade date rather than to the evening it opens can
reach that shape. Plan §8 says do not encode a row you cannot state exactly, so
settle it or record an explicit acceptance first.

Also: **block order is non-decreasing, not strictly increasing.** Two blocks may
share `(open_day_offset, open_ssm)` when their kinds differ. Documented on
`DateException::ReplaceSessions`, at `exceptions::validation::first_block_violation`,
and in the `holidays!` doc. Do not assume a validator will catch a strict order.

## The task, condensed from §8

Complete every served instrument scope from the permanent 2025 floor (or its
later sourced launch) through the operator's sufficiently-specified,
unconditional publication horizon. **PR order:** one CME family per PR reusing
its captured 2025–2027 artifacts; then Coinbase 2025-onward; CFE; ICE Futures
U.S.; Eurex. A shared-operator PR may carry sibling keys on the same evidence if
it stays bounded.

Per PR: reconcile normal-week changes, baseline and required phases and every
holiday arrangement; encode only exact sourced scalar or replacement rows;
**resolve gaps rather than widening a window over them**; keep broad venue
intersections explicitly partial; write evidence, tests, ledger cells and
CHANGELOG together. `#98` covers remaining non-CME document-id tables, `#105`
exact product-scope handling — shared branding is not proof of matching hours.

Acceptance for §8: derive row expectations from cited bytes independently of the
module; cover every retained cutover, holiday kind, required phase, end-exclusive
boundary, wrap, weekend and trade-date consequence; mutation-check each changed
behaviour. A shorter historical window or an unresolved in-window gap **blocks**
completion — record the precise missing source rather than passing the gate.

## Where the authority lives

- `docs/schedules/coverage-2025.md` — the Stage 1 inventory: per-scope rows,
  windows, withheld dates, and a `Closing issues` cell naming what closes each
  gap. Its "the scalar layer cannot state" wording is now imprecise for the
  special-session rows (the block kind exists, the rows do not); it is fenced by
  `tests/schedule_documentation/coverage_inventory.rs`, so changing its wording
  means changing that fence deliberately.
- The research store `/Users/agedvagabond/Developer/exchange-hours-research` —
  `STATUS.md` (the full review record; the Stage 3 sections are at the end),
  the captured artifacts, and `STAGE-3-BENCH-*.txt` (four criterion runs: the
  main/branch pair and the two main-to-main control runs).
- `docs/evidence/<owner>.md` per owner, `docs/schedules/verification.md` for the
  ledger row, `docs/schedules/sources.md` for monitoring entry points.

## Process lessons that cost real time

- **Benchmark engine changes with a same-machine control.** Stage 3's first cut
  measured 1.06× median against `main`; a `main`→`main` control measured 0.99×
  with a 1.41× max on individual rows. Without the control, 1.06× reads as
  noise. With it, it was a real regression that a one-bit guard fixed (max
  outlier 1.26× → 1.13×).
- **Check your fixtures' dates against coverage, not just the acceptance list.**
  Two of plan §7's acceptance items had *only* pre-2015 fixtures, which since
  Stage 2B assert `BeforeSupportFloor` rather than behaviour. The acceptance
  table looked covered and was not. Sweep each fixture's dates.
- **Re-run a probe on `main` before calling something a defect.** Two candidate
  defects in Stage 3 turned out to be byte-identical on `main`; one was a
  fixture bug, the other a genuine pre-existing issue (#130).
- **Never `replace_all` an anchor across a whole file.** A `CalendarSource::Exchange(Exchange::Cme)`
  replacement hit six pre-existing tests outside the new section. Use line-addressed
  or uniquely-anchored edits, and check `git diff -U0 | grep '^@@'` afterwards.
- **GitHub closes issues on `closes #N` phrasing, including inside "partially
  closes #N".** That silently closed #86 this session. After any merge, check the
  tracker issues are still open.
- **Mutation-check every fence**, and expect the interesting result to be the
  fence that *doesn't* fail — that is how the unfenced composition arm was found.
- Prefer an exhaustive `match` over `_ =>` in engine code; a reviewer flagged a
  wildcard that contradicted a claim in the PR body, and the fix made a future
  variant a build error.

## Housekeeping

- `AGENTS.md` is the charter; run the whole verification chain before claiming
  anything is done. `docs/plans/2026-09-12-path-to-release.md` §2 is the execution
  contract (§6 lists what a stage handoff must record, including the review
  verdict and the research-store update).
- Every post an agent makes through the maintainer's account opens by naming the
  exact model and harness (LAW-AGENT-ATTRIBUTION); commit messages carry a
  `Model:` trailer. The crate's own files never carry it.
- Three untracked `docs/plans/*-prompt.md` files and one `git stash` entry in the
  primary checkout predate this work and are deliberately left alone.
- `origin/stage-2b-query-migration` still exists. Its content is fully in `main`
  (squash-merged, empty tree diff), so it is safe to delete — the maintainer
  declined that deletion twice, so it stays until they say otherwise.
