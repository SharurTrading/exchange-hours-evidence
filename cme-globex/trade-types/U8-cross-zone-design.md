<!-- SPDX-License-Identifier: MIT-0 -->

# U-8 — cross-zone representability for the CME TAM and BTIC shapes

**Gate:** `U8-cross-zone-design`, from
`docs/plans/2026-09-05-cme-trade-type-handoff.md` §2 row **U-8**.
**Written:** 2026-09-06. **For:** the maintainer to decide. Nothing is implemented, and no file
inside `exchange-hours-rs` was edited.

**Evidence:** `raw/U8-cross-zone-design/INDEX.md` (six CME artifacts captured first-hand today
through the public text reader, plus two independent tz-database computations). Second-hand
artifacts already in `cme-globex/shape-queue/` are cited by file and block number rather than
re-fetched.

**Revision note (2026-09-06, second pass over the same gate id).** Every stored artifact was
re-hashed against `SHA256SUMS.txt` (all pass), the CME service bytes were re-read rather than
quoted from the draft, the tz arithmetic was re-derived by a second script written from scratch
(`recheck-2026-09-06b.py`), and every in-repo line was re-read at HEAD `fdc5408`. Four corrections
landed, none of them load-bearing: the US/UK misalignment is **21 or 28 calendar days a year**, not
20 or 27 (§1.5); the boundary nearest Chicago midnight is **Nikkei/TOPIX BTIC at 00:30 CT**, not
`CLC` at 01:00 (§1.6 ii, §3.5, §4 T8); there are **six** shipped `reference_delta_seconds` call
sites, not five (Option G); and the Energy TAM FAQ carries `Published Time: 2024-06-05`, so it is
not an undated page (`INDEX.md`). §4 T5 was widened from two transition weekends to all four, and
the shipped ICE Endex test named as its template. The recommendation is unchanged.

---

## The one-line answer

**The crate already solves this, six times, and none of the six needed an API change.**
`ICE Endex`, `ICE Abu Dhabi`, `Eurex fixed income`, `Eurex` (the benchmark-index Asian slice), `B3`
and `BMV` all express a grid whose endpoints are anchored in two zones, by shipping **two static
profiles and selecting between them with `reference_delta_seconds`** — a pure function of the
caller's instant and the IANA database. Two of the six are `MarketHoursKey`s, not exchanges, so the
precedent exists on the side U-8 needs it.
U-8 is therefore not "is this representable"; it is "is the shipped pattern the right one *here*,
and what does it cost". It is, and the cost is one selector function per shape plus a four-instant
test.

---

## 1. The affected shapes, their two anchors, and the measurement

### 1.1 What "affected" means

A shape is affected when its open and its close are anchored in zones whose **relative UTC offset
changes during the year**. That is narrower than "two cities are named".

- `America/New_York` against `America/Chicago` shares one DST calendar and a constant −1 h offset.
  A New-York-anchored close is **exactly** representable in a Chicago-tz profile. **TMAC**
  (16:00 ET), **equity/sector/AIR BTIC** (16:00 ET), **credit BTIC**, **TACO**, and **crypto BTIC
  New York** (16:00–16:05 ET) are therefore *not* U-8 problems. Do not spend the mechanism on them.
- `Europe/London` against `America/Chicago` misaligns twice a year, because the UK switches on the
  last Sunday of March/October and the US on the second Sunday of March / first Sunday of November.
- `Asia/Singapore`, `Asia/Shanghai`, `Asia/Hong_Kong`, `Asia/Tokyo` observe **no DST at all**, so
  the Chicago clock of a fixed local instant there moves at every US transition. Both states are
  large, not marginal.

### 1.2 The twelve affected shapes

One row per proposed key. Counting *moving rule endpoints* rather than shapes gives fifteen, because
`6EB`'s interruption and the two crypto BTIC stops each have two ends that move together; nothing
downstream depends on which number you quote, but the two must not be conflated.

Chicago clock values below are the boundary as it appears in a `America/Chicago`-tz profile.
"Aligned" = the state the golden file renders (see §3.6). Weekday counts are for calendar 2026
(261 weekdays), from `raw/U8-cross-zone-design/drift-computation-2026-09-06.txt` and reproduced
independently in `raw/U8-cross-zone-design/recheck-2026-09-06b.txt`.

