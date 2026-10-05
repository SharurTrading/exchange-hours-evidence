<!-- SPDX-License-Identifier: MIT-0 -->

# DECISIONS — implementation choices the design memo left open

**Opened:** 2026-09-12 (UTC, `date -u`, LAW-UTC-DATES)
**Governs:** the implementation of
`exchange-hours-research/holidays/DESIGN-holiday-tables.md` in
`exchange-hours-rs`.
**Rule of the file:** the memo decides the design. Where it leaves an
implementation detail open, the simplest thing consistent with it is chosen and
recorded here, with the memo section it answers to. A decision here never
overrides a decision in §0 of the memo.

---

## Wave 0 — the engine, with zero rows

### W0-1 — Module layout: three files under `schedules/holidays/`

**Memo:** D10 (`src/calendar/schedules/holidays/<owner>.rs`, one module per
identity, resolved by a no-catch-all `table_for`).

**Choice.**

| File | Holds |
|---|---|
| `holidays/mod.rs` | the public value types (`EvidenceTier`, `HolidayKind`, `Holiday`, `HolidayCoverage`), the internal `HolidayRow` / `HolidayTable`, and the `holidays!` macro |
| `holidays/fences.rs` | the constant-evaluation fences and the terse kind constructors the macro rows use |
| `holidays/routing.rs` | `table_for`, as two no-catch-all matches — one over `Exchange`, one over `MarketHoursKey` |

**Why.** The fences are only reachable through the macro, so they carry the one
wave-0 lint suppression (W0-7) and keeping them in their own module scopes it to
exactly the items it is about. `routing.rs` is 132 one-line arms and would
otherwise drown the types. Wave 1's `holidays/<owner>.rs` modules sit beside
these three and are named by `routing.rs`'s arms.

### W0-2 — The public types live in the schedules tree and are re-exported flat

**Memo:** §2.4 lists `HolidayKind`, `Holiday` and `HolidayCoverage` as public.

**Choice.** They are defined in `schedules/holidays/mod.rs` and re-exported by
`src/calendar/mod.rs`, which `src/lib.rs` re-exports flat. `EvidenceTier` is
added as a fourth public type, because §2.4's `Holiday::tier()` has to return
something and LAW-PRIMARY-SOURCES names exactly four tiers.

`EvidenceTier` is **not** `#[non_exhaustive]`: the law fixes the set at four, so
a caller matching on it should be able to match exhaustively. `HolidayKind` is
`#[non_exhaustive]`, per §2.4 and because §7's follow-up 8 (block rows) adds a
variant.

### W0-3 — Macro grammar

**Memo:** D2 (`(trade_date, kind, tier, document_id)`, built by a `holidays!`
macro with const-eval fences, exactly like `revisions!`).

**Choice.**

```rust
// Evidence: docs/evidence/<owner>.md
pub(crate) static TABLE: &HolidayTable = holidays! {
    coverage: (2025, 1, 1) ..= (2027, 12, 31),
    rows: [
        (2025, 1, 20, early_close(12 * 3_600), T2, "CME-SVC-2025-01-20"),
        (2025, 12, 25, HolidayKind::Closed, T2, "CME-HOL-2025-CHRISTMAS"),
    ],
};
```

Six fields per row, document id last, mirroring `revisions!`'s
citation-literal-last shape so the evidence fence parses both with one tuple
scanner. `coverage:` and `rows:` are literal tokens, which lets the fence find
the window without matching braces. `fences::early_close`, `fences::late_open`
and `fences::late_open_and_early_close` exist so a row stays inside one source
line at ~200 rows per module; `Closed` and `Unsourced` are written as
variants, needing no constructor.

### W0-4 — Eight const-eval assertions, in one function

**Memo:** §1.2 lists five build-time checks.

**Choice.** `fences::assert_table` performs them all, so the macro makes one
call and only one item carries the wave-0 suppression. Verified on
2026-09-12 by temporarily instantiating the macro and breaking each invariant in
turn; each produced a distinct `error[E0080]` naming the violated rule:

| # | Invariant | Message |
|---|---|---|
| 1 | coverage window ordered | `holiday coverage window is inverted: …` |
| 2 | strictly ascending trade dates | `holiday table is not strictly ascending by trade date; …` |
| 3 | every row inside the window | `holiday row falls outside its table's coverage window` |
| 4 | every row cited | `holiday row carries no document id` |
| 5a | tier T1 or T2 only | `holiday row is sourced below T2; LAW-PRIMARY-SOURCES admits only …` |
| 5b | close in `0..=86_400` | `holiday row's early close is outside 0..=86_400` |
| 5c | open in `0..86_400` | `holiday row's late open is outside 0..86_400` |
| 6 | a real calendar date | `invalid hard-coded holiday trade date` |

### W0-5 — **Deviation.** No `open < close` fence on `LateOpenAndEarlyClose`

**Memo:** §1.2 fence 4 is `close_ssm <= 86_400`, `open_ssm < 86_400` — the
`StaticDayPolicy` ranges, and nothing about their order. The wave-0 task brief
additionally asked for `open < close` on the combined variant.

**Choice: the memo's fence, without the ordering constraint.** The ordering
constraint would reject sourced data. A wrapped trading day's late open is
interpreted on the **preceding local date** when its wall clock is at or after
the day's normal first open (§1.5, `policy.rs:51-56`), so a legitimate combined
row reads `open_ssm = 19:00` on the eve and `close_ssm = 12:00` on the trade
date — numerically `open > close`. The crate already says so in terms:

> Their numeric order is deliberately not constrained: a wrapped trading day can
> open on the preceding local date at a numerically later wall clock than its
> final close on `trade_date`.
> — `DayOverride::late_open_and_early_close`

`tests/holiday_tables.rs::a_late_open_and_an_early_close_compose_on_one_trade_date`
encodes exactly that shape against `globex_equity_index` and passes; a fence on
the order would have to reject it. The fence function's doc comment records the
reason where the next reader will look.

### W0-6 — No committed instantiation of `holidays!`

**Memo:** Wave 0 "merges with **zero rows**".

**Choice.** Nothing in the committed tree invokes `holidays!`. The obvious
alternative — a synthetic probe table to keep the macro type-checked — was
rejected: it would put holiday-shaped rows with invented document ids into a
repository whose charter exists to prevent exactly that, and the evidence fence
would then demand an evidence file for them. The macro is instead verified by
temporary instantiation (W0-4) at each wave boundary, and the fence records what
was checked.

### W0-7 — One lint suppression per wave-0-only item, each self-healing

`dead_code` fires on every fence item while nothing invokes the macro, and
`unused_macros` / `unused_imports` fire on the macro and its re-export.

**Choice.** `#[expect(..., reason = "…Wave 1…")]`, never `#[allow]`, and scoped
as narrowly as the lint allows: one module-level `#![expect(dead_code)]` in
`fences.rs` (whose every item is macro-only), and one `#[expect]` each on the
macro and its `pub(crate) use`. `#[expect]` was chosen over `#[allow]` precisely
because it *fails the build once it stops being true*: instantiating the macro
turns both into `unfulfilled_lint_expectations`, which `-D warnings` rejects, so
Wave 1 cannot land a table without deleting them. Confirmed on 2026-09-12: the
temporary instantiation of W0-4 produced exactly those two unfulfilled-expectation
warnings.

`routing.rs` carries two `#[expect(clippy::match_same_arms)]`, one per match.
The alternative clippy asks for — collapsing 132 identical arms into one
or-pattern — would destroy the property the match exists for: one arm per
identity is what a reviewer edits when that family's table lands, and a
collapsed arm silently absorbs the next new identity.

### W0-8 — The gate window is a function of the identity, in `identity.rs`

**Memo:** §2.3's table.

**Choice.** `identity::trade_date_window(context, open_day)` returns the
inclusive window, beside `assign_normal`, whose conventions it is a claim about
— so the two cannot drift into different files. The windows are the memo's, as
safe supersets of what `assign_normal` can actually produce:

| Class | Window | Why it is a superset |
|---|---|---|
| ordinary | `[D, D+1]` | a rule spans at most one local midnight, so the close date is `D` or `D+1` |
| `SetThailand` | `[D-1, D+1]` | the prior-opening-date branch reaches `D-1`; `D+1` is carried from the memo rather than narrowed |
| `GlobexRoughRice` | `[D, D+1]` | the following-local-date branch reaches `D+1` |
| `GlobexCryptocurrency`, `GlobexEventContractsBtc` | `[D, D+18]` | `3` days to Monday `+ 14` roll steps `+ 1` for the close-date wrap |

`None` (date-arithmetic overflow at the ends of the representable calendar)
falls through to the ungated path, which is correct, only slower.
`tests/holiday_tables.rs::the_coverage_gate_is_sound_for_every_trade_date_convention`
fences one identity per class against an ungated reference over a dense grid.

### W0-9 — An exception provider with **no** coverage window is not gated out

**Memo:** §2.3 gates the caller's `SessionExceptionSource` on `coverage()`.

**Choice.** `coverage() -> None` is treated as "may affect", not as "answers
nothing". The trait documents that every date outside the window must return
`OutOfCoverage`, but it cannot enforce it for a hand-rolled implementation, and
a missed exception is a wrong answer where a missed optimisation is only slow.
`StaticSessionExceptions` always returns `Some`, so the crate's own table is
gated.

### W0-10 — `DayPolicy::may_affect` is **not** added in this wave

**Memo:** §2.3 proposes it; §7 follow-up 9 lists it as an open issue; D13 caps
the wave's public API at three items.

**Choice.** Not added. A caller's `DayPolicy` answers "may affect" = `true`
unconditionally, so a policy-carrying query costs exactly what it costs today
and nothing regresses. §6.3's `≤ 2×` row for that case is explicitly written
"once `may_affect` ships", and `BENCH-wave0.md` records the measured 15.7× it
still costs — which is the number that should carry the follow-up.

### W0-11 — Layers compose through one scalar clip value

**Memo:** D12 (precedence and tightening).

**Choice.** A private `DayClip { closed, unavailable, early_close_ssm,
late_open_ssm }` with `DayClip::NONE` and `DayClip::tighten`. The built-in table
and the caller's `DayPolicy` each produce one, and `resolve_rule_bounds`
composes them before clipping, rather than each layer having its own branch. The
identity element is exercised in wave 0 (the built-in layer contributes
`NONE`, and every `DayPolicy` fence in `tests/holiday_tables.rs` runs through
`tighten`); the `min`/`max` arms become live with wave 1's first row.

`unavailable` is a fourth field rather than folding an out-of-range boundary
into `closed`, because the two are not the same thing: an invalid caller record
is not evidence that the operator was shut, so it must not feed the
following-business-day roll. `an_out_of_range_boundary_is_unavailable_and_never_rolls_a_trade_date`
is the fence.

