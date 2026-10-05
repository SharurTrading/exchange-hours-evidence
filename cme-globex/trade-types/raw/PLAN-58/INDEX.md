# PLAN-58 evidence index

Gate: PLAN-58 (planner for exchange-hours-rs issue #58)
Role: planner. **No new retrieval was performed.** This gate consumed only
artifacts already on disk and already hash-indexed by the eight research gates
and their adversarial verifiers.

| File | URL | Capture timestamp | sha256 |
|---|---|---|---|
| (none) | — | — | — |

## Inputs consumed (read-only; each carries its own INDEX.md and hashes)

- `/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/*.json` (9 gate results)
- `/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/*.verify.json` (9 verdicts; where a verdict reports a discrepancy, the verdict wins)
- `/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/U8-cross-zone-design.md`
- `/Users/agedvagabond/Developer/exchange-hours-rs/AGENTS.md` @ 687e562
- `/Users/agedvagabond/Developer/exchange-hours-rs/docs/plans/2026-09-05-cme-trade-type-handoff.md`
- `/Users/agedvagabond/Developer/exchange-hours-rs/docs/plans/2026-09-05-cme-globex-family-coverage.md`
- repository surface at `main` @ 687e562: `git show 91c3119`, `git show 8673557`,
  `src/calendar/futures_profile.rs`, `src/calendar/futures_profile/profiles.rs`,
  `src/calendar/schedules/timeline.rs`, `src/calendar/schedules/futures/us/mini_grains.rs`,
  `src/calendar/schedules/futures/international/ice_abu_dhabi.rs`,
  `src/calendar/query/identity.rs`, `tests/schedule_documentation/mod.rs`,
  `tests/venue_sessions/named_profiles.rs`, `tests/unsupported_market_hours_keys.rs`,
  `tests/golden_grids.rs`, `tests/futures_family_boundaries/`,
  `docs/schedules/verification.md`, `docs/schedules/sources.md`,
  `docs/schedules/unsupported-families.md`, `docs/schedules/audit-2026-08-22.md`, `README.md`

## Outputs

- `/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/PLAN-58-trade-type-keys.md`
- `/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/PLAN-58.json`

No file inside `/Users/agedvagabond/Developer/exchange-hours-rs` was modified.