| Shape (roots) | Open anchor | Moving boundary | Foreign anchor | Chicago value A | Chicago value B | days A / B (2026) |
|---|---|---|---|---|---|---|
| Energy TAM London `CLL BZL HOL RBL` | 17:00 `America/Chicago` | daily close | 16:30 `Europe/London` | 10:30 | 11:30 | 241 / 20 |
| Energy TAM Singapore `CLS BZS` | 17:00 Chicago | daily close | 16:30 `Asia/Singapore` | 03:30 | 02:30 | 170 / 91 |
| Energy TAM Shanghai `CLC` | 17:00 Chicago | daily close | 15:00 `Asia/Shanghai` | 02:00 | 01:00 | 170 / 91 |
| Gold TAM `GCD` | 17:00 Chicago | daily close | 15:02 `Europe/London` | 09:02 | 10:02 | 241 / 20 |
| Copper TAM `HGF` | 17:00 Chicago | daily close | 12:35 `Europe/London` | 06:35 | 07:35 | 241 / 20 |
| Europe-index BTIC `DVT E3T` | 17:00 Chicago | daily close | 16:30 `Europe/London` | 10:30 | 11:30 | 241 / 20 |
| FTSE China 50 BTIC `FTC` | 17:00 Chicago | daily close | 16:00 `Asia/Hong_Kong` | 03:00 | 02:00 | 170 / 91 |
| Nikkei BTIC `NIT NKT` † | 17:00 Chicago | daily close | 15:30 `Asia/Tokyo` | 01:30 | 00:30 | 170 / 91 |
| TOPIX BTIC `TPB TPT` | 17:00 Chicago | daily close | 15:30 `Asia/Tokyo` | 01:30 | 00:30 | 170 / 91 |
| Crypto BTIC London (9 roots, row 8) | 24/7 grid | 5-min stop start | 16:00 `Europe/London` | 10:00 | 11:00 | 241 / 20 |
| Crypto BTIC APAC (5 roots, row 14) | 24/7 grid | 5-min stop start | 16:00 `Asia/Hong_Kong` | 03:00 | 02:00 | 170 / 91 |
| FX BTIC `6EB` | 17:00 Chicago | **interior gap**, both ends | 15:40 → 16:30 `Europe/London` | 09:40–10:30 | 10:40–11:30 | 241 / 20 |

† Nikkei BTIC additionally carries a second, **Noon–17:00 ET** midday window that TOPIX lacks
(`shape-queue/btic-basis-trade-at-index-close-inventor.json` block [11], row 23:
`PO 15:30, Ready 16:00, halt 21:00`). That window is New-York-anchored and therefore fixed on the
Chicago clock; only the Tokyo close moves. Same key, one moving boundary.

