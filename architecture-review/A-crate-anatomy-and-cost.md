<!-- SPDX-License-Identifier: MIT-0 -->

# A — Crate anatomy and cost model

Facts gathered 2026-09-12 (UTC) for the architectural review of
`/Users/agedvagabond/Developer/exchange-hours-rs`. **No file in
`exchange-hours-rs` or `SharurPlatform` was modified**; both working trees were
read-only throughout.

**Measurement baseline.** `exchange-hours-rs` was checked out on branch
`trade-type-metals-tas` @ `5530f22` ("Add the five metals TAS keys"), which is
`origin/main` @ `b8aedcd` plus 5 commits. That branch **is** PR #83 — the second
PR of the 32-key trade-type plan — so every number below already includes the
five metals TAS keys. Where a figure differs on `main` it is called out. Working
tree clean.

---

## 1. Public API inventory

The crate root re-exports one module (`src/lib.rs:154` `mod calendar;` →
`pub use calendar::*;`). `src/calendar/mod.rs:62-103` is the complete export
list. `src/lib.rs` is 156 lines, of which **149 are the crate-level doc comment**
(4 of those lines are the doctested quick-start example).

### 1.1 Types (21 exported)

| Item | Defined at | The question it answers | Used by SharurPlatform? |
|---|---|---|---|
| `Exchange` | `src/calendar/exchange/mod.rs:13` (`exchanges!` table) | *Which venue?* — 96 `#[non_exhaustive]` variants with stable `snake_case` wire names | **yes** (25 distinct variants in `crates/*/src`) |
| `ParseExchangeError` | `src/calendar/exchange/name.rs:48` | `FromStr` rejection of an unknown venue name | **yes** (1 site) |
| `MarketHoursKey` | `src/calendar/futures_profile.rs:114` (`market_hours_keys!` table) | *Which product family?* — 36 variants | **yes** (8 distinct variants) |
| `ParseMarketHoursKeyError` | `src/calendar/futures_profile/key_serde.rs:116` | `FromStr` rejection of an unknown key name | no |
| `FuturesSessionProfile` | `src/calendar/futures_profile.rs:54` | The fixed current normal-week table for a key (`tz`, `regular`, `extended`, `order_entry`, `has_daily_close`, `has_weekend_close`) | no |
| `MarketHours` | `src/calendar/hours.rs:39` | A **detached fixed snapshot** — same six fields plus a `CalendarSource` tag; the pre-calendar API | no |
| `ExchangeCalendar` | `src/calendar/exchange_calendar/mod.rs:62` | *The date-aware calendar* — `Copy + Send + Sync + 'static`, reselects the profile in force at each queried instant | **yes** (the only calendar the consumer holds) |
| `CalendarSource` | `src/calendar/exchange_calendar/mod.rs:29` | Which identity a calendar/snapshot carries (`Exchange(..)` or `MarketHoursKey(..)`) | **yes** |
| `SessionRule` | `src/calendar/rule.rs:63` | One weekday mask + `open_ssm`/`close_ssm` slice | no |
| `SessionRuleError` | `src/calendar/rule.rs:136` | Why a hand-built `SessionRule` is invalid | no |
| `SessionKind` | `src/calendar/rule.rs:172` | `Regular` / `Extended` / `Both` selector on every query | **yes** (6 sites; the market-clock UI and `is_closed_all_day_at`) |
| `SessionState` | `src/calendar/state.rs:8` | The one mutually-exclusive classification: `OpenRegular`, `OpenExtended`, `OrderEntry`, `Halt`, `Maintenance`, `Closed` | **yes** (mapped 1:1 into `chart::session::SessionState`) |
| `CalendarResolution` | `src/calendar/resolution.rs:23` | Bar size for `candle_start`/`candle_end` | **yes** (9 sites) |
| `DayPolicy` | `src/calendar/policy.rs:37` | Caller-owned trade-date overlay trait (closed / early close / late open) | **yes** (held as `Option<Arc<dyn DayPolicy>>`) |
| `NoPolicy` | `src/calendar/policy.rs:64` | The empty overlay | no |
| `PolicyCalendar<'a>` | `src/calendar/policy.rs:105` | The borrowed overlay-applied query surface | **yes** (1 site) |
| `DayOverride` | `src/calendar/policy/static_policy.rs:24` | One validated hard-coded day override record | no |
| `StaticDayPolicy<'a>` | `src/calendar/policy/static_policy.rs:159` | A const-validated table of those records | no |
| `StaticDayPolicyError` | `src/calendar/policy/static_policy.rs:252` | Why such a table is invalid | no |
| `ExceptionBlock` / `ExceptionBlockKind` | `src/calendar/exceptions.rs:68` / `:44` | One phase of a **replacement** trading day | no |
| `DateException<'a>`, `ExceptionCoverage`, `ExceptionScopeError`, `SessionExceptionRecord<'a>`, `SessionExceptionSource`, `StaticSessionExceptions<'a>`, `StaticSessionExceptionsError` | `src/calendar/exceptions.rs:167,183,247,223` and `exceptions/static_table.rs:20,133,322` | The whole replacement-trade-date layer: provider trait, record format, coverage window, scope error | **no — zero references anywhere in SharurPlatform** |

### 1.2 Free functions (26 exported)

| Group | Items | Question answered | Consumer? |
|---|---|---|---|
| Venue selection | `hours_for_exchange` (`presets/historical.rs:42`) | venue + instant → fixed snapshot | no |
| Calendar constructors | `calendar_for_exchange` (`exchange_calendar/mod.rs:318`), `calendar_for_market_hours_key` (`:328`) | identity → date-aware calendar | **yes, both** |
| Key selection | `session_profile` (`futures_profile/profiles.rs:383`), `hours_for_market_hours_key` (`futures_profile.rs:448`) | key → static-current table / key + instant → snapshot | `hours_for_market_hours_key` **yes**; `session_profile` no |
| Fixed-snapshot adapters | `session_bounds`, `session_bounds_with`, `next_session_after`, `next_session_after_with`, `next_session_open_after` (`session.rs:27-73`); `candle_start`, `candle_start_with`, `candle_end`, `candle_end_with`, `time_end_of_day` (`candle.rs:44-97`) | bounds / bar edges over a detached `MarketHours` | **none** — the consumer uses the identical methods on `ExchangeCalendar` |
| Bulk builders | `hours_for_all`, `hours_for_us_equities`, `hours_for_eu_equities`, `hours_for_apac_equities`, `hours_for_global_equities`, `hours_map_for`, `hours_map_us_equities`, `hours_map_eu_equities`, `hours_map_apac_equities`, `hours_map_global_equities` (`bulk.rs:100-190`) | a region's venues in one call | **none of the ten** |

### 1.3 Methods

`ExchangeCalendar` exposes **31** public methods (`exchange_calendar/mod.rs`,
`exchange_calendar/candles.rs`, `exchange_calendar/week.rs`).
`PolicyCalendar` mirrors **34** (`policy.rs`, `policy/candles.rs`,
`policy/week.rs`) — the same surface plus `with_day_policy`,
`with_session_exceptions`, `session_exception_on`, `has_day_policy`,
`has_session_exceptions`, `calendar`. `MarketHours` exposes 18.
Counting every `pub fn`/`pub const fn`: **133 public methods** across the crate.

### 1.4 Exercised by the test suite only

Measured by grepping all of `SharurPlatform/crates/**/*.rs` (the only consumer
found — `Sharur`, `NautilusResearch` and `globex-reference-catalog` contain zero
references to `exchange_hours`):

* the entire **session-exception layer** — 9 exported items, `264 + 443 = 707`
  lines of `src/calendar/exceptions.rs` + `exceptions/static_table.rs`, plus
  `src/calendar/query/replacement.rs` (254 lines) and
  **`tests/session_exceptions.rs` (1,147 lines, 29 tests — the single largest
  test file in the repo)**. Zero consumer references.
* the entire **`StaticDayPolicy` record format** — `DayOverride`,
  `StaticDayPolicy`, `StaticDayPolicyError`, `policy/static_policy.rs`
  (301 lines), `tests/static_day_policy.rs` (193 lines, 7 tests). The consumer
  implements `DayPolicy` itself (`Option<Arc<dyn DayPolicy>>`) and never uses
  the static table.
* all **10 bulk builders** (`bulk.rs`, 192 lines) — used only by
  `tests/global_equities/`, `tests/apac_equities/` and `tests/surface_agreement.rs`.
* all **10 fixed-snapshot free functions** and `MarketHours` itself — the
  consumer's entire calendar path is `ExchangeCalendar`/`PolicyCalendar`
  methods. `tests/surface_agreement.rs` (161 lines, 4 tests) exists purely to
  assert the two surfaces agree.