### W0-12 — `without_holidays()` detaches the table, it does not merely stop applying it

**Memo:** §2.4 (a `const fn`, one `bool`, the exact A/B for the benchmark).

**Choice.** `ExchangeCalendar` gains a `holidays: bool` field, and a detached
calendar reports `holiday_on() == None` and `holiday_coverage() == None` as well
as answering the queries without the table. A calendar that reported rows it
declined to apply would be a third state nobody asked for. `PartialEq`/`Hash`
therefore distinguish a detached calendar from an attached one, which is right:
they answer differently.

### W0-13 — §2.3's reduction 1 (lazy `first_open`) is applied now

**Memo:** §2.3 lists it as a reduction "to be applied if §6's measurement says
the holiday-day cost still matters".

**Choice.** Applied unconditionally, because it is free and behaviour-identical:
`first_open` was already used only by the late-open branch, so deriving it
inside that branch removes one full daily-window derivation per rule from every
overlay-affected query that has no late open — which is ~99 % of them. Reduction
2 (hoisting the trade-date derivation out of the per-rule loop) is **not**
applied; it is a real refactor and `BENCH-wave0.md` says whether it is needed.

### W0-14 — The gate runs **before** the daily-close guard

**Memo:** §2.3 shows the gate after the existing checks.

**Choice.** The gate is the first thing `resolve_rule_bounds` does once it knows
an overlay is attached — ahead of `has_daily_close_at`, which resolves a profile
to answer. All three branches return the same unmodified bounds, so the reorder
is observably identical, and it is what takes the gated path from +25 % to
+0.5 % (`BENCH-wave0.md` §3).

### W0-15 — Evidence-file layout and the fence

**Memo:** §3.3.

**Choice.** The memo's layout, taken literally, with the fence reading it:

```markdown
## Holidays

**Coverage:** 2025-01-01 .. 2027-12-31 (inclusive trade dates). Tier: …

### 2025

| Trade date | Kind | Instant as printed | Document | Tier | Derived from |
|---|---|---|---|---|---|
| 2025-01-20 | early close | `12:00 preopen` — 12:00 CT (13:00 ET) | `CME-SVC-2025-01-20` | T2 | eventDate 2025-01-20, CME trade date 2025-01-21 |
```

- The `## Holidays` section may sit anywhere relative to the four sections
  `REQUIRED_SECTIONS` already orders; put it after `## Revision rows`.
- The **Kind** cell is one of `closed`, `early close`, `late open`,
  `late open and early close`, `unsourced` — the five the crate can represent,
  checked by the fence, so an unrepresentable day cannot be written as if it
  shipped.
- The **Tier** cell is `T1` or `T2`; the fence rejects anything lower, mirroring
  the const-eval fence on the row itself.
- Three tests in `tests/schedule_documentation/evidence_files.rs`:
  `every_holiday_row_appears_in_its_evidence_file` (forward: date **and**
  document id, under the right `### <year>`),
  `every_holiday_table_states_its_coverage_window`, and
  `every_evidence_holiday_line_is_well_formed` (grammar, in both directions).
  All three pass trivially while no module ships a `holidays!` block.
