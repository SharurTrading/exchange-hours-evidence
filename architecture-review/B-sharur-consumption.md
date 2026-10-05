# Task B — How SharurPlatform actually uses `exchange-hours`

Facts only. Every claim below is cited to a file and line read on 2026-09-12.
No file in `exchange-hours-rs` or `SharurPlatform` was modified; both working
trees are clean.

Repos inspected:

- `/Users/agedvagabond/Developer/SharurPlatform` (the live consumer, Rust workspace, 14 crates)
- `/Users/agedvagabond/Developer/exchange-hours-rs` (the crate, 215 `.rs` files, 43 861 lines)
- `/Users/agedvagabond/Developer/Sharur` (the *predecessor* platform — has its own vendored `crates/market-hours`, does **not** depend on `exchange-hours`)
- `/Users/agedvagabond/Developer/NautilusResearch` (Python research repo — **zero** references to `exchange-hours`)
- `/Users/agedvagabond/Developer/nautilus_trader` (the engine NautilusResearch uses)

---

## 0. Executive facts (the short version)

| Fact | Value | Evidence |
| --- | --- | --- |
| Dependency form | git pin, not a version | `Cargo.toml:50` — `rev = "a245618ade40b8d4f5b68e2a95bb922143bf4f95"` |
| Pinned rev is **not an ancestor of `main`** | `git merge-base --is-ancestor a245618 main` → **no**; `main` head is `687e562` (the squash-merge of the same work) | measured |
| Crates that import `exchange_hours` directly | **2** of 14 — `domain` and `ui` | `crates/domain/Cargo.toml:17`, `crates/ui/Cargo.toml:28` |
| `MarketHoursKey` variants in the crate | **36** (incl. `always_open`, `sgx`, 5 metals-TAS on this branch) | `src/calendar/futures_profile.rs:143`+ |
| `MarketHoursKey` variants Sharur can ever produce | **8** | `crates/domain/src/globex_products.rs` |
| `Exchange` variants in the crate | **~96** | `src/calendar/exchange/mod.rs:37` |
| `Exchange` variants reachable from a *tradable instrument* | **8** (CBOT, CDE, CFE, CME, COMEX, EUREX, ICEUS/NYBOT, NYMEX) | `crates/adapters/rithmic/src/catalog.rs:74–172` |
| `Exchange` variants reachable from the *UI world clock* | **24** | `crates/ui/src/market_clock/sets.rs` |
| `ExchangeCalendar` public methods | **32** | `src/calendar/exchange_calendar/mod.rs` + `candles.rs` |
| …of which Sharur calls in production | **13** | §1 |
| Roots in Sharur's root→key table | **104**, *all* with a key (zero `None` rows) | `crates/domain/src/globex_products.rs:82–186` |
| GLBX roots with **no** key (listing-exchange fallback) | **1 342** | `catalog-artifacts/audit.md` |
| Instrument kinds either live adapter admits | **`Future` only** | `crates/adapters/projectx/src/capabilities.rs:33–35`, `crates/adapters/rithmic/src/capabilities.rs:60` |
| Holiday / early-close data in production | **none** — `DayPolicy` seam exists, is never injected | §4.1 |
| Deepest observed calendar walk | **2007-07-15**, 2.5 years below the crate's January-2010 floor | §3.2, measured from the on-disk seed cache |
| Hot-path query rate | **4 999 `is_open` + 1 `session_close` per cold chart-axis build** | `crates/chart/tests/unit/charting/time_axis/context.rs:478–481` |

---

## 1. Every call site

### 1.1 Shape of the dependency

Sharur does **not** call `exchange_hours` from application code. It wraps it once:

```
exchange_hours::{ExchangeCalendar, MarketHoursKey, SessionState, DayPolicy, SessionKind, CalendarResolution, Exchange}
        │
        ├── crates/domain/src/data/calendar/exchange/{mod.rs,port.rs,grid.rs}   ← the ONE adapter
        │        └── implements domain::SessionCalendar (crates/domain/src/data/calendar/mod.rs:102)
        │                └── consumed by application/, app/, chart/ (via a second port), ui/
        │
        └── crates/ui/src/market_clock/*                                        ← the ONLY direct second consumer
```

`crates/domain/src/data/calendar/mod.rs:32,42,48` re-export `MarketHoursKey`,
`DayPolicy`, `SessionState` verbatim ("the platform has ONE such identity");
`crates/domain/src/instrument/mod.rs:28` re-exports `Exchange` and
`ParseExchangeError`. So `MarketHoursKey`'s canonical `snake_case` string is a
**persisted wire identity** carried on the instrument definition
(`calendar/mod.rs:29–31`) — renaming a key is a breaking change for Sharur's
stored definitions.

### 1.2 Crate APIs called in production (13)

All inside `crates/domain/src/data/calendar/exchange/`:

| Crate API | Call site | Purpose |
| --- | --- | --- |
| `calendar_for_market_hours_key` | `mod.rs:106` | build calendar from authored family |
| `calendar_for_exchange` | `mod.rs:157` | build calendar from listing exchange (fallback) |
| `ExchangeCalendar::candle_start` / `candle_end` | `mod.rs:192–201` | `CalendarResolution::{Daily,Weekly,Monthly}` period bounds |
| `ExchangeCalendar::tz` | `mod.rs:220` | venue zone for the intraday wall-clock grid |
| `ExchangeCalendar::source` | `mod.rs:89` | `Debug` only |
| `ExchangeCalendar::market_hours_key` | `mod.rs:131` | log/persist identity |
| `ExchangeCalendar::exchange` | `mod.rs:166` | log/persist identity |
| `ExchangeCalendar::with_day_policy` | `mod.rs:149` | **never reached in production** (see §4.1) |
| `ExchangeCalendar::is_open` | `port.rs:24–25` | hot-path predicate |
| `ExchangeCalendar::session_bounds` | `port.rs:33–34` | block containment (no production consumer — §5.2) |
| `ExchangeCalendar::session_state` | `port.rs:111–112` | one classification for the whole UI |
| `ExchangeCalendar::next_session_open_after` | `port.rs:120–121` | "opens in …" countdown |
| `ExchangeCalendar::is_closed_all_day_at(t, tz, SessionKind::Both)` | `port.rs:132–133` | no production consumer (§5.2) |
| `ExchangeCalendar::trade_date` | `port.rs:141–142` | session label |