* `session_profile`, `FuturesSessionProfile`, `SessionRule`, `SessionRuleError`,
  `NoPolicy`, `ParseMarketHoursKeyError`.

**Roughly half the exported surface has exactly one consumer: this crate's own
test suite.**

---

## 2. The data model

### 2.1 How the pieces relate

```
Exchange (96)  ─┐                      ┌─ CalendarSource::Exchange(Exchange)
                ├─→ CalendarSource ────┤
MarketHoursKey ─┘                      └─ CalendarSource::MarketHoursKey(key)
     (36)

ExchangeCalendar { source: CalendarSource }        ← Copy, 'static, date-aware
    │  .hours_at(instant)
    ▼
hours_for_exchange(exch, as_of)            hours_for_market_hours_key(key, as_of)
    │ match in presets/historical.rs           │ match in futures_profile.rs:448
    │ (no catch-all arm)                       │ (no catch-all arm)
    ▼                                          ▼
  <venue>_profile_at(as_of)  ────────────►  select_revision(day, BASELINE, REVISIONS)
                                                  │ partition_point over an
                                                  │ ascending &'static [Revision]
                                                  ▼
                                          &'static StaticHoursProfile
                                                  │ from_profile(source, profile)
                                                  ▼
                                          MarketHours { source, tz,
                                                        regular/extended/order_entry:
                                                        Cow::Borrowed(&'static [SessionRule]),
                                                        has_daily_close, has_weekend_close }
```

`Exchange` and `MarketHoursKey` are **parallel, not nested**: they are two
alternatives inside one `CalendarSource` enum
(`src/calendar/exchange_calendar/mod.rs:29`). A key is not "a product on a
venue" in the type system; it is a *separate identity* that happens to route to a
module under `schedules/futures/`. Venue-keyed compatibility defaults exist
(CME → `GlobexEquityIndex`, CBOT → `GlobexGrains`) but are documented as
approximations. `AGENTS.md` forbids any in-crate symbol→key mapper: the caller's
catalog must select the exact family.

`StaticHoursProfile` (`schedules/profile.rs`, `pub(crate)`) and
`FuturesSessionProfile` (`futures_profile.rs:54`, `pub`) are the same six fields;
`from_profile` converts one to `MarketHours` and `to_market_hours` converts the
other. **There are three near-identical profile shapes in the crate** — the
internal static one, the public futures one, and `MarketHours` — differing only
in ownership (`&'static [..]` vs `Cow<'static, [..]>`) and whether they carry an
identity tag.

### 2.2 How history is represented

`src/calendar/schedules/timeline.rs` (167 lines) is the whole mechanism:

* `Revision { effective: NaiveDate, profile: &'static StaticHoursProfile, source: SourceRef }`
* `revisions![ (y, m, d, &PROFILE, "citation"), … ]` — a macro that builds a
  `&'static [Revision]` and **fails the build** unless dates are strictly
  ascending (`assert_ascending`) and every row carries a non-empty citation
  label (`assert_cited`). Both are `const fn` run in const-eval.
* `select_revision(day, baseline, revisions)` — `partition_point`; a date before
  the first row returns `baseline`.
* `reference_delta_seconds(as_of, venue_tz, reference_tz)` — the cross-zone /
  seasonal primitive, used at venue-local noon.

History is therefore **a flat per-selector array of (date, profile) pairs with a
short citation string**; the full quotation and URL live in the comment beside
the table, not in the type. There is no era identity, no supersession record, no
"withheld window" type, and no machine-readable link from a row to the document
that dates it. Everything a reviewer needs to audit a row is prose.

### 2.3 Trade dates and session identity

`src/calendar/query/identity.rs` (116 lines) is the entire identity-dependent
topology, and it is a **hard-coded match on three sourced exceptions**:

* `joins_adjacent_same_kind` (line 18) — true only for
  `GlobexCryptocurrency | GlobexEventContractsBtc`; joins storage-only rule
  pieces so a 24/7 week reads as one block.
* `assign_normal` (line 36) — default trade date is the venue-local date of the
  session's **final close**, with three exceptions:
  1. `Exchange::SetThailand` — an after-midnight DR night phase opening before
     03:00 belongs to the *prior* local date (line 46).
  2. `MarketHoursKey::GlobexRoughRice` — an evening leg opening at/after 19:00
     belongs to the *following* local date, sourced to CBOT Submission 18-001's
     own "for trade date Monday" (lines 52-70).
  3. `GlobexCryptocurrency | GlobexEventContractsBtc` — weekend blocks carry the
     following open **business** date, walking forward past caller-closed dates
     with a 14-day lookahead (`TRADE_DATE_LOOKAHEAD_DAYS`, lines 72-105).

`src/calendar/query/status.rs` (162 lines) computes `session_state` in a fixed
precedence: `OpenRegular` → `OpenExtended` → `OrderEntry` → gap classification.
The gap classification uses `MAX_MAINTENANCE_GAP = 4 hours` and the ISO-week
test: same trade date → `Halt`; different trade date, ≤4h, same ISO week →
`Maintenance`; otherwise `Closed`. `trade_date` resolves an order-entry instant
*through the next session* so a Sunday pre-open reports Monday.

The 4-hour constant and the ISO-week rule are **crate policy, not exchange
facts**, and they are the single load-bearing heuristic in the query engine.

### 2.4 `regular` vs `extended` vs `order_entry`, operationally

From `AGENTS.md` "Modeling conventions" and `state.rs`:

| Phase | Trade can print? | Orders accepted? | Encoding rule |
|---|---|---|---|
| `regular` | yes | yes | the venue's primary/core continuous session, or a derivatives operator's explicitly published **RTH** |
| `extended` | yes | yes | electronic/overnight outside RTH, auction calls, post-close / trade-at-last |
| `order_entry` | **no** | yes | pre-open queues and post-close order windows in which nothing matches |

`is_open` = regular ∪ extended. `is_accepting_orders` = open ∪ order_entry.
`is_order_entry_only` = accepting ∧ ¬open.

**Which consumers actually care.** Three call sites in SharurPlatform, all
downstream of `SessionState`:

* `crates/chart/src/indicators/portable/inputs.rs:230` — `opens.regular` fires
  on the `OpenRegular` transition. This is the **only** place the
  regular/extended distinction changes a computed number (RTH-anchored
  indicators).
* `crates/ui/src/market_clock/{markets,color,paint,timeline}.rs` — RTH vs ETH
  labels and two colour bands in the world-clock widget.
* `crates/chart/src/session.rs:98` — bar emission is gated on
  `OpenRegular | OpenExtended`; `OrderEntry` deliberately emits **no bar**
  (there is no price). This is the one place `order_entry` earns its existence.

Notably, `regular: &[]` is the correct answer for **13 of the 36
`FuturesSessionProfile` statics** today — `globex_energy`,
`globex_interest_rates`, `globex_fx`, `globex_cryptocurrency`,
`globex_weather`, `globex_spot_quoted`, `globex_event_contracts`,
`globex_event_contracts_btc`, and all five metals TAS keys — and the trade-type
plan states `regular: &[]` for **all 32** proposed keys (PLAN-58 §2
conventions, resolved by research gate U-4). On the futures side the
regular/extended split is already absent from more than a third of the keys and
would be absent from 45 of 68 after the plan; it does most of its real work on
cash equities.

---

## 3. Size and shape

### 3.1 Lines of code

| Area | Files | Lines |
|---|---:|---:|
| `src/` total | 127 | **23,962** |
| — `src/calendar/schedules/**` (the data) | 93 | **17,369** (72.5% of `src`) |
| — everything else (`query`, `policy`, `exceptions`, values, engine) | 34 | 6,593 |
| `tests/` total | 87 | **19,857** |
| `benches/` | 1 | 42 |
| `README.md` | | 747 |
| `AGENTS.md` | | 488 |
| `CHANGELOG.md` | | 1,713 (**1,232 of them under `[Unreleased]`** since 1.0.0 on 2026-08-22) |
| `docs/schedules/*.md` | 6 | 1,610 |
| `docs/plans/*.md` | 4 | 1,164 |
| `tests/golden/normal_week_grids.txt` | | 716 |

Inside `src/calendar/schedules/**`: **6,288 comment lines (36.2%)**, 10,078 code
lines, 1,003 blank, and **1,224 URLs** (215 of them `web.archive.org`). The
newest modules invert the ratio — `event_contracts.rs` is 83% comment,
`spot_quoted.rs` 82%, `weather.rs` 76%, `sgx_equity_index/history.rs` 73%.