- **Not** implemented: the reverse multiset fence the revision rows have
  ("every evidence row's date appears in the module **or** under that year's
  gaps"). It needs the per-year gaps escape hatch §3.3 describes, and the gap
  vocabulary arrives with the first family's gaps. Open it as an issue with
  Wave 1.

---

## Wave 1 and later

### `globex_cryptocurrency`, 2025-01-01 .. 2027-12-31

### W1-CRYPTO-1 — Document ids are `CME-SVC-<holiday trade date>`

**Memo:** §3.2 (the id is the operator artifact's own stable name where it has
one, otherwise `<OWNER>-HOL-<YYYY>-<SLUG>`, with `CME-SVC-<date>` given as the
form for a service window).

**Choice.** Every `globex_cryptocurrency` row rests on one window of CME's
trading-hours service, so every id takes the service form, slugged with the
**CME holiday date the window answers** rather than with the window's own
endpoints: `CME-SVC-2025-11-27` is the Thanksgiving-2025 window, and it cites
both the 2025-11-27 and the 2025-11-28 rows. The research payload's local `D01`
.. `D67` namespace is not used — it collides across research files by
construction — and the mapping from it is recorded in the evidence file's
`### Documents` table together with URL, capture or retrieval time in UTC and
sha256.

### W1-CRYPTO-2 — A sourced closure that changes no answer keys no row

**Memo:** D3 ("rows are reserved for dates that change an answer"), §5.4 item 8
(Saturday 2025-11-29 "is a sourced `Closed`, not a gap and not a session").

**Choice.** Saturday 2025-11-29 is recorded in the evidence file as audited and
sourced, and keys **no** row: the five-day era's week has no Saturday trade
date, so a `Closed` row there would be indistinguishable from the absence it
already has. The date is inside the coverage window, so it reads as audited
normal, and the evidence file says which of the two kinds of "normal" that is.

### W1-CRYPTO-3 — A row may be keyed from a neighbouring day's printed trade date

**Memo:** D1 (key by the crate's trade date; the operator's printed trade date
is corroborating evidence for the conversion).

**Choice.** `Closed(2027-12-24)` is keyed from the **2027-12-23** record, whose
re-open prints `/TD 2027-12-27`. CME publishes no cryptocurrency record for
2027-12-24 at all — the 24/7 grid never stops, so there is nothing to print —
and the skipped trade date is stated only by the neighbouring day's events.
Without the row the crate would assign trade date 2027-12-24 to the block that
opens Thursday evening, which the operator's own data contradicts. The
derivation is recorded in the row's `Derived from` cell.

### W1-CRYPTO-4 — The late-open test case is discharged by asserting its absence

**Memo:** §4.1 case 4 (a late open, on both cutoff branches).

**Choice.** This family keys no `LateOpen` row in 2025–2027, and none is
invented to satisfy the case. The test instead walks the whole coverage window
and asserts that every shipped row is `Closed` or `EarlyClose`, with the reason
in its doc comment: what a cryptocurrency holiday removes is the trade date,
never the start of trading. The assertion fails the moment a later wave keys a
late open here, which is what re-imposes the two-branch cutoff test rather than
letting the case quietly disappear.

### W1-CRYPTO-5 — `pub(crate) static TABLE: &HolidayTable`, as W0-3 prints it

**Memo:** D2, D10; W0-3's worked invocation.

**Choice.** The module exposes `pub(crate) static TABLE: &HolidayTable`, and
`routing::table_for` — a `const fn` — resolves it as
`Some(super::globex_cryptocurrency::TABLE)`. Verified on 2026-09-12 that this
compiles: the static holds a `&'static` reference produced by the macro's own
`const` item, so the const context reads a reference, not a place. No `const`
item or non-`const` `table_for` was needed.

### W1-CRYPTO-6 — The five-day era's `Closed` rows ship with their loss declared

**Memo:** D9 and §1.7's third bullet (pre-24/7 crypto has `has_weekend_close:
true`, "so the same `Closed` rows behave as ordinary closures in the five-day
era"); §1.4 ("every `[N3]` row must be re-classified `Closed`").

**Choice.** The rows ship as the memo decides, and the consequence is declared
as an **executable-hours gap** per year rather than softened. On the nine
five-day-era Monday and Thursday holidays CME published no final close: matching
ran continuously from the previous 17:00 CT through the holiday, with every
event carrying the following business date. The holiday's own trade date
genuinely does not exist — which is what the row states — but because that era's
profile closes over the weekend, the following-business-date roll is
short-circuited and the row also deletes the connected block. `is_open` answers
false for roughly 23 hours per date that the operator published as open. The
alternative — withholding the rows — would instead assert a trade date the
operator denies, and would leave the 24/7 era's correct behaviour unreachable.
Closing condition: the memo's §7 follow-up 8 block rows, or a sourced statement
letting the five-day era roll its business date.


---

## Wave 1 — `globex_fx`, 2025-01-01 .. 2027-12-31

### W1-FX-1 — The `[N3]` Monday/Thursday holidays ship **no row**, as declared gaps

**Memo:** §1.1 (the worked event-date→trade-date normalisation, whose flagship
example is `EarlyClose(2025-01-20, 12:00 CT)` for equity index and interest
rates); §1.4 ("every `[N3]` row must be re-classified `Closed` during the
migration", naming FX 2025-01-20); §1.6's triage steps 3–6; D8.

**The conflict.** On the Monday and Thursday holidays CME publishes, for *every*
24-hour group, a record whose events all carry the **following** business date —
there is no `closed` event on the holiday and therefore no trade date of its
own. The groups differ only in the instant at which matching stops:

| Group | Published holiday events | Normal weekday | Memo's own row |
|---|---|---|---|
| Equity Index, Interest Rates | `12:00 preopen; 17:00 open` | `16:00 closed; 16:45 preopen; 17:00 open` | §1.1: `EarlyClose(12:00 CT)` |
| FX (and pre-24/7 Cryptocurrency) | `16:00 preopen; 17:00 open` | the same | §1.4: `Closed` |

§1.1 and §1.4 therefore prescribe different kinds for the same published fact.
Applied uniformly, §1.4's rule would turn §1.1's flagship example into
`Closed(2025-01-20)` for equity index too, which §1.1 explicitly rejects.

**Choice — §1.1 governs; the `[N3]` dates ship no row.** The coherent rule the
two sections share is: *key by the crate's own trade date and encode the
operator's printed final matching stop.* For equity index that instant is
12:00 CT and the row is an early close; for FX it is 16:00 CT, which **is** the
family's normal close, so the row would be a no-op and none ships. Every
executable phase on those dates is the normal week's: matching runs from the
previous 17:00 CT to 16:00 CT on the holiday and resumes at 17:00 CT.

**Why not `Closed`.** `globex_fx` has no business-date roll
(`identity::assign_normal`'s default close-date branch), so `Closed` does not
re-assign the connected block — it **deletes** it. `is_open` would answer false
for roughly 23 hours across each of the 16 affected dates, on a market the
operator published as open, which is the error class AGENTS.md ranks most
serious ("executable windows are the priority") and would make the crate worse
on those dates than shipping no table at all. D9's `Closed` rows are correct for
`globex_cryptocurrency` precisely because the roll rescues them there; that
rescue does not exist here.

**What is recorded instead.** Two declared gaps per date in
`docs/evidence/globex_fx.md`: the **trade-date merge** (the scalar vocabulary
cannot state that two of the crate's trade dates are one of the operator's) and
the **order-entry window** (the pre-open opens 16:00 CT instead of 16:45 CT —
the same class §1.4 itself rules "record it; do not model it"). Closing
condition for both: the memo's §7 follow-up 8 block rows.

**Sibling consistency.** `globex_equity_index` and `globex_interest_rates` ship
`EarlyClose(12:00)` on these dates, i.e. they follow §1.1 as well.
`globex_cryptocurrency` ships `Closed` under D9, and its own W1-CRYPTO-6 records
the same 23-hour loss for its five-day era. FX and pre-24/7 crypto share CME's
printed row, so the two keys answer differently on 2025-01-20, 2025-02-17,
2025-05-26, 2025-06-19, 2025-09-01 and 2025-11-27. **This is the one item in the
FX encoding that wants a maintainer ruling**, and it should be settled for both
keys at once.

### W1-FX-2 — A Friday early close keeps the crate's trade date, not the operator's

**Memo:** D1 (the operator's printed trade date is corroborating evidence for
the conversion, not the key).

**Choice.** On 2026-06-19, 2026-07-03 and 2027-06-18 CME prints `12:00 closed`
with its own trade date set to the following Monday. The row is keyed by the
crate's venue-local trade date — the Friday — so the clip lands on the correct
civil instant and shortens the leg that opened Thursday at 17:00 CT. The
differing trade-date label is recorded as a per-year gap, in the same class as
W1-FX-1's merge.

### W1-FX-3 — Saturday 2025-11-29 ships a `Closed` row that changes no answer

**Memo:** §1.2 ("rows are reserved for dates that change an answer"); D17 (a
venue table is the intersection of the families that route to it).

**Choice.** The row ships. The family's normal week has no Saturday session, so
it changes nothing at runtime, but `globex_livestock` ships the same date and
D17's venue intersection is computed date by date; a family that silently
omitted an audited closure would drop it from every venue table. The three
Saturdays CME *does* publish a session for (2026-06-20, 2026-07-04, 2027-06-19)
are gaps, not rows — `late_open_ssm` cannot create an occurrence the normal week
lacks (§1.5 / D7).

### W1-FX-4 — Document ids are `CME-SVC-<trade date>`, one per row

**Memo:** §3.2 (`<OWNER>-HOL-<YYYY>-<SLUG>`, or `CME-SVC-<window>` for a service
window).

**Choice.** One id per shipped trade date, matching `globex_livestock`'s
convention, so the module's citation and the evidence file's resolution table
line up one to one even where two rows are read from a single service response
(2025-12-24 and 2025-12-25 both come from the 2025-12-24..26 window). Each id
resolves in the evidence file to the URL, the capture or retrieval time in UTC,
the sha256 and the research file's own local code.

### W1-FX-5 — The late-open test case is discharged by asserting its absence

**Memo:** §4.1 case 4.

**Choice.** As W1-CRYPTO-4: this family keys no `LateOpen` in the window — CME
never reopens standard-grid FX later than its normal 17:00 CT — and none is
invented. The test asserts every shipped row's date, kind and tier against a
handwritten list, so a late open cannot appear without the test changing, and
additionally fences the post-closure reopen at 17:00 CT.

### W1-FX-6 — `pub(crate) static TABLE: &HolidayTable`

**Memo:** D2, D10; W0-3.

**Choice.** As W1-CRYPTO-5, for the same reason and with the same routing arm
shape. The task brief's `pub(crate) static TABLE: HolidayTable` would not match
`table_for`'s `Option<&'static HolidayTable>` in a `const fn`.

## Wave 1 — `globex_energy`, 2025-01-01 .. 2027-12-31

Encoded 2026-09-12 (UTC). 36 rows: 26 `EarlyClose`, 10 `Closed`, no `LateOpen`,
no `Unsourced`. Source: `holidays/cme-2025-2027.json` after the 2026-09-12
repair round, with `cme-2025-2027.verify.json` (round 2) governing; every row
was additionally re-read from the cited service bytes under
`holidays/raw/cme-2025-2027*/`.

### W1-ENERGY-1 — Energy and metals never disagree, so D17 is never reached

**Memo:** D17 (a venue table is the intersection of the families that route to
it; a date on which two halves disagree ships no row).

**Choice.** No date is withheld. CME's trading-hours service returns `CL` and
`GC` with identical event lists on every date in the window — the retrieval
records them under one combined product-group label, and the raw bytes were
re-parsed per date to confirm it. The D17 rule therefore does not bite for this
key, and the evidence file says so explicitly rather than leaving a reader to
assume it was checked.

### W1-ENERGY-2 — A `13:30 preopen` with no printed close **is** the final close

**Memo:** §1.1 (the Equity Index `12:00 preopen` row of 2025-01-20 becomes
`EarlyClose(2025-01-20, 12:00 CT)`); §1.6 triage rule 4.

**Choice.** On the fourteen `[N16]` dates — every MLK, Presidents', Memorial,
Labor, Juneteenth-on-a-weekday and Thanksgiving in the window, plus
2027-07-05 — CME publishes `13:30 preopen` and `17:00 open` and no `closed`
event. The row is `EarlyClose(td, 13:30 CT)`. The warrant is the operator's own
event-type legend, quoted in the evidence file: PREOPEN allows order entry with
"No order matching", OPEN is the "Start of continuous trading phase". Matching
therefore ends at 13:30 CT, which is what a final close is. The ordinary 17:00
CT open that follows starts the next trade date and keys no row.

### W1-ENERGY-3 — A Friday early close keeps the crate's trade date

**Memo:** D1; D9 (the crypto `Closed`-row treatment is justified by its
business-date roll).

**Choice.** Identical to W1-FX-2, and worth restating because the operator
records are the same bytes. On 2026-06-19, 2026-07-03 and 2027-06-18 CME prints
`12:00 closed` with its own trade date set to the following Monday, so on the
operator's clearing convention the Friday has no trade date at all. The row
stays on the Friday as `EarlyClose(12:00 CT)`. `Closed` would be actively wrong
here: this family has `has_weekend_close: true` and no following-business-day
roll, so a closure would delete the whole 17:00 CT Thursday to 12:00 CT Friday
span that CME publishes as open. The trade-date divergence is a recorded
interpretive step per year.

### W1-ENERGY-4 — `[N6]` eve rows collapse into the neighbouring `Closed` row

**Memo:** §1.6 triage rule 3.

**Choice.** The seven dates CME prints as `16:00 closed` with no evening
re-open — 2025-04-17, 2025-12-31, 2026-04-02, 2026-12-31, 2027-03-25,
2027-12-23 and 2024-12-31 — ship **no row**. `16:00 CT` is the family's normal
final close, so the eve's own trade date is normal; the only thing missing is
the evening leg, and the `Closed` row on the following trade date already
deletes it. 2027-12-23 is the clearest case: CME's holiday date for Christmas
2027 is that Thursday, and the crate's only row is `Closed(2027-12-24)`.

### W1-ENERGY-5 — Saturday 2025-11-29 ships a `Closed` row that changes no answer

**Memo:** §1.2; §5.4 item 8; D17.

**Choice.** As W1-FX-3, for the same two reasons: the venue intersection is
computed date by date, and CME's own 2025 Globex table states the Thanksgiving
period as "27 - 29 November 2025", so an audited Saturday is a positive answer
worth carrying. The three Saturdays CME *does* publish a session for
(2026-06-20, 2026-07-04, 2027-06-19) are declared gaps, not rows.

### W1-ENERGY-6 — The 2025-11-28 `07:00 preopen; 07:30 open` pair is a gap

**Memo:** §1.3 (the same pair on Equity Index); §1.6 triage rule 6.

**Choice.** The finalised Thanksgiving publication (capture
2026-01-29T01:23:09Z) prints `07:00 preopen; 07:30 open; 13:45 closed` for both
halves of the key, on a trading day that opened 17:00 CT the previous evening.
That implies a halt CME does not print. The `EarlyClose(13:45 CT)` row ships —
it is the sourced final close and is unchanged between the superseded and
finalised publications — and the morning pair is a declared gap. It is **not** a
`LateOpen`: 07:30 CT is below the family's normal first open of 17:00 CT, so the
cutoff would land on the trade date itself and delete fourteen hours CME
publishes as open.

### W1-ENERGY-7 — Document ids are `CME-SVC-<trade date>`, one per row

**Memo:** §3.2.

**Choice.** As W1-FX-4 and W1-CRYPTO-1. Two ids may resolve to one service
response (2025-11-27 and 2025-11-28 both come from the 2025-11-26..28 window);
the evidence file's document table carries the window, the capture or retrieval
time in UTC, the sha256 and the research file's own local code for each.

### W1-ENERGY-8 — The late-open test case is discharged by asserting its absence

**Memo:** §4.1 case 4.

**Choice.** As W1-CRYPTO-4 and W1-FX-5. CME moves the pre-open on a holiday but
never the 17:00 CT open itself, so this family keys no `LateOpen` in the window
and none is invented. The test walks every date of the coverage window through
`holiday_on` and asserts every shipped kind is `Closed` or `EarlyClose`, so a
row of the wrong kind cannot ship unseen.

### W1-ENERGY-9 — **Deviation.** `pub(crate) static TABLE: &HolidayTable`

**Brief:** "expose `pub(crate) static TABLE: HolidayTable`".

**Choice.** `&HolidayTable`, matching W1-CRYPTO-5, W1-FX-6 and the
`globex_livestock` arm already in `routing.rs`. Unlike the note in W1-FX-6, the
brief's shape does compile — `static TABLE: HolidayTable` with
`Some(&super::globex_energy::TABLE)` in the `const fn` was built and tested
before this change — so the reason is uniformity across the eight Wave 1
modules and the routing arm shape the assembler is already writing, not a
language constraint. Recorded because it is a deliberate departure from the
brief.

## Wave 1 — `globex_livestock`, 2025-01-01 .. 2027-12-31

Encoded 2026-09-12 (UTC) from `holidays/cme-2025-2027.json` as repaired that
day, against its latest verdict `holidays/cme-2025-2027.verify.json` (round 2).
36 rows: 31 `Closed`, 5 `EarlyClose`. Nothing in the verdict disputes a
Livestock instant or status, so no result-versus-verdict conflict had to be
resolved for this family; the one material finding that touches it (discrepancy
3, Saturday 2025-11-29) is already carried in the repaired result and is
encoded as a row.

### W1-LIVESTOCK-1 — Document ids are `CME-SVC-<trade date>`, one per row

**Memo:** §3.2 — the id is the artifact's own stable name where it has one, and
otherwise `<OWNER>-HOL-<YYYY>-<SLUG>`, with `CME-SVC-2026-06-19` given as the
example "for a service window".

**Choice.** One id per row, spelled `CME-SVC-<the row's own trade date>`, which
is the memo's printed example taken literally. A service window answers two or
three trade dates, so several ids resolve to one artifact; the `### Documents`
table in the evidence file resolves every id to its window, capture or retrieval
time in UTC, research-store path and sha256, and the `Derived from` column
carries the research-store id (`D01` … `D65`) so a reader can go back to the
retrieval file. The rejected alternative was one id per artifact
(`CME-SVC-A-20251126-20251128`): it is unique too, but it is unreadable in a
table of 36 rows and it collides with nothing the memo asked for. The same
choice was reached independently for `globex_cryptocurrency`, `globex_fx` and
`globex_energy`, so Wave 1 is uniform on it.

### W1-LIVESTOCK-2 — Saturday 2025-11-29 ships a `Closed` row that changes no answer

**Memo:** D3 (rows are reserved for dates that change an answer); §5.4 item 8
(the Saturday is "a sourced `Closed`, not a gap and not a session").

**Choice.** Ship the row. The family has traded Monday-Friday since 2016-02-29,
so a Saturday closure changes nothing, but CME's live service was asked and
answered — a 2025-11-29 schedule for all ten `THBP-A` products, every one of
them empty — and the row is the record of that answer. The test asserts the
neutrality (`is_closed_trade_date` is true with the table attached and with it
detached) rather than leaving it as a claim. This matches W1-FX-3 and
W1-ENERGY-5 and deliberately differs from W1-CRYPTO-2, whose family trades the
weekend and for which a Saturday row would have to be defended rather than
merely noted.

### W1-LIVESTOCK-3 — The order-entry residue on a holiday is a declared gap, and it is fenced

**Memo:** §1.4 — an order-entry-only deviation is not representable and is
recorded as a gap.

**Choice.** Record it, and add a test that asserts the residue exists. On a
closed or shortened Livestock date CME publishes no `14:30 pcp` and no
`16:00 closed`, but the crate's 14:30-16:00 CT Post-Close window already
carries the **following** trade date, so neither a `Closed` nor an
`EarlyClose` row on the holiday can reach it: `is_accepting_orders` stays true
for 90 minutes on Christmas Day 2025 and on each early-close date. The memo
says not to model it; the addition here is that the test states the current
answer in both directions, so the gap is visible in the fence rather than only
in prose, and closing it later fails the test rather than passing silently.

### W1-LIVESTOCK-4 — Two of the seven required test cases are discharged as negatives

**Memo:** §4.1 — seven required cases per family, including a late open and a
wrap removed by a closure.

**Choice.** Both are written as tests, with the reason in the test's own doc
comment.

* **Late open.** CME publishes none for this family in 2025-2027.
  `the_table_ships_no_late_open_in_this_window` walks all 1,095 dates of the
  coverage window, asserts every row is `Closed` or `EarlyClose`, fixes the
  counts at 31 and 5, and then asserts that each early-close date still opens
  at 08:30 CT and not before. Asserting the absence is what makes the negative
  a fence instead of a gap in coverage.
* **Wrap removed.** The grid has no wrapping occurrence, so no closure can
  delete a prior-evening leg. The nearest real case — and the one the crate
  must get right — is the previous civil day's Post-Close queue, which already
  carries the closed trade date: `Closed(2027-12-24)` deletes the
  14:30-16:00 CT queue of the audited-normal Thursday 2027-12-23, and
  `next_session_open_after` then returns Monday 2027-12-27 rather than Friday.
  `a_closure_removes_the_previous_days_post_close_queue` is that test, with the
  detached calendar as its control.

### W1-LIVESTOCK-5 — 2027-12-23 is audited normal and ships no row

**Memo:** D3 (no `Normal` rows) and §1.6's triage.

**Choice.** No row. CME's holiday date for Christmas 2027 is Thursday
2027-12-23, but the Livestock line prints `08:00 preopen; 08:30 open;
13:05 closed; 14:30 pcp; 16:00 closed` for trade date 2027-12-23 — the family's
ordinary Thursday grid, instant for instant, against the reference week
2026-10-18 .. 2026-10-24. The date is recorded in the evidence file's 2027
interpretive steps as audited, and the closure it belongs to is the following
day. The family has no `modified` row anywhere in the window, so §1.6's triage
had nothing else to decide.

### W1-LIVESTOCK-6 — `pub(crate) static TABLE: &HolidayTable`, as W0-3 prints it

**Brief:** "expose `pub(crate) static TABLE: HolidayTable`".

**Choice.** The reference form, matching W0-3's printed invocation and the other
seven Wave 1 modules. `holidays!` expands to a `const TABLE: &HolidayTable`, so
the reference form is what the macro hands back; the routing arm is
`Some(super::globex_livestock::TABLE)`. Recorded because it is a deliberate
departure from the brief's wording, made for uniformity with the rest of the
wave.

### W1-IR-1 — The noon pre-open of a Monday or Thursday holiday is an early close, not a closure

**Memo:** §1.1 (the worked MLK example), §1.4 (`[N3]` / `[N17]` rows are
`Closed`).

**Choice.** `globex_interest_rates` splits CME's two holiday shapes by whether
the family matched at all on the date. Where CME prints `12:00 preopen` (note
`N15`, and `13:30 preopen` on 2027-07-05, note `N16`), matching ran from the
previous evening's 17:00 CT open until that instant, so the row is
`EarlyClose(trade date, instant)` — §1.1 decides this case by name. Where CME
prints only `16:00 preopen; 17:00 open` (note `N17`) or `no events published`
(note `N1`), no matching happened on the date at all and the row is `Closed`.
Making the `N15` dates `Closed` would delete a session that really traded; the
operator's own rolled trade date on those dates is recorded as an interpretive
step instead.

### W1-IR-2 — An `N6` eve ships no row

**Memo:** §1.6 triage rule 3.

**Choice.** 2024-12-31, 2025-04-17, 2025-12-31, 2026-12-31, 2027-03-25 and
2027-12-23 print the family's ordinary weekday `16:00 closed` and differ from
the normal week only by the missing evening leg. That leg's trade date is the
neighbouring closed date, which already deletes it, so the eve is audited
normal and carries no row.

### W1-IR-3 — A Friday whose printed close carries Monday's trade date is still an early close

**Memo:** D1; §1.4; the round-2 verdict's discrepancy 4 (the six Friday
Cryptocurrency rows).

