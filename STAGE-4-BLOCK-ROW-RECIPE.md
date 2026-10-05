# Stage 4 — block-row recipe

Written 2026-09-25 (UTC) during Stage 4 (#116). This is the working method for
turning a published CME special session into a `HolidayKind::ReplacementBlocks`
row, derived from the two cases done so far (the `globex_energy` Saturday
sessions in #133, and the merged trade-date geometry probed against the engine).
It is a research note, not a specification: the charter and plan are authority,
and `docs/evidence/<owner>.md` carries the quotations.

Every geometry below was **probed through the public surface**, not derived on
paper — see [Verification probes](#verification-probes). One of them corrects a
paper derivation that was wrong (see the merged trade date).

## The model, in one paragraph

A replacement record is keyed by **venue-local trade date** and states that
date's **complete** ordered block set. A block is `(kind, open_day_offset,
open_ssm, close_ssm)`: the kind selects which of the family's three rule sets it
belongs to, `open_day_offset` places the block's **opening** local day relative
to the trade date, and the two `_ssm` values are venue-local seconds since
midnight. `open_ssm >= close_ssm` wraps, and a wrapping block closes on
`opening day + 1` — that is the whole of the close-day rule
(`resolve_block_bounds`). `MIN_DAY_OFFSET` is `-7`, `MAX_DAY_OFFSET` is `0`, and a
block at offset `0` may not wrap.

Because a record **replaces the complete trade date**, every block the normal
week would have contributed to that trade date must be restated in the set. A
set that covers less than the day does not partition it: it deletes the
remainder (#130, settled in #131).

## The shapes

### 1. A session added on a normally empty day

CME's Saturday sessions: `05:00 open; 17:00 closed` on a Saturday, carrying the
following Monday's trade date. Key the row to that Monday.

```
extended(-2, 05:00, 17:00)      the Saturday session
```

If the family's normal week has no session on that Monday at all, this one block
is the complete day and nothing else is needed. **If the normal week does have
one** — every standard Globex family's Monday opens Sunday 17:00 — the day is not
just the Saturday, and the rest must be stated. See shape 2.

### 2. A complete standard Globex trade date

The shapes below all restate a trade date whose normal week is the usual
Sunday-17:00-to-Monday-16:00 session plus its queues. The `globex_energy` rows in
#133 are the worked example:

```
extended(-1, 16:00, 17:00)      order-entry: the Sunday Pre-Open queue
extended(-1, 17:00, 16:00)      the Sunday-17:00-to-Monday-16:00 session (wraps)
```

Sunday Pre-Open is `16:00` on the live service. Note the family's *normal-week*
profile for the dated era states the Sunday queue as `16:15-17:00` with the
16:00-16:15 quarter-hour withheld under #79 — the operator's published value for
these dates is `16:00`, so the row states `16:00` and does not inherit the
withholding. Check the reference week (`live/normal/normalweek_main.json`) before
assuming either value.

### 3. A merged trade date (the five-day-era `[N3]` holidays)

> **Read the decision recorded at the end of this section before writing one.**
> The shape below is verified and stateable, but the merge turns out to be a
> **trade-date relabelling with no `is_open` consequence**, so whether to state
> it is a design call rather than a data gap to close. Round 16 measured that.

On a Monday or Thursday holiday CME publishes `16:00 preopen; 17:00 open` with
both events carrying the **next** business day's trade date and no final close of
its own. The span Sunday-17:00-to-Tuesday-16:00 then carries one trade date. Key
the row to the following business day.

```
extended(-2, 17:00, 16:00)      Sunday 17:00 -> Monday 16:00 (wraps)
order_entry(-1, 16:00, 17:00)   the Monday-evening queue
extended(-1, 17:00, 16:00)      Monday 17:00 -> Tuesday 16:00 (wraps)
```

**Verified**: the engine accepts this set for trade date 2025-01-21, and
`session_bounds` at Sunday 18:00 and Monday 10:00 CT both answer with
`trade_date = Some(2025-01-21)`. It is **not** one 47-hour block — that is
impossible — and it does not need to be.

**What the merge actually changes (round 16, measured).** For `globex_fx` on the
MLK 2025 holiday, the operator's window prints **every** event against trade date
2025-01-21 — the Sunday `17:00 open` and the Monday `16:00 preopen; 17:00 open`
alike — and each of those days' `16:00 closed` events carry the *previous* trade
date. So the operator's 2025-01-21 spans Sunday 17:00 through Tuesday 16:00
continuously.

The crate, on its normal week with no rows, answers:

| instant | `is_open` | crate trade date | operator trade date |
|---|---|---|---|
| Sun 01-19 18:00 | true | 2025-01-20 | 2025-01-21 |
| Mon 01-20 10:00 | true | 2025-01-20 | 2025-01-21 |
| Mon 01-20 18:00 | true | 2025-01-21 | 2025-01-21 |
| Tue 01-21 10:00 | true | 2025-01-21 | 2025-01-21 |

**`is_open` agrees at every instant.** The whole difference is which trade date
owns Sunday evening through Monday 16:00. Nothing closes, nothing opens, no
boundary moves.

**So the decision is not "can we state it" but "should we."** Stating it means
one replacement row keyed to the operator's trade date whose block set spans
offset `-2` through `0`; the crate's own 2025-01-20 label then disappears for
that span and its `trade_date` answers move to 2025-01-21. That is a **broader
change than the Saturday rows**: those made a published session exist, whereas
this reassigns two dates' worth of answers on the strength of a label the
operator prints and the crate's own convention contradicts. It is in scope under
LAW-HOLIDAY-SCOPE's "trade-date reassignments", but it is the maintainer's call
whether Stage 4 should take it, and it should be an explicit acceptance rather
than a row slipped into a family PR. **Not written.**

### 4. A holiday trade date carrying both a Saturday session and an early close

The complete day for trade date 2026-06-22 (Juneteenth Friday 2026-06-19 is an
early close, the Saturday carries this trade date, the Sunday-Monday session is
ordinary):

```
extended(-4, 17:00, 12:00)      Thursday evening -> Friday 12:00 (wraps; the early close)
extended(-2, 05:00, 17:00)      the Saturday session
order_entry(-1, 16:00, 17:00)   the Sunday Pre-Open
extended(-1, 17:00, 16:00)      the Sunday-Monday session
```

**Verified accepted**, and every probe instant returns `trade_date =
Some(2026-06-22)`. Note the block states `12:00` for the early close because that
is what the operator printed for that date; the family's own `early_close` holiday
row for 2026-06-19 is keyed to the **previous** trade date and does not clip this
one.

## Rules a row author must not learn the hard way

1. **State the complete day.** A partial set deletes the remainder (#131); it is
   not merged with the normal week.
2. **Each block's close is clipped by whatever layer governs the day it lands
   on.** A block that closes on a holiday date is clipped by that date's own
   `early_close` row. This is precedence working, not a bug, but it means a
   block's stated `close_ssm` is not always the close a query reports.
3. **`close_ssm` is interpreted on `opening day + 1` when it wraps** — so
   `extended(-2, 17:00, 16:00)` is a 23-hour block ending 16:00 the day after it
   opens, not a one-hour block.
4. **Blocks are ordered by opening day then open time, non-decreasing.** Two
   blocks of *different* kinds may share `(offset, open_ssm)` — an `order_entry`
   phase and the session that starts with it — so `08:00 order_entry` and
   `08:00 extended` is legal and `first_block_violation` accepts it.
5. **The operator's trade-date label and the crate's are both real.** Where they
   differ, the row is keyed to the crate's venue-local trade date and the
   divergence is recorded in the evidence file, as `globex_energy`'s `[N3]`
   handling and #133's rows both do.
6. **A row changes the venue intersections.** Adding a row to a family table
   moves four derived venue tables and the coverage inventory's date and
   `Unsrc` cells. Compute, do not guess: the intersection is `AuditedNormal`
   (no venue row) when every family that answers states nothing, `Agreed` when
   they all state the same row, and `Disputed` (`Unsourced`) when at least one
   states a row and they do not all agree. A date can resolve **differently** for
   `cme` and `cbot`, because they route different family sets.

## Sourcing rules that cost time

- **Read the bytes before writing the row.** Three of the three dates in #133
  needed a window check: the evidence file cited a window for 2026-07-04 whose
  product set (`THBP-A`) contains no Crude Oil product, so the claim rested on
  nothing until the correct window was found. Check the window **and its product
  list**.
- **Check the window covers the whole span you are stating.** A service call is
  bounded by `fromEventDate..toEventDate`; a trade date that opens on a Saturday
  or a Sunday needs those days *inside* the window, and more than one holiday
  window in the store stops one day short. When no saved window covers the day,
  retrieve it (`live/thbp/...` through `https://r.jina.ai/<url>`, saving the
  reader page and its digest) rather than inferring the instants from the normal
  week.
- **A weekend instant may be refused by the gate even when the crate has the
  answer.** Two instances are open: #132 (the order-entry and `trade_date` gates
  judge the local day a phase opens on rather than the trade date it belongs to).
  A row is still correct; the query that reads it may refuse. Record the refusal
  in the test rather than asserting the defect as correct — and make the
  assertion fail when the gate is fixed.

