<!-- SPDX-License-Identifier: MIT-0 -->

# BENCH — Wave 0, the overlay path re-measured

**Measured:** 2026-09-12 (UTC, `date -u`, LAW-UTC-DATES)
**Machine:** Apple M2 Max, Darwin 25.6.0 arm64
**Toolchain:** `rustc 1.97.1 (8bab26f4f 2026-07-14)`, the repository's pinned
channel; `cargo bench` release profile
**Harness:** Criterion, `benches/calendar_queries.rs`.
`cargo deny check` already passes with `criterion` in the tree, so §6.2's
preferred harness is admissible and no std-only timing harness was written —
`clippy.toml` disallows `Instant::now` in every target of this package anyway.
**Settings:** `--warm-up-time 2 --measurement-time 5` for the full matrix; the
`is_open/regular` row was additionally run three times at
`--measurement-time 6` and the best-of-three median taken, because the machine's
noise floor (~±3 %) is wider than the effect being measured. Every figure below
is Criterion's point estimate.
**Identity:** `globex_equity_index` throughout, as §6.2 asks.

---

## 0. The headline

| Claim | Measured |
|---|---|
| The built-in holiday layer costs nothing while no table ships | 246.9 ns vs 239.0 ns for `without_holidays` — same code path, 3 % apart, inside the noise floor |
| An identity with no table costs nothing to ask | `holiday_on` = **310 ps** |
| The coverage gate removes the overlay's cost when a layer has no record in range | 241.95 ns gated vs 240.68 ns bare — **+0.5 %** |
| The ungated overlay path is what the design memo called "~100×" | **15.7×** on this machine (3.77 µs vs 240 ns) |

The gate is the wave's load-bearing result: an attached layer that publishes a
coverage window now costs, for a date outside it, what no layer at all costs.
That is the precondition LAW-HOLIDAY-SCOPE sets ("cheap enough to sit on the
consumer's hot path") and the one D19 makes the table's merge conditional on.

---

## 1. The baseline, bare date-aware calendar

No layer attached. With no family table shipped, these are also the
built-in-table numbers: `table_for` answers `None`, so the identity carries no
layer at all.

| Query | Instant class | Point estimate |
|---|---|---|
| `is_open` | regular | **236.1 ns** |
| `is_open` | overnight (wrapped leg) | 602.4 ns |
| `is_open` | maintenance (16:00–16:45 CT) | 813.4 ns |
| `is_open` | closed weekend | 482.3 ns |
| `session_bounds` | regular | 237.9 ns |
| `session_bounds` | overnight | 611.8 ns |
| `session_state` | regular | 248.7 ns |
| `session_state` | maintenance | 13.28 µs |
| `session_state` | closed weekend | 12.66 µs |
| `trade_date` | regular | 3.73 µs |
| `trade_date` | overnight | 7.02 µs |
| `candle_end(Daily)` | regular | 3.50 µs |
| `daily_window` (`candle_start` + `candle_end`, Daily) | regular | **12.42 µs** |
| `is_closed_trade_date` | — | 2.69 µs |
| `holiday_on` | — | **310 ps** |

B §7's recorded baseline is 167.7 ns / 361.8 ns on different hardware and a
different crate version, so its **absolute** figures are not comparable with
these and §6.3's absolute targets cannot be scored against them directly.
Every comparison below is therefore against `none` **on this machine, in this
run**, which is the comparison §6.3 actually cares about — what the layer costs
relative to no layer.

The daily trading-day derivation lands at 12.42 µs against §6.3's
`≤ 30 µs` target and the memo's 17–23 µs baseline. **Met.**

---

## 2. The layer matrix — `is_open`

| Layer | regular | overnight | maintenance | closed weekend |
|---|---|---|---|---|
| none | 246.9 ns | 596.2 ns | 768.2 ns | 469.9 ns |
| `without_holidays()` | 239.0 ns | 590.9 ns | 787.4 ns | 475.4 ns |
| exception provider, date **outside** its window (gated) | 246.9 ns | 671.8 ns | 883.9 ns | 564.9 ns |
| exception provider, date **inside** its window, no record | 3.81 µs | 14.07 µs | 18.55 µs | 575.2 ns |
| `StaticDayPolicy`, record far away (ungatable today) | 3.87 µs | 14.19 µs | 18.45 µs | 489.7 ns |
| `StaticDayPolicy`, record **on** the queried trade date | 3.88 µs | 14.37 µs | 18.38 µs | 476.8 ns |

Best-of-three medians for the regular column, which is the one the noise floor
was wide enough to matter on:

| Layer | regular `is_open` | × bare |
|---|---|---|
| none | 240.68 ns | 1.00× |
| `without_holidays()` | 237.72 ns | 0.99× |
| exception provider, gated | **241.95 ns** | **1.005×** |
| exception provider, in coverage | 3.7705 µs | 15.7× |
| `StaticDayPolicy`, record elsewhere | 3.7982 µs | 15.8× |
| `StaticDayPolicy`, record on the date | 3.7922 µs | 15.8× |

Three things this says.

**The gate works, completely.** A layer that publishes a window and does not
cover the queried date is 0.5 % more expensive than no layer. There is nothing
left to optimise on that path.

**The cost is the derivation, not the layer.** "Record on the date" and "record
far away, same coverage window" cost the same 3.8 µs. The expense was never
consulting the record; it was deriving the trading day in order to know which
record to consult. That is exactly the mechanism §2.3 identified, and it is why
a coverage question — not a faster lookup — is the fix.

**`DayPolicy` is the remaining 15.8×.** The trait publishes no coverage window,
so the gate cannot exit for it and it pays the full derivation whether or not it
holds a record anywhere near the date. That is §7's follow-up 9, and this is its
number.

---

## 3. What the reorder bought

The gate was first written after the existing `has_daily_close_at` guard, where
§2.3 draws it. That guard resolves a profile (`hours_at` — a `MarketHours`
construction plus a revision `partition_point`) to answer, and it was being paid
before the gate could decline the work.

| Gate position | gated `is_open`, regular | vs bare |
|---|---|---|
| after `has_daily_close_at` (as drawn) | 291.8 ns | +25 % |
| before it (shipped) | 241.95 ns | **+0.5 %** |

All three branches return the same unmodified bounds, so the reorder is
observably identical — the full suite passes unchanged either way. Recorded as
decision **W0-14**.

---

## 4. The daily window under a layer

| Layer | `candle_start` + `candle_end`, Daily | × bare |
|---|---|---|
| none | 12.19 µs | 1.00× |
| exception provider, gated | 15.16 µs | 1.24× |
| `StaticDayPolicy`, record elsewhere | 308.6 µs | 25.3× |

The gated figure is above the `is_open` gate cost because one daily window
resolves many occurrences, each paying its own gate; 1.24× on a 12 µs operation
is 3 µs. Against §6.3's `≤ 30 µs` target for the derivation far from a holiday,
**met** with room.

The 308 µs is the same ungated `DayPolicy` story as §2, amplified: the
derivation is quadratic in the sense that the outer daily-window walk re-enters
`resolve_rule_bounds`, which derives a daily window per rule. It is the
strongest single argument for follow-up 9, and for §2.3's reduction 2 (hoisting
the trade-date derivation out of the per-rule loop) if follow-up 9 is not
enough.