`6EB` was **not** in U-8's list and belongs there. Its cross-zone boundary is an interior
interruption inside an otherwise Chicago-anchored 17:00→16:00 CT envelope, so it needs the same
mechanism applied to two rule endpoints rather than to a close
(`shape-queue/btic-basis-trade-at-index-close-inventor.json`, evidence block [11], row 34:
`PO 15:15, Ready 15:30 … Close 14:40` = 16:15/16:30 London restart, 15:40 London roll; the same
file's block [6] quotes CME: *"Trading halt from 3:40 p.m. London time (9:40 a.m./10:40 a.m. CT)
to 4:30 p.m. London Time (10:30 a.m./11:30 a.m. CT)"*).

### 1.3 The measurement, first-hand

The prior probe recorded in U-8 is confirmed and extended. `id=8407` is `GCD`, group `GM`, *Gold
London Trade At Marker First PM*; `id=7956` is `FTC`, group `C1`, *BTIC E-mini FTSE China 50 Index
Futures*. All four files are in `raw/U8-cross-zone-design/`.

| week | US / UK state | `GCD` events (`svc-8407-*.txt`) |
|---|---|---|
| 2026-10-26 → 10-30 | US CDT, UK GMT (**misaligned**) | `closed@10:02`, `preopen@16:50`, `open@17:00` |
| 2026-12-07 → 12-11 | US CST, UK GMT (aligned) | `closed@09:02`, `preopen@16:50`, `open@17:00` |
| 2027-03-15 → 03-19 | US CDT, UK GMT (**misaligned**) | `closed@10:02`, `preopen@16:50`, `open@17:00` |

| week | US state | `FTC` events (`svc-7956-*.txt`) |
|---|---|---|
| 2026-10-26 → 10-30 | US CDT | `closed@03:00`, `preopen@16:45`, `open@17:00` |
| 2026-12-07 → 12-11 | US CST | `closed@02:00`, `preopen@16:45`, `open@17:00` |

Verbatim, `svc-8407-oct.txt`:
`{"tradingDate":"2026-10-26","eventTime":"10:02","marketEventType":"closed"}` …
`{"tradingDate":"2026-10-27","eventTime":"17:00","marketEventType":"open"}`.
Verbatim, `svc-8407-dec.txt`:
`{"tradingDate":"2026-12-07","eventTime":"09:02","marketEventType":"closed"}`.

Three things follow, and they are the whole factual basis of this memo:

1. **The open never moves.** `open@17:00` and its pre-open (`16:50` for `GM`, `16:45` for `C1`) are
   identical in every week sampled. The open is `America/Chicago`.
2. **The close moves exactly with the foreign zone**, in both the spring and the autumn
   misalignment windows, and the 2027 sample shows CME publishes it that way six months ahead.
3. **The state is a function of the two zones' offsets, not of a date CME announced.** No CME
   notice states "on 2026-10-26 the close becomes 10:02". Encoding this as revision rows would
   invent 2 dates per shape per year — precisely what LAW-NO-FABRICATED-DATES forbids.

### 1.4 CME publishes both states itself, for three of the shapes

`raw/U8-cross-zone-design/energy-tam-faq.jina.txt`, captured 2026-09-06, Q7 verbatim:

> CLS and BZS trading halts at the marker time, daily, at 4:30 p.m. Singapore time (2:30/3:30 a.m.
> Central time).
>
> CLC trading halts at the marker time, daily, at 3:00 p.m. China time (1:00/2:00 a.m. Central
> time).
>
> CLL, RBL, HOL and BZL trading halts at the marker time, daily, at 4:30 p.m. London time.

For `CLS/BZS` and `CLC`, **the two Central values are the operator's own published pair**
(`2:30/3:30` and `1:00/2:00`), matching the table in §1.2 exactly. A two-grid encoding for those
two keys is transcription of a primary source, not inference. For the four London TAM roots CME
states only the London time, so their two Chicago values are derived from the tz database — the
same standing the `ICE Endex` and `ICE Abu Dhabi` tables already have (`verification.md:144-145`:
*"recurring US/EU DST grids are exact"*; *"the New-York-locked grid and pre-open are translated
into `Asia/Dubai` with date-aware US DST selection"*).

Note also that this is **session language** under LAW-SESSION-NOT-EXPIRY — *"trading halts … at the
marker time, daily"* — which is why these closes may enter a profile at all. The adjacent marker
*calculation* windows (gold *"3:00 p.m. – 3:02 p.m. prevailing London time"*, copper *"12:34 p.m. –
12:35 p.m. London Time"*) are not, and `GCD`/`HGF` rest on the service's own `closed@` events
instead (handoff §1.4, overturning the shape-queue verdict).

### 1.5 How much drift, and exactly how wrong a single grid would be

`drift-computation-2026-09-06.txt` enumerates the misalignment windows 2010–2030, and
`recheck-2026-09-06b.txt` reproduces them from an independently written script. The US/UK
misalignment is **21 or 28 calendar days a year** — 14 or 21 days in spring (the US springs forward
first) plus exactly 7 in autumn (the UK falls back first) — which is **15 or 20 affected weekdays**.
2026 is a long year: 2026-03-08…03-28 (21 days, 15 weekdays) and 2026-10-25…10-31 (7 days, 5
weekdays) = 20 weekdays. The autumn window is always exactly 7 days, because the last Sunday of
October and the first Sunday of November are always one week apart. The pattern is stable across
the entire audit window and to 2030.

*(An earlier draft of this memo said "20 or 27 calendar days"; that counted the spring transition
Sunday out and the autumn one in. The weekday figures in §1.2 were unaffected and are correct.)*

- **London-anchored shapes, single grid encoded as the aligned state (10:30 CT):** the crate reports
  `Closed` while the market is executing, for **60 minutes on each of 20 weekdays in 2026 — 20
  hours a year of false-closed executable window**. Under AGENTS.md's *"Executable windows are the
  priority"* that is the most serious class of error the crate can make.
- **London-anchored shapes, single grid encoded as the misaligned state (11:30 CT):** false-**open**
  for 60 minutes on 241 weekdays. Worse: a caller routing an order at 11:00 CT in July is told the
  market is open when `CLL` halted half an hour earlier.
- **Asia-anchored shapes:** there is no "mostly right" single grid. Whichever of the two you encode,
  you are an hour wrong on **91 or 170 of 261 weekdays** (35 % or 65 % of the year).

The drift is **real market behaviour, not a modelling artifact**: because the two anchors sit in
zones whose relative offset changes, the executable window genuinely lengthens by an hour in the
misalignment weeks (`CLL` runs 17.5 h normally and 18.5 h in a misaligned week; `CLS` runs 10.5 h
in US summer and 9.5 h in US winter). A single-grid encoding asserts the window never changed
length, which is a claim about the market and a false one.

### 1.6 Two structural facts that make the problem tractable

**(i) The state only ever changes while the market is shut.** Every DST transition relevant here
lands outside a running session for these shapes:

- US transitions occur at 02:00 local Sunday — the Sunday session opens at 17:00 CT, fifteen hours
  later.
- UK transitions occur at 01:00 UTC Sunday, i.e. **Saturday 20:00 CDT** — before the Sunday open.
  (Always CDT: the UK's spring transition is always after the US one, and its autumn transition
  always before, so the US is on daylight time on both UK transition dates.)
- The Asian anchors have no transitions at all.

So no occurrence of any of these rules ever spans an offset change. Combined with
`schedule.rs`'s `profile_for_open_day` — which anchors selection at `OPEN_DAY_ANCHOR_SSM = 86_399`
on the **opening** local day and resolves each occurrence's open *and* close from that one profile
— a two-state selector can never split a running session, which is the hazard
LAW-NO-FABRICATED-DATES names for day-level boundaries.

Worked check for the tightest case, `CLL` across 2026-10-25: the UK fell back at 2026-10-25 01:00
UTC = 2026-10-24 20:00 CDT (market shut); the Sunday session opens 2026-10-25 17:00 CDT; its
profile anchor is Sunday 23:59:59 CDT; `reference_delta_seconds` evaluates at Sunday noon Chicago,
by which time the UK has already switched → misaligned grid → close Monday 11:30 CT, which is what
`svc-8407-oct.txt` publishes for the same week.

**(ii) The swap never flips wrap vs. non-wrap for any of the twelve shapes.** Every moving
close in §1.2 stays in `00:30..11:30` and therefore keeps wrapping past local midnight, and the
`6EB` interior gap stays same-day in both states. The trade-date default (`identity.rs`
`assign_normal`: the local date of the final close in the profile's tz) therefore returns Monday in
both states for every shape. **The nearest miss is the Nikkei/TOPIX BTIC close at 00:30 CT** in the
US-winter state — thirty minutes from Chicago midnight — with `CLC` at 01:00 CT second
(`recheck-2026-09-06b.txt`, Q4). A foreign-anchored close inside an hour of Chicago midnight is
where this margin runs out: the misaligned state would push it across midnight, flip
`wraps_to_next_day()`, and move the trade date by a day between the two profiles. Any
implementation should assert `wraps_to_next_day()` agrees across the two profiles rather than
leave that to review, and should say so loudest for the Tokyo-anchored pair.

---

## 2. Representation options

Six were considered. For each: API surface, serde/golden impact, LAW-DETERMINISM, LAW-PANIC,
migration for existing keys, and the laws touched.

### Option A — per-rule time zone on `SessionRule`

Add `tz: Tz` (or `close_tz: Option<Tz>`) to `SessionRule` so one rule can open in Chicago and close
in London.

- **API surface:** `SessionRule` is `pub`, `#[non_exhaustive]`, `Copy`, `Serialize`, `Deserialize`,
  and is *the* atom the whole crate is built on. Every profile table in `src/calendar/schedules/`
  (94 exchanges + 31 keys) is a struct literal over it. `SessionRule::new` and `validate` gain a
  new domain; `wraps_to_next_day()` becomes ill-defined (the "next local day" of *which* zone?).
- **serde/golden:** a new field changes the wire format of a public type. `#[serde(default)]` can
  keep old payloads readable, but the serde identity fences and `rule_validation.rs` both move, and
  `golden_grids.rs`'s renderer must print a zone per row — i.e. **every line of
  `tests/golden/normal_week_grids.txt` is rewritten**, so the one artifact designed to make a
  schedule edit reviewable becomes an unreviewable diff on the very change it is meant to police.
- **LAW-DETERMINISM:** fine (still pure).
- **LAW-PANIC:** new failure surface. `normal_week_rule_intervals` projects rules onto a nominal
  86 400 s/day axis; a cross-zone rule has no nominal duration, so `normal_week_open_seconds`
  either lies or needs a real-time computation, and `resolve_rule_bounds`'s `raw_open >= raw_close`
  guard starts rejecting legitimate occurrences near a transition.
- **Migration:** touches every existing key and venue.
- **Laws:** structural rules (one canonical wire form, `#[non_exhaustive]` discipline), and it
  risks LAW-PANIC.
- **Verdict:** the largest possible change for nine keys. Reject.

### Option B — profile-level `close_tz` override

Add `close_tz: Option<Tz>` to `StaticHoursProfile` (`pub(crate)`) and carry it through `MarketHours`
(`pub`), resolving `close_ssm` in `close_tz` when present.

- **API surface:** `MarketHours` is public with `pub` fields and a 7-argument `MarketHours::new`.
  An 8th positional argument is a breaking change for every external caller that models its own
  venue; a second constructor avoids that but leaves two constructors forever. `MarketHours.tz`
  stops meaning "the venue's zone" and starts meaning "the open's zone", which quietly changes what
  `is_closed_all_day_on` and `trade_date` mean for consumers.
- **serde/golden:** `MarketHours` is not itself serialized, so no wire break; but the golden
  renderer must print the second zone, and `week.rs`'s nominal-week arithmetic has the same problem
  as Option A.
- **LAW-DETERMINISM:** fine.
- **LAW-PANIC:** `resolve_rule_bounds` must pick the close's civil day in a foreign zone. Around
  Chicago midnight (`CLC`) the "same day / next day" choice becomes genuinely ambiguous, and a
  wrong pick produces a 24-hour session rather than an error — an unspecified answer where the
  crate currently has a total, well-defined one.
- **Migration:** every existing profile gets `close_tz: None`; the golden file is rewritten;
  `identity.rs` needs a rule for which zone names the trade date.
- **Laws:** modelling convention *"Session rules are seconds-since-local-midnight in the venue's own
  IANA zone"* would have to be rewritten, and *"the venue's zone stays an internal detail"* weakens.
- **Verdict:** cheaper than A, still a public-semantics change for a problem with a zero-API
  solution. Reject.

### Option C — split each shape into two profiles joined by a rule

Model the Chicago-anchored leg and the foreign-anchored leg as separate profiles and join them.

- A profile carries exactly one `tz`, so "two profiles" means two keys — and then **no key answers
  "is `CLL` tradeable at 11:00 CT"**, which is the only question a caller asks. Joining them inside
  one key would need a new sum type in `ExchangeCalendar` and a new merge rule in
  `containing_session_with`.
- Splitting the *session* instead (Chicago 17:00→24:00, then 00:00→close) does not help: the second
  piece's close is still a foreign instant expressed as a Chicago SSM, so the drift is untouched,
  and the split is visible to callers as two sessions unless the key opts into
  `joins_adjacent_same_kind` (`identity.rs:18`), which exists only for CME crypto and `ECBTC` and is
  documented as *"an identity capability, not a shape heuristic"*.
- **Laws:** *"Identity-dependent topology belongs on the date-aware identity calendar"* and the
  structural rule that `ExchangeCalendar` stays `Copy + Send + Sync + 'static` with allocation-free
  hot-path queries.
- **Verdict:** solves nothing it does not first break. Reject.

### Option D — express the whole grid in the close's zone and accept an open that drifts

Give `CLL` a `Europe/London` profile with a fixed 16:30 close and a fixed 23:00 London open.

- **Quantified drift:** exactly the mirror of §1.5. The open would be an hour wrong on the same 20
  weekdays (London shapes) or on 91/170 weekdays (Asian shapes). The instants misreported are at the
  **start** of the executable window, so the crate would either refuse an hour of genuine trading or
  claim an hour before the market opened. Same magnitude, same class of error, worse target.
- It also imports a second problem for free: `DayPolicy` and `is_closed_all_day_on` become
  London-dated for a US-holiday venue, and `assign_normal`'s trade date becomes the London date of
  the close.
- **Note the symmetry**, because it is the crux of the whole gate: a profile has one `tz`, so
  whichever zone you choose, *the other endpoint needs two values*. Option D is not an alternative
  to a two-state encoding — it is the same two-state encoding with the roles swapped, minus the
  benefit. The only true "accept the drift" variant is a single grid, and §1.5 prices that.
- **Verdict:** reject on the executable-window priority.

### Option E — model the close as a "marker close" event rather than a session boundary

Add a phase kind that records the marker instant without ending a session.

- This is LAW-SESSION-NOT-EXPIRY applied in the wrong direction. For the energy TAM shapes CME
  states *"trading halts at the marker time, daily"* — that **is** session language, and the
  handoff's decision rule admits it precisely because of that sentence. Downgrading it to an event
  would make the crate answer "open" at 12:00 CT for a `CLL` position that cannot trade, which is
  the false-open failure of §1.5 made permanent and deliberate.
- **Verdict:** reject. (For `GCD`/`HGF`, where the *prose* is only a calculation window, the correct
  conservative answer is not a new event type — it is either the service's own `closed@` events, as
  the handoff already argues, or leaving the shape unmapped under Option F.)

### Option F — defer: leave the shapes `UNMAPPED`

- **Cost:** 9 keys / ~40 roots stay unmodelled, including all five TAM shapes.
- **Benefit:** asserts nothing false; costs nothing; fully law-clean.
- This is the honest fallback and should stay the answer for any shape whose *hours* are not
  sourced in session language. It is **not** needed for representability, because Option G exists.

### Option G — offset-selected seasonal profile pair (the shipped pattern) ✅

Keep `tz: America::Chicago`. Ship two `StaticHoursProfile` values per shape — one per relative
offset state — and pick between them in the key's `*_profile_at` with
`schedules::timeline::reference_delta_seconds`, exactly as **six** shipped modules already do
(`ice_endex.rs:150`, `ice_abu_dhabi.rs:103`, `eurex_fixed_income.rs:287`, `europe.rs:120`,
`b3.rs:201`, `bmv.rs:235`).

The crate has already written down this memo's central argument, in
`eurex_fixed_income.rs:36-41`, for a `MarketHoursKey`:

> A single fixed-local-wall-clock profile would therefore be wrong for roughly half of every year,
> so the seasons are two profiles selected by the venue's own UTC offset

and its selector doc adds the structural reason the switch is safe here too:

> Both seasonal timelines carry the same effective dates; the venue's own UTC offset on that day
> picks the CET or CEST grid. Berlin's changeover falls on a Sunday, which is not a Eurex trading
> day, so the two never disagree about a day that has a session.

Sketch (illustrative; not to be applied):

```rust
// London is six hours ahead of Chicago whenever both are on standard time or
// both are on summer time; five hours in the two windows a year where the US
// has already sprung forward, or the UK has already fallen back, and the other
// has not. CME states only "4:30 p.m. London time", so the two Chicago values
// come from the zone database, as ICE Endex's and ICE Abu Dhabi's do.
const LONDON_ALIGNED_DELTA_SECONDS: i32 = 6 * 3600;

pub(crate) fn energy_tam_london_profile_at(as_of: DateTime<Utc>) -> &'static StaticHoursProfile {
    let day = local_date(as_of, US::Central);
    if day < TAM_LONDON_LAUNCH { return &CLOSED_CENTRAL; }      // SER-5788, trade date 2011-06-13
    let seasonal = if reference_delta_seconds(as_of, US::Central, Europe::London)
        == LONDON_ALIGNED_DELTA_SECONDS { ALIGNED } else { MISALIGNED };
    select_revision(day, seasonal.baseline, seasonal.revisions)
}
```

- **API surface change: none.** No public type, field, constructor or signature moves.
- **serde impact: none.** Keys serialize by canonical name from the `market_hours_keys!` table
  (`key_serde.rs`); a seasonal profile is invisible to the wire format.
- **golden impact:** additive rows only for the new keys; **no existing key's rows move** (the
  coverage plan's explicit requirement). See §3.6 for the one caveat — the golden file renders only
  one of the two states.
- **LAW-DETERMINISM:** satisfied structurally. `reference_delta_seconds` reads no clock, performs no
  I/O and is already shipped; it is a pure function of `as_of` and the compiled tz database, so a
  backtest and a live query take the identical path.
- **LAW-PANIC:** satisfied. `reference_delta_seconds` resolves through `mk_local_open`, documented
  total for any zone and input, and the branch is a two-arm `if`/`else` with no fallible step.
- **LAW-NO-FABRICATED-DATES:** satisfied, and this is the decisive point. The seasonal switch is
  **not** a revision row and asserts **no** effective date; the `revisions!` timeline carries only
  genuine sourced days (`SER-5788` trade date 2011-06-13 for London TAM, `SER-5794` 2011-07-11 for
  Singapore, `SER-9380` 2024-06-17 for Shanghai, Globex Notice 20171016 trade date 2017-10-23 for
  `GCD`, Globex Notice 20190211 trade date 2019-02-25 for `HGF`). The pattern is already blessed by
  the B3 comment: *"Circular 127/2015-DP introduced the recurring pair from 2015-12-21 and tied it
  to the Brazil/New York daylight-time relationship"* — a dated start for the regime, an undated
  function inside it.
- **Robust to a rule change nobody announces:** if the EU or the US alters its DST rule, the offset
  function tracks the tz database automatically. A hard-coded date table would silently rot, and CME
  would issue no notice, because from CME's side nothing changed — *"4:30 p.m. London time"* still
  holds.
- **Migration for existing keys: none.** `EurexFixedIncome` already ships this shape as a key
  (`eurex_fixed_income.rs:283-297`), so the precedent exists on the key side and not only on the
  exchange side.
- **Laws touched:** none adversely. AGENTS.md already anticipates it: *"A cross-zone or otherwise
  recurring selector also needs date-aware `ExchangeCalendar` transition coverage"* (Adding or
  revising a venue, item 3).

---

## 3. Recommendation

**Adopt Option G.** Then apply Option F per shape, on the *evidence*, not on the representation.

### 3.1 Reasoning

1. **The representability blocker is false.** U-8 reads *"neither endpoint is expressible without
   the other drifting"*. That is true only of a *single* profile. The crate has never been limited
   to one profile per era: `select_revision` returns a `&'static StaticHoursProfile`, and five
   shipped modules already return different ones for the same calendar date depending on the
   instant's offset state. `ICE Endex` is the exact analogue — an Amsterdam-zoned grid anchored to
   New York, with a `MISMATCH` profile for precisely the weeks in §1.5, tested at both the autumn
   (2026-10-27) and spring (2027-03-16) windows.
2. **The alternative is a first-class error, not a rounding.** §1.5 prices a single grid at 20
   hours/year of false-closed executable window (London) or an hour wrong on up to 65 % of weekdays
   (Asia). AGENTS.md ranks executable-window gaps above everything else and says row count is not
   impact.
3. **It costs no public surface.** Options A and B change `SessionRule` or `MarketHours` — the two
   types the whole crate and every downstream caller are built on — to serve nine keys. Option G
   changes nothing a caller can see.
4. **For three shapes it is transcription.** CME's own `(2:30/3:30 a.m. Central time)` and
   `(1:00/2:00 a.m. Central time)` are the two profiles, written out by the operator (§1.4).
5. **It stays honest about what is unknown.** Option G is a *representation*; it does not source an
   hour. `GCD`, `HGF`, `CLS/BZS` and `CLC` remain gated on their own evidence, U-4 (regular vs
   extended) is untouched, and any shape that fails the handoff's session-language test still goes
   `UNMAPPED` under Option F.

### 3.2 Unblocked by this decision

The handoff gates five TAM shapes on U-8 (`globex_energy_tam_london`,
`globex_energy_tam_singapore`, `globex_energy_tam_shanghai`, `globex_gold_tam`,
`globex_copper_tam`) and, in substance, four BTIC shapes (`globex_europe_index_btic`,
`globex_ftse_china_50_btic`, `globex_cryptocurrency_btic_london`,
`globex_cryptocurrency_btic_apac`) plus `globex_nikkei_btic` / `globex_topix_btic` and
`globex_fx_btic_euro`. **U-8 no longer blocks any of them.** What still blocks each is its own
row: the open/pre-open onset, U-4, and (for `GCD`/`HGF`) whether a `closed@` service event is
accepted as session language.

### 3.3 Not affected — do not use the mechanism

`globex_equity_index_btic`, `globex_credit_index_btic`, `globex_cryptocurrency_btic_new_york`,
`globex_equity_index_taco`, `globex_equity_index_tmac`, `globex_commodity_index_btic`. Their
foreign anchor is `America/New_York` (or Chicago outright), a constant offset. A seasonal pair here
would be two identical profiles and pure noise.

### 3.4 Implementation notes for whoever writes the tables

- Pick the **relative delta**, not the venue's own offset. `reference_delta_seconds(as_of, venue,
  reference)` returns `reference_offset − venue_offset`, so with `venue = US::Central`:
  `reference_delta_seconds(as_of, US::Central, Europe::London) == 6 * 3600` is the **aligned**
  state (0 − (−6) in winter, +1 − (−5) in summer) and `5 * 3600` is the misaligned one.
  For the no-DST anchors the delta against Singapore/Shanghai/Hong Kong is `13 h` in US summer and
  `14 h` in US winter, and against Tokyo `14 h` / `15 h` — but prefer
  `reference_delta_seconds(as_of, US::Central, UTC) == 5 * 3600` (US summer) for those, since only
  the US side moves and the intent reads better. Verify the arithmetic against
  `drift-computation.py` rather than from the sign convention alone; it is easy to invert.
- Name the constant and state in a comment *why only two states exist*, with the misalignment window
  table from `drift-computation-2026-09-06.txt`. Two states is a fact about these zone pairs since
  before the January-2010 floor, not a general truth.
- Assert in a test that the two profiles agree on `wraps_to_next_day()`, `has_daily_close`,
  `has_weekend_close`, day masks and rule count — the only thing that may differ is an SSM (§1.6 ii).
- The launch/revision rows go in `revisions!` as usual, and **not** one row per DST change.
- `normal_week_open_seconds()` legitimately differs between the two profiles (five sessions ×
  3600 s = 18 000 s for a five-day shape). That is correct — the window really is longer — so any
  invariant test must expect it rather than assert equality.

### 3.5 Follow-ups that must be opened as GitHub issues before any of this merges

Per LAW-FOLLOW-UPS-ARE-ISSUES, named here means opened:

1. **`session_profile` cannot represent a seasonal key, and its doc claims it can.**
   `futures_profile/profiles.rs` documents `session_profile` as *"equal[ling] the revision
   timeline's selection at any instant on or after the family's knowledge-bound row"*. For
   `EurexFixedIncome` that is already false for roughly half of every year — `FUTURES_EUREX_FIXED_INCOME`
   is the CEST grid. Adding nine seasonal keys makes the inaccuracy load-bearing. The doc must say
   which state the static table is, or the accessor must be documented as summer-state-only.
   **Pre-existing defect; not created by this design.**
2. **`hours_for_market_hours_key`'s doc sentence** *"Keys with no in-scope recorded change resolve
   to their one grid at every instant"* becomes wrong for a seasonal key. Same fix, same issue or a
   sibling.
3. **`6EB` belongs in U-8's shape list** (§1.2) and its interior gap is a two-endpoint case the
   original row did not enumerate.
4. **The COMEX metals-marker page's copper DST carve-out was not independently re-verified today**
   (rate-limited); it is quoted second-hand from
   `shape-queue/tam-taco-tmac-marker-and-close-variants.json` block [4]. If it is cited beside a
   table, re-fetch it first.
5. **The near-midnight wrap risk** (§1.6 ii) deserves a standing note wherever the mechanism is
   documented, because the next cross-zone shape may not be so lucky. The tightest margin among the
   twelve is the **Tokyo-anchored Nikkei/TOPIX BTIC close at 00:30 CT**, not `CLC` at 01:00 as an
   earlier draft of this memo said; both still wrap in both states, so nothing in the design turns
   on it, but the standing note must name the right shape.

### 3.6 The one thing Option G does not give you for free

`tests/golden_grids.rs` renders every identity at a **single fixed instant**,
`UNIX_EPOCH + 1_787_400_000 s` = **2026-08-22 12:00 UTC** — Chicago on CDT, London on BST, i.e. the
**aligned** state. A seasonal key's second profile therefore never appears in
`tests/golden/normal_week_grids.txt`, and a typo in the misaligned table would ship green. The
golden file is the crate's main defence against a silent table edit, and it is blind here by
construction. **This is exactly why §4 exists**, and why the paired assertions in §4 must be
handwritten rather than derived.

---

## 4. Minimal test set pinning the DST transition weeks for a two-zone shape

Written for `globex_energy_tam_london` (`CLL/BZL/HOL/RBL`, 17:00 `America/Chicago` →
16:30 `Europe/London`) as the worked example; the Asia-anchored and crypto shapes need the same set
with their own instants. New file
`tests/futures_family_boundaries/cme_trade_type_cross_zone.rs`, per the coverage plan's
*"tests in a submodule of `tests/futures_family_boundaries/`, never fattening the root"*.
Every assertion goes through the public surface (TEST-LAYOUT).

**T1 — aligned summer, both endpoints.** At an instant in the 2026-08-31 week
(`hours_for_market_hours_key(key, …)`): closed at 16:59:59 CT Sunday; open at 17:00:00 CT Sunday;
open at 10:29:59 CT Monday; **closed at 10:30:00 CT Monday** (end-exclusive).

**T2 — aligned winter.** The same four assertions in the 2026-12-07 week. Same Chicago clock values.
This is the assertion that proves the *aligned* state is genuinely offset-driven and not a summer
accident: US and UK are both on standard time, the delta is again 6 h, and the close is again 10:30.

**T3 — autumn misalignment (UK off DST, US still on).** The 2026-10-26 week: open at 11:29:59 CT
Monday, **closed at 11:30:00 CT Monday**, and `open@17:00 CT` **unchanged**. Assert the open
explicitly — the entire claim is that one endpoint moves and the other does not.

**T4 — spring misalignment (US on DST, UK not yet).** The 2027-03-15 week: identical to T3.
The spring window is the longer of the two (14 or 21 calendar days against the autumn window's
invariant 7) and is a different code path only in the sense that a naive "autumn-only"
implementation passes T3 and fails T4.

**T5 — the transition weekends themselves, date-aware.**
Using `calendar_for_market_hours_key(key)` (a fixed snapshot cannot cross a transition — see
`tests/seasonal_calendars/transition_scans.rs::resolved_snapshot_is_exact_at_its_instant_but_not_across_a_transition`):
Cover **all four** transition weekends — misalignment entry and exit in *both* spring and autumn —
not just the autumn pair. `tests/seasonal_calendars/international.rs::endex_calendar_scans_reselect_both_mismatch_entries_and_exits`
is the shipped template and uses exactly that four-case table; copy its shape.
- `next_session_after(Friday 2026-10-23 10:30 CT)` == `(Sunday 2026-10-25 17:00 CT, Monday
  2026-10-26 11:30 CT)` — **autumn entry**: the UK fell back on the Saturday evening (Chicago), and
  the state that changed over the weekend is the one the reopening session uses.
- `next_session_after(Friday 2026-10-30 11:30 CT)` == `(Sunday 2026-11-01 17:00 CT, Monday
  2026-11-02 10:30 CT)` — **autumn exit**: the US falls back that Sunday and the close returns
  to 10:30.
- `next_session_after(Friday 2027-03-12 10:30 CT)` == `(Sunday 2027-03-14 17:00 CT, Monday
  2027-03-15 11:30 CT)` — **spring entry**: the US springs forward that Sunday at 02:00 local.
- `next_session_after(Friday 2027-03-26 11:30 CT)` == `(Sunday 2027-03-28 17:00 CT, Monday
  2027-03-29 10:30 CT)` — **spring exit**: the UK springs forward on 2027-03-28 01:00 UTC =
  2027-03-27 19:00 CDT, the Saturday evening before the open.
- `session_bounds(Monday 2026-10-26 11:00 CT)` returns the containing session, not the next one:
  the session that opened Sunday is still running an hour past where the aligned grid would end.
  This is the assertion that would have caught the false-closed error of §1.5.

**T6 — no session ever spans an offset change (§1.6 i).** For each of the four transition Sundays in
2026 and 2027, assert `is_open(...) == false` at the transition instant itself
(US: 02:00 local Sunday; UK: 01:00 UTC Sunday). If a future edit or a tz-database change breaks
this, the two-state model stops being exact and the test says so.

**T7 — the two profiles differ only in the SSM.** Compare `hours_for_market_hours_key` at a T1
instant and a T3 instant: identical `tz`, identical rule counts, identical `days` masks, identical
`has_daily_close` / `has_weekend_close`, identical `wraps_to_next_day()` per rule; the **only**
difference is `close_ssm`, by exactly 3600. Also assert
`normal_week_open_seconds()` differs by exactly `3600 × <number of closing days>` — this pins the
golden file's blind spot (§3.6) with a handwritten expectation.

**T8 — trade date is stable across states.** `trade_date(Monday 10:00 CT)` in the T1 week and
`trade_date(Monday 11:00 CT)` in the T3 week both return the Monday. Guards the near-midnight wrap
risk. For the Tokyo-anchored shapes — the tightest margin at 00:30 CT — make this assertion on
*both* states explicitly rather than reusing the London instants.

**T9 — serde and identity.** The new key round-trips through its canonical `snake_case` name in
both directions and appears in `EXPECTED_MARKET_HOURS_KEY_NAMES` / `named_profiles.rs` /
`unsupported_market_hours_keys.rs`. Standard for any key; listed so it is not forgotten alongside
the interesting tests.

**T10 — mutation check, as the coverage plan requires.** Move the launch revision one day and
confirm failure; flip the aligned/misaligned branch and confirm T3 and T4 fail; change one
`close_ssm` by 60 s and confirm T1 fails. Say in the PR that you did it.

---

## 5. What this memo does not decide

- Whether `GCD` and `HGF` may be keyed at all — that is the `closed@`-as-session-language question
  in handoff §1.4, not a representation question.
- U-4, regular vs extended, for any of these shapes.
- The Pre-Open onsets (`16:50` for `GM`, `16:45` for `C1`, `16:45`/`16:00` elsewhere) and whether
  they are order-entry with a sourced day or a knowledge-bound row.
- Key granularity — three energy TAM keys vs one — which handoff §3.3 leaves to family semantics.
  Note only that Option G makes the three-key answer cheap: the three differ by one constant each.