Largest 20 source modules (all ≥286 lines) are listed in §5. Eleven files are
≥400 lines against the 500-line ceiling:

```
488  src/calendar/futures_profile.rs          ← 12 lines of headroom
454  schedules/futures/international/sgx_equity_index/history.rs
448  schedules/futures/us/mini_grains.rs
443  src/calendar/exceptions/static_table.rs
425  schedules/futures/international/sgx_equity_index.rs
422  src/calendar/futures_profile/profiles.rs
421  schedules/futures/international/sgx_equity_index_more.rs
418  schedules/futures/us/metals_tas.rs
415  schedules/equities/us/cboe.rs
408  src/calendar/policy.rs
406  src/calendar/query/schedule.rs
```

### 3.2 Tests

`cargo nextest list` → **549 tests** in 17 binaries, plus 3 doctests
(`cargo test --doc`). On `origin/main` (before the metals TAS branch) the count
is 544.

| Suite | Tests |
|---|---:|
| `venue_sessions` | 245 |
| `futures_family_boundaries` | 94 |
| `session_exceptions` | 29 |
| `apac_equities` | 26 |
| `seasonal_calendars` | 25 |
| `schedule_documentation` | **25** |
| `global_equities` | 22 |
| `calendar_policies` | 19 |
| `session_invariants` | 17 |
| `rule_validation` | 17 |
| `static_day_policy` | 7 |
| `no_session_contract` | 7 |
| `order_entry_phase` | 6 |
| `surface_agreement` | 4 |
| `unsupported_market_hours_keys` | 3 |
| `calendar_value_traits` | 2 |
| `golden_grids` | 1 |

### 3.3 Identity and revision counts

| Quantity | Count |
|---|---:|
| `Exchange` variants | **96** (95 real + `Unknown`) |
| `MarketHoursKey` variants | **36** (35 real + `AlwaysOpen`) — the task brief's "~33" is one PR out of date |
| Verification-ledger rows | **132** = 96 + 36 |
| `revisions!` timelines | **106** |
| Revision rows, total | **279** |
| — owned by `MarketHoursKey` modules (`schedules/futures/`) | **130** |
| — owned by `Exchange` modules (`schedules/equities/`) | **149** |
| Revision rows per key (mean over 35 real keys) | **3.7** |
| Keys with 0 revision rows | 1 (`eurex` — its history is a seasonal selector, not a timeline) |
| Largest single timeline | `pse.rs` REVISIONS = 10; largest key timeline: `globex_cryptocurrency` = 9, `globex_event_contracts_btc` = 9 |

Revision rows per key (module-owned; keys that share a module share its rows):

```
9  globex_cryptocurrency · globex_event_contracts_btc
8  cfe_vix
7  globex_mini_grains · globex_rough_rice
6  globex_grains
5  globex_equity_index · sgx_equity_index_japan · sgx_equity_index_singapore
4  globex_livestock · globex_nikkei_225_dollar · ice_us_sugar · sgx_equity_index_china
3  globex_interest_rates · globex_gold_tas · globex_silver_tas · globex_copper_tas
   · sgx_equity_index_ntr_usd
2  globex_energy · globex_fx · ice_us · ice_us_coffee · ice_us_cocoa · ice_us_cotton
   · eurex_fixed_income (+2 winter) · sgx_equity_index_taiwan · globex_weather
1  ice_us_orange_juice · ice_us_dollar_index · globex_spot_quoted
   · globex_event_contracts · globex_platinum_tas · globex_palladium_tas · sgx
0  eurex
```

### 3.4 Cross-zone and seasonal selectors

`reference_delta_seconds` (`schedules/timeline.rs:163`) has **6 call sites** —
the complete set of non-timeline selectors in the crate:

| Module | Line | Kind | Identity |
|---|---:|---|---|
| `schedules/futures/international/europe.rs` | 120 | self-DST (Berlin vs UTC) | `MarketHoursKey::Eurex` |
| `schedules/futures/international/eurex_fixed_income.rs` | 287 | self-DST + 2 winter revision timelines | `MarketHoursKey::EurexFixedIncome` |
| `schedules/futures/international/ice_endex.rs` | 150 | cross-zone (Amsterdam vs New York) | `Exchange::IceEndex` |
| `schedules/futures/international/ice_abu_dhabi.rs` | 103 | cross-zone (Dubai vs New York) | `Exchange::IceAbuDhabi` |
| `schedules/equities/americas/b3.rs` | 201 | cross-zone (São Paulo vs New York) | `Exchange::B3` |
| `schedules/equities/americas/bmv.rs` | 235 | cross-zone (Mexico City vs New York) | `Exchange::Bmv` |

So **2 of 36 keys** and **4 of 96 exchanges** use a seasonal/cross-zone
selector today. PLAN-58 §0 identifies **12 more shapes** that need one (PRs 11,
12, 13 — energy TAM, metals TAM, TOPIX/Nikkei/FX BTIC), gated on maintainer
decision **D-1**.

`tests/seasonal_calendars/` (846 lines, 25 tests) covers these 6 selectors.

### 3.5 The documentation-fence tests

All 25 live in `tests/schedule_documentation/` (1,373 lines across 4 files) and
are integration tests that `include_str!` the repo's own Markdown
(`README.md`, `verification.md`, `sources.md`, `updating.md`,
`audit-2026-08-22.md`, `date-exceptions.md`, `unsupported-families.md`,
`databento-venues.md`) and assert prose against derived counts.