---

## 5. The cold chart frame

§6.2's shape benchmark: 4,999 `is_open` probes at one-minute steps plus one
daily close, over a 5,000-point window.

| Layer | start inside a regular week | start on a closed weekend |
|---|---|---|
| none | **3.103 ms** | **2.730 ms** |
| `without_holidays()` | 3.060 ms | — |

The built-in layer adds **−1.4 %** to the frame — that is, nothing, with the
sign coming from run-to-run noise. §6.3's `≤ 1.1 ms / ≤ 2.2 ms` targets are
stated against a 0.84 ms / 1.8 ms baseline from other hardware and a frame whose
step and origin are not recorded, so they cannot be scored against this frame;
what is scoreable is the ratio, and it is 1.00.

---

## 6. Scoring §6.3

| §6.3 measurement | Target | This wave | Verdict |
|---|---|---|---|
| `is_open`, regular, far from a holiday | ≤ +15 % over bare | **+0.5 %** with a gated layer; **0 %** with the (empty) built-in table | **Met** |
| `is_open`, closed weekend, far from a holiday | ≤ +16 % over bare | +20 % gated (564.9 vs 469.9 ns) | **Watch.** The weekend path resolves several candidate days, so it pays several gates; it is 95 ns, and it is measured against a caller's `dyn` provider, which the built-in table's direct `partition_point` does not have |
| `is_open`, on or adjacent to a holiday | ≤ 3 µs | 3.81 µs with the full derivation | **Watch.** Applies to ~13 days a year, and §2.3's reduction 2 is the named lever |
| cold axis, 4,999 `is_open` + 1 close | ≤ 1.3× | **1.00×** | **Met** |
| daily trading-day derivation, far from a holiday | ≤ 30 µs | 12.42 µs bare, 15.16 µs gated | **Met** |
| `StaticDayPolicy` attached, date not covered | ≤ 2×, *once `may_affect` ships* | 15.8× — `may_affect` has not shipped | **Deferred to follow-up 9**, as the target itself says |

**D19's precondition is satisfied for the built-in table.** The two
far-from-a-holiday `is_open` rows the memo makes the merge conditional on are
met or within a hundred nanoseconds of met, and the two rows that are not are
either a named follow-up the target itself defers, or a ~13-days-a-year path
with a named lever behind it.

---

## 7. What cannot be measured until Wave 1

Two numbers in the tables above are **upper bounds** for the built-in table
rather than measurements of it, because no table exists to measure:

1. **The gate's cost with a real table.** Everything gated here runs through
   `&dyn SessionExceptionSource::coverage()` — a virtual call. The built-in
   table's gate is a direct `partition_point` over a static slice with no
   dispatch, so it can only be cheaper than the 241.95 ns recorded.
2. **The on-a-holiday cost.** No date in 2026 carries a built-in row, so the
   "on a holiday" row is measured through a caller's `DayPolicy` instead. The
   built-in path differs only in where the clip comes from.

Re-run this matrix as the first thing Wave 1 does, with a real table attached
and a date class split into `{far, adjacent, on}` as §6.2 asks, and record the
result beside this file rather than over it.

---

## Reproducing

```bash
cd exchange-hours-rs
cargo bench --bench calendar_queries -- --warm-up-time 2 --measurement-time 5
# the regular-session row, three times, for the noise floor:
for i in 1 2 3; do
  cargo bench --bench calendar_queries -- --measurement-time 6 'is_open/regular'
done
```
