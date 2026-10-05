<!-- SPDX-License-Identifier: MIT-0 -->

# BENCH — Wave 1, the matrix re-measured with real tables attached

**Measured:** 2026-09-12 (UTC, `date -u`, LAW-UTC-DATES)
**Machine:** Apple M2 Max, Darwin 25.6.0 arm64
**Toolchain:** `rustc 1.97.1 (8bab26f4f 2026-07-14)`, the repository's pinned
channel; `cargo bench` release profile
**Harness:** Criterion, `benches/calendar_queries.rs`, extended this wave with
the two date classes §6.2 asks for — see §6 below.
**Settings:** `--warm-up-time 2 --measurement-time 5` for the full matrix. The
`globex_equity_index` group was additionally re-run three times at
`--measurement-time 6` with nothing else on the machine, and the **median of
three** is what §1 reports: the first pass of that group overlapped a
`cargo nextest` run and its figures were 20–50 % high. Every figure is
Criterion's point estimate.
**Identity:** `globex_equity_index` throughout, as §6.2 asks. It now ships a
real table: 36 rows over trade dates 2025-01-01 .. 2027-12-31.

This file sits beside `BENCH-wave0.md`, not over it. Wave 0's §7 named two
numbers that were upper bounds for want of a table to measure; both are
measured here.

---

## 0. The headline

| Claim | Measured |
|---|---|
| The built-in table costs nothing far from a holiday | `is_open`, regular: **240.9 ns** with the table, 236.9 ns with it detached — **+1.7 %**, inside the noise floor |
| Wave 0's gate measurement was an upper bound, and it held | the gate is now a direct `partition_point` with no `dyn` dispatch, and the far-from-a-holiday cost is the same as no layer at all |
| Asking an identity with a table for a row is a binary search | `holiday_on` = **5.04 ns** (310 ps with no table — that was the `None` arm) |
| The cold chart frame is unaffected | **2.962 ms** with the table against 3.138 ms detached — the sign is noise |
| On or adjacent to a holiday the derivation runs, and it is the cost | **5.4 µs** / **6.0 µs** against 228 ns detached — above §6.3's 3 µs, on ~13 days a year, with a named lever |

---

## 1. The bare calendar, with the table attached

Median of three clean runs. Wave 0's column is the same query on the same
machine with **no table shipped at all**, so the difference is exactly what the
built-in layer costs.

| Query | Instant class | Wave 0 (no table) | Wave 1 (table) | Δ |
|---|---|---|---|---|
| `is_open` | regular | 236.1 ns | **240.9 ns** | +2.0 % |
| `is_open` | overnight | 602.4 ns | 622.9 ns | +3.4 % |
| `is_open` | maintenance | 813.4 ns | 802.5 ns | −1.3 % |
| `is_open` | closed weekend | 482.3 ns | 481.0 ns | −0.3 % |
| `is_open` | **adjacent to a row** | — | **5.986 µs** | new |
| `is_open` | **on a row** | — | **5.397 µs** | new |
| `session_bounds` | regular | 237.9 ns | 242.1 ns | +1.8 % |
| `session_state` | regular | 248.7 ns | 250.8 ns | +0.8 % |
| `session_state` | maintenance | 13.28 µs | 13.84 µs | +4.2 % |
| `session_state` | closed weekend | 12.66 µs | 13.03 µs | +2.9 % |
| `trade_date` | regular | 3.73 µs | 3.793 µs | +1.7 % |
| `candle_end(Daily)` | regular | 3.50 µs | 3.463 µs | −1.1 % |
| `daily_window` | regular | 12.42 µs | 12.41 µs | −0.1 % |
| `holiday_on` | — | 310 ps | **5.04 ns** | the `None` arm became a search |

