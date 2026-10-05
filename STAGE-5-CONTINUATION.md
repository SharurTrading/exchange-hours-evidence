# Stage 5 — continuation note

Written **2026-09-26** (UTC), superseding `STAGE-5-HANDOFF.md` for current state.
That note still describes the Stage-4 end state and is worth reading for the
authority map (its §5) and the process lessons (its §6); this one says where
things actually stand now.

## 1. Open work

**`main` is `e5399a8` and all four changes are ON it**, verified in the real tree:
fmt, clippy `-D warnings`, **nextest 1016/1016, 0 skipped**, doctests 3/3, rustdoc
`-D warnings`, `cargo deny check`, `cargo +1.95 check --all-targets`. The
whole-surface audit reports **161** mismatches, down from **207** at the session's
start.

#141, #143, #144 and #145 are all MERGED, the last three via a consolidation PR
(#146) because **GitHub merges a stacked PR into its *base branch*, not into
`main`** — all three reported MERGED while `main` still held only #141. Also:
**`main` is protected ("Changes must be made through a pull request")**, so a
direct fast-forward push is refused; land via PRs.

The tables below are kept as the historical record of how they were opened.

Both are **held, not merged**, for the reason in §4. `main` is still `21e5204`.

Issues filed this session: **#140** (the remaining trade-date classes, with the
derived per-date spec), **#142** (evidence rows cite interpretive notes `N1`,
`N15`, `N17` that are defined nowhere).

Research store, all written this session:

- **`STAGE-5-TRADE-DATE-AUDIT.md`** — the derivation. §3 the four outcome classes,
  §6 the complete 2025-2027 spec with the per-family value table, §7 the
  whole-surface audit and its retracted false positives, §8 the dangling notes,
  §9 the probe-verified merged geometry, §10 the 2026-07-06 unwitnessed instant.
  **Read this before writing any row in this family.**
- `STATUS.md` — the running record; the Stage 5 rounds are at the tail.

## 2. What landed

**PR #141** — the composite/Saturday trade dates. CME assigns **five** phases to
the 2026-06-22, 2026-07-06 and 2027-06-21 trade dates; the rows shipped by #134,
#136 and #137 stated three, omitting the Thursday-evening leg that ends at the
Friday holiday's early close. Four families gained two blocks and
`globex_equity_index` gained three (its envelope splits at the regular
boundaries). Its second commit witnesses the 2026-07-06 final close, which no
artifact had contained, and fixes a latent panic in `stated_times` — the fence
sliced a byte window raw and aborted on an em dash instead of reporting a
mismatch.

**PR #143** — `globex_fx`'s merged trade dates, **all seventeen of them,
2025-2027**. Three statics, because the `-2` queue is the weekday `16:45` when
the holiday is a Thursday and `16:00` when it is a Sunday, and the holiday's own
queue is `16:00` either way. The two day-after-Thanksgiving dates changed from a
bare `EarlyClose { 13:45 }` to replacements ending at that same instant.

Measured effect of both PRs: the whole-surface audit reports **207 → 190**
mismatches and **`globex_fx` at zero** — across 1037 tradeable instants in every
captured window, that family's `trade_date` now matches the operator's printed
`tradingDate` at every one.

## 3. What remains, in priority order

### 3.1 The recipe, as `globex_fx` proved it

For each remaining family the change is: extend the statics with a merged set
whose `-1` queue is that family's **holiday** Pre-Open, add the rows, then let the
fences drive the rest. Every value below was measured from the bytes this session
(§6 and §9 of the audit note), and `globex_fx` is the worked example to read.

