<!-- SPDX-License-Identifier: MIT-0 -->

# ENGINE — Wave 0 result

**Written:** 2026-09-12 (UTC, `date -u`, LAW-UTC-DATES)
**Repository:** `exchange-hours-rs`, branch `holiday-tables` off `ledger-reshape`
**Commit:** `e9610cd` — *Holiday tables: the engine, with no rows* (not pushed)
**Implements:** `exchange-hours-research/holidays/DESIGN-holiday-tables.md`
§5.2 Wave 0 — "the engine, with no data"
**Gate chain:** all seven steps green (`fmt`, `clippy --all-targets -D warnings`,
`nextest --all-targets`, `test --doc`, `doc -D warnings`, `deny check`,
`+1.95 check --all-targets`). **620 tests pass**, up from 563; the golden file
`tests/golden/normal_week_grids.txt` is byte-identical.

---

## 1. What was built

### 1.1 The types and the macro — memo §1.2, D2, D3, D15

`src/calendar/schedules/holidays/` is a three-file module. Four types are
public and re-exported flat from the crate root:

| Type | Shape |
|---|---|
| `HolidayKind` | `#[non_exhaustive]`: `Closed`, `EarlyClose { close_ssm }`, `LateOpen { open_ssm }`, `LateOpenAndEarlyClose { open_ssm, close_ssm }`, `Unsourced` |
| `Holiday` | `kind() -> HolidayKind`, `tier() -> EvidenceTier`, `document_id() -> &'static str` |
| `HolidayCoverage` | `first()`, `last()`, `contains()` — mirroring `ExceptionCoverage` field for field |
| `EvidenceTier` | `T1` / `T2` / `T3` / `T4`, the four LAW-PRIMARY-SOURCES names |

Two are internal: `HolidayRow { trade_date, kind, tier, document: SourceRef }`
— reusing `timeline::SourceRef` as the memo asks — and
`HolidayTable { first, last, rows: &'static [HolidayRow] }`.

`holidays!` builds a `&'static HolidayTable` from

```rust
holidays! {
    coverage: (2025, 1, 1) ..= (2027, 12, 31),
    rows: [
        (2025, 1, 20, early_close(12 * 3_600), T2, "CME-SVC-2025-01-20"),
        (2025, 12, 25, HolidayKind::Closed, T2, "CME-HOL-2025-CHRISTMAS"),
    ],
}
```

and **eight** constant-evaluation assertions fail the build, each with its own
message. Every one was verified on 2026-09-12 by temporarily instantiating the
macro and violating the invariant:

| # | Invariant | Compile error |
|---|---|---|
| 1 | coverage window ordered | `holiday coverage window is inverted: its last trade date precedes its first` |
| 2 | strictly ascending trade dates | `holiday table is not strictly ascending by trade date; a row is out of order or shadowed by a duplicate` |
| 3 | every row inside the window | `holiday row falls outside its table's coverage window` |
| 4 | every row cited | `holiday row carries no document id` |
| 5 | tier T1 or T2 only | `holiday row is sourced below T2; LAW-PRIMARY-SOURCES admits only the operator's own statement or the operator's own machine channel` |
| 6 | close in `0..=86_400` | `holiday row's early close is outside 0..=86_400` |
| 7 | open in `0..86_400` | `holiday row's late open is outside 0..86_400` |
| 8 | a real calendar date | `invalid hard-coded holiday trade date` |

That instantiation was reverted; **nothing in the committed tree invokes
`holidays!`** (decision W0-6), so the crate ships no holiday-shaped data and no
invented document id.

### 1.2 Routing — memo D10, §2.1

`table_for(CalendarSource) -> Option<&'static HolidayTable>` is a `const fn`
over two matches with **no catch-all arm**: 96 `Exchange` arms and 36
`MarketHoursKey` arms, one per variant, every one `None` in this wave. Adding an
identity is a compile error until someone decides whether it has a table.

### 1.3 Application — memo D11, D12, D9, §2.2

`QueryContext` gains `holidays: Option<&'static HolidayTable>`, resolved once
per query in `::date_aware` and `::overlay`. `::fixed` gets `None` — a detached
`MarketHours` snapshot has no identity and the crate never guesses one.
`::baseline()` drops it alongside the caller's two layers, for the same reason:
it is a day-level modification of the normal week, and a baseline that kept it
would recurse.

Precedence is implemented as one scalar clip value:

```
caller SessionExceptionSource (explicit Closed / ReplaceSessions)
    ↓ suppresses
built-in family table
    ↓ tightened by
caller DayPolicy
```