Every far-from-a-holiday row moves by less than the ±3 % noise floor Wave 0
recorded. **The gate does what it was built to do.** `holiday_on` going from
310 ps to 5.04 ns is not a regression: 310 ps was `table_for` answering `None`
and the compiler folding the call away; 5.04 ns is a binary search over a
36-row static slice, which is the number LAW-HOLIDAY-SCOPE's "bounded,
allocation-free and cheap enough to sit on the consumer's hot path" was asking
for.

## 2. The date-class split — Wave 0's deferred measurement

This is what `BENCH-wave0.md` §7 item 2 could not measure. The probes are both
**regular-session minutes**, so the only variable against the `regular` row is
the date class (W1-ASM-5 in `DECISIONS.md`).

| Date class | Probe | `is_open`, table attached | table detached | × |
|---|---|---|---|---|
| far from any holiday | 2026-04-20 10:00 CT | 239.6 ns | 236.9 ns | **1.01×** |
| adjacent to a row | 2026-11-25 10:00 CT | 5.696 µs | 228.5 ns | 24.9× |
| on a row | 2026-11-27 10:00 CT | 5.136 µs | 228.4 ns | 22.5× |

Three things this says.

**The gate is binary, and that is the design.** A date whose gate window holds
no row costs one `partition_point`; a date whose window holds one pays the full
trading-day derivation. There is no middle cost, because the expense was never
the lookup — it was deriving the trading day in order to know which row to
consult. That is §2.3's mechanism, measured on the built-in path rather than on
a caller's provider.

**The gate window is wider than a day.** 2026-11-25 carries no row of its own
and still pays 5.7 µs, because the occurrence it resolves could be assigned to
2026-11-26, which does. That is the gate being *sound* rather than tight, and
it is why "adjacent" is a date class in the memo at all.

**5.4 µs is above the 3 µs target.** It is a **Watch**, unchanged in kind from
Wave 0's 3.81 µs on a caller's layer, and §2.3's reduction 2 — hoisting the
trade-date derivation out of the per-rule loop — is the named lever. It applies
to the ~13 dates a year a family has rows for, plus their neighbours.

## 3. The layer matrix

`is_open`, full matrix run. The `none` row now means "built-in table and
nothing else", which is what a consumer actually gets.

| Layer | regular | overnight | maintenance | closed weekend | adjacent | on a row |
|---|---|---|---|---|---|---|
| none (built-in table) | 239.6 ns | 603.4 ns | 780.8 ns | 481.2 ns | 5.696 µs | 5.136 µs |
| `without_holidays()` | 236.9 ns | 576.5 ns | 757.3 ns | 456.5 ns | 228.5 ns | 228.4 ns |
| exception provider, gated out | 241.1 ns | 646.3 ns | 856.1 ns | 554.9 ns | 5.856 µs | 5.267 µs |
| exception provider, in coverage | 3.733 µs | 14.01 µs | 18.32 µs | 563.8 ns | 5.968 µs | 5.278 µs |
| `StaticDayPolicy`, record elsewhere | 3.759 µs | 13.92 µs | 18.65 µs | 468.7 ns | 5.844 µs | 5.272 µs |
| `StaticDayPolicy`, record on the date | 3.827 µs | 14.07 µs | 18.56 µs | 473.9 ns | 7.787 µs | 5.441 µs |

The `without_holidays` row is the A/B control the memo's §6.2 asks for, and it
is now a real control rather than the identity function it was in Wave 0: on
the two holiday date classes it is 25× faster because it has nothing to
consult. That is also what makes the fence
`without_holidays_is_the_identity_without_a_table_and_a_detachment_with_one`
provable.

Once a `StaticDayPolicy` is attached the built-in table's cost disappears into
it — the derivation is paid once and both layers read it — so the bottom three
rows are barely above the two-layer figures.

## 4. The daily window

| Layer | `candle_start` + `candle_end`, Daily | × bare |
|---|---|---|
| none (built-in table) | 12.31 µs | 1.00× |
| exception provider, gated | 14.88 µs | 1.21× |
| `StaticDayPolicy`, record elsewhere | 292.0 µs | 23.7× |