**Choice.** On 2026-06-19, 2026-07-03 and 2027-06-18 CME prints `12:00 closed`
and gives it the following Monday's trade date. The crypto family answers this
with `Closed` because its business-date roll carries the trading forward; this
family has no roll, so a `Closed` row would delete a Thursday-evening-to-Friday
session that matched for nineteen hours. The row is therefore
`EarlyClose(Friday, 12:00 CT)` and the trade-date divergence — the crate says
Friday, CME says the following Monday — is a declared gap in the evidence file,
labelling only, with `is_open`, `session_bounds` and the daily candle unaffected.

### W1-IR-4 — Saturday 2025-11-29 ships a row

**Memo:** §1.2 ("rows are reserved for dates that change an answer"); D17 (a
venue table is the date-by-date intersection of the families that route to it).

**Choice.** The row ships, as `globex_fx`'s W1-FX-3 and `globex_livestock`'s
equivalent. It changes no answer — the family's normal week has no Saturday
session — but a family that silently omitted an audited closure would drop it
from every venue intersection that includes this one. The three Saturdays CME
*does* publish a session for (2026-06-20, 2026-07-04, 2027-06-19) are gaps, not
rows: `late_open_ssm` cannot create an occurrence the normal week lacks
(§1.5 / D7).

### W1-IR-5 — The late-open case is discharged by asserting its absence

**Memo:** §4.1 case 4.

**Choice.** As W1-CRYPTO-4 and W1-FX-5: no 2025-2027 holiday moves this
family's first open — every post-closure reopen is the ordinary 17:00 CT one —
so no `LateOpen` is invented. The test fences both post-closure reopens at
16:59:59 / 17:00:00 CT and asserts that every named row is `Closed` or
`EarlyClose`, so a late open cannot appear without the test changing.

### W1-IR-6 — Document ids are `CME-SVC-<trade date>`, and `TABLE` is a `&HolidayTable`

**Memo:** §3.2; D2, D10; W0-3.

**Choice.** Both as `globex_fx` (W1-FX-4, W1-FX-6), for cross-family
consistency: one id per shipped trade date resolving in the evidence file to the
service window, the capture or retrieval time in UTC and the research file's own
local code, and `pub(crate) static TABLE: &HolidayTable`, which is what
`table_for`'s `Option<&'static HolidayTable>` takes in a `const fn`.

### W1-NKD-1 — The eight 2025 windows ship from the Equity Index line, not as `Unsourced`

**Memo:** §5.4 item 4(a) and 4(c); D15.

**Choice.** CME's trading-hours service answers for past windows only back to
Thanksgiving 2025, so `NKD` and `NIY` return empty schedules for the eight
windows New Year 2025 through Labor Day 2025 and no archived capture of the
`THBP-B` id set exists for them. Those nine rows — 2025-01-01, 2025-01-20,
2025-02-17, 2025-04-18, 2025-05-26, 2025-06-19, 2025-07-03, 2025-07-04 and
2025-09-01 — are taken from the `ES` line of the same ten-product capture and
ship with that capture's `THBP-A` document id, which is what §5.4 item 4(a)
directs. They are **not** `Unsourced`: the source is T2 and names the date and
the instant; what it does not name is this family's line. The corroboration is
mechanical rather than assumed — on all 36 product-dates from Thanksgiving 2025
to 2028-01-01 where CME publishes both lines, `NKD` and `NIY` match `ES` event
for event and trade date for trade date, including the one discriminating case
(Good Friday 2026: `NKD`/`NIY` at 08:15 CT with `ES`, not the 10:15 CT of `ZN`,
`6E` and `BTC`). Recorded as a residual risk per year in the evidence file, with
2025-07-03 named because that is the single date where the Equity Index line
diverges from its neighbours and so where the inference carries most weight.

### W1-NKD-2 — `THBP-B` document ids carry a `-B-` infix

**Memo:** §3.2 ("ids are unique repository-wide").

**Choice.** `CME-SVC-<trade date>` as W1-FX-4 for rows taken from the
ten-product `THBP-A` capture, and `CME-SVC-B-<trade date>` for rows taken from
the `id=168,167,320,323,19,27` capture that carries the Nikkei line. Without the
infix, this family and `globex_equity_index` would use one id for two different
artifacts on the same date — different bytes, different product sets, different
retrieval times. The infix costs two characters and keeps §3.2's uniqueness
claim true. Both forms resolve in the evidence file's `### Documents` table to
the service window, the capture or retrieval time in UTC, the sha256 and the
research file's own local code.

### W1-NKD-3 — `[N15]` is `EarlyClose`, never `Closed`, even though CME drops the trade date

**Memo:** D1; §1.1; §1.4.

