# TASK C — Prior art and alternative models

Fact-gathering for the `exchange-hours-rs` architectural review.
Compiled 2026-09-12 (UTC). Read-only pass: nothing under
`/Users/agedvagabond/Developer/exchange-hours-rs` or
`/Users/agedvagabond/Developer/SharurPlatform` was modified.

Repo state observed: `exchange-hours-rs` at `5530f22` ("Add the five metals TAS
keys", 2026-09-12).

**Provenance convention used throughout.** Claims are tagged:
- **[L]** — verified from a local file in this pass; path and line given.
- **[W]** — verified from a source fetched in this pass (one of four fetches);
  URL given.
- **[M]** — from model memory, *not* verified in this pass. Treat as a lead,
  not as evidence.

---

## 0. The one-paragraph summary

Nothing in the local stack models trading hours at all. NautilusTrader has no
exchange-calendar type and no hours field on any instrument; the
Globex reference catalog stores no hours and not even the security group;
Databento's instrument-definition record carries no session field. All three
deliberately push the question outward — Nautilus to a *data* stream
(`InstrumentStatus`), the catalog to its consumer, Databento to CME. The
Python ecosystem (`exchange_calendars`, `pandas_market_calendars`) models hours
but at venue or product-family granularity, with **no trade-type dimension at
all**, **holidays in scope**, and **dated history supported by the data
structure but almost unused for CME**. QuantLib models no intraday times
whatsoever. Meanwhile CME itself publishes two machine-readable session
channels keyed on exactly the field Databento already carries
(`market_segment_id` + `group` = FIX 1300 + 1151), covering 1,364 security
groups — but publishing only *transitions*, never the Regular/Extended
classification, and only for the current week. That asymmetry — machine
truth exists for the envelope, human prose is required for the semantics — is
the structural fact behind every design option in §2.

---

## 1. Prior art, system by system

### 1.1 NautilusTrader (local: `/Users/agedvagabond/Developer/nautilus_trader`, `c7e04fe618`)

**Granularity of hours modelling: none. There is no calendar.** [L]

- `FuturesContract` (`crates/model/src/instruments/futures_contract.rs:52-104`)
  carries identity, asset class, exchange MIC, underlying, `activation_ns`,
  `expiration_ns`, currency, precisions, increments, multiplier, lot size,
  margins, fees, quantity/price bounds, tick scheme, and a free-form
  `info: Option<Params>`. **No trading-hours, session, calendar or timezone
  field.** The same holds across `crates/model/src/instruments/` (22 instrument
  modules) — none defines an hours field.
- A crate-wide search for `market_calendar|exchange_calendar|trading_hours|session_open|is_trading_hours`
  returns hits only in the Interactive Brokers adapter, the vendored `ibapi`
  dependency, and unrelated "session" words (WebSocket sessions, auth
  sessions). There is no `MarketCalendar`, `ExchangeHours` or equivalent type.
- The only place IB's `trading_hours` string is touched is
  `crates/adapters/interactive_brokers/src/providers/parse.rs:92-120`: it parses
  IB's `"20240411:0000-20240411:1800;..."` string **solely to recover a
  contract's last-trade time for `expiry`**, then discards it. The parsed
  window is never stored on the instrument. IB's only other hours-shaped
  surface is a boolean, `use_regular_trading_hours`
  (`crates/adapters/interactive_brokers/src/config.rs:94`; documented at
  `docs/integrations/ib.md:283` as "Restrict requests to regular trading hours").

**How Nautilus answers "is it open?" instead — an event stream, not a table.** [L]

- `InstrumentStatus` (`crates/model/src/data/status.rs:40-58`):
  `instrument_id`, `action: MarketStatusAction`, `ts_event`, `ts_init`,
  `reason`, `trading_event`, `is_trading`, `is_quoting`,
  `is_short_sell_restricted`.
- `MarketStatusAction` (`crates/model/src/enums.rs:999-1030`) has 16 variants:
  `None, PreOpen, PreCross, Quoting, Cross, Rotation, NewPriceIndication,
  Trading, Halt, Pause, Suspend, PreClose, Close, PostClose,
  ShortSellRestrictionChange, NotAvailableForTrading`. A separate coarse
  `MarketStatus` (`enums.rs:950-962`) has 6: `Open, Closed, Paused, Halted,
  Suspended, NotAvailable`.
- This is fed from the venue: Databento's `status` schema maps to
  `InstrumentStatus` (`docs/integrations/databento.md:103`), subscribed via
  `subscribe_instrument_status` (`:380-384`).

**Bar/session boundaries.** Time-bar aggregation is grid-based, not
session-based: `crates/data/src/aggregation.rs:1770,1809` expose
`time_bars_origin_offset: Option<SignedDuration>` and
`skip_first_non_full_bar: bool`, and `get_time_bar_start(now, &bar_type,
origin_offset)` (`:1880`) computes the window. There is no venue-day
intersection: a daily bar is a fixed 24h grid cell plus an operator-chosen
offset. [L]

**History / holidays / cross-zone / DST / evidence / maintenance:** not
applicable — none are modelled. There is no provenance mechanism because there
are no schedule facts.

**What it explicitly leaves out:** everything `exchange-hours-rs` does. This is
the single strongest prior-art datum for the review: the reference open-source
backtesting engine ships with *no* exchange calendar and has not needed one,
because it derives openness from the venue's own status feed and buckets bars
on a wall-clock grid.

### 1.2 globex-reference-catalog (local, `/Users/agedvagabond/Developer/globex-reference-catalog`)

**Granularity of hours modelling: none, and it does not even retain the join
key.** [L]

`InstrumentRow` (`crates/catalog-core/src/model.rs:368-432`) stores: `root`,
`raw_symbol`, `exchange` (MIC), `underlying`, `strategy_type`, `currency`,
`base_currency`, `kind`, `asset_class`, `option_kind`, `price_precision`,
`size_precision`, `activation_ns`, `expiration_ns`, `ts_event_ns`,
`ts_init_ns`, `price_increment`, `size_increment`, `multiplier`, `lot_size`,
`strike_price`, `maturity_year/month/day/week`, `source_publisher`,
`leg_start`, `leg_count`.

**Not stored: `group` (FIX 1151), `market_segment_id` (FIX 1300), any hours
field, any timezone.** A crate-wide grep for `trading_hours|TradingHours|1151|
security_group|SecurityGroup` returns zero schedule-related hits; every
`session` hit is a resolver cache session (`crates/catalog-core/src/archive.rs:1289-1360`).

This matters twice over: (a) the catalog is the "generated catalog that maps
instrument roots to `MarketHoursKey`" in the review's framing, yet it carries
no hours column *by design* — the mapping lives in SharurPlatform source, not
in the catalog; and (b) because `group`/`market_segment_id` are dropped at
generation time, the CME `(1300,1151)` join described in §1.4 cannot currently
be performed from the published artifact, only from raw DBN.

### 1.3 Databento instrument definitions (local: `dbn` 0.56.0 / 0.63.0 vendored in `~/.cargo/registry`)

**Does the definition record carry session/trading-hours data? No.** [L]

`InstrumentDefMsg` (`dbn-0.63.0/src/record.rs:655-903`) — full field sweep
performed. Temporal fields are exactly: `ts_recv` (`:663`), `expiration`
(`:680`), `activation` (`:687`), `decay_start_date`, `maturity_year`,
`maturity_month`, `maturity_day`, `maturity_week`. **There is no
`trading_hours`, `session`, `open_time`, `close_time`, `timezone` or
`schedule` field of any kind.**

What the record *does* carry that is schedule-adjacent:
- `group: [c_char; 21]` (`:822`) — "The security group code of the instrument"
  = CME FIX tag **1151**. This is one half of the CME schedule join key.
- `market_segment_id: u32` (`:749`) — "The market segment of the instrument"
  = CME FIX tag **1300**. The other half.
- `exchange: [c_char; 5]` (`:826`), `asset: [c_char; ASSET_CSTR_LEN]` (`:830`),
  `underlying_product: u8` (`:875`, "product complex"),
  `channel_id`, `appl_id`, `match_algorithm`, `security_update_action`.

Nautilus's Databento decoder
(`crates/adapters/databento/src/decode/instruments.rs`) reads
`asset`, `currency`, `min_price_increment`, `min_lot_size_round_lot`,
`unit_of_measure_qty`, `exchange`, `cfi`, `secsubtype`, `strike_price`,
`contract_multiplier`, `activation`, `expiration` — **and never reads `group`
or `market_segment_id`.** [L]

**Databento's own answer to "when is it open?" is a separate schema** — `status`
— delivered as timestamped events, not as a schedule
(`nautilus_trader/docs/integrations/databento.md:103`). [L] So the vendor
models session state exactly as Nautilus does: a stream, not a table, with no
history beyond what you have data for and no forward answer at all.

### 1.4 CME's own published session channels (evidenced from the local research store)

This is the most consequential prior art, because it is the operator's own
machine-readable output and it already keys on a field Databento delivers.

**(a) `TradingSessionList.dat` — the weekly Globex Market Schedule file.** [L]
Documented in
`/Users/agedvagabond/Developer/exchange-hours-research/catalog-artifacts/market-hours-profile-inventory.md`:

- Published Sunday, for the coming week, from
  `https://www.cmegroup.com/ftp/SBEFix/Production/`; format spec at CME's
  "CME Globex Market Schedule File Overview" wiki page (updated 2024-12-26).
- The 2026-08-30 file contains **1,364 security-group rows; 1,316 contain
  status 17 (`Ready to Trade`)**.
- Join key: Databento `(market_segment_id, group)` → CME `(tag 1300, tag 1151)`.
- Payload is raw FIX. Sample row content, verbatim from
  `catalog-artifacts/market-hours-electronic-envelope-candidates.tsv` field 11:
  `75=20260831|386=3|336=21|341=20260830210000000000|625=30|336=17|341=20260830220000000000|336=4|341=20260831210000000000|…`
  — i.e. per trade date (`75`), an ordered transition list of
  status (`336`) + start time (`341`, **UTC nanoseconds, DST already resolved**),
  with a sub-ID (`625`). Here: Pre-Open 21:00 UTC (16:00 CT Sunday), Ready
  22:00 UTC (17:00 CT), Close next day 21:00 UTC (16:00 CT) — the canonical
  Globex 17:00→16:00 envelope with its 16:00 CT pre-open.
- **What it explicitly does not publish:** the audit records it directly —
  "The schedule feed publishes Pre-Open, Ready, Halt, Not Available, Close and
  Post Close. It does **not** publish the Regular-versus-Extended
  classification used by `MarketHoursKey`, so an equal electronic envelope
  alone cannot prove two semantic profiles interchangeable."
- **No history.** It is a one-week snapshot. The audit's own caveat: the April
  definition keys and the August schedule are four months apart, and of 1,201
  audit roots found in the 2026-08-28 product sheet, **46 changed route and 1
  overlapped** — so even a four-month-stale join is measurably wrong for ~4% of
  roots.

**(b) `https://www.cmegroup.com/services/trading-hours-by-product?id=<N>&fromEventDate=&toEventDate=`** [L]
Per-day `preopen` / `open` / `closed` events with trade dates. Paged to
exhaustion 2026-09-07/08 it returned **3,243 products across 645 Globex product
groups** (`exchange-hours-research/cme-globex/shape-queue/event-contracts-UNBLOCK.md:63-64`).
Coverage gaps are real: zero products named "Event"; security groups
`VE/VB/VG/VS` absent entirely.

**(c) `https://refdata.api.cmegroup.com/refdata/v3/tradingSchedules`** — the one
CME feed that would carry the missing families — **returns `401 "api key or
token is invalid"`** and is therefore **out of scope under the repo's
`LAW-PUBLIC-SOURCES`**
(`exchange-hours-research/cme-globex/shape-queue/event-contracts-UNBLOCK.md:68`). [L]
This is a direct, documented cost of the current evidence law: the
authoritative machine channel is excluded by rule, forcing prose archaeology.

**(d) `ContractSpecs` / `ProductSlate`:** `https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/<N>`
and `/CmeWS/mvc/ProductSlate/V2/List` (3,251 products). These are the channels
that print hours **in session language**, including `TAS:` and `BTIC:` rows —
the only channel that distinguishes a trade-type window from its underlying's.
Retrieval is fragile: `cmegroup.com` "now returns `403` with *This IP address
is blocked…*" to curl on `/CmeWS/*`, `/services/*` and `.html`, PDFs still 200
(`event-contracts-UNBLOCK.md:60`). [L]

### 1.5 `exchange_calendars` (Python) [W]

Source examined: `README.md`, `exchange_calendars/exchange_calendar.py` (2,968
lines), `exchange_calendars/exchange_calendar_cmes.py` (113 lines), fetched
from `raw.githubusercontent.com/gerrymanoim/exchange_calendars/master/…`.

- **Granularity: venue, and only venue.** "A Python library for defining and
  querying calendars for security exchanges… more than 50 exchanges". Calendars
  are ISO MICs: `XNYS`, `XCBF`, `CMES`, `IEPA`, `XSES`… **CMES is one calendar
  for the entire CME Group.** There is no product-family key, no product key,
  and no trade-type concept anywhere in the API.
- **History: supported by the data structure, unused for CME.**
  `open_times`/`close_times` are `Sequence[tuple[pd.Timestamp | None, time]]`
  — "(start_date, open_time) where start_date: date from which open_time
  applies… None for first item"
  (`exchange_calendar.py:465-493`, `:520-546`). The docstring's own example
  shows five dated steps back to 1978. **`CMES` uses none of it:**
  `open_times = ((None, time(17)),)`, `close_times = ((None, time(16)),)`
  (`exchange_calendar_cmes.py:61-64`), with `open_offset = -1`. One envelope,
  no dated change, for all of CME Group, for all time.
- **Holidays and early closes: fully in scope, and are most of the content.**
  `regular_holidays`, `adhoc_holidays`, `special_closes`, `special_closes_adhoc`,
  `special_opens`. CMES declares only `USNewYearsDay, GoodFriday, Christmas` as
  full closures plus a 12:00 `special_closes` list of ten US holidays
  (`:71-113`). Its source comment is an explicit admission of the same
  granularity problem the review is about: *"The CME has different holiday rules
  depending on the type of instrument… Equity, Interest Rate, FX, Energy,
  Metals & DME Products close at 1200 CT on July 4, 2016, while Grain, Oilseed
  & MGEX Products and Livestock, Dairy & Lumber products are completely
  closed. For now, we will treat the CME as having a single calendar, and just
  go with the most conservative hours"* (`:72-81`). **They saw the split and
  declined it, in writing.**
- **Cross-zone / DST:** one `tz` per calendar (`ZoneInfo("America/Chicago")`);
  local times are localized per session; the `open_offset = -1` property is how
  an evening-open contract is expressed. A calendar whose boundary is anchored
  in a *different* zone from its own `tz` is not representable.
- **Evidence/provenance:** a URL in a module comment
  (`# https://www.cmegroup.com/trading-hours.html`, `:41-42`) and occasional
  inline links. **No ledger, no per-row citation, no review date, no
  verification status.**
- **Maintenance:** explicit and entirely community-driven. README FAQ:
  *"**All** of the exchange calendars are maintained by user contributions. If
  a calendar you care about needs revising, please open a PR - that's how this
  thing works!"* (`README.md:195`). CI is pre-commit + ruff. Calendars are
  version-stamped by the release they were added in (a "Version Added" column
  in the README table), not by a review date.
- **Explicitly out of scope, stated in the README (`:201`):** *"considers an
  exchange to be open only during periods of regular trading. During any
  pre-trading, post-trading or auction period the exchange is treated as
  closed. An exchange is also treated as closed during any observed lunch
  break."* So: **no extended session, no pre-open/order-entry phase, no
  auction, no maintenance state.** The state model is binary (open/closed) plus
  a break, against `exchange-hours-rs`'s six-state
  `SessionState {OpenRegular, OpenExtended, OrderEntry, Halt, Maintenance, Closed}`.

### 1.6 `pandas_market_calendars` (Python) [W]

Source examined: the `pandas_market_calendars/calendars/` listing via the
GitHub API (30 modules) plus `cme_globex_base.py`, `cme_globex_energy_and_metals.py`,
`cme_globex_agriculture.py`, `cme_market_times.py`.

- **Granularity: PRODUCT FAMILY — the closest prior art to `MarketHoursKey`.**
  Seven CME Globex modules: `cme_globex_agriculture.py`,
  `cme_globex_crypto.py`, `cme_globex_energy_and_metals.py`,
  `cme_globex_equities.py`, `cme_globex_fixed_income.py`, `cme_globex_fx.py`,
  over a shared `cme_globex_base.py`; plus a legacy `cme.py`, `eurex.py`,
  `eurex_fixed_income.py`, `ice.py`, `sifma.py`. Compare
  `exchange-hours-rs`'s eight Globex families actually consumed by
  SharurPlatform — the *same* cut of the market, arrived at independently.
- **Root→family mapping is inside the library, as an `aliases` list.**
  `CMEGlobexEnergyAndMetalsExchangeCalendar.aliases` is ~60 strings covering
  both descriptive names and bare roots: `"CL"`, `"HO"`, `"RB"`, `"MCL"`,
  `"NG"`, `"TTF"`, `"NN"`, `"CGO"`, `"NGO"`, `"GEO"`, `"GC"`, `"SI"`, `"PL"`,
  `"HG"`, `"ALI"`, `"QC"`, `"HRC"`, `"BUS"`, `"TIO"`
  (`cme_globex_energy_and_metals.py:94-155`). This is the *opposite* of
  `exchange-hours-rs`'s stance ("The crate performs no symbol-to-family
  mapping", `docs/schedules/unsupported-families.md:192`) and of
  SharurPlatform's, which authors the map in `domain::globex_products`.
- **History: same `(date|None, time)` mechanism, again unused for CME.**
  `regular_market_times = {"market_open": ((None, time(17), -1),),
  "market_close": ((None, time(16)),)}` (`cme_globex_energy_and_metals.py:159-162`)
  — the third tuple element is the day offset. Grains:
  `{"market_open": ((None, time(19), -1),), "market_close": ((None, time(13,20)),),
  "break_start": ((None, time(7,45)),), "break_end": ((None, time(8,30)),)}`
  (`cme_market_times.py:4-9`). **Not one dated change in any CME module.**
  (Note: this is the *current* standard-grains grid, identical to what
  `exchange-hours-rs` models — but with none of its 2012/2015/2022 history and
  no mini-grain divergence.)
- **Holidays: in scope, with dated variants.** `special_closes` carries three
  tiers for energy/metals — `time(12)` for the pre-2022 holiday set,
  `time(12,45)` for Friday-after-Thanksgiving, `time(13,30)` for the
  from-2022 set — using explicitly dated holiday objects
  (`USMartinLutherKingJrPre2022` vs `…From2022`, etc.)
  (`cme_globex_energy_and_metals.py:184-222`). Plus
  `special_closes_adhoc = [(time(15,15), ["2010-12-31"])]` (`:225-230`) — a
  single-date, single-time override. That one line is precisely the case
  `exchange-hours-rs` forbids from a profile under `LAW-HOLIDAY-SCOPE` and
  routes to the caller's `DayPolicy`.
- **Cross-zone / DST:** one `tz` per calendar; day offsets for evening opens;
  no foreign-zone anchoring.
- **Evidence:** URL comments in docstrings (e.g. *"Sample GLOBEX Trading Times
  https://…light-sweet-crude.contractSpecs.html — Sunday - Friday: 5:00pm -
  4:00 pm CT"*, `cme_globex_energy_and_metals.py:86-90`). No ledger, no review
  dates, no basis grading. Commented-out code left in place
  (`# @property def adhoc_holidays…`, `:181-183`).
- **Explicitly out of scope, stated in docstrings:** *"NOT IMPLEMENTED: Dubai
  Mercantile Exchange (DME) follows this schedule but with holiday
  exceptions"* (`:54`). Also absent: pre-open/order-entry phases, Regular vs
  Extended, **and every trade-type shape** — no TAS, TAM, BTIC, TACO or TMAC
  calendar exists in the library.

### 1.7 QuantLib calendars (C++) [W]

Source examined: `ql/time/calendars/unitedstates.hpp` (212 lines), fetched.

- **Granularity: a *calendar purpose* within a country, not a venue and not a
  product.** `UnitedStates::Market = { Settlement, NYSE, GovernmentBond, NERC,
  LiborImpact, FederalReserve, SOFR }` (`unitedstates.hpp:197-204`). The cut is
  by what the dates are *used for* (settlement, bond accrual, a fixing), not by
  where something trades.
- **No intraday times at all.** The `Calendar` interface is
  `isBusinessDay / isHoliday / isWeekend / isEndOfMonth / adjust / advance /
  businessDaysBetween` plus `addHoliday`/`removeHoliday`. [M — interface names
  from memory; the header fetched here only shows the `Market` enum and the
  holiday prose.] A QuantLib calendar cannot answer "is the market open now".
- **History: as dated holiday *rules*.** The header's prose carries the
  conditions inline: MLK "since 1983" for Settlement but "since 1998" for
  NYSE; "Presidential election day, first Tuesday in November of election
  years (**until 1980**)"; "Special historic closings (see
  nyse.com/pdfs/closings.pdf)" (`:43-89`). So history lives as `if (year >= N)`
  branches in `isBusinessDay`, back to the 19th century for NYSE.
- **Holidays: the entire content.** There is nothing else.
- **Cross-zone/DST:** not applicable — dates only, no times, no zones.
- **Evidence:** URLs in the class docstring (opm.gov, nyse.com, theice.com,
  bondmarkets.com). No per-date citation, no ledger.
- **Maintenance:** contributor PRs against the QuantLib repo; regression tests
  assert known holiday lists year by year. [M]
- **Explicitly out of scope:** sessions, times, trade types, extended hours.

### 1.8 QuantConnect LEAN `MarketHoursDatabase` [M — NOT VERIFIED IN THIS PASS]

A sparse checkout exists at
`<scratchpad>/lean` but `Data/market-hours/` and `Common/Securities/*.cs` are
**empty** (0 `.cs` files present), so nothing below was confirmed here. Flagged
because it is the closest architectural analogue to `exchange-hours-rs` and
worth a verified pass if the review leans on it.

From memory: LEAN ships `Data/market-hours/market-hours-database.json`, a single
JSON file keyed by `"<securityType>-<market>-<symbol>"` with a
`"[type]-[market]-[*]"` wildcard row per (security type, market) and explicit
per-symbol rows overriding it — i.e. **a two-level key with a documented
fallback**, exactly the shape SharurPlatform's `SessionHoursBasis` ladder
describes. Each entry carries `dataTimeZone`, `exchangeTimeZone`, a
`monday..sunday` array of segments each tagged `preMarket` / `market` /
`postMarket`, a `holidays` list of dates, an `earlyCloses` map (date → time),
a `lateOpens` map, and a `bankHolidays` list. Provenance: none per row.
Maintenance: PRs to the `Lean` repo plus a data-vendor refresh; no citations.
History: **no dated revisions of the recurring week** — the JSON describes the
present, with holidays/early closes as an ever-growing date list. The
CME futures rows are per-root where they differ, which means LEAN *does* carry
per-product rows without carrying per-product history.

### 1.9 Bloomberg / Refinitiv-style session tables [M — NOT VERIFIED]

No local artifact. From memory, for shape only:
- **Bloomberg** exposes exchange-level session metadata through `DSCO`/`XLTP`
  and field-level items (`TRADING_DAY_START_TIME_EOD`,
  `TRADING_DAY_END_TIME_EOD`, `EXCH_MARKET_STATUS`, session-phase fields).
  Granularity is exchange × security-type, with per-contract overrides pushed
  through the contract's own DES page. History is not queryable as a schedule
  — you get today's table; prior sessions are inferred from data.
- **Refinitiv/LSEG** ships a "Trading Session" / calendar reference product
  (formerly Exchange Trading Calendars, and the `ExchangeCode`-keyed session
  tables in DSS) with venue + instrument-class granularity, holiday and
  half-day calendars several years forward, and dated effective ranges on
  session rows. Provenance is vendor assertion; the value proposition is a
  paid SLA, not citations.
- The generalizable point: **commercial vendors sell the maintenance, not the
  evidence.** Nobody publishes a per-row citation ledger. The closest public
  analogue to a citation ledger is what `exchange-hours-rs` built itself.

### 1.10 Side-by-side

| | granularity | history of the recurring week | holidays / early closes | cross-zone & DST | evidence recorded | maintained by | notable exclusions |
|---|---|---|---|---|---|---|---|
| **exchange-hours-rs** | venue (96 `Exchange`) **+** product family (36 `MarketHoursKey`), incl. 5 trade-type keys | **154 dated revision rows**, floor Jan-2010, `select_revision` by local date | **out of scope by law** (`LAW-HOLIDAY-SCOPE`), delegated to caller `DayPolicy` | one `tz` per profile; cross-zone via two profiles + `reference_delta_seconds` | per-row ledger, 130 rows, Primary/Partial + gap-kind + `Reviewed on` | one maintainer + agents; PR-per-family | holidays, expiry, symbol→family mapping |
| NautilusTrader | — (no calendar) | — | — | — | — | core team | all of it; uses `InstrumentStatus` stream |
| globex-reference-catalog | — (no hours; drops `group`) | — | — | — | build manifests + SHA-256 | one maintainer | hours, security group |
| Databento DBN defs | — (no hours field) | — | — | — | — | vendor | sessions; sold as `status` schema |
| CME `TradingSessionList.dat` | **security group** (1,364 rows) | **none — one week** | holidays appear as that week's actual transitions | times in **UTC ns**, DST pre-resolved | operator primary | CME, weekly | Regular vs Extended |
| CME `trading-hours-by-product` | product (3,243 across 645 groups) | queryable date range | yes, as events | per-product | operator primary | CME | 645 groups ≠ all groups (event contracts absent) |
| `exchange_calendars` | **venue only** (50+, `CMES` = all of CME) | `(date,time)` tuples supported; **CMES uses none** | **in scope**, `special_closes` + adhoc | one tz/calendar, `open_offset` | URL comments | **community PRs** | extended hours, pre-open, auctions, all trade types |
| `pandas_market_calendars` | **product family** (7 CME modules) + root aliases | same mechanism; **no CME dated change** | **in scope**, dated holiday variants + `special_closes_adhoc` | one tz/calendar, day offsets | URL comments | community PRs | DME, pre-open, Reg/Ext, all trade types |
| QuantLib | country × calendar purpose | dated rules inside `isBusinessDay`, to 1800s | **the entire content** | n/a (dates only) | URL in class doc | community PRs | all intraday |
| LEAN [M] | (type, market) wildcard + per-symbol override | none for the week; dates accrete | in scope: `holidays`, `earlyCloses`, `lateOpens` | `dataTimeZone` + `exchangeTimeZone` | none | QC + PRs | citations, dated grid revisions |
| Bloomberg / LSEG [M] | exchange × class (+ contract override) | vendor-internal | in scope, forward-published | yes | vendor assertion | vendor SLA | public citations |

**Three observations the table makes unavoidable:**
1. **No public system models a trade-type dimension.** Not one. TAS/BTIC/TAM/
   TACO/TMAC hours appear nowhere in `exchange_calendars`,
   `pandas_market_calendars`, QuantLib, LEAN or Nautilus. The 32-key plan is
   without prior art anywhere in open source.
2. **Everyone who models hours also models holidays.** `exchange-hours-rs` is
   alone in excluding them, and alone in carrying an evidence ledger.
3. **Dated revision history of the recurring week is the rarest feature.**
   Two libraries provide the *mechanism* and neither uses it for CME.
   `exchange-hours-rs`'s 154 revision rows are, as far as this pass could
   establish, the only such corpus in public code.

---

## 2. The trade-type question: five design options

### What the existing work has already established (load-bearing for all five)

**(a) Every TAS envelope is arithmetically {underlying's open} + {end of that
asset class's settlement determination range}.** [L] Verified in code, not just
in prose:

| key | `days` | `open_ssm` | `close_ssm` | source file |
|---|---|---|---|---|
| `globex_gold_tas` | `SUN_PLUS_MON_THU` | `17*3600` (17:00 CT) | `12*3600+30*60` (12:30 CT) | `src/calendar/schedules/futures/us/metals_tas.rs:193-197` |
| `globex_silver_tas` | `SUN_PLUS_MON_THU` | `17*3600` | `12*3600+25*60` | `:198-202` |
| `globex_copper_tas` | `SUN_PLUS_MON_THU` | `17*3600` | `12*3600` | `:203-207` |
| underlying `globex_energy` | — | `17*3600` | `16*3600+15*60` then `16*3600` | `src/calendar/schedules/futures/us/energy_metals.rs:75-81` |

The open and the day-mask are byte-identical to the underlying; only
`close_ssm` differs, and it equals the published settlement range end
(Gold `13:29:00-13:30:00 ET` = 12:30 CT; Silver `13:24:00-13:25:00 ET`;
Copper `12:59:00-13:00:00 ET` — the handoff matches these **six-for-six in the
metals/Treasury group and four-for-four in energy/ag**,
`docs/plans/2026-09-05-cme-trade-type-handoff.md:185`).

**(b) The derivation is *causal*, not coincidental — and the livestock case
proves it.** The handoff states it directly (`:220`): *"Every TAS envelope
decomposes as {underlying's open} + {end of that asset class's settlement
determination range}, and the livestock case proves the derivation (TAS
inherited the underlying's open change in 2015/2016 and kept the settlement
close)."* The open-side revision the livestock TAS grid inherited is
`"Monday, 9:05 a.m. – 1 p.m. / Tuesday – Friday, 8 a.m. – 1 p.m."` →
`"Monday - Friday 8:30 a.m. - 1:00 p.m. CT"`, whose effective day is itself
**still undated**, bracketed only by two fact-card creation dates
2015-06-11 … 2016-03-04 (handoff `:87`, unresolved item **U-14** at `:168`).

**(c) The counter-argument the repo already made.** Handoff `:220`: *"A reviewer
can fairly say the crate is minting ~13 keys whose content is a formula. The
answer is that the crate answers 'is this identity tradeable at instant t': at
14:00 CT a `CL` holder is trading and a `CLT` holder is not — group 80:CT is
closed 13:30–16:45 CT and then runs a full Pre-Open/Ready cycle, which a fixing
inside a session never produces."* And handoff `:215` quantifies it:
grain TAS 13:15 vs grains 13:20; livestock TAS 13:00 vs 13:05; energy TAS 13:30
vs 16:00; gold TAS 12:30 vs COMEX 16:00; crypto TAS 15:00 vs crypto 16:00 —
**executable-window differences of 5 minutes to 4 hours.**

**(d) CME's own granularity is six, not thirteen.** Handoff `:222`: the TAS
eligibility workbook `/trading/files/tas-tam-eligibility.xlsx` has *exactly six
tabs* — Cryptocurrency TAS / Energy TAS / Grain and Oilseed TAS / Livestock TAS
/ Metals TAS / Treasury TAS — and its single "Energy TAS" sheet covers `CLT`,
`MCT`, `NGT`, `HHT`, `7FT`, `TAS`, `TTS` together, where the plan proposes
three keys. [L]

**(e) The scale.** Plan: **32 new keys across 13 PRs, 6 keys blocked, 3 groups
rejected** (`docs/plans/2026-09-12-cme-trade-type-keys.md:31-33, 85-99,
131-146, 155-162`). Five already landed (`GlobexGoldTas`, `GlobexSilverTas`,
`GlobexCopperTas`, `GlobexPlatinumTas`, `GlobexPalladiumTas` — `5530f22`),
bringing `MarketHoursKey` from 31 to **36**. The full 32 would take it to ~63.
[L]

**(f) The consumer does not use any of it.** SharurPlatform's authored table
`crates/domain/src/globex_products.rs` maps **104 roots to exactly 8 distinct
keys** — `GlobexCryptocurrency` (21), `GlobexEnergy` (20),
`GlobexInterestRates` (18), `GlobexFx` (17), `GlobexGrains` (12),
`GlobexEquityIndex` (11), `GlobexLivestock` (4), `GlobexNikkei225Dollar` (1).
**Zero TAS, BTIC, TAM, TACO or TMAC roots appear.** Nor do
`GlobexMiniGrains`, `GlobexRoughRice`, `GlobexWeather`, `GlobexSpotQuoted`,
`GlobexEventContracts`, `GlobexEventContractsBtc` or any of the five SGX keys.
**28 of the crate's 36 keys have no consumer in SharurPlatform today.** [L]

**(g) The catalog scale the keys are aimed at.** The GLBX.MDP3 audit found
**1,342 distinct future roots emitted on the listing-exchange fallback**
(`catalog-artifacts/audit.md`), across **41 exact current transition
signatures** of which 37 are new shapes; the largest single signature is
**1,146 roots sharing the 17:00–16:00 CT envelope** across 184 security groups
(`catalog-artifacts/market-hours-profile-inventory.md`). The 32-key plan covers
signatures 2, 3, 6–41 — roughly **225 roots**. It leaves ~1,120 roots (the
semantic split of signature 1) untouched. [L]

---

### Option (i) — own key per variant (the current plan)

*One `MarketHoursKey` per trade-type family per asset class:
`globex_gold_tas`, `globex_equity_index_btic`, `globex_energy_tam_london`, …*

**Cost.**
- 32 new enum rows. Per the plan's own "registration surface" checklist
  (`2026-09-12-cme-trade-type-keys.md:165-181`), **each key touches 14
  places**: the `market_hours_keys!` row; the `hours_for_market_hours_key` arm;
  the date-aware `calendar_for_market_hours_key` surface with tests both sides
  of the opening day; the `session_profile` arm + `FuturesSessionProfile`
  static; module `pub(crate) use` re-exports; `EXPECTED_MARKET_HOURS_KEY_NAMES`
  (array length bump); `EXPECTED_MARKET_HOURS_KEYS`; `SUPPORTED_FAMILY_NAMES`;
  the ledger row; `CHANGELOG.md`; README counts **and prose**; the regenerated
  golden file; a new submodule under `tests/futures_family_boundaries/`.
- The plan explicitly predicts serialized, conflicting merges: *"each merge
  breaks the next one's mergeability. That is expected: land one, rebase the
  rest"* (`:205-210`), and cites two historical count-conflict incidents
  (#51 and #49) where *"both branches were internally right"*.
- 13 sequenced PRs; **5 of 13 currently blocked** on four open issues
  (#71, #72, #76, #77), two of which the plan explicitly refers to the
  maintainer as **law edits to `AGENTS.md`** (D-3, D-4 — `:118-130`).
- Ledger growth: 130 rows → ~162, each needing an independent `Reviewed on`
  advance at every future cutoff.
- Calibration from the nearest completed comparable: **the five SGX keys took
  1,861 lines of Rust across 6 files, 19 revision rows, 4 PRs (#67, #68, #69 +
  a floor follow-on), 417 research files and 101 MB of retrieved evidence** —
  and left an open follow-on. [L]

**Accuracy.** Highest available. Every key can carry its own history, its own
`regular: &[]` justification with the specific channels behind it, and its own
cross-zone profile pair. It is the only option under which `session_state(t)`
distinguishes `CLT`'s 13:30–16:45 CT closure from `CL` trading through it, and
the only one that can represent a TAS grid diverging from its underlying in the
future without a schema change.

**Failure modes.**
1. **Prose-count fragility, already realized twice.** Finding 5 of STATUS.md:
   *"Narrative counts drift silently. Two consecutive key additions shipped
   stale prose."* PR 1 of the plan exists solely to convert that into a red
   test.
2. **Blocked-key inflation.** 6 of 38 names are "blocked, not rejected" — they
   sit in `docs/schedules/unsupported-families.md:181-186` as prose the reader
   must consult, i.e. the key namespace acquires a third state (registered /
   blocked / absent) that consumers cannot query.
3. **Granularity disputed by the operator's own artifact.** CME says six TAS
   families (§2(d)); the plan says ten. D-2 (`:111-114`) resolves this "on
   family semantics and history rather than on the envelope" — a judgement, not
   a source. Rows 10 and 22 (CLT/HOT/RBT/BZT/BBT vs NGT/NNT) were kept as one
   key because *"they differ only by a Pre-Open second the crate does not
   encode"* — which is the merge argument applied inconsistently one level up.
4. **Evidence channel is degrading under it.** The plan's own residual risk
   (`:222-228`): *"`cmegroup.com` returns 403 at IP level to this machine, so
   much of the evidence was read as extracted text through a public reader."*
   32 keys is 32 more rows resting on the weakest channel the repo has.
5. **Consumer gap.** Per §2(f), no SharurPlatform instrument resolves to any
   of these keys today. The plan ships a public API surface with no caller.

---

### Option (ii) — a variant dimension on an existing key (base key + close override + pre-open)

*`MarketHoursKey` stays at family granularity; a second, small type names the
trade type. E.g. `hours_for(key: MarketHoursKey, variant: TradeVariant)` where
`TradeVariant ∈ {Outright, Tas, Tam(Zone), Btic(Zone), Taco, Tmac}`, and the
variant supplies `{close_ssm override, own order_entry rules, own day-mask
tweak}` applied over the base key's dated profile.*

**Cost.**
- One new enum (~6–10 variants) + one override table. The override table is
  ~32 rows of `(base_key, variant, era) → (close_ssm, order_entry)` — the same
  facts as option (i), but **without** 32×14 registration sites, 32 ledger
  rows, 32 test submodules, 32 README prose edits, or the 13-PR rebase chain.
- Real new cost: a second dimension on every API entry point
  (`hours_for_market_hours_key`, `calendar_for_market_hours_key`,
  `session_profile`, serde, `FromStr`, `ALL`) — i.e. a **breaking API change**,
  and a decision about the wire form (`"globex_gold"` + `"tas"` vs
  `"globex_gold_tas"`). Serde compatibility is explicitly called out as a
  breaking persisted-wire concern for key renames
  (`src/calendar/futures_profile.rs:125-128`).
- The composition rule must be *sourced as a rule*, not derived: "the TAS grid
  inherits the underlying's open and day-mask, and overrides only the close"
  is currently an observation across 5 keys, not a CME statement. Under
  `LAW-PRIMARY-SOURCES` it would need to be recorded as a **convention** — the
  precedent exists (D-7(a) records CVB's regular/extended split "as a
  convention rather than a source", plan `:138-142`).

**Accuracy.** Equal to (i) *where the composition rule holds*, and the evidence
says it holds broadly: identical `days` and `open_ssm` in all five landed TAS
keys [L], and the livestock inheritance is direct evidence that the rule is
causal (§2(b)).

**Failure modes.**
1. **The rule is not universal, and the counterexamples are already known.**
   `globex_nikkei_btic` has a **second daily window** its underlying does not:
   *"BTIC: Sunday - Friday 6:00 p.m. ET - 3:30 p.m. Tokyo time … **and Monday -
   Friday Noon to 5:00 p.m. ET**"* while TOPIX BTIC has *"no midday clause"*
   (handoff `:1.1`, NIT/NKT and TPB/TPT rows). `globex_fx_btic_euro` has a
   **mid-session trading close** 3:40–4:30 p.m. London plus the 60-minute
   break. The crypto BTIC shapes are *"the 24/7 grid plus one 5-minute
   reference-rate stop"* — a hole, not a close. A close-override model cannot
   express any of these; the type would need `Vec<SessionRule>` overrides,
   at which point it is a profile, and the saving evaporates.
2. **Era misalignment.** Energy TAS has **two eras** on RA1104-4 (plan D-5,
   `:132-134`); TACO has two eras; the underlying `globex_energy` has its own
   (2015 COMEX/NYMEX close change). A variant dimension must answer "which era
   of the base, crossed with which era of the override" — a cartesian product
   the current flat `revisions![]` timeline expresses cleanly and a two-layer
   model does not.
3. **`regular: &[]` is a per-shape fact, not a variant fact.** The plan requires
   *"each module comment naming **the channels its own empty `regular` rests
   on**. They differ per shape"* (`:184-186`), and names one shape
   (`globex_equity_index_btic_plus_taco_plus`) that Rule 524 does not reach. A
   shared variant row cannot carry per-shape provenance.
4. **Cross-zone interacts badly.** D-1 (`:104-110`) adopts two
   `StaticHoursProfile`s per key selected by `reference_delta_seconds`, scoped
   to *"the ten shapes carrying CME's Friday-16:00/Sunday-17:00 CT weekly
   close"* and explicitly *"not exact for the two 24/7 crypto BTIC shapes"*. A
   variant override would have to carry its own profile pair — again, a profile.

**Net:** (ii) is cheap and accurate for the **10 TAS shapes** (where the
inheritance is verified) and breaks on the **13 BTIC/TAM/TACO/TMAC shapes**.
A hybrid — variant dimension for TAS only, own keys for the rest — is the
option the evidence actually supports, and is not one of the five named.

---

### Option (iii) — unmodelled; catalog maps variants to the underlying with a flag

*`CLT` → `MarketHoursKey::GlobexEnergy` + `is_trade_type_variant: true`.
The crate models the underlying; the consumer knows the answer is approximate.*

**Cost.** Near zero in the crate — literally one doc sentence per family plus
whatever flag the consumer chooses. SharurPlatform already has the exact
machinery: `Instrument::session_hours_basis()` returns a typed
`SessionHoursBasis` distinguishing an exact `ProductFamily`, an intentionally
`Exchange`-keyed shape, and an *"explicitly approximate `ExchangeFallback`"*,
and the chart *"marks that stream `HOURS≈`"*
(`SharurPlatform/AGENTS.md:136-145`). The operator ruling is already on the
record: *"Minor per-symbol hours inaccuracy is accepted and disclosed
(operator ruling 2026-09-05); silent inaccuracy is not."* (`AGENTS.md:159-160`).
Adding a fourth basis — "underlying's family, variant not modelled" — is a
one-variant change in the consumer.

**Accuracy.** Wrong by a known, bounded, *published* amount: **5 minutes to
4 hours** (handoff `:215`). Specifically:

| shape | modelled close (underlying) | true close | error |
|---|---|---|---|
| grain TAS | 13:20 CT | 13:15 CT | 5 min |
| livestock TAS | 13:05 CT | 13:00 CT | 5 min |
| crypto TAS | 16:00 CT | 15:00 CT | 1 h |
| metals TAS (gold) | 16:00 CT | 12:30 CT | 3.5 h |
| energy TAS | 16:00 CT | 13:30 CT | 4.5 h |

**Failure modes.**
1. **The error is one-sided and it is the dangerous side.** The crate reports
   *open* during a window the instrument is *closed* — never the reverse. A
   backtest fills a `CLT` order at 14:00 CT that could not have existed; a live
   UI shows a countdown to a close that already happened 4.5 hours ago; a bar
   consolidator emits a session-final candle at the wrong instant.
2. **It hides a genuine full re-open cycle.** Handoff `:220`: group 80:CT is
   *"closed 13:30–16:45 CT and then runs a full Pre-Open/Ready cycle"*. Under
   (iii) the crate reports one continuous session where the venue runs two,
   which means `session_close_containing` and `next_session_open_after` — two
   of the five operations SharurPlatform's `SessionCalendar` trait exposes —
   return values that are not merely imprecise but structurally wrong.
3. **The flag must be believed.** It relies on every downstream consumer
   checking a boolean. SharurPlatform's design already assumes this and enforces
   it typefully, so the risk here is low *for this consumer* and unbounded for
   any other.

**Where this option is strongest:** the two 5-minute cases (grain TAS,
livestock TAS) are indistinguishable from tick-timestamp jitter at any bar
resolution ≥1 minute. Where weakest: the 3.5–4.5-hour metals/energy cases.
A cost/benefit split on the size of the error is available and is not currently
part of the plan's decision rule.

---

### Option (iv) — unmodelled; catalog marks them non-tradeable / out of scope

*The consumer's catalog refuses to bind `CLT`, `GCT`, `EST`, … at all.*

**Cost.** Zero in the crate. But the consumer's own law forbids it:
*"A root the table does not cover is reported at RUNTIME by the adapter that
needed it… there is no admission exclusion list, because the supplying
provider's own listing is the scope, and **absent hours evidence is never a
reason to refuse an instrument**"* (`SharurPlatform/AGENTS.md:150-154`), and
`PAT-DEFINITION`: *"There is no pre-generated artifact, no reference-catalog key
and no membership gate: a venue result the provider can define BINDS"*
(`:587-590`). So (iv) is not merely a policy the consumer would dislike — it
**contradicts two stated consumer laws** and would require changing them first.

**Accuracy.** Perfect (nothing is asserted) at the cost of coverage. The crate
already has a precedent surface for this: `docs/schedules/unsupported-families.md`
records three rejected groups on evidence (Treasury TAS `TNT/UBT/ZBT/ZFT/ZNS/ZTT`,
Dutch TTF TAS `TAS/TTS`, commodity-index BTIC `AWT/BAT/BET/BGT/BLT/BMT/BPT/BST/CCT`)
and six blocked names (`:76-79`, `:181-186`), and states the boundary: *"The
crate performs no symbol-to-family mapping; refusing an unsupported product
belongs in the caller's instrument catalog."* (`:192-193`).

**Failure modes.**
1. **Scale.** Applied consistently it excludes ~225 trade-type roots *plus* the
   1,120-root residue of signature 1 — i.e. it is indistinguishable from (iii)
   without the flag, unless the consumer really refuses to display them.
2. **It converts an accuracy problem into an availability problem**, which for
   a trading UI is usually worse: an operator who can see `CL` but not `CLT`
   concludes the platform is broken, not conservative.
3. **It is unstable under growth.** Every newly-listed trade-type root becomes
   an instrument the platform silently cannot show, discovered by a user.

### Option (v) — a generic "settlement-window close" derived from the underlying

*No trade-type keys and no per-shape data. Instead the crate exposes, per
family, the asset class's settlement determination range end, and a caller
asking for a TAS variant gets {underlying's open, day-mask} + {settlement
range end} computed.*

**Cost.** One new small table: ~10 asset-class rows. The data already exists
and is already cited — CME's *"Daily Settlement Time Details"*, which the
handoff quotes verbatim per class (`:185`): *Livestock `12:59:30-13:00:00 CT`,
Grains/Oilseeds `13:14:00-13:15:00 CT`, Energy `14:28:00-14:30:00 ET`,
Bitcoin `14:59:00-15:00:00 CT`, Gold `13:29:00-13:30:00 ET`, Silver
`13:24:00-13:25:00 ET`, Platinum `13:03:00-13:05:00 ET`, Copper
`12:59:00-13:00:00 ET`, Palladium `12:58:00-13:00:00 ET`, Treasuries
`13:59:30-14:00:00 CT`.* That is **one document, ten rows, covering every TAS
shape in the plan** — against ten separately-sourced keys with ~10 ledger rows
and ~10 histories.

**Accuracy.** Matches the observed closes **six-for-six in the metals/Treasury
group and four-for-four in energy/ag** (handoff `:185`) — i.e. **10 for 10** on
everything checked. For TAS, this is the highest accuracy-per-unit-cost of any
option.

**Failure modes — and these are fatal under the current law.**
1. **It is exactly what `LAW-SESSION-NOT-EXPIRY` forbids.**
   `AGENTS.md:74-90`: *"an instrument's termination of trading, expiration,
   **settlement**, marker or fixing instant is **never** a session boundary,
   and this crate does not model it at any resolution."* Option (v) makes a
   settlement instant *the* session boundary by construction. It cannot be
   adopted without rewriting that law — the law would have to become something
   like "a settlement instant is not a session boundary *for the outright*, but
   **is** the published close for a trade-type book of that class, when CME
   states it in session language for at least one member."
2. **The coincidence is explicitly declared to prove nothing.**
   `AGENTS.md:87-90`: *"Every trade-type shape surveyed … closes at an instant
   that is also a settlement or fixing instant for its asset class, so the
   coincidence proves nothing on its own."* Option (v) is the bet that the
   coincidence *does* prove something — a bet the evidence supports (10/10) and
   the law forbids.
3. **It covers TAS and nothing else.** BTIC closes at an *index close* (16:00
   ET / 15:00 CT), TACO at an *opening auction*, TAM at a *foreign fixing*
   (London 16:30, Singapore, Shanghai, Tokyo 15:30). Those are different
   reference series with different publishers; a single "settlement range end"
   table does not reach them. So (v) is at best a partial substitution:
   ~10 of 32 keys.
4. **It loses history.** The settlement range end is a *current* table. The
   livestock TAS open-side revision (§2(b), undated, U-14) and the energy TAS
   two-era split (D-5) are open-side and era-side facts a close-derivation
   model has no place for. It would have to be combined with (ii) to be
   complete, at which point it is (ii) with a cheaper close source.
5. **Two known counterexamples to the derivation itself.** `MCT` is mapped
   *"on published-group identity, sourced on `BZT`"* rather than on its own
   statement (D-6, plan `:135-137`) — a membership question a formula cannot
   answer. And Treasury TAS was **rejected** precisely because its 14:00 CT
   close *"is feed-only and equals CME's stated Treasuries settlement range end
   `13:59:30-14:00:00 CT`"* (handoff `:80`) — i.e. under the current law the
   formula matching is the *reason to refuse*, not the reason to accept.

### Option comparison

| | crate cost | consumer cost | accuracy | worst failure | blocked by |
|---|---|---|---|---|---|
| (i) own key | 32 keys × 14 sites, 13 PRs, +32 ledger rows, 5 PRs blocked | ~225 root→key rows to author | exact | prose/count drift; namespace with 3 states; no caller today | 4 open issues, 2 needing law edits |
| (ii) variant dimension | 1 enum + ~32 override rows; **breaking API** | 1 extra field at the call site | exact for TAS; **cannot express** Nikkei BTIC's 2nd window, FX BTIC's mid-close, crypto BTIC's 5-min hole | era cartesian product; per-shape `regular: &[]` provenance lost | needs a recorded composition convention |
| (iii) flag on underlying | ~0 | 1 basis variant (machinery exists) | wrong by 5 min – 4.5 h, always "open when closed" | hides a full Pre-Open/Ready re-open cycle; `session_close`/`next_open` structurally wrong | nothing |
| (iv) refuse | 0 | contradicts 2 consumer laws | perfect or absent | availability failure; unstable under new listings | `AGENTS.md:150-154`, `:587-590` |
| (v) derived settlement close | ~10 rows, one document | 0 | **10/10 observed**, TAS only | forbidden by `LAW-SESSION-NOT-EXPIRY`; no reach to BTIC/TAM/TACO; no history | `AGENTS.md:74-90` |

---

## 3. History depth: three models

### (A) Blanket January-2010 floor (current)

`AGENTS.md:49-50`: *"Amendment history is recorded back to **January 2010**;
earlier changes are out of scope by design."*
Below-floor behaviour, `AGENTS.md:171-195`: *"Below the January-2010 floor, the
earliest sourced profile stands"*; *"Carry the earliest sourced state back to
the audit floor."* Worked example at `:207-208`: energy/metals *"16:15 at the
floor and 16:00 currently, so 16:15-17:00 is carried from the floor with no
cutover asserted."*

- **Cost:** the floor is uniform, so a venue whose documents begin in 2016 must
  either carry a state back six years on a convention, or be labelled Partial.
  **22 of 57 Partial rows are "executable"** — the gap touches a window where
  trades print — and the ledger names the cause for most of them as exactly
  this: the six ICE Futures U.S. keys (*"pre-August-2011 grid is carried back,
  bounded by document availability"*), `globex_nikkei_225_dollar`
  (*"sessionless before its grid's first sourced appearance"*), the five SGX
  keys (*"a sourced intersection, sessionless before the first surviving
  calendar edition"*) — `docs/schedules/verification.md:56-62`. [L]
- **Accuracy:** high where documents exist; **fabricated-by-convention** where
  they do not (the carry-back is the crate's own rule, not a source).
- **Failure mode:** the floor is a constant against a variable — document
  survival. It manufactures work in exactly the venues where evidence is
  thinnest, and it is the single largest driver of the Partial population.

### (B) Per-venue data horizon

*Each venue/key declares the earliest date at which its evidence begins, and
answers `Unknown`/refuses below it. No carry-back.*

- **Cost:** one `horizon: NaiveDate` field per profile timeline + one new
  answer state at the API boundary. The consumer's `SessionCalendar` trait
  already returns `Option` on three of five operations
  (`SharurPlatform/crates/domain/src/data/calendar/mod.rs:120,150,225`) and
  already documents `None` as *"no clamp boundary applies"* / *"A countdown
  with no target shows nothing rather than a fabricated time"* — so a
  below-horizon `None` is expressible without an API change. `is_open` and
  `session_state` would need a decision (default `Closed`? a new
  `SessionState::Unknown`?).
- **Accuracy:** strictly higher than (A) — it removes every carry-back
  convention and therefore every executable Partial caused by one. It would
  convert most of the 22 executable-gap rows into either Primary-above-horizon
  or an explicit refusal.
- **Failure mode:** a backtest starting before a venue's horizon silently
  loses bars, or crashes, depending on the `None` policy. Callers must handle a
  third answer. And "the horizon" is itself a judgement about what counts as
  the earliest *sufficient* document.

### (C) Current + dated changes only since a stated date

*No floor at all. Model today's week; record every change the repo has sourced,
with its date; state plainly "changes before <date> are not modelled."*

- **Cost:** lowest. It removes the carry-back convention, removes the
  "sessionless before first edition" state, and removes the pressure to
  retrieve pre-floor documents entirely. The existing `select_revision`
  machinery is unchanged — only the baseline's meaning changes from "the
  earliest sourced state, carried back" to "the oldest modelled state, valid
  from its own date forward."
- **Accuracy:** exactly as good as (A) *above* the oldest revision row, and
  honestly silent below it rather than dishonestly confident. Its weakness is
  that "not modelled" and "unchanged" become indistinguishable to a caller,
  unless the baseline row carries its own effective date — which is what SGX
  PR #67 already had to invent (STATUS.md: *"floor row = `select_revision`
  baseline not a 2010-01-01 row"*). [L]
- **Failure mode:** a caller backtesting 2012 gets 2026's grid with no warning
  unless the baseline date is surfaced in the API. That is a *surfacing*
  problem, and the crate already has the surface (`MarketHours.source` /
  `CalendarSource`).

### What each would have saved on the two case studies

**SGX pre-2020 (issues #45, #62, #64, #65, #66; PRs #67, #68, #69).** [L —
STATUS.md, and `src/calendar/schedules/futures/international/sgx*`]

Actual cost under (A): 5 keys, **1,861 lines of Rust across 6 modules, 19
revision rows**, 4 merged PRs plus an open floor follow-on, **417 files and
101 MB** in the research store, an era-table synthesis workflow with 5
proposals and 10 refutations, an adversarial review producing **19 findings
(18 confirmed)**, plus 3 spawned follow-up issues. The evidence chain had to
include: a Fubon **trading-member mirror** of DT/AM 50 of 2024; an Excel
**change log whose cells say "eff 4 Nov" with no year**, requiring a
second-order inference from a neighbouring date cell bound only by *cell-border
formatting*; SGX's **2009 psv specification pages**; and 22 content-api
captures. Two of the four blocking questions were *only* pre-2020 questions.

- **Under (B) or (C):** SGX's first surviving calendar edition sets the
  horizon. The five keys would begin there, the floor rows would not exist, the
  "sourced intersection" construction for the pre-first-edition era would not
  be needed, and **the five SGX rows would leave the 22-row executable-gap
  list**. The 2009 psv-page discovery (#65), which under the intersection
  convention *changes three floor rows* and forced an additional follow-on PR
  (`sgx-pre2020/2026-09-06-PLAN-floor-2009-intersection.md`), would have had no
  effect at all — there would be no floor rows to change.
- **Retained under all three:** the 2019-11-11 05:15 close and the 2024-11-04
  Japan move are post-2013 dated changes; they are in scope under (C) exactly
  as under (A). **The saving is not the SGX work — it is the SGX *floor*
  work**, which is where the year-inference risk, the member-mirror
  dependency, and the reopened follow-on all sat.

**ECBTC after 2026-05-29 (issue #57, PR #60).** [L — STATUS.md,
`docs/schedules/unsupported-families.md:47-75`]

This one is **not a history-depth problem at all** — it is a *source-conflict*
problem about a **future** effective date. Two CME primaries disagree by one
hour on the new weekday close (16:00 vs 15:00 CT) and *"the disputed hour is
exactly its former expiry instant."* Resolution required establishing, from
**Confluence's own version API**, that the wiki figure entered at version 4
under the page's 2026-04-22 revision row and was never superseded; that
SER-9740R's Table 2 is *"the cryptocurrency cell carried over unchanged"* and
misstates ECBTC's own prior hours; and that no CME channel has restated it.
The delivered answer serves the **sourced intersection** (open 16:02→15:00 CT
weekdays, the 15:00–16:00 hour withheld), and `AGENTS.md`'s intersection bullet
was extended to cover source conflict.

- **(A), (B) and (C) are all identical here.** No history-depth policy saves
  any of it.
- What *would* have: a **tiered evidence policy** (§4) that lets the operator's
  own machine feed adjudicate between two operator prose statements — and a
  policy on which prose channel wins when two operator documents disagree.
  Note the near-miss recorded at `unsupported-families.md:69-74`: *"Two
  near-identically titled wiki pages give different windows… Reading the wrong
  page makes the conflict appear not to exist; that happened once during review
  and was corrected."*

---

## 4. Evidence policy: primary-only vs tiered

### Current: primary-only, with a public-availability gate

- `LAW-PRIMARY-SOURCES` (`AGENTS.md:23-29`): *"every session time in a profile
  table is backed by a primary source (the exchange's own site, rulebook,
  notice, or regulator circular), cited in a comment next to the table.
  Secondary sources corroborate only."*
- `LAW-PUBLIC-SOURCES` (`AGENTS.md:30-35`): *"every cited source must be
  publicly available without authentication… Material behind a member portal or
  an authenticated feed is out of scope as a data source, though its existence
  and publication date may be cited as evidence that a change occurred."*
- The ledger grades outcome, not source: **Primary** (73 rows) /
  **Partial** (57 rows, of which 35 order-entry and 22 executable), plus
  excluded classes **Known issue / Secondary / Pragmatic / Synthetic**
  (`docs/schedules/verification.md:30-62`). **There is no per-citation tier.**

**Measured consequences of the current policy, all documented in-repo:**
1. **The operator's own authoritative machine feed is excluded by rule.**
   `refdata.api.cmegroup.com/refdata/v3/tradingSchedules` → `401`, therefore
   out of scope (`event-contracts-UNBLOCK.md:68`). [L]
2. **The permitted channels are failing.** `cmegroup.com` 403s at IP level;
   recent citations were read through *"a public text-extraction reader in
   front of the same cmegroup.com URLs"*, and `sources.md` carries a
   **"Channel limit"** note asking for re-verification (STATUS.md). The
   trade-type plan's standing residual risk is that *"every PR here extends
   it"* and that *"a review date must never be advanced on the weaker channel
   alone"* (`2026-09-12-cme-trade-type-keys.md:222-228`). [L]
3. **A member mirror was load-bearing anyway.** SGX's 2024-11-04 Japan move was
   dated by *"DT/AM 50 of 2024 (Fubon mirror, verified)"* — a trading member's
   copy of an operator circular, admitted because the mirror is public even
   though the operator's own portal copy is not. [L] The law already bends here
   in practice; it is just not written down as a tier.
4. **Feed-only boundaries are rejected even when unanimous.** Treasury TAS
   (6 roots), Dutch TTF TAS (2), commodity-index BTIC (9) are **rejected** —
   *"Each has a launch, a root list and a measurable feed boundary; none has a
   CME document stating hours in session language"*
   (`unsupported-families.md:76-80`). [L] 17 roots refused because the
   measurement exists and the sentence does not.

### Alternative: tiered, with the tier recorded per citation

A concrete four-tier scheme the existing evidence already sorts into:

| tier | definition | examples in this repo | proposed use |
|---|---|---|---|
| **T1 operator statement** | operator or regulator prose, in session language, publicly retrievable | CBOT Submission 18-001; SER-9519; RA1104-4; CME ContractSpecs `TAS:` rows | alone sufficient; **Primary** |
| **T2 operator feed** | operator's own machine-readable schedule output | `TradingSessionList.dat`; `/services/trading-hours-by-product`; `refdata/v3/tradingSchedules` (401) | sufficient for the **envelope**; never for Regular-vs-Extended; can **adjudicate** a T1 conflict |
| **T3 member / authenticated mirror** | a member's or vendor's public copy of an operator document | Fubon's DT/AM 50 of 2024; the SGX Titan catalogue workbook | sufficient when it reproduces a T1 document verbatim; tier recorded |
| **T4 press / secondary** | trade press, third-party libraries, blog reconstructions | (none currently admitted) | corroboration only, as today |

**What tiering buys, concretely.**
- **The 17 rejected trade-type roots become T2-sourced rows** with an honest
  tier label, instead of absent keys. The measurement is the operator's own.
- **ECBTC becomes adjudicable.** A T2 reading of the security group's own
  transitions for a week after 2026-05-29 settles 15:00 vs 16:00 CT
  empirically. Today that evidence is either unavailable (the group is absent
  from `trading-hours-by-product`) or inadmissible; a tiered policy would at
  least make "we measured it, tier 2" a recordable answer rather than a
  withheld hour.
- **The 1,146-root signature-1 residue becomes tractable.** Its envelope is
  T2-known for all 184 security groups; only the semantic split needs T1. A
  tiered policy could ship the envelope at T2 and mark Regular/Extended
  unclassified — versus today, where 1,120 roots get a venue fallback.
- **The "channel limit" caveat becomes a field instead of a footnote.** The
  reader-extracted citations are a distinguishable tier; the plan already asks
  each ledger row to *"say which of its citations came through that channel"*
  (`:226`) — that is a tier column being requested by hand.

**What tiering costs.**
- A per-citation tier field is ~500 citation sites to backfill (154 revision
  rows + 130 ledger rows + module comments across 91 schedule files).
- It weakens the crate's strongest differentiator. No other system in §1 has a
  ledger at all; a tier column is still far ahead of "a URL in a docstring."
- It requires a **conflict-resolution rule** (which tier wins), which the repo
  has so far handled case-by-case: the ECBTC ruling turned on *recency and
  derivation* (the wiki figure is earlier and never revised; SER-9740R's cell
  is a carry-over that misstates known prior hours) — a rule about **document
  lineage**, not about tier. A tier system must not overwrite that.

---

## 5. Facts index (for citation in the review)

**exchange-hours-rs at `5530f22`** [L]
- 96 `Exchange` variants (95 venues + `Unknown`) — `src/calendar/exchange/mod.rs:37`
- 36 `MarketHoursKey` variants — `src/calendar/futures_profile.rs:143`; 5 are TAS keys already landed
- 127 `.rs` files / 23,962 lines in `src`; 91 files under `src/calendar/schedules`
- 87 test files / 19,857 lines; 11 docs / 3,173 lines; 500-line file cap
- 154 dated revision rows crate-wide; 19 of them SGX
- Ledger: 130 rows — **73 Primary, 57 Partial** (35 order-entry gap, 22 executable gap); cutoff `2026-08-22`
- 9 named laws: `LAW-PRIMARY-SOURCES`, `LAW-PUBLIC-SOURCES`, `LAW-NO-FABRICATED-DATES`, `LAW-UTC-DATES`, `LAW-SESSION-NOT-EXPIRY`, `LAW-HOLIDAY-SCOPE`, `LAW-FOLLOW-UPS-ARE-ISSUES`, `LAW-DETERMINISM`, `LAW-PANIC`

**The plan** (`docs/plans/2026-09-12-cme-trade-type-keys.md`) [L]
- 32 new keys, 13 PRs, 6 blocked keys, 3 rejected groups; 5 of 13 PRs blocked on #71/#72/#76/#77
- 14 registration sites per key; explicit expectation of serialized rebases

**SharurPlatform** [L]
- `crates/domain/src/globex_products.rs`: 104 roots → **8 distinct keys**; no trade-type roots
- `crates/domain/src/data/calendar/mod.rs:102-230`: `SessionCalendar` trait — `is_open`,
  `session_close_containing`, `window_bounds`, `trading_day_bounds`,
  `intraday_window_in_day`, `session_state`, `next_session_open_after`, …
- `crates/ui/src/session_calendar.rs` (141 lines) adapts exactly 5 of them
- **28 of the crate's 36 keys have no SharurPlatform consumer**

**Databento GLBX.MDP3 audit** (`exchange-hours-research/catalog-artifacts/`) [L]
- 1,342 future roots on listing-exchange fallback; 1,797-row root classification
- 41 exact transition signatures; signature 1 = **1,146 roots / 184 security groups** on one envelope
- CME `TradingSessionList.dat` week of 2026-08-30: **1,364 group rows, 1,316 with Ready**
- 46 roots changed route between April keys and August schedule (~4%)

**Fetched this pass** [W]
- `raw.githubusercontent.com/gerrymanoim/exchange_calendars/master/README.md`
- `…/exchange_calendars/exchange_calendar.py`, `…/exchange_calendar_cmes.py`
- `raw.githubusercontent.com/rsheftel/pandas_market_calendars/master/pandas_market_calendars/calendars/{cme_globex_base,cme_globex_energy_and_metals,cme_globex_agriculture,cme_market_times,mirror}.py`
- `raw.githubusercontent.com/lballabio/QuantLib/master/ql/time/calendars/unitedstates.hpp`

---

## 6. Open questions this pass could not close

1. **LEAN's `market-hours-database.json` was not verified.** The local checkout
   at `<scratchpad>/lean` has empty `Data/market-hours/` and zero `.cs` files.
   §1.8 is memory-only. It is the closest analogue to `exchange-hours-rs`
   (two-level key + wildcard fallback, phase-tagged segments, holidays and
   early closes in-band) and deserves a verified pass before the review leans
   on it.
2. **Does `TradingSessionList.dat` have a retrievable archive?** If CME's FTP
   directory or the Wayback CDX retains past weeks, T2 evidence acquires
   *history*, which changes the §3 calculus materially. Not tested here.
3. **What does `refdata/v3/tradingSchedules` actually return?** It is the
   channel most likely to carry Regular-vs-Extended semantics as well as the
   envelope. It is `401` and excluded by law; whether a free developer key
   exists was not established.
4. **Is `Instrument::session_hours_basis()`'s approximate mark already enough?**
   SharurPlatform ships `HOURS≈` and an operator ruling accepting "minor
   per-symbol hours inaccuracy… disclosed". Whether a 4.5-hour TAS error counts
   as "minor" under that ruling is a policy question for the maintainer, and it
   is the single question that decides between options (i)/(ii) and (iii).
5. **Bloomberg/Refinitiv shapes (§1.9) are unverified memory.** If the review
   wants to cite commercial practice, that needs a real source.
6. **`exchange_calendars` and `pandas_market_calendars` defect rates were not
   measured.** A useful datum would be: how wrong is `pandas_market_calendars`'
   undated CME grid for 2012–2022, measured against `exchange-hours-rs`'s own
   154 revision rows? That is a computable number and would quantify what the
   history investment actually buys.
