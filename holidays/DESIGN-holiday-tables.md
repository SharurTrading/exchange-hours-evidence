<!-- SPDX-License-Identifier: MIT-0 -->

# DESIGN — built-in per-family holiday tables

**Written:** 2026-09-12 (UTC, `date -u`, LAW-UTC-DATES)
**Revised:** 2026-09-12 (UTC) — after the retrieval fix rounds and the second/third
adversarial verification rounds. Every number below is recounted from the current
result files; see **§8 Revision 2026-09-12** for what changed and why.
**Audience:** the maintainer, and the agent that implements this.
**Status:** decision memo. Nothing in `exchange-hours-rs` was modified.

**Inputs read in full**

| Input | What it settled |
|---|---|
| `holidays/cme-2010-2012 .. cme-2025-2027.json` (6 files) + `cfe-eurex-ice-cde-smfe-2026-2027.json` | The shape and volume of the retrieved evidence, and its vocabulary |
| the seven `*.verify.json` files — the **latest** verdict per task (superseded verdicts kept beside them as `*.verify.r1.json` / `*.verify.r2.json`, superseded results as `*.r0.json` / `*.r1.json`) | Which rows may ship and which must be re-retrieved first (**verdicts win**) |
| `src/calendar/policy.rs`, `policy/static_policy.rs` | `DayPolicy` / `StaticDayPolicy` vocabulary and its exact clipping contract |
| `src/calendar/exchange_calendar/mod.rs`, `query/schedule.rs`, `query/status.rs`, `query/sessions.rs`, `query/candles.rs` | Where an overlay attaches, and **why it costs ~100×** |
| `src/calendar/query/identity.rs` | The crypto weekend→business-date roll, and why it already does the right thing |
| `src/calendar/schedules/timeline.rs`, `schedules/profile.rs`, `exceptions.rs`, `exceptions/static_table.rs` | The static-table + const-eval-fence idiom this must copy |
| `architecture-review/B-sharur-consumption.md` §7, `D-consequences.md` §9.1 | The performance budget the table has to fit inside |
| `AGENTS.md` — LAW-HOLIDAY-SCOPE, LAW-PRIMARY-SOURCES, LAW-EVIDENCE-FILES, LAW-SERVICE-TIERS, LAW-NO-FABRICATED-DATES | The constraints this memo is not free to re-decide |

---

## 0. Decisions at a glance

| # | Question | Decision |
|---|---|---|
| D1 | Table key | The crate's **venue-local trade date**, never the operator's event date. The operator's own printed trade date is corroborating evidence for the conversion. |
| D2 | Row shape | `(trade_date, kind, tier, document_id)` in a `&'static [HolidayRow]`, strictly ascending, built by a `holidays!` macro with const-eval fences, exactly like `revisions!`. |
| D3 | Row kinds | `Closed`, `EarlyClose{ssm}`, `LateOpen{ssm}`, `LateOpenAndEarlyClose{..}`, `Unsourced`. No `Normal` rows. |
| D4 | Coverage | Every table carries an inclusive `(first, last)` trade-date window, mirroring `ExceptionCoverage`. In-coverage + no row = audited normal. Outside = "no answer". |
| D5 | Early close on a wrapping grid | Already correct under the existing `clamp_to_policy` semantics; no new mechanism. |
| D6 | Closure removing the prior-evening wrap | Already correct: `resolve_rule_bounds` drops any occurrence whose derived trade date is closed. No new mechanism. |
| D7 | Late open | Use the existing wrapped/unwrapped `late_open_ssm` disambiguation verbatim. A "late open" that would *create* a session the normal week does not have (the 2026-06-20 Saturday) is **not** a late open; it is a declared gap. |
| D8 | Mid-day-halt "modified" days | Triage first (most are the family's *normal* intraday grid). A genuine topology change is a **declared gap**, per LAW-HOLIDAY-SCOPE. |
| D9 | Crypto family | Ships `Closed` rows on holiday trade dates. They delete no trading; they make `identity::assign_normal`'s business-date roll skip the date. Requires the overlay to be live, which the built-in table makes it. |
| D10 | Where the table lives | `src/calendar/schedules/holidays/<owner>.rs`, one module per identity, resolved by a no-catch-all `table_for(CalendarSource)` match. |
| D11 | How it is applied | A third, **innermost** layer in `QueryContext`, resolved once per query, applied inside `resolve_rule_bounds` before the caller's `DayPolicy`. |
| D12 | Precedence | caller `SessionExceptionSource` (explicit `Closed`/`ReplaceSessions` only) → built-in table → caller `DayPolicy` clips. Clips compose by tightening (`min` close, `max` open, `OR` closed). |
| D13 | Public API added | Exactly three items: `holiday_on(trade_date)`, `holiday_coverage()`, `without_holidays()`. Nothing else. |
| D14 | Hot path | A **coverage gate**: one `partition_point` over the sorted rows before any trading-day derivation. ~97 % of days exit in ~20 ns. |
| D15 | Evidence tier | T1 preferred; **T2 admissible** and carried *in the row*, not only in a comment. T3/T4 rejected at compile time. |
| D16 | Evidence layout | `docs/evidence/<owner>.md` gains a `## Holidays` section, one subsection per year, one table row per holiday row; split to `docs/evidence/<owner>/holidays-<year>.md` when a file stops being reviewable. A fence checks every row's date appears there. |
| D17 | Venue calendars (`CME`, `CBOT`, `COMEX`, `NYMEX`) | Table = the **intersection** of the families that route to the venue. A date on which two families disagree ships no row and is a declared gap. |
| D18 | First wave | Served families, 2025–2027, **after** the four material round-2 findings against `cme-2025-2027` are repaired. Then backwards by three-year block. `cme-2016-2018` is **no longer blocked** — it has been verified three times and carries one load-bearing verbatim-attribution defect. |
| D19 | Performance gate | The table does not merge until the re-measured overlay cost meets §6's targets. This is the charter's own precondition ("cheap enough to sit on the consumer's hot path"), and D §9.1's. |

---

## 1. The data shape

### 1.1 Key the table by trade date, not by the operator's event date

Every retrieved record is keyed by the **operator's event date** and separately
records the operator's own trade date. From `cme-2025-2027.json`, MLK 2025:

```
Grains & Oilseeds (ZC)      | date 2025-01-19 | closed      | "eventDate 2025-01-19: 16:00 preopen (trade date 2025-01-21)"
Equity Index (ES); Rates(ZN)| date 2025-01-20 | early_close | "eventDate 2025-01-20: 12:00 preopen; 17:00 open (trade date 2025-01-21)"
Grains & Oilseeds (ZC)      | date 2025-01-20 | closed      | "eventDate 2025-01-20: 19:00 open (trade date 2025-01-21)"
```

Those three event-date records are **two** crate rows:

- `globex_equity_index` / `globex_interest_rates`: `EarlyClose(2025-01-20, 12:00 CT)`.
  The Sunday-evening open runs into Monday and stops at 12:00 instead of 16:00.
- `globex_grains`: `Closed(2025-01-20)`. The Sunday 19:00 leg that would have fed
  trade date Monday is deleted **by that one row** — which is precisely what the
  `2025-01-19` event record is describing.

This is the single most important normalisation in the whole migration, and it
is what makes the table small and unambiguous: **an eve record is evidence for
the holiday's row, not a row of its own** — unless the eve carries an early
close of its *own* trade date, as Christmas Eve does
(`2025-12-24: 12:15 closed (trade date 2025-12-24)` → `EarlyClose(2025-12-24, 12:15 CT)`).

It also resolves the verifier's advisory C against the venue task. CFE prints
`New Year's Day,2026-01-01,None,5:00 PM (Thu) to 8:30 AM (Fri)` and the task
recorded `closed` despite the non-empty Extended cell. On a trade-date key that
is correct and needs no defence: the 17:00 Thursday block belongs to trade date
Friday 2026-01-02; trade date 2026-01-01 has neither a regular session nor the
Wednesday-evening block that would have fed it. Record the reasoning; test it.

### 1.2 Row and table types

Copy the `revisions!` idiom (`schedules/timeline.rs:56-107`) exactly — it is the
crate's established way to make a static table's invariants build failures.

```rust
// src/calendar/schedules/holidays/mod.rs
pub(crate) enum HolidayKind {
    Closed,
    EarlyClose { close_ssm: u32 },
    LateOpen { open_ssm: u32 },
    LateOpenAndEarlyClose { open_ssm: u32, close_ssm: u32 },
    Unsourced,
}

pub(crate) struct HolidayRow {
    pub(crate) trade_date: NaiveDate,
    pub(crate) kind: HolidayKind,
    pub(crate) tier: EvidenceTier,     // T1 | T2 only
    pub(crate) document: SourceRef,    // reuse timeline::SourceRef
}

pub(crate) struct HolidayTable {
    pub(crate) first: NaiveDate,       // inclusive coverage start
    pub(crate) last: NaiveDate,        // inclusive coverage end
    pub(crate) rows: &'static [HolidayRow],
}
```

`holidays!` const-asserts, at build time:

1. trade dates strictly ascending (the `partition_point` search needs a total order — `assert_ascending`, `timeline.rs:88`);
2. every row's `document` non-empty (`assert_cited`, `timeline.rs:101`);
3. every row's `tier` is `T1` or `T2` — a T3/T4 holiday row does not compile;
4. `close_ssm <= 86_400`, `open_ssm < 86_400` (the `StaticDayPolicy` ranges, `static_policy.rs:184-200`);
5. every row inside `[first, last]` (the `StaticSessionExceptions` rule).

**Tier and document id go in the row, not in an adjacent comment.** LAW-EVIDENCE-FILES
says "a row's tier and document id live beside the row". With ~200–250 rows per family a
comment line per row doubles the module and cannot be mechanically checked; a typed
field can be, and fence (3) then makes "a holiday sourced at T4" unrepresentable.

**No `Normal` rows.** `StaticSessionExceptions` offers `known_normal` for callers;
the built-in table does not need it. In-coverage-with-no-row already means audited
normal, and the audit itself is recorded in the evidence file where a human can read
the quotation. Rows are reserved for dates that change an answer.

**`Unsourced` earns its variant.** The retrieval still produces genuine unknowns, but
they have moved: `cme-2022-2024` now has **13** `unknown` rows (every one
`globex_nikkei_225_dollar`, 2024-01-15 .. 2024-12-31 — CME's T2 service returns only
the ten representative products the trading-hours page requests and no Nikkei is
among them), `cme-2016-2018` now has **0** (the 2017-12-25 cryptocurrency row was
closed from CME's 2017 annual bundle, which does print a `Bitcoin` row), and
`cme-2025-2027` still has 2 — though its round-2 verifier proved **both** closeable
from the live T2 service and they should not ship as `Unsourced`. A
contiguous coverage window forces a choice between claiming those dates are normal
and cutting the window in half. `Unsourced` says the third thing, costs one enum
variant, does nothing at runtime (it clips nothing, exactly like `DateException::OutOfCoverage`,
`exceptions.rs:156-170`), and is visible through `holiday_on`. The precedent is
already in the crate; follow it.

### 1.3 Early close on a wrapping Sun–Fri 17:00→16:00 CT grid

**No new mechanism is needed.** Take the Friday after Thanksgiving 2025,
`EarlyClose(2025-11-28, 12:15 CT)` for `globex_equity_index`. `clamp_to_policy`
(`schedule.rs:362-397`) computes `cutoff = mk_local_close(tz, 2025-11-28, 12:15)`
and applies `close = close.min(cutoff)` to every occurrence whose derived trade
date is 2025-11-28:

| Occurrence | Raw | After clip |
|---|---|---|
| wrapped extended, Thu 17:00 → Fri 16:00 | opens Thu | closes Fri 12:15 |
| regular, Fri 08:30 → 15:15 | closes Fri 15:15 | closes Fri 12:15 |
| extended, Fri 15:15 → 16:00 | opens Fri 15:15 | dropped — `open < close` fails (`schedule.rs:396`) |

The clip is stated on the **trade date**, so it lands on the correct civil day for
a session that opened the previous evening, and the occurrence that begins after
the cutoff disappears rather than inverting. This is already tested for
`StaticDayPolicy`; the built-in table inherits it unchanged.

One factual update since this example was written. The 2025-11-28 rows are now
sourced from CME's **finalised** Thanksgiving publication (capture
`20260129012309`), which the round-1 verifier proved exists and the retrieval had
denied. The close instants are unchanged (`12:15 CT` equity/rates, `13:45 CT`
FX/energy/metals/crypto, `12:05 CT` grains/livestock/lumber), so §1.3's table still
holds row for row — but the finalised publication additionally prints a
`07:00 preopen; 07:30 open` pair on that trade date that the superseded publication
did not. An open at 07:30 CT is **earlier** than the family's normal 08:30 CT regular
open, so it is not a `LateOpen`, and the scalar vocabulary cannot state it. It is an
intraday-topology item for §1.6's triage, not a change to the early-close row.

### 1.4 A closure that removes the prior-evening wrap

Also no new mechanism. `Closed(2025-12-25)` for `globex_equity_index`:
`resolve_rule_bounds` derives each occurrence's trade date and returns `None` when
that date is closed (`schedule.rs:349-355`). The Wednesday 17:00 CT block, whose
trade date is Thursday 2025-12-25, disappears. The Thursday 17:00 CT block, whose
trade date is Friday 2025-12-26, is untouched — which matches CME exactly
(`eventDate 2025-12-25: 16:00 preopen; 17:00 open (trade date 2025-12-26)`).

One residue: that record's pre-open starts at 16:00, not the normal 16:45 (the
research's note `[N17]`). That is a **queue** difference. `DayPolicy` has no
order-entry boundary and the table copies its vocabulary, so an order-entry-only
deviation is **not representable** and is recorded as a gap in the evidence file.
It changes no `is_open` answer, only `is_accepting_orders` / `is_order_entry_only`
for 45 minutes. Record it; do not model it; do not let it block the row.

The round-1 verifier of `cme-2025-2027` raised the same class of thing as its
discrepancy 3: 17 rows carry note `[N3]` ("16:00 preopen; 17:00 open") and were
labelled `normal`, but on those dates the family has **no final close and therefore
no trade date of its own** — e.g. FX on 2025-01-20 carries trade date 2025-01-21
throughout. The fix round accepted it: **all 17 `[N3]` rows now read
`status: "modified"`**, and the round-2 verifier re-counted them programmatically and
marked the item RESOLVED. That does not change what the crate must do. On a
trade-date key those rows are `Closed(2025-01-20)`, not `normal` and not "modified":
there is no trade date 2025-01-20, so no session is assigned to it. **Every `[N3]`
row must be re-classified `Closed` during the migration** — the retrieval's
`modified` is the honest limit of *its* vocabulary, and the crate's existing
vocabulary says the rest.

The round-2 verifier then found the same defect in a place the fix round did not
carry it through (its discrepancy 4, material): **six Cryptocurrency rows on Friday
holidays** — 2026-06-19, 2026-07-03, 2026-12-25, 2027-01-01, 2027-03-26, 2027-06-18 —
are still labelled `normal` with note `[N8]`. Their event *times* equal the normal
Friday grid, but their 16:00 CT final close carries the **following Monday's** trade
date instead of the Friday's own (verified against each row's own cited bytes:
`2026-12-25 -> /TD 2026-12-28`, and so on), where the reference week prints
`16:00 closed /TD 2026-10-23` for an ordinary Friday. Those six are the same
`Closed(trade_date)` case as the `[N3]` rows and must be triaged identically. The
twelve rows still labelled `normal` in `cme-2025-2027` are exactly these six plus
three 2027-12-23 agricultural rows and three 2028-01-01 rows (the last of which,
Cryptocurrency on a Saturday, is genuinely normal for that grid).