A private `DayClip { closed, unavailable, early_close_ssm, late_open_ssm }`
carries each layer's contribution, and `DayClip::tighten` composes them: `OR` on
closures, `min` on early closes, `max` on late opens. A caller can always make a
trading day shorter; a caller can never widen the crate's answer. `KnownNormal`
deliberately suppresses nothing (§2.2's reasoning, quoted in the code).

`has_overlay()` now counts a built-in table (D9), so `identity::assign_normal`'s
following-business-day roll is live the day a cryptocurrency table lands — which
is what stops a closure from deleting a whole day of a 24/7 family's trading
rather than deleting its trade date. `trade_date_is_closed` consults the
built-in layer too, so the roll skips a date the table closes.

### 1.4 The coverage gate — memo D14, §2.3

Before any trading-day derivation, `resolve_rule_bounds` asks
`identity::trade_date_window(context, open_day)` for the inclusive set of trade
dates this occurrence could be assigned to, and then asks every attached layer
whether it holds a record in it. The windows are the memo's, each a safe
superset of what `assign_normal` can produce: `[D, D+1]` ordinarily,
`[D-1, D+1]` for SET Thailand, `[D, D+18]` for the two rolling families.

- built-in table: one `partition_point` over the sorted rows;
- caller `SessionExceptionSource`: its published `coverage()` window (a provider
  claiming *no* window is treated as possibly relevant — decision W0-9);
- caller `DayPolicy`: opaque, always `true`. `may_affect` is §7's follow-up 9
  and D13 caps this wave's public API at three items, so it is not added.

The gate sits **ahead of** the existing daily-close guard rather than after it
as §2.3 draws, because that guard resolves a profile to answer and all three
branches return the same unmodified bounds. The reorder is observably identical
and is worth 25 % of `is_open` (decision W0-14).

§2.3's reduction 1 — deriving `first_open` lazily, behind the late-open branch —
is applied unconditionally, since it was already used nowhere else and is
behaviour-identical (decision W0-13). Reduction 2 is not applied.

### 1.5 Public API — memo D13, §2.4

Exactly three items, mirrored on `PolicyCalendar`:

```rust
impl ExchangeCalendar {
    pub fn holiday_on(self, trade_date: NaiveDate) -> Option<Holiday>;
    pub fn holiday_coverage(self) -> Option<HolidayCoverage>;
    pub const fn without_holidays(self) -> Self;
}
```

On `PolicyCalendar` they are documented as reporting the **built-in row only**;
the caller's own layers stay introspectable through `session_exception_on`.
`without_holidays` detaches the table outright, so a detached calendar reports
no row and no window as well as not applying one — the exact A/B control the
benchmark needs (decision W0-12). Nothing else was added.

### 1.6 The evidence fence — memo §3.3, D16

Three tests in `tests/schedule_documentation/evidence_files.rs`:

- `every_holiday_row_appears_in_its_evidence_file` — every row's trade date
  **and** document id appears under `## Holidays` / `### <year>` in every
  evidence file the module declares;
- `every_holiday_table_states_its_coverage_window` — the window is written as
  `**Coverage:** <first> .. <last>`;
- `every_evidence_holiday_line_is_well_formed` — every line under `## Holidays`
  parses: an ISO trade date, a kind the crate can represent, a backticked
  document id, a T1 or T2 tier, and a non-empty `Derived from` recording the
  operator event dates the row was converted from.

All three pass trivially with zero rows. Each was verified to fire, on
2026-09-12, by temporarily attaching a two-row table to a real evidence file and
breaking one thing at a time — a missing row, a changed document id, a wrong
coverage window, a missing `### <year>` subsection, a T3 tier, an
unrepresentable kind, and a module block with no `// Evidence:` declaration.
Seven for seven; all temporary edits reverted.

The block parser skips matches on comment lines, so the worked example inside
`holidays!`'s own doc comment is not mistaken for a table.

### 1.7 Tests — memo §4.2

`tests/holiday_tables.rs`, 14 tests over the public surface only:

**No data ships.** `no_identity_ships_a_holiday_table` (all 132 identities),
`no_identity_reports_a_holiday_row` (all 132 identities × every 11th day from
2009-01-01 to 2029-01-01), `without_holidays_changes_no_answer_while_no_table_ships`
(dense grid across a holiday fortnight, six identities, five queries),
`without_holidays_is_idempotent_and_keeps_the_identity`,
`policy_calendar_mirrors_the_builtin_accessors`.

**The gate.** `the_coverage_gate_is_sound_for_every_trade_date_convention` —
one identity per gate-window class, each against an ungated reference over a
dense grid, with the provider's window both remote and covering.
`the_gate_window_reaches_the_neighbouring_trade_dates` — a one-day coverage
window on a Monday still reaches the Sunday-evening occurrence that carries it.

**The clip path, through a synthetic `StaticDayPolicy`.**
`an_early_close_clips_a_trading_day_that_opened_the_previous_evening` walks
§1.3's table row for row on the family it was written for;
`a_closed_trade_date_removes_the_previous_evenings_wrap` is §1.4;
`a_late_open_resolves_on_both_of_its_branches` is §1.5, both branches;
`a_late_open_and_an_early_close_compose_on_one_trade_date` is the shape that
justifies the deviation in §3.

**Layering.** `a_caller_replacement_resolves_the_day_before_a_clip_applies`,
`a_known_normal_record_suppresses_nothing_below_it`,
`an_out_of_range_boundary_is_unavailable_and_never_rolls_a_trade_date`.

The no-op regression is the existing suite: 563 tests unchanged and green, plus
the golden file byte-identical.

### 1.8 The benchmark — memo §6

`cargo deny check` already passes with `criterion` in the dev-dependency tree,
so §6.2's preferred harness is admissible; a std-only timing harness would in
any case be blocked by `clippy.toml`, which disallows `Instant::now` in every
target of this package. `benches/calendar_queries.rs` was extended from five
benchmark ids to 45 across four groups: the bare calendar over the four instant
classes, the layer matrix, the 5,000-point cold chart frame, and the remaining
query surface. Numbers in `BENCH-wave0.md`.

---

## 2. Files

| File | Lines | Code lines | State |
|---|---:|---:|---|
| `src/calendar/schedules/holidays/mod.rs` | 329 | 157 | new |
| `src/calendar/schedules/holidays/fences.rs` | 136 | 91 | new |
| `src/calendar/schedules/holidays/routing.rs` | 189 | 160 | new |
| `tests/holiday_tables.rs` | 633 | 439 | new |
| `src/calendar/query/schedule.rs` | 625 | 407 | +291 / −59 |
| `src/calendar/exchange_calendar/mod.rs` | 399 | 213 | +71 |
| `src/calendar/query/identity.rs` | 163 | 95 | +47 |
| `src/calendar/policy.rs` | 444 | 245 | +36 |
| `src/calendar/mod.rs` | 101 | — | +6 |
| `src/calendar/schedules/mod.rs` | 17 | — | +1 |
| `src/lib.rs` | 158 | — | +10 |
| `benches/calendar_queries.rs` | 347 | 275 | +331 |
| `tests/schedule_documentation/evidence_files.rs` | 1244 | — | +300 |
| `CHANGELOG.md` | — | — | +28 |

Every production file is under the 500-line-of-code reviewability guard; the
largest is `query/schedule.rs` at 407. Test files are exempt.

---

## 3. Deviations from the memo

### 3.1 No `open < close` fence on `LateOpenAndEarlyClose` — deliberate

The wave-0 task brief asked for `ssm < 86_400` and, for the combined variant,
`open < close`. The memo's own §1.2 fence 4 asks only for the `StaticDayPolicy`
ranges — `close_ssm <= 86_400`, `open_ssm < 86_400` — and that is what shipped.

An ordering fence would reject sourced data. A wrapped trading day's late open
is interpreted on the **preceding** local date whenever its wall clock is at or
after the day's normal first open (memo §1.5, `policy.rs:51-56`), so a real
combined row reads `open_ssm = 19:00` on the eve against `close_ssm = 12:00` on
the trade date — numerically `open > close`, semantically fine. The crate
already states this for the caller-facing twin:

> Their numeric order is deliberately not constrained: a wrapped trading day can
> open on the preceding local date at a numerically later wall clock than its
> final close on `trade_date`.
> — `DayOverride::late_open_and_early_close`

`a_late_open_and_an_early_close_compose_on_one_trade_date` encodes exactly that
shape against `globex_equity_index` and passes; the fence would have to reject
it. The reason is recorded on `fences::assert_instants` and in `DECISIONS.md`
W0-5. The other two range checks shipped as asked, in the memo's form.

### 3.2 The gate runs before the daily-close guard, not after — deliberate

§2.3 draws the gate after the existing checks. It ships ahead of
`has_daily_close_at`, which resolves a profile to answer. All three branches
return the same unmodified bounds, so the reorder is observably identical — the
suite passes either way — and it is the difference between +25 % and +0.5 % on
gated `is_open`. Recorded as `DECISIONS.md` W0-14, measured in `BENCH-wave0.md`
§3.

### 3.3 §2.3's reduction 1 applied now rather than "if measured" — deliberate

Deriving `first_open` lazily behind the late-open branch is free and
behaviour-identical, so it went in with the rest rather than waiting for a
measurement to justify it. Reduction 2 (hoisting the trade-date derivation out
of the per-rule loop) was **not** applied; §6's numbers say whether it is needed,
and they say it is the lever for the `DayPolicy` path, not for the table.

### 3.4 `DayPolicy::may_affect` not added — as the memo itself schedules it

§2.3 describes it as part of the gate, but §7 lists it as open follow-up 9 and
D13 caps this wave's public API at three items. Not added; the measured 15.8×
it would address is recorded as that follow-up's number.

### 3.5 The reverse evidence fence is not implemented

§3.3 asks for both directions: "every `trade_date` in a family's holiday module
appears in that family's evidence file, **and** every evidence row's date
appears in the module or is listed under that year's gaps." The forward
direction and a both-directions grammar check shipped. The reverse membership
fence needs the per-year gaps escape hatch, whose vocabulary arrives with the
first family's gaps. Open it as an issue with Wave 1 (`DECISIONS.md` W0-15).

### 3.6 Three wave-0-only lint suppressions

`fences.rs` carries a module-level `#![expect(dead_code)]` and the macro and its
re-export carry one `#[expect]` each, because nothing invokes `holidays!` yet.
`#[expect]` rather than `#[allow]` is the point: instantiating the macro turns
all three into `unfulfilled_lint_expectations`, which `-D warnings` rejects, so
Wave 1 physically cannot land a table without deleting them. Confirmed during
the W0-4 verification. `routing.rs` also carries two
`#[expect(clippy::match_same_arms)]`, because collapsing 132 identical arms into
an or-pattern would destroy the property the match exists for.

---

## 4. Performance — does D19's precondition hold?

Full detail in `BENCH-wave0.md`. Apple M2 Max, rustc 1.97.1, 2026-09-12.

| | |
|---|---|
| bare `is_open`, regular session | **240.7 ns** |
| the same with an out-of-coverage layer attached (gated) | **242.0 ns**, +0.5 % |
| the same with a layer that cannot publish a window | **3.80 µs**, 15.8× |
| `holiday_on` on an identity with no table | **310 ps** |
| cold 5,000-point chart frame, with and without the layer | 3.10 ms / 3.06 ms — 1.00× |
| daily trading-day derivation, no layer / gated | 12.4 µs / 15.2 µs, against a ≤ 30 µs target |

**Yes.** The gate removes the overlay's cost entirely for a layer that publishes
a coverage window: an attached-but-irrelevant layer costs 0.5 % more than no
layer at all. §6.3's two far-from-a-holiday `is_open` rows — the ones D19 makes
the merge conditional on — are met, the cold-frame ratio is 1.00, and the daily
derivation is comfortably inside its target. The two rows that are not met are
the `DayPolicy` row, which the target itself defers to follow-up 9, and the
on-a-holiday row (3.8 µs against ≤ 3 µs) which applies to ~13 days a year and
has §2.3's reduction 2 behind it.

Two caveats stated plainly, because no table exists to measure: everything gated
here runs through a `&dyn` provider's `coverage()`, which the built-in table's
direct `partition_point` does not, so 242 ns is an **upper bound** for the
built-in gate; and "on a holiday" is measured through a caller's `DayPolicy`
rather than a built-in row, which differs only in where the clip comes from.
Re-run the matrix as Wave 1's first act.

---

## 5. Wave 1's preconditions, from here

1. Delete the three wave-0 `#[expect]`s the first `holidays!` invocation makes
   unfulfilled; the build will demand it.
2. Write the owner module beside `routing.rs` and flip that identity's arm from
   `None`. Nothing else in the engine changes.
3. Write the `## Holidays` section in that owner's evidence file first — three
   fences will refuse the module otherwise.
4. Re-run `benches/calendar_queries.rs` with a real table and a
   `{far, adjacent, on}` date split, and record the result beside
   `BENCH-wave0.md`.
5. Open the two issues this wave names: the reverse evidence fence (§3.5) and
   `DayPolicy::may_affect` (§3.4, memo follow-up 9).
