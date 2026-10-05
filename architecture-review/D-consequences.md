<!-- SPDX-License-Identifier: MIT-0 -->

# D — Consequence analysis

What each candidate policy would break in SharurPlatform, and what it would
save in `exchange-hours-rs`. Facts gathered 2026-09-12 (UTC). **No file in
`exchange-hours-rs` or `SharurPlatform` was modified**; both trees were verified
clean before and after.

Inputs: `A-crate-anatomy-and-cost.md`, `B-sharur-consumption.md`,
`C-prior-art.md`, re-verified against the two repositories where a number is
load-bearing for a conclusion. Baseline: `exchange-hours-rs` @ `5530f22`
(branch `trade-type-metals-tas`, = PR #83, 36 keys);
`SharurPlatform` @ `7af5d5f4`.

I do not decide policy. Sections 1–3 build the frame; §4–§9 work each policy
against Sharur's own code; §10 is the risk-asymmetry question the maintainer
asked; §11 ranks and says which combinations are coherent; §12 corrects three
facts in reports A and B.

---

## 1. The one structural fact that orders everything else

**Sharur's consumption of the calendar is asymmetric. Being told "closed" when
the venue is open destroys data. Being told "open" when the venue is closed
corrupts labels and gates, and destroys nothing.**

### 1.1 Under-open destroys data — three mechanisms, all citable

| # | Mechanism | Site | Effect |
|---|---|---|---|
| 1 | Live trade drop | `crates/application/src/bars/consolidator.rs:189` — `if !calendar.is_open(trade.time()) { warn; return Ok(None) }` | The print never enters a bar. Irrecoverable for that bar: the OHLCV is wrong forever, and the warn is one line per print. |
| 2 | Footprint drop | `crates/application/src/bars/footprint.rs:95` | Same gate, same silent-but-warned drop, on the per-price ladder. |
| 3 | Historical mis-placement | `crates/domain/src/data/close_time.rs:70-72` — *"For an instant in a closed stretch the answer is the NEXT trading day's first window"* | A daily/weekly/monthly bar the venue returns inside a falsely-closed stretch is folded into the **next** trading day's opening window (`crates/app/src/history.rs:426` `place_calendar_windows`). Two bars collide; one is silently overwritten or dropped. |

Additionally the seed window shrinks: `window_open_back`
(`crates/domain/src/data/window_reach.rs`) counts the venue's own windows, so a
narrower envelope means fewer windows per calendar day and a shorter
`[start, end)` than the chart plots — the failure mode Sharur already names by
number (`crates/application/src/engine/history_depth.rs:134-160`: *"delivered
3 433 of 5 000 five-minute bars (#345)"*).

### 1.2 Over-open corrupts labels and gates — and nothing else

When the calendar claims a session the venue does not run, **there are no prints
in that window**, so no bar can be mis-folded and no trade can be mis-dropped.
The bar's OHLCV is byte-identical to the correct answer. What moves is:

| Symptom | Site |
|---|---|
| DOM ladder buy/sell stays armed on a closed book | `crates/ui/src/dom/trading/mod.rs:115` `tradable() = enabled() && market_open`, fed by `:125` `calendar.is_open(clock.now())`; passed as `interactive` at `crates/ui/src/dom/body.rs:399` |
| Closed banner absent; "opens in …" countdown points at the wrong instant | `crates/ui/src/session_calendar.rs:100,129` |
| Bar-close countdown ticks toward a bar that will not form | `crates/chart/src/charting/frame_admission.rs:53` |
| Session-break line drawn at the wrong x | `crates/chart/src/charting/render/session_breaks.rs:36` |
| Dead time not compressed out of the axis | `crates/chart/src/charting/time_axis/spacing.rs:392` |
| Daily bar's stamped `close_time` late; indicator bucket key late | `crates/ui/src/session_calendar.rs:123`; `crates/chart/src/indicators/portable/inputs.rs:124` `session_id_for_bar` |
| Seed asks a window *wider* than needed | `window_open_back`; surfaces as `report_shortfall`, not as corruption |

Every one of these is a display or affordance defect an operator can see and a
later calendar fix repairs in place. None of them changes a stored number.

### 1.3 Consequence for the ranking

> A policy that can only **widen** the envelope relative to truth is
> recoverable. A policy that can **narrow** it is not.

Of the five granularity policies, **only P1 narrows**. P2 narrows only where the
crate is already wrong. P4 and P5 widen. Of the three history policies, **H3's
"unknown" is the only place a narrowing can be introduced by accident**, and only
if `unknown` is implemented as `Closed` (§6.4).

---

## 2. Sharur's real exposure surface, measured

Everything the review is arguing about is only reachable through this surface.
Measured directly this pass.

### 2.1 Which keys can be reached at all

Per-variant census over `SharurPlatform/crates/**/*.rs`
(`MarketHoursKey::<V>` or the `Hours::<V>` alias in `globex_products.rs`):

| Reachability | Count | Variants |
|---|---:|---|
| Production reference | **12 of 36** | `GlobexEquityIndex`, `GlobexEnergy`, `GlobexGrains`, `GlobexFx`, `GlobexInterestRates`, `GlobexLivestock`, `GlobexCryptocurrency`, `GlobexNikkei225Dollar` (catalog + world clock) · `CfeVix`, `Eurex`, `IceUs`, `Sgx` (world clock only) |
| Test-only reference | **1** | `IceUsDollarIndex` (`crates/adapters/rithmic/tests/unit/registry.rs:127`) |
| **Zero reference anywhere** | **23 of 36** | `GlobexMiniGrains`, `IceUsSugar`, `IceUsCoffee`, `IceUsCocoa`, `IceUsCotton`, `IceUsOrangeJuice`, `EurexFixedIncome`, all 5 `SgxEquityIndex*`, `GlobexRoughRice`, `GlobexWeather`, `GlobexSpotQuoted`, `GlobexEventContracts`, `GlobexEventContractsBtc`, all 5 `*Tas`, `AlwaysOpen` |

The world-clock rows are `crates/ui/src/market_clock/sets.rs:43,48,50,51,55,57,61`
(the seven Globex families) and `:97,98,99,100` (`CfeVix`, `Eurex`, `IceUs`,
`Sgx`).

**The five SGX equity-index keys are not reachable even from the world clock.**
Its one SGX row is `MarketHoursKey::Sgx` — the generic venue key, 1 revision row,
Basis Primary (`sets.rs:100`, `Market::family("Three-Month SORA", "SGX", …)`).
The pre-2020 SGX programme (A §5.3: 6 issues, 4 PRs, 10 calendar days, ~100 agent
runs, 417 files / 101 MB, 1,532 source lines, 969 test lines, 14 revision rows)
produced **zero reachable rows** for this consumer.

### 2.2 Which revision rows can be reached

279 revision rows across 106 `revisions!` blocks (bracket-matched count, matches
A exactly). Distribution by effective year:

```
2010 26   2011 20   2012 22   2013 26   2014 13   2015 15   2016 17
2017 11   2018 20   2019 15   2020 18   2021  9   2022  4   2023 11
2024  7   2025 17   2026 28
pre-2020: 185 (66.3%)      2020+: 94 (33.7%)
futures modules: 130       equities modules: 149
```

Rows reachable from a Sharur instrument — the eight catalog keys only:

| Key | Rows | Effective dates |
|---|---:|---|
| `globex_equity_index` | 5 | 2010-11-15, 2012-11-18, 2015-09-20, 2021-06-27, 2026-08-22 |
| `globex_energy` | 2 | 2015-09-20, 2026-08-22 |
| `globex_fx` | 2 | 2010-11-15, 2026-08-22 |
| `globex_interest_rates` | 3 | 2010-11-15, 2011-10-02, 2026-08-22 |
| `globex_grains` | 6 | 2010-04-19, 2011-12-27, 2012-05-20, 2013-04-07, 2013-08-18, 2015-07-05 |
| `globex_livestock` | 4 | 2014-10-27, 2016-02-29, 2016-06-06, 2020-05-31 |
| `globex_cryptocurrency` | 9 | 2017-12-17, 2026-05-29, -05-30, -08-01, -08-02, -08-29, -08-30, **-09-19**, -09-20 |
| `globex_nikkei_225_dollar` | 4 | 2011-01-12, 2012-11-18, 2013-03-03, 2015-09-20 |
| **Total** | **35 of 279 (12.5%)** | **21 pre-2020 · 14 from 2020** |

Two facts inside that table matter more than the totals:

1. **Exactly two of Sharur's 35 reachable rows fall in 2020-01-01 … 2025-12-31**
   (`globex_livestock` 2020-05-31, `globex_equity_index` 2021-06-27). Twelve of
   the remaining fourteen are dated in **2026**.
2. **Four of the fourteen 2020+ rows are the same knowledge-bound row**
   (`2026-08-22`, reason string *"2026-08-22 review: verified current, onset
   undated"*, e.g. `src/calendar/schedules/futures/us/cme_group.rs:306-312`,
   `energy_metals.rs:164-170`). Each widens a **Sunday order-entry queue by the
   16:00–16:15 CT quarter-hour**. `is_open` cannot see them at all.

### 2.3 What the ledger says is uncertain about Sharur's keys

`docs/schedules/verification.md`:

| Key | Basis | Gap kind | Line |
|---|---|---|---:|
| `globex_equity_index` | Partial | **order-entry** | 405 |
| `globex_energy` | Partial | **order-entry** | 406 |
| `globex_grains` | Partial | **order-entry** | 407 |
| `globex_fx` | Partial | **order-entry** | 409 |
| `globex_interest_rates` | Partial | **order-entry** | 410 |
| `globex_livestock` | Partial | **order-entry** | 411 |
| `globex_cryptocurrency` | Partial | **order-entry** | 412 |
| `globex_nikkei_225_dollar` | Partial | **executable** | 422 |

**Seven of Sharur's eight keys carry a documented gap in a phase Sharur's
`is_open`, consolidator, DOM gate, bar windows and trade dates cannot observe.**
`order_entry` is excluded from `is_open` by construction
(`src/calendar/query/status.rs:75-86`; `crates/chart/src/session.rs:95-99`
`is_open` = `OpenRegular | OpenExtended`). The single executable gap belongs to
the one key with **one** mapped root (`NKD`).

### 2.4 The eight production `is_open` call sites

`crates/ui/src/session_calendar.rs:118` · `crates/ui/src/market_clock/markets.rs:183` ·
`crates/ui/src/dom/trading/mod.rs:125` · `crates/app/src/history_tick_bar_fetch.rs:143` ·
`crates/app/src/history.rs:248` · `crates/chart/src/charting/frame_admission.rs:53` ·
`crates/chart/src/charting/time_axis/spacing.rs:392` ·
`crates/application/src/bars/{consolidator.rs:189, footprint.rs:95}` (via
`crates/domain/src/data/calendar/exchange/port.rs:24-25`).

**Seven of the eight ask about `now` or the fetch cutoff.** The only one that
asks about a historical instant is `history_tick_bar_fetch.rs:143`, whose
`source_start` is bounded to the current or previous **daily** window
(`:138-147`). SharurPlatform ships **no historical replay engine** — `backtest`
appears in `crates/application/src/engine/driver.rs:42` only as a comment about a
path that skips the driver, and the predecessor `Sharur` repo owns the one that
exists. So **no historical print is ever passed through `is_open` today.**

### 2.5 The history a Sharur instrument can actually hold

- Intraday horizons measured from the on-disk seed cache (B §3.2): 1 m → 4 days,
  5 m → 25 days, 15 m → 75 days.
- The daily walk reached **2007-07-15** for `MNQU26` and the venue returned
  **0 rows**.
- The reason it reached 2007 is that **nothing clamps the walk to the
  instrument's own listing window.** `InstrumentDetails` carries `activation`
  and `expiration` (`crates/domain/src/instrument/catalog.rs:82-83`) and
  `is_listed_at` (`:221-222`), but `grep -rn "activation" crates/app/src
  crates/application/src` returns **no hit in the history-fetch path**. The only
  backstop is the Unix epoch (`window_reach.rs:297`).
- There is **no continuous-contract concept** in SharurPlatform. Every
  instrument is one dated contract month. A quarterly future's listable life is
  months to a few years.

**Therefore: with a one-line clamp to `details().activation`, no Sharur query
would ever reach below roughly 2024.** The deep-history exercise is an artefact
of an unclamped walk, not a requirement.

### 2.6 Where the `regular` / `extended` split can carry information

Read from `src/calendar/futures_profile/profiles.rs` and the schedule modules:

| Key | `regular` | `extended` | Sharur roots |
|---|---|---|---:|
| `globex_equity_index` | `CME_REGULAR` 08:30–15:15 CT | non-empty | 11 |
| `globex_grains` | `CBOT_REGULAR_CURRENT` 08:30–13:20 | non-empty | 12 |
| `globex_livestock` | 08:30–13:05 | **`&[]`** | 4 |
| `globex_nikkei_225_dollar` | **whole 17:00→16:00 envelope** | **`&[]`** (`cme_nikkei.rs:67`) | 1 |
| `globex_energy` | **`&[]`** | 17:00→16:00 | 20 |
| `globex_fx` | **`&[]`** | 17:00→16:00 | 17 |
| `globex_interest_rates` | **`&[]`** | 17:00→16:00 | 18 |
| `globex_cryptocurrency` | **`&[]`** | 24/7 pieces | 21 |

- **76 of 104 roots (73%) have `regular: &[]`** — `SessionState::OpenRegular`
  is unreachable for them, so `opens.regular`
  (`crates/chart/src/indicators/portable/inputs.rs:230`) can never fire.
- **5 more have `extended: &[]`** — `OpenExtended` unreachable.
- **Only 23 of 104 roots (22%) can ever produce both open states.**
- `NKD` and `globex_equity_index` are both CME equity-index products and
  classify the *same* 17:00→16:00 envelope oppositely: NKD calls all 23 hours
  `regular`, equity index calls 08:30–15:15 `regular` and the rest `extended`.
  The split tracks **whether CME printed the word "RTH"**, not a market fact.

---

## 3. The four consumer purposes, and which policy dimension touches each

| Purpose | Crate answer used | Sharur site | Sensitive to granularity? | To history depth? | To evidence tier? | To holidays? | To RTH split? |
|---|---|---|---|---|---|---|---|
| **Candle construction** | `candle_start`/`candle_end` at `Daily`/`Weekly`/`Monthly`; the venue wall-clock grid inside the day | `domain/.../exchange/port.rs:67-72`, `grid.rs:9-27`, `close_time.rs:83,105`, `day_memo.rs:181` | **Yes** — the trading day's two ends | Only via the daily walk (§2.5) | No | **Yes** — a closed day still gets a window | **No** — the grid uses `SessionKind::Both` |
| **Session-break detection** | `session_state(..).is_closure()` | `chart/.../render/session_breaks.rs:36`, `time_axis/spacing.rs:392` | **Yes** | Chart depth only | No | **Yes** | No |
| **Trade-date assignment** | `trade_date`; `session_close` bucket key | `port.rs:141`, `ui/src/session_calendar.rs:135`, `chart/.../inputs.rs:124` | **Yes**, where families roll differently | No | No | **Yes** (early close moves the stamp) | No |
| **Is-open / order-routing gate** | `is_open(now)` | `ui/src/dom/trading/mod.rs:125`; `consolidator.rs:189`; `footprint.rs:95` | **Yes** | **No** — always `now` | No | **Yes** | No |

Two conclusions fall straight out of this table and hold for the whole review:

1. **History depth touches exactly one purpose, through one accidental path**
   (the unclamped daily walk). Nothing else Sharur does asks about the past.
2. **Holidays touch all four.** Granularity touches all four. Evidence tier
   touches none of them directly — it changes *which row you are allowed to
   write*, not what the consumer computes.

---

## 4. P1 — exchange envelope only (delete `MarketHoursKey`)

Sharur would resolve every instrument through
`SessionHoursBasis::ExchangeFallback` →
`exchange_hours::calendar_for_exchange`. The crate's venue defaults are at
`src/calendar/presets/historical.rs:84-91`: `Cme → cme_profile_at`
(= equity index), `Cbot → cbot_profile_at` (= grains),
`Comex | Nymex → energy_metals_profile_at`.

### 4.1 Worked example A — `ZN` (10-Year T-Note, CBOT, 18 rate roots)

| | Envelope |
|---|---|
| True (`globex_interest_rates`, `interest_rates.rs:85-89`) | Sun+Mon–Thu **17:00 → 16:00 CT**, continuous |
| Under P1 (`cbot_profile_at` = grains, `grains.rs:194-198` + `:85-89`) | Sun+Mon–Thu 19:00 → 07:45 **and** Mon–Fri 08:30 → 13:20 |

Falsely **closed** every trading day:

| Window | Duration |
|---|---|
| 17:00 – 19:00 CT | 2 h 00 |
| 07:45 – 08:30 CT | 0 h 45 |
| 13:20 – 16:00 CT | 2 h 40 |
| **Total** | **5 h 25 per day ≈ 27 h per week** |

- **Candle construction:** every historical daily `ZN` bar has its afternoon
  prints (13:20–16:00 CT, which contains the 14:00 CT Treasury settlement window)
  folded into the *next* trading day's 19:00 opening window
  (`close_time.rs:70-72` → `history.rs:426`). Live 1-minute bars covering
  those 325 minutes are never built: every print is dropped at
  `consolidator.rs:189`.
- **Session breaks:** three break lines a day instead of one; the axis compresses
  5 h 25 of live trading out of existence (`spacing.rs:392`).
- **Trade date:** the 13:20–16:00 prints bucket to the **following** trading day
  (`session_id_for_bar`, `inputs.rs:124`) — every indicator that splits per
  session splits in the wrong place.
- **Order-routing gate:** the DOM ladder greys out at 13:20 CT on the most liquid
  Treasury contract listed.

Same error applies to `YM` and `MYM` (equity index listed on CBOT, `Cbot` row in
`globex_products.rs`): **20 of 104 roots.**

### 4.2 Worked example B — `BTC`/`MBT` (21 crypto roots)

| | Envelope |
|---|---|
| True (`cryptocurrency.rs` `CURRENT_EXTENDED`) | 24/7, minus Mon–Fri 16:00–16:02 CT and Sat 02:00–04:00 CT |
| Under P1 (`cme_profile_at`) | Sun 17:00 → Fri 16:00, with a 16:00–17:00 CT daily break |

Falsely closed:

| Window | Duration |
|---|---|
| Fri 16:02 → Sat 02:00 | 9 h 58 |
| Sat 04:00 → Sun 17:00 | 37 h 00 |
| Mon–Thu 16:02 → 17:00 (×4) | 3 h 52 |
| **Total** | **≈ 50 h 50 per week per root, on 21 roots** |

Every weekend print on CME's 24/7 crypto book is dropped live and mis-folded
historically. This is the single worst outcome available anywhere in the five
granularity policies.

### 4.3 Worked example C — `LE`/`HE`/`GF`/`PRK` (4 livestock roots) — the other direction

| | Envelope |
|---|---|
| True (`livestock.rs:91-95`, `extended: &[]`) | Mon–Fri **08:30 – 13:05 CT only** — 22 h 55 per week |
| Under P1 (`cme_profile_at`) | Sun 17:00 → Fri 16:00 — ≈ 115 h per week |

**≈ 92 hours per week of false-open.** No data is destroyed (there are no prints
to mis-fold), but the DOM ladder is armed ~19 h a day on a closed book, and the
closure-compressed axis stops compressing, so a 5 000-point 1-minute `LE` chart
becomes roughly 80% whitespace.

### 4.4 P1 damage roll-up over Sharur's 104 roots

| Group | Roots | Outcome under P1 |
|---|---:|---|
| CME equity index (`ES`…`RTY`) | 9 | exact |
| NYMEX + COMEX energy/metals | 20 | exact |
| CBOT grains | 12 | exact |
| CME FX + `SR1`/`SR3` | 19 | **union identical**, `regular`/`extended` labels wrong only |
| `NKD` | 1 | union identical, labels wrong |
| CBOT rates + `YM`/`MYM` | 20 | **−5 h 25 / day false-closed** |
| CME crypto | 21 | **−50 h 50 / week false-closed** |
| CME livestock | 4 | **+92 h / week false-open** |
| **Materially wrong on `is_open`** | **45 (43%)** | |
| **Wrong only on RTH labels** | **20 (19%)** | |
| **Exact** | **41 (39%)** | |

### 4.5 What P1 would save

| Deleted | Lines |
|---|---:|
| `src/calendar/schedules/futures/**` (41 files) | **9,376** |
| `src/calendar/futures_profile.rs` + `futures_profile/{profiles,key_serde}.rs` | 1,054 |
| `tests/futures_family_boundaries/**` (13 files) | **4,665** |
| Ledger rows / source-set prose / README counts for 36 keys | 36 of 132 rows, ~79 KB of ledger notes (A §5.1) |
| **Total source + test** | **≈ 15,100 lines** |

It also removes the entire 32-key plan (A §5.5: ~9,000–11,500 new source lines,
~70 revision rows, 169 registration edits, 12 guaranteed ledger conflicts) and
removes `CalendarSource`'s second arm, collapsing three near-identical profile
shapes (A §2.1) to two.

**Verdict on P1: the largest saving available and the only policy that can
destroy data. 43% of the consumer's current roots break, three of them badly.
It is not survivable as stated.** A *narrow* variant — keep keys only where the
venue default is measurably wrong (rates, crypto, livestock, grains-vs-minis) —
is P2 with a pruning rule, not P1.

---

## 5. P2 — product family (status quo)

This is what ships. It is exact for all 104 Sharur roots today, and its residual
uncertainty is order-entry-only on 7 of the 8 keys (§2.3).

### 5.1 What it costs, per A, and what share of that cost the consumer sees

| Cost centre | Measure | Share consumed by Sharur |
|---|---|---|
| Key modules | 41 files / 9,376 lines | 8 modules of 41 |
| Revision rows | 130 futures rows | **35 (27%)** |
| Ledger notes for key rows | 79,438 chars | ~8/36 of rows |
| Keys | 36 | **12 referenced, 8 mapped** |
| `tests/futures_family_boundaries` | 4,665 lines | ~8 of 13 submodules |

The waste is not in P2's *shape*; it is in P2's *admission rule*. `AGENTS.md`
imposes no test of demand before a key is added, so 23 of 36 keys were added with
no consumer and none has acquired one (§2.1).

### 5.2 What P2 does not cover, and should

Rithmic admits eight venue namespaces (`crates/adapters/rithmic/src/catalog.rs:74-172`:
CBOT, CDE, CFE, CME, COMEX, EUREX, NYBOT, NYMEX) but `globex_products` is
Globex-only. So an ICE Sugar No. 11 routed via `NYBOT` gets
`ice_us_fang_profile_at` — 20:00–18:00 ET against Sugar's 03:30–13:00 ET
(B §2.3): a ~12.5 h/day error on a key the crate **already has**
(`IceUsSugar`). Eurex fixed income gets FESX hours against an existing
`EurexFixedIncome` key.

**The crate is over-built for the roots Sharur maps and under-reachable for the
venues Sharur's own adapter admits.** That is a catalog problem, not a crate
problem, and it costs zero crate work to fix.

---

## 6. P3 / P4 / P5 — the trade-type question

### 6.1 The shared starting facts

- SharurPlatform has **zero** TAS/TAM/BTIC/TACO/TMAC references anywhere
  (B §2.6; re-verified: all five `*Tas` keys have zero references, §2.1).
- Both live adapters admit `InstrumentKind::Future` only
  (`projectx/src/capabilities.rs:33-35`, `rithmic/src/capabilities.rs:60`).
- The plan's own survey: *"Out of roughly 180 trade-type roots surveyed,
  **exactly one** genuinely reuses an underlying's key"*
  (`docs/plans/2026-09-05-cme-trade-type-handoff.md:37`, restated `:195`) — `6EP`,
  Euro FX BTIC+, on a CME sentence.
- The plan's own counter-evidence: CME's live ContractSpecs prints the
  **outright** envelope for `EST`, `IPT`, `RVT`/`RSV`, so *"the verdict recorded
  as 'sourced' three roots on which CME contradicts itself across two of its own
  channels"* (`handoff:232`).
- CME's own TAS eligibility workbook has **six** tabs where the plan proposes ten
  keys (`handoff:222`).

### 6.2 P3 — 32 new keys (the plan)

**Harm to Sharur: zero, and benefit to Sharur: zero.** No adapter can produce a
trade-type root; nothing in the catalog names one; the 162 trade-type roots in
the 1,342-root unmapped GLBX set are not reachable (B §2.5).

**Cost (A §5.5, projected from measured rates):** ~9,000–11,500 new source
lines · ~70 new revision rows (279 → ~349; futures 130 → ~200, +54%) · keys 36 →
68 (+89%) · ledger 132 → 164 rows · ~132 KB of new ledger prose · ~13 test
modules · ~65–100 tests · ~25–35 GitHub issues · ~70 mutation checks · 169
hand-written registration edits · **12 guaranteed ledger rebase conflicts** · four
maintainer decisions gating 4 of 13 PRs.

**Two structural problems it walks into immediately:**

1. `src/calendar/futures_profile.rs` is at **488 of the 500-line ceiling** and
   PR #83 added 14 net lines per key. **PR 3 (2 keys, ≈28 lines) breaches it**,
   and the plan allocates no split (A §3.6).
2. Every PR touches `verification.md`, `README.md`, `CHANGELOG.md` and
   `sources.md`, so merges serialise by construction
   (`2026-09-05-cme-globex-family-coverage.md:211` Trap 6, Trap 7).

**The one honest argument for P3 that survives the consumer facts:** the crate is
a public artefact that answers *"is this identity tradeable at instant t"*, and
`handoff:220` is right that `CLT` at 14:00 CT is a different answer from `CL`.
That argument stands on the crate's public purpose, not on SharurPlatform.

### 6.3 P4 — map the variant to the underlying key, flag it in the catalog

Sharur's machinery already exists: `SessionHoursBasis`
(`crates/domain/src/instrument/mod.rs:199-210`) and the `approximate_session_hours`
flag on `StreamRegistration` (`crates/ui/src/chart_feed/binding.rs:222`), with
`HOURS≈` in the chart. The governing consumer ruling is
`SharurPlatform/AGENTS.md:159-160`: *"Minor per-symbol hours inaccuracy is
accepted and disclosed (operator ruling 2026-09-05); silent inaccuracy is not."*

**Worked example — `GCT` (Gold TAS) if Sharur ever admitted it.** `GC` maps to
`GlobexEnergy` (`globex_products.rs`), so `GCT` would too.

| | Close |
|---|---|
| True (`metals_tas.rs:193-197`) | Sun+Mon–Thu 17:00 → **12:30 CT** |
| Under P4 (`globex_energy`, `energy_metals.rs:78-82`) | Sun+Mon–Thu 17:00 → **16:00 CT** |

- **Candle construction: unharmed in content.** No print exists on the `GCT` book
  between 12:30 and 16:00, so the daily bar's OHLCV is identical. What is wrong
  is the bar's stamped `close_time` (3 h 30 late) and therefore the x-position of
  the session break.
- **Trade-date assignment: unharmed.** Both sessions close on the same venue-local
  date, so `assign_normal` (`src/calendar/query/identity.rs:36-42`) returns the
  same date. This holds for all five TAS keys.
- **Session-break detection: wrong by 3 h 30** per day; the axis does not compress
  12:30–16:45.
- **Order-routing gate: wrong, and in the direction that matters to an operator.**
  `is_open(14:00 CT)` returns true, `tradable()` stays true
  (`dom/trading/mod.rs:115`), the operator clicks buy, the venue rejects. The book
  is genuinely closed 12:30–16:45 CT and then runs a full Pre-Open/Ready cycle
  (`handoff:220`), so `next_session_open_after` and `session_close_containing`
  are structurally, not merely imprecisely, wrong.

Error sizes across the family (`handoff:215`): grain TAS 5 min · livestock TAS
5 min · crypto TAS 1 h · gold TAS 3 h 30 · energy TAS 4 h 30.

**P4's real defects, ranked by how much they would actually bite Sharur:**

1. The 5-minute cases are below any resolution Sharur draws (finest boundary
   observed is a whole minute, B §5.5) — genuinely "minor per-symbol inaccuracy".
2. The 3.5–4.5 h cases are not minor by any reading, and the failure is on the
   *offer* side (an armed ladder on a closed book), which is the one class of
   defect an operator experiences as the platform lying.
3. P4 cannot express the shapes where the variant has **more** structure than the
   underlying — Nikkei BTIC's second `Noon–17:00 ET` window, `6EB`'s 50-minute
   London interruption, crypto BTIC's 5-minute reference-rate stop rolling the
   trade date at three different city closes (`handoff:213-218`). For those,
   P4 *is* under-open, and §1.1 applies.

**Cost: ~zero in the crate** (one doc sentence per family), one new
`SessionHoursBasis` variant in the consumer.

### 6.4 P5 — declare trade-type variants out of scope in the catalog

`P5` is what SharurPlatform already does *by omission* — those roots are simply
absent from `globex_products`, and an absent root is **not refused**: it falls to
`ExchangeFallback` (`instrument/mod.rs:199-210`). So a literal "refuse to bind"
reading of P5 contradicts two of the consumer's own laws:

- `SharurPlatform/AGENTS.md:145-147` — *"A valid future whose family has no
  authored evidence remains usable with its listing-exchange fallback."*
- `:589-590` (`PAT-DEFINITION`) — *"There is no pre-generated artifact, no
  reference-catalog key and no membership gate: a venue result the provider can
  define BINDS."*

Read as *"do not author a trade-type row; let it fall through"*, P5 is
**identical to P4 minus the flag** — and the fallback it falls to is worse than
P4's. `GCT` would route on its listing exchange (`COMEX`) →
`energy_metals_profile_at` — the same answer P4 gives, but without the `HOURS≈`
disclosure. On a venue where the fallback is wrong (e.g. an `NYBOT` trade-type
root) the error is the 12.5 h/day FANG+ error of §5.2.

**So P5 is strictly dominated by P4**: same crate cost (zero), same or worse
accuracy, and it forfeits the disclosure the consumer's own law requires.

### 6.5 The hybrid the evidence actually supports (named because no listed option covers it)

C §2 (ii) establishes that a close-override variant dimension is exact for TAS
(identical `days` and `open_ssm` on all five landed keys, verified at
`metals_tas.rs:193-207`) and inexpressible for BTIC/TAM/TACO/TMAC.
§6.1 establishes that CME's own granularity is six TAS families.

**P4 for TAS (with an error-size threshold) + P3 for the rest + P5 for
everything Sharur cannot route** is coherent and is the only combination whose
per-shape cost tracks per-shape evidence. It is not one of the five options.

---

## 7. H1 / H2 / H3 — history depth

### 7.1 What Sharur actually asks of history

From §2.5 and §3: history reaches the crate through **one** path, the daily
chart's backward walk, and that walk is unclamped by accident. Intraday never
exceeds ~75 days. `is_open` is never asked about a historical instant in any
live path. There is no backtest replay engine.

### 7.2 H1 — blanket January-2010 floor (current)

`AGENTS.md:49-50` and `:171-195`. **185 of 279 revision rows (66.3%) are
pre-2020.** For Sharur, 21 of its 35 reachable rows are pre-2020, and none of
them is reachable by any query the platform makes on purpose.

- **Candle construction:** a 5 000-bar daily `MNQU26` chart walks to 2007-07-15
  and the venue returns **0 rows** (B §3.2). Cost: ~5 000 trading-day
  derivations at 17–23 µs = **85–115 ms per daily-chart open**, for nothing.
- **Session breaks / trade dates / is-open:** untouched. None of them asks about
  2010.
- **Maintenance cost:** this is where the crate's most expensive programmes live.
  The SGX pre-2020 case (A §5.3) — 10 calendar days, ~100 agent runs, 417 files /
  101 MB, 1,532 source lines, +3,348/−1,438 across four PRs — produced **14
  revision rows on five keys that are unreachable from SharurPlatform entirely**,
  and issue #66 is still open. The floor is also the *cause* of most of the
  executable-gap population: `verification.md:56-62` names the six ICE U.S. keys
  (*"pre-August-2011 grid is carried back"*), `globex_nikkei_225_dollar`
  (*"sessionless before its grid's first sourced appearance"*) and the five SGX
  keys (*"a sourced intersection, sessionless before the first surviving calendar
  edition"*).

### 7.3 H2 — per-venue data horizon

Each key declares the date its evidence begins; below it, no answer.

- **Sharur already runs this, today, on 21 roots.** `globex_cryptocurrency`'s
  `select_revision` baseline is `CLOSED` (`cryptocurrency.rs:245`), so a `BTC`
  daily chart walking back past 2017-12-17 finds no trading day, the walk hits
  `MAX_CLOSURE_SECONDS` and stops, returning the count it placed
  (`window_reach.rs:331-339`), and `report_unreachable_past`
  (`crates/app/src/history.rs:374-385`) says so once at `warn`. **The graceful
  path exists and is exercised in production.**
- **Candle construction:** unchanged above the horizon. Below it, a daily bar the
  venue returns is dropped individually with one aggregated warn —
  `place_calendar_windows`' documented contract: *"A marker this instrument's
  calendar can place NO window for costs that one bar and nothing else: it is
  dropped, and the answer around it seeds (ANTI-DEGRADE)"*
  (`crates/app/src/history.rs:406-409`). Intraday bars pass through untouched
  (`:433-435`).
- **Session breaks / trade dates:** unchanged above the horizon; absent below it.
- **Is-open gate:** unreachable below the horizon (`now` is always above it).
- **Saving:** removes every carry-back convention and therefore the mechanism
  that produced 22 of the 57 executable-gap rows. On the SGX programme
  specifically, it removes the floor work — the year-inference from cell-border
  formatting, the 2009 psv-page discovery (#65) that re-keyed three floor rows,
  and the whole `#69` re-keying PR (A §5.3, C §3).

### 7.4 H3 — current + dated changes from a repo-wide date (e.g. 2020)

- **What it discards that is already paid for:** at a 2020 boundary, **185 of 279
  rows**, including **21 of Sharur's 35**. `globex_grains`' entire six-row
  timeline is pre-2020 (last change 2015-07-05) — so a 2020 boundary would
  declare *unknown* a grid the crate has correctly modelled and sourced since
  2015. `globex_nikkei_225_dollar` loses all four rows.
- **What it saves prospectively:** everything H2 saves, plus the judgement call
  H2 requires about what counts as "the earliest sufficient document". It is the
  cheapest of the three and the only one with a single repo-wide constant.
- **The asymmetry:** H3's saving is **entirely prospective**. Retrospectively it
  is a deletion of correct, paid-for information. H2 keeps every row that has a
  source and stops the *manufacture* of rows that do not.

### 7.5 What "unknown" must mean — the question the maintainer asked

Three implementable meanings, measured against Sharur's code:

| Meaning | Mechanism in Sharur | Verdict |
|---|---|---|
| **`Closed`** | `is_open` false → `consolidator.rs:189` drops; `close_time.rs:70` folds a historical bar into the next open window | **Unacceptable.** This is §1.1 under-open. It silently corrupts any bar below the boundary rather than declining to answer. |
| **Envelope** (carry the oldest sourced profile back — what H1 does today) | No change | Safe but dishonest: indistinguishable from "unchanged", which is exactly what `AGENTS.md:171-179` already concedes and what C §3(C) flags as a *surfacing* problem. |
| **`None` / absent** | `window_open_back` stops with a count + `report_unreachable_past` warn; `place_calendar_windows` drops individual daily bars with one aggregated warn; intraday untouched | **The correct answer, and it already works.** Sharur's `SessionCalendar` returns `Option` on three of five operations (`crates/domain/src/data/calendar/mod.rs:120,150,225`) and documents `None` as *"A countdown with no target shows nothing rather than a fabricated time"*. |

**The only genuinely open sub-question is `session_state` below the boundary.**
Sharur maps it 1:1 into `chart::session::SessionState` and `is_closure()` drives
axis compression. A below-horizon `Closed` would compress the pre-horizon span
out of the axis — which is arguably right (there are no bars there) and is
certainly harmless, because the bars were dropped anyway. A new
`SessionState::Unknown` would be a breaking enum change on a `#[non_exhaustive]`
type and would require a Sharur match-arm edit; it buys nothing the `None` on
the window operations does not already buy.

**Recommendation-shaped fact, not a decision:** the safe implementation of
"unknown" is *absent window* (`Option::None`), never `Closed` on `is_open`.

---

## 8. E1 / E2 — evidence policy

### 8.1 What E1 (primary-only + public-only) actually buys Sharur

Nothing that is currently observable. All eight of Sharur's keys are **Partial**
(§2.3), and seven of the eight gaps are in `order_entry`, a phase Sharur's
`is_open`, consolidator, DOM gate, bar grid and trade-date logic cannot see. The
highest-evidence keys in the crate (`globex_spot_quoted` Primary,
`cfe_vix` Primary, `eurex` Primary, `sgx` Primary) are either unreachable or
world-clock-only.

### 8.2 What E1 costs, measured

A §6 attributes ~35% of effort to retrieval and ~25% to adjudication — 60% of
the programme. The specific mechanisms:

- **The operator's own authoritative machine feed is excluded by rule.**
  `refdata.api.cmegroup.com/refdata/v3/tradingSchedules` returns `401`, therefore
  out of scope under `LAW-PUBLIC-SOURCES` (`AGENTS.md:30-35`; C §1.4(c)).
- **The permitted channel is failing.** `cmegroup.com` 403s at IP level; recent
  citations were read through a public text-extraction reader; `sources.md`
  carries a standing "Channel limit" note (A §6).
- **The law already bends in practice without a tier to record it.** SGX's
  2024-11-04 Japan move is dated by a Fubon **trading-member mirror** of DT/AM 50
  of 2024 — admitted because the mirror is public (C §4).
- **Unanimous measurement is rejected for want of a sentence.** Treasury TAS
  (6 roots), Dutch TTF TAS (2), commodity-index BTIC (9) are refused because
  *"none has a CME document stating hours in session language"*
  (`docs/schedules/unsupported-families.md:76-80`).
- **`LAW-SESSION-NOT-EXPIRY` (`AGENTS.md:61-90`) forbids the cheapest correct
  answer.** C §2(v): CME's own settlement-determination table matches the
  observed TAS closes **10 for 10**, in one document, ten rows — and the crate's
  law makes that coincidence *the reason to refuse* (Treasury TAS,
  `handoff:80`).

### 8.3 What E2 (tiered, Primary reserved for operator statements) would change

For Sharur: **still nothing directly**, because the tier of a row is not an input
to any computation. What it changes is which rows can exist:

- The 17 rejected trade-type roots become T2-sourced rows with an honest label
  rather than absent keys.
- `refdata/v3/tradingSchedules` and `TradingSessionList.dat` become admissible as
  T2 for the **envelope** (never for Regular-vs-Extended, which they do not
  publish — C §1.4(a)), which is precisely the field Sharur consumes and
  precisely the field it does not.
- The reader-extracted channel becomes a recorded field instead of a footnote —
  the plan is already asking for this by hand
  (`2026-09-12-cme-trade-type-keys.md:226`: each row should *"say which of its
  citations came through that channel"*).

**Cost of E2:** ~500 citation sites to backfill (279 revision rows + 132 ledger
rows + module comments across 91 files), plus a conflict-resolution rule the repo
currently handles case-by-case — and the ECBTC ruling turned on **document
lineage**, not tier (C §4), so a tier system must not overwrite that.

**The sharpest framing:** E1 is a policy about *the crate's standing as a public
artefact*. It is not a policy about SharurPlatform's correctness, and no measured
consumer outcome distinguishes E1 from E2.

---

## 9. X, R, M — holidays, rule shape, citation location

### 9.1 X1 / X2 / X3 — holidays

This is the **only** dimension in the whole review where the crate's current
policy produces a defect Sharur experiences every year, on every mapped root.

`LAW-HOLIDAY-SCOPE` (`AGENTS.md:90-101`) puts holidays out of scope. Sharur built
the `DayPolicy` seam (`crates/domain/src/data/calendar/exchange/mod.rs:111-125`),
which overlays every query in one place (`:142-151`) — and **never injects it**:
`with_day_policy` has four test-only uses
(`crates/domain/tests/unit/data/calendar/exchange/tests.rs:321,657,672,692`) and
no holiday table, file, fetch or crate exists in the workspace (B §4.1).

**Live consequences, today, on all 104 roots:**

| Purpose | Christmas / Thanksgiving / Good Friday | Early close (13:00 CT half-day) |
|---|---|---|
| Is-open gate | `is_open` true all day; DOM ladder armed all day (`dom/trading/mod.rs:115,125`); closed banner absent | armed for the 3 h after the real close |
| Candle construction | `window_open_back` places a window on a day that never traded | the last daily bar's `close_time` is hours late |
| Session breaks | no break drawn; the closed day is not compressed out of the axis | break at the wrong x |
| Trade date | the phantom day carries a trade date | the stamp moves with the wrong close |

**Magnitude.** `exchange_calendars`' `CMES` declares 3 full closures plus 10
special closes (C §1.5) — call it **~13 affected days per year**. On a 5 000-bar
daily chart (≈19 calendar years of trading days) that is **~250 phantom trading
days inside the requested window, ≈5% of it** — every day, on every instrument,
in both the live and the seeded path.

Compare with what the crate spends its effort on: a 15-minute uncertainty in a
2011 SGX T+1 close, on a key with **zero references anywhere in SharurPlatform**.

- **X1 (out of scope, status quo):** zero crate cost; the 5% error above is
  permanent and belongs to the consumer, who has not paid it in 24 days of crate
  work and shows no sign of doing so.
- **X2 (holidays in the crate):** every comparable library does this
  (`exchange_calendars`, `pandas_market_calendars`, LEAN, QuantLib — C §1.10:
  *"Everyone who models hours also models holidays"*). The known trap is that CME
  holiday behaviour is **per-family, not per-venue** — `exchange_calendars`'
  `CMES` source comment says so in writing and declines the split anyway
  (C §1.5). The crate's family granularity is the right shape for it. Cost
  scoped to the eight Sharur keys: ~13 rows/year/family ≈ **~100 rows/year**,
  against ~1,000+/year if scoped to all 96 exchanges + 36 keys.
- **X3 (separate crate/dataset):** identical data, different repository. It buys
  a release cadence (holidays change annually and errata are common) that the
  schedule crate does not want, and it costs a second dependency, a second
  version pin and a second review surface. It also keeps `LAW-DETERMINISM`
  intact.

The measured blocker on X2/X3 is performance, not scope: the overlay costs ~100×
on `is_open` and ~130× on the bar-window derivation
(`SharurPlatform/crates/domain/README.md:293-296`), a figure recorded as **not
re-measured** since 0.2.x (`docs/benches/stage-3.md:490`). At 4 999 `is_open`
calls per cold axis build (`crates/chart/tests/unit/charting/time_axis/context.rs:478-481`),
a 100× overlay turns 0.84 ms into 84 ms — a dropped frame. **Making the overlay
affordable is a prerequisite for X2 or X3 and is a crate-side task under any of
them.**

### 9.2 R1 / R2 — required fields

**R1 (regular + extended + order_entry all required)** is the status quo. Its
cost is concentrated in `regular`: research gate U-4 needed four independent
channels to establish `regular: &[]` for the trade-type shapes, and PLAN-58
requires *"each module comment naming the channels its own empty `regular` rests
on"* (A §2.4; `2026-09-12-cme-trade-type-keys.md:184-186`).

**What the split is worth, measured (§2.6):**

- 76 of 104 Sharur roots have `regular: &[]`; 5 more have `extended: &[]`.
  **81 of 104 roots (78%) cannot produce both open states.**
- `regular: &[]` is already correct for 13 of 36 key profiles and is specified
  for all 32 proposed keys — 45 of 68 after the plan.
- The two CME equity-index keys classify the same envelope oppositely (NKD
  regular-everywhere vs equity index 08:30–15:15), because the field tracks
  CME's use of the word "RTH".
- The split changes exactly **one** computed number in the consumer:
  `opens.regular` at `crates/chart/src/indicators/portable/inputs.rs:230`, the
  RTH-anchored session-VWAP trigger — which fires on only 23 of 104 roots.
  Everything else it feeds is a label or a colour
  (`ui/src/market_clock/{markets,color,paint,timeline}.rs`).

**`order_entry` earns its place and should not be optional.** It is what keeps
`OrderEntry` out of `is_open`, which is what stops the consolidator accepting a
print inside CME's Pre-Open (`crates/chart/src/session.rs:98` — `OrderEntry`
emits no bar because there is no price), and it is the second half of the
VWAP extended anchor (`inputs.rs:235`). Seven of Sharur's eight ledger gaps sit
in this field precisely *because* the crate models it.

**R2's shape, stated against the evidence:** session boundaries (the union) and
trade date are load-bearing for all four purposes. `order_entry` is load-bearing
for two. `regular` is load-bearing for one, on 22% of roots. R2 as phrased —
"RTH split only where a consumer builds RTH bars" — would make `regular`
optional and keep `order_entry` optional, which inverts the measured order of
value. **The evidence supports: boundaries + trade date required, `order_entry`
required, `regular` optional-and-declared.**

### 9.3 M1 / M2 — where the citation lives

`LAW-PRIMARY-SOURCES` requires the citation *"in a comment next to the table"*
(`AGENTS.md:23-29`).

**Measured prose volume (this pass):**

| Measure | Value |
|---|---:|
| `src/**/*.rs` total bytes | 1,028,187 |
| — comment lines | 8,425 |
| — comment bytes | **582,358 (56.6% of `src`)** |
| — code (non-comment, non-blank) lines | 14,029 (≈446 KB) |
| `src/calendar/schedules/**` bytes | 758,825 |
| — comment lines / bytes | 6,288 / **455,742 (60.1%)** |
| URLs in `schedules/**` | 1,008 |
| `docs/**/*.md` bytes | 464,513 |
| — `verification.md` | 168,695 bytes in 440 lines |
| — `sources.md` | 111,036 bytes in 478 lines |

**Evidence prose : Rust code ≈ 1,046,871 : 445,829 bytes = 2.35 : 1.**

**M2 is already invented, in the wrong place.**
`src/calendar/schedules/futures/international/sgx_equity_index/history.rs` is
454 lines of which **lines 1–340 are pure comment** (333 comment lines, 73%) and
only lines 341–454 hold rule tables; its own doc comment says it *"owns the
published evidence behind every row"*. Its sibling `eras.rs` was split off
*"so that module stays readable"*, and `sgx_equity_index_more.rs` states it was
split *"only to keep each production file within the source-reviewability
ceiling"* (A §3.6). **The crate is already paying the 500-line ceiling to store
prose inside `src/`.**

**What M2 would change:**

| | M1 (status quo) | M2 (evidence file under `docs/`, pointer in the module) |
|---|---|---|
| 500-line ceiling | Binds on prose. `futures_profile.rs` at 488/500; four modules split for the ceiling alone | Stops binding. ~5,000 comment lines leave `src/calendar/schedules/**`, taking it from 17,369 to ≈12,400 |
| Review diff locality | A reviewer sees the citation and the literal in one hunk | Two files per change; the fence tests must enforce the link |
| Fence tests | Already parse Markdown (`tests/schedule_documentation/`, 4 files, 1,455 lines, 25 tests) and already resolve owner-module and source-set links | The same machinery resolves the evidence-file link. **No new mechanism is needed.** |
| Law | Satisfied as written | `LAW-PRIMARY-SOURCES` must change "in a comment next to the table" to "in the key's evidence file, linked from the table" |
| Consumer | Irrelevant — Sharur consumes neither comments nor docs | Irrelevant |

**M1 vs M2 is a pure maintenance question with no consumer consequence at all.**
It is the cheapest structural change available in the whole review, and the
crate has already demonstrated it works.

---

## 10. Is the rigour protecting against something that cannot hurt Sharur?

### 10.1 Errors that cannot hurt Sharur — with the spend attached

| Class | Evidence it cannot hurt | Spend |
|---|---|---|
| **Any error in the 23 unreferenced keys** | Zero references anywhere in SharurPlatform (§2.1) | 23 of 36 key modules; the whole SGX pre-2020 programme (417 files / 101 MB / ~100 agent runs / 4 PRs / 10 days), the ECBTC adjudication (8 runs, 37 artefacts, one disputed hour), the five metals TAS keys, weather, spot-quoted, event contracts, rough rice, mini grains, the six ICE softs, Eurex fixed income |
| **Any pre-2020 revision row** | No Sharur query reaches there on purpose; the one that does (the daily walk) is unclamped by accident and gets 0 rows back (§2.5) | **185 of 279 rows (66%)**; the entire January-2010 floor apparatus (`AGENTS.md:171-195`), the carry-back convention, and the executable-gap population it creates |
| **Any `order_entry`-phase uncertainty** | `order_entry` is excluded from `is_open` by construction; it reaches Sharur only as a `QUEUE` label and one VWAP anchor | **7 of Sharur's 8 keys' entire documented gap** (`verification.md:405-412`); the 35 order-entry rows of the 57 Partial rows; four of Sharur's fourteen 2020+ rows are the `2026-08-22` knowledge-bound row widening a Sunday queue by 15 minutes |
| **The `regular`/`extended` classification on 81 of 104 roots** | Both states unreachable on those roots (§2.6) | Research gate U-4's four-channel establishment of `regular: &[]`; per-shape provenance for all 32 planned keys |
| **Any trade-type row** | Zero TAS/TAM/BTIC/TACO/TMAC references in SharurPlatform; neither adapter admits a non-`Future` kind | The whole 32-key plan (A §5.5) |

The task's own example is exact: **a 15-minute error in a 2011 SGX T+1 close is
unreachable three times over** — SGX equity index has no Sharur consumer, 2011 is
below any deliberate query, and the affected phase on the reachable SGX key is
order-entry.

### 10.2 Errors that would hurt — and whether current policy prevents them

| Class | Would it hurt? | Does the current policy prevent it? |
|---|---|---|
| **A wrong *current* close on a traded root** | **Yes, maximally.** Under-open drops live prints (`consolidator.rs:189`) and mis-folds seeded bars (`close_time.rs:70`). Over-open arms the DOM ladder on a closed book. | **Partly.** All eight keys' executable windows are sourced and dated. But the assurance is not differentiated: the same law and the same ledger row grade a 2011 SGX close and a 2026 CME crypto close. |
| **A missed *future* schedule change on a traded root** | **Yes.** `globex_cryptocurrency` carries a **forward-dated row for 2026-09-19** (`cryptocurrency.rs` REVISIONS), seven days after this measurement, on 21 Sharur roots. If a notice slips or a new one lands unnoticed, 21 roots get the wrong Saturday. | **Only by vigilance.** Eight of the nine crypto rows are 2026; the family changed three times in five weeks. Nothing in the governance prioritises monitoring a high-churn reachable key over archaeology on an unreachable one. |
| **A wrong trade-date roll on a weekend session** | **Yes.** `assign_normal` (`identity.rs:72-105`) rolls crypto weekend blocks to the following open **business** date with a 14-day lookahead, and Sharur stamps every bar with it (`inputs.rs:124`, `ui/src/session_calendar.rs:135`). 21 of 104 roots depend on this one hard-coded arm. | **Yes** — and this is the crate doing genuinely valuable, consumer-visible work that no comparable library does (C §1.10). |
| **Holidays and early closes** | **Yes** — ~13 days/year, ~5% of a 5 000-bar daily window, all four purposes, every root (§9.1). | **No. It is excluded by law and the seam is never injected.** |
| **`MAX_MAINTENANCE_GAP = 4 h` + the ISO-week rule** | **Yes.** `src/calendar/query/status.rs:18,98,118` decides `Maintenance` vs `Closed`, which drives `is_closure()`, which drives axis compression and session-break rendering on every chart. It is **crate policy, not an exchange fact** (A §2.3). | **Not by any law.** It is the one load-bearing heuristic in the engine and it carries no ledger row, no citation and no Basis. |

### 10.3 The imbalance, stated in one line each

- **185 of 279 revision rows are pre-2020; 35 of 279 are reachable; 2 of 35 fall
  in 2020–2025.**
- **7 of Sharur's 8 keys' entire documented uncertainty is in a phase
  `is_open` cannot see.**
- **The one defect that hits every root every year — holidays — is excluded by
  law, and the seam built for it has four test-only uses.**
- **The one heuristic that decides how every chart renders a gap has no
  citation, no ledger row and no Basis.**
- **Prose outweighs Rust in the crate by 2.35 : 1 by bytes.**

---

## 11. Ranking and coherent combinations

### 11.1 Granularity

Ranked by (harm to Sharur's core purposes, then maintenance cost):

| Rank | Policy | Harm to Sharur | Crate cost | Note |
|---:|---|---|---|---|
| 1 | **P2 (status quo shape)** | **None** — exact on all 104 roots | High but bounded; 8 of 41 modules earn it | The shape is right; the *admission rule* is what is unbounded |
| 2 | **P4 (map to underlying + flag)** | **None today** (no trade-type root exists in the catalog). If one were admitted: 0 for trade-date, 0 for bar content, 3.5–4.5 h for gating on metals/energy TAS, 5 min on grain/livestock TAS | ≈ zero | Consumer machinery already exists; `AGENTS.md:159-160` already licenses disclosed inaccuracy. Breaks on shapes with *more* structure than the underlying |
| 3 | **P5 (out of scope)** | Same as P4 **minus the disclosure**, and it contradicts `SharurPlatform/AGENTS.md:145-147` and `:589-590` if read as refusal | zero | **Strictly dominated by P4** |
| 4 | **P3 (32 keys)** | Zero harm, zero benefit | The largest single cost item in the review; breaches the 500-line guard at PR 3 | Justifiable only on the crate's public-artefact purpose, not on this consumer |
| 5 | **P1 (envelope only)** | **43% of roots materially wrong**, three groups badly, one of them data-destroying | ≈15,100 lines removed — the largest saving available | The only policy that can destroy data. Not survivable as stated |

### 11.2 History

| Rank | Policy | Harm | Saving |
|---:|---|---|---|
| 1 | **H2 (per-venue horizon, `None` below it)** | None — the graceful path is already exercised on 21 crypto roots | Removes every carry-back convention and the executable-gap population it manufactures; removes the SGX-floor class of work |
| 2 | **H3 (repo-wide boundary)** | None to Sharur; discards 185 already-paid-for rows including 21 of Sharur's 35 | Cheapest; one constant; no per-key judgement |
| 3 | **H1 (Jan-2010 floor)** | None to Sharur, but 85–115 ms per daily-chart open for 0 rows | Zero saving; the largest cost driver in the crate |

H2 and H3 are near-equivalent for this consumer. H2 preserves paid-for truth and
costs a per-key judgement; H3 is cheaper and throws paid-for truth away. **Both
require "unknown" = absent window, never `Closed`** (§7.5).

### 11.3 Evidence

No measured consumer outcome separates E1 from E2. **E2 dominates on cost**
(it readmits the operator's own machine channels, converts three refused root
groups into labelled rows, and turns the standing "channel limit" footnote into a
field) at the price of ~500 backfilled citation sites and a lineage-preserving
conflict rule. E1's value is reputational, and it is real: no other system
surveyed in C has a ledger at all.

### 11.4 Holidays

**X2 or X3 ≫ X1 on consumer harm, by a wide margin** — this is the only
dimension where current policy causes a recurring, measurable defect on every
root. X3 (separate crate/dataset) is the better shape: annual cadence, errata,
and it keeps `LAW-DETERMINISM` and the schedule crate's release discipline
intact. Either one is blocked on re-measuring and fixing the overlay's ~100×
cost — which is crate-side work under all three options.

### 11.5 Rule shape

**Boundaries + trade date required · `order_entry` required · `regular`
optional-and-declared** is what the measurements support. R1 over-invests in
`regular` (inert on 78% of roots, inconsistent between two CME equity-index keys)
and R2 as phrased under-invests in `order_entry` (which keeps `OrderEntry` out of
`is_open` and is the second half of the VWAP anchor).

### 11.6 Citation location

**M2 ≫ M1 on maintenance, with zero consumer consequence.** It is the cheapest
structural change in the review, the fence machinery already exists, and the
crate has already built one such file inside `src/` and paid the 500-line ceiling
for it.

### 11.7 Coherent combinations

**Coherent — "serve the consumer, keep the standing":**
`P2(+pruning rule) · P4 · H2 · E2 · X3 · R(boundaries+trade date+order_entry) · M2`
Every dimension pulls the same way: model what is reachable, at the depth
evidence exists, with the tier recorded, holidays supplied out of band, prose
out of `src`. Requires editing `LAW-PRIMARY-SOURCES` (M2), `LAW-PUBLIC-SOURCES`
(E2), `LAW-NO-FABRICATED-DATES`' floor clause (H2) and `LAW-HOLIDAY-SCOPE` (X3).

**Coherent — "public artefact first":** `P3 · H1 · E1 · X1 · R1 · M1`
The status quo plus the plan. Internally consistent, zero consumer benefit,
and it breaches its own 500-line guard at the plan's third PR.

**Coherent — "minimum viable calendar":** `P1(narrowed) · H3 · E2 · X3 · R2 · M2`
Only coherent if P1 is narrowed to "venue default, *plus* a key wherever the
default is measurably wrong" — which for Sharur is rates, crypto, livestock and
mini-vs-standard grains. As literal P1 it is incoherent with any consumer at all.

**Incoherent pairings to avoid:**

- **P3 + E1.** P3 adds 32 keys resting on the weakest retrieval channel the repo
  has, while E1 forbids the operator's machine feed that would date them. The
  plan already records this as a standing residual risk
  (`2026-09-12-cme-trade-type-keys.md:222-228`).
- **H3 + "unknown = Closed".** Introduces §1.1 under-open on 185 rows' worth of
  history at one stroke.
- **P4/P5 + X1.** Both rest on "disclosed inaccuracy is acceptable"; keeping
  holidays out of scope means the largest undisclosed inaccuracy in the system
  stays undisclosed, which undercuts the argument that licenses P4.
- **R1 + P3.** `regular: &[]` for all 32 proposed keys, each needing its own
  sourced justification for an empty field, on shapes where the field can never
  carry information.
- **M1 + the 500-line ceiling.** Already failing: `futures_profile.rs` at
  488/500, four modules split for the ceiling alone, and prose is 60% of
  `schedules/**` by bytes.

---

## 12. Corrections to reports A and B

1. **A's "the consumer's catalog is stale — `MZC`/`MZL`/`MZM`/`MZS`/`MZW` still
   point at `GlobexGrains`" is wrong.** Those are **Micro Ag** futures, and the
   crate itself states they belong on the standard grid:
   `src/calendar/futures_profile.rs:168` (*"and the Micro Ag futures, which follow
   the standard grid"*) and
   `src/calendar/schedules/futures/us/mini_grains.rs:28-29` (*"Excluded: … the
   Micro Ag futures MZC/MZS/MZW, which launched February 2022 on the standard
   grid"*). `GlobexMiniGrains` covers `XC`/`XK`/`XW`/`MKC`, none of which Sharur
   lists. **Sharur's mapping is correct; `GlobexMiniGrains` is simply
   unreachable.**
2. **A's URL count for `schedules/**` (1,224) and mine (1,008) differ** by
   counting method. Mine is `grep -oE "https?://[^ )\"]+"` over the concatenated
   tree. Both are order-of-magnitude consistent; neither is load-bearing.
3. **B's "28 crate keys are unreachable from any Sharur instrument … 17 entirely
   unreachable from SharurPlatform" understates it slightly.** The per-variant
   census (§2.1) gives **24 of 36 with no production reference** and **23 of 36
   with no reference of any kind**, including `AlwaysOpen`. `IceUsDollarIndex` has
   exactly one test-file reference.

---

## 13. Open questions this analysis could not close

1. **Is the daily walk's depth intentional?** A one-line clamp to
   `details().activation` in `crates/app/src/history.rs:229` would cap every
   Sharur query at the contract's listing date and make the entire pre-2020
   corpus unreachable by construction. Whether the maintainer wants that clamp
   decides most of the H1/H2/H3 argument.
2. **What is the `MAX_MAINTENANCE_GAP = 4 h` + ISO-week rule worth, empirically?**
   It has no citation and no ledger row, and it decides how every Sharur chart
   renders every gap. A sweep of its output against CME's
   `TradingSessionList.dat` transitions would be a computable answer.
3. **What does the `DayPolicy` overlay actually cost now?** The ~100×/~130×
   figures are recorded as not re-measured since 0.2.x
   (`SharurPlatform/docs/benches/stage-3.md:490`). X2 and X3 are both gated on
   this number.
4. **Is the pinned rev still fetchable?** `SharurPlatform/Cargo.toml:50` pins
   `a245618…`, which is not an ancestor of `main` (B §0). Independent of policy,
   a fresh clone may not resolve it.
5. **Would Sharur admit ICE U.S. or Eurex fixed income?** Rithmic's namespace
   census admits `NYBOT` and `EUREX`; the crate has correct keys for both; no
   root table reaches them, so today they would get a 12.5 h/day wrong envelope
   (§5.2). That is a live, current-schedule error on a traded venue — the exact
   class §10.2 says would hurt — and it costs zero crate work to fix.
6. **Does `TradingSessionList.dat` have a retrievable archive?** If CME's FTP
   directory or the Wayback CDX retains past weeks, T2 evidence acquires history,
   which changes both the E and the H calculus (C §6.2).