Against §6.3's `≤ 30 µs` target for the derivation far from a holiday,
**met** with room. The 292 µs is the same ungated `DayPolicy` story as Wave 0
(308.6 µs there) and is the strongest single argument for follow-up 9, now
filed as **#94**.

## 5. The cold chart frame

4,999 `is_open` probes at one-minute steps plus one daily close, over a
5,000-point window.

| Layer | start inside a regular week | start on a closed weekend |
|---|---|---|
| none (built-in table) | **2.962 ms** | **2.714 ms** |
| `without_holidays()` | 3.138 ms | — |

The table-attached frame is **6 % faster** than the detached one, which is the
noise floor on a 20-sample Criterion group, not a real effect. Wave 0 recorded
3.103 ms / 2.730 ms with no table. **The built-in layer does not cost a frame.**

## 6. What changed in the harness

`benches/calendar_queries.rs` gained two instant classes, `adjacent` and
`holiday`, wired through `bench_queries` so every layer in §3 is measured on
them. Both are regular-session minutes on `globex_equity_index`:

- `adjacent` = 2026-11-25 10:00 CT, the trade date before Thanksgiving;
- `holiday` = 2026-11-27 10:00 CT, which the table clips to a 12:15 CT close.

A first run used **2026-04-03 10:00 CT** for `holiday` — Good Friday, whose row
clips the close to 08:15 CT, making 10:00 a *closed* instant. That probe
measured **19.0 µs**, and it is a real number about a real query: `is_open` on
a closed minute of a holiday date scans candidate days and pays a derivation
for each. It is recorded here as the closed-instant observation it is, and not
as the date-class figure, because comparing it against §6.3's 167.7 ns regular
baseline would compare two different questions.

§8 adds one more group, `hot_path_year`, for the reason §8 states: a per-instant
figure cannot show how *often* the expensive instant is reached, which is what
the coverage gate's window decides.

## 7. Scoring §6.3

| §6.3 measurement | Target | Wave 1 | Verdict |
|---|---|---|---|
| `is_open`, regular, far from a holiday | ≤ +15 % over bare | **+1.7 %** with the real table | **Met** |
| `is_open`, closed weekend, far from a holiday | ≤ +16 % over bare | +5.4 % (481.0 vs 456.5 ns detached) | **Met** — Wave 0's +20 % was the `dyn` provider's gate, and the built-in table's direct `partition_point` is the cheaper path Wave 0 §7 predicted |
| `is_open`, on or adjacent to a holiday | ≤ 3 µs | 5.4 µs on a row, 6.0 µs adjacent | **Watch.** ~13 dates a year plus neighbours; §2.3's reduction 2 is the lever |
| cold axis, 4,999 `is_open` + 1 close | ≤ 1.3× | **0.94×** | **Met** |
| daily trading-day derivation, far from a holiday | ≤ 30 µs | 12.41 µs | **Met** |
| `StaticDayPolicy` attached, date not covered | ≤ 2×, once `may_affect` ships | 15.6× — `may_affect` has not shipped | **Deferred to #94**, as the target itself says |

**D19's precondition holds with real data.** The two far-from-a-holiday
`is_open` rows the memo makes the merge conditional on are met, and the
closed-weekend row that Wave 0 marked Watch is now met as well, for the reason
Wave 0 §7 item 1 predicted: the built-in gate has no virtual call in it.

**Restated after #97 — see §8.** The wave-1 table above is written against the
`[D, D + 1]` window the wave-1 engine actually had. W1-ASM-6 later widened it to
the derivation's own `[D - 1, D + 19]`, which made the *frequency* of every
expensive row above wrong even though its *price* was unchanged; §8 re-measures
both against the narrowing that restores `[D, D + 1]` where the derivation
allows it. The two far-from-a-holiday rows, the cold axis and the derivation
still meet their targets; the on-or-adjacent row is still a Watch, now with the
follow-up issue that re-measurement opened named against it.

