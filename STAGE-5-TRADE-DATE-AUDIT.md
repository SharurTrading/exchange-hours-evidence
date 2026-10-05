# The Globex trade-date gap family — derived spec

Written **2026-09-26** (UTC). Reconnaissance for Stage 5's first data PR. Every
number here was measured at `main` = `21e5204` with the scripts described below;
nothing is carried from another tree.

## 1. What the operator does

CME's `trading-hours-by-product` service prints, per event, a `tradingDate`. On
dates where the exchange publishes **no final close for a trade date**, the
session that would normally carry that trade date is printed against the
**following** trade date instead. The crate keeps its own label, so its
`trade_date` answer contradicts the operator's on those spans.

The mechanism is already shipped: `HolidayKind::ReplacementBlocks` (#93) and the
`SATURDAY_SESSION_BLOCKS` geometry in `globex_fx.rs:111`. The gap is that the
shipped block sets do not cover every leg the operator assigns to the trade date.

## 2. Method

- Source: `holidays/raw/cme-2025-2027/arc/thbp_*.json` and
  `holidays/raw/cme-2025-2027-repair/json/*.json` in this store — the raw replay
  of CME's own endpoint, product `id=58` (`6E` Euro FX).
- Derivation: group every event by its `tradingDate`, then compare the resulting
  span for each trade date against the crate's normal-week span for that trade
  date (previous local day 16:45 preopen / 17:00 open → trade date 16:00 closed).
- Engine check: a scratch crate at `/tmp/eh-merged-probe` over the public
  surface, using `SessionExceptionRecord::replace_sessions` +
  `ExchangeCalendar::with_session_exceptions`. No production file was edited.

**The outcome classes are not interchangeable.** Four distinct shapes appear,
and treating them as one is how a "sibling file" fix goes wrong.

## 3. Outcome classes, measured (2025 and 2026 windows; 6E)

| Class | Trade dates | Operator span | Crate today |
|---|---|---|---|
| **Merged** | 2025-01-21, 02-18, 05-27, 06-20, 09-02; 2026-01-20, 02-17, 05-26, 09-08 | prev-prev day 16:00 queue, 17:00 open; holiday 16:00 queue, 17:00 open; T 16:00 closed | answers the *holiday's* trade date for the first two legs |
| **Merged + early close** | 2025-11-28; 2026-11-27 | Wednesday 16:45 queue, 17:00 open; Thursday 16:00 queue, 17:00 open; Friday `13:45 closed` | ships `early_close(13:45)` on T only; the Wednesday and Thursday legs keep the holiday's trade date |
| **Composite** (holiday + Saturday session) | 2026-06-22; 2026-07-06 (and 2027-06-21) | Thursday 16:45 queue, 17:00 open → Friday 12:00 closed; Saturday 05:00-17:00; Sunday 16:00 queue, 17:00 open → Monday 16:00 | ships 3 blocks, omitting the Thursday→Friday leg |
| **Order-entry only** | 2025-01-02, 2025-12-26, 2026-01-02 | queue opens 16:00 instead of 16:45; **trade date already correct** | correct trade date, wrong queue onset |

The **order-entry-only** class is the trap: its trade date needs no change, so a
row written from the merge template would rewrite a correct answer.

## 4. The shipped defect (measured, not inferred)

`globex_fx.rs:94-100` says the Saturday rows state "all three of the trading
day's phases" and that "stating only the Saturday would delete the
Sunday-evening session". The cited window prints **five** phases for those trade
dates — the Thursday-evening→Friday-early-close leg is a fourth and fifth block.

Probe at `21e5204`, `6E`, crate answers vs the operator's printed trade date:

| instant (CT) | operator TD | crate TD today |
|---|---|---|
| 2026-06-18 18:00 | 2026-06-22 | **2026-06-19** |
| 2026-06-19 10:00 | 2026-06-22 | **2026-06-19** |
| 2026-07-02 18:00 | 2026-07-06 | **2026-07-03** |
| 2026-07-03 10:00 | 2026-07-06 | **2026-07-03** |
| 2027-06-17 18:00 | 2027-06-21 | **2027-06-18** |
| 2027-06-18 10:00 | 2027-06-21 | **2027-06-18** |
| 2025-06-18 18:00 | 2025-06-20 | **2025-06-19** |
| 2025-06-19 10:00 | 2025-06-20 | **2025-06-19** |

So the defect is live on `main` for rows merged as #134, #136 and #137, and the
module's own prose asserts the completeness the bytes contradict.

**Additive fix verified.** Overlaying a 5-block replacement for TD 2026-06-22
(`order_entry(-4, 16:45, 17:00)`, `extended(-4, 17:00, 12:00)`,
`extended(-2, 05:00, 17:00)`, `order_entry(-1, 16:00, 17:00)`,
`extended(-1, 17:00, 16:00)`) makes every probe above answer `2026-06-22`, and
the existing `early_close` row on 2026-06-19 can **stay** — the replacement row
wins for the trade-date answer, so no row kind has to be invented and no ledger
count moves.

## 5. Scope note

The same operator windows govern every Globex family on the same grid, so this is
not `globex_fx`'s alone: the `2026-01-19` window prints the same merged shape for
`CL`, `GC`, `ZN`, `ES`, `BTC` and `CSC`, each with its own queue onset. The
shipped Saturday rows of `globex_energy`, `globex_equity_index`,
`globex_interest_rates` and `globex_nikkei_225_dollar` carry the same omission as
`globex_fx`'s and must be checked against this spec, not mirrored from it.

### 5.1 A wrong rationale already shipped

`globex_equity_index.rs:113-117` is not merely silent about the Thursday leg — it
**states a reason for omitting it**:

> The Friday evening before the Saturday is deliberately **not** stated. CME
> publishes no Friday-evening open for these dates — the Friday carries the early
> close that ends the *previous* trade date's session — so there is no trading to
> claim, and a block there would put an open on the clock at an instant no
> operator document states.

Two claims, one true and one false. There is indeed no *Friday-evening* open. But
the Friday early close does **not** end "the previous trade date's session": the
operator labels that very event `tradingDate = 2026-06-22`
(`thbp_2026-06-18_2026-06-20_20260619113404.json`, `ES`, eventDate `2026-06-19`,
`12:00 closed`). The session that opens Thursday 17:00 and closes Friday 12:00
belongs to trade date 2026-06-22, so there is trading to claim and a block there
is exactly what the operator document states.

The crate's own convention agrees once the holiday is accounted for: a session's
trade date is the venue-local date of its final close, and that session's final
close is the *next trading day's*, not the holiday's. The defect is therefore not
a modelling choice; it is a misreading of the window, asserted in a module
comment and fenced by no test.

`globex_equity_index`'s five blocks are also **not** the same five as the fix in
§4 — they split the Monday envelope at the `regular` boundaries (08:30-15:15).
A fix that "mirrors the sibling" by copying its block count would be wrong in
both directions. Each family's set must be derived from its own window.

## 6. Correction and the complete 2025-2027 spec

**Correction to an earlier draft of this section.** It said the 2027 windows were
not in the store. They are — under `holidays/raw/cme-2025-2027/live/thbp/*.json`
and `live/extra/*.json`, which the first glob missed because it only read `arc/`
and `-repair/json/`. No retrieval is needed. Lesson 2 of the Stage 4 handoff
applies to the auditor as much as to the author.

Re-derived over every source (`arc/`, `live/thbp/`, `live/extra/`,
`-repair/json/`, and the two `live/thbp/*.md` r.jina.ai retrievals), product
`6E`, per trading date, 2025-2027 — 68 trade dates. Four classes:

**Merged** (4 blocks: `-2` queue, `-2`→`-1` session, `-1` queue, `-1`→`0`
session) — **14 dates**:

| trade date | the `-2` queue onset |
|---|---|
| 2025-01-21, 2025-02-18, 2025-05-27, 2025-09-02 | 16:00 (Sunday) |
| 2025-06-20 (Juneteenth Thu) | **16:45** (Wednesday) |
| 2026-01-20, 2026-02-17, 2026-05-26, 2026-09-08 | 16:00 (Sunday) |
| 2027-01-19, 2027-02-16, 2027-06-01, 2027-09-07 | 16:00 (Sunday) |
| 2027-07-06 (July 4 observed Mon) | 16:00 (Sunday) |

The `-2` queue onset is **not uniform**: 16:45 when the `-2` day is an ordinary
weekday and 16:00 when it is a Sunday. A single static cannot serve both.

**The `-1` queue onset is family-specific, and it is not the normal-week queue.**
Measured across 2025-01-21, 2026-01-20 and 2027-01-19 — all three agree, so this
is a stable per-family value and not a per-date one:

| family | product | holiday (`-1`) Pre-Open | Sunday (`-2`) Pre-Open |
|---|---|---|---|
| `globex_fx` | `6E` | **16:00** | 16:00 |
| `globex_energy` | `CL` | **13:30** | 16:00 |
| `globex_equity_index` | `ES` | **12:00** | 16:00 |
| `globex_interest_rates` | `ZN` | **12:00** | 16:00 |
| `globex_nikkei_225_dollar` | `NKD`, `NIY` | **12:00** | 16:00 |
| `globex_cryptocurrency` | `BTC` | 16:00 | 16:00 |

Each family's ordinary Mon-Thu queue is 16:45, so **every** merged row departs
from its own normal week on the holiday, and every one of them departs by a
different amount. This is the single most dangerous place in the whole family for
a mirrored fix: a row copied from `globex_fx` would put the `globex_energy` queue
two and a half hours late and the `globex_equity_index` queue four hours late.

The same per-family value holds for both holiday shapes — verified on the MLK
Mondays (2025-01-21, 2026-01-20, 2027-01-19), Juneteenth Thursday 2025-06-19 and
Thanksgiving Thursday 2025-11-27 — and the **closing** instant of the
merged-plus-early-close class is family-specific too:

| family | holiday (`-1`) Pre-Open | day-after-Thanksgiving close |
|---|---|---|
| `globex_fx` | 16:00 | 13:45 |
| `globex_energy` (`CL`, `GC`) | 13:30 | 13:45 |
| `globex_equity_index` (`ES`) | 12:00 | **12:15** |
| `globex_interest_rates` (`ZN`) | 12:00 | **12:15** |
| `globex_nikkei_225_dollar` | 12:00 (MLK window) | not yet read — second product set |

Both per-family closes are already shipped as `early_close` rows in each family's
table for the day itself, so the merged-plus-early rows restate a value the crate
already holds rather than introducing one. The `-2` day's queue is 16:45 when
that day is an ordinary weekday and 16:00 when it is a Sunday, for every family.



**Merged + early close** — 2025-11-28, 2026-11-27, 2027-11-26. Four blocks, the
last ending at `13:45`; `-2` queue 16:45.

**Composite** — 2026-06-22, 2026-07-06, 2027-06-21 (the PR in flight).

**Order-entry only** — 2025-01-02, 2025-12-26, 2026-01-02. `-1` queue 16:00
instead of 16:45; the trade date is already correct, so a merge-shaped row would
rewrite a right answer.

### 6.1 The recipe's shape 3 omits the Sunday queue

`STAGE-4-BLOCK-ROW-RECIPE.md` shape 3 gives three blocks and round 16 verified
them for `trade_date` and `is_open`. It does not state the Sunday `16:00 preopen`
that the operator prints against the same trade date — while the shipped
Saturday rows **do** state that queue (`order_entry(-1, 16:00, 17:00)`).

Measured: on 2025-01-19 16:30 and 2025-01-20 16:30 CT, **both** the 3-block and
the 4-block set return `OutsideCoveredRange` for `is_accepting_orders` and
`is_order_entry_only`, because the `#79` declaration refuses the whole date. The
difference is therefore unobservable today and cannot be settled by probe. The
4-block set is the one consistent with the operator's bytes and with the
shipped Saturday rows, so a merged row should carry it — but the point must be
recorded as reasoning, not claimed as a measured improvement.

### 6.2 Open question PR 2 must settle: `comex`/`nymex`'s holiday `early_close`

`venues/comex.rs:403,429` and `venues/nymex.rs:407,433` ship
`early_close(13:30)` on the **holiday itself** (2025-01-20, 2026-01-19). The
operator's window for those dates prints no `closed` event at all for these
families — the Monday carries `13:30 preopen; 17:00 open` (for `CL`/`GC`) and
`12:00 preopen; 17:00 open` (for `ZN`/`ES`), every event dated to the *following*
trade date. So the `13:30` in the window is a **Pre-Open**, not a close.

Whether the `early_close(13:30)` rows are a defect, or are legitimately about a
different product set the venue scope covers, was **not** established here. It is
recorded rather than asserted: settling it needs the venue scope's own product
list and its own window, which is PR 2's work. What is established is that the
merged-date analysis must not assume a holiday close exists.

### 6.3 Still unverified

- **Trade date 2027-01-04.** The `thbp_2026-12-30_2028-01-02` window prints no
  events for 2027-01-01 or 2027-01-04, so the New Year queue onset for that year
  is not established by any artifact in the store. It needs a fresh retrieval
  before a 2027 row set is complete.
- The same four classes for the other families. The windows show `CL`, `ES`,
  `GC`, `ZN`, `NKD` and `NIY` printing the identical event set to `6E` on every
  merged date, and `BTC` printing a different grid — but each family's block
  offsets depend on its own normal week and envelope split, so each must be
  derived rather than mirrored.

## 7. Whole-surface audit (first pass)

Added 2026-09-26 UTC. Scratch crate `/tmp/eh-merged-probe`, bin `audit`: parse
every captured CME window, convert each event to an instant in `America/Chicago`,
and compare the operator's `tradingDate` with `ExchangeCalendar::trade_date` one
second **inside** the session the event bounds — a second *before* a `closed`
event and a second *after* an `open`, because a close is end-exclusive. Only
`open` and `closed` are probed: a `preopen` is a queue with no executable
session, and `trade_date` is entitled to answer `None` there.

**Result: of 1037 tradeable instants, 808 agree, 22 are refused by a declared
gap, and 207 disagree.**

| scope | mismatches |
|---|---|
| `globex_grains` | 79 |
| `globex_livestock` | 39 |
| `globex_energy` | 17 |
| `globex_equity_index` | 17 |
| `globex_fx` | 17 |
| `globex_interest_rates` | 17 |
| `globex_nikkei_225_dollar` | 12 |
| `globex_cryptocurrency` | 9 |

### 7.1 What this does and does not establish

**Established.** The five families' 17/17/17/17/12 are the **merged** class of
§6 and are consistent with the spec derived there: the probes name the Sunday
`17:00 open` and the holiday's `17:00 open`, each carrying a trade date one day
later than the crate's. PR 2 closes them.

**Not established — do not read these as defect counts.** `globex_grains` (79)
and `globex_livestock` (39) show a **different signature**: their mismatches
cluster at `13:30 closed` (the crate answers `None` where the operator says a
session is ending) and at `16:00 closed` (the crate answers the *next* trade
date). That is the shape of an intraday session-model question about those two
grids — regular 08:30-13:30, `14:30 pcp`, `16:00 closed`, evening reopen 19:00 —
not of the merged-trade-date class. **This audit is not sufficient to characterise
them**, and their counts must not be quoted as defects until they are analysed on
their own terms. They are nonetheless worth attention: `coverage-2025.md` reads
both scopes as "complete to 2027-12-31", so nothing in the current fences is
looking at their trade-date answers at all.

**Method limits, stated.** The probe samples one instant per event rather than
sweeping each open→closed interval; it does not model intraday `paused`/`pcp`
markers; and it covers only the calendar windows captured in this store, which is
the 2025-2027 holiday and edge windows rather than every ordinary week. A scope
absent from that set is not audited at all.

**Follow-up, measured: most of the grains and livestock counts are an artefact of
this probe.** Probing `globex_grains` directly on 2025-01-02
(`/tmp/eh-merged-probe`, bin `grains`) shows the crate models the regular session
as 08:30-13:20 — the operator's own `13:20 paused` — so at 13:29:59, one second
before the `13:30 closed` event, the market is genuinely paused and
`trade_date = None` is **correct**. My rule "a second before a close is inside the
session" is false whenever a pause immediately precedes the close. The `13:30`
half of both counts is therefore an artefact and is discarded.

What survives is narrower and real: at the `16:00 closed` events, 15:59:59 CT
answers `OrderEntry` with the **next** trade date (`2025-01-03`) where the
operator prints `16:00 closed` carrying `2025-01-02`. That is one claim about the
13:20-16:00 window on those two grids, not 118, and it is not yet analysed.


### 7.2 A flagged risk for PR 2: the equity-index merged row is not a scaled copy

`globex_equity_index` needed **eight** blocks for the composite class because its
envelope splits at the regular boundaries. The merged class looks similar but is
not the same shape, and it must not be derived by analogy:

- On a merged Monday holiday the operator prints, for `ES`, `12:00 preopen;
  17:00 open` carrying the **following** trade date. It prints **no** `08:30
  open` or `15:15 closed` on that Monday, where an ordinary Monday would carry
  the regular 08:30-15:15 session.
- So whether the merged row states a `regular(-1, 08:30, 15:15)` block for the
  holiday itself is an open question, and the answer changes the block count.
- The same window prints `12:00 preopen` for `globex_equity_index`'s **other**
  Monday holidays (Memorial 2026-05-25 and friends), where the family already
  ships `early_close(12:00)`. Whether that `12:00 preopen` is the same event as
  the early close, mislabelled, or a distinct queue is not established here.

**Do not write the equity-index merged row by scaling the composite one.** Derive
it from the family's own window and its own normal week, as `#134`'s eight-block
composite set had to be. The other four families' merged sets are four blocks and
are not affected by this.

## 8. A blocker on the *trustworthiness* of the merged rows: dangling notes

Recorded 2026-09-26 UTC, filed as **#142**.

While deriving the equity-index merged row, its `12:00 preopen` event turned out
to be shipped as an `early_close(12:00)` row, and the row's basis is a citation:
`… CME trade date 2026-01-20; note N15`. **`N15` is defined nowhere in the
repository.** Neither is `N1` (which that same file cites on other rows and
`globex_livestock.md` cites at line 374) nor `N17`
(`globex_cryptocurrency.md:63`). `docs/evidence/globex_equity_index.md` has 25
rows citing the three, and no notes section at all.

The convention existed — `docs/plans/archive/` carries a `**N1:**` note — so
these are missing rather than novel. It matters here because `N15` *is* the
interpretive step that reads the operator's `12:00 preopen` as a close, and every
merged-date row for `globex_equity_index` inherits that reading. The value may
well be right; the basis cannot currently be followed, which is what
LAW-EVIDENCE-FILES asks the evidence file to guarantee.

**Consequence for PR 2:** derive the equity-index merged row from the bytes and
state the `12:00 preopen` reading explicitly in the row's own basis, so the new
rows do not lean on a note that does not exist. Do not inherit the citation.

## 9. PR 2's shape, verified before any row is written

Recorded 2026-09-26 UTC. Scratch crate `/tmp/eh-merged-probe`, bin
`mergedshape`, at `a6ffa12` (the PR #141 head, which the main checkout carries).

A caller-supplied `SessionExceptionRecord::replace_sessions` for trade date
**2026-01-20** was overlaid on each family, with this four-block set:

```
order_entry(-2, 16:00, 17:00)   Sunday Pre-Open, 16:00 for every family
extended(-2, 17:00, 16:00)      Sunday 17:00 -> Monday 16:00
order_entry(-1, H, 17:00)       the holiday Pre-Open, H family-specific
extended(-1, 17:00, 16:00)      Monday 17:00 -> Tuesday 16:00
```

`trade_date` was then probed at Sunday 18:00, Monday 10:00, Monday 18:00 and
Tuesday 10:00 CT — every one of which the operator dates to 2026-01-20:

| family | `H` | result |
|---|---|---|
| `globex_fx` | 16:00 | all four probes answer 2026-01-20 |
| `globex_energy` | 13:30 | all four probes answer 2026-01-20 |
| `globex_interest_rates` | 12:00 | all four probes answer 2026-01-20 |
| `globex_nikkei_225_dollar` | 12:00 | all four probes answer 2026-01-20 |

So the geometry is not in doubt for those four, and the family-specific `H` is
load-bearing rather than cosmetic — it is what the operator prints on the holiday
and it differs from every family's ordinary 16:45 queue.

**`globex_equity_index` is deliberately absent from that table** and is not
covered by this verification. Its merged row depends on the `12:00 preopen`
reading that §8 shows is currently unverifiable, and on whether the holiday
Monday carries a `regular` block at all. It needs its own derivation, and its
row must not be written until that is settled.

## 10. PR #141 self-check: one overstated basis, found and closed with bytes

Recorded 2026-09-26 UTC. No reviewer was obtainable (see `STATUS.md`), so the
charter's step-3 check was run by the author and labelled as such.

Every document id cited in PR #141's changed evidence rows resolves to a store
artifact by window, and the five-phase claim was validated against the bytes for
all five families and all three trade dates — after fixing this script's own glob,
which had missed `live/thbp/*.md` a second time and produced a false "nikkei is
missing two phases" result. The recursion, not the pattern, is what makes that
check trustworthy.

**One real gap survived.** No artifact in the store contained *any* event on
eventDate **2026-07-06**. The window the 2026-07-06 rows cite,
`thbp_2026-07-03_2026-07-05`, stops at Sunday 2026-07-05, so the `16:00 closed`
that ends trade date 2026-07-06 was not witnessed by anything — while the edited
evidence text claimed the window "runs through its own Sunday and prints the whole
day, so the one document states every block". The value is right (it is the
family's own normal-week close, restated because a replacement states the whole
day, exactly as the module comments say), but the sentence overstated the basis.

**Retrieved and saved**, so the claim now rests on bytes:

- `live/thbp/thbp_2026-07-05_2026-07-07.md` — sha256
  `f6e1900b4971eda307f63d1c905f94741c268350fe4623e916580065c4c194cb`, retrieved
  2026-09-26T02:55:11Z. Prints `2026-07-06 16:00 closed /TD 2026-07-06` and
  `16:45 preopen; 17:00 open /TD 2026-07-07` for `6E`, `CL`, `ES`, `GC` and `ZN`.
- `live/extra/extra_2026-07-05_2026-07-07.md` — sha256
  `4998f2fbf8016ce92132df7efcb1ea98555270c28ad453262e70213d2b519a4d`, same
  timestamp. Prints the same for `NKD` and `NIY`, which are in CME's second
  product set and absent from the headline window.

Both are added to `cme-2025-2027/INDEX.md` with their URLs, retrieval dates and
hashes.

**Owed:** the 2026-07-06 evidence row in all five families should cite the new
document and drop the "prints the whole day" phrasing. Deferred deliberately —
`stage-5-merged-fx` (PR 2) is editing those same five evidence files and the
`globex_fx` module right now, and retargeting its base mid-flight is the
"one writer per worktree" mistake in a new costume. Apply it as a single
amending commit on PR #141 once that branch is pushed, then rebase PR 2.

## 11. Retraction: §7's `globex_nikkei_225_dollar` count is sound

Recorded 2026-09-26 UTC. **This section replaces an earlier one that was wrong.**

The earlier version claimed §7's 12 nikkei mismatches had unexplained provenance,
on the strength of `grep -rl '"id":168' --include='*.json'` returning no artifact
covering 2025-11-26, 2026-01-18, 2026-02-15 or 2026-05-24. It concluded the audit
might have a bug and that no nikkei row should be written from that count.

**Both conclusions were wrong, and the audit was right.** The artifacts are
`cme-2025-2027-repair/json/probeB_2025-11-26_2025-11-29.json` and its siblings
(`probeB_2026-01-18_2026-01-20.json`, `probeB_2026-02-15_2026-02-17.json`,
`probeB_2026-05-24_2026-05-26.json`, …), which are inside the audit's glob and do
carry products `167` and `168`. The grep missed them because those files write
`"id": 320` — **with a space after the colon** — and the pattern had none.

Instrumenting the audit to print the artifacts behind each scope settled it in
one run: nikkei draws on **25 artifacts**, the fourteen `live/extra/*.json` and
eleven `probeB_*.json`. The count is substantiated.

**The lesson is not the one the retracted section drew.** It is narrower and it
has now cost this session three separate false findings: *a search that returns
nothing is not evidence of absence until the pattern is checked against the
bytes.* The three were a glob missing `live/thbp/*.md` (hid the nikkei Sunday
windows), a glob missing `live/` entirely (hid every 2027 window), and this grep
missing a space (invented a provenance gap and nearly suppressed a valid work
item). In each case the tool reported success and the conclusion was confident
and wrong.

**What survives and is worth keeping:** §7 printed per-scope counts with no record
of which artifacts produced them, so an under-specified input set looked exactly
like a finding. The audit now prints its artifacts per scope — cheap, and it is
what turned this from a suppression into a one-run answer.

**Consequence for the work:** `globex_nikkei_225_dollar` remains a valid next
unit, and it is the *cheapest* one, because `cme` does not route it — no venue
cascade, unlike every other family.

## 12. The remaining merged class is blocked on one unresolved reading

Recorded 2026-09-26 UTC, found by attempting `globex_nikkei_225_dollar` and
stopping. **This supersedes the ordering advice in `STAGE-5-CONTINUATION.md`.**

Each of the four remaining families ships **exactly one** row on the merged
holiday date, and that row reads CME's `preopen` event as a **close**. Measured
on 2026-01-19, for the row keyed to that holiday:

| family | holiday queue the operator prints | row on the holiday date |
|---|---|---|
| `globex_fx` | `16:00 preopen` | **none** |
| `globex_equity_index` | `12:00 preopen` | one `early_close(12:00)` |
| `globex_interest_rates` | `12:00 preopen` | one `early_close(12:00)` |
| `globex_energy` | `13:30 preopen` | one `early_close(13:30)` |
| `globex_nikkei_225_dollar` | `12:00 preopen` | one `early_close(12:00)` |

The operator prints **`preopen`** on that date for every family and **never
`closed`** — it reserves `closed` for real closes, as it does on the
day-after-Thanksgiving Fridays (`12:15 closed`, `13:45 closed`), which those same
modules ship as early closes and which are not in doubt.

**The two models are mutually exclusive.** If the shipped reading is right — the
holiday closes at 12:00 or 13:30 and reopens at 17:00 — then the span is *not*
continuous, and a merged row asserting `extended(-2, 17:00, 16:00)` would claim
trading across a closure. If the pre-open reading is right, those holiday rows are
misreadings and the merged row is correct. The crate cannot ship both, and I did
not ship either.

**`globex_fx` was safe only by accident**, and that is why its change landed:
it happens to ship no row on the merged holiday, so nothing contradicted it. The
earlier advice that `globex_energy` was the next unblocked family was **wrong** —
energy has the same conflict at `13:30`.

**So the whole remaining merged class reduces to one question**, and it is the
same one #142 already tracks: *is CME's `preopen` event on a holiday a close, or
a queue?* Settling it unblocks four families at once; nothing else in this family
needs to be re-derived first.

**Work preserved, not discarded.** The complete `globex_nikkei_225_dollar`
change — two statics, twelve rows, twelve evidence rows, the inventory count and
the test fixtures — is in `git stash` on branch `stage-5-merged-nikkei`
(`nikkei merged rows — blocked on the preopen-vs-close reading (#142)`). It was
verified working: the family's twelve mismatches went to **zero**, the session
total 190 → 178, and the whole chain was green before the reading question
stopped it. It should be popped and finished once #142 is settled — either as-is,
or with the holiday rows corrected in the same change.

**What would settle it**, in rough order of cost: a CME holiday page or notice
that prints a `closed` event for one of these dates; a capture of the service on
the holiday itself rather than around it; or the operator's own contract
specification for the event vocabulary. The research store's `cdx/` enumerations
already list where to look.

## 13. Resolution: the merged `-2` leg ends at the holiday's early close

Recorded 2026-09-26 UTC. **This supersedes §12's conclusion that the remaining
merged class was blocked.** It was not blocked; my block set was wrong.

§12 noted that four families ship a holiday row that reads CME's `preopen` as a
close, and that a merged row asserting a continuous span contradicts it. I framed
that as an unresolved reading of the operator's vocabulary. It is not unresolved,
and the answer was already in the repository:

- `globex_equity_index` ships **`early_close(12:00)`** on MLK, Presidents,
  Memorial and Labor Days for **2021** and **2022**, cited to **T1** artifacts —
  `2021-holiday-calendars.zip#2021-mlk-day-schedule-compact.xls` and
  `2022-mlk-day-holiday-schedule.xls`. CME's own holiday *schedule* states the
  early close, so the `12:00 preopen` the service prints is the **queue that opens
  at** that close, not a close and not a contradiction.

So the two facts are one fact, and the correct merged block set carries the
holiday's own close as the end of its `-2` leg:

```
order_entry(-2, 16:00, 17:00)      the published Sunday Pre-Open
extended(-2, 17:00, C)             Sunday evening -> the holiday's early close C
order_entry(-1, C, 17:00)          the holiday queue, which opens at C
extended(-1, 17:00, 16:00)         the holiday evening -> the next 16:00
```

where `C` is `12:00` for `globex_equity_index`, `globex_interest_rates` and
`globex_nikkei_225_dollar`, and `13:30` for `globex_energy`. `globex_fx` has no
early close on these dates and no holiday row, which is why its already-landed
set ends the leg at `16:00` — that difference is real, not an inconsistency.

**Verified by probe** (`/tmp/eh-merged-probe`, bin `earlyclip`; nikkei, trade date
2026-01-20, `C = 12:00`): Sunday 17:30 open, holiday 11:59:59 open, holiday
**12:00 closed**, holiday 15:00 closed, holiday 17:30 open, next day 10:00 open —
and every instant answers trade date **2026-01-20**. The corrected set satisfies
the operator's trade dates *and* the shipped T1-backed early-close fences at the
same time. That both hold is the mark of the right answer; §12's set satisfied
only the first.

**Consequence:** the stashed `globex_nikkei_225_dollar` change needs one edit —
`extended(-2, 17:00, 16:00)` becomes `extended(-2, 17:00, 12:00)` — and its three
failing fixtures should then pass unchanged, because they were right all along.
The same correction applies to `globex_energy` (with `13:30`),
`globex_interest_rates` and `globex_equity_index` (with `12:00`, plus the regular
boundary split inside the clipped leg).

**The lesson §12 should have drawn.** I had the answer in the repository and
looked past it: the first thing to check when a row contradicts an intended
change is whether the row cites a **T1** document. §12's row counts took a `grep`
of the module; one line further into the *evidence* would have shown `T1` and a
holiday-schedule filename, and settled it in a minute instead of a round.

## 14. `globex_interest_rates`: derived and ready, with one date that resists mirroring

Recorded 2026-09-26 UTC. Derivation only — no row written. All seventeen merged
trade dates are witnessed in the store, so this family needs **no retrieval**.

The spans, read from product `316` (`ZN`), are the nikkei shape with rates'
values:

| trade date | `-2` day / queue | holiday queue | span ends |
|---|---|---|---|
| 2025-01-21, 2025-02-18, 2025-05-27, 2025-09-02 | Sunday / 16:00 | `12:00` | 16:00 |
| 2025-06-20 (Juneteenth Thu) | **Wednesday / 16:45** | `12:00` | 16:00 |
| 2025-11-28 | **Wednesday / 16:45** | `12:00` | **12:15** |
| 2026-01-20, 2026-02-17, 2026-05-26, 2026-09-08 | Sunday / 16:00 | `12:00` | 16:00 |
| 2026-11-27 | **Wednesday / 16:45** | `12:00` | **12:15** |
| 2027-01-19, 2027-02-16, 2027-06-01, 2027-09-07 | Sunday / 16:00 | `12:00` | 16:00 |
| **2027-07-06** | Sunday / 16:00 | **`13:30`** | 16:00 |
| 2027-11-26 | **Wednesday / 16:45** | `12:00` | **12:15** |

**2027-07-06 is the date that resists mirroring.** Its holiday is the July 4
observed Monday 2027-07-05, and CME publishes `13:30 preopen` there, not the
`12:00` every other Monday holiday carries. The crate already knows this —
`globex_interest_rates.rs:524` ships `early_close(13:30)` for that date where
lines 511, 513 and 517 ship `12:00` — so the merged row's evening leg must end at
`13:30` and its queue open there. A set mirrored from MLK would close the session
three and a half hours early on that one date, and **nothing in the current
fences would catch it**: the trade-date assertions would still pass, because only
`is_open` moves.

So the family needs **four** statics, not three: Sunday-`-2` ending 12:00;
Sunday-`-2` ending 13:30; Wednesday-`-2` ending 12:00; Wednesday-`-2` ending
12:15.

**The rule this makes explicit, and it generalises to the two families left:**
*the merged row's `-2` leg must end at whatever close the crate already ships for
that holiday, and that value is per-date, not per-family.* Read it off the shipped
holiday row rather than from any table — this session's §6 table lists each
family's *usual* value and would have been wrong here.

## 15. `globex_equity_index`: derived and ready — and it is the last family

Recorded 2026-09-26 UTC. Derivation only; no row written. All seventeen merged
trade dates are witnessed, so no retrieval is needed.

**Its holiday close is uniformly `12:00`.** Unlike `globex_interest_rates`, there
is no July-4 exception here: `globex_equity_index.rs` ships `early_close(NOON)`
for 2027-07-05 exactly as for MLK, Presidents, Memorial and Labor, so the
per-date rule that mattered for rates does not bite on this family. The
day-after-Thanksgiving close is `QUARTER_PAST_NOON` = `12:15`.

**It is also the family that needs the regular-boundary split inside the clipped
leg**, which is what makes its block sets longer rather than its values harder.
The equity-index envelope carries a `regular` session 08:30-15:15, so a merged
span whose holiday leg ends at `12:00` has `extended` up to 08:30 and `regular`
from 08:30 to that close. Three statics:

```
Sunday eve, C = 12:00:                 Wednesday eve, C = 12:00:
  order_entry(-2, 16:00, 17:00)          order_entry(-2, 16:45, 17:00)
  extended(-2, 17:00, 08:30)             extended(-2, 17:00, 08:30)
  regular(-1, 08:30, 12:00)              regular(-1, 08:30, 12:00)
  order_entry(-1, 12:00, 17:00)          order_entry(-1, 12:00, 17:00)
  extended(-1, 17:00, 08:30)             extended(-1, 17:00, 08:30)
  regular(0, 08:30, 15:15)               regular(0, 08:30, 15:15)
  extended(0, 15:15, 16:00)              extended(0, 15:15, 16:00)
```

The third is the Wednesday-eve set with the trade date's own session ending at
the Thanksgiving `12:15`: `regular(0, 08:30, 12:15)` and no trailing `extended`.

| dates | static |
|---|---|
| 2025-01-21, 2025-02-18, 2025-05-27, 2025-09-02, 2026-01-20, 2026-02-17, 2026-05-26, 2026-09-08, 2027-01-19, 2027-02-16, 2027-06-01, 2027-07-06, 2027-09-07 | Sunday, C=12:00 |
| 2025-06-20 (Juneteenth Thu) | Wednesday, C=12:00 |
| 2025-11-28, 2026-11-27, 2027-11-26 | Wednesday, C=12:15 |

**The cascade is the smallest of the remaining two**: `cme` routes equity index
but `cbot` does not, so only `cme` may need rows — and per §14's experience it
probably needs **none**, because the `globex_fx` change already made every one of
these dates disputed on that six-family intersection. Check before inserting; a
duplicate is refused at compile time rather than shipped, but it is a wasted
round.

**One verification worth doing first.** The composite rows for 2026-06-22,
2026-07-06 and 2027-06-21 already carry a seven-block set for this family with a
different shape. A merged row and a composite row are keyed to different trade
dates and should not interact — but the two are adjacent in the same table and
share the `regular` boundaries, so a probe of both a composite date and a merged
date after the change is the cheap way to be sure.

## 16. `globex_equity_index` written and verified — stopped on one composition question

Recorded 2026-09-26 UTC. The family's change is **written, green on everything it
was measured against, and preserved in `git stash`** on branch `stage-5-merged-ei`
(`equity-index merged rows — complete and verified except one DayPolicy
composition question`). It was not shipped, for the reason in §16.2.

### 16.1 What it does

Three statics as §15 derived. Seventeen rows, and the audit's total moves
**161 → 144** with this family at zero. Every fence passed that was expected to
move — the seventeen evidence rows, the block-bound instants fence, the inventory
count (40 → 54) — and, as §15 predicted, **`cme` needed no new rows and no venue
fence fired at all**: the `globex_fx` change had already made these dates
disputed on that intersection.

### 16.2 The question that stopped it

`tests/calendar_policies.rs`'s
`cme_mlk_and_presidents_day_close_at_noon_then_reopen_at_five` fails, and it is
not a stale expectation. It attaches a **caller-supplied `DayPolicy`** whose early
close is keyed to **the holiday** (2026-01-19, 12:00) and asserts that the
Sunday-evening candle *ends* at that close.

With a merged row keyed to the **following trade date**, the span is one session
under 2026-01-20, and the caller's early close — keyed to 2026-01-19 — no longer
clips it. The candle now runs to 2026-01-20 16:00.

**That may be a real regression, not just a test that needs updating.** The
charter says *"an explicit caller `Closed` or `ReplaceSessions` record takes
precedence over the built-in date arrangement; the caller's `DayPolicy` then
clips the result"* — and a consumer that supplies an early close naming a holiday
would reasonably expect it to keep working. Under the merge it silently does not,
because the trade date it would have clipped no longer owns the span.

Two readings, and they are not equivalent:

1. **The composition is right as it now behaves.** The caller named a trade date
   that, on these dates, the operator does not have; a policy keyed to a
   non-existent trade date clipping nothing is defensible.
2. **The composition is wrong.** A caller's `DayPolicy` is a *date* instruction —
   "this venue-local date closes at noon" — and should clip whatever session
   covers that date regardless of which trade date owns it.

This is a design question about `DayPolicy`, not about the equity-index rows.
**It is untested for the three families that already shipped** — the existing
policy test names `GlobexEquityIndex` only, so `globex_fx`,
`globex_nikkei_225_dollar` and `globex_interest_rates` have no coverage of the
combination at all. Their suites are green, but green says nothing here: nothing
was looking.

**Unverified, and the first thing to check next:** attach a `StaticDayPolicy`
whose early close names a merged holiday — 2026-01-19 at `12:00` is the fixture —
to `globex_fx` and see whether the Sunday session still ends there. If it does
not, the three shipped PRs carry the same open question and it should be filed
against them rather than discovered later.

### 16.3 What to do

1. Decide which reading is intended, and if it is (2), fix the composition —
   the merged rows are not the defect.
2. If it is (1), update the test and say in its comment *why* a holiday-keyed
   policy no longer clips, so the next reader does not "fix" it back.
3. Then pop the stash, re-run, and ship. The rest of the change is done and was
   verified before this question appeared.

## 17. Measured: a holiday-keyed `DayPolicy` composes **inconsistently** across families

Recorded 2026-09-26 UTC. Scratch crate `/tmp/eh-merged-probe`, bin `policyclip`,
run at `e5c64fd` — the state where `globex_fx`, `globex_nikkei_225_dollar` and
`globex_interest_rates` have shipped their merged rows and `globex_equity_index`
has not.

The probe attaches a `StaticDayPolicy` whose early close names the **merged
holiday** 2026-01-19 and asks what the Sunday-evening session's bounds become. A
single run at `12:00` proves nothing, because that is also what nikkei's and
rates' built-in rows state — so the probe was re-run with **`10:00`**, which no
family's built-in rows contain. That is the decisive version:

| family | caller says 2026-01-19 closes at | session end reported | clipped? |
|---|---|---|---|
| `globex_nikkei_225_dollar` | 10:00 CT | **10:00 CT** | **yes** |
| `globex_interest_rates` | 10:00 CT | 12:00 CT | **no** |
| `globex_fx` | 10:00 CT | 16:00 CT | **no** |

`globex_nikkei_225_dollar` honours the caller's policy; `globex_interest_rates`
and `globex_fx` ignore it. **The three families carry byte-identical merged block
shapes** (`order_entry(-2, 16:00, 17:00)`, `extended(-2, 17:00, C)`,
`order_entry(-1, C, 17:00)`, `extended(-1, 17:00, 16:00)` with `C = 12:00` for the
first two and `16:00` for fx's `-1` leg), so the difference is **not** explained by
the rows this session wrote. It is either in the policy layer or in something
about how each family's profile resolves an overlaid day.

### 17.1 Settled: the merged rows introduced it, for two of the three families

The same probe was run at **`21e5204`** — `main`, before any of this session's
work:

| family | at `21e5204` (`main`) | at `e5c64fd` (after #143/#144/#145) |
|---|---|---|
| `globex_fx` | **10:00 CT — clipped** | 16:00 CT — **not clipped** |
| `globex_nikkei_225_dollar` | **10:00 CT — clipped** | **10:00 CT — clipped** |
| `globex_interest_rates` | **10:00 CT — clipped** | 12:00 CT — **not clipped** |

**So this is a regression introduced by the merged rows, in two of the three
families that shipped them — and the third behaves differently from the other
two, which is the part that is not explained.** All three rows are byte-identical
in shape and differ only in `C`, so the divergence is not in what this session
wrote.

**Consequences, none of which are optional:**

1. **PRs #143 and #145 carry an open regression.** A consumer whose `DayPolicy`
   names a merged holiday no longer gets that day clipped for `globex_fx` or
   `globex_interest_rates`; it did before. That is a behaviour change outside the
   trade-date fix those PRs claim to be, and it is exactly the class of thing this
   repository's review rule exists to catch.
2. **PR #144 (`globex_nikkei_225_dollar`) does not.** It still clips, so whatever
   distinguishes it is worth finding before touching the other two — the fix may
   simply be to make them match it.
3. **The equity-index change must not ship until this is decided** (§16.2's
   question was the visible symptom; this is the substance).
4. **§16.2's reading (1) is now hard to hold.** It said a policy keyed to a trade
   date the operator does not have legitimately clips nothing. But `main` clipped,
   one shipped family still clips, and a *caller's explicit instruction* about a
   calendar date ceasing to apply is a surprising thing for a data fix to cause.

The likely shape of the answer — not yet verified — is that the policy overlay is
applied per-date to the session the *normal week* associates with that date, and a
replacement row keyed to a different trade date bypasses it for some families and
not others depending on which layer supplies the bound. **That is a hypothesis and
should be tested, not adopted.**

### 17.2 Which date clips, per family

A second probe attaches the same `10:00` close to each candidate **date** in turn
and reads the Sunday-evening session's end. This is the diagnostic that says where
the policy attaches:

| policy names | `globex_fx` | `globex_nikkei_225_dollar` | `globex_interest_rates` |
|---|---|---|---|
| 2026-01-18 (the Sunday) | 16:00 — no effect | 12:00 — no effect | 12:00 — no effect |
| 2026-01-19 (the holiday) | 16:00 — no effect | **10:00 — clipped** | 12:00 — no effect |
| 2026-01-20 (the trade date) | 16:00 — no effect | 12:00 — no effect | 12:00 — no effect |

Three different behaviours from three byte-identical block shapes:

- **`globex_nikkei_225_dollar`** is clipped, by a policy naming the **holiday** —
  which is the date `main` clipped by, so its behaviour is unchanged.
- **`globex_interest_rates`** is clipped by **nothing**. A policy naming the
  Sunday, the holiday or the trade date all leave the bound at the built-in
  `12:00`.
- **`globex_fx`** is likewise clipped by nothing, its bound staying at its own
  built-in `16:00`.

**Read this as a layer question, not a date question.** On `main` a holiday-keyed
policy clipped all three, which is consistent with the overlay being applied to
the session the *normal week* associates with that date. A replacement row keyed
to a different trade date supersedes that session, and the overlay — applied
before or to the superseded layer — then has nothing to clip. Nikkei is the odd
one out, and the likeliest reason is that its replacement blocks are `extended`
where its normal-week envelope is `regular`, so a session of a different kind
survives the replacement and the overlay still reaches it; the other two replace
`extended` with `extended`. **That is a hypothesis, stated to be tested, not a
conclusion.**

**The design recommendation, for the maintainer.** The charter's words are *"the
caller's `DayPolicy` then clips the result"* — the result, not a layer beneath it.
A `DayPolicy` is a caller's statement about a calendar date; it should clip
whatever session covers that date, whoever supplied it. On that reading the
overlay must be applied **last**, after replacement resolution, and the fix is in
the policy layer rather than in any of these rows. That reading also keeps
`globex_nikkei_225_dollar`'s current behaviour as the correct one and makes the
other two match it — which is the cheapest of the available fixes.


## 18. Correction: §17's "regression" was my misreading. The composition is correct.

Recorded 2026-09-26 UTC. **This supersedes §17 and §17.1 entirely, and the
"should not merge" flags I posted on #143 and #145 were wrong.** Both PRs are
sound on this point.

The thing I failed to read is the API's own key. `DayPolicy::early_close_ssm` is

```rust
fn early_close_ssm(&self, trade_date: NaiveDate) -> Option<u32>;
```

— keyed by **trade date**, not by calendar date, and documented as *"Moves the
**trade date's** final close"*, with the overlay clipping a
`SessionExceptionSource` day *"exactly as it clips a normal week"*. So the
question I posed — *is a `DayPolicy` a date instruction or a trade-date
instruction?* — is already answered by the trait, and it is the second.

**Measured, with the probe corrected to read a leg that belongs to the merged
trade date** (the Monday-evening session, bounds read at Monday 18:00, caller
closing at 10:00):

| policy names | `globex_fx` | `globex_nikkei_225_dollar` | `globex_interest_rates` |
|---|---|---|---|
| 2026-01-18 | 01-20 16:00 — no effect | 01-20 16:00 — no effect | 01-20 16:00 — no effect |
| 2026-01-19 | 01-20 16:00 — no effect | 01-20 16:00 — no effect | 01-20 16:00 — no effect |
| **2026-01-20** | **01-20 10:00 — clipped** | **01-20 10:00 — clipped** | **01-20 10:00 — clipped** |

All three families clip, identically, when the caller names the trade date that
owns the span. That is the documented behaviour, reached consistently.

**What §17 actually measured, and why it misled me.** All three of its probes read
the *Sunday* leg while varying the policy's date. A holiday-keyed policy cannot
affect a leg owned by the next trade date — correctly — and the only reason
`globex_nikkei_225_dollar` appeared to be clipped was that its own holiday row
(`early_close(12:00)` on 2026-01-19) is still live under the replacement. So §17
compared a correct no-op against a leftover row of a different provenance and read
the difference as a regression.

**Lesson, and it is the sharpest of the session.** I declared a served-behaviour
regression from a probe I designed before reading the trait it was probing. One
look at the signature — `early_close_ssm(&self, trade_date: NaiveDate)` — would
have prevented it, and it cost two public PR comments that now needed correcting.
*Read the API you are measuring before you measure it.* The four mechanisms for
obtaining a review all failed this session, and this is the defect one would have
caught.

**Consequences.** No policy-layer change is needed; my recommendation to apply the
overlay last was wrong and is withdrawn. The `DayPolicy` composition needs no
CHANGELOG note. `globex_nikkei_225_dollar`'s residual holiday-keyed clip is the
only open oddity, it is *pre-existing row provenance* rather than anything these
PRs introduced, and it is worth a sentence in its evidence file rather than a
code change.

## 19. `globex_energy`: derived, written, verified — and stashed mid-cascade

Recorded 2026-09-26 UTC. The module change and its seventeen rows are **written
and verified**; the venue cascade is not. It is in `git stash` on branch
`stage-5-merged-energy` (`energy merged rows — module+rows verified (audit
144->127); needs evidence x3, comex/nymex/cme cascade, counts and tests`), based
on `main` = `9589257`.

### 19.1 The derivation, which is unusually uniform

All seventeen merged trade dates witnessed, no retrieval needed. **Every holiday
closes at `13:30`** — including 2027-07-05, the July 4 observed Monday, which for
`globex_interest_rates` was the one `13:30` exception and here is simply the rule.
The day-after-Thanksgiving close is **`13:45`**. The `-2` queue is `16:00` when
that day is a Sunday and the weekday `16:45` when the holiday is a Thursday.

So three statics, four blocks each, and **no regular-boundary split** — this
family's envelope is `extended` throughout, unlike `globex_equity_index`. The
audit moves **144 → 127** with the family at zero, and the build is green.

### 19.2 What is left, and it is the largest cascade of the five

Unlike `globex_nikkei_225_dollar`, this family feeds **three** venue tables:

- **`comex`** and **`nymex`** route energy alone, so each reproduces the family
  table whole and needs all seventeen rows **and** its own evidence rows. Both
  currently `use` `globex_energy::SATURDAY_SESSION_BLOCKS`, so the new statics
  should be exported `pub(crate)` and imported the same way rather than copied —
  the fence `the_energy_venues_carry_the_family_table_unchanged` exists to hold
  them identical.
- **`cme`** routes six families. Per §14's experience it probably needs **no** new
  rows, because the earlier families already made these dates disputed there —
  but `the_venue_table_is_the_intersection_of_its_families` is failing, so check
  rather than assume.
- Six fences are red: the two evidence fences, the inventory count, the energy
  venue fence, the intersection fence, and
  `session_exceptions::a_caller_replacement_suppresses_the_built_in_row_for_that_trade_date`,
  which uses this family as its fixture and needs reading rather than updating.

Nothing here is novel — it is the same cascade as §14 and §17.2, one table wider.
Pop the stash, work the fences in the order the suite reports them, and expect the
evidence rows (three files) to be the bulk.
