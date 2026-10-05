# Stage 4 → Stage 5 handoff

Written **2026-09-26** (UTC) at the end of the Stage 4 session. Read this, then
`docs/plans/2026-09-12-path-to-release.md` **§9** (the authoritative Stage 5 task)
and issue **#117** (the tracker). This note is orientation and state, not a
replacement for either. `STAGE-4-HANDOFF.md` is the *entry* note written at the end
of Stage 3; this one records what Stage 4 actually did and what it left behind.

---

## 1. State of `main`

**`main` is `21e5204`.** Verified green by me on a detached worktree at that exact
commit: `cargo fmt --all --check` · `clippy --all-targets -- -D warnings` **0
findings** · **`nextest --all-targets` 1015/1015, 0 skipped** · `test --doc` 3/3 ·
`RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` · `cargo deny check` (advisories,
bans, licenses, sources all ok) · `cargo +1.95 check --all-targets`.

Tree and environment state, all verified rather than assumed:

- **One worktree** (the primary checkout, fast-forwarded to `21e5204`), **no
  `stage-*` branches** locally or on `origin`. All six Stage 4 branches were deleted
  after their content was confirmed present on `main`.
- The three untracked `docs/plans/*-prompt.md` files and the pre-existing
  `stash@{0}` (2026-09-18) are **deliberately left alone**.
- `origin/stage-2b-query-migration` still exists. Its content is fully in `main`
  (empty tree diff); the maintainer has declined its deletion twice, so it stays.
- **#135** (the draft integration branch) is **closed**, per its own instruction,
  with the outcome recorded in a closing comment.

### What landed

| PR | Scope | Squash | `main` tally |
|---|---|---|---|
| #131 | engine: settles #130 (a block meeting the next trade date's open takes its place) | `fe4c5d2` | 1002 |
| #133 | `globex_energy` — CME's three Saturday-session trade dates | `4afe54a` | 1006 |
| #134 | `globex_equity_index` — same three dates, ordered five-block split | `81d65b3` | 1008 |
| #136 | `globex_interest_rates` + `globex_fx` (shared-operator PR) | `3e259c3` | 1012 |
| #137 | `globex_nikkei_225_dollar` — same three dates | `21e5204` | **1015** |

The three trade dates are **2026-06-22, 2026-07-06 and 2027-06-21**, each a
Saturday session CME publishes as `05:00 open; 17:00 closed` carrying the following
Monday's trade date. **Five families** carry them as `ReplacementBlocks` rows (three
each: `globex_energy`, `globex_equity_index`, `globex_interest_rates`, `globex_fx`,
`globex_nikkei_225_dollar`); `comex` and `nymex` reproduce the family row because each
routes a single family; `cme` and `cbot` carry three `Unsourced` rows each because
their intersections disagree there. `globex_grains` and `globex_livestock` correctly
state no row.

---

## 2. The one thing Stage 5 should fix first, in its own PR

**A gap declaration and its documentation now contradict the shipped data, and the
fence that should have caught it is itself the stale artifact.**

`src/calendar/schedules/sourcing.rs:185-197` declares the special-session gap for
`globex_fx` and `globex_cryptocurrency`, and its doc comment reads:

> The vocabulary a row needs for them shipped in Stage 3 (#93) … so what this
> declaration still waits on is the operator row and its evidence, which is Stage 4
> (#116). **Until that row lands the gap is real** and this reason stays declared.

**That row landed in #136.** `globex_fx` now ships all three dates as
`ReplacementBlocks(&SATURDAY_SESSION_BLOCKS)` rows (`globex_fx.rs:539,542,569`), and
`CHANGELOG.md`'s #136 entry says so. So for `globex_fx` the special-session gap is
no longer "unrepresentable" — the representable remainder is the **merged trade
dates** (`docs/evidence/globex_fx.md:555-568` (the merged-trade-date bullet is at :558)), which is a modelling decision Stage
4 explicitly deferred. `globex_cryptocurrency`'s position is unchanged: it still
ships nothing for those dates.

Why it matters and why it survived: `tests/schedule_documentation/coverage_inventory.rs`
compares the crate's declarations against a **handwritten fixture**,
`declared_phase_gaps()` (line 384), which asserts
`("globex_fx", vec![quarter_hour, special_sessions])` and the `(8, 10)` tally at line
534. **The fence checks that the declaration list matches the fixture; it cannot notice
that both are stale together.** This is the charter's own warning in the reviewing
section — "a list that copies the module fences nothing" — realised in the negative
direction.

Suggested scope for that PR:

1. Correct the `unstateable_special_sessions` doc comment: the vocabulary shipped in
   Stage 3, the `globex_fx` rows shipped in Stage 4 (#136), the remaining
   representable gap for `globex_fx` is the **merged trade dates**, and
   `globex_cryptocurrency` still ships nothing.
2. Decide whether `CoverageGapReason::SpecialSessionUnrepresentable` is still the
   right reason for `globex_fx`, or whether the merged-trade-date remainder needs its
   own reason and issue. **The merged-trade-date question is a maintainer decision**,
   analysed in `STAGE-4-BLOCK-ROW-RECIPE.md` shape 3 and measured in STATUS round 16:
   the merge changes only which trade date owns Sunday-evening-through-Monday-16:00,
   with `is_open` agreeing at every instant.
3. Update `docs/schedules/coverage-2025.md`'s `globex_fx` row (line 73) —
   `Missing / disputed` and `Complete?` both still read "special-session dates the
   scalar layer cannot state (#93)" — plus the same file's **§6**, whose wording I
   rewrote in #136.
4. Only then touch `declared_phase_gaps()`, the `(8, 10)` tally and its message, and
   the fixtures at line 560 ("declares no phase-level gap") and 680-755
   (`closed_at_both`).

**A related, separately-judged advisory:** `coverage-2025.md` §6's
`globex_cryptocurrency` clause is overbroad — on the strict reading it is false for
all three dates, not just the two 2026 sessions, because that family's own evidence
calls the 2026 Saturdays "neither a row or a gap" and the 2027 session "recorded only
so a reader does not look for a row". A reviewer judged it advisory (it *overstates*
a served scope's incompleteness, cannot produce a wrong served value, and points at
the artifact stating the truth). It is a one-line change; if it rides the same PR,
re-run the chain.

---

## 3. What Stage 4 did and did not close

**Closed:** `globex_energy`, `globex_equity_index`, `globex_interest_rates`,
`globex_fx`, `globex_nikkei_225_dollar` — each now states CME's three
Saturday-session trade dates. Their derived venue tables (`cme`, `cbot`, `comex`,
`nymex`) were recomputed from them.

**Not closed, and deliberately so:**

| Item | State |
|---|---|
| **#79** — the Sunday 16:00-16:15 CT quarter-hour | **Still open and still the reason six scopes read incomplete.** Both CME notice channels were read in full across the bracket 2012-05-28..2012-06-07 and are silent: this is a **source gap, not an authoring gap**. Affects `cme`, `comex`, `nymex`, `globex_energy`, `globex_equity_index`, `globex_interest_rates` (and is one of two gaps on `globex_fx`). |
| **Merged trade dates** (`globex_fx`, `globex_cryptocurrency`) | **Stateable now, deliberately not written.** Measured as a pure trade-date relabelling with `is_open` agreeing at every instant. Needs an explicit maintainer acceptance. See `STAGE-4-BLOCK-ROW-RECIPE.md` shape 3. |
| **#139** — `globex_nikkei_225_dollar`'s published Pre-Open | **Filed this session.** The module comment claimed CME "publishes no normal-week pre-open or order-entry start time for NKD"; the store's own `live/normal/normalweek_extra.json` prints `16:45 preopen` Mon-Thu and `16:00 preopen` Sunday for `NKD` and `NIY` alike, and the evidence file cited that artifact nowhere. The comment was corrected and the contradiction recorded; **the reading is still open** and #139 now names its paired closing artifacts in a comment (the `sourcing.rs` arm, both `coverage-2025.md:77` cells, and the `coverage_inventory.rs` fixtures). |
| **#132** — order-entry queries on dates with a withheld phase | **Documented policy, not a defect.** `require_phase_coverage` refuses the order-entry API for any date a declared phase-level gap applies to; `is_open` still answers. Both halves are fenced by `tests/coverage_query_errors.rs::a_withheld_phase_refuses_the_order_entry_query_but_not_the_session_query`. The remaining question is for the maintainer: the refusal is by whole date, so a fully-sourced instant inside a Monday-Thursday `16:45-17:00` queue is refused along with the withheld quarter-hour. |
| **#138** — an order-entry replacement record assigns its trade date to a tradeable occurrence it does not displace | Open, unfixed, found during #136's review. |
| `globex_grains`, `globex_livestock` | `complete to 2027-12-31` with no `Unsourced` 2025+ dates. Their remaining gaps are historical (the 2012-2013 grains queue regime, the 2016-2020 livestock PCP) and lie **below the 2025 floor** — Stage 5 territory. |

**Stage 4 is not "all served scopes complete" and never claimed to be.** The floor
set by #79 means six scopes legitimately read `**incomplete**`. Do not try to close
#79 by widening a window over the quarter-hour.

---

## 4. Stage 5 — what §9 asks, condensed

**Entry:** reviewed Stage 1 baseline inventory and Stage 2 errors. **Inputs:** retained
profiles and seasonal selectors, revision and exact-instant fences, golden grids,
owner evidence, coverage records, and any overlapping Stage 4 corrections.

**Separate cleanup PRs:** CME owners, other served owners, then dormant owners; split
further by cohesive module if required.

**Retain**, for complete New Year answers: the state sourced at the 2025 floor, all
later changes, and enough context for sessions and gaps that cross the boundary.
**Remove:** obsolete earlier runtime profiles/revisions and historical identity
coverage expectations.

**Do not:** rename identities, rewrite wire names, freeze seasonal behaviour, reset a
real launch, or add a fictitious January-2025 exchange revision. Retain cited older
documents needed for the baseline and all raw research. Move touched narrative under
#85 and reconcile retained dated selectors under #86.

**Acceptance:** preserve independently captured in-range public results across
representative normal weeks and all retained cutovers/holiday rows and boundary
context; justify intentional corrections with separate sources; test unsupported
earlier identity requests. **Retain generic date-arithmetic and detached-snapshot
fixtures even when their dates precede 2025.** Update golden/history fences only for
genuinely removed coverage claims. Remove affected shipped claims before retiring
#89/#101/#112 as superseded; **do not implement #110's old encoding task.** Check
#79's surviving baseline consequences separately. Full gates and relevant benchmarks
per PR.

**Handoff:** owners pruned, retained baseline citations and boundary dependencies,
closed/surviving issue numbers, regression results, remaining owners.

---

## 5. Where the authority lives

- `AGENTS.md` — the charter and its named laws; the verification chain in the exact
  order CI runs it.
- `docs/plans/2026-09-12-path-to-release.md` — §2 the execution contract, §6 what a
  stage handoff must record, **§9 Stage 5**, §10-11 Stage 6-7.
- `docs/schedules/coverage-2025.md` — the per-scope inventory. Fenced by
  `tests/schedule_documentation/coverage_inventory.rs`.
- `docs/evidence/<owner>.md` — quotations, URLs, retrieval dates, conflicts,
  interpretive steps, residual risks.
- `docs/schedules/verification.md` — the ledger row per identity;
  `docs/schedules/sources.md` — monitoring entry points (the watch list).
- Research store `/Users/agedvagabond/Developer/exchange-hours-research/`:
  - `STATUS.md` — **the running record, now ~5,270 lines.** Read the tail for this
    session; the Stage 4 merge-queue sections and the rounds they cite are the
    audit trail for every claim above.
  - `STAGE-4-BLOCK-ROW-RECIPE.md` — block geometries, the rules a row author trips
    over, the probe procedure, and shape 3 (merged trade dates).
  - `STAGE-4-AUDIT-rows.py`, `STAGE-4-AUDIT-all-rows.py` — the row auditors.
  - `STAGE-4-BENCH-*.txt` — four criterion runs from #131.
  - The captured artifacts under `holidays/raw/`, including the Sunday windows and
    the Nikkei `THBP-B` set.

---

## 6. Process lessons from Stage 4 that cost real time

These are not general advice; each one cost a round trip or a wrong verdict here.

1. **A branch's green suite cannot see the tree it will land on.** Five separate
   defects in Stage 4 were prose or engine claims that were true of the branch and
   false of `main` after merging: the replacement-fence resolver, the "no built-in
   replacement-block row covers these dates" sentences in two files, a venue
   withheld-count, a family attribution, and a universal "every instant is quoted"
   claim. **Re-derive every count and sentence from the merged tables**, not from
   the branch.
2. **Measure the artifact you are holding; never carry a count between trees.** I
   asserted four wrong numbers across this session — `cbot` 256 (it is 253), "a
   one-sided resolution yields 1008" (it is 1010), a `venues.rs` claim from a grep
   that also matched `holidays_cme_venues.rs`, and a grep against a stale checkout
   that reported 0 in files shipping four. Every one was a claim about a **different
   tree** than the one in hand. Reviewers caught all four by measuring.
3. **`git checkout --` plus `touch` destroys uncommitted work in the same file.**
   A mutation harness using it silently erased a module's prose fix, and the harness
   still printed a clean-looking result. **A mutation harness must snapshot the whole
   file and restore from that snapshot**, and scratch scripts belong in `/tmp`, never
   the worktree.
4. **A hand-resolved merge can parse, look plausible, and have silently lost or
   fused content.** My first union splice dropped the newline before each `=======`
   marker, fusing a struct field into its doc comment and a match arm into the comment
   above it. **Verify a resolution by confirming each side's text is recoverable
   byte-for-byte**, not by whether it compiles. `cargo fmt --check` surfaced the last
   two fusions only incidentally.
5. **"The same fix applies to the sibling file" is wrong often enough to test.**
   Twice in Stage 4 a mirrored change was wrong in the mirror: narrowing a
   `matches!` arm that a 2025-2027 loop legitimately needs, and assuming a fence's
   tail hunk was a superset when each side added a different test.
6. **A verdict of MERGEABLE does not mean "no unresolved threads."** The ruleset's
   `required_review_thread_resolution` counts threads opened by the review that just
   approved, so `gh pr merge` can refuse a PR reading `MERGEABLE CLEAN`. **Re-check
   the thread count immediately before merging.**
7. **Squash merges make branch commits non-ancestors by construction.** Verify a
   branch is safe to delete by **content** (`git diff` against its squash, and the
   key fixes' presence on `main`), never by `merge-base --is-ancestor`, which
   reported all six merged branches "NOT contained".
8. **`cargo nextest list` is the cheap way to prove a fence is load-bearing.**
   Disabling one `#[test]` and diffing the tally distinguishes "the fence covers
   this" from "the fence exists".
9. **A shared `CARGO_TARGET_DIR` between a worktree and a `/tmp` scratch build makes
   cargo report another tree's binaries as fresh.** One run reported 1009 tests and a
   merged-only failure for a branch. Run `cargo clean -p exchange-hours` before
   believing a surprising tally.
10. **A gate summary hides its evidence.** Reading a PR's checks does not tell you
    whether a *prose* claim inside it is true. Three of Stage 4's four re-review
    rounds returned CHANGES REQUESTED for prose while every check was green.

---

## 7. Parallel agent instructions — how to run this faster

Stage 4 ran one worktree per PR with a reviewer per PR and was dominated by serial
round trips: a fix, a push, a re-review, another fix. The structure below is what I
would use from the start next time. It is written to be pasted into a delegating
session.

### 7.1 The division of labour

| Role | May do | Must not do |
|---|---|---|
| **Author** (one per PR) | edit, commit, push its own branch; run the chain in its own worktree | post to GitHub; touch another PR's files; merge |
| **Reviewer** (one per PR) | read; create a detached worktree at the head; post a review; append to `STATUS.md` | write production code; push; use any `eh-wt-*` worktree |
| **Fixer** (dispatched on a CHANGES REQUESTED verdict) | edit/commit/push the branch; re-run mutations | post to GitHub; review its own fix |
| **Merger** (the delegating session) | merge; verify `main`; reply to and resolve threads; clean up | author data; trust a remembered number |

**One writer per worktree, always.** A fixer and a reviewer must never share a tree —
the Stage 4 reviewer that refused to run cargo to avoid a target-lock fight with an
in-flight fixer was right.

### 7.2 Wave structure

Run **families in parallel, gates in series.** Concretely:

```
Wave 1 (parallel, independent):   author A (family 1)  author B (family 2)  author C (family 3)
                                  └─ all cut from the SAME main, same day
Wave 2 (parallel):                reviewer 1   reviewer 2   reviewer 3      ← one per PR, at its pushed head
Wave 3 (parallel):                fixer 1      fixer 2      fixer 3         ← only for CHANGES REQUESTED
Wave 4 (parallel):                re-reviewer 1  re-reviewer 2  re-reviewer 3
Wave 5 (serial, one at a time):   merge → verify main → merge → verify main → ...
```

**Waves 1-4 are embarrassingly parallel. Wave 5 is not** and must not be parallelised:
merging two PRs at once makes "which merge broke `main`" unanswerable.

### 7.3 Non-negotiable rules for parallel authors

1. **Cut every branch from the same `main` commit**, recorded in the handoff. Then a
   conflict is a known set, not a surprise.
2. **One operator/family per PR.** If two PRs must touch the same file, say so in the
   brief *before* work starts, and expect a union merge.
3. **Never let an author edit a shared counter, inventory row, or CHANGELOG entry it
   does not own.** In Stage 4, #133, #134 and #136 all moved the same venue counters
   and the same CHANGELOG region; every one of those became a conflict. Prefer one
   author owning the shared file, or accept the union merge knowingly.
4. **Dispatch a re-review only on an observed push.** Never gate on a fixer being
   "probably done". Record the head hash the verdict applies to; a later push
   invalidates it.
5. **Serialize per worktree**, parallelise across worktrees.

### 7.4 Brief templates

**Author brief — must include:**

- The PR's exact scope *and* an explicit list of what it must not touch.
- The branch name, the base commit, and "work only in `<worktree>`".
- The full verification chain **in charter order**, with the expected test tally.
- "Every count must be re-derived from the tables with your own parser; state the
  parser. Do not quote a count from this brief."
- Mutation requirements: which row to flip, and "restore from a saved snapshot, never
  `git checkout --`".
- Attribution: commit messages carry a `Model:` trailer; **do not post to GitHub**.
- "Report the head sha, the counts you measured, the mutations, and an explicit list
  of anything you could not verify."

**Reviewer brief — must include:**

- "Read `AGENTS.md`'s *Reviewing a change* and follow it."
- The PR number, the **head hash to confirm before starting**, and that the verdict
  applies to that hash only.
- "Create your own detached worktree at that hash. Do not use any `eh-wt-*` tree."
- **Name the three or four highest-risk claims** and require them re-derived, not read
  back: this is what makes reviews find real defects instead of restating the PR.
- The cross-tree risk in one line: "check this against the **merged** tree, not the
  branch" — with the merge command to use.
- For prose/files: "recompute every number in the ledger, README, CHANGELOG and PR
  body; check the PR body as data."
- Mutation: flip one shipped value, name the test that fails, restore and verify.
- Posting rule: inline for in-diff defects, a review-body comment for whole-PR or
  outside-diff; attribution line verbatim; append to `STATUS.md`.
- **"Report only what you executed and measured; state explicitly what you could not
  verify."**

**One deliberate anti-pattern to allow:** a reviewer whose findings are *all*
non-blocking should open **no inline threads** and put file:line in the body instead,
because thread resolution is a merge gate. A Stage 4 reviewer did exactly this and it
saved a round trip.

### 7.5 The delegating session's own checklist

Before merging anything:

- [ ] `gh pr view <n> --json headRefOid` matches the hash the MERGEABLE verdict names.
- [ ] `quality` **and** `msrv (1.95)` are both `SUCCESS`.
- [ ] **Unresolved thread count is 0** (query it; do not infer from `mergeStateStatus`).
- [ ] The branch contains current `main` (`git merge-base --is-ancestor origin/main HEAD`).
- [ ] After merging: **verify `main` in a detached worktree** — full chain, and the
      tally matches expectation.
- [ ] Then, and only then, start the next merge.

### 7.6 What to delegate vs do yourself

**Delegate:** authoring a family's rows; a full review; a bounded fix on a
CHANGES REQUESTED verdict; a conflict resolution with an exact expected-count spec.

**Do yourself, because round-tripping is slower than doing:** a two-token prose fix; a
count correction you have already verified; replying to and resolving threads; the
merge itself; and any check that is one command (`grep -c`, a tally, a `git diff`).
Three of Stage 4's four fix rounds were single-sentence body edits that took longer to
dispatch and re-review than to make and verify.

### 7.7 Budget notes

- A review agent's value is in **re-derivation**, so give it the exact expected values
  and ask it to confirm or refute them. An open-ended "check this PR" produced weaker
  reports than "these are my counts, my tally and my three riskiest claims — refute
  them".
- Expect **two review rounds minimum** per data PR: one substantive, one to confirm the
  fix. Budget for it rather than treating the second as failure.
- The parallel win is real but bounded by the **serial merge tail**. With four PRs,
  waves 1-4 ran concurrently and the merge tail was the critical path; adding a fifth
  author costs almost nothing, adding a fifth *merge* costs a full verification chain.

---

## 8. Housekeeping owed at the end of Stage 5

- `AGENTS.md` is the charter. Run the whole verification chain before claiming
  anything is done.
- Every post an agent makes through the maintainer's account opens by naming the exact
  model and harness (LAW-AGENT-ATTRIBUTION); commit messages carry a `Model:` trailer.
  **The crate's own files never carry attribution** — and note that a module comment
  carrying a paragraph of explanation will fail `modules_carry_no_narrative`. Narrative
  belongs in the evidence file; the module gets data plus a citation.
- Record new follow-ups as issues *before* merging, with the number cited where the
  follow-up is named (LAW-FOLLOW-UPS-ARE-ISSUES). Stage 4 filed **#139** this way and
  had to correct a PR body that named a follow-up without one.
- Append the review record to `STATUS.md` at every step. It is the only durable audit
  trail for claims that are not in the repository.