---

## 8. The narrowed window re-measured — issue #97

**Measured:** 2026-09-17 (UTC, `date -u`, LAW-UTC-DATES)
**Machine:** Apple M2 Max, Darwin 25.6.0 arm64, macOS 26.6.2
**Toolchain:** `rustc 1.97.1 (8bab26f4f 2026-07-14)`, the repository's pinned
channel; `cargo bench` release profile
**Harness:** Criterion, `benches/calendar_queries.rs`, extended with the
`hot_path_year` group below. §6's instants, layers and settings are unchanged,
so every wave-1 number is directly comparable.
**Head:** `coverage-gate-narrowing` off `main` = `6fc7bd7` (the merged wave 4).
The A/B is that same harness and head with **only**
`src/calendar/query/{identity,schedule,periods}.rs` reverted to the base.

### 8.1 What the narrowing changed, measured A/B

| `globex_equity_index`, full matrix | Base (`[D-1, D+19]`) | Narrowed | Change |
|---|---|---|---|
| `is_open`, regular minute | 244.21 ns | **238.64 ns** | −2 % |
| `is_open`, adjacent to a row | 7.412 µs | **5.517 µs** | **−26 %** |
| `is_open`, on a row | 8.371 µs | **4.975 µs** | **−41 %** |
| `is_open`, closed weekend minute | 644.14 ns | **476.65 ns** | **−26 %** |
| `is_open`, maintenance minute | 1.321 µs | **801.5 ns** | **−39 %** |
| `is_open`, overnight minute | 672.45 ns | **622.9 ns** | −7 % |
| `session_state`, regular | 250.72 ns | **237.2 ns** | −5 % |
| `session_state`, closed weekend | 12.62 µs | 12.83 µs | +2 % |
| `session_state`, maintenance | 13.66 µs | 13.76 µs | +1 % |
| `trade_date`, regular | 3.848 µs | 3.960 µs | +3 % |
| `candle_end(Daily)`, regular | 3.563 µs | 3.574 µs | — |
| `daily_window` | 12.77 µs | 12.86 µs | +1 % |
| **`hot_path_year`, table attached** | **242.84 ms** | **55.19 ms** | **−77 %** |
| `hot_path_year`, `without_holidays()` | 18.97 ms | 19.82 ms | +4 % |

The load-bearing figure is the last pair, and it is a **cost**, not an exit
count: `hot_path_year` times 35,040 `is_open` probes through 2026 with the table
attached and with it detached, and nothing in it observes a gate exit. The exit
rate below is therefore **computed** from the shipped rows and the window rule —
the gate exits exactly when `may_affect([first, last])` finds no row, and the
window is the one §8.1's A/B shows — and the measured ratio is what that rate
buys:

- base: **12.8×** the detached cost, i.e. the gate opened on essentially every
  instant, which is the consequence W1-ASM-6 recorded;
- narrowed: **2.8×**. Of 2026's 35,040 probes, **2,074 (5.9 %)** resolve into a
  window that holds a row — a probe before the day's first open resolves the
  previous day's wrapped occurrence, so a row on `R` is in the window of the
  probes from `R - 1` 17:00 CT through `R` 08:30 CT — so **94.1 % of instants
  cannot open the gate at all** and leave it on one binary search. §6's and D14's
  "~97 % of days exit in ~20 ns" is approached rather than reached on this table.
- and the 5.9 % is concentrated where it belongs: the twelve 2026 rows, two of
  them whole-day closures whose own closed minutes (192 of those probes) cost the
  candidate-day scan §6 records at ~19 µs, the day before each row from its
  17:00 CT evening leg, and the row's own day.

The count reproduces from `src/calendar/schedules/holidays/globex_equity_index.rs`'s
2026 rows and the window rule alone; the script is in §8.5.