| family | holiday (`-1`) Pre-Open | day-after-Thanksgiving close | notes |
|---|---|---|---|
| `globex_fx` | 16:00 | 13:45 | **done** |
| `globex_energy` | 13:30 | 13:45 | `comex` and `nymex` **import** `globex_energy::SATURDAY_SESSION_BLOCKS`, so their rows follow automatically and their evidence and tests must move too. **Blocked — see below** |
| `globex_interest_rates` | 12:00 **except 2027-07-05, which is 13:30** | 12:15 | carries a historical 17:30 CT open and four queue statics across eras — use the one in force. **Derived and ready; see §14 of the audit note** for the full per-date table |
| `globex_nikkei_225_dollar` | 12:00 | not yet read | second product set (`id=168,167,...`); its bytes are the fourteen `live/extra/*.json` **and** the eleven `probeB_*.json` under `cme-2025-2027-repair/json/`. **No venue cascade** — `cme` does not route it — so this is the cheapest family to do next |
| `globex_equity_index` | 12:00 | 12:15 | **needs its own derivation** — see item 2 below; do not copy |

The `-2` queue is `16:00` when that day is a Sunday and the family's ordinary
weekday `16:45` when it is a Thursday, for every family.

**Capture coverage is complete for all three, so no retrieval is needed.** Checked
2026-09-26 against every JSON window in the store that carries the second- and
headline-product sets: `globex_energy` (`CL`, `GC`), `globex_interest_rates`
(`ZN`) and `globex_equity_index` (`ES`) each have **every** merged trade date
witnessed — 6/6 in 2025, 5/5 in 2026, 6/6 in 2027. This matters because the
nikkei work nearly foundered on exactly this: its second-product-set captures
begin at 2025-11, and an earlier 2025 date would have been a **sourcing** gap
rather than an authoring one. Nothing like that blocks these three.

**Read §13 of the audit note before starting any of these.** Each ships a row on
the merged holiday date, and those rows are **right**: CME's own holiday
schedules state an early close at T1 (the crate has shipped `early_close(12:00)`
for MLK since 2021, cited to `2021-mlk-day-schedule-compact.xls`). The operator's
`12:00 preopen` is the queue that opens *at* that close.

So the merged `-2` leg must **end at the holiday's close**, not at 16:00:

```
order_entry(-2, 16:00, 17:00)   the published Sunday Pre-Open
extended(-2, 17:00, C)          Sunday evening -> the holiday's early close C
order_entry(-1, C, 17:00)       the holiday queue, which opens at C
extended(-1, 17:00, 16:00)      the holiday evening -> the next 16:00
```