Plus the direct UI consumer:

| Crate API | Call site | Purpose |
| --- | --- | --- |
| `ExchangeCalendar::new(Exchange)` / `::for_market_hours_key` | `crates/ui/src/market_clock/markets.rs:56–60` | world-clock rows |
| `ExchangeCalendar::session_state` | `markets.rs:97` | phase label (`OPEN`/`EXT`/`QUEUE`/`HALT`/`MAINT`/`CLOSED`) |
| `ExchangeCalendar::is_open` | `markets.rs:183` | "CLOSES IN"/"OPENS IN" verb |
| `ExchangeCalendar::session_bounds` | `markets.rs:181` | countdown boundary |
| `ExchangeCalendar::session_bounds_with(kind)` | `markets.rs:119,166` | **RTH vs ETH dial rings** |
| `ExchangeCalendar::tz` | `markets.rs:163`, `panel.rs`, `timeline.rs` | display projection |
| `SessionKind` | `color.rs:34–41`, `paint.rs:74–101`, `timeline.rs:133` | ring colouring |

### 1.3 Who consumes the answer, and for what

| # | Call site | Port method | What the caller does with the answer |
| --- | --- | --- | --- |
| 1 | `crates/application/src/bars/consolidator.rs:189` | `is_open(trade.time())` | **Drops the trade** if the session says closed, with a `warn`. Once per print — the hottest path in the process. |
| 2 | `crates/application/src/bars/footprint.rs:95` | `is_open(trade.time())` | Same gate for the per-price (footprint) consolidator. Silent drop. |
| 3 | `crates/domain/src/data/close_time.rs:83,105` | `window_bounds(resolution, t)` | **Candle/bar boundaries.** `window_open` / `close_time`. |
| 4 | `crates/domain/src/data/close_time.rs:141` | `intraday_window_in_day(...)` | Cheap half of the same derivation, given a held trading day. |
| 5 | `crates/domain/src/data/day_memo.rs:181,185` | `trading_day_bounds` + `window_bounds_in_day` | `TradingDayMemo` — buys the expensive trading-day search once per day instead of once per bar. |
| 6 | `crates/domain/src/data/window_reach.rs:335,343,366` | `trading_day_bounds`, `intraday_window_in_day` | **Backfill window derivation.** Walks *N* of the venue's own windows backwards from now. |
| 7 | `crates/app/src/history.rs:171` → `224` | `session_calendar()` → `window_open_back` | **Backfill window for the bar seed.** Converts "5 000 bars" into a real `[start, end)` against this instrument's sessions (#345: nominal spans delivered 3 433 of 5 000 bars). |
| 8 | `crates/app/src/history.rs:248` | `is_open(end)` | Decides whether a live tail exists at the fetch cutoff. |
| 9 | `crates/app/src/history.rs:591,615` | `session_calendar()` → `window_open_back` | Same, for the footprint/volume-profile seed (#347, #391). |
| 10 | `crates/app/src/history_tick_bar_fetch.rs:67` → `138–147` | `is_open(end)`, `window_open`, `window_open_back` | `source_start` — elects the stable replay origin for one-tick-bar seeds (the current daily window's open, or the previous one if closed). |
| 11 | `crates/app/src/history_raw_print_fetch.rs:75` | same `source_start` | Same election for raw-print (tape) replay. |
| 12 | `crates/application/src/engine/mod.rs:403–408` | `session_hours_basis()` + `session_calendar()` | Resolves the calendar **once per stream at creation**, shares it down the consolidation chain. |
| 13 | `crates/application/src/engine/mod.rs:415–421` | — | Emits `warn!("stream uses approximate listing-exchange session hours")` when the basis is `ExchangeFallback`. |
| 14 | `crates/ui/src/chart_window/mod.rs:294–295` | `basis.session_calendar()` | Builds the chart's `SessionCalendarAdapter`. |
| 15 | `crates/ui/src/session_calendar.rs:100` | `session_state` | Chart's single status source. |
| 16 | `crates/ui/src/session_calendar.rs:118` | `is_open` | **Deliberate override** of the trait default, because `session_state` costs 34.6× more on a closed weekend (12.52 µs vs 361.8 ns) and the chart asks it every frame. |
| 17 | `crates/ui/src/session_calendar.rs:123` | `window_bounds(Resolution::days(1), t)` | `session_close` — the trading-day end indicators bucket on. |
| 18 | `crates/ui/src/session_calendar.rs:129` | `next_session_open_after` | Closed-banner countdown target. |
| 19 | `crates/ui/src/session_calendar.rs:135` | `trade_date` | Header session label (Sunday-evening print → Monday). |
| 20 | `crates/ui/src/dom/trading/mod.rs:125` (called from `crates/ui/src/dom/body.rs:273`) | `is_open(clock.now())` | **Order-routing gate.** `DomTrading::tradable() = enabled() && market_open` (`mod.rs:115`); `body.rs:399` passes it as `interactive`, so the DOM ladder's buy/sell actions are disabled while the session says closed. Queried every repaint, building a fresh `ExchangeHoursCalendar` each time (the constructor is `const`). |
| 21 | `crates/chart/src/charting/frame_admission.rs:53,119` | `is_open(now)` | Suppresses the bar-close countdown while closed. |
| 22 | `crates/chart/src/charting/time_axis/spacing.rs:392` | `is_open` then `session_state(...).is_closure()` | **Closure-compressed time axis** — squeezes weekends/maintenance out of the x-axis but never a halt. |
| 23 | `crates/chart/src/charting/render/session_breaks.rs:36` | `session_state(*at).is_closure()` | Draws the vertical session-break line before a session's first bar. |
| 24 | `crates/chart/src/indicators/portable/inputs.rs:228–235` | `session_state(before)`, `session_state(open)`, `next_open` | **Session VWAP anchors.** `opens.regular` fires on a transition *into* `OpenRegular`; `opens.extended` fires when the prior state was a closure **or `OrderEntry`**. This is the one place the `OrderEntry` phase is load-bearing outside the world clock. |
| 25 | `crates/chart/src/indicators/portable/inputs.rs:124` | `session_close` (via `session_id_for_bar`) | Trading-day bucket key for every indicator. Falls back to UTC dates when no calendar. |
| 26 | `crates/ui/src/market_clock/*` | `session_state`, `is_open`, `session_bounds`, `session_bounds_with(kind)`, `tz` | The global market-clock window: 5 curated sets (Overview 18, Globex 7, Forex 8, Equities 17, Derivatives 9), radial dial + timeline, 1 Hz repaint. |
| 27 | `crates/ui/src/chart_feed/binding.rs:222` | `SessionHoursBasis` match | Sets `approximate_session_hours` on the published `StreamRegistration` so the UI can disclose the fallback. |

### 1.4 Purpose → API → call site → precision/history actually needed

| Purpose | Crate API | Sharur call site | Time precision needed | History depth needed |
| --- | --- | --- | --- | --- |
| Drop out-of-session prints | `is_open` | `application/src/bars/consolidator.rs:189`, `bars/footprint.rs:95` | second (prints carry ns, boundary is a second) | **live only** — prints are current |
| Candle/bar boundaries (intraday) | `candle_start`/`candle_end` @ `Daily` + own wall-clock grid | `domain/.../exchange/port.rs:67–68`, `grid.rs` | **the two ends of the trading day only** — the grid inside is venue wall clock, indifferent to intraday structure (`grid.rs:9–27`) | as deep as the chart: 1 m → ~4 days, 5 m → ~25 days, 15 m → ~75 days (measured §3.2) |
| Candle boundaries (D/W/M) | `candle_start`/`candle_end` @ `Daily`/`Weekly`/`Monthly` | `port.rs:70–72` | minute | **to 2007** on a 5 000-point daily chart (measured) |
| Backfill window sizing | `trading_day_bounds` + `intraday_window_in_day` | `domain/src/data/window_reach.rs:335–366` ← `app/src/history.rs:224,615` | minute | same as the chart's depth; the walk *stops at the Unix epoch*, not at 2010 (`window_reach.rs:297`, `checked_sub(1)`) |
| Replay-origin election | `is_open`, `window_open`, `window_open_back` | `app/src/history_tick_bar_fetch.rs:138–147`, `history_raw_print_fetch.rs:75` | minute | 1–2 trading days |
| Trade-date stamping | `trade_date` | `domain/.../port.rs:141`, surfaced at `ui/src/session_calendar.rs:135` | **date** | whatever the chart shows |
| Is-open gate for order routing (UI) | `is_open` | `ui/src/dom/trading/mod.rs:125` | second | **now only** |
| Closed banner / countdown | `session_state`, `next_session_open_after` | `ui/src/session_calendar.rs:100,129` | second | **now only** |
| Session-break lines, axis compression | `session_state` (`is_closure`) | `chart/.../render/session_breaks.rs:36`, `time_axis/spacing.rs:392` | minute | chart depth |
| Session VWAP anchors (RTH/ETH) | `session_state` transitions incl. `OrderEntry` | `chart/src/indicators/portable/inputs.rs:228–235` | minute | chart depth |
| World clock (24 venues, 11 families) | `session_state`, `session_bounds_with(SessionKind)`, `tz` | `ui/src/market_clock/*` | minute | **±1 day** — the dial only draws today and the next real session day (`markets.rs:143–175`) |

---

## 2. The catalog: how a root becomes a key

### 2.1 There is no generated catalog inside SharurPlatform

The handoff's "SharurPlatform's generated catalog" is **hand-authored today**, not
generated. The single table is:

`/Users/agedvagabond/Developer/SharurPlatform/crates/domain/src/globex_products.rs`
— 190 lines, a `static PRODUCTS: &[(&str, Exchange, Option<MarketHoursKey>)]`
sorted for `binary_search` (`:46–55`).

Its header (`:14–25`) records that it was *validated against* a generated
artifact — Databento GLBX.MDP3, publication `sharur-reference-publication-v1`,
generator rev `97cad78c7f93df692103b67b0eb562cda254c6af`, bundle SHA-256
`95784420261e0da3bf2d090d06d49a35fa807176baf0cba9f40d60266a6ea4c7`, checked
2026-09-05 — but explicitly states the extraction helper "is **not** a runtime
dependency or a retained generator". The generator lives in
`/Users/agedvagabond/Developer/globex-reference-catalog` (vendored into the
*other* repo at `Sharur/vendor/globex-reference-catalog`).

The artifacts named in the handoff live only in
`/Users/agedvagabond/Developer/exchange-hours-research/catalog-artifacts/`.

### 2.2 The resolution chain

```
venue search row (root, optional exchange hint)
   │
   ├─ rithmic:  products::address(root, hint)       crates/adapters/rithmic/src/products.rs:19-25
   │            products::market_hours(root)        crates/adapters/rithmic/src/products.rs:28-34   → warn! if None
   ├─ projectx: products::listing_exchange(...)     crates/adapters/projectx/src/products.rs:19-32  → error! + Exchange::Cme default
   │            products::market_hours(root)        crates/adapters/projectx/src/products.rs:35-46  → warn! if None
   │
   ▼
InstrumentDetails { exchange, market_hours: Option<MarketHoursKey> }   crates/domain/src/instrument/catalog.rs:101
   │
   ▼
Instrument::session_hours_basis()                  crates/domain/src/instrument/mod.rs:199-210
   ├─ Some(key)                 → SessionHoursBasis::ProductFamily(key)
   ├─ None & futures-shaped     → SessionHoursBasis::ExchangeFallback(exchange)
   └─ None & CurrencyPair       → SessionHoursBasis::Exchange(exchange)
   │
   ▼
SessionHoursBasis::session_calendar()              crates/domain/src/instrument/mod.rs:57-63
   ├─ ProductFamily → exchange_hours::calendar_for_market_hours_key(key)
   └─ Exchange/Fallback → exchange_hours::calendar_for_exchange(exchange)
```

**Both adapters use the same table** (`rithmic/src/products.rs:29` and
`projectx/src/products.rs:37` both call `domain::globex_products::outright_future`).
No runtime lookup happens inside the calendar: "Neither calendar path performs a
runtime root lookup" (`crates/domain/src/data/calendar/exchange/mod.rs:33–36`).

### 2.3 What happens to a root with no key

**It is still fully usable.** It is not excluded, and it is *not* treated as
always-open. It gets the crate's venue-level compatibility default:

| Venue namespace admitted | `Exchange` | Crate default profile | Correct for |
| --- | --- | --- | --- |
| `CME` | `Cme` | `cme_profile_at` (≙ `GlobexEquityIndex`) | equity index only |
| `CBOT` | `Cbot` | `cbot_profile_at` (≙ `GlobexGrains`) | standard grains only |
| `COMEX`, `NYMEX` | `Comex`/`Nymex` | `energy_metals_profile_at` (≙ `GlobexEnergy`) | energy/metals only |
| `CFE` | `Cfe` | `cfe_profile_at` (≙ `CfeVix`) | VX — the only CFE futures family Rithmic lists |
| `EUREX` | `Eurex` | `eurex_profile_at` (FESX/FDAX/FDXM) | **wrong for FGBL/FGBM/FGBS/FGBX** |
| `NYBOT` | `Iceus` | `ice_us_fang_profile_at` | **wrong for SB/KC/CC/CT/OJ/DX** |
| `CDE` | `CoinbaseDerivatives` | `coinbase_derivatives_profile_at` | — |
| `SMFE` | `Smfe` | `small_exchange_profile_at` | — (no futures grammar observed) |

(`src/calendar/presets/historical.rs:84–91`; namespaces at
`crates/adapters/rithmic/src/catalog.rs:74–172`.)

The failure is **silent-but-logged**, three ways:

1. `tracing::warn!` at the adapter (`rithmic/src/products.rs:31`, `projectx/src/products.rs:40`).
2. `tracing::warn!` at stream creation (`application/src/engine/mod.rs:415–421`).
3. A boolean `approximate_session_hours` on the published `StreamRegistration`
   (`ui/src/chart_feed/binding.rs:222–225`) so the UI can badge it.

**Concrete magnitude of a wrong fallback.** ICE Futures U.S. Sugar No. 11 trades
Mon–Fri 03:30–13:00 ET (`src/calendar/schedules/futures/us/ice_sugar.rs:27–31`).
NYSE FANG+ trades Sun 18:00 → Mon–Thu 20:00–18:00 ET
(`src/calendar/schedules/futures/us/ice_us.rs:24–35`). A Sugar contract routed
through Rithmic's `NYBOT` namespace gets FANG+ hours — a ~12.5 hour/day error in
`is_open`, wrong trade dates, and a daily bar spanning the wrong window. The
crate **already has** `IceUsSugar`, `IceUsCoffee`, `IceUsCocoa`, `IceUsCotton`,
`IceUsOrangeJuice`, `IceUsDollarIndex` and `EurexFixedIncome`; Sharur is
**structurally unable to reach any of them**, because its only root→key table is
Globex-only.

### 2.4 Mapped counts

Sharur's authored table (`globex_products.rs`): **104 roots, 0 unmapped**.

By listing exchange: CME 54, CBOT 30, NYMEX 12, COMEX 8.

By key (8 of the crate's 36):

| Key | Roots |
| --- | ---: |
| `GlobexCryptocurrency` | 21 |
| `GlobexEnergy` | 20 |
| `GlobexInterestRates` | 18 |
| `GlobexFx` | 17 |
| `GlobexGrains` | 12 |
| `GlobexEquityIndex` | 11 |
| `GlobexLivestock` | 4 |
| `GlobexNikkei225Dollar` | 1 |

**28 crate keys are unreachable from any Sharur instrument**, including all 5
SGX equity-index keys, all 6 ICE U.S. softs/DX keys, `EurexFixedIncome`,
`GlobexMiniGrains`, `GlobexRoughRice`, `GlobexWeather`, `GlobexSpotQuoted`,
`GlobexEventContracts(Btc)`, and the 5 metals-TAS keys just added on this branch.
(11 of them *are* reachable from the world-clock UI: `CfeVix`, `Eurex`, `IceUs`,
`Sgx` plus the 7 Globex families — `crates/ui/src/market_clock/sets.rs:41–110`.)

### 2.5 The 1 342 unmapped GLBX roots — what they actually are

From `catalog-artifacts/audit.md` and `market-hours-root-classification.tsv`
(1 797 rows), `missing-market-hours.tsv` (1 342 rows):

By Databento exchange: **XNYM 769, XCME 420, XCBT 105, XCEC 48**.
Disposition: **1 341 of 1 342 are `ready_non_test`**.

Grouped by the CME schedule description on each row:

| Group | Roots | Would Sharur ever trade these? |
| --- | ---: | --- |
| NYMEX ClearPort / OTC-cleared energy swap-futures (`CPC-*`, `50 MW POWER- CMED`, fuel oil, petrochem, refined, ethanol, Henry Hub swaps) | **655** | No — block/EFRP-cleared, not on a retail Globex order book |
| CME weather futures | **179** | No |
| Trade-type variants (TAS / TAM / BTIC / TACO / TMAC) | **162** | **See §2.6** |
| Freight, ferrous scrap, alumina, urea, RIN/biofuel, environmental, LNG | **100** | No |
| Everything else (Brent penultimate financial, real estate (HI), UMBS, Bloomberg credit, lithium, cobalt, uranium, Shanghai gold, sector indices, exotic FX crosses, dairy, lumber, housing…) | **~246** | A handful (lumber `LBR`, dairy `DC/CB/CSC`, mini S&P SmallCap) are plausible; the rest are not |

Only **82 of 1 797** roots carry `continuous_price_series = True`, and all 82 are
CME's synthetic `*CP1`/`*CPA` continuous-series identifiers (e.g. `ESCP1`) —
*not* order books, and all in the `synthetic_no_ready` exclusion bucket. So that
column is not a tradability proxy; the schedule-description grouping above is.

The audit's own note: signature #1 — the plain **17:00–16:00 CT Globex
envelope** — covers **1 146 of the 1 371** non-test roots (`audit.md`, signature
table row 1). Only ~225 roots have a genuinely different-shaped week.

### 2.6 Are TAS/TAM/BTIC/TACO/TMAC ever subscribed?

**No.** `rg -i "\bTAS\b|BTIC|TACO|TMAC|\bTAM\b"` over all of SharurPlatform
(excluding `target/` and lockfiles) returns **zero** hits that are not
coincidental substrings of `ChartDataCoordinator` / `MarketDataCounts`. No TAS,
TAM, BTIC, TACO or TMAC root appears in `globex_products.rs`, in either adapter's
product tables, in any test fixture, or in any config.

### 2.7 Are spreads, options, or ClearPort ever subscribed?

**No.** Both live adapters admit exactly one instrument kind:

- `crates/adapters/projectx/src/capabilities.rs:33–35` — `market_data`,
  `history` and `execution` are each `&[InstrumentKind::Future]`.
- `crates/adapters/rithmic/src/capabilities.rs:60` —
  `ROUTED_INSTRUMENT_KINDS: &[InstrumentKind] = &[InstrumentKind::Future]`.
- `crates/adapters/projectx/src/reference.rs:155` constructs only
  `Instrument::Future(FuturesContract::new(...))`.

`domain::Instrument` *models* `FuturesOption`, `FuturesSpread`,
`FuturesOptionSpread` and `CurrencyPair` (`crates/domain/src/instrument/mod.rs:86–95`),
and `session_hours_basis` has arms for them (`:203–209`) — but no adapter can
produce one. The `CurrencyPair` arm is the only one that resolves to
`SessionHoursBasis::Exchange` (non-approximate) rather than `ExchangeFallback`.

Databento is **not** a live data source for SharurPlatform. Its only appearances
are (a) the reference-catalog provenance comment in `globex_products.rs`, and
(b) an order-book parity test, `crates/chart/tests/parity/databento_lob_parity.rs`.
Live data comes from Rithmic and ProjectX only.

---

## 3. Data horizons

### 3.1 Sharur configures no dataset start dates

There is no "since" constant, no dataset start date, no backfill floor anywhere
in SharurPlatform. History depth is expressed purely as a **count of the
instrument's own windows**:

- `crates/application/src/engine/history_depth.rs:99–132` — `HistoryDepth { resolution, points }`.
- `MAX_SEED_RECORDS = 250_000` (`history_depth.rs:88`) is the only hard cap.
- The chart's own cap is smaller: `DEFAULT_MAX_CHART_DATA_POINTS = 5_000`
  and `MAX_VISIBLE_BAR_COUNT = 5_000` (`crates/chart/src/charting/metrics.rs:42,61`).
- `history_depth.rs:134–160` is explicit that a nominal span must **never** be
  used as a window: "on a contract that shuts every weekend that window is
  roughly half again as wide as this number, which is exactly why treating the
  two as the same thing delivered 3 433 of 5 000 five-minute bars (#345)".

The conversion count → window happens in `domain::window_open_back`
(`crates/domain/src/data/window_reach.rs`), which walks the calendar backwards
one window at a time. Its only backstop is the **Unix epoch**
(`window_reach.rs:297`: `open.as_unix_nanos_u64().checked_sub(1)?`) and
`MAX_CLOSURE_SECONDS = 400 * 86_400` (`:65`). **Nothing stops the walk at 2010.**

### 3.2 Measured: Sharur walks the calendar to 2007

The on-disk durable seed cache
(`/Users/agedvagabond/Developer/SharurPlatform/.sharur-data-store/venue-seeds/rithmic/`,
schema `SeedCacheKey`, written by `crates/app/src/history_cache.rs`) records the
exact `[start_unix_nanos, covered_to_unix_nanos)` window each seed **asked for**.
For `MNQU26` (Rithmic), as of 2026-09-12:

| Resolution | Window start the calendar produced | Window end | Rows the venue returned |
| --- | --- | --- | ---: |
| **1 D** | **2007-07-15 22:00:00 UTC** | 2026-09-12 02:17:47 | **0** |
| 15 m | 2026-06-29 13:00:00 UTC | 2026-09-12 02:17:01 | 4 967 |
| 5 m | 2026-08-18 01:45:00 UTC | 2026-09-12 02:15:16 | 5 150 |
| 1 m | 2026-09-08 06:40:00 UTC | 2026-09-12 02:16:51 | 5 000 |

Conclusions:

- **The daily chart routinely queries the crate 2.5 years below its January-2010
  floor.** 5 000 `GlobexEquityIndex` trading days walked back from 2026-09-12
  land on 2007-07-15. Per `AGENTS.md:171–179`, everything below the floor
  resolves to the venue's oldest recorded revision, carried back unreviewed.
- **That history is pure waste here**: Rithmic returned **0 daily bars** for a
  September-2026 contract over a 19-year window. The walk cost ~5 000 trading-day
  derivations at 17–23 µs = **~85–115 ms**, for nothing.
- **Intraday never leaves ~3 months.** 1 m → 4 days, 5 m → 25 days, 15 m → 75
  days. The crate's dated revisions matter to intraday only through the daily
  window's two ends.
- Sharur never queries SGX, and would not query SGX hours before SGX data began
  even if it did — §2.4: no Sharur instrument can carry an SGX key, and Rithmic's
  namespace census (`crates/adapters/rithmic/src/catalog.rs`) lists no SGX venue.
  The crate's five SGX equity-index keys and their pre-2020 era work serve the
  world clock's one `MarketHoursKey::Sgx` row
  (`crates/ui/src/market_clock/sets.rs:99`), which asks only "now" and "the next
  session day".

### 3.3 The other repos' horizons

- **NautilusResearch** builds front-month artifacts from **2019-05-06**
  (`pipelines/build_frontmonth.py:303`), ending 2026-04-30. Example backtests run
  2026-01-05 → 2026-02-06 (`examples/backtest_trendline_pyramid.py:12`). Venue is
  `GLBX` (`src/nautilus_research/config.py:34`).
- **Sharur** (predecessor) ships `catalog-artifacts/glbx-mdp3/publication.json`
  with `publication_id: glbx-mdp3-20260517` — a 2026 snapshot.

Nothing in any repo needs exchange hours before 2019, except the accidental
daily-chart walk documented in §3.2.

---

## 4. What Sharur needs that the crate does not provide, and how it works around it

### 4.1 Holidays and early closes — no data at all

`LAW-HOLIDAY-SCOPE` puts holidays out of the crate's scope. Sharur accepts that
and built the `DayPolicy` seam
(`crates/domain/src/data/calendar/exchange/mod.rs:111–125`), which overlays every
query in one place (`mod.rs:142–151`).

**It is never injected.** `rg "with_day_policy"` over SharurPlatform returns the
declaration (`mod.rs:120`), the internal branch (`:149`), the re-export
(`calendar/mod.rs:42`), doc references, and **four test-only uses**
(`crates/domain/tests/unit/data/calendar/exchange/tests.rs:321,657,672,692`).
There is no holiday table, no holiday file, no holiday fetch, no holiday crate
anywhere in the workspace.

The platform states this plainly:
`crates/domain/README.md:281–297` — "The platform has no sourced holiday data
yet, so the composition root injects nothing; what the platform never does is
hand-roll a closure (LAW-UTC). Supplying the data is a platform task, not a
crate one."
`crates/ui/README.md:1032–1034` — the market-clock footer discloses
"holidays and half-days are not claimed without sourced `DayPolicy` overlays".

**Live consequences today** (all citable, none hypothetical):

- Thanksgiving / Christmas / Good Friday: `is_open` returns `true`, the DOM
  ladder's buy/sell stays enabled (`ui/src/dom/trading/mod.rs:115,125`), the
  closed banner is absent, and `session_state` reports `OpenRegular`.
- `window_open_back` places windows on closed days, so a 5 000-bar seed asks a
  window that is *short* of 5 000 real sessions — which surfaces as the
  `report_unreachable_past` warning (`crates/app/src/history.rs:374–383`) rather
  than as a correction.
- Early closes (13:00 CT half-days) put the last daily bar's close in the wrong
  place, and hence the trade-date label too.

**The measured reason the seam is off**: an overlay that closes nothing still
costs ~100× on `is_open` and ~130× on the bar-window derivation
(`crates/domain/README.md:293–296`; the figure is flagged **not re-measured**
since 0.2.x was removed, at `docs/benches/stage-3.md:490`). So "make the overlay
affordable" is an explicit standing crate-side request.

### 4.2 Expiries — not asked of the crate

The crate's `LAW-SESSION-NOT-EXPIRY` is respected. Listing lifetime lives on the
instrument definition: `InstrumentDetails { activation, expiration }`
(`crates/domain/src/instrument/catalog.rs:82–83`), validated at `:106–111`,
queried by `is_listed_at` (`:221–222`). No calendar call is involved. The crate's
`GlobexEventContracts` doc-note that "Termination of Trading is not this family's
session close" matches how Sharur already works.

### 4.3 RTH-vs-ETH candles — not needed for bars; needed for the clock and VWAP

- The **bar grid does not split RTH from ETH at all**. `window_bounds` uses
  `SessionKind::Both` implicitly (the trading day open→maintenance start, D41)
  and an epoch/venue wall-clock grid inside it
  (`crates/domain/src/data/calendar/exchange/grid.rs:9–27`). There is no
  "RTH-only chart" mode anywhere in the UI.
- `SessionKind::Regular`/`Extended` is used in exactly **two** places:
  the world clock's two dial rings and its `"ETH 07:00–09:30 · RTH 09:30–16:00"`
  hours label (`ui/src/market_clock/markets.rs:205–211`, `paint.rs:74–101`,
  `color.rs:34–41`); and, indirectly, the **session-VWAP regular/extended anchors**
  derived from `SessionState` transitions
  (`chart/src/indicators/portable/inputs.rs:228–235`).
- `is_closed_all_day_at` is always called with `SessionKind::Both`
  (`domain/.../port.rs:132–133`).

### 4.4 Order-entry / pre-open — the platform's documented gap is **already closed by the crate**

`crates/domain/README.md:303–313` lists, under "Awaiting the calendar crate":

> **A matching-vs-order-entry distinction.** The crate models the venue's
> *accepted-order* envelope: CME Group's 16:45 CT Pre-Open is a session … while
> the API exposes no way to ask which. … the closed banner calls the queue
> "open", the consolidator would accept a print inside it …

**That is stale.** In the pinned crate:

- CME Group's Pre-Opens are modelled as `order_entry`, *not* as sessions:
  `src/calendar/schedules/futures/us/cme_group.rs:99–102` ("They are therefore
  `order_entry`, not …"), with `CME_ORDER_ENTRY_1650` (`:182`),
  `CME_ORDER_ENTRY_1645` (`:194`), `CME_ORDER_ENTRY_CURRENT` (`:208`).
- `session_state` returns `SessionState::OrderEntry` only after both open checks
  fail (`src/calendar/query/status.rs:75–86`), so `is_open` already excludes the
  queue.
- The crate additionally exposes `is_accepting_orders`
  (`src/calendar/exchange_calendar/mod.rs:161`) and `is_order_entry_only` (`:173`),
  neither of which Sharur calls.

Sharur already *consumes* the distinction through `SessionState::OrderEntry`
(`ui/src/session_calendar.rs:85`, `market_clock/markets.rs:100` → `QUEUE`,
`chart/src/indicators/portable/inputs.rs:235`). The README paragraph is the only
thing out of date.

### 4.5 Maintenance windows — provided and used

`SessionState::Maintenance` drives `is_closure()`
(`crates/chart/src/session.rs:66–69`), which the closure-compressed axis and the
session-break renderer both depend on, and which is explicitly *not* extended to
`Halt` ("an axis that compressed one would tell the operator the halted minutes
never happened", `time_axis/spacing.rs:385–391`).

### 4.6 Exact-instant cutovers — not needed

The crate's revisions are keyed to venue-local **dates** (`select_revision`,
`src/calendar/schedules/timeline.rs:147`). Sharur never asks for a sub-day
cutover. The one place a cutover could have mattered — the intraday bar grid —
was deliberately decoupled: the grid is anchored at venue **midnight**, not at
the day's open or close, precisely so "a sourced historical close (16:15 CT for
equity index before 2015) would [not] shift replayed history"
(`crates/domain/src/data/calendar/exchange/grid.rs:18–27`).

### 4.7 Cross-zone closes — handled, and the one place DST precision matters

`grid.rs:34–53` resolves venue wall clocks with an explicit `Edge::{Open,Close}`
rule for DST fall-back repeats and a bounded 240-minute spring-forward probe,
"the rule the calendar crate applies to its own session boundaries, so a bar edge
and a session edge cannot land on different sides of the repeat". This is a
platform-side mirror of a crate rule — the one genuine coupling to crate
internals outside the public API.

---

## 5. What Sharur pays for and never uses

### 5.1 Crate surface never called

Of `ExchangeCalendar`'s 32 public methods, **19 are never called** by
SharurPlatform:

`candle_start_with`, `candle_end_with`, `hours_at`, `is_accepting_orders`,
`is_closed_all_day_in_calendar`, `is_closed_all_day_on`, `is_closed_trade_date`,
`is_maintenance`, `is_open_extended`, `is_open_regular`, `is_open_with`,
`is_order_entry_only`, `next_session_after`, `next_session_after_with`,
`time_end_of_day`.

(`time_end_of_day` *is* used — but by the **predecessor** repo's own crate:
`Sharur/apps/backtest/src/session_run.rs:650` calls
`market_hours::time_end_of_day` for the day-close forced-exit deadline.)

### 5.2 Platform port methods with no production caller

Three `domain::SessionCalendar` methods are implemented, documented at length,
tested, benchmarked — and called only by tests:

| Method | Declared | Production callers |
| --- | --- | --- |
| `session_close_containing` | `crates/domain/src/data/calendar/mod.rs:120` | **none** (only `tests/`, and a README paragraph at `domain/README.md:220`) |
| `is_closed_all_day` | `calendar/mod.rs:233` | **none** (only `tests/`) |
| `is_maintenance` | `calendar/mod.rs:251` | **none** (only `tests/` and `ui/tests/`) |

`session_close_containing` is the *only* consumer of the crate's
`session_bounds` inside the domain adapter, and `is_closed_all_day` is the only
consumer of `is_closed_all_day_at`. So the crate's **block structure** (the
15:15–16:00 CT post-close block, etc.) is paid for in the domain path and used
only by the world clock.

### 5.3 Keys and venues paid for and unreachable

- **28 of 36 `MarketHoursKey` variants** cannot be produced by any Sharur
  instrument (§2.4). 11 of those are reachable from the world clock; **17 are
  entirely unreachable from SharurPlatform**, including all 5 SGX equity-index
  keys, `EurexFixedIncome`, `GlobexMiniGrains`, `GlobexRoughRice`,
  `GlobexWeather`, `GlobexSpotQuoted`, `GlobexEventContracts`,
  `GlobexEventContractsBtc`, and the 5 metals-TAS keys on this branch.
- **~72 of ~96 `Exchange` variants** are referenced by neither the adapters nor
  the world clock.

### 5.4 History paid for and unused

Per §3.2: the intraday paths never reach further back than ~75 days. The only
consumer of pre-2020 history is the daily chart's backwards *walk*, which reaches
2007 and gets zero rows back. **Every dated revision older than roughly 2019 is,
for Sharur today, exercised only by a walk whose data never arrives.**

### 5.5 Sub-minute detail

Every `SessionRule` boundary Sharur consumes is a whole minute. The finest thing
it asks for is `Resolution` down to 1 second (`spec.rs` validates 1 s ..= 24 h),
but the *boundaries* are the trading day's two ends plus the wall-clock grid.
Sub-minute precision in the crate's rules is never observed.

---

## 6. The Nautilus angle

### 6.1 NautilusResearch does not use the crate

`rg "exchange_hours|exchange-hours|MarketHoursKey|ExchangeCalendar|SessionState"`
over `/Users/agedvagabond/Developer/NautilusResearch` → **zero hits**. It is a
Python repo (`pyproject.toml`, `databento>=0.83`, `nautilus_trader`).

It reimplements session logic arithmetically and at much lower fidelity:

- `src/nautilus_research/alpha/day_regime.py:32–39` —
  `DAY_OPEN_ET = time(18, 0)`, `DAY_CLOSE_ET = time(17, 0)`,
  `TOKYO_OPEN_TIME`, `LONDON_OPEN_TIME`, `US_OPEN_TIME = time(9, 30)`.
- `maintenance_session_ids` (`day_regime.py:58–80`) buckets bars by
  "18:00 **America/New_York**" — not Chicago, not the venue's own zone — with no
  maintenance break, no holidays, and no dated history.
- `window_boundaries` (`:83–109`) localises fixed wall clocks per market centre.

So the session semantics Sharur's chart and engine share with the crate are
duplicated, differently and less correctly, in the research repo.

### 6.2 `nautilus_trader` has no session/calendar concept

- `crates/model/src/instruments/futures_contract.rs:52–96` — `FuturesContract`
  carries `activation_ns` and `expiration_ns` and **no trading-hours field**. No
  instrument type in the model crate carries one.
- Bar aggregation is **UTC-epoch anchored with a fixed offset**, not
  session-aware: `get_time_bar_start`
  (`crates/model/src/data/bar.rs:197–260`) floors `now` to the step for
  ms/s/min/hour/day, anchors weeks to UTC Monday 00:00 and months to UTC 1 Jan,
  and adds only `time_bars_origin_offset: Option<SignedDuration>`
  (`crates/data/src/aggregation.rs:1770,1809,1880`).
- `rg "trading_hours|TradingHours"` over `crates/model/src` → **zero hits**. The
  only `trading_hours` references in the tree are in the Interactive Brokers
  adapter (a vendor field) and unrelated venue adapters.

**Implication.** A Nautilus `1-DAY` bar for `MESZ26.GLBX` is a UTC
midnight-to-midnight bucket unless someone sets an origin offset — exactly what
Sharur's `AlwaysOpenCalendar` / `epoch_grid_bounds` fallback does
(`crates/domain/src/data/calendar/mod.rs:278–280`). Nothing in Nautilus consumes
`MarketHoursKey`, `SessionState`, or dated revisions. If Nautilus ever became
Sharur's backtest engine, the crate would have to be pushed in at the
*aggregation* layer (a session-aware `BarAggregator`), because the engine's own
instrument model has nowhere to put the data.

### 6.3 The predecessor `Sharur` repo runs a *different*, vendored calendar

`/Users/agedvagabond/Developer/Sharur/crates/market-hours` is a self-contained
2 531-line single-module crate (`src/calendar.rs`) with its own `Exchange`,
`MarketHours`, `SessionRule`, `CalendarResolution` and `MarketHoursKey`. It is
**exchange-level, undated, and has no holiday hook**: "Holiday and product-level
calendars are intentionally out of scope; the `is_holiday` hook is a stub today,
so these are pure normal-week defaults" (`crates/market-hours/src/lib.rs:32–33`).

Its root table (`crates/instrument-catalog/src/root_sessions.rs:24–57`) maps
~50 roots to **6** keys, and notably lumps CBOT Treasuries (`ZT ZF ZN TN ZB UB`)
into `GlobexEnergy` — a grouping SharurPlatform's table has since split out into
`GlobexInterestRates`.

This is the "vendored v1 catalog tables" the chart's adapter doc-comment refers
to (`crates/ui/src/session_calendar.rs:10–15`): "Two calendars in one process
can disagree on holidays, half-days, and DST, and the disagreement shows up as a
rendering bug."

---

## 7. Performance profile (measured, from the platform's own benches)

From `/Users/agedvagabond/Developer/SharurPlatform/docs/benches/stage-3.md:276–297`
(`cargo bench -p domain --bench session_calendar_cost_by_query`, `GlobexEquityIndex`):

| Query | regular | overnight | maintenance | closed |
| --- | ---: | ---: | ---: | ---: |
| `is_open` | 167.7 ns | 561.3 ns | 704.0 ns | 361.8 ns |
| `session_state` | 168.6 ns | 561.2 ns | 20.20 µs | 12.52 µs |
| `daily_window` | 17.15 µs | 23.19 µs | 23.17 µs | 17.03 µs |
| `hourly_window` | 17.33 µs | 23.31 µs | 23.33 µs | 17.19 µs |

Consequences Sharur has already engineered around:

- **`session_state` is 34.6× `is_open` on a closed weekend**, which is why the
  UI adapter overrides the trait default (`ui/src/session_calendar.rs:104–119`)
  and why the axis asks `is_open` first (`time_axis/spacing.rs:383–392`).
- **The trading-day window is the expensive query at 17–23 µs.** It is bought
  once per trading day via `TradingDayMemo`
  (`crates/domain/src/data/day_memo.rs:29–55,181`), not once per bar.
- **Pinned frame budget**: a cold closure-compressed axis over 5 000 points costs
  exactly **4 999 `is_open` + 1 `session_close`**
  (`crates/chart/tests/unit/charting/time_axis/context.rs:478–481`) — that is
  0.84 ms (regular) to 1.8 ms (closed) per cold build, and the test comment notes
  that 4 999 `session_close` calls "is ~90 ms inside one render frame". Cold
  builds happen on "a retention shift, a resolution change and a rebind"
  (`context.rs:443–445`).
- **The daily-chart backfill walk** (§3.2) is ~5 000 trading-day derivations =
  **85–115 ms**, once per daily-chart open.
- The `DayPolicy` overlay's claimed ~100×/~130× multiplier is recorded as
  **not re-measured** (`docs/benches/stage-3.md:490`).

---

## 8. Open questions this task could not settle from the repos

1. **Is the pinned rev `a245618` still fetchable from GitHub?** It is not an
   ancestor of `main` (verified locally), so it is reachable only from a PR ref
   or from GitHub's reflog. A fresh clone + `cargo fetch` may or may not resolve
   it.
2. **Which `MarketHoursKey` string values are already persisted** in
   `.sharur-data-store/` workspaces and ledger rows? The serde form is a stable
   wire identity (`calendar/mod.rs:29–31`), but I did not decode the SQLite/JSONL
   stores to enumerate which keys are actually on disk.
3. **Does ProjectX's live catalog ever return a non-CME-family root?**
   `DEFAULT_LISTING_EXCHANGE = Exchange::Cme` (`projectx/src/capabilities.rs:29`)
   is the declared fallback when the root table misses; no census output was in
   the tree to say how often that fires in practice.
4. **Whether Sharur intends to admit ICE U.S. / Eurex fixed-income instruments.**
   Rithmic's namespace census admits `NYBOT` and `EUREX`
   (`rithmic/src/catalog.rs:121–147`), and the crate has correct keys for both,
   but no root table exists to reach them — so today they would silently get
   FANG+ / FESX hours (§2.3).