The adjacent/on-a-row columns show the same effect from the other side: those
two instants still pay a derivation, because the *wrapped evening occurrence*
opening the day before Thanksgiving carries Thanksgiving's trade date, but the
gate is no longer open on their neighbours — the day before that, or the same
day a week earlier — which is what −26 %/−41 % on those classes is measuring.

Two codegen notes, because they decide whether the narrowing is free:

1. A tradeable rule answers the self-dating question with its own close, so the
   session path — every `is_open`, `session_state`, `session_bounds` and
   `next_session_after` query — pays **nothing**; only an order-entry rule scans
   the day's session rules.
2. That scan is `#[inline(never)]`. Inlined into the window function it moved
   the multi-candidate queries by tens of percent with byte-identical answers —
   measured on the same harness: `trade_date` 3.85 → 6.06 µs (base → inlined
   narrowing), `candle_end(Daily)` 3.56 → 4.82 µs, `session_state` on a closed
   weekend 12.6 → 18.6 µs, `is_open` on an overnight minute 672 → 903 ns. Held
   out of line, every one of them is at parity with the base, as the table above
   shows. A reviewer can reproduce the pair by removing the attribute and
   re-running §8's command.

### 8.2 §6.3 re-scored

Median of three clean runs of the key group at `--measurement-time 6`, as §1's
methodology asks; the detached control from the same runs.

| §6.3 measurement | Target | Wave 1 | #97 | Verdict |
|---|---|---|---|---|
| `is_open`, regular, far from a holiday | ≤ +15 % over bare | +1.7 % | **+8.7 %** (246.3 vs 226.7 ns) | **Met** |
| `is_open`, closed weekend, far from a holiday | ≤ +16 % over bare | +5.4 % | **+1.8 %** (486.8 vs 478.2 ns) | **Met** |
| `is_open`, on or adjacent to a holiday | ≤ 3 µs | 5.4 / 6.0 µs | 5.19 µs on a row, 5.66 µs adjacent | **Watch** — unchanged in price, and now paid on 5.9 % of the year's probes rather than nearly all of them; the follow-up issue named below holds the lever |
| cold axis, 4,999 `is_open` + 1 close | ≤ 1.3× | 0.94× | **1.03×** (3.106 vs 3.022 ms detached) | **Met** |
| daily trading-day derivation, far from a holiday | ≤ 30 µs | 12.41 µs | **12.95 µs** | **Met** |
| `StaticDayPolicy` attached, date not covered | ≤ 2×, once `may_affect` ships | 15.6× | 19.8× | **Deferred to #94**, unchanged: the trait still publishes no coverage window |

**D19's precondition holds, and now on the clause it was written for.** The
far-from-a-holiday rows are met on a *real* table whose rows are inside the
window — which is the state the wide window made impossible to reach — and a
year of hot-path probes costs 2.8× a calendar with no table at all, with 94.1 %
of those probes unable to open the gate. The `≤ 3 µs` row is still a Watch, and
it is the one that keeps the year scan at 2.8× rather than ~1.0×.

### 8.3 The fence's own cost

`the_coverage_gate_is_sound_for_every_shipped_row` sweeps the same rows with a
reference layer that covers the whole sweep, so its *reference* path derives at
every probe by construction and the narrowing cannot remove that half. Measured
on this branch's head in a debug build: **1,349.7 s (22.5 min)**, against
**~1,611 s (27 min)** recorded for the wave-4 head — a 16 % saving from the
gated half alone, and the figure to compare against when the next wave's rows
land. The new premise fence,
`every_shipped_session_occurrence_is_dated_by_its_own_open_or_the_next_day`,
costs **82.6 s** for its full population — 18 years × all 128 close-dated
identities, 1,195,680 occurrences. The first version of the sweep was no cheaper
(82.7 s) while covering only 83 of those identities: it ended at the first gap
longer than the 14-day search behind `next_session_open_after`, which is what a
launch-dated identity's pre-launch span is. The review at head `db55666` asked
for a population guard, the guard found it, and the fixed sweep covers 45 more
identities for the same money.