## Verification probes

Before writing rows for a family, probe the proposed geometry through the public
surface in a scratch test (`tests/probe_*.rs`, deleted before the PR):

1. `StaticSessionExceptions::new` **accepts** the block set — this catches
   ordering, offset, instant-range and wrap-at-`0` mistakes before a row exists.
2. `session_bounds` and `trade_date` at the **first instant of every block**, the
   **instant before each close**, and **inside each gap**.
3. `is_open` at each block's close, to confirm end-exclusivity.
4. `is_closed_trade_date` for any date the merge removes (a merged holiday should
   read as having no session of its own).

Then, for the shipped row: mutation-check it. The three mutations that caught
real mistakes in #133 were moving a block's open, dropping a block from the set,
and keying a block one day late — the last is the offset-sign error that a paper
derivation got wrong in round 1.

## The remaining CME families, derived

Verified 2026-09-25 (round 8) by reading the saved service windows for the
products each family routes, and probing each family's own grid. **The operator
publishes the same event times for every affected family on these dates** —
`CL`, `ES`, `ZN` and `6E` all print `05:00 open; 17:00 closed` for the Saturday
and the same Sunday-Monday times — so the block sets are the same across
families and only the profile behind them differs. `ZC`, `LE`, `CSC` and `LBR`
print nothing on the Saturday (grains, livestock and dairy are closed on the
Juneteenth Friday), and `BTC` prints its own 24/7 grid.