with `C` read **per date from the shipped holiday row**, not from any per-family
table: rates is `12:00` on MLK/Presidents/Memorial/Labor but **`13:30` on the July
4 observed Monday 2027-07-05**, and the crate already ships exactly that. `globex_fx`
has no such close and its already-landed set ends at `16:00` — that difference is
real. `globex_nikkei_225_dollar` is **done** (PR #144) and is the worked example
for the rest, including the `12:15` day-after-Thanksgiving close and the regular
boundary split that `globex_equity_index` additionally needs.

The venue cascade is the same every time and is not optional: `cme` routes six
families, so every date only the changed family states becomes an `Unsourced`
row there, and its two counts move; `cbot` routes grains and interest rates only;
`comex`/`nymex` route energy. Expect to touch `coverage-2025.md`, the venue
module, the venue evidence file, and the constant in
`tests/venue_sessions/holidays_cme_venues.rs`.

### 3.2 The order of work

1. **The same merged shape in the other four families** — `globex_energy`,
   `globex_interest_rates` and `globex_nikkei_225_dollar` show 17, 17 and 12
   mismatches; `globex_fx` is done and is the worked example to copy. The spec is
   §6 of the audit note and the geometry is probe-verified for all four (§9).
   Expect the same cascade every time: `coverage-2025.md` counts, `cme`'s
   `Unsourced` rows, the cme evidence file, the venue fence's constant. That
   cascade is the design working, not friction — and `globex_equity_index` needs
   its own derivation (see item 2) rather than a copy.
2. **The `globex_equity_index` merged row** — **do not scale the other four.**
   §7.2 of the audit note records why: on a merged Monday holiday the operator
   prints no `08:30 open`/`15:15 closed`, so whether the row states a `regular`
   block for the holiday at all is open, and that changes the block count. It is
   also entangled with **#142**: those rows' basis is the reading that CME's
   `12:00 preopen` event is an early close, and the note that explains it does not
   exist. Settle #142 first.
3. **PR 3 — the stale declarations.** `src/calendar/schedules/sourcing.rs:185-198`
   and the *public* `CoverageGapReason` documentation at
   `src/calendar/coverage.rs:223-234` both still say the special-session row
   "still waits on Stage 4 (#116)", which landed in #136; and
   `coverage-2025.md`'s `globex_fx` cells and §6 contradict each other. The fence
   that should have caught it — `declared_phase_gaps()` at
   `tests/schedule_documentation/coverage_inventory.rs:384` and the `(8, 10)`
   tally — is a handwritten fixture, so it cannot see both go stale together.
   **This was the handoff's first item and is still open**; it is best done once
   the rows that close the gap have landed, so that the declaration is *deleted*
   rather than re-worded.
4. **The order-entry-only class** — 2025-01-02, 2025-12-26, 2026-01-02, where the
   queue opens at `16:00` instead of `16:45` and the trade date is **already
   correct**. A row written from the merge template would rewrite a right answer.
   Currently unobservable, because the `#79` declaration refuses order-entry
   queries across those dates.
5. **`globex_grains` (79) and `globex_livestock` (39)** — audit hits that are
   **not** this family's shape. Most are an artefact of the audit's own probe
   (§7.1): a pause immediately precedes the `13:30 closed`, so `None` is correct
   there. What survives is one claim about the 13:20-16:00 window. Neither scope
   deserves its `coverage-2025.md` reading of "complete to 2027-12-31" until that
   is analysed.

## 3.9 The "regression" was my misreading — nothing is blocked

**§18 of the audit note supersedes this section's original text.** The `DayPolicy`
"regression" I reported on #143 and #145 does not exist. `DayPolicy::early_close_ssm`
is keyed by **trade date** (`fn early_close_ssm(&self, trade_date: NaiveDate)`), so
a policy naming a merged holiday correctly clips nothing once the span belongs to
the following trade date. Re-measured with the probe reading a leg owned by the
merged trade date, all three families clip identically and correctly. My earlier
probe varied the policy's date while reading a leg owned by a different trade
date — a measurement error, corrected on both PRs.

**So: no policy-layer change, no CHANGELOG note, and the remaining families are
not blocked behind anything.** The original text is kept below only as the record
of what I got wrong.

## 3.9 (superseded) — a regression needs a decision

**Read `STAGE-5-TRADE-DATE-AUDIT.md` §17 before touching any family.** The merged
rows for `globex_fx` (#143) and `globex_interest_rates` (#145) changed behaviour
outside the trade-date fix: a caller-supplied `DayPolicy` whose early close names
a **merged holiday** no longer clips that day's session for those two families.
`globex_nikkei_225_dollar` (#144) is unaffected. All three block sets are
byte-identical in shape.

Measured, with the caller closing the holiday at `10:00` — a value no built-in row
contains — and the Sunday session's end read back:

| policy names | `globex_fx` | `globex_nikkei_225_dollar` | `globex_interest_rates` |
|---|---|---|---|
| 2026-01-18 (Sunday) | 16:00 — no effect | 12:00 — no effect | 12:00 — no effect |
| 2026-01-19 (holiday) | 16:00 — no effect | **10:00 — clipped** | 12:00 — no effect |
| 2026-01-20 (trade date) | 16:00 — no effect | 12:00 — no effect | 12:00 — no effect |

At `21e5204` (`main`) a holiday-keyed policy clipped **all three**, so this is a
regression, not a pre-existing quirk. The likely mechanism is that the overlay is
applied to the session the *normal week* associates with the date, and a
replacement row keyed to a different trade date supersedes that layer — with
nikkei escaping because its replacement blocks are `extended` where its
normal-week envelope is `regular`. **Hypothesis, not established.**

**Recommended fix, grounded in the charter rather than invented:** the charter says
*"the caller's `DayPolicy` then clips the **result**"*. If that is the intended
reading, the overlay must apply **last**, after replacement resolution, and the
fix is in the **policy layer**, not in any row. That also makes nikkei's behaviour
the correct one and the other two match it. **It is an engine change and deserves
a review like any other** — do not make it casually.

Two decisions are needed, and both are the maintainer's:

1. Is a `DayPolicy` a **date** instruction that must clip whatever session covers
   that date (the `main` behaviour, and the recommendation above), or a
   **trade-date** instruction that a merged row legitimately supersedes?
2. Given (1), do #143 and #145 need the policy fix before merging, or is the
   behaviour change acceptable and to be noted in the CHANGELOG?

Everything below is already done and waiting on those answers.

## 4. The review blocker, and what was tried

The objective requires a **reviewed** PR. Three mechanisms were attempted and all
three are unavailable here:

1. A full charter-review subagent ran three rounds, reached step 8 of 10 (its last
   words were "Now the mutation test. Snapshot first.") and produced no report.
2. A tightly-scoped review subagent created its worktree and never compiled
   anything.
3. `.coderabbit.yaml` configures a CodeRabbit cloud review that indexes
   `AGENTS.md` — but CodeRabbit has commented on none of PRs #134, #136, #137,
   #141, #143 or #144, so the app is not installed. Configuration without a
   reviewer.
4. **`kodus` is installed** (`/opt/homebrew/bin/kodus`, v0.4.19) and its
   `kodus review` flow would be a real independent review — but it is on a
   **lapsed trial**: `kodus status` reports `Auth: trial`, and both
   `kodus auth status` and `kodus review` fail with `Request failed with status
   404`. No team key is configured. Retired backend, not a missing install —
   do not spend a round on it without checking `kodus status` first.

**Four subagents were dispatched this session in total and all four stalled.**
Everything landed was authored directly. The one mitigation that worked: a brief
demanding an early checkpoint file (the PR 2 author wrote a usable one within
minutes), which turns a stall from a total loss into recoverable state. Add that
to the Stage-4 handoff's §7.4 author-brief template.

**What would unblock:** enabling a reviewer on the repository, or the maintainer
directing that CI plus author verification suffices. Holding is deliberate —
PR #141 changes prose in 15 evidence rows and 5 module doc comments, and Stage
4's record is that three of its four re-review rounds returned CHANGES REQUESTED
for prose while every check was green. Merging moves `main` irreversibly.

## 5. Lessons this session added

1. **A pattern-based search will lie to you — four times this session, always
   confidently and always with a clean exit.** A glob missing `live/thbp/*.md`
   hid the nikkei Sunday windows and produced a false "nikkei is missing two
   phases"; a glob missing `live/` produced a false "the 2027 windows are not in
   the store"; and `grep '"id":168'` produced a false "nikkei's count has no
   provenance", because those files write `"id": 168` with a space. **A search
   that returns nothing is not evidence of absence until the pattern is checked
   against the bytes.** Prefer an instrumented tool — the audit now prints the
   artifacts behind each scope, which turned the last of these into a one-run
   answer.
2. **Probe inside the session an event bounds.** A second after a `closed` event
   lands in the next session; a second before one lands in a pause if a pause
   precedes the close. Both produced false defect counts before being corrected.
3. **Derive the block set from its own family's window, every time.** In this one
   family, four separate "the sibling is the same" assumptions were false.
4. **A fence that panics reads as a defect in the change.** `stated_times`
   aborted on Unicode; had it not been fixed, the next author would have debugged
   the wrong thing.
5. **`stated_days` had the guard `stated_times` lacked.** When one function in a
   file handles a hazard, check its neighbours.