### 8.4 What this does not close

The per-instant price of an instant whose own occurrence can carry a row —
5.19 µs on a row, 5.66 µs adjacent — is the wave-1 Watch, and the narrowing
changes only how often it is charged. Two levers remain: §2.3's reduction 2
(hoisting the trade-date derivation out of the per-rule loop), and making the
gate's window **per occurrence** rather than per opening day, which would let the
regular session of the day before a row exit even though that day's wrapped
evening leg legitimately reaches the row. Both are tracked as **#107**, the
issue this re-measurement opened.

### 8.5 The computed exit share

The count in §8.1 is arithmetic on the shipped rows and the window rule, and it
reproduces from `globex_equity_index`'s 2026 rows. A probe at UTC instant `t`
resolves an occurrence opening on the venue-local day `D` of `t`; when `t` is
before that day's first open (08:30 CT) it resolves the *previous* day's wrapped
occurrence instead, whose window is `[D - 1, D]`. The gate opens exactly when the
window holds a row:

```python
from datetime import date, datetime, timedelta

rows = {date(2026, 1, 1), date(2026, 1, 19), date(2026, 2, 16), date(2026, 4, 3),
        date(2026, 5, 25), date(2026, 6, 19), date(2026, 7, 3), date(2026, 9, 7),
        date(2026, 11, 26), date(2026, 11, 27), date(2026, 12, 24),
        date(2026, 12, 25)}                      # all twelve, from the module
open_minutes = 8 * 60 + 30                       # the equity grid's first open

def local(t):                                    # UTC probe -> CT wall clock
    day = t.date()
    cdt = date(2026, 3, 8) <= day < date(2026, 11, 1)
    return t - timedelta(hours=5 if cdt else 6)

expensive = total = 0
t, end = datetime(2026, 1, 1), datetime(2027, 1, 1)
while t < end:
    total += 1
    here = local(t)
    day = here.date()
    first, last = ((day - timedelta(days=1), day) if here.hour * 60 + here.minute < open_minutes
                   else (day, day + timedelta(days=1)))
    expensive += first in rows or last in rows
    t += timedelta(minutes=15)
print(f"{expensive} of {total} = {100 * expensive / total:.1f} % expensive, "
      f"{100 * (total - expensive) / total:.1f} % exit")
```

It prints `2074 of 35040 = 5.9 % expensive, 94.1 % exit` — the same figure §8.1
states, and the reason the *measured* ratio is the one to quote and the exit
share is the one to compute. An earlier draft of this section listed nine of the
module's twelve 2026 rows — the three written across several lines
(`2026-04-03`, `2026-11-27`, `2026-12-24`) fell outside a single-line scan — and
printed `1690 / 4.8 % / 95.2 %`. The review at head `db55666` recomputed it and
was right; the measured ratio never depended on the list.

---

## Reproducing

```bash
cd exchange-hours-rs
cargo bench --bench calendar_queries -- --warm-up-time 2 --measurement-time 5
# the bare group, three times, with nothing else running:
for i in 1 2 3; do
  cargo bench --bench calendar_queries -- --measurement-time 6 '^globex_equity_index/'
done
```

§8's A/B is the same command with the base sources restored for the three
query-engine files and nothing else changed:

```bash
git stash push -- src/calendar/query/identity.rs src/calendar/query/schedule.rs src/calendar/query/periods.rs
cargo bench --bench calendar_queries -- --warm-up-time 2 --measurement-time 5 \
  'hot_path_year|^globex_equity_index/|^overlay_layers/none/'
git stash pop
```

The codegen pair in §8.1 is the attribute removed and the same group re-run:

```bash
# remove `#[inline(never)]` from `a_session_reaches` in src/calendar/query/identity.rs
cargo bench --bench calendar_queries -- --warm-up-time 2 --measurement-time 5 \
  '^globex_equity_index/|^overlay_layers/none/'
```
