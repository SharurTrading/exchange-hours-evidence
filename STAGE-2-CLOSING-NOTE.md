Posted by an AI agent running as `deepseek-flash` (DeepSeek Harness), using the maintainer's GitHub login.

Closing note. Both halves of Stage 2 are merged: **2A** the coverage metadata and error vocabulary (#122), **2B** the query and adapter migration (#126, merged as `d5cf64f`).

`main` at `d5cf64f` passes the full chain: fmt, `clippy --all-targets -D warnings` (0 findings), **990/990** tests, doctests, `doc -D warnings`, MSRV, and `cargo deny`.

## What 2B delivered

Identity-backed date-aware queries return `Result<existing_value, CalendarQueryError>`, preserving `Option` inside `Ok` where it means genuine absence. Unsupported coverage, a known closure, an absent session and search exhaustion stay distinct, and no error is converted to `false`, `None` or a default grid. Detached caller-supplied `MarketHours` snapshots keep their signatures and their no-holiday contract, because a snapshot carries no identity and therefore claims no coverage.

## Three pre-existing defects found and fixed

1. **Overlays bypassed the floor.** `PolicyCalendar`'s candle adapters and `normal_week_open_seconds_containing` on both calendars omitted the gate `ExchangeCalendar`'s twins apply, so attaching **any** `DayPolicy` or `SessionExceptions` provider turned a pre-floor probe from a refusal into an answer.
2. **A detached snapshot lost `Halt`/`Maintenance` below the floor.** `trade_date` clamped the pre-floor trade date unconditionally, so a caller-supplied snapshot reported a plain closure where its own rules say `Halt`.
3. **The phase gate masked the floor** on pre-floor order-entry probes, reporting `OutsideCoveredRange` where the floor governs.

## Acceptance

`tests/coverage_query_errors.rs` (17 tests) covers the floor in opposing zones and in venue-local time, a returned session never truncated at a date boundary, a positive answer never refused, no refusal readable as `false`/`None`, detached snapshots answering pre-floor, `without_holidays` answering its normal week without lifting the floor, an overlay unable to bypass the floor, and a sourced closure reading as `Closed`. The remaining plan cases live where they already had a home: `calendar_policies.rs` (`SearchExhausted` distinct from `Ok(None)`), `order_entry_phase.rs` (the queue boundary), `coverage_metadata.rs` (supported metadata fixtures). The benchmark comparison is in the PR body as §6 requires.

## Follow-ups filed, not left in prose

- **#125** — `is_open` regressed 3-5x (measured, non-overlapping CIs). Judged **not** a merge blocker, with the reasoning stated in the PR body: correctness is what this stage is for, the queries remain bounded and allocation-free, and nothing pins a version until Stage 6 (#118).
- **#127** — an empty `SessionExceptions` provider changes an answer on a withheld date; the bare path is the suspect.
- **#128** — the gate and `coverage_on` report different variants on a doubly-gapped date.
- **#86** stays open, partially closed: the dated-constant fence now reads all 15 shipped constants across both `## Revision rows` and `## Dated selectors`, but a cutover written as a comparison inside a selector is still not collected. That belongs to Stage 5's retained-boundary audit.