### 1.5 A late open after a closed day

Use `late_open_ssm` with the existing disambiguation, stated at `policy.rs:51-56`
and implemented at `schedule.rs:380-394`:

- a reopen at 19:00 CT on the evening of 2025-12-25 for trade date 2025-12-26 →
  `LateOpen(2025-12-26, 19*3600)`. `19:00 ≥` the normal first open (17:00) so the
  cutoff lands on the **preceding** local date. Correct.
- a reopen at 08:30 CT on the trade date itself → `LateOpen(td, 8*3600+30*60)`.
  `08:30 <` 17:00 so the cutoff lands on the trade date. Correct.

Both branches must be tested per family that has a late open — the branch choice is
data-dependent and silently produces a 24-hour error if it flips.

**What is not a late open.** `cme-2025-2027` carries
`eventDate 2026-06-20: 05:00 open; 17:00 closed (trade date 2026-06-22)` — a
**Saturday** session, on a grid whose normal week has none. `late_open_ssm` can only
push an existing occurrence later; it cannot create one. Same for 2026-07-04 and
2027-06-19. These are **declared gaps** for the scalar table and the natural first
customers for the v2 block rows named in §7.

### 1.6 A "modified" day with a mid-day halt

LAW-HOLIDAY-SCOPE settles the outcome ("not representable by scalar boundaries and
is recorded as a gap") but not the triage, and the triage is where the work is:
the retrieved data now carries **~220 `modified` rows** across the eight served keys
(up from ~145 before the fix rounds — the `[N3]` re-classification and
`cme-2022-2024`'s new 16:00-CT early-close rule moved rows *into* this bucket), and
most of them are not modified at all.

```
Grains, 2026-04-02: 07:45 paused; 08:00 preopen; 08:30 open; 13:20 paused;
                    13:30 closed; 14:30 pcp; 16:00 closed   [N7]  -> "modified"
```

That is the ordinary CBOT grain day. What is actually different is that there is no
19:00 evening leg — because 2026-04-03 (Good Friday) is closed, and `Closed(2026-04-03)`
already deletes it (§1.4). The row is **normal**.

**Triage rule, to be applied to every `modified` row and recorded per row:**

1. Resolve the family's normal-week profile for that era (`hours_at` at the date).
2. Compare the printed intraday phases against it.
3. Identical → the row is `Normal` (no crate row) and, if the difference is only a
   missing evening leg, the neighbouring `Closed` row already carries it.
4. Differs only in the final close instant → `EarlyClose`.
5. Differs only in the first open instant → `LateOpen`.
6. Anything else — an extra halt, a phase removed mid-day, a split session, a
   regular/extended asymmetry — → **declared gap**, quoted in the evidence file,
   and an issue for a served identity (LAW-FOLLOW-UPS-ARE-ISSUES).

`cme-2013-2015`'s own `missing[7]` says the same thing from the evidence side:
"none of these documents describes what happens to a family's internal phases …
Anything finer is a gap." So most category-6 outcomes will be *unsourced* topology
rather than *sourced-but-unrepresentable* topology, which is a cheaper gap to carry.

### 1.7 The cryptocurrency family

`globex_cryptocurrency` is 24/7 from trade date 2026-05-30 (CME filing 26-114,
`cryptocurrency.rs:182-187`). The data says holidays do not stop it:

```
Cryptocurrency (BTC), eventDate 2026-06-19 (Juneteenth):
  16:00 closed; 16:01 preopen; 16:02 open (trade date 2026-06-22)   [N8] -> "normal"
```

That row is one of the six the round-2 verifier requires be re-labelled `modified`
(§1.4): the 16:00 CT close carries Monday 2026-06-22, not the Friday. The verifier's
finding **confirms** the reading below rather than disturbing it — it is the
operator's own statement that Cryptocurrency has no trade date of its own on that
Friday. Note also that the retrieval's coverage prose ("on holidays it publishes only
'16:01 preopen / 16:02 open', the 16:00 CT final close is omitted") is true only of
the Monday and Thursday holidays; on the six Friday holidays the 16:00 CT close *is*
printed and it is the trade date that moves (verifier discrepancy 6).

Trading is continuous; the **trade date rolls past the holiday**. The crate already
implements exactly this — `identity::assign_normal` (`identity.rs:99-113`) walks
forward from the nominal date, skipping weekends and any date an overlay closes,
up to `TRADE_DATE_LOOKAHEAD_DAYS`.

**Therefore: the crypto table ships `Closed` rows on holiday trade dates.** The row
means "there is no trade date 2026-06-19", not "no trading happens". Two consequences
the implementer must hold onto:

- The roll only runs when an overlay is attached (`identity.rs:100`,
  `!context.has_overlay()`). `has_overlay()` must be extended to include the
  built-in table, or the table ships and the roll stays dead.
- The roll is what stops `resolve_rule_bounds` from **deleting a whole day of
  trading**. A Wednesday-opening block whose default trade date is a closed
  Thursday gets re-assigned to Friday, is therefore not closed, and survives. If
  the roll and the table are wired up in the wrong order, the 24/7 family goes dark
  on every holiday. This is the single highest-risk interaction in the change; §4
  makes it a required test.
- Pre-2026-05-30 crypto has `has_weekend_close: true`, which short-circuits the roll
  (`identity.rs:100`) — so the same `Closed` rows behave as ordinary closures in the
  five-day era, which is what the 2018–2025 data shows. Both eras need a test.

---

## 2. Application, hot path, layering, and public API

### 2.1 Where the table attaches

`ExchangeCalendar` stays `Copy` and keeps holding only a `CalendarSource`
(`exchange_calendar/mod.rs:64-67`). The table is resolved **once per query**, when
the `QueryContext` is built:

```rust
// query/schedule.rs
struct QueryContext<'a> {
    source: ProfileSource<'a>,
    tz: Tz,
    holidays: Option<&'static HolidayTable>,   // NEW, resolved in ::date_aware / ::overlay
    policy: Option<&'a dyn DayPolicy>,
    exceptions: Option<&'a dyn SessionExceptionSource>,
}
```

`QueryContext::fixed` gets `None`: a detached `MarketHours` snapshot has no identity,
and the crate already refuses to infer one ("never guess a family from coincident
rules", AGENTS.md). Resolution is a no-catch-all `match` in
`schedules/holidays/mod.rs`, mirroring `hours_for_market_hours_key`, so a new key
cannot silently acquire or lose a table.

`hours_at` and `session_profile` continue to return the **unmodified** normal-week
profile. The table applies to queries, not to tables — the rule `policy.rs:96-98`
already states for the overlays.

### 2.2 Precedence

1. **Caller `SessionExceptionSource`** — an explicit `Closed` or `ReplaceSessions`
   record wins outright and suppresses the built-in row for that trade date.
2. **Built-in family table.**
3. **Caller `DayPolicy`** — clips whatever survives.

Composition is monotone-tightening: `is_closed` is `OR`, `early_close_ssm` is `min`,
`late_open_ssm` is `max`. A caller can always make a day shorter; a caller cannot
widen the crate's answer with a `DayPolicy`.

**`KnownNormal` deliberately does not suppress the built-in row.** It is not
distinguishable at the trait level from "in coverage, no record"
(`StaticSessionExceptions::exception_on` returns `KnownNormal` for both), so treating
it as an assertion would silently disable the whole built-in table for every caller
who attaches an exception provider. The per-date undo channel is therefore
`ReplaceSessions` with the family's normal blocks, and the coarse undo is
`without_holidays()` (§2.4). Document both.

### 2.3 Making the lookup cheap — the coverage gate

This is the part that decides whether the feature ships. Today, the moment **any**
overlay is attached, `resolve_rule_bounds` (`schedule.rs:324-360`) does this **per
rule, per candidate day, inside `is_open`**:

```rust
if !context.has_overlay() { return Some((raw_open, raw_close)); }   // the fast path today
...
let final_close = candles::candle_end_with(&baseline, raw_open, Daily, Both);   // ~17-23 µs
let first_open  = candles::candle_start_with(&baseline, raw_open, Daily, Both); // ~17-23 µs
let trade_date  = context.normal_trade_date_for_bounds(raw_open, final_close);
```

`candle_start_with(Daily)` routes to `period_start`, which calls `candle_end_with`
again and then walks up to 21 `daily_close_for_trade_date` probes plus a
`next_session_after_with` (`query/candles.rs:104-156`). Two full trading-day
derivations, per rule, to compute one date. Against B §7's measured 167.7 ns
baseline `is_open` and 17–23 µs daily window, **that is the ~100× — it is not a
mystery and it is not inherent.**

Once the table ships by default, `has_overlay()` becomes true for every query on
every family that has a table. So the gate is not an optimisation; it is a
precondition.

**The gate.** The overlay can only change an answer if some layer has a record for
a trade date that an occurrence opening on local day `D` could be assigned to. That
set is bounded and known at compile time from the identity's own conventions:

| Identity class | Trade dates reachable from open day `D` | Gate window |
|---|---|---|
| ordinary (close-date default) | `D`, `D+1` | `[D, D+1]` |
| `SetThailand` (prior opening date, `identity.rs:52-58`) | `D-1`, `D`, `D+1` | `[D-1, D+1]` |
| `GlobexRoughRice` (following local date, `identity.rs:69-76`) | `D`, `D+1` | `[D, D+1]` |
| `GlobexCryptocurrency`, `GlobexEventContractsBtc` (business-date roll, `identity.rs:99-113`) | up to `D+3+14` | `[D, D+18]` |

Then, before any derivation:

```rust
if !context.any_layer_may_affect(first_candidate, last_candidate) {
    return Some((raw_open, raw_close));
}
```

- built-in table: one `partition_point` over `rows` plus a coverage-window compare —
  ~8 comparisons over a ~250-row slice, no allocation, no branch misprediction worth
  naming.
- caller `SessionExceptionSource`: `coverage()` is already a cheap `(first, last)`
  compare (`exceptions.rs:172-200`).
- caller `DayPolicy`: opaque. Add a **provided** trait method
  `fn may_affect(&self, first: NaiveDate, last: NaiveDate) -> bool { true }`,
  implemented by `StaticDayPolicy` as the same `partition_point`. Defaulting to
  `true` keeps every existing implementation source- and behaviour-compatible; it is
  a non-breaking addition that lets the crate's own `StaticDayPolicy` — and the
  consumer's records — buy the same 97 % exit.

On ~239 of 252 trading days a year the gate exits with one binary search. On the
remaining ~13 the expensive path runs exactly as it does today.

**Two further reductions, in priority order, to be applied if §6's measurement says
the holiday-day cost still matters:**

1. `first_open` (`schedule.rs:342-348`) is used **only** by the late-open branch of
   `clamp_to_policy`. Compute it lazily, behind `late_open_ssm(trade_date).is_some()`.
   Late opens are rare (30 rows in grains, 19 in livestock, 6 in equity index across
   18 years), so
   this removes roughly half the remaining cost from ~99 % of overlay-affected
   queries.
2. Hoist the trade-date derivation out of the per-rule loop in `find_occurrence`
   (`schedule.rs:286-305`). Two rules on one open day can belong to different trade
   dates (grains' Monday 08:30–13:20 day session vs. its Monday 19:00 evening leg),
   so memoise per `(open_day, wraps_to_next_day)` rather than per open day. Do this
   only if measured — it is a real refactor and the gate may make it unnecessary.

Do **not** reach for interior mutability inside `QueryContext`: it is `Copy` and a
`Cell` would take that away for no benefit the hoist does not already give.

### 2.4 The public API — three items, no more

```rust
#[non_exhaustive]
pub enum HolidayKind { Closed, EarlyClose { close_ssm: u32 }, LateOpen { open_ssm: u32 },
                       LateOpenAndEarlyClose { open_ssm: u32, close_ssm: u32 }, Unsourced }

pub struct Holiday { /* kind(), document_id() -> &'static str, tier() -> EvidenceTier */ }

pub struct HolidayCoverage { /* first(), last(), contains() — mirrors ExceptionCoverage */ }

impl ExchangeCalendar {
    pub fn holiday_on(self, trade_date: NaiveDate) -> Option<Holiday>;
    pub fn holiday_coverage(self) -> Option<HolidayCoverage>;
    pub const fn without_holidays(self) -> Self;
}
```

Mirrored on `PolicyCalendar`, documented there as **reporting the built-in row only**
— the caller's own layers are introspected through the existing
`session_exception_on` (`policy.rs:178-183`).

- `holiday_on` returning `None` means *either* "no table" *or* "outside coverage" *or*
  "audited normal". `holiday_coverage()` is what separates them, which is why both
  exist and why neither is enough alone. This is the same three-way distinction
  `DateException::OutOfCoverage` was introduced for (`exceptions.rs:156-170`).
- `without_holidays()` is `const`, costs one `bool`, gives the consumer an exact A/B
  for the benchmark in §6, and is the escape hatch when a shipped row is wrong and
  the consumer cannot wait for a release.

**Deliberately not added:** holidays-in-a-range iteration, `is_early_close`, a
per-year accessor, a `Holiday` list, a `DayPolicy` impl over the built-in table.
Each is a caller convenience over data the three accessors already expose, and each
would have to be kept correct forever.

### 2.5 What comes along for free

Everything routes through `resolve_rule_bounds`, so `session_bounds`,
`next_session_after`, `session_state`, `trade_date`, `candle_end`, the weekly and
monthly boundaries, the bulk builders and the trading-day derivation all become
holiday-aware with no further change. That is the payoff for putting the table under
the existing overlay seam instead of beside it.

Two behaviours that will surprise someone and must be documented where they live:

- `is_closed_all_day_on(holiday)` can be **false** on a full closure, because the
  next trade date's session opens on the holiday evening. `is_closed_trade_date` is
  the query that answers "was this a holiday" (`policy.rs:325-338` already says so
  for `DayPolicy`).
- An `Unsourced` row changes no answer. That is deliberate, and it is why
  `holiday_on` exists.

---

## 3. Evidence tier and the per-family-year evidence layout

### 3.1 Tier

LAW-HOLIDAY-SCOPE asks for T1. The retrieved corpus is not uniformly T1 and
pretending otherwise would be the fabrication the charter exists to prevent:

| Block | Dominant tier | What it is |
|---|---|---|
| 2010–2021 | **T1** | CME's own per-holiday PDF / XLS Globex schedules |
| 2022–2023 | **T1** | the 2022 XLS sheets and the 2023 one-pagers (219 of `cme-2022-2024`'s 362 rows) |
| 2024 | **T2** | CME's trading-hours service JSON, read as bytes and saved. The fix round retrieved the six windows the verifier proved recoverable, so this block grew from 66 to **143** T2 rows and now covers all ten 2024 U.S. holidays plus the 3 July early close |
| 2025–2027 | **T2** | same service (all 313 rows); `cme-2025-2027` `missing[4]` records that no T1 per-asset-class rendering could be driven out of the page. One T1 operator page (`D50`) corroborates Good Friday 2026 but states no instants |
| CFE / Eurex / ICE / CDE 2026 | **T1** | operator hours pages, calendar PDFs, exchange notices, market notices. **All 203 rows are now T1 and none is `unknown`** (5 of them Eurex 2027, which is T1-but-indicative and does not ship — §5.2 Wave 8) |

**Decision:** T1 and T2 both ship, the tier is carried in the row (§1.2), and
LAW-PRIMARY-SOURCES is satisfied as written — T2 is "the operator's own machine
channel … read as bytes and saved", which is exactly what these captures are. The
absence of a T1 rendering for 2024–2027 is recorded as a named gap on each affected
ledger row, not as a reason to withhold the rows. T3 and T4 do not compile.

### 3.2 Document ids

The research files use per-file local namespaces (`D02` in `cme-2025-2027` is not
`D02` in `cme-2013-2015`; `D13GF`, `CBOE-HOURS-USFUT-2026`, `IFUS-CAL-2026`,
`2012-good-friday.pdf`). Those collide the moment two blocks land in one module.

**Scheme:** the document id is the operator artifact's own stable name where it has
one (`2012-good-friday.pdf`, `CDE-MN-26-01`), and otherwise
`<OWNER>-HOL-<YYYY>-<SLUG>` (`CME-HOL-2025-THANKSGIVING`,
`CME-SVC-2026-06-19` for a service window). Ids are unique repository-wide, resolved
in the evidence file to URL, capture/retrieval time in UTC, sha256 and tier. A fence
asserts that every id used in a module appears in that owner's evidence file.

### 3.3 Evidence file layout

Keep LAW-EVIDENCE-FILES' one-file-per-owner rule. `docs/evidence/<owner>.md` gains:

```markdown
## Holidays

**Coverage:** 2010-01-01 .. 2027-12-31 (inclusive trade dates). Tier: T1 to 2023-12-31, T2 from 2024-01-01.

### 2025

| Trade date | Kind | Instant as printed | Document | Tier | Derived from |
|---|---|---|---|---|---|
| 2025-01-20 | early close | `12:00 preopen` — 12:00 CT (13:00 ET) | `CME-SVC-2025-01-20` | T2 | eventDate 2025-01-20, CME trade date 2025-01-21 |
| 2025-11-28 | early close | `12:15 closed` — 12:15 CT (13:15 ET) | `CME-HOL-2025-THANKSGIVING` | T2 | eventDate 2025-11-28, CME trade date 2025-11-28 |
| 2025-12-25 | closed      | `no events published` | `CME-HOL-2025-CHRISTMAS` | T2 | eventDate 2025-12-25 |

**Gaps, 2025:** …  **Interpretive steps, 2025:** …
```

Rules, all mechanically checkable:

- One subsection per **year** — this is the per-family-year unit the task asks for
  and it is the unit a LAW-WATCH review actually works in.
- The **instant is quoted exactly as printed, in both zones CME prints** (CT with ET
  in parentheses), beside the crate's normalised SSM. `cme-2019-2021`'s verifier
  discrepancy D5 is precisely a case of a task inserting a `CT` token the operator
  did not print; quoting the cell text and bracketing any editorial insertion is the
  remedy it names, and it becomes the house rule here.
- A **`Derived from` column** recording the operator's event date(s) and the
  operator's own printed trade date. This is the audit trail for the §1.1
  conversion and the only way a later reader can re-check it.
- **Gaps and interpretive steps per year**, not pooled at the end of the file.
- If a file stops being reviewable, split to `docs/evidence/<owner>/holidays-<year>.md`
  and link from the owner file. Do not split to make room for narrative.

**New fence** (mirroring the existing revision-date fence): every `trade_date` in a
family's holiday module appears in that family's evidence file, and every evidence
row's date appears in the module or is listed under that year's gaps. This is the
fence that stops a row from shipping without its quotation.

**Ledger.** `docs/schedules/verification.md` rows gain nothing structural — the
fixed shape already carries `Evidence tier`, `Horizon`, `Reviewed on`, `Cadence` and
a basis note. Add the holiday coverage window and the named holiday gaps to the
basis note, and set `Cadence` to **monthly** for every family with a shipped table:
the operator publishes next year's calendar annually and issues errata, which is
exactly LAW-WATCH's "changed within the last year" trigger.

---

## 4. Tests

`TEST-LAYOUT` applies: integration tests over the public surface only, thin
top-level harness (`tests/holiday_tables.rs`) with per-identity submodules
(`tests/holiday_tables/<owner>.rs`).

### 4.1 Per served family, seven required cases

For each of the eight family keys, pick real dates from that family's own shipped
rows and assert against the **public** surface:

| # | Case | Assertions |
|---|---|---|
| 1 | **A closed day** | `is_closed_trade_date(d, Both)` true; `is_open` false at three probes inside the civil day; `holiday_on(d)` is `Closed`; `is_open` false at the *previous* evening's normal open instant (the wrap is gone, §1.4); `next_session_after` from the eve's morning lands on the correct post-holiday open |
| 2 | **An early close — before** | `is_open(cutoff - 1ns)` true |
| 3 | **An early close — at** | `is_open(cutoff)` false; `session_bounds` for the day ends exactly at `cutoff`; `candle_end(Daily)` equals `cutoff`; the post-cutoff same-day occurrence is absent |
| 4 | **A late open** | `is_open(cutoff - 1ns)` false and `is_open(cutoff)` true, **for both branches** — one row whose ssm ≥ the normal first open (cutoff on the preceding local date) and one whose ssm < it (cutoff on the trade date) |
| 5 | **A wrap removed** | the Christmas shape: no session at 17:30 CT on 12-24; `next_session_after(12-24 12:20 CT)` returns the 12-25 17:00 CT open, not the 12-24 one |
| 6 | **The trade-date consequence** | `trade_date` inside a shortened day still returns the holiday's trade date; `trade_date` at the eve's evening open returns the *post*-holiday date; and for `globex_cryptocurrency`, `trade_date` rolls past the closed date **while `is_open` stays true throughout** — the 24/7 no-deletion invariant of §1.7, tested on a mid-week holiday (Christmas Thursday → Friday) and a Monday holiday (→ Tuesday), in both the five-day and the 24/7 era |
| 7 | **Both sides of coverage** | `holiday_coverage()` returns the declared `(first, last)`; `holiday_on(first - 1 day)` and `holiday_on(last + 1 day)` are `None`; `is_open` on `last + 1 day` equals the pure normal-week answer (the table does not silently extend); a known holiday one day outside coverage is **not** applied |

### 4.2 Crate-wide

- **No-op regression.** Every identity **without** a table answers bit-identically to
  today. Extend `tests/golden_grids.rs` rather than writing a parallel harness.
- **`without_holidays()` identity.** For a family **with** a table,
  `without_holidays()` reproduces the pre-table answers over a dense instant grid
  across a holiday week. This is both a contract test and the benchmark's control.
- **Gate soundness (the one that prevents a silent wrong answer).** For each
  identity, over a dense grid spanning every shipped row ±3 days, assert the gated
  path and an ungated reference path agree exactly. The gate window table in §2.3 is
  a *claim about the identity's conventions*; this test is what makes it true rather
  than hoped.
- **Layering.** Caller `ReplaceSessions` overrides a built-in row; caller
  `DayPolicy::is_closed` closes a date the table left open; a caller early close
  earlier than the table's wins and a later one does not; `KnownNormal` does **not**
  suppress a built-in row.
- **Const-eval fences.** `trybuild`-style or documented compile-fail coverage for
  each of the five `holidays!` assertions, including "a T3 holiday row does not
  compile".
- **Evidence fence.** Every row's date appears in the evidence file (§3.3).
- **Mutation check.** For each family, perturb one shipped instant by one minute and
  confirm at least one test fails — the crate's existing practice for cutover
  fences, applied to holiday rows.

---

## 5. Migration order

### 5.1 Verdict inventory — what may ship, and when

Verdicts win over results. **All seven** retrieval tasks now have a verifier, and
six of the seven have been through a fix round and a second (or third) adversarial
round. The verdict that governs is the one in `<task>.verify.json`; earlier verdicts
are kept as `<task>.verify.r1.json` / `.r2.json` and earlier results as
`<task>.r0.json` / `.r1.json`.

| Block | Latest verdict | Load-bearing findings that must be repaired **before** rows ship |
|---|---|---|
| `cme-2025-2027` | round 2, `matches: false`, 7 discrepancies (**4 material**) | All seven round-1 findings are RESOLVED and independently re-checked. The four material round-2 findings are all consequences of one false premise the task repeats — "the live service carries only FORWARD holidays": (1) `missing[0]`/`missing[1]` are **false for nine holidays** — the live service still answers for windows back to Thanksgiving 2025 for the THBP-B product set, so **NKD/NIY, ZS, ZW, HE and DC are sourced** for Thanksgiving 2025, Christmas 2025, New Year 2026, MLK 2026, Presidents' 2026, Good Friday 2026, Memorial 2026, Juneteenth 2026 and Independence 2026 (Good Friday 2026: NKD and NIY print `08:15 closed /TD 2026-04-03` — the Equity Index instant, **not** the 10:15 CT of ZN/6E/BTC); (2) the **two remaining `unknown` rows** (Cryptocurrency 2026-06-17 and 2026-07-02) are closeable from the same channel and currently quote a publication the task itself labels superseded; (3) Saturday 2025-11-29 is **not** a gap — the live service returns all ten THBP-A products with no events, i.e. a sourced `Closed`; (4) the **six Friday Cryptocurrency rows** of §1.4 |
| `cme-2022-2024` | round 2, **FAIL**, 6 discrepancies (2 load-bearing) | Both round-1 load-bearing findings are RESOLVED: the six 2024 windows were retrieved (T2 rows 66 → 143; 7 new dates; the **ES 12:15 CT early close on 2024-07-03 is now recorded**), corroborated by a second vintage (the 2024-12-20 crawl is byte-identical to the 2024-07-08 crawl), and four `TRADE DATE`-out-of-an-empty-cell verbatims were corrected. Remaining: (1) a **fifth instance of the same verbatim over-claim** — 2023-11-23 GRAINS still quotes a `TRADE DATE: FRI 24 NOV` label from a cell that is empty; (2) a **false zone-provenance claim** — three of the seven one-pagers print the Central Time sentence once, in the header only, not in header *and* footer |
| `cme-2019-2021` | round 2, **FAIL on evidence discipline only**, 4 discrepancies (**0 load-bearing**) | "No date, status, tier or instant VALUE is wrong anywhere in the 440 family rows, and none is inferred from another year." The fabricated 2019-01-01 Nikkei quotation, the Wayback-error-page artifact, the two misrecorded capture dates and the ten inserted `CT` tokens are all RESOLVED. Remaining, none of which blocks a row: (N1) the *corrected* index now makes a **false enumeration claim** — a standalone 2020 Good Friday workbook **does** exist in the archive (the fix round's crawl was windowed `from=2019 to=2023` and could not see the 2024 capture); (N2) the paraphrased-instant class survives outside the eleven rewritten fields; (N3) 67 files still hashed nowhere while the addendum implies otherwise; (N4) **314 `verbatim`/instant fields hard-truncated mid-token** at a fixed character budget, contrary to the file's own stated notation, losing part of a printed instant in two named fields |
| `cme-2016-2018` | round 3, `matches: false`, 4 discrepancies (**1 load-bearing**) | **No longer unverified.** All 11 round-2 findings are RESOLVED against the bytes: the 2017 and 2018 annual bundles were retrieved (they carry CME's *final* revisions and supersede eight per-file captures), 167/167 hashes reproduce, 8/8 re-fetched documents are byte-identical, ET = CT+1 holds on all 375 rows, and no row cites a document from another year. Remaining load-bearing: on **2018-07-03, 2018-11-23 and 2018-12-24** the Grains verbatim still quotes a sibling `MGEX Apple Juice` row that CME **deleted** in the very revisions those rows were re-keyed to, so three claimed quotations are not in their cited documents. "No instant, status or family-level value is wrong anywhere in the file." |
| `cme-2013-2015` | round 2, `matches: false`, 12 discrepancies (**5 load-bearing**) | All 8 round-1 findings are RESOLVED: the `.xls` class was retrieved (45 documents, 28 newly cited, including both 2013 multi-sheet bundles and the 2014/2015 annual master workbooks), the `interest_rates+fx` grouping is now *confirmed* rather than assumed, 41 rows gained a corroborating per-product instant, 11 rows carry a `superseded` statement with lineage, and **the 2015 Labor Day T1-vs-T1 conflict is resolved by lineage** — CME's September 2015 revision prints `16:00` Regular Fri. Close where the March 2015 draft printed `15:15` Early Fri. Close, so the row is `normal` and the earlier statement is recorded as superseded. Remaining: (1) **`2013-4th-of-july-done.pdf` — CME's later revision of the 2013 Independence Day schedule — sits in BOTH rounds' own saved CDX enumerations and was retrieved by neither**; it moves Dairy, Lumber and Livestock into explicit early closes at 1200/1202/1215 CT on 2013-07-03, which the file records as `normal`: **a wrong final-state status**; (2) the same revision prints `1215 CT — Early MGEX Wheat & Apple Juice close` for grains; (3) 42 earlier distinct-digest captures of the cited PDF URLs were never retrieved while `missing[10]` presents the superseded set as complete, and two of them carry different session values; (4) `missing[2]`'s "Good Friday 2013 1355 zone unknown" is **already closed by a document in this corpus** (`X13GFPD`'s `Good Fri.` sheet, Notes row "All times are CT"); (5) the "57 of 58 Interest-Rate/FX row pairs are identical" claim has a counterexample |
| `cme-2010-2012` | round 1, **PASS** (8 defects, none load-bearing) | None blocking, and **no fix round has run** — all eight defects stand. Fix the quoting convention (20 joined lines), the 92 instants not quoted in their own row's verbatim, the `nikkei 2010-02-15` label (defect H: CME's words are an *exception to the group's Sunday open*, not a modification of the Nikkei's own schedule), the 2012 Good Friday canonical capture (which replays now), the 2010-12-23 energy parenthetical sourced from an uncited document, and the `five`/`six` count typo before carrying rows across |
| `cfe-eurex-ice-cde-smfe-2026-2027` | round 2, **`matches: true`**, **0 discrepancies**, 4 advisories | **Nothing blocks.** Both round-1 load-bearing findings are RESOLVED: the **Coinbase Derivatives 2026 MLK false negative is corrected** (notice `CDE-MN-26-01` retrieved and re-fetched byte-identical — `Energy, Metal & Equity` = `closed` "Closed for holiday", `Crypto (24x7)` = `normal`), and the untested "archive unreachable" claim is withdrawn in three places, which surfaced a fresher ICE 2026 calendar variant now cited. Independently: 53/53 artifacts re-hash, 10/10 re-fetched documents byte-identical, 121 ICE entries machine-checked cell-by-cell with zero mismatches, **all 203 entries T1 and none `unknown`**. The four advisories are record-hygiene only (see §8) |

### 5.2 Waves

**Wave 0 — the engine, with no data.** The gate (§2.3), the types and macro (§1.2),
the three API items (§2.4), the fences, the no-op regression and the benchmark
harness (§6). Merges with **zero rows** and therefore zero behaviour change, and
publishes the re-measured overlay number. This is the wave that decides whether the
rest is affordable, and it is sized to LAW-BOUNDED-WORK.

**Wave 1 — served families, 2025-01-01 .. the published future.** All eight keys.
Repair the **four material round-2** `cme-2025-2027` findings first — they are all one
retrieval: re-query the live trading-hours service (it answers back to Thanksgiving
2025) for the THBP-B product set over the nine named windows, for Cryptocurrency on
2026-06-17 and 2026-07-02, and for Saturday 2025-11-29; then re-label the six Friday
Cryptocurrency rows. That closes `missing[0]`, `missing[1]`, `missing[2]` and
`missing[6]` and removes both remaining `Unsourced` rows from this block. Coverage `last` = 2027-12-31 for the
seven families CME has published through 2027 (`cme-2025-2027` runs to 2028-01-01);
this is the charter's "operator's published future" and LAW-NO-FABRICATED-DATES
explicitly permits encoding it ahead of its effective day.

**Wave 2 — 2022-01-01 .. 2024-12-31.** The 2024 T2 retrieval the round-1 verifier
proved recoverable **has been done**: all ten 2024 U.S. holidays plus the 3 July early
close are recorded, on a second-vintage-corroborated capture. Repair the two remaining
load-bearing evidence defects (the 2023-11-23 grains verbatim, the zone-provenance
sentence) and ship. 2023 MLK / Presidents' Day / Good Friday remain genuine gaps —
re-confirmed empty at every 200 capture in round 2 — so they ship as `Unsourced` rows,
not as silence; and `globex_nikkei_225_dollar` ships **13 `Unsourced` rows across 2024**,
because the T2 service returns only ten representative products and no Nikkei is among
them.

**Wave 3 — 2019-01-01 .. 2021-12-31.** The fabricated quotation and all nine other
round-1 findings are repaired, and the round-2 verdict is explicit that **no value is
wrong in any of the 440 rows**. What is left is evidence discipline, and two items of
it touch the rows: repair the 314 hard-truncated `verbatim`/instant fields before the
evidence file is written from them (two of those fields lose part of a printed
instant), and withdraw the false "the archive holds no standalone 2020 Good Friday
workbook" claim — it does, and the fix round's crawl window hid it. Juneteenth
2019–2021 has no CME document at all: `Unsourced`.

**Wave 4 — 2016-01-01 .. 2018-12-31. Unblocked.** The verification task ran, and ran
three times. The caution was justified: it found that CME's *annual bundles* carry the
final revisions and that eight per-file captures were superseded, which moved 140 rows
on 13 dates and changed four substantive values (2017 Christmas Bitcoin row and a
withdrawn grain leg; 2018-07-03 Bitcoin early close 12:15; 2018-12-25 Bitcoin "Globex
Closed"; 2018-12-26 Equity 15:15/15:30). One load-bearing defect remains and it is
narrow — three Grains verbatims quote an `MGEX Apple Juice` sibling row CME deleted in
those same revisions. Repair the three quotations; the instants and statuses stand.

**Wave 5 — 2013-01-01 .. 2015-12-31.** The excluded `.xls` class **has been retrieved**
(45 documents, 28 newly cited) and the 2015 Labor Day T1-vs-T1 conflict is **resolved by
lineage alone** — CME's own September 2015 revision supersedes the March 2015 draft, so
nothing has to be withheld and the intersection rule is not reached. The wave is now
blocked on a *different* retrieval: `2013-4th-of-july-done.pdf`, CME's later revision of
the 2013 Independence Day schedule, which sits in both rounds' own saved CDX
enumerations and was never downloaded. It changes a recorded status (Dairy, Lumber and
Livestock on 2013-07-03 are early closes at 1200/1202/1215 CT, recorded as `normal`), so
no 2013-07-03 row may ship until it is read. Take the 42 unretrieved earlier captures of
the cited PDF URLs in the same pass.

**Wave 6 — 2010-01-01 .. 2012-12-31.** Lowest risk; the January-2010 floor lands here
and closes the served-identity obligation.

**Wave 7 — venues.** `CBOT` = `globex_grains` ∩ `globex_interest_rates`;
`COMEX`/`NYMEX` = the metals and energy halves of `globex_energy` (which agree on
15/15 shared dates in 2022–2024, so the intersection is nearly lossless); `CME` =
the intersection of the six families that route to it. Full closures agree across
families; most early closes do not, and those dates ship no venue row and are named
gaps. This is D17, and it is the honest reading of LAW-PRIMARY-SOURCES' conflict rule.

**Wave 8 — `CFE`, `EUREX`, `ICE Futures U.S.`, `Coinbase Derivatives`, `SMFE`.**
2026-01-01 onwards only; there is **no** retrieved history below 2026 for any of
them, so their coverage windows start there and their ledger rows say so plainly.
The two load-bearing venue findings **are repaired** and this is the one block whose
verifier returns `matches: true` — it is the natural candidate to move ahead of the
CME blocks if a wave has to be re-ordered. Note three data facts that shape
these rows: Eurex 2027 is published "on a preliminary and indicative basis" and is
therefore **not** an unconditional dated future (LAW-NO-FABRICATED-DATES — it does
not ship); Eurex's additional German closures for FDAX/FDXM are printed as "to be
announced"; and SMFE publishes nothing because the DCM is dormant (CFTC no-action,
2026-07-24), which is a service-tier fact, not a gap.

### 5.3 Rows the retrieved data implies

Non-normal dated rows per served key per year, after mapping the seven retrieval
vocabularies onto the eight crate keys. **These are pre-triage magnitudes**, not
final counts: §1.4's `[N3]` re-classification will move rows between kinds, §1.6's
triage will delete most `modified` rows and promote a few to gaps, and §1.1's
event-date→trade-date collapse removes the eve duplicates. Recounted 2026-09-12 from
the current result files; the previous counts are in parentheses where they moved.

```
key              10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27   TOT
equity_index     10 10 14 14 13 11 10 11 12 12 11 10 10  9 14 15 15 14    215  (208)
interest_rates   17 16 18 17 16 14 10 10 11 11 11 10 10  8 13 14 15 14    235  (229)
fx               17 16 18 17 16 14 10 10 11 11 11 10 10  8 13 14 15 14    235  (212)
energy           17 10 11 11 11 11 10 10 11 11 11 10 10  8 13 14 16 14    209  (203)
grains           11 10 15 15 15 14 11 12 12 13 13 10 10  9 14 23 22 21    250  (242)
livestock        11 11 15 14 16 16 11 12 12 13 13 10 10  8 12 12 12 11    219  (212)
crypto            -  -  -  -  -  -  -  1 12 12 11 10 10  8 13 14  9  7    107   (90)
nikkei            1  -  -  -  -  - 10 11 12 12 12 11 10  9 14  -  6 14    122  (113)
                                                                        -----
                                                                         1,592 (1,509)
```

≈ **199 rows per family**, ≈ **1,600 rows across the eight keys**, ≈ 11–16 per
family-year. That is still the same order as D §9.1's estimate ("~13 affected days per
year … ~100 rows/year") and it is still small: eight modules of 200–350 lines each,
well inside the 500-line reviewability guard, with no need to fragment by decade.
**No sizing or layout decision changes.**

Where the 83 extra rows come from: the six 2024 windows `cme-2022-2024` retrieved
(the whole 2024 column moves from 6–7 to 12–14 per key), the seventeen `[N3]` rows
`cme-2025-2027` re-labelled (which is why `fx` 2025–2027 jumps from 8/10/8 to
14/15/14), the 2018-12-26 entry `cme-2016-2018` added from the 2018 bundle, the
2015-07-06 entry `cme-2013-2015` added, and fourteen `cme-2019-2021` rows that moved
off `normal`.

Kind mix across the eight keys: **551 closed** (was ~533), **739 early close** (~749),
**67 late open** (~61), **220 `modified`** (~145, to be triaged), **15 `unknown`** (9).
Late opens remain rare — 30 in grains, 19 in livestock, 6 each in equity index,
interest rates and FX, none anywhere else — so §2.3's lazy `first_open` is still
nearly free.

### 5.4 What the retrieval could not source

Carry these as `Unsourced` rows (inside coverage) or as coverage limits, and open an
issue for each on a served identity (LAW-FOLLOW-UPS-ARE-ISSUES):

1. **2023 MLK, Presidents' Day, Good Friday — all families.** Still genuine, and
   independently re-confirmed in round 2 (`neg_api_2023-01-15/-02-19/-04-06.json`:
   `hasEvents:false` at every 200 capture that exists). Good Friday 2023 matters most:
   CME is understood to have run a limited session around the employment report, so
   this is not a repeat-of-last-year gap.
2. **Juneteenth 2019, 2020, 2021 — all families.** No CME document of any kind.
   Unchanged.
3. **Columbus Day / Veterans Day, most years.** CME publishes settlement and clearing
   advisories but no Globex trading schedule. 2013 is the exception and is a positive
   T1 statement of normality ("Products listed on Globex are unaffected"). For the
   other years, coverage is contiguous, so these dates read as normal; that has to be
   named in the evidence file rather than left implicit. Unchanged.
4. **`globex_nikkei_225_dollar` as a distinct printed line — now three different
   situations, not one.** (a) **2010–2023 and 2025 through Labor Day 2025:** CME prints
   no Nikkei row; the family is governed by the Equity Index block, ships with the
   Equity document id, and the interpretive step is recorded per year. The 2019-01-01
   row's fabricated quotation is **repaired**; the 2010-02-15 `modified` label still
   has to be re-decided (`cme-2010-2012` verify defect H — CME's words are an exception
   to the *group's* Sunday open, not a modification of the Nikkei's own schedule).
   (b) **2024:** 13 rows are genuinely `Unsourced` — the T2 service returns only ten
   representative products and no Nikkei is among them. (c) **Thanksgiving 2025
   onwards:** NKD and NIY **are** separately published by the live service and must be
   retrieved rather than inferred; on Good Friday 2026 they print `08:15 closed` —
   the Equity Index instant, not the 10:15 CT of ZN/6E/BTC — which corroborates the
   interpretive step for that date but does not licence keeping it.
5. **`globex_grains` / `globex_livestock` / dairy sub-lines before Labor Day 2026
   (ZS, ZW, HE, DC).** Same channel and same correction as item 4(c): declared missing,
   in fact served by the live T2 channel for nine holidays from Thanksgiving 2025.
6. **Order-entry-phase deviations on holidays** (§1.4). Not representable; no `is_open`
   consequence. Unchanged.
7. **Intraday topology on "modified" days** (§1.6). Mostly unsourced rather than
   unrepresentable. Now ~220 rows to triage rather than ~145. The 2025-11-28
   `07:00 preopen; 07:30 open` pair (§1.3) is a new, *sourced* member of this class.
8. **The 2026-06-20 / 2026-07-04 / 2027-06-19 Saturday sessions** (§1.5). Sourced,
   unrepresentable under the scalar vocabulary. The strongest argument for §7's v2.
   **Saturday 2025-11-29 is no longer in this list in either direction** — the live
   service publishes all ten products with no events for it, so it is a sourced
   `Closed`, not a gap and not a session.
9. **A T1 rendering for 2024–2027.** T2 only; recorded per ledger row. Unchanged.
10. **Venue history below 2026** for CFE, Eurex, ICE US, CDE, SMFE. Not retrieved at all.
    Unchanged.
11. **ICE Daily Gold and Silver** may close on further LBMA holidays announced by
    Exchange Notice; the calendar is not exhaustive by the operator's own admission.
    Unchanged. Related and also unchanged: every ICE date marked `open1` on the 2026
    and 2027 calendars carries no instant by construction, CFE has published no 2027
    schedule, Eurex's additional German closures for FDAX/FDXM are printed "to be
    announced", and CDE's 2026 Thanksgiving and Christmas notices had not issued at
    retrieval.
12. **2013-07-03 Dairy / Lumber / Livestock — a gap the corpus does not yet know it
    has.** `2013-4th-of-july-done.pdf` (CME's later revision, in both saved CDX
    enumerations, retrieved by neither round) states early closes at 1200/1202/1215 CT
    where the file records `normal`. Until it is read, those rows are not merely
    unsourced, they are **wrong**, which is why Wave 5 is blocked on it.

---

## 6. The performance plan

### 6.1 What is being claimed, and what is actually measured

The ~100× `is_open` / ~130× bar-window multiplier comes from
`SharurPlatform/crates/domain/README.md:293-296` and is recorded as **not
re-measured since 0.2.x** (`docs/benches/stage-3.md:490`). It is not re-measured
here either. What §2.3 establishes is the *mechanism* — two full daily-window
derivations per rule per candidate day, against a 167.7 ns baseline — which makes a
two-order-of-magnitude multiplier entirely credible and, more usefully, removable.

### 6.2 How to re-measure

Extend `benches/calendar_queries.rs` (it currently benches `GlobexEquityIndex`
without any overlay) to a matrix:

- **query** × `{is_open, session_state, trade_date, candle_end(Daily), session_bounds}`
- **instant class** × `{regular, overnight, maintenance, closed}` — B §7's four, so the
  numbers are directly comparable
- **date class** × `{far from any holiday, adjacent to a holiday (±1 day), on a holiday}`
- **layer** × `{none, built-in table, StaticDayPolicy only, built-in + StaticDayPolicy,
  without_holidays()}`

Plus one **shape benchmark that reproduces the consumer's cold frame**: 4,999
`is_open` + 1 `session_close` over a 5,000-point window
(`chart/tests/unit/charting/time_axis/context.rs:478-481`), reported as a single
per-build figure. That is the number that decides whether a frame drops, and it is
the one to put in the CHANGELOG.

Report with the machine, the toolchain and the UTC date (LAW-UTC-DATES). Criterion
in CI is not a gate; the recorded number is the artifact.

### 6.3 Targets

| Measurement | Baseline (B §7) | Target with the built-in table |
|---|---|---|
| `is_open`, regular, far from a holiday | 167.7 ns | **≤ 195 ns** (≤ +15 %, i.e. the gate only) |
| `is_open`, closed weekend, far from a holiday | 361.8 ns | **≤ 420 ns** |
| `is_open`, on or adjacent to a holiday | 167.7 ns | **≤ 3 µs** (the real derivation, ~13 days/yr) |
| cold axis: 4,999 `is_open` + 1 `session_close` | 0.84 ms regular / 1.8 ms closed | **≤ 1.1 ms / ≤ 2.2 ms** — against ~84 ms at the unfixed 100× |
| daily trading-day derivation (`TradingDayMemo` unit) | 17–23 µs | **≤ 30 µs** far from a holiday |
| `StaticDayPolicy` attached, date not covered | ~100× (claimed) | **≤ 2×**, once `may_affect` ships |

**The table does not merge until the far-from-a-holiday rows are met.** LAW-HOLIDAY-SCOPE
requires holiday lookups "cheap enough to sit on the consumer's hot path"; D §9.1
calls making the overlay affordable "a prerequisite … and a crate-side task under
any" option. Wave 0 exists to satisfy that before a single row ships. If the gate
does not reach the target, apply §2.3's reductions 1 and 2 and re-measure; if it
still does not, the design question reopens before the data work is spent.

---

## 7. Named follow-ups

Each of these is an issue before its wave merges (LAW-FOLLOW-UPS-ARE-ISSUES):

**Closed since the first draft** (kept here so the ledger shows the disposition, not
just the disappearance): verify `cme-2016-2018` — done, three rounds, Wave 4 unblocked;
re-retrieve the six 2024 holidays — done, including the ES 12:15 CT early close on
2024-07-03; rebuild the 2019-01-01 `globex_nikkei_225_dollar` row — done; retrieve the
`.xls` class for 2013–2015 and resolve the 2015 Labor Day T1-vs-T1 conflict — done, and
the conflict dissolved on lineage; retrieve CDE notice `26-01` and re-run the skipped
archive enumeration — done, and that block's verifier now returns `matches: true`.

**Open:**

1. **Re-query CME's live trading-hours service for the nine windows back to
   Thanksgiving 2025**, for the THBP-B product set (NKD, NIY, ZS, ZW, HE, DC), for
   Cryptocurrency on 2026-06-17 and 2026-07-02, and for Saturday 2025-11-29. This
   single retrieval closes four `cme-2025-2027` `missing[]` entries and both remaining
   `Unsourced` rows, and it is Wave 1's precondition.
2. **Re-label the six Friday Cryptocurrency rows** in `cme-2025-2027` (§1.4), and
   correct the coverage sentence that says the 16:00 CT close is omitted on holidays —
   it is omitted on Monday and Thursday holidays only.
3. **Retrieve `2013-4th-of-july-done.pdf`** and the 42 unretrieved earlier captures of
   the cited 2013–2015 PDF URLs. Wave 5 is blocked on the first of these because it
   changes a recorded status.
4. **Repair the three `MGEX Apple Juice` verbatims** in `cme-2016-2018`
   (2018-07-03, 2018-11-23, 2018-12-24) — the sibling row was deleted in the very
   revisions those rows cite.
5. **Repair `cme-2022-2024`'s fifth `TRADE DATE`-from-an-empty-cell verbatim**
   (2023-11-23 grains) and its zone-provenance sentence.
6. **Un-truncate `cme-2019-2021`'s 314 `verbatim`/instant fields** before any evidence
   file is generated from them, and withdraw the false "no standalone 2020 Good Friday
   workbook exists" claim.
7. **Correct the eight `cme-2010-2012` defects.** No fix round has run on that block at
   all; it is the only block whose verifier findings are entirely unactioned.
8. **v2 block rows.** A fifth `HolidayKind` carrying
   `&'static [ExceptionBlock]` — the public type already exists
   (`exceptions.rs:57-152`) and the replacement scan already exists
   (`query/replacement.rs`), so the incremental cost is a macro arm, a fence and the
   evidence work. It is what turns §5.4 items 5 and 7 from gaps into rows. It needs a
   LAW-HOLIDAY-SCOPE amendment ("recorded as a gap" becomes "recorded as a gap until a
   block row can state it"), so it is the maintainer's call, not the implementer's.
9. **`DayPolicy::may_affect`** as a provided trait method, so the consumer's own
   overlay gets the same gate.
10. **Venue-intersection audit.** Confirm the family agreement assumption behind D17
    across all waves, not only the 15 dates checked in 2022–2024.

---

## 8. Revision 2026-09-12 (after verification fixes)

This memo was written against the round-0 results and the round-1 verdicts. Six of
the seven retrieval tasks then ran a **fix round**, and every task was re-verified —
`cme-2016-2018` three times. This section records what moved. **No decision in §0 is
withdrawn or amended.** Every corrected fact either confirmed a decision (D1, D9) or
changed only a count, a wave's precondition, or a follow-up's disposition.

### 8.1 What changed in the data

| Change | Effect on this memo |
|---|---|
| `cme-2022-2024` retrieved the six 2024 T2 windows the verifier proved recoverable — 7 new dates, 285 → 362 rows, T2 rows 66 → 143, **and the ES 12:15 CT early close on 2024-07-03 is now recorded** | §5.3's whole 2024 column moves from 6–7 to 12–14 per key; Wave 2's precondition is met; follow-up 2 closes |
| `cme-2022-2024` settled a single early-close rule across all three years: the 16:00 CT holiday halt CME prints for FX and Cryptocurrency on holiday Mondays and Thursdays is the families' *ordinary* final close, so **28 rows moved from `early_close` to `modified`** | Explains most of the early-close/modified swing in §5.3's kind mix; the crate's triage (§1.4, §1.6) is unaffected — those rows are `Closed(trade_date)` either way |
| `cme-2025-2027` re-labelled **all 17 `[N3]` rows** `normal` → `modified`, and re-sourced Thanksgiving 2025 from the finalised capture `20260129012309` | §1.4's re-classification rule is now supported by the retrieval's own vocabulary; §1.3's early-close instants are unchanged but the finalised publication adds a `07:00 preopen; 07:30 open` pair |
| `cme-2025-2027` fixed the 2025-07-03 Equity Index row to `early_close` / `12:15 CT`, defined `N17`/`N18`, and published a working re-fetch path | Three of the five round-1 findings §5.1 listed are gone |
| `cme-2016-2018` retrieved the 2017 and 2018 **annual bundles**, which carry CME's final revisions and supersede eight per-file captures — 140 rows re-keyed on 13 dates, four substantive value changes, a new 2018-12-26 entry, 363 → 375 rows, and the last `unknown` row closed | Wave 4 unblocked; §1.2's "`cme-2016-2018` has 1 `unknown` row" is now 0; **this is the concrete vindication of D15/§3's insistence that the evidence file record which capture a row rests on** |
| `cme-2013-2015` retrieved the excluded `.xls` class — 45 documents, 28 newly cited, 41 corroborating instants, 11 superseded statements with lineage, a new 2015-07-06 entry, and the `interest_rates+fx` grouping confirmed rather than assumed | Wave 5's first precondition is met; the 2015 Labor Day T1-vs-T1 conflict **dissolved on lineage** and never reached the intersection rule |
| `cme-2019-2021` repaired all ten round-1 findings, including the fabricated 2019-01-01 Nikkei quotation; 14 rows moved off `normal`, 424 → 440 | §5.4 item 4's "must be rebuilt from scratch" is discharged; follow-up 3 closes |
| `cfe-eurex-ice-cde-smfe-2026-2027` retrieved CDE notice `26-01`, withdrew the untested "archive unreachable" claim, and cited a fresher ICE 2026 calendar — **the last `unknown` row is gone and all 203 entries are T1** | The only block with a clean verdict; follow-up 5 closes |

### 8.2 Verified clean vs. still carrying discrepancies

**Verified clean — nothing load-bearing outstanding:**

- **`cfe-eurex-ice-cde-smfe-2026-2027`** — round 2, `"matches": true`,
  `"new_load_bearing_discrepancies": 0`. Verbatim:
  *"No load-bearing defect remains. Four non-blocking advisories are recorded below."*
  The four advisories are record hygiene and label fidelity, not values: **G** *"the
  restated rule is incomplete"* (the JSON is right); **H** a Contentful href quoted
  with the escaping normalised; **I** the round-0 `INDEX.md` still asserts three
  statements the fix disproved, with no pointer to the correction — *"A reader who
  opens only that file is misled"*; **J** *"A small number of ICE family labels are
  lightly normalised rather than reproduced as printed … Each is a label, never a
  status or an instant."*
- **`cme-2019-2021`** — round 2 is a `FAIL` on discipline with **no load-bearing
  finding**. Verbatim: *"FAIL on evidence discipline only — every load-bearing holiday
  fact now reproduces. … No date, status, tier or instant VALUE is wrong anywhere in
  the 440 family rows, and none is inferred from another year."* Treat its rows as
  shippable once N4's truncation is repaired, because the evidence file is generated
  from those strings.
- **`cme-2010-2012`** — round 1 `PASS`. Verbatim: *"PASS — nothing load-bearing fails.
  Every recorded instant is backed verbatim by the cited T1 CME Group document; no
  instant is inferred from another year; the archive holds nothing that the 'missing'
  list wrongly claims is absent."* Caveat: **no fix round has run**, so all eight
  defects stand exactly as first recorded.

**Still carrying discrepancies (verbatim from the latest verdict):**

- **`cme-2013-2015`** — round 2, `matches: false`, 12 items, five load-bearing:
  1. *"load-bearing (wrong recorded status)"* — `holidays 2013-07-03, family 'livestock+dairy+lumber'`
  2. *"load-bearing (superseded line quoted as current)"* — `holidays 2013-07-03, family 'grains_oilseeds'`
  3. *"load-bearing (completeness claim not met)"* — the enumeration *"covered only the .xls/.zip half of it"*; 42 earlier distinct-digest captures never retrieved
  4. *"load-bearing (a recorded gap the corpus already closes)"* — `missing[2]`, the Good Friday 2013 `1355` zone
  5. *"load-bearing (a stated evidential claim with a counterexample)"* — the "all 45 files … identical in every column" claim
  plus *"moderate (unrecorded gap for crate identities)"* (Weather and Mini-Sized Grains carry distinct holiday instants and are not modelled) and six minor items.
- **`cme-2016-2018`** — round 3, `matches: false`, one load-bearing:
  *"load-bearing (verbatim attribution)"* — on 2018-07-03, 2018-11-23 and 2018-12-24 the
  Grains verbatim quotes an `MGEX Apple Juice` sibling row CME deleted in the cited
  revision, *"so three claimed quotations cannot be found in their cited documents"*.
  The verdict is explicit that *"No instant, status or family-level value is wrong
  anywhere in the file."* Items 2–4 are minor.
- **`cme-2022-2024`** — round 2, `"verdict": "FAIL"`, two load-bearing:
  `R2-1` *"verbatim over-claim: quoted text that is not in the document - a surviving
  instance of the round-1 D2 defect class"* (2023-11-23 grains, *"That cell is
  completely empty."*); `R2-2` *"false statement about where the operator prints the
  zone"*. Both are flagged **"state-neutral"** — no status or instant changes. Plus one
  moderate (`R2-3`, the incomplete 2022 UTC-offset enumeration) and three minor.
- **`cme-2025-2027`** — round 2, `matches: false`, **four material**, all from one false
  premise: *"the task asserts throughout that CME's live trading-hours service 'carries
  only FORWARD holidays' and that 'past holidays are dropped'. It does not."*
  1. *"false 'missing' claim - the named channel does serve these windows"* — nine holidays × six products
  2. *"false 'missing' claim + two rows left at status 'unknown' when the current operator publication is available"*
  3. *"recorded gap that the operator's own channel closes"* — Saturday 2025-11-29
  4. *"status misclassification - the holiday's own trade date is lost"* — the six Friday Cryptocurrency rows
  plus three minor. All four are additive: they add rows and delete gaps; none
  contradicts a row that is already recorded.

### 8.3 Do any corrected facts invalidate a design decision?

No. Explicitly, for the decisions the corrections touch:

- **D1 (trade-date key)** is *strengthened*. The round-2 verifier of `cme-2025-2027`
  found the six Friday Cryptocurrency rows by exactly the test D1 prescribes — comparing
  the printed trade date against the family's own reference week — and the fix round had
  already accepted the same reasoning for the 17 `[N3]` rows. The operator's data now
  says out loud what §1.1 inferred.
- **D9 (crypto ships `Closed` rows)** is *confirmed*, not disturbed. The row §1.7 quotes
  is one the verifier requires be re-labelled, and the reason is that the 16:00 CT close
  carries the following Monday's trade date — i.e. there is no trade date on the holiday,
  which is precisely what the `Closed` row is for.
- **D3 (`Unsourced` earns its variant)** survives on different evidence. The three
  examples §1.2 cited have changed: `cme-2016-2018`'s single unknown is closed, and both
  of `cme-2025-2027`'s are closeable. What justifies the variant now is
  `cme-2022-2024`'s **13 Nikkei rows across 2024**, where the operator's channel
  structurally cannot answer, plus 2023 MLK / Presidents' Day / Good Friday.
- **D15/D16 (tier in the row, evidence file per family-year)** are *vindicated*. The
  single largest data change in this revision — `cme-2016-2018`'s 140 re-keyed rows — was
  a **supersession** discovered only by comparing captures of the same URL. A row that
  carries its document id and capture makes that discoverable; a row that does not, does
  not. Add the capture timestamp to the evidence-file `Document` column, which §3.3's
  layout already has room for.
- **D17 (venue intersection)** is untouched, and the one T1-vs-T1 conflict that would
  have exercised its sibling rule (2015 Labor Day) resolved on lineage instead. The
  conflict rule is still needed — §5.1's `cme-2013-2015` item 1 is a live example — but
  it has not yet been forced to withhold anything.
- **D18 (first wave)** changes its *content*, not its shape: `cme-2016-2018` is no longer
  a blocker, `cme-2025-2027`'s repair list is now four material items instead of five
  mixed ones, and `cfe-eurex-ice-cde-smfe-2026-2027` is the one block that could ship
  today on its verdict alone.

§6's performance plan, §2's layering and hot path, §4's tests and §3.3's evidence layout
are unaffected by anything in this revision.

---

## Appendix — retrieved corpus

Recounted 2026-09-12 from the current result files; the first-draft figures are in
parentheses where they moved.

| File | Holidays | Family rows | Date span | Latest verdict |
|---|---:|---:|---|---|
| `cme-2010-2012.json` | 71 | 608 | 2009-12-31 .. 2012-12-31 | round 1 **PASS**, 8 minor defects, **unrepaired** |
| `cme-2013-2015.json` | 72 (71) | 346 (342) | 2013-01-01 .. 2015-12-31 | round 2, `matches:false`, 12 discrepancies, **5 load-bearing** |
| `cme-2016-2018.json` | 36 (35) | 375 (363) | 2016-01-01 .. 2018-12-26 | round 3, `matches:false`, 4 discrepancies, **1 load-bearing** |
| `cme-2019-2021.json` | 44 | 440 (424) | 2019-01-01 .. 2021-12-31 | round 2, FAIL on evidence discipline, 4 discrepancies, **0 load-bearing** |
| `cme-2022-2024.json` | 34 (27) | 362 (285) | 2022-01-01 .. 2024-12-31 | round 2, **FAIL**, 6 discrepancies, **2 load-bearing** |
| `cme-2025-2027.json` | 31 | 313 | 2025-01-01 .. 2028-01-01 | round 2, `matches:false`, 7 discrepancies, **4 material** |
| `cfe-eurex-ice-cde-smfe-2026-2027.json` | 43 | 203 (202) | 2026-01-01 .. 2028-01-03 | round 2, **`matches: true`**, 0 discrepancies, 4 advisories |
| | **331** | **2,647** | | |

Tier split, recounted: `cme-2010-2012` 608 T1; `cme-2013-2015` 346 T1;
`cme-2016-2018` 375 T1; `cme-2019-2021` 440 T1; `cme-2022-2024` 219 T1 + 143 T2;
`cme-2025-2027` 313 T2; venues 198 T1 + 5 T1-but-indicative (Eurex 2027, which does
not ship). No T3 or T4 row exists anywhere in the corpus, so fence (3) of §1.2 rejects
nothing that was actually retrieved.

Retrieval vocabularies differ per file (`equity_index` / `Equity Index` /
`globex_equity_index` / `Equity Index (ES) | date 2025-01-20`), and
`cme-2025-2027` encodes the event date inside the family label. A normalisation
table from the seven vocabularies to the eight crate keys is the first artifact each
wave must produce, and it belongs in the evidence file beside the rows it produced.
Two further vocabulary facts the fix rounds added: `cme-2013-2015` rows may now carry
an `other_statements` array (67 entries, 18 `superseded` and 49 `corroborating`), and
`cme-2022-2024` moved the Energy/Metals key decoration into a separate `line` field.
Both are additive and neither changes D2.

---

### 8.4 Correction 2026-09-12 (after the wave-1 review)

Two statements in this memo were found false against the code they describe, and
one was found unimplementable as written. All three are corrected here rather
than silently worked around; the implementation records are `W1-ASM-6` and
`W1-ASM-7` in `holiday-tables/DECISIONS.md`.

**§2.3's gate-window table is wrong, and cannot be implemented as written.** It
gives an ordinary identity's window as `[D, D + 1]` on the premise that "a rule
spans at most one local midnight, so the close-date default can only land on `D`
or `D + 1`". `resolve_rule_bounds` (`src/calendar/query/schedule.rs`) does not
date an occurrence by its own close: it dates it by the local date of the
**trading day's** final close,
`candles::candle_end_with(&baseline, raw_open, Daily, Both)`. An occurrence whose
`raw_open` falls after its own trading day's final close — CBOT's 14:30-16:00 CT
order-entry window on a Friday, ICE's 13:30/14:00/14:30-18:00 ET post-close
queues — is dated by the *next* trading day, which over a weekend or a
weekend-plus-holiday is `D + 3` or more. `[D, D + 1]` is not a superset of what
the derivation can reach, so `any_layer_may_affect` was asked the wrong question
and the built-in table silently failed to apply on six shipped families
(`globex_grains`, `globex_livestock`, `ice_us_sugar`, `ice_us_coffee`,
`ice_us_cocoa`, `ice_us_orange_juice`), with the same query flipping its answer
when an unrelated, *empty* caller layer was attached.

The correct bound is the derivation's own walk:
`next_daily_close_and_trade_date_after_with` (`query/periods.rs`) starts at
`local_day.pred_opt()` and iterates `CLOSE_LOOKAHEAD_DAYS = 21` times, so every
trade date it can return lies in `[D - 1, D + 19]`, before `assign_normal`'s
identity conventions are applied on top. Read §2.3's table as
`[D - 1, D + 19]` for an ordinary identity, `[D - 2, D + 19]` for SET Thailand,
and `[D - 1, D + 19 + ROLLING_WINDOW_DAYS]` for CME cryptocurrency and `ECBTC`.

**§6's overlay targets and D19 must be re-measured against the corrected
window.** The sound window opens the gate on roughly every day within 19 of a
row, so the ~97 % exit rate §6 assumes no longer holds and D19's performance
precondition is *not* met by the wave-1 branch. A narrowing that could restore it
is stated in `W1-ASM-6` and tracked as issue #97; it must be *proved* from the
already-selected static profile, not assumed from an identity table, and §6's
numbers re-measured before the merge D19 gates.

**§3.2's "unique repository-wide" was contradicted by the per-family slug rules.**
Six family decisions spelled a CME service-window id `CME-SVC-<the row's own
trade date>`, which is non-injective by construction: two families may read the
same `eventDate` out of two different service windows. Three ids each resolved to
two artifacts and two artifacts each carried two ids. The repository now uses one
rule, `CME-SVC-<first eventDate>` — the artifact's own name — with `-SAT` and
`-PRE` suffixes where two windows share a first event date, and §3.2's
requirement is fenced by three tests rather than intended
(`W1-ASM-7`). §3.2 should be read as naming the artifact, never the row.
