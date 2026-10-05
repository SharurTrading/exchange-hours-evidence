# Stage 2B — signature migration map (working note)

Derived from `src/calendar/exchange_calendar/mod.rs` at the Stage 2A head

(`2c47997839785770e8509166e5870586908b4777`), then re-checked against the Stage 2A

**merged** head `59bb955` (PR #122, squash of `fa5f0e9`; parent `7fa3cb5`). This is

the handoff artifact plan section 6 asks for; it is a note, not a committed file.

## State at handoff

Stage 2A is merged and `main` is `59bb955`. Stage 2B has not started. `#115` stays

open because it tracks both halves. The 2A public surface this migration builds on

is live and fenced: `CalendarQueryError` (`BeforeSupportFloor`, `OutsideCoveredRange`,

`UnresolvedGap`, `SearchExhausted`), `CalendarCoverage` (`coverage_on`,

`is_complete_on`, `complete_ranges`, `gaps`, `phase_gaps`, `holiday_contract`),

`DateRange`, `DateCoverage`, `CoverageGap`, `CoverageGapReason`, `HolidayContract`,

`PhaseGap`, `ExchangeCalendar::coverage()`. The counts below (18 methods, 11

unchanged, 22 call-site files) are re-verified at that head.

Two open items carried into 2B, neither blocking it: `#124` (the `#79` era bound day

is unprobed by the Sunday fence) and `#123` (the crypto Pre-Open onset is undated).

## Rule

The plan: *identity-backed date-aware queries return*

`Result<existing_value, CalendarQueryError>`*, preserving `Option` inside `Ok` where it*

*means genuine absence*. So a method migrates when it resolves an *instant or date*

through the identity's calendar. Constructors and accessors do not.

## Methods that MIGRATE (18)

| Method | New shape |
|---|---|
| `is_open` | `Result<bool, CalendarQueryError>` |
| `is_open_with` | `Result<bool, CalendarQueryError>` |
| `is_open_regular` | `Result<bool, CalendarQueryError>` |
| `is_open_extended` | `Result<bool, CalendarQueryError>` |
| `is_accepting_orders` | `Result<bool, CalendarQueryError>` |
| `is_order_entry_only` | `Result<bool, CalendarQueryError>` |
| `session_bounds` | `Result<Option<(DateTime<Utc>, DateTime<Utc>)>, CalendarQueryError>` |
| `session_bounds_with` | `Result<Option<(DateTime<Utc>, DateTime<Utc>)>, CalendarQueryError>` |
| `next_session_after` | `Result<Option<DateTime<Utc>>, CalendarQueryError>` |
| `next_session_after_with` | `Result<Option<DateTime<Utc>>, CalendarQueryError>` |
| `next_session_open_after` | `Result<Option<DateTime<Utc>>, CalendarQueryError>` |
| `is_maintenance` | `Result<bool, CalendarQueryError>` |
| `session_state` | `Result<SessionState, CalendarQueryError>` |
| `trade_date` | `Result<Option<NaiveDate>, CalendarQueryError>` |
| `is_closed_trade_date` | `Result<bool, CalendarQueryError>` |
| `is_closed_all_day_in_calendar` | `Result<bool, CalendarQueryError>` |
| `is_closed_all_day_on` | `Result<bool, CalendarQueryError>` |
| `is_closed_all_day_at` | `Result<bool, CalendarQueryError>` |

## Methods that DO NOT migrate (11)

| Method | Why |
|---|---|
| `new` | constructor |
| `for_market_hours_key` | constructor |
| `without_holidays` | detaches a layer; resolves no date |
| `holiday_on` | returns the row itself; `None` already means absent-or-normal |
| `holiday_coverage` | reports the window; adds no answer |
| `coverage` | the metadata accessor 2A added |
| `source` | accessor |
| `exchange` | accessor |
| `market_hours_key` | accessor |
| `hours_at` | the plan states `hours_at`/`hours_for_*` check normal-week coverage only and keep their no-holiday contract |
| `tz` | invariant zone; the plan requires resolving it without a pre-floor epoch snapshot |

The same file's two remaining public functions — `calendar_for_exchange` and
`calendar_for_market_hours_key` — are the identity-to-calendar constructors. They
resolve no date, so they do not migrate. 18 + 11 + 2 accounts for all 31 public
functions in `exchange_calendar/mod.rs`, which is why neither list can silently drop
one.

Also unchanged, outside this type: `hours_for_exchange`,
`hours_for_market_hours_key`, `session_profile`, the `bulk` builders,
detached caller-supplied `MarketHours` queries, and the fixed-snapshot adapters.

## Public free functions that migrate

| Function | New shape |
|---|---|
| `session_bounds` / `session_bounds_with` | `Result<..>` |
| `next_session_after` / `next_session_after_with` / `next_session_open_after` | `Result<..>` |
| `candle_start` / `candle_end` (+ `_with`) | `Result<..>` |
| `time_end_of_day` | see note |

## In-crate call sites to migrate in the same PR

- `src/calendar/candle.rs`
- `src/calendar/coverage.rs`
- `src/calendar/exceptions.rs`
- `src/calendar/exceptions/static_table.rs`
- `src/calendar/exchange_calendar/candles.rs`
- `src/calendar/futures_profile.rs`
- `src/calendar/hours.rs`
- `src/calendar/mod.rs`
- `src/calendar/policy.rs`
- `src/calendar/policy/candles.rs`
- `src/calendar/policy/static_policy.rs`
- `src/calendar/query/candles.rs`
- `src/calendar/query/identity.rs`
- `src/calendar/query/periods.rs`
- `src/calendar/query/replacement.rs`
- `src/calendar/query/schedule.rs`
- `src/calendar/query/sessions.rs`
- `src/calendar/query/status.rs`
- `src/calendar/resolution.rs`
- `src/calendar/schedules/holidays/mod.rs`
- `src/calendar/session.rs`
- `src/lib.rs`

## The benchmark is a 2B call site *and* the required comparison

`benches/calendar_queries.rs` (`[[bench]] name = "calendar_queries"`, `harness = false`,
criterion) calls six of the migrated methods, so it must be migrated in the same PR:

| method | call sites in the bench |
|---|---|
| `is_open` | 14 |
| `candle_end` | 5 |
| `session_state` | 3 |
| `candle_start` | 3 |
| `trade_date` | 2 |
| `session_bounds` | 2 |

Benchmark groups: `globex_equity_index`, `hot_path_year`, `query_surface`,
`overlay_layers`, `cold_axis`.

The plan requires 2B to "include benchmark comparison", so the run must be captured
**before** the migration (at the 2A head, or at 2B's base) and after, on the same
machine, and recorded. `cargo bench --bench calendar_queries`.

Note for the record: `cold_axis` exercises the pre-floor epoch-snapshot path, and the
plan's contract says to resolve invariant timezone metadata *without* querying a
pre-floor epoch snapshot — so that group's setup may need reworking rather than a
mechanical `?`.

## Suggested 2B order

1. `src/calendar/query/schedule.rs` — thread the coverage check through `QueryContext`
   so every query family fails at one place rather than eighteen.
2. `src/calendar/exchange_calendar/mod.rs` — the 18 method signatures, plus the free
   functions in `session.rs` and `candle.rs`.
3. `src/calendar/policy.rs`, `policy/candles.rs` — the caller layers.
4. `benches/calendar_queries.rs` and the in-crate call sites.
5. Tests: the existing suites migrate mechanically; add the plan's boundary cases
   (before/at the floor in opposing zones, crossing sessions, post-close queues, future
   bounds, internal gaps, lookahead, periods, overlays, synthetic and no-holiday scopes).
6. Resolve #77 (static-season docs) and #86 (retained-boundary fences) in the same PR,
   as plan section 6 requires.

## Open question for 2B

`gaps()` reports a declared phase gap *in place of* a scope's overlapping date-level
spans, rather than in addition to them (documented on `gap_reason_on` in 2A, and fenced
by `the_declared_phase_level_gaps_match_the_inventory`). Note the `#79` declaration is
**era-bounded** as of the fix merged in #122: it is retired at 2026-08-22, so for `cme`
the phase record covers the dated era (2025-01-01 through 2026-08-21) and dates at or
after the bound fall through to the ordinary date-level facts. `coverage_on`,
`is_complete_on`, `complete_ranges` and `gaps` agree on where the gap stops. Where a
declaration is whole-domain, `#93`'s record still shadows `#123`'s for
`globex_cryptocurrency`; the full list is on `phase_gaps()`.

The verdicts are unchanged either way. But if 2B's error mapping needs per-date reasons
— `UnresolvedGap` versus `OutsideCoveredRange` — this is the place to revisit it,
because `gaps()` will not always name every span a caller might want a reason for.