| # | Test | Prose it derives / guards |
|---|---|---|
| 1 | `verification_ledger_has_every_exchange_once_and_in_order` | ledger `Exchange` rows == `EXPECTED_EXCHANGE_NAMES`, same order |
| 2 | `verification_ledger_has_every_market_hours_key_once_and_in_order` | ledger key rows == `EXPECTED_MARKET_HOURS_KEY_NAMES` (a hand-written `[&str; 36]`), same order |
| 3 | `market_hours_key_selection_contract_is_explicit` | README/ledger state that the crate maps no symbols to keys |
| 4 | `exchange_rows_have_complete_review_metadata` | every exchange row has 6 cells, a valid Basis, an ISO `Reviewed on` |
| 5 | `market_hours_key_rows_have_complete_review_metadata` | same for key rows |
| 6 | `every_market_hours_key_owner_and_source_link_resolves` | each key row's owner module path and source-set anchor exist on disk |
| 7 | `readme_and_review_dates_match_the_repository_cutoff` | README "**Repository-wide review completed:** \`YYYY-MM-DD\`" == the ledger cutoff == the **oldest** non-synthetic exchange review date |
| 8 | `readme_test_inventory_counts_match_the_ledger` | README "keep all *N* `Exchange` rows (*N−1* non-synthetic plus `Unknown`) and *M* `MarketHoursKey` rows (*M−1* operator-derived plus `AlwaysOpen`) in canonical order" |
| 9 | `readme_and_audit_quantify_assurance_from_the_ledger` | README "**N source-backed market identities**", "(96 `Exchange` variants total)", "36 variants—35 operator-derived…", plus "Hours verified against the exchange at the review date: `X of Y`" and "Full dated history back to January 2010: `P of Y`" in README **and** the dated audit |
| 10 | `every_ledger_source_link_has_a_registry_anchor` | every `sources.md#anchor` cited in the ledger exists |
| 11 | `every_exchange_owner_link_resolves` | every owner-module link in an exchange row exists |
| 12 | `conditional_future_revisions_remain_unencoded_pending_confirmation` | the update-guide watch list still names the conditional future changes |
| 13 | `date_exception_contract_distinguishes_boundaries_coverage_and_finality` | README links `date-exceptions.md`; the update guide routes special days there |
| 14 | **`the_gap_kind_split_is_quoted_consistently_everywhere`** | counts `"Gap: order-entry"` and `"Gap: executable"` in the ledger and asserts **six** restatements: README "the split is **35 order-entry to 22 executable** across the 57 rows in the ledger.", ledger "Of the 57, **35 are order-entry**", ledger "**22 are executable**", README "The executable twenty-two —", ledger "The executable twenty-two are", ledger "None of the twenty-two serves", and the audit's "twenty-nine product-family keys are **Partial**" |
| 15 | `assurance_prose_restates_exchange_counts_from_the_ledger` | every *running-prose* restatement of the exchange basis counts in README and audit |
| 16 | `every_real_source_set_has_two_clickable_monitoring_channels` | each of the 56 `sources.md` source sets carries 2 clickable channels |
| 17 | `every_source_set_is_referenced_by_a_ledger_row` | no orphan source set |
| 18 | `supplied_venue_inventory_maps_every_distinct_label_to_a_real_exchange` | `databento-venues.md` labels → real `Exchange` values |
| 19 | `supplied_venue_inventory_has_expected_family_counts_and_unique_identities` | that file's per-family counts, **including each venue's ledger Basis snapshot** |
| 20 | `ledger_covers_every_market_hours_key_variant` | ties the hand-written `EXPECTED_MARKET_HOURS_KEY_NAMES` to `MarketHoursKey::ALL` (added in PR #78 — the suite did not import `MarketHoursKey` at all before) |
| 21 | `handoff_keys_are_registered_or_rejected` | every `globex_*` name proposed in `docs/plans/2026-09-05-cme-trade-type-handoff.md` is shipped, rejected in `unsupported-families.md`, or scheduled in the in-repo plan |
| 22 | `rejected_handoff_roots_are_named_in_the_register` | the roots of the 3 rejected handoff rows appear in the register |
| 23 | `cme_source_set_prose_counts_match_the_ledger` | `sources.md` `US-CME-GROUP` Status "All nineteen …" / "Eighteen of the nineteen are Partial" |
| 24 | `every_executable_gap_row_is_named_in_the_prose` | every `Gap: executable` row is named in README's and the ledger's enumerations, by wire name or a declared collective phrase whose spelled-out count matches |
| 25 | `golden_header_identity_counts_match_the_ledger` | `tests/golden_grids.rs`'s header "all 96 exchanges and all 36 keys at once" |

Five of these (7, 8, 9, 14, 15, 23, 24, 25) exist **because prose silently
drifted**. The source comments say so explicitly:

* `mod.rs:331` — the README test-inventory sentence "lagged the public surface by
  two key additions before anyone noticed."
* `mod.rs:557` — "README.md once said 'Four key rows are Primary' while the
  ledger held five, and the headline bullet said '11 operator-derived' long after
  the count reached 24."
* `mod.rs:596` — "it happened on two consecutive product-family additions before
  this fence existed."
* `mod.rs:704` — "Adding two venues on 2026-09-09 updated every headline yet left
  four restatements at 26, one at 93, and the audit's 'Twenty-six' behind while
  the tests stayed green."

There is a helper, `number_words(n)` (`mod.rs:675`), whose sole purpose is to
spell counts the way the prose spells them, with `assert!(n < 100, "extend the
number words past {n}")`. PR #78's own result note records that the two *local*
word lists it replaced "would have panicked on PR 2" (25-entry list) and
"silently produced 'Six key rows are **Primary** and 24 are **Partial**'"
(20-entry list).

### 3.6 The 500-line / 100-line limits and splits caused by them

* **500 lines**, `AGENTS.md` "Structural rules": "Production source files stay
  cohesive and reviewable, ordinarily at or below 500 lines… Test files are
  exempt."
* **100 lines per function** is not written in `AGENTS.md`; it is
  `clippy::too_many_lines` under `pedantic = warn` + CI `-D warnings`
  (`Cargo.toml` `[lints.clippy]`).

Modules whose doc comment names the ceiling as the *only* reason for the split:

| Module | Lines | Split from | Stated reason |
|---|---:|---|---|
| `schedules/futures/international/sgx_equity_index_more.rs` | 421 | `sgx_equity_index.rs` | "Split out **only** to keep each production file within the source-reviewability ceiling." |
| `schedules/futures/international/sgx_equity_index/eras.rs` | 232 | ditto | "this file holds the tables so that module stays readable." |
| `schedules/futures/international/sgx_equity_index/history.rs` | 454 | ditto | holds "the published evidence behind every row" |
| `schedules/futures/us/pgm_tas.rs` | 224 | `metals_tas.rs` | PLAN-58 PR 2: "Two modules because the citation blocks are long and `mini_grains.rs` reached 448 lines for one key with seven revisions." |
| `schedules/equities/us/options/history.rs` | 263 | `options.rs` | selectors split from tables |
| `schedules/equities/us/history.rs` | 188 | `equities.rs` | selectors split from tables |
| `futures_profile/profiles.rs` | 422 | `futures_profile.rs` | fixed-current statics split from the identity table |
| `exceptions/static_table.rs` | 443 | `exceptions.rs` | record format split from the trait |
| `policy/static_policy.rs`, `policy/candles.rs`, `policy/week.rs` | 301/67/19 | `policy.rs` | surface split |
| `exchange_calendar/candles.rs`, `exchange_calendar/week.rs` | 68/55 | `exchange_calendar/mod.rs` | surface split |

Test-side splits for the **100-line function** limit:

* `tests/schedule_documentation/mod.rs:552` — "Split out of
  `readme_and_audit_quantify_assurance_from_the_ledger` to keep that test inside
  the crate's 100-line function limit."
* `tests/seasonal_calendars/chrono_edges.rs:198` — "The surfaces are split into
  helpers to stay inside the 100-line limit."

**One number matters more than the rest: `src/calendar/futures_profile.rs` is at
488 of 500 lines.** The metals TAS branch added `+75/−5` there for 5 keys —
**14 net lines per key** (a variant doc block, a `session_profile` arm and a
`hours_for_market_hours_key` arm). PR 3 of the plan adds 2 keys, ≈28 lines: the
guard is breached by the very next PR in the sequence. Nothing in the plan
allocates a split for it; PR2-result.md only notes it landed "inside the
500-line guard".

---

## 4. The governance

### 4.1 Named laws (9)

| Law | `AGENTS.md` line | One-line statement | Per-key / per-row cost it imposes |
|---|---:|---|---|
| **LAW-DETERMINISM** | 10 | No clock, no I/O, no randomness; `chrono` built without `clock` so `Utc::now()` does not compile | One-off structural cost; `clippy.toml` `disallowed-methods` list must be maintained. ~Zero per key. |
| **LAW-PANIC** | 14 | Public queries are total: no panic, hang, or unreachable | `unwrap/expect/panic/todo/unreachable` denied crate-wide; every const-eval assert needs an `#[expect(..., reason=...)]`. ~Zero per key. |
| **LAW-PRIMARY-SOURCES** | 23 | Every session time is backed by an exchange/rulebook/regulator source **cited in a comment next to the table**; a coinciding venue still gets its own named profile | **The dominant per-key cost.** 36.2% of `schedules/**` is comment; 1,224 URLs. Newest key modules run 63–83% comment. Forbids deduplicating modules that currently agree. |
| **LAW-PUBLIC-SOURCES** | 30 | Every cited source must be reachable without authentication | Kills whole channels (SGX member portal; see `sgx-pre2020/2026-09-06-rulebook-channel-ruled-out.md`). Forces archive replay. |
| **LAW-NO-FABRICATED-DATES** | 36 | A cutover exists only on an **unconditional, day-level** stated effective date; otherwise a documented gap. Rows key to the local **opening day**; a day-level boundary never splits a running session; history back to **January 2010** | Per row: find a dated primary, then decide the *opening day* (a wrapping evening grid keys to the preceding Sunday). PLAN-58 §0 records **5 of 5** TAM launch rows in the research gate were **one day wrong** on exactly this. |
| **LAW-UTC-DATES** | 51 | Every date the repo records about its own work is the UTC date of that work | Per row: the ledger `Reviewed on` must come from `date -u`. PR2-result.md item 8 records that the maintainer's machine "runs ten hours ahead of UTC". |
| **LAW-SESSION-NOT-EXPIRY** | 61 | Termination of trading / expiry / settlement / fixing is never a session boundary; a close enters a profile only in **session language** | Per shape: read every candidate close and classify the *language*. This law exists because the alternative reading "would have produced six product families where the operator publishes one" (line 83) — the event-contracts near-miss. |
| **LAW-HOLIDAY-SCOPE** | 90 | A single-trade-date (or bounded run) change is a holiday, owned by the caller's `DayPolicy`, never a profile/revision edit | Per finding: classify every dated change as schedule-vs-holiday before encoding. |
| **LAW-FOLLOW-UPS-ARE-ISSUES** | 102 | Any follow-up named anywhere is done in that change or **opened as a GitHub issue before the change merges**, with the number cited | Measured: PR #78 opened **5** issues (#73–#77); PR #83 opened **4** (#79–#82). **9 issues for 5 keys + one fence PR.** The repo has 29 issues against 54 PRs. |

### 4.2 Named modeling conventions (14, `AGENTS.md` 117-278)

Each is a rule a contributor must apply per key or per row:

1. **UTC in, UTC out** — no local time crosses the public boundary.
2. **Closes are end-exclusive.**
3. **`open_ssm >= close_ssm` wraps**; equal endpoints = one full local day.
4. **DST bias is asymmetric**: opens earliest, closes latest. "Never simplify."
5. **Regular vs extended** — RTH only when the operator publishes RTH; auction
   calls / pre-open / post-close always `extended` or `order_entry`.
6. **Cash-equity venue envelope** — the availability union of automated
   order-capable systems in the row's scope; excludes reporting/cancel-only.
7. **Product-neutral family selection** — no symbol→key mapper in-crate.
8. **Trade dates and state** — final-close date, the 4-hour maintenance bound,
   ISO-week rule; `is_maintenance` ≡ the maintenance case of `session_state`.
9. **Caller-owned day overrides** — holidays never touch a template; a closed
   date removes the prior-evening wrap except where the operator rolls it.
10. **Exchange-level boundaries, not per-security auction outcomes** — document
    the deterministic representation for randomized uncrosses.
11. **Below the January-2010 floor, the earliest sourced profile stands**
    (decided 2026-09-01). "Do not add a lower bound to the timelines."
12. **Carry the earliest sourced state back to the audit floor** — "absence is a
    claim too."
13. **Prefer the sourced intersection to omission** — serve what every sourced
    state supports; withhold the disputed remainder; record the conflict.
    Worked examples: CME Sunday Pre-Open 16:00–16:15; `ECBTC`'s disputed hour.
14. **A knowledge boundary is the first source that lists the modelled product**
    (SGX FTSE Taiwan) — *and* **may only widen** (SGX FTSE China A50); a row
    that lengthens or creates a wrapping overnight close keys to the following
    Monday.
15. **An operator's own dated change log is a primary source** — but only under
    a **four-part test** (operator-authored and issue-dated in the file; the
    effective day stated inside the same entry or a border-partitioned header
    row; session language; calibrated against a cutover already held from a
    circular). Admitting SGX's change log required checking that "every one of
    SGX's 195 bare effective days resolves… to within eleven weeks of its issue
    date, 193 in the issue year".
16. **"Unsourced" means "not worked up", never "no source exists"** — you may
    not write that nothing survives until the predecessor channels have been
    searched.
17. **Absence is `None`** — never fabricate a degenerate session.

Plus 8 **structural rules** (`AGENTS.md` 306-360): `#[non_exhaustive]` forever;
one generated table for each identity; one canonical `snake_case` name shared by
serde/`as_str`/`Display`/`FromStr`; the 500-line ceiling; `static` profile
tables; `Copy + Send + Sync + 'static` calendars; identity topology only on the
date-aware calendar; instant-only selection with no clock-less "current" router.

### 4.3 The per-key change set (`AGENTS.md` 362-430 + PLAN-58 §2)

`AGENTS.md` "Adding or revising a product-family key" is 6 numbered steps;
PLAN-58 expands it to a **13-item registration surface**, all of which
`AGENTS.md` forbids generating from `MarketHoursKey::ALL` ("These lists must
remain handwritten so they can catch production omissions"):

1. `market_hours_keys!` enum row + canonical name + variant doc
2. `hours_for_market_hours_key` arm (and cutover/boundary tests through
   `calendar_for_market_hours_key` on both sides of the opening day)
3. `session_profile` arm + a `FuturesSessionProfile` static in `profiles.rs`
4. `pub(crate) use` re-exports in `schedules/futures/us/mod.rs`
5. `EXPECTED_MARKET_HOURS_KEY_NAMES` (a `[&str; N]` — **the array length is
   part of the edit**) in `tests/schedule_documentation/mod.rs`
6. `EXPECTED_MARKET_HOURS_KEYS` in `tests/venue_sessions/named_profiles.rs`
7. `SUPPORTED_FAMILY_NAMES` in `tests/unsupported_market_hours_keys.rs`
8. the ledger row in `verification.md` — Basis, gap kind, `Reviewed on` ≥ cutoff,
   exactly 6 cells, **no `|` anywhere inside a cell**
9. `sources.md` — source set and its prose counts
10. `CHANGELOG.md` `[Unreleased]` / **Added**
11. README fenced counts **and** coverage/limitations prose. PR #83 changed
    **eight distinct README/audit counts** for five keys
12. regenerate `tests/golden/normal_week_grids.txt`; confirm no other key moved
13. a new submodule of `tests/futures_family_boundaries/`

Plus, per row: **mutation-check every cutover fence** (move the date one day,
confirm red, restore, and say so in the PR) — PR #83 did 11 of these.

### 4.4 Every "Trap" in `docs/plans/2026-09-05-cme-globex-family-coverage.md`

All 9 are in the "Traps already paid for" section at line 211:

1. **Envelope match is not family identity** — two products can share an
   electronic envelope and differ in RTH classification and history.
2. **Check the contract set, not just the grid** — a source only sources a
   family if that family appears in it (SGX FTSE Taiwan; identical hours hid it).
3. **A two-endpoint bracket assumes nothing happened between** — "that
   assumption was wrong three times this cycle (SGX twice, CME Nikkei once)."
4. **"Unsourced" means "not worked up"** — check retired operator sites in the
   archive first.
5. **Paper trails are not always clean** — the 2012-05-20 CBOT grain cutover was
   certified by Submission 12-144 for a superseded June date.
6. **Every one of these PRs touches the same ledger, so each merge breaks the
   next one's mergeability** — land one, rebase the rest; put a fence PR before
   the PRs it protects.
7. **Two PRs can move the counts along different axes** — #51 added a key row
   while #49 changed exchange rows; both internally right, both wrong once
   merged. Re-derive every tally from the merged ledger.
8. **`docs/schedules/databento-venues.md` snapshots each venue's ledger Basis**
   and a test asserts they agree — changing a Basis means changing that file.
9. **A non-wrapping evening leg needs a trade-date exception** in
   `src/calendar/query/identity.rs` (Rough Rice); a wrapping one does not.

---

## 5. Cost per key, measured

### 5.1 Per-key module cost (comment vs rule data)

`cmt` = comment lines, `code` = non-blank non-comment lines, `url` = URLs in the
file, `rows` = revision rows in the timelines the key uses. Keys sharing a
module share its figures.

| Key | Module | tot | cmt | code | cmt% | urls | rows | Basis | Gap | Added by |
|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| `globex_equity_index` | `futures/us/cme_group.rs` | 321 | 116 | 198 | 36% | 31 | 5 | Partial | order-entry | initial `a116b2a`; #19 #21 #22 #24 #25 |
| `globex_energy` | `futures/us/energy_metals.rs` | 181 | 85 | 88 | 47% | 27 | 2 | Partial | order-entry | initial; #19 #21 #22 #24 #25 |
| `globex_grains` | `futures/us/grains.rs` | 325 | 97 | 218 | 30% | 29 | 6 | Partial | order-entry | #19; #21 #22 #24 #25 #47 #51 |
| `globex_mini_grains` | `futures/us/mini_grains.rs` | 448 | 228 | 207 | 51% | 49 | 7 | Partial | order-entry | **#51 only** |
| `globex_fx` | `futures/us/fx.rs` | 178 | 79 | 91 | 44% | 26 | 2 | Partial | order-entry | #19; #21 #22 #24 #25 |
| `globex_interest_rates` | `futures/us/interest_rates.rs` | 234 | 90 | 133 | 38% | 28 | 3 | Partial | order-entry | #19; #21 #22 #24 #25 |
| `globex_livestock` | `futures/us/livestock.rs` | 217 | 58 | 143 | 27% | 14 | 4 | Partial | order-entry | #19; #21 #22 #24 #25 |
| `globex_cryptocurrency` | `futures/us/cryptocurrency.rs` | 246 | 58 | 172 | 24% | 14 | 9 | Partial | order-entry | #19; #21 #25 **#63** |
| `cfe_vix` | `futures/us/cfe.rs` | 329 | 91 | 224 | 28% | 22 | 8 | Primary | — | initial; #21 |
| `eurex` | `futures/international/europe.rs` | 165 | 44 | 111 | 27% | 12 | 0 (seasonal) | Primary | — | initial; #21 |
| `ice_us` | `futures/us/ice_us.rs` | 116 | 27 | 81 | 23% | 3 | 2 | Primary | — | initial; #19 #21 |
| `ice_us_sugar` | `futures/us/ice_sugar.rs` | 205 | 91 | 98 | 44% | 20 | 4 | Partial | **executable** | **#20**; #21 #25 #38 |
| `ice_us_coffee` | `futures/us/ice_coffee.rs` | 179 | 91 | 75 | 51% | 17 | 2 | Partial | **executable** | #20; #21 #25 #38 |
| `ice_us_cocoa` | `futures/us/ice_cocoa.rs` | 176 | 88 | 75 | 50% | 17 | 2 | Partial | **executable** | #20; #21 #25 #38 |
| `ice_us_cotton` | `futures/us/ice_cotton.rs` | 224 | 142 | 70 | 63% | 26 | 2 | Partial | **executable** | #20; #21 #25 #38 |
| `ice_us_orange_juice` | `futures/us/ice_fcoj.rs` | 161 | 98 | 53 | 61% | 19 | 1 | Partial | **executable** | #20; #21 #25 #38 |
| `ice_us_dollar_index` | `futures/us/ice_usdx.rs` | 192 | 113 | 69 | 59% | 17 | 1 | Partial | **executable** | #20; #21 #25 #38 |
| `globex_nikkei_225_dollar` | `futures/us/cme_nikkei.rs` | 247 | 136 | 95 | 55% | 20 | 4 | Partial | **executable** | #20; #21 #22 #25 **#39** #56 |
| `eurex_fixed_income` | `futures/international/eurex_fixed_income.rs` | 297 | 105 | 171 | 35% | 10 | 2+2 winter | Primary | — | #20; #21 |
| `sgx_equity_index_japan` | `futures/international/sgx_equity_index.rs` | 425 | 140 | 259 | 33% | 17 | 5 | Partial | **executable** | #20; #21 #25 **#44 #67 #68 #69** |
| `sgx_equity_index_china` | (same module) | — | — | — | — | — | 4 | Partial | **executable** | same |
| `sgx_equity_index_singapore` | (same module) | — | — | — | — | — | 5 | Partial | **executable** | same |
| `sgx_equity_index_taiwan` | `futures/international/sgx_equity_index_more.rs` | 421 | 162 | 238 | 38% | 29 | 2 | Partial | **executable** | same |
| `sgx_equity_index_ntr_usd` | (same module) | — | — | — | — | — | 3 | Partial | **executable** | same |
| (shared) | `sgx_equity_index/history.rs` | 454 | 333 | 114 | **73%** | 43 | — | — | — | #67 #68 #69 |
| (shared) | `sgx_equity_index/eras.rs` | 232 | 144 | 69 | 62% | 18 | — | — | — | #67 #69 |
| `globex_rough_rice` | `futures/us/rough_rice.rs` | 241 | 113 | 116 | 47% | 11 | 7 | Partial | order-entry | **#47 only** |
| `globex_weather` | `futures/us/weather.rs` | 350 | **267** | 71 | **76%** | 37 | 2 | Partial | **executable** | **#53 only** |
| `globex_spot_quoted` | `futures/us/spot_quoted.rs` | 283 | **231** | 42 | **82%** | 13 | 1 | **Primary** | — | **#54**; #55 |
| `globex_event_contracts` | `futures/us/event_contracts.rs` | 315 | **263** | 42 | **83%** | 12 | 1 | Partial | **executable** | **#55**; #59 #60 |
| `globex_event_contracts_btc` | `futures/us/bitcoin_event_contracts.rs` | 374 | 156 | 202 | 42% | 11 | 9 | Partial | **executable** | **#60 only** |
| `globex_gold_tas` | `futures/us/metals_tas.rs` | 418 | 265 | 137 | 63% | 45 | 3 | Partial | **executable** | **#83 (open)** |
| `globex_silver_tas` | (same module) | — | — | — | — | — | 3 | Partial | **executable** | #83 |
| `globex_copper_tas` | (same module) | — | — | — | — | — | 3 | Partial | **executable** | #83 |
| `globex_platinum_tas` | `futures/us/pgm_tas.rs` | 224 | 140 | 71 | 63% | 21 | 1 | Partial | **executable** | #83 |
| `globex_palladium_tas` | (same module) | — | — | — | — | — | 1 | Partial | **executable** | #83 |
| `sgx` | `futures/international/sgx.rs` | 93 | 21 | 64 | 23% | 4 | 1 | Primary | — | initial; #21 |
| `always_open` | (no module) | — | — | — | — | — | — | Synthetic | — | — |

**Ledger basis totals across all 132 rows: 73 Primary, 57 Partial, 2 Synthetic.**
For the 35 real keys: **6 Primary, 29 Partial**. The 57 Partial rows split
**35 order-entry / 22 executable** (the split the fence test derives).

**Citation prose has inflated ~9×.** Mean characters in a ledger row's Notes
cell:

| Row group | Rows | Total note chars | Mean |
|---|---:|---:|---:|
| 96 `Exchange` rows (mostly authored 2026-08-20…22) | 96 | 45,607 | **475** |
| 36 `MarketHoursKey` rows | 36 | 79,438 | **2,206** |
| the 14 newest key rows (weather, spot-quoted, event contracts ×2, the 5 SGX, the 5 TAS) | 14 | 57,760 | **4,125** |
| whole ledger | 132 | 125,045 | 947 |

Longest single ledger cells: `sgx_equity_index_japan` **6,029** chars,
`globex_gold_tas` 6,024, `globex_copper_tas` 5,668, `globex_event_contracts_btc`
4,962, `globex_event_contracts` 4,924.

### 5.2 Measured PR cost per key

| PR | Merged | Keys | Files | +ins | −del | Commits | Review events | Wall clock (open→merge) | Tests added |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| #20 "thirteen sourced product-family keys" | 2026-08-23 | 13 | — | — | — | — | — | — | — |
| #44 SGX 2025 cutover + Taiwan boundary | 2026-09-03 | 0 (fix) | 17 | 1,170 | 805 | 4 | 9 | 49 min | — |
| **#47 `GlobexRoughRice`** | 2026-09-05 | **1** | 22 | **794** | 58 | 2 | 5 | 1 h 38 m | 451→458 (+7) |
| **#51 `GlobexMiniGrains`** | 2026-09-05 | **1** | 18 | **1,314** | 32 | 3 | 0 | 25 min | 458→471 (+13) |
| **#53 `GlobexWeather`** | 2026-09-05 | **1** | 18 | **1,089** | 25 | 3 | 10 | 8 h 21 m | — |
| **#54 `GlobexSpotQuoted`** | 2026-09-05 | **1** | 17 | **885** | 30 | 2 | 5 | 40 min | — |
| **#55 `GlobexEventContracts`** | 2026-09-05 | **1** | 19 | **1,086** | 52 | 2 | 7 | 14 min | — |
| #56 land the handoff | 2026-09-06 | 0 | 4 | 323 | 5 | — | — | — | — |
| #59 add LAW-SESSION-NOT-EXPIRY | 2026-09-06 | 0 | 4 | 69 | 13 | — | — | — | — |
| **#60 `GlobexEventContractsBtc`** | 2026-09-06 | **1** | 22 | **949** | 117 | 4 | 3 | 26 min | 505→514 |
| #63 crypto Saturday extensions | 2026-09-06 | 0 (2 rows) | 5 | 142 | 43 | — | — | — | — |
| **#67 SGX pre-2020 eras** | 2026-09-06 | 0 (re-model 5) | 11 | **1,238** | 276 | 3 | 5 | 27 min | 514→522 |
| #68 SGX 2019 change-log dating | 2026-09-06 | 0 (2 rows) | 10 | 201 | 167 | 1 | 0 | 14 min | — |
| #69 SGX 2009 floor intersection | 2026-09-06 | 0 (re-key) | 10 | 739 | 190 | 3 | 9 | 55 min | — |
| #70 CDE + SMFE | 2026-09-11 | 0 (2 venues) | 22 | 677 | 47 | — | — | — | — |
| **#78 fences before the families** | 2026-09-12 | **0** | 7 | **831** | 65 | 4 | 11 | 1 h 05 m | +6 fence tests |
| **#83 five metals TAS keys** | open | **5** | 17 | **1,411** | 36 | 1 | 0 | — | 544→554 (+10) |

**Single-key PRs cost 794–1,314 insertions across 17–22 files.** Mean of the
five single-key CME PRs (#47, #51, #53, #54, #55): **1,034 insertions, 18.8
files**. The five-key PR #83 cost **1,411 insertions / 17 files = 282
insertions per key** — the only economy of scale observed, and it comes from
sharing one module and one test file across keys.

A single-key PR's insertions break down roughly as: **~250–450 lines of new
schedule module** (60–83% of it citation comment), **~320–650 lines of new test
module**, and **~100–150 lines of documentation churn** spread over
`CHANGELOG.md`, `README.md`, `verification.md`, `sources.md`,
`audit-2026-08-22.md`, the plan doc, the golden file, and 4–5 hand-written test
lists.

### 5.3 Case study — SGX pre-2020 (#45, #62, #64–#69, PRs #44/#67/#68/#69)

From `/Users/agedvagabond/Developer/exchange-hours-research/STATUS.md` and
`sgx-pre2020/`:

| Measure | Value |
|---|---|
| GitHub issues | **6** — #31 (opened 2026-08-31, closed 09-03), #45 (09-03 → 09-06), #62 (09-06, 1 h 36 m), #64, #65 (both 09-06, closed same day), #66 (**still open**) |
| PRs | **4** merged — #44, #67, #68, #69 (+ #25's SGX over-reporting fix) |
| Calendar span | research files 2026-08-28 → 2026-09-06; issue #31 opened 2026-08-31; last PR merged 2026-09-06 05:45Z. **10 calendar days end-to-end; 9 days from first issue.** |
| Distinct research workflows | **≥9** — `wf_13367f25-68a`, `wf_4b4e4f3d-898`, `wf_ef0dc8d0-674` (grids), `wf_a20bca25-bef` (alt sources), `wf_95f5a14f-739` (era tables), `wf_220107a5-7d7` (adversarial review), `wf_db3476fa-d54` (shared hunt/verify with ECBTC), `wf_02be92b0-530` (follow-ups 64/65/66), `wf_5034d90c-c8f` (PR #68 review) |
| Agent runs recorded in journals | **100** for SGX alone (38 + 22 + 16 + 12 + 6 + 6), of 126 across the whole store |
| Saved artifacts | **417 files, 101 MB** under `sgx-pre2020/` — 144 JSON, 96 HTML, 58 TXT, 42 PDF, 35 BIN, 21 MD, 6 PY, 6 JSONL, 5 SH, 2 TSV, 1 ZIP, 1 XLSM (the SGX products workbook) |
| Distilled decision notes | 21 Markdown files incl. `2026-09-06-era-FINAL-ledger-and-risks.md` (**142 KB**), `era-FINAL.json` (147 KB), `era-proposals.json` (158 KB), `era-refutations.json` (**232 KB**) |
| Adversarial review outcome | **19 findings, 18 confirmed**, all fixed in one commit (`d475f20`) — including a **fabricated content-api `queryId`** in `history.rs` |
| Code produced | `sgx_equity_index.rs` 425 + `sgx_equity_index_more.rs` 421 + `history.rs` 454 + `eras.rs` 232 = **1,532 lines** across 4 modules (2 of them split purely for the 500-line ceiling), **14 revision rows** for 5 keys, `history.rs` at **73% comment** |
| Tests produced | `tests/futures_family_boundaries/sgx_equity_index_eras.rs` 660 + `sgx_equity_index.rs` 309 = **969 lines** |
| PR churn | #44 +1,170/−805 · #67 +1,238/−276 · #68 +201/−167 · #69 +739/−190 = **+3,348/−1,438** |
| Reversals during the work | the 2026-09-05 rule-out of the SGX change log was **reversed** on 2026-09-06 (`2026-09-06-catalogue-changelog-REVERSAL.md`); the whole floor treatment was re-keyed twice (#67 then #69) |
| Residue | issue #66 open; `sgx_equity_index_*` are all still **Partial / Gap: executable** |

**~100 agent runs, 417 saved artifacts, 9 workflows, 4 PRs, 10 calendar days,
1,532 lines of source and 969 lines of test — to produce 14 revision rows
across 5 keys that remain Partial.**

### 5.4 Case study — `ECBTC` (#57 / PR #60)

| Measure | Value |
|---|---|
| Issue #57 | opened 2026-09-06T00:16Z, closed 02:37Z — **2 h 21 m** |
| PR #60 | opened 02:11Z, merged 02:37Z — **26 min**, 22 files, +949/−117, 4 commits, 3 review events, both CodeRabbit findings fixed |
| Research | `ecbtc/` — **37 files, 1.0 MB**, all created 2026-09-06; "all eight workflow results" from `wf_db3476fa-d54` (agents hunt-0..3, verify-4..7 — 4 landed in `ecbtc/`, 4 in `sgx-pre2020/`), the wiki version history, and **26 weekly CME Globex notices (2026-02…08) saved as text** |
| Outcome | one key, `globex_event_contracts_btc`, **9 revision rows**, 374-line module, 318-line test module, ledger note **4,962 chars**, Basis **Partial / Gap: executable** |
| Why it cost what it did | two CME primaries disagree **by one hour** on the new daily close, and the disputed hour is exactly the former expiry instant. Adjudication required establishing statement order from Confluence's version API and proving SER-9740R's Table 2 is a carried-over crypto cell that misstates ECBTC's *own* prior hours |
| Governance side-effects | added an intersection-for-source-conflict bullet to `AGENTS.md`; rewrote `docs/schedules/unsupported-families.md`; PR #59 added **LAW-SESSION-NOT-EXPIRY** as a direct consequence of this family |

**One key, one contested hour: 8 agent runs, 37 artifacts, ~2.4 hours wall
clock, +949 lines, one new law and one new modeling convention.**

### 5.5 Projected cost of the trade-type plan (issue #58)

Source: `/Users/agedvagabond/Developer/exchange-hours-research/cme-globex/trade-types/PLAN-58-trade-type-keys.md`
(**1,846 lines, 139 KB**, planned 2026-09-12 against `main` @ `687e562`).

**Shape:** 13 PRs, **32 new keys**, 6 keys deliberately blocked, 2 rejections
recorded on evidence. Keys per PR: 0, 5, 2, 1, 2, 3, 3, 3, 3, 2, 3, 2, 3.

**Inputs already consumed:** 8 research gates + 9 adversarial verdicts
(`U1`, `U4`, `U6`, `U8`, `U16-U17`, `D8`, `ag-crypto-tas-history`,
`btic-non-equity-groups`, `metals-tas-history`, `standalone-products-gates`,
each with a `.verify.json`), **2,072 raw files** under `trade-types/raw/`,
`cme-globex/` at **150 MB**.

**What the plan itself says it requires:**

* **63 distinct primary-document citations** already identified by ID
  (RA0907-4 … RA2302-5, SER-5542 … SER-9740R, Submissions 10-070 … 26-234,
  Clearing Advisories 20-061 / 21-234) — plus ~200 dated capture observations.
* **10 maintainer decisions** — D-1 (cross-zone representation, gates PRs 11-13),
  D-2 (TAS/TAM granularity), D-3 (does "pending CFTC review" defeat an effective
  day? — gates PRs 10, 13), D-4 (does a labelled `closed@` feed event promote a
  marker to a close? — gates PR 12), D-5, D-6, D-7a/b/c, D-8. PRs 1-4 need none;
  PRs 5-9 need the four minor ones; **PRs 10-13 are blocked on D-1…D-4**.
* **13-item registration surface per PR** (§4.3 above), all hand-written.
* **Mutation-check every cutover row.**
* **Every PR touches `verification.md`, `README.md`, `CHANGELOG.md` and
  `sources.md`** — "each merge breaks the next one's mergeability… land one,
  rebase the rest, and re-derive every tally from the *merged* ledger."
* One fence PR first (delivered as #78).
* `regular: &[]` for **all 32 keys**, each module naming the channels its own
  empty `regular` rests on.

**Measured so far (PRs 1 and 2 of 13):**

| | PR 1 (#78, merged) | PR 2 (#83, open) |
|---|---|---|
| Keys | 0 | 5 |
| Files / diff | 7 / +831 −65 | 17 / +1,411 −36 |
| Commits | 4 (incl. 2 CodeRabbit rounds) | 1 |
| Review events | 11 | 0 yet |
| New tests | 6 fence tests | 10 boundary tests (544→554) |
| Revision rows | 0 | **11** |
| Mutation checks | — | **11** |
| GitHub issues opened | **5** (#73–#77) | **4** (#79–#82) |
| README/audit counts changed | the fences themselves | **8** |
| Wall clock | 1 h 05 m | — |

**Projection from the measured rate.** Extrapolating PR 2's 282
insertions/key over 32 keys, plus 11 more PRs' fence and documentation churn at
PR 1's rate:

| Projected quantity | Estimate | Basis |
|---|---:|---|
| New source lines | **~9,000–11,500** | 32 × 282 = 9,024, plus ~11 × 150 doc churn |
| New revision rows | **~70** | 11 rows / 5 keys = 2.2 per key × 32 |
| Revision rows after | 279 → **~349** (+25%); futures rows 130 → **~200** (+54%) |
| Ledger rows after | 132 → **164** | 96 + 68 |
| `MarketHoursKey` variants after | 36 → **68** (+89%) |
| Ledger note prose added | **~132 KB** | 32 × 4,125 chars (the recent mean) |
| New test modules | **~13** | one submodule per PR |
| New tests | **~65–100** | 10 tests / 5 keys (PR 2) to 10 / 1 key (single-key PRs) |
| GitHub issues opened | **~25–35** | 9 issues across the first 2 PRs |
| Mutation checks | **~70** | one per revision row |
| Hand-written list edits | **13 × 13 = 169** registration-surface items |
| Ledger rebase conflicts | **12** guaranteed (each PR after the first) |
| `futures_profile.rs` growth | 488 + 32×14 = **~936 lines** | 14 net lines/key measured on #83 — **breaches the 500-line ceiling at PR 3** |
| `EXPECTED_MARKET_HOURS_KEY_NAMES` | `[&str; 36]` → `[&str; 68]` | hand-written, array length included |
| `number_words` ceiling | `assert!(n < 100)` still holds at 68 | but Partial keys go 29 → ~61 |

Blocked/rejected work the plan also produces: 6 blocked keys (already filed as
#73, #74, #75), 2 evidence-based rejections (Treasury TAS, Dutch TTF TAS) plus
a third (commodity-index BTIC) already written into
`docs/schedules/unsupported-families.md` §76-167.

---

## 6. Where the time actually goes

Classified from the research store's journals, decision notes and `STATUS.md`,
plus the repo's own git and PR record. The percentages are best estimates
anchored to the byte and count evidence in each row.

| Activity | Est. share of effort | Evidence |
|---|---:|---|
| **Retrieval** — finding and fetching the primary document at all | **~35%** | 3,134 `web.archive.org` references across the store; 175 occurrences of "403", 57 of "429", 33 of "blocked"/"BLOCKED", 2 of "503". `STATUS.md`: "cmegroup.com now 403s this machine at IP level regardless of headers, and many 2025-2026 SERs are absent from the Wayback CDX. Recent citations were read through a public text-extraction reader"; `sources.md` carries a "Channel limit" note asking for re-verification. Of the 417 SGX files, **360 are under `raw/`** — 10 sub-directories, one per retrieval channel (`portal-hours-page`, `catalogue`, `circulars`, `contract-sets-and-boundaries`, `calendar-pdfs-2016-2019`, `intermediate-2019-state`, `taiwan-2020-content-api`, `64-contentapi-2021-2024`, `65-spec-leaves`, `66-2016-notice`). Whole channels were ruled out after being worked: `2026-09-06-rulebook-channel-ruled-out.md` (member portal, defeated by LAW-PUBLIC-SOURCES), `2026-09-06-altsrc-*.json` (three alternative-source sweeps: broker platforms, vendors/regulator, "chase-4"). |
| **Adjudicating conflicts and interpretation** | **~25%** | `era-proposals.json` 158 KB → `era-refutations.json` **232 KB** → `era-FINAL.json` 147 KB: the refutation pass is the single largest artifact in the store, and "all 10 refutations… every time survives, corrections are to keying/labels". The SGX change log was **ruled out on 2026-09-05 and reversed on 2026-09-06** (`catalogue-changelog-REVERSAL.md`, `DECISION-changelog-admitted.md`), then required a bespoke four-part admission test in `AGENTS.md` plus a statistical warrant over **195 bare effective days**. ECBTC's whole cost was one disputed hour between two CME primaries. PLAN-58 §0 lists **7 handoff conclusions the gates overturned**, including **5 of 5** TAM launch dates being one day wrong. The floor treatment was re-keyed twice across #67 and #69. Ten maintainer decisions (D-1…D-8) remain open and **gate 4 of 13 PRs**. |
| **Writing citation prose** | **~20%** | 6,288 comment lines (36.2%) in `schedules/**`, rising to **63–83%** in every module written since 2026-09-05. Ledger notes: **125,045 characters**, mean per key row **2,206**, per *recent* key row **4,125** — a 9× inflation over the 475-char mean of the original exchange rows. `sgx_equity_index/history.rs` (454 lines, 73% comment, 43 URLs) exists **only** to hold prose; `eras.rs` was split off "so that module stays readable". `event_contracts.rs` is 263 comment lines to 42 code lines. |
| **Fence maintenance** | **~10%** | 25 fence tests, 1,373 lines, in a dedicated suite that parses the repo's own Markdown. At least **8 of them exist because prose silently drifted** (documented at `mod.rs:331`, `:557`, `:596`, `:704`). A `number_words()` helper exists solely to spell counts in prose. PR #83 changed **8 distinct README/audit counts** for 5 keys. PR #78 was an entire PR (7 files, +831, 11 review events, 5 issues opened) that shipped **zero keys** — purely fences. `databento-venues.md` snapshots each venue's Basis and a test asserts agreement, so a Basis change is a two-file edit. Trap 7: "Two PRs can move the counts along different axes, so neither branch's figures survive the merge." |
| **Review cycles** | **~10%** | 54 PRs in 24 calendar days; the 12 PRs sampled carry **64 review events** and **30 commits** for 12 merges — i.e. ~2.5 commits per PR, most of them review-response. PR #53: 10 review events, 3 commits, 8 h 21 m open. PR #78: 11 review events, 4 commits, two of them "CodeRabbit round one/two". The SGX adversarial review (`wf_220107a5-7d7`, 22 agent runs, 71 KB journal) produced **19 findings, 18 confirmed**, one of them a fabricated URL parameter in shipped code. `.coderabbit.yaml` is **21 KB** of repo-specific review policy. |

**Supporting aggregate.** Across the whole research store: **126 recorded agent
runs**, 10 named workflows, **255 MB** of saved evidence, against **54 PRs, 100
commits, 23,962 source lines and 279 revision rows** produced in **24 calendar
days** (2026-08-20 → 2026-09-12). The store is **10.6× larger than the crate's
entire source tree by byte count**.

**The single sharpest cost signal.** Compare what the repository produced in its
first three days with what it produces now:

| | 2026-08-20…23 | 2026-09-05…12 |
|---|---|---|
| Identities added | 96 exchanges + 13 keys, in ~4 PRs | 1 key per PR (5 in the one batched PR) |
| Insertions per identity | `a116b2a`+`8a53de3`+`5c946cf` delivered 109 identities | **794–1,314 per key** |
| Ledger note per row | **475 chars** | **4,125 chars** |
| Module comment share | 10–30% | **63–83%** |
| Fence tests | 0 | 25 |
| Issues opened per PR | ~0 | **4–5** |

The per-identity cost has risen by roughly **an order of magnitude** while the
consumer's demand has not moved: **SharurPlatform's generated catalog maps 104
roots to exactly 8 of the 36 keys** (`GlobexCryptocurrency` 21,
`GlobexEnergy` 20, `GlobexInterestRates` 18, `GlobexFx` 17, `GlobexGrains` 12,
`GlobexEquityIndex` 11, `GlobexLivestock` 4, `GlobexNikkei225Dollar` 1) and
**25 of the 96 exchanges** — and that catalog is stale relative to the crate
(`MZC`/`MZL`/`MZM`/`MZS`/`MZW` still point at `GlobexGrains`; nothing points at
`globex_mini_grains`, `globex_rough_rice`, `globex_weather`,
`globex_spot_quoted`, the event-contract keys, the SGX keys, the ICE keys, or
the five TAS keys). **None of the 22 keys added since 2026-08-23 has a consumer
today**, and the plan proposes to add 32 more.

---

## 7. Open questions for the review

1. **`src/calendar/futures_profile.rs` is at 488 of 500 lines and grows 14 lines
   per key.** PR 3 of the plan breaches it. The plan does not allocate a split.
2. **Half the exported API has only the test suite as a consumer** — the whole
   session-exception layer (707 source lines + 1,147 test lines), the whole
   `StaticDayPolicy` record format, all 10 bulk builders, all 10 fixed-snapshot
   free functions, `MarketHours`, `SessionRule`, `session_profile`. Is that
   surface a deliverable or an unpaid liability?
3. **The regular/extended split is `regular: &[]` for 13 of 36 key profiles
   today and for all 32 proposed keys.** On the futures side the distinction is
   carrying almost no information, yet it is one of the two things `AGENTS.md`
   demands a primary source for — research gate U-4 needed four independent
   channels to establish the empty `regular` for the trade-type shapes.
4. **Prose is the product.** 36% of the schedule tree and 83% of the newest
   modules are comment; the ledger holds 125 KB of notes; 25 tests exist to keep
   counts in prose consistent. Nothing in the crate's type system holds a
   citation, a withheld window, an era, or a conflict — so all of it has to be
   guarded by string assertions.
5. **`Gap: executable` is now the normal outcome for a new key.** 22 of 57
   Partial rows, and **12 of the 14 most recently added key rows**. The
   "executable-hours first" priority in `AGENTS.md` is not being satisfied by
   the keys being added.
6. **Ten maintainer decisions gate 4 of the plan's 13 PRs** and have been open
   since 2026-09-12. Two of them (#71, #72) are filed as issues.