**Choice.** As W1-IR-3, and for the same reason, but this family reaches it
through the Monday and Thursday holidays as well as the Fridays. On the `[N15]`
dates CME publishes a `preopen` rather than a `closed` at noon and labels the
whole span with the following business day's trade date; read literally that
would make the date `Closed`, which would delete a session that matched for the
nineteen hours from the previous 17:00 CT. `EarlyClose(holiday, 12:00 CT)`
reproduces CME's `is_open` answer event for event; only the trade-date label
differs, and that divergence is a declared residual risk per year rather than a
row. Verified against the operator's own bytes for MLK 2026, where the Sunday
17:00 CT open carries `/TD 2026-01-20` and no `closed` event carries
`/TD 2026-01-19` at all.

### W1-NKD-4 — 2025-11-28's morning pre-open pair is a declared executable gap

**Memo:** §1.3, §1.6 triage rule 6.

**Choice.** The finalised Thanksgiving 2025 publication prints
`07:00 preopen; 07:30 open` before the 12:15 CT close, with no `closed` or
`paused` event between the previous 17:00 CT open and it. Read literally,
matching stopped at an unstated instant and resumed at 07:30 CT. That is
intraday topology, so it is a declared gap — labelled **executable**, because a
trade could have printed in the window it describes — and the early-close row is
unchanged. It is the only date in 2025-2027 where this family shows the shape;
Thanksgiving 2026 and 2027 print the 12:15 CT close alone.

## Wave 1 — `globex_equity_index`, trade dates 2025-01-01 .. 2027-12-31

Recorded 2026-09-12 (UTC). Source: `holidays/cme-2025-2027.json` after the
2026-09-12 repair round, governed by `holidays/cme-2025-2027.verify.json`
(round 2). 36 rows: 8 `Closed`, 28 `EarlyClose`, 0 `LateOpen`, 0 `Unsourced`.

### W1-EQUITY-1 — The Monday/Thursday `preopen` is the trade date's final close

**Memo:** D1 and §1.1's worked example, which names MLK 2025 for this family.

**Choice.** The nineteen `[N15]` rows — CME prints `12:00 preopen; 17:00 open`
and carries the whole span under the *following* business day's trade date —
ship as `EarlyClose(D, 12:00 CT)` on the holiday's own trade date. CME publishes
no `closed` event on those dates, so in its terms the holiday has no trade date;
the crate keys a trading day by its final close, so the previous evening's leg
through the holiday noon is trade date `D` and 12:00 CT is where it ends.
`Closed(D)` is wrong here: it would delete trading that happened. The
consequence is a trade-date divergence from the operator on those mornings, not
an hours divergence, and it is declared in the evidence file per year.

### W1-EQUITY-2 — The six Friday-holiday `12:00 closed` rows are treated identically

**Memo:** D1; verifier discrepancy 4, which forced the same reading for crypto.

**Choice.** On 2026-06-19, 2026-07-03 and 2027-06-18 CME's `12:00 closed` event
carries the *following Monday's* trade date. That is the same "the holiday has
no trade date of its own" fact as W1-EQUITY-1, arriving through a different
event type. `EarlyClose(Friday, 12:00 CT)` for the same reason: this family has
`has_weekend_close: true` and no business-date roll, so a `Closed` row would
delete the Thursday-evening-through-Friday-noon block rather than re-assign it.
D9's `Closed` rows are crypto-specific precisely because the roll exists there.

### W1-EQUITY-3 — The five `[N6]` eve rows ship nothing

**Memo:** D8 and §1.6's triage, step 3.

**Choice.** 2024-12-31, 2025-04-17, 2025-12-31, 2026-12-31, 2027-03-25 and
2027-12-23 each print `16:00 closed` and no evening re-open. Against the
reference week 2026-10-18 .. 2026-10-24 that is the family's normal grid minus
its evening leg, and the leg's trade date is the following date, which already
carries a `Closed` row. No row; recorded in the evidence file's per-year
interpretive steps.

### W1-EQUITY-4 — Saturday 2025-11-29 is audited, not shipped

**Memo:** D3 (no rows for dates that change no answer).

**Choice.** The live service publishes an empty schedule for all ten products on
Saturday 2025-11-29 — a sourced `closed`, and the verifier's discrepancy 3. The
family's normal week has no Saturday session, so a `Closed` row would change no
answer. Recorded in the evidence file as audited, with its own document id
`CME-SVC-2025-11-26-SAT`, rather than shipped.

### W1-EQUITY-5 — Document ids are `CME-SVC-<window start>`

**Memo:** §3.2 (`CME-SVC-2026-06-19` for a service window).

**Choice.** Each id names the first event date of the service window the row was
read from, so one capture that answers two trade dates — Thanksgiving and the
day after, Christmas Eve and Christmas Day — is cited once under one id. The
research corpus's own `D01`..`D67` codes are file-local and collide across
blocks, so they are not used; the evidence file's `### Documents` table resolves
every id to its URL, capture or retrieval time in UTC, tier and sha256.

### W1-EQUITY-6 — No parentheses in comments inside the macro body

**Memo:** §3.3's evidence fence, discovered by running it.

**Choice.** `every_holiday_row_appears_in_its_evidence_file` parses the rows
list with a paren scanner that does not skip comments, so a `(…)` inside a
citation comment is read as a malformed row tuple and fails the fence with a
confusing message. Citation comments therefore carry no `(`, `)`, `[`, `]` or
`"`. Worth a one-line note in the macro's own documentation if a later wave
hits it again.

### W1-EQUITY-7 — `pub(crate) static TABLE: &HolidayTable`, as W0-3 prints it

**Brief:** "expose `pub(crate) static TABLE: HolidayTable`".

**Choice.** The reference form, for uniformity with W0-3's worked invocation and
with the sibling Wave 1 modules; the routing arm is
`Some(super::globex_equity_index::TABLE)`. The by-value form
(`static TABLE: HolidayTable = *holidays! { … }`) was written first and does
compile — verified 2026-09-12 — but it would have made this the only module
needing `Some(&…)` in `table_for`. Recorded as a deliberate departure from the
brief's wording.

### W1-EQUITY-8 — No late open ships, and the absence is fenced

**Memo:** D7; §4.1 case 4.

**Choice.** Every reopen in this window is the family's ordinary 17:00 CT, so
the family has no `LateOpen` row and neither late-open branch can be exercised
on real data. `no_late_open_row_ships_in_the_2025_2027_window` walks every trade
date in coverage through the public `holiday_on` and asserts the only kinds
present are `Closed` and `EarlyClose`, and additionally asserts the three
sourced Saturday sessions are absent as rows. That converts §4.1's fourth case
into a recorded fact about this family rather than a silently skipped test.

### W1-GRAINS-1 — `pub(crate) static TABLE: &HolidayTable`, as W0-3 prints it

**Brief:** "expose `pub(crate) static TABLE: HolidayTable`".

**Choice.** The reference form, for the same reason W1-EQUITY-7 gives: it is
what W0-3's worked invocation prints, what the sibling Wave 1 modules use, and
what `table_for`'s arms already expect — `Some(super::globex_grains::TABLE)`.
A by-value module would have been the only one needing `Some(&…)`. Recorded as
a deliberate departure from the brief's wording.

### W1-GRAINS-2 — Document ids are `CME-SVC-<trade date>`, not `<holiday slug>`

**Memo:** §3.2, which prints `CME-SVC-2026-06-19` "for a service window".

**Choice.** One id per shipped trade date, matching the sibling Wave 1 modules.
A service window answers two or three trade dates, so several ids resolve to
one artifact; the evidence file's per-year **Artifacts** table does the
resolving and lists the ids each file backs. The research corpus's own
`D01`..`D67` codes are file-local, are nowhere resolved to a file inside
`cme-2025-2027/INDEX.md`, and collide across blocks, so they are not used as
repository ids — they are named only where an interpretive step needs to point
at a specific superseded or corroborating capture.

### W1-GRAINS-3 — A holiday eve with the day session and no evening leg ships no row

**Memo:** D6; §1.6 triage case 3.

**Choice.** Fourteen dates in the 2025-2027 window print
`07:45 paused; 08:00 preopen; 08:30 open; 13:20 paused; 13:30 closed; 14:30 pcp;
16:00 closed` — the ordinary CBOT grain day — and then no `16:45 preopen` /
`19:00 open` pair. That withheld pair is the evening leg whose derived trade
date is the neighbouring closed date, which `Closed` already deletes, so the eve
itself is audited normal and ships nothing. Listed in
`docs/evidence/globex_grains.md` under the section preamble's conversion 2 so a
reader can check the fourteen by name.

### W1-GRAINS-4 — The day after a closure is `LateOpen(08:30 CT)`, on the trade-date branch

**Memo:** D7; §1.5.

**Choice.** On 2025-01-02, 2025-12-26, 2026-01-02 and 2027-07-06 CME prints a
`06:00 preopen` where the normal week prints `07:45 paused; 08:00 preopen`: the
prior-evening leg did not run and matching still begins 08:30 CT. `08:30` is
numerically earlier than the trading day's normal 19:00 CT first open, so the
existing `late_open_ssm` disambiguation puts the cutoff on the trade date
itself, which drops the evening occurrence and leaves the day session at its
own open. The three days after Thanksgiving carry the same late open plus a
12:05 CT final close and are the family's only `LateOpenAndEarlyClose` rows.

### W1-GRAINS-5 — Saturday 2025-11-29 ships a `Closed` row; other empty weekend dates do not

**Memo:** §1.2 ("rows are reserved for dates that change an answer"); round-2
verdict discrepancy 3.

**Choice.** The row changes no answer — the normal week has no Saturday grain
session — but CME's own 2025 Globex table states the Thanksgiving period as
"27 - 29 November 2025" and the governing verdict required the Saturday be
answered rather than left a gap. The repair round answered it from the
operator's channel, so the row records that sourced closure. The other weekend
dates a window happens to span (2025-04-19, 2025-07-05, 2026-06-20, 2026-07-04,
2026-12-26, 2027-01-02, 2027-03-27, 2027-06-19, 2027-12-25) carry no operator
statement that a holiday period extends over them and ship nothing. Same choice
as the livestock module, which also ships only 2025-11-29.

### W1-GRAINS-6 — Sunday 2027-07-04 ships no row

**Memo:** D1.

**Choice.** CME prints no events for Sunday 2027-07-04, and none for the Monday
it is observed on. On this grid no occurrence is ever assigned to a Sunday trade
date, so a `Closed(2027-07-04)` row would delete nothing; the Sunday-evening leg
that would have opened trade date Monday is deleted by `Closed(2027-07-05)`.
The Sunday's empty schedule is the operator's corroboration of that row, and is
recorded in the evidence file's 2027 interpretive steps rather than as a row.

### W1-GRAINS-7 — The post-close queue that a closure eve loses is a declared gap