| Family | Sunday Pre-Open | Envelope | Set to ship |
|---|---|---|---|
| `globex_energy` | `16:00-17:00` | one `17:00-16:00` span | **shipped** (#133) |
| `globex_equity_index` | `16:00-17:00` | one span containing the `08:30-15:15` regular leg | **shipped** (#134) |
| `globex_interest_rates` | `16:15-17:00` normal week | one `17:00-16:00` span | energy's three blocks |
| `globex_fx` | `16:00-17:00` normal week | one `17:00-16:00` span | energy's three blocks |
| `globex_nikkei_225_dollar` | `16:00-17:00` | one `17:00-16:00` span (`cme_nikkei.rs`) | energy's three blocks — **retrieval done, see below** |
| `globex_grains`, `globex_livestock` | no Saturday session published | — | nothing to state for these dates |
| `globex_cryptocurrency` | 24/7 era | — | see shape 3 and the maintenance-minute gap |

So the next family PR is either `globex_interest_rates` **or** `globex_fx` as a
single-family PR, or those two together as one bounded shared-operator PR — both
are served, both route to `Exchange::Cme`, and both take the same three blocks
from the same three documents, which is the case plan §8 allows a shared PR for.
`globex_nikkei_225_dollar` cannot join them: its rows need a retrieval first,
because the headline product set does not contain `NKD` or `NIY` and the family's
own module documents a different historical grid.

**Two gates apply to every one of them.** `is_order_entry_only` refuses a Sunday
probe on all four of these families (#132), so a row's Sunday queue block cannot
be asserted through that query — assert the correct answer or the coverage
refusal, and never the refusal as if it were the answer. And the merged-trade-date
shapes for `globex_fx` and `globex_cryptocurrency` are a **separate** row set from
their Saturday sessions: those two families need both shapes, and the merged one
is stateable by recipe shape 3.

## `globex_nikkei_225_dollar` — retrieved and verified (round 11)

`NKD` and `NIY` are **not** in the headline product set (`THBP-A`); they are in
`[THBP-B]` (`id=168,167,320,323,19,27`). The store already held the 2027 window
for them (`live/extra/extra_2027-06-17_2027-06-19.json`); the two 2026 windows
were retrieved on 2026-09-25 through `https://r.jina.ai/` and saved:

| Window | Artifact | sha256 |
|---|---|---|
| 2026-06-18 .. 2026-06-20 | `live/extra/extra_2026-06-18_2026-06-20.md` | `d7ed68588f7892863f631e879365bd60bfe088179dcc53a323200543cbdc39b6` |
| 2026-07-03 .. 2026-07-05 | `live/extra/extra_2026-07-03_2026-07-05.md` | `7839fef6e7506422826614eb7c6aef23c97da1db45799ab62453bb60976e6150` |

**Both products print the same shape as every other family**: `05:00 open;
17:00 closed` on the Saturday, `16:00 preopen; 17:00 open` on the Sunday, and the
Monday `16:00 closed`, all carrying the following Monday's trade date. `cme_nikkei.rs`
documents NKD's current grid as one continuous `17:00-16:00` envelope per trade
date, which is the same grid, so **energy's three blocks are the whole set** —
the family's different historical grid does not reach 2026-2027. The set was
probed through the public surface and accepted, with every instant resolving to
the right trade date.

So this family is authorable now with no further retrieval. It was **not**
written in round 11: four family PRs are already open and unreviewed, and the
marginal value of a fifth is lower than the value of the retrieved bytes and the
verified shape, which are what the round produced.

## What is still unstated

- `globex_fx` and `globex_cryptocurrency` merged trade dates: **stateable** by
  shape 3, not yet written.
- Saturday sessions for `globex_equity_index`, `globex_interest_rates` and
  `globex_nikkei_225_dollar` on 2026-06-20, 2026-07-04 and 2027-06-19: same
  shape as #133, not yet written.
- The 60-second maintenance minute on the 24/7-era cryptocurrency holidays: needs
  a block set that omits the gap the normal week has, not yet attempted.