**Memo:** §1.4's order-entry residue; D3.

**Choice.** The crate assigns the 14:30-16:00 CT post-close queue to the *next*
trade date, while CME's service labels it with the eve's own. On an eve whose
following trade date is closed, the built-in `Closed` row therefore removes an
order-entry window CME does publish. No executable answer moves — `is_open`,
`session_bounds`, `trade_date` and `candle_end` are unchanged — but
`is_accepting_orders` and `is_order_entry_only` do. The scalar vocabulary has no
order-entry boundary, so this is recorded as a gap rather than modelled, and it
is named explicitly in the evidence file because it is the one deviation in
which a shipped row removes something the operator publishes rather than merely
failing to state something.

**Consequence for another test.**
`tests/futures_family_boundaries/cme_mini_grains.rs::mini_grains_and_the_standard_grain_grid_disagree_outside_the_converged_eras`
compares `globex_mini_grains` and `globex_grains` through
`calendar_for_market_hours_key(..).session_state` over the week of 2026-06-14,
which spans Juneteenth 2026. It fails at 2026-06-18 15:00 CT — grains answers
`Closed`, mini grains `OrderEntry` — as soon as grains has a table and mini
grains does not. The fix belongs to whoever closes that pair: either the mini
grain table lands with the same rows, or the comparison reads through
`without_holidays()`. Not repaired here; this module's scope is its own three
files.

### W1-GRAINS-8 — Only one late-open branch exists on this family's real data

**Memo:** §4.1 case 4, which asks for both branches.

**Choice.** Every late open this family ships is 08:30 CT, which is below the
trading day's 19:00 CT normal first open, so only the "cutoff on the trade date"
branch is reachable from shipped rows. The other branch — an ssm at or above the
normal first open, resolving to the preceding local date — stays covered by the
engine's own `StaticDayPolicy` fences in `tests/holiday_tables.rs`. Recorded so
a later reviewer does not read the single branch as an omission.

---

## Wave 8 — the 2026+ non-CME venue block (CFE, Eurex, ICE US, CDE, SMFE)

Source: `holidays/cfe-eurex-ice-cde-smfe-2026-2027.json`, round-2 verdict
`matches: true`, zero discrepancies, four record-hygiene advisories.

### W8-1 — One module per venue, one `holidays!` block per distinct table

**Memo:** D10 (`holidays/<owner>.rs`, one module per identity).

**Choice.** Four modules — `holidays/cfe.rs`, `holidays/eurex.rs`,
`holidays/ice_us.rs`, `holidays/coinbase_derivatives.rs` — holding nine blocks
between them. Where several identities are served by one operator statement the
block is shared and its `// Evidence:` line names every owner's file, exactly as
`schedules/futures/us/cfe.rs` already does for one `revisions!` block:

| Block | Identities | Rows |
|---|---|---|
| `cfe::TABLE` | `cfe`, `cfe_vix` | 12 |
| `eurex::TABLE` | `eurex` (venue), `eurex`, `eurex_fixed_income` | 7 |
| `ice_us::SUGAR_COFFEE_COCOA` | `ice_us_sugar`, `ice_us_coffee`, `ice_us_cocoa` | 21 |
| `ice_us::ORANGE_JUICE` | `ice_us_orange_juice` | 20 |
| `ice_us::COTTON` | `ice_us_cotton` | 21 |
| `ice_us::FANG` | `ice_us` | 22 |
| `ice_us::DOLLAR_INDEX` | `ice_us_dollar_index` | 21 |
| `ice_us::VENUE` | `iceus` | 24 |
| `coinbase_derivatives::TABLE` | `coinbase_derivatives` | 8 |

**Why.** D10's unit is the *table*, not the file: what it forbids is a wildcard
that hands an identity an answer nobody decided, and the no-catch-all
`table_for` still does one named arm per identity. Eight ICE identities in eight
files would have duplicated 21 identical rows three times in source for no extra
fence — the evidence files already carry that redundancy, because the fence
makes every declared file hold every row. `ice_us.rs` is 366 lines, 165 of them
code, well inside the reviewability guard.

### W8-2 — A CFE `RTH: None` row with a non-empty ETH cell is an **early close**

**Memo:** §1.1, which works the same conversion for CME and calls out CFE's
2026-01-01 row by name.

**Choice.** Cboe prints `Regular Trading Hours` and `Extended Trading Hours` per
civil date. On nine 2026 dates the regular cell is `None` and the extended cell
still names a block. On the crate's trade-date key that block *is* the holiday's
own trading day — it opened at 17:00 CT the previous evening — so the row is
`EarlyClose` at the stated instant, not `Closed`. Two dates differ: 2026-01-01,
where the only block printed is the Thursday-evening leg of trade date
2026-01-02 and nothing belongs to 2026-01-01 (`Closed`, which is the memo's own
worked example), and 2026-12-25, which prints `None,None`. 2026-04-03's close of
08:30 CT equals the regular open, so the regular occurrence collapses and
disappears rather than inverting, which `clamp_to_clip`'s `open < close` guard
already does.

### W8-3 — An ICE `open1` cell with no Exchange Notice ships `Unsourced`

**Memo:** §1.2 (`Unsourced` "says the third thing"), D4.

**Choice.** ICE's calendars mark a date on which a product group trades
non-regular hours `open1`, footnoted "Trading Hours for these contracts will be
announced in advance of the respective holiday via Exchange Notices". That is a
positive operator statement that the date is **not** normal, with no instant.
Silence inside a contiguous window would claim the date was audited normal;
`Unsourced` states what is true, clips nothing, and is visible through
`holiday_on`. It covers 2026 MLK and Presidents' Day (no notice exists — tested
against a Wayback CDX enumeration, not assumed), 2026 Thanksgiving and Boxing
Day (notices not yet issued), and every 2027 `open1` date.

### W8-4 — The `iceus` venue ships `Unsourced` on a disagreement date

**Memo:** D17 ("a date on which two families disagree ships no row and is a
declared gap") read together with D4 and §1.2.

**Choice.** The intersection is taken over the **seven `ice_us*` keys**, the
families the crate routes to the venue; four dates ship `Closed` because every
one of them is closed, and the other twenty ship `Unsourced` with the
disagreement printed in the evidence file. D17's "no row" is about a
*scheduling* row, and it is satisfied — the venue states no closure and no
instant it cannot support. But inside a contiguous coverage window silence is
the positive claim that the date was audited normal, which on Memorial Day 2026
is false, so the choice is between a false claim and the variant §1.2 created
for exactly this. Canola, Energy and Daily Gold and Silver are ICE product
groups with no crate identity and are outside the intersection; on all four
dates that do ship a row they are closed too, so including them would change
nothing. Both facts are recorded in `docs/evidence/iceus.md`.

### W8-5 — NYSE FANG+ takes the NYSE-index bullet's instant

**Memo:** §5.4 item 4(a), which does the same for `globex_nikkei_225_dollar`.

**Choice.** ICE's calendars key FANG+ on the group "Currency, Digital Asset,
Stock, SOFR, MSCI Bond, and Mortgage Index Contracts"; its notices split that
group into an index bullet and a currency bullet. Two 2026 notices name FANG+
explicitly and both put it with NYSE Stock Index at the same instant (Good
Friday 09:15, Labor Day 13:00). Memorial Day, Juneteenth and Independence Day
print the same bullet at 13:00 without spelling FANG+ out; those three rows take
13:00 on that reading, calibrated twice by the operator's own spelling. The
interpretive step is recorded per year in `docs/evidence/ice_us.md`. The
alternative — `Unsourced` — would discard an instant the operator states for the
bullet the family demonstrably sits on.

### W8-6 — Coverage ends where each operator's published future ends

| Identity | Coverage | Why |
|---|---|---|
| CFE | 2026-01-01 .. 2026-12-31 | Cboe has published no 2027 schedule |
| Eurex | 2026-01-01 .. 2026-12-31 | 2027-2036 are "preliminary and indicative", so LAW-NO-FABRICATED-DATES keeps them out |
| ICE (all eight) | 2026-01-01 .. 2028-01-03 | the last trade date the T1 2027 calendar names |
| CDE | 2026-01-01 .. 2026-09-07 | the last holiday Market Notice issued at retrieval |

Each window's upper edge is fenced on both sides by a test that names a real
holiday one step outside it and asserts the table does not reach it.

### W8-7 — SMFE gets no table, recorded as a service-tier fact

**Task brief and LAW-SERVICE-TIERS.**

**Choice.** `Exchange::Smfe` stays `None` in `table_for`. Small Exchange, now
Kraken Derivatives Exchange, publishes no 2026 or 2027 holiday calendar because
the DCM is dormant; the crate's own profile is `CLOSED` from 2025-03-24, so a
row could only shorten a day that already has no session. The basis for the
dormancy is **T3** — CFTC press release 9272-26 of 2026-07-24 — which never keys
a row, and none is keyed. The fact, its evidence and its closing condition are
in `docs/evidence/small_exchange.md` under **Gaps and residual risks**, which is
where LAW-SERVICE-TIERS puts a dormant identity's obligations.

### W8-8 — Cotton's 2026-07-06 late open is sourced but inert

**Memo:** §4.1 case 4.

**Choice.** The row ships because ICE states it. It changes no answer: the
crate's Cotton grid opens for trade date `D` at 21:00 NY on `D-1` and names no
Sunday, so there is no modelled trade date 2026-07-06 for the row to clip. That
is a limitation of the Cotton *profile*, already recorded in
`docs/evidence/ice_us_cotton.md`, not of the holiday table, and the test asserts
the answer that would break first if the row were mis-keyed — the Monday-evening
leg of trade date 2026-07-07 — rather than pretending to a clip.

### W8-9 — Only the trade-date branch of `late_open_ssm` is reachable here

**Memo:** §4.1 case 4, which asks for both branches.

**Choice.** Every late open in this block — 07:30 and 08:00 NY for the softs,
05:00 NY for the two index families — is below its family's normal first open on
the preceding local date, so `clamp_to_clip` resolves the cutoff on the trade
date itself. The preceding-local-date branch stays covered by the engine's own
`StaticDayPolicy` fences in `tests/holiday_tables.rs`. Recorded so a later
reviewer does not read the single branch as an omission.

### W8-10 — The wave-0 "no table ships" fences are replaced, not deleted

`tests/holiday_tables.rs` carried `no_identity_ships_a_holiday_table` and
`no_identity_reports_a_holiday_row`, which are false the moment any family
lands. They are replaced by
`an_identity_without_a_table_reports_no_row_anywhere` (the same claim, scoped to
the identities that still have none, with a non-empty assertion so the fence
cannot pass vacuously) and `every_shipped_table_answers_only_inside_its_own_window`
(the crate-wide half of the per-family coverage fences, plus the
`without_holidays` detachment check of W0-12). The three wave-0 `#[expect]`
suppressions W0-7 predicted would self-heal were removed in the same change.

---

## Assembly — wiring the wave, the ledger and the user-facing records

Written 2026-09-12 (UTC) while assembling the branch `holiday-tables` from the
family modules the encoders left. These decisions are about the *change set*,
not about any family's data.

### W1-ASM-1 — The ledger gains a twelfth column, `Holidays`, derived by a fence

**Memo:** §2.4 and the charter's consumer contract, which already says "the
crate's ledger tells the consumer which identities are served, which are
dormant, and each identity's horizon and holiday coverage".

**Choice.** A new column between `Horizon` and `Reviewed on`, holding
`first..last` or an em dash, and `LEDGER_CELLS` moves 11 → 12. The alternative
was a sentence in the Basis note, but LAW-EVIDENCE-FILES caps that note at three
sentences and every row that gained a table was already at three, so the note
could only have carried the window by deleting something a reader needs more.

**What makes it a record rather than a claim.** `shipped_holiday_window` in
`tests/schedule_documentation/mod.rs` resolves the row's wire name to its
identity, calls the crate's own `holiday_coverage()`, and asserts the cell
equals it. A table that lands, moves its window or is withdrawn fails the ledger
until the cell is corrected, and no cell can name a window the crate does not
answer over. The README's "22 of the 132 ledger rows" prose is then derived from
that column by a second fence, so the chain README → ledger → shipped table has
nothing hand-maintained in it.

### W1-ASM-2 — The four CME venue calendars ship no table, and say so

**Memo:** D17 and §5.2 Wave 7.

**Choice.** `Exchange::Cme`, `Cbot`, `Comex` and `Nymex` keep their `None` arms
even though every family that routes to them now has a table. A venue's table is
the **intersection** of those families; full closures agree but most early
closes do not, so an intersection built carelessly would either publish one
family's early close as the venue's or silently drop the dates where they
disagree. Each of the four evidence files gains a `holidays, no table` gap
bullet naming D17, Wave 7 and memo §7 follow-up 10 as the closing condition, and
saying what a consumer should do today: route through the product-family key.

### W1-ASM-3 — `globex_mini_grains` stays without a table, and the convergence test detaches the layer

**Memo:** §5.2, which scopes Wave 1 to the eight served keys; the mini-grains
ledger row is `dormant`, and LAW-SERVICE-TIERS makes a dormant identity's
holiday table best-effort.

**Choice.** No table. That makes `globex_mini_grains` and `globex_grains`
disagree inside the week `tests/futures_family_boundaries/cme_mini_grains.rs`
probes, because it contains Juneteenth 2026-06-19 — but they disagree on the
*holiday layer*, not on the grid, and the grid is what that test's name claims.
The state comparison therefore runs on `without_holidays()` on both sides, with
the reason in a comment. Rewriting the probe week to dodge the holiday was
rejected: it would have hidden the divergence instead of stating it.

### W1-ASM-4 — Three more wave-0 assertions are reframed rather than deleted

**Memo:** none; this is the same housekeeping W8-10 records for its two.

**Choice.** `without_holidays_changes_no_answer_while_no_table_ships` becomes
`without_holidays_is_the_identity_without_a_table_and_a_detachment_with_one`:
the identity-function claim survives for the identities that still have no
table, and for the ones that do the probe window (which straddles Christmas)
must show a divergence, so a `without_holidays` that quietly kept applying the
table would fail. `policy_calendar_mirrors_the_builtin_accessors` moves its
caller overrides off 2025-12-24/25 — both of which are now built-in rows — onto
2025-12-23/26, and additionally asserts that the crate's own Christmas row and
its coverage window *do* come through the wrapper. `an_out_of_range_boundary_is_unavailable_and_never_rolls_a_trade_date`
moves its crypto probe from Friday 2026-06-19, now a built-in `Closed` row, to
Friday 2026-08-21, which carries none, so the only layer under test is still the
caller's; it asserts `holiday_on` is `None` there rather than trusting the date.

### W1-ASM-5 — The benchmark gains the memo's date-class split, on regular minutes

**Memo:** §6.2 (`date class × {far, adjacent, on}`), which `BENCH-wave0.md` §7
explicitly deferred to this wave because no table existed to measure.

**Choice.** Two instant classes added to `benches/calendar_queries.rs`,
`adjacent` (2026-11-25 10:00 CT, the trade date before Thanksgiving) and
`holiday` (2026-11-27 10:00 CT, which the table clips to a 12:15 CT close).
Both are **regular-session** minutes, so the only variable against the existing
`regular` probe is the date class, and the numbers are comparable with §6.3's
167.7 ns regular baseline. A first run used 2026-04-03 10:00 CT for `holiday`,
which the 08:15 CT Good Friday row makes a *closed* instant; it measured 19.0 µs
and is reported in `BENCH-wave1.md` as the closed-instant observation it is,
not as the date-class number.

---

### W1-ASM-6 — The coverage gate's ordinary window is `[D - 1, D + 19]`, the span the derivation can actually reach

**Memo:** §2.3's gate-window table, which is corrected here rather than
implemented — its premise is false — and §6/D19, whose overlay targets must be
re-measured against the corrected window before the table merges.

**Choice.** §2.3 gives an ordinary identity's gate window as `[D, D + 1]` on the
premise that "a rule spans at most one local midnight, so the close-date default
can only land on `D` or `D + 1`". `resolve_rule_bounds` does not date an
occurrence by its own close: it dates it by the local date of the **trading
day's** final close, `candle_end_with(&baseline, raw_open, Daily, Both)`. An
occurrence whose `raw_open` falls after its own trading day's final close — CBOT's
14:30-16:00 CT order-entry window on a Friday, ICE's 13:30/14:00/14:30-18:00 ET
post-close queues — is therefore dated by the *next* trading day, which over a
weekend or a weekend-plus-holiday is `D + 3` or more. `[D, D + 1]` is not a
superset of that, so `any_layer_may_affect` was asked the wrong question and
returned `false` for records the derivation would have found. Six shipped
families answered `is_accepting_orders`, `session_state` and `trade_date` wrongly
on the affected Friday windows — `globex_grains`, `globex_livestock`,
`ice_us_sugar`, `ice_us_coffee`, `ice_us_cocoa`, `ice_us_orange_juice` — and the
same query flipped its answer when an unrelated, *empty* caller layer was
attached.

The sound bound is the derivation's own walk:
`next_daily_close_and_trade_date_after_with` starts at `local_day.pred_opt()`
and iterates `CLOSE_LOOKAHEAD_DAYS = 21` times, so every trade date it can
return lies in `[D - 1, D + 19]` before `assign_normal`'s identity conventions
are applied on top. `trade_date_window` now returns that, widened by each
convention's own offset: SET Thailand one further day back, the business-date
roll of CME cryptocurrency and `ECBTC` `ROLLING_WINDOW_DAYS` further forward.

**Consequences recorded rather than hidden.** The sound window opens the gate on
roughly every day within 19 of a row, so §6's ~97 % exit rate no longer holds and
**D19's performance precondition is not met on this branch**. The narrowing that
could restore it is named in the review and is *not* implemented here, because it
needs a proof rather than an assumption: gate on `[D, D + 1]` only when the
occurrence is dated by its own trading day, which is answerable from the
already-selected static profile with no candle walk — is there a `Regular` or
`Extended` rule active over this occurrence whose resolved close is at or after
`raw_open`? Landing that, and re-measuring §6's targets, is follow-up issue #97.
The same widening is why `the_coverage_gate_is_sound_for_every_shipped_row` costs
about seven minutes in a debug build: both paths now derive at nearly every
probe. That cost is the honest cost of the sound window and comes down with the
narrowing.

**Closed by #97 (2026-09-17 UTC).** The narrowing is landed and measured, and it
is proved rather than assumed. The premise it rests on is that the close walk —
which runs over `QueryContext::baseline` and so cannot see any day-level layer —
dates a self-dated occurrence by its own trading day: a `Regular` or `Extended`
rule active on the occurrence's opening day answers the self-dating question with
its *own* close, so the session path pays nothing for the narrowing, and an
order-entry rule (which never joins the session union the walk reads) is answered
by scanning that day's session rules. That argument needs one property of the
shipped data — no session occurrence is dated more than one local day past its own
open — and the property is fenced over the whole population rather than sampled:
`every_shipped_session_occurrence_is_dated_by_its_own_open_or_the_next_day` walks
every `Regular` and `Extended` occurrence of every close-dated identity from the
January-2010 floor through 2027, one second past each open so adjacent phase
boundaries are visited, against `without_holidays()` (a clip shortens a block and
never extends one). It fails on a mutated profile whose blocks chain past two
local midnights. The three sourced conventions — SET Thailand, CBOT Rough Rice,
cryptocurrency and `ECBTC` — keep the full `[D - 1, D + 19]` window, because their
assignment is not the close-date default and the rolling one is itself
layer-sensitive. §6's re-measured figures, including the `hot_path_year` group
that makes the exit rate a measured ratio, are §8 of `BENCH-wave1.md`; the
per-instant cost that remains is tracked in the follow-up issue that
re-measurement opened.

**Fenced.** `the_coverage_gate_is_sound_for_every_shipped_row`
(`tests/holiday_tables.rs`) is memo §4.2 run to spec — every identity that ships
a table, every shipped row ±3 days, gated path against an ungated empty-provider
reference, comparing `is_open`, `session_state`, `session_bounds`,
`next_session_after`, `trade_date` and `is_accepting_orders`. It fails on
`globex_grains` at 2025-01-17 20:47 UTC with the old `(0, 1)` arm restored. The
test it replaces is kept under the name of what it actually proved,
`attaching_an_irrelevant_exception_provider_changes_no_answer`, and
`a_friday_order_entry_window_answers_the_same_with_and_without_an_empty_layer` is
the named regression.

### W1-ASM-7 — CME service-window ids are `CME-SVC-<first eventDate>`, one id per artifact

**Memo:** §3.2 ("unique repository-wide") and §8.3's D15/D16 bullet, which makes
the id-plus-capture pair the mechanism that made `cme-2016-2018`'s 140-row
supersession discoverable.

**Choice.** `DECISIONS.md` declared two incompatible slug rules in one flat
namespace: `CME-SVC-<the row's own trade date>` (W1-CRYPTO-1, W1-FX-4,
W1-ENERGY-7, W1-LIVESTOCK-1, W1-IR-6, W1-GRAINS-2) and
`CME-SVC-<window start>` (W1-EQUITY-5). The trade-date rule is non-injective by
construction, because two families may read the same `eventDate` out of two
different service windows, and it collided three times:
`CME-SVC-2026-12-24` resolved to both the 2026-12-22..24 and the 2026-12-24..26
windows, and `CME-SVC-2025-11-27` / `CME-SVC-2025-11-28` to both the 3-day
`thbp_2025-11-26_2025-11-28` capture and the 4-day `probeA_2025-11-26_2025-11-29`
live retrieval. Conversely one artifact carried two ids in two files. No shipped
instant was wrong — each row is still re-verifiable inside its owner's file — but
a repository-wide audit by id was ambiguous in both directions.

W1-EQUITY-5's spelling is adopted repository-wide and supersedes the slug choice
of the six entries above: the id names the **artifact** by its window's first
`eventDate`, `CME-SVC-<first eventDate>` (`CME-SVC-B-…` for the six-product
THBP-B set), with an explicit suffix where two windows share that date — `-SAT`
for the weekend-extended probe, `-PRE` for a superseded pre-holiday publication,
both already in use in `globex_equity_index.md`. This is what W1-LIVESTOCK-1's
rejected `CME-SVC-A-20251126-20251128` was reaching for, at the readability
W1-LIVESTOCK-1 wanted. 111 distinct ids were renamed across eight evidence files,
eight holiday modules and three family test files.

**Normalized so the invariant could be fenced at all.** §3.2's resolution
requirement was met in six mutually incompatible table shapes, which is why no
fence could be written. Every CME evidence file now carries exactly one
`### Documents` section with the fixed header
`| Document | Window | Capture or retrieval, UTC | Tier | sha256 |`;
`globex_interest_rates.md` gains the sha256 column §3.2 requires and had never
carried; `globex_grains.md`'s three per-year artifact tables and
`globex_fx.md`'s bullet list collapse into one.

**Fenced.** Three new tests in `tests/schedule_documentation/evidence_files.rs`:
`every_document_id_resolves_to_one_artifact_repository_wide`,
`every_artifact_carries_one_document_id`, and
`every_cited_document_id_is_resolved_exactly_once`. The third is scoped to the
evidence files that carry a `### Documents` table — the CME service windows, the
only date-shaped ids a rename can collide. Extending the fixed shape to CFE,
Eurex, ICE Futures U.S. and Coinbase Derivatives, so that fence covers the whole
crate, is follow-up issue #98.

### W1-ASM-8 — One audited operator closure ships a row in every family that routes to the venue

**Memo:** §1.2 line 132 ("rows are reserved for dates that change an answer") and
**D17** (a venue table is the intersection of the families that route to it).

**Choice.** This entry replaces W1-CRYPTO-2, W1-FX-3, W1-ENERGY-5,
W1-LIVESTOCK-2, W1-IR-4, W1-EQUITY-4 and W1-GRAINS-5, and the unrecorded eighth
ruling in `globex_nikkei_225_dollar.md`. One operator fact — CME's published
closure of Saturday 2025-11-29, `status: "closed"`, `verbatim: "eventDate
2025-11-29: no events published [N1]"`, recorded twice (D65 for the ten THBP-A
products, D54 for the six THBP-B products), with CME's 2025 Globex table stating
the period as "27 - 29 November 2025" — was encoded two ways inside one wave.
Five served families shipped it as a `Closed` row and three withheld it, so
`holiday_on(2025-11-29)` gave two contradictory public answers across the same
complex, and the D17 venue intersection Wave 7 will derive from these tables
would have read a unanimous operator fact as a families-disagree gap for `Cme`,
`Cbot`, `Comex` and `Nymex`.

An audited closure now ships a row in **every** family that routes to the venue,
even when it changes no answer, so the intersection is computed from one uniform
input. Rows added: `globex_equity_index` (`CME-SVC-2025-11-26-SAT`),
`globex_cryptocurrency` (`CME-SVC-2025-11-26-SAT`) and
`globex_nikkei_225_dollar` (`CME-SVC-B-2025-11-26`, whose THBP-B window already
reaches the Saturday). §1.2 line 132 and D17 are the citation, not D3 — D3 is the
row-kind list. W1-LIVESTOCK-2's distinguishing reason, that the crypto family
"trades the weekend", is dropped: `globex_cryptocurrency`'s own header dates the
24/7 era to trade date 2026-05-30, so in November 2025 that family had no
Saturday trade date either.

### W1-ASM-9 — `globex_cryptocurrency`'s nine five-day-era `[N3]` dates carry no row (supersedes W1-CRYPTO-6)

**Memo:** §1.6 triage step 4, §1.7's third bullet and §1.4's `[N3]` instruction,
whose premise the corpus contradicts for these nine dates.

**Choice.** W1-CRYPTO-6 shipped `HolidayKind::Closed` on nine dates where CME
printed a 16:00 CT **pre-open** in place of the 16:00 CT final close, with every
event carrying the following business date: 2025-01-20, 2025-02-17, 2025-05-26,
2025-06-19, 2025-09-01, 2025-11-27, 2026-01-19, 2026-02-16 and 2026-05-25. In the
five-day era `has_weekend_close` short-circuits `identity::assign_normal`'s
business-date roll, so each row deleted exactly 1380 minutes — 23 hours — of
matching CME published as open. No `[N6]` predecessor exists on any of the
preceding evenings, so the prior-evening open was normal and matching ran: what
changed is only the trade-date label CME attached to the span, and 16:00 CT is
this family's own normal close, so the published stop instant moves no executable
boundary. The correct kind is **no row** — which is how `globex_fx` reads the same
shared records (W1-FX-1), and the sibling of how `globex_equity_index` /
`globex_interest_rates` (`early_close(12:00)`) and `globex_energy`
(`early_close(13:30)`) read their own variants of it. The scalar vocabulary cannot
state a merge of two crate trade dates into one operator trade date, so the nine
dates are declared gaps, closing condition the block rows (#93).

W1-CRYPTO-6's second justification — that the rows were what made the 24/7-era
roll reachable — is disproved by test: with the nine rows dropped,
`the_twenty_four_seven_era_rolls_the_trade_date_without_deleting_a_day` still
passes. The table goes from 32 rows (28 `closed`, 4 `early close`) to 24
(20 `closed`, 4 `early close`), counting W1-ASM-8's 2025-11-29 addition.
`a_closed_monday_removes_the_sunday_evening_block` asserted the deleted
behaviour and is replaced by its inverse,
`a_trade_date_merge_keeps_the_sunday_evening_block`;
`an_early_close_survives_a_closed_neighbour` becomes
`an_early_close_stands_without_a_closed_neighbour`.

### W1-ASM-10 — Every served row that ships a table moves to a monthly cadence, and a fence holds it there

**Memo:** §3.3 "Ledger", which directs `Cadence` = **monthly** for every family
with a shipped table.

**Choice.** Six served rows still carried their pre-branch schedule-churn cadence
of `quarterly` — `cfe`, `eurex`, `iceus`, `globex_grains`, `globex_livestock`,
`globex_nikkei_225_dollar` — while `globex_grains`'s own evidence file already
asserted that LAW-WATCH's monthly cadence applies because CME finalises holiday
hours roughly two weeks before each holiday. All six move to `monthly`, and
`assert_row_shape` now fails any served row whose `Holidays` cell is non-empty and
whose `Cadence` is not `monthly`, so a table landing in a later wave cannot ship
on a quarterly watch.

### W1-ASM-11 — The reverse holiday-evidence fence, and the doc sentences that outlived wave 0

**Memo:** §3.3, which asks for the evidence fence in **both** directions.

**Choice.** `every_holiday_row_appears_in_its_evidence_file` was forward-only, so
deleting a shipped row left the suite green with the evidence file still recording
it — verified by experiment before the fix. `every_evidence_holiday_line_exists_in_its_module`
closes the reverse direction: every `| <trade date> |` line under a `## Holidays`
heading must name a row of a module that declares the file, and must cite a
document id that module ships for that trade date. A date the crate deliberately
does not carry is a declared gap, which is prose beside the year's table and never
a line in it.

Separately, four public doc blocks still asserted that **no** holiday table
ships — `ExchangeCalendar::holiday_on`, `ExchangeCalendar::holiday_coverage`,
the `lib.rs` Scope section, `policy.rs`'s `DayPolicy` and `calendar/mod.rs`'s
"What this calendar is not" — which is the opposite of what wave 1 shipped and
told the consumer that `holiday_on` is always `None`. All five are rewritten to
name the wave rather than a count or a window, so they stay true as later waves
land. No gate can detect that phrasing, so the rule is recorded here: the "no
table ships" sentence must never be reintroduced.

---

## W7-1 — CME/CBOT/COMEX/NYMEX venue tables land (2026-09-13 UTC)

Stage 2.1 of `docs/plans/2026-09-12-path-to-release.md`, branch `cme-venue-holidays`,
one module `src/calendar/schedules/holidays/venues.rs` holding all four tables.

**D17's "ships no row" is read as `Unsourced`, not silence — and `iceus` already
decided this.** `HolidayCoverage` documents that inside the window a date with no
row is **audited normal**. Dropping a disputed date therefore makes the crate
positively claim the date was ordinary, which is false on every one of these dates,
and the reverse evidence fence (`every_evidence_holiday_line_exists_in_its_module`)
will not let a venue evidence file list a date its module does not ship — so the
choice is between a false claim and the variant §1.2 created for exactly this.
`W8-4` recorded the same reasoning for `iceus`; this change applies it to the four
CME venues and the two now agree on their face.

**"Disagree" includes a family that states no row.** A family with no row on a date
where another family states one has *audited the date normal*: that is a different
answer, not a missing one. Counting those as disagreements is what makes the
`no row in FX` dates gaps, and it is the conservative reading: the alternative would
let six of the twenty-two disputed dates ship an early close the FX family's own
evidence file audits as its ordinary grid.

Consequences: `cme` 9 `Closed` + 32 `Unsourced`; `cbot` 9 + 31; `comex` and `nymex`
36 rows each, no `Unsourced`, no dropped date. `cbot`'s ledger cadence moves
`quarterly` -> `monthly` (`W1-ASM-10`); the README count moves 22 -> 26. `W1-ASM-2`
is discharged for all four venues.

**Open, and deliberately not closed here:** `#95`'s cross-wave agreement audit. This
change derives the intersection over the one window the family tables cover
(2025-2027); the audit re-runs the same assertion over 2010-2027 and closes with the
last stage-2.2 family wave, each of which extends these four tables over its own
years by the same derivation.

**Measured cost, for #97.** `the_coverage_gate_is_sound_for_every_shipped_row` now
covers 26 identities instead of 22 and runs in **530 s** debug, up from ~7 minutes;
the four venue tables add 153 rows to a corpus that already opened the `[D-1, D+19]`
gate on nearly every day. `is_open` inside a regular session is unchanged at
**~241 ns** (237.8 ns detached), so the hot path this change could have hurt is not
the one it did; the gate's scan is.
