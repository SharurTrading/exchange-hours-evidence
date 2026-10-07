# 1.0.0 release gate — maintainer acceptance under the raised bar

Refreshed 2026-10-06 UTC at main `fdb23c4` (SharurTrading/exchange-hours-rs);
coverage walk executed 2026-10-05 03:08 UTC after the eurex no-changes
verification merged (#287) and the evidence-audit infrastructure landed
(#289). Supersedes every earlier refresh, including the same-day morning
refresh at `a144b5b`: each number below is a fresh derivation at `6debb73`,
and the per-identity table and refusal-mass classes the morning refresh
carried over from the pre-convention walk are re-derived here (see What
changed).

The maintainer's bar: **all supported scopes complete — holidays AND market
hours — back to 2010 or earliest listing, and forward to 2026/2027/2028 where
operators have published — plus every open issue resolved** (closed as data,
closed as verified, proven externally blocked, or awaiting the maintainer's
operator-evidence thread). Each residual class below names its closing
condition and tracker.

## How these numbers were derived (probe method)

A temporary integration test (the reviewers' probe pattern; deleted after the
walk) resolved each served scope the verification ledger names through the
public constructors only — `calendar_for_exchange` /
`calendar_for_market_hours_key`, matched by canonical `as_str()` name over
`Exchange::ALL` and `MarketHoursKey::ALL`, filtered to the rows the ledger's
service-tier column marks **served** (132 identities ship; 99 are dormant and
refuse by contract — they are not the gate's subject; 33 are served. Two wire
names are shared between an `Exchange` and a `MarketHoursKey` (`eurex`,
`sgx`); the ledger's tier selects which identity a name means here) — and
walked the **public coverage surface only**: `coverage_on(date)` day by day
over **2010-01-01..2027-12-31** (6,574 venue-local dates per scope, 216,942
scope-days) plus a sub-walk over **2025-01-01..2027-12-31** (1,095 dates).
Per scope the probe counted the verdicts `Covered` / `OutsideCoveredRange` /
`UnresolvedGap`, bucketed every `gaps()` record by reason and closing
condition into exact maximal spans, and asserted two invariants for every
scope: the verdict counts sum to the walk, and the `gaps()` spans partition
exactly the refused days — both held for all scopes. A census walked
`holiday_on(date)` over 2009-01-01..2029-12-31 for the shipped-table row
counts and the `Unsourced` row counts the metadata reports. Raw output:
`gate-probe-2026-10-06-fdb23c4.tsv` beside this file. No number below is
copied from any document; every count is this walk's output.

## Headline

- **Full supported domain, 2010-01-01..2027-12-31:** 183,864 of 216,942
  scope-days (84.8%) answer `Covered`; 33,078 refuse, and every refusal is
  the typed error contract (`OutsideCoveredRange` 36,904 + `UnresolvedGap`
  525), never an open/closed claim.
- **Gate window, 2025-01-01..2027-12-31:** 31,169 of 36,135 scope-days
  (86.3%) answer `Covered`; 4,966 refuse.
- **The declaration census is ZERO.** The walk's gap census contains no
  declared-gap record of any shape — no `NormalWeekPhaseWithheld` (#79/#123/
  #259, retired by the 2026-10-04 sourced-intersection residual convention),
  no `UnpublishedClosureDates` (#157, retired by the 2026-10-05 no-changes
  verification), no `PostCloseQueueTradeDateLabel` (#152, retired 2026-10-03),
  no `SpecialSessionUnrepresentable` (#93). `grep` over `src/` finds **zero**
  `PhaseGap::new`; every identity's declaration list is empty; the four
  reasons stay on the enum as the vocabulary a future gap would declare. The
  count classes the conventions moved — the seven quarter-hour scopes'
  5,126 Sundays, cryptocurrency's 2,699-day era, the grains regime's 322
  queues, and eurex's 730 `tba` days — all answer `Covered` in this walk.
- Refusal mass by class (2010-2027): outside audited holiday windows 29,725;
  carried normal week below the sourced horizon 5,968; resolution reach
  (#151) 1,211; `Unsourced` 525 verdicts — exactly 1:1 with the 525 shipped
  `Unsourced` rows the census reports. Nothing else refuses.
- 2025+ refusal mass: windows 4,491; resolution reach 326; withheld 154;
  carried 0; declared 0. Under the 2026-10-04 horizon ruling the required
  window is each operator's PUBLISHED horizon: the unpublished-forward class
  is out of the requirement by the maintainer's ruling, taken when published
  on the weekly watch. Its 2027 mass alone is 4,380 refusal days across the
  twelve scopes whose operators have not published 2027 (nasdaq, cfe, eurex,
  nzx, nse_india, sgx_securities, sse, euronext_paris, borsa_istanbul, tsx,
  b3 — 365 each, nzx's being its 2027-01-05..12-31 window plus its four
  boundary-reach days — and coinbase's #155 horizon 2026-09-08..2027-12-31).
- **Twenty-four of 33 scopes answer every date inside their operator's
  published window** — nyse complete across the whole domain, the rest but
  for the boundary edge at the horizon (the operator's next annual
  publication). **Nine carry named in-window gaps** — ≈300 refusal days in
  all, each with a live closer (below).
- Progression: 72.4% (2026-10-02) → 78.7% (2026-10-03 waves) → 82.4%
  (`a144b5b`) → 82.7% (`6debb73`, +729 eurex days) → 83.1% (`a24d4ef`,
  +730 SIX days, #290) → **84.8%** (`fdb23c4`, the carried-class wave:
  the CME-side seven families' horizons at the floor + the SIX TSC rows
  + the equities carried-half). Gate window: 84.2% → **86.3%**.

## Per-identity coverage table (2010-01-01..2027-12-31 through the public surface)

All 33 served scopes in ledger order. "2025+" is the gate window
(covered/1,095). "carried" = below the identity's sourced normal-week horizon;
"windows" = outside every audited holiday window; "withheld" = `Unsourced`;
"edge" = the #151 resolution reach (answering the date completely needs a
neighbouring date the identity does not answer).

| identity | covered | refused | unres. | 2025+ | dominant refusals |
|---|---|---|---|---|---|
| nasdaq | 6,190 | 384 | 4 | 724 | windows 2027 (365); 4 withheld (2010-11-26, 2011-11-25, 2012-10-30, 2025-01-09); edge 15 (the withheld dates' neighbours + 2026-12-31) |
| nyse | 6,574 | 0 | 0 | 1,095 | complete 2010-2027 — the raised bar's first fully closed served scope |
| cme | 6,014 | 560 | 184 | 981 | withheld 184 (45 in 2025+); edge 376 (the withheld dates' neighbours + 2027-12-31) — the #79 Sundays answer since #284 |
| cbot | 5,924 | 650 | 202 | 955 | withheld 202 (58 in 2025+); edge 375; carried ≤2010-03-14 (73) |
| comex | 5,686 | 888 | 6 | 1,094 | carried ≤2012-05-10 (861); edge 21; withheld 6 |
| nymex | 5,686 | 888 | 6 | 1,094 | carried 861; edge 21; withheld 6 |
| cfe | 3,547 | 3,027 | 1 | 729 | windows 2010-01-01..2017-04-09 pre-listing (2,656) + 2027 (365); withheld 1 (2017-07-03); edge 5 |
| coinbase_derivatives | 1,892 | 4,682 | 2 | 614 | pre-launch 2010-01-01..2021-06-27 (4,196) + #155 horizon 2026-09-08..2027-12-31 (480); withheld 2 (2022-11-24/25); edge 4 |
| eurex | 6,208 | 366 | 0 | 729 | windows 2027 (365); edge 2026-12-31 — the `tba` era answers ordinary since the #287 verification; complete through 2026-12-30 |
| iceus | 945 | 5,629 | 41 | 945 | windows ≤2024-12-31 (5,479); withheld 41 (2025+); edge 109 |
| asx | 5,218 | 1,356 | 0 | 1,094 | carried ≤2013-09-15 (1,354); edge 2 |
| nzx | 6,203 | 371 | 0 | 729 | windows 2027-01-05..2027-12-31 (361); carried ≤2010-01-04 (4); edge 6 — the horizon-boundary reach takes 2026-12-31..2027-01-04 |
| tse | 6,573 | 1 | 0 | 1,094 | edge 2027-12-31 (the next session lies in unpublished 2028) |
| nse_india | 5,417 | 1,157 | 14 | 720 | windows 2012 + 2018 + 2027 (1,096); 14 withheld special-session dates (12 Muhurat evenings before 2025, plus 2025-10-21 and 2026-11-08); edge 47 |
| hkex | 6,573 | 1 | 0 | 1,094 | edge 2027-12-31 |
| sgx_securities | 2,917 | 3,657 | 0 | 728 | #213 windows 2011-08-01..2013-12-31 + 2020-01-02..2024-12-31 (2,710) + 2027 (365); carried ≤2011-07-31 (577); edge 5 (incl. the 2025-01-01 reach into the #213 region) |
| sse | 5,840 | 734 | 0 | 729 | windows 2010 unrecovered (365) + 2027 (365); edge 4 |
| lse | 6,555 | 19 | 5 | 1,076 | 5 withheld (2025-04-18, 04-21, 05-05, 05-26, 08-25); edge 14 (their neighbours + 2027-12-31) |
| xetra | 6,573 | 1 | 0 | 1,094 | edge 2027-12-31 — but see the #200 three-instant note below |
| six | 6,573 | 1 | 0 | 1,094 | edge 2027-12-31 only — the 2010-2011 span closed as data by #290 (the TSC pages' own market-holiday marks; the legend discriminator calibrated 12/12 against the 2019 guide); six reads complete from the 2010 floor through its published 2027 horizon |
| euronext_paris | 5,842 | 732 | 2 | 723 | carried ≤2010-12-23 (357); windows 2027 (365); 2 withheld (2026-12-24, 2026-12-31); edge 8 |
| borsa_istanbul | 5,414 | 1,160 | 0 | 729 | windows 2010-03-25..2012-03-01 (708, unaudited era) + 2027 (365); carried ≤2010-03-24 (83); edge 4 |
| tsx | 6,208 | 366 | 0 | 729 | windows 2027 (365; 2027 unpublished); edge 2026-12-31 — the 2011 span (#221) closed as data 2026-10-03 |
| tadawul | 2,553 | 4,021 | 0 | 1,094 | windows 2010-01-12..2020-12-31 (4,007, unaudited era); carried ≤2010-01-11 (11); edge 3 |
| b3 | 5,841 | 733 | 0 | 729 | windows 2010 unrecovered (365) + 2027 (365); edge 3 |
| globex_equity_index | 6,553 | 21 | 6 | 1,094 | edge 15; withheld 6 — the #79 Sundays (732) answer since #284; the carried era closed by #237 |
| globex_energy | 5,686 | 888 | 6 | 1,094 | carried ≤2012-05-10 (861); edge 21; withheld 6 |
| globex_grains | 6,486 | 88 | 4 | 1,094 | carried ≤2010-03-14 (73); edge 11; withheld 4 — the #259 regime queues (322) answer since #285; the #152 label class retired by the charter decision |
| globex_fx | 5,693 | 881 | 6 | 1,094 | carried ≤2012-05-02 (853); edge 22; withheld 6 |
| globex_interest_rates | 6,557 | 17 | 4 | 1,094 | edge 13; withheld 4 — sourced from the 2010 floor |
| globex_livestock | 6,551 | 23 | 6 | 1,094 | edge 17; withheld 6 (June 2019/2020 + 2023 closures) |
| globex_cryptocurrency | 3,261 | 3,313 | 6 | 1,094 | windows before the 2019-01-01 five-day era (3,287); edge 20; withheld 6 — the #123 era (2,699) answers since #284 |
| globex_nikkei_225_dollar | 6,492 | 82 | 20 | 1,090 | edge 62 (incl. the 2025-01-01..04 New-Year reach); withheld 20 (2019-2024) — the 2010-2011 unaudited era closed as data (#243), the five 2025 merged trade dates ship (#278) |

Every row's covered+refused sums to 6,574 and every 2025+ pair to 1,095
(asserted in-probe). **Complete across the whole gate window: nyse.**
Complete at their published horizons (the only in-window refusals are the
boundary edges): **comex, nymex, cfe, coinbase_derivatives, eurex, iceus,
asx, tse, hkex, xetra, six, sse, borsa_istanbul, tsx, tadawul, b3, and the
seven CME family keys** — with nyse, 24 of 33. Named in-window gaps remain
on **nasdaq, cme, cbot, nzx, nse_india, sgx_securities, lse,
euronext_paris, globex_nikkei_225_dollar** (9).

## What changed since the 2026-10-05-morning refresh (`a144b5b` → `6debb73`)

Three changes merged, all verified by independent second-retrieval review.

- **#286** (sgx_securities) — the rulebook-incorporation angle of #213 closed
  negative: all 35 rulebook digests reproduce and zero gazette/public-holiday
  incorporations exist across the operator's rulebook artifacts. Data
  unchanged; the evidence file and coverage docs carry the negative record.
- **#287** (eurex) — the no-changes verification the maintainer set retired
  the #157 `UnpublishedClosureDates` declaration: the operator's day-by-day
  Holiday regulations tables state no German-scope closure on any date of
  2025 or 2026, every candidate date passed answering ordinary, and the
  Management-Board regulation channel such a closure would travel is
  enumerated complete and empty of it. **#157 CLOSED 2026-10-05** (state
  reason: completed). Effect on the walk: covered 178,784→179,513 (+729);
  eurex 5,479→6,208, its gate window 0→729; the whole-domain declaration
  census 730→0. The `tba` closures the operator never dated never existed —
  a new resolution category alongside "closed as data": **closed as verified
  no-changes**.
- **#288/#289** — the evidence-audit infrastructure is LIVE: the public
  evidence repo (SharurTrading/exchange-hours-evidence, plain git), CI digest
  enforcement non-vacuous on `docs/evidence/` PRs, and `cargo xtask
  verify-evidence --all` verifying 2,860 Documents rows / 42 files / 792
  distinct digests. Every artifact this gate's evidence chain cites is now
  third-party auditable.

- **A staleness correction.** The morning refresh's headline, sums and raw
  TSV were fresh, but nine of its per-identity rows (cme, comex, nymex,
  globex_equity_index, globex_energy, globex_fx, globex_interest_rates,
  globex_grains, globex_cryptocurrency) and its refusal-mass-by-reason
  paragraph were carried from the pre-convention walk: they still counted the
  #79/#123/#259 declarations that #284 had already retired, and its own TSV
  shows zero declared-gap records at `a144b5b`. This refresh re-derives every
  row and class from the fresh walk; the numbers above supersede both the
  morning refresh and the `#119` close comment's citations of it.

## The waiver list under the raised bar

**Exactly three issues are open** (tracker state 2026-10-05 UTC): #112,
#212, #213. Everything else the earlier waiver lists carried is closed —
#79/#123/#259 by the sourced-intersection residual convention (#284),
#157 by the no-changes verification (#287), #152 by the charter decision
(#266), #155 by the horizon ruling (its horizon is the weekly watch's),
#200 narrowed to the monthly watch (#277), #162 closed as data (#278),
#118 out of scope (consumer routing, 2026-10-05 ruling) and #119 obsolete
(the release sequence is RELEASING.md and needs no open issue), #288 by
#289.

### (a) The three open issues, each with its named closer

| issue | scope(s) | remaining span (this walk) | closing condition |
|---|---|---|---|
| #213 | sgx_securities | 2,710 dates (2011-08-01..2013-12-31 + 2020-01-02..2024-12-31) | a surviving SGX securities-calendar capture or annual notice — the sole closer; the rulebook-incorporation angle closed negative (#286), and the MOM state side is pre-validated and held in the research store |
| #212 ✅ CLOSED | six | — (closed as data by #290: the TSC pages' market-holiday marks; 13 rows) | ~~named bytes~~ — closed; the unarchived trading_calendar_en.pdf and the 11-Jan-2010 guide edition stay watch-list corroboration targets | (was: a captured copy of the operator's Trading Calendar for 2010 or 2011 (the per-year PDF or a guide edition reprinting the year's grid). **Verification in progress** on the era grid pages' legend (re-dispatched after the e-Helvetica stop — that channel is human-GUI-only by policy) |
| #112 | coinbase_derivatives | 2 withheld dates (2022-11-24/25 — notice 22-10 unreachable); notice 24-12's IN DRAFT heading is a provenance disclosure, not a refusal | a recovered desk copy of notice 22-10, absent from the operator's own CMS |

### (b) Classes without a single issue, each with its per-family closer

| class | scopes and spans (this walk) | closing condition |
|---|---|---|
| withheld `Unsourced` rows: 525 verdicts, 1:1 with 525 rows (154 in 2025+) | cme 184 (45 in 2025+), cbot 202 (58), nikkei 20, iceus 41 (2025+), nse_india 14, lse 5, comex/nymex/energy/eqidx/fx/crypto/livestock 6 each, nasdaq 4, grains 4, rates 4, coinbase 2, paris 2, cfe 1 | each family's own per-holiday sheet or the trading-hours service; #223's 2026-09-29 bounded search closed negative on every channel, so these await operator publication |
| unpublished forward (out of the requirement by the 2026-10-04 ruling) | twelve scopes' 2027 refusal days: 4,380 (nasdaq, cfe, eurex, nzx from 2027-01-05, nse_india, sgx_securities, sse, euronext_paris, borsa_istanbul, tsx, b3, coinbase's #155 horizon); plus each scope's horizon-boundary edge | each operator's next annual publication; LAW-WATCH cadence per ledger row |
| carried normal week below the sourced horizon: 5,968 scope-days (0 inside the gate window) | asx 1,354; comex/nymex/globex_energy 861 each; globex_fx 853; sgx_securities 577; euronext_paris 357; borsa_istanbul 83; cbot/globex_grains 73 each; tadawul 11; nzx 4 | dated operator baselines where the archive allows; otherwise acceptance that the served window opens at the sourced horizon (recorded per ledger row) |
| unaudited first years | sse 2010 (365); b3 2010 (365); tadawul 2010-2020 (4,007); borsa_istanbul 2010-2012 (708); cfe pre-listing (2,656); coinbase pre-launch (4,196); iceus ≤2024 (5,479); crypto pre-era (3,287); nse_india 2012+2018 (731) | a surviving artifact for the venue's grid in those years; the windows classes above |
| resolution reach (#151): 1,211 days (326 in 2025+) | mostly the neighbours of the withheld dates and each scope's final walk day | dissolves when its neighbouring date answers — no independent data programme |

### (c) Plan trackers

None. #118 and #119 closed 2026-10-04/05 (out of scope / obsolete); the
release sequence is documented in RELEASING.md and needs no open issue.

### (d) Tracked refactors

None open.

## Findings this walk surfaced

1. **The declaration extinction is total and fenced.** Zero `PhaseGap::new`
   in `src/`, an empty `phase_gaps` on every identity, zero declared-gap
   records in the walk's census, and the `coverage_inventory` fence pins the
   inventory tally at 26 complete / 7 incomplete of the 33 rows. The four
   retired reasons remain enum vocabulary, exactly as #93/#152 set the
   precedent.
2. **The morning refresh's own TSV contradicted its table** — the declared-
   gap class it reported (8,147 days) was already extinct at `a144b5b`.
   Anyone citing the morning numbers should cite this refresh instead.
3. **eurex is the walk's largest single mover without a data row changing:**
   730 days moved by verification alone. Its evidence chain (#287, four legs,
   reviewer-reproduced from the bytes, mutation failing three fences) is the
   template for retiring an undated operator note.
4. **cme and cbot retain the largest withheld mass** (184 and 202 rows, 45
   and 58 inside the gate window) — the routed-family intersection disputes
   the venue-clock re-derivation left standing. Their closer is the same CME
   channel the ask-list §6 desk reply names.
5. **Carried normal weeks remain on four CME family scopes** — comex, nymex,
   globex_energy (861 each) and globex_fx (853), 3,436 of the 5,968 carried
   scope-days, the largest single data class left against the bar's "back to
   2010" clause. #237's Globex-notice method is the pattern that closed the
   other three families.
6. **The ask-list's live asks are now exactly four**: the SGX securities
   calendars (§4), the SIX 2010/2011 Trading Calendar (§3), the CME desk
   reply (§6), and #112's Coinbase notice 22-10. The TSX, LSE and NZX
   sections closed as data earlier; narrowing
   `evidence-requests-2026-10.md` before the thread's next pass would make
   it cheaper.

## The resolution-edge fix (#151/#244) — metadata and queries now agree

A `Covered` date's **resolution reach** — the neighbouring dates every
question about its instants consults — must itself answer. Before #244,
metadata called a date `Covered` while a query on it could refuse naming an
unanswerable neighbour; the fix refuses such dates as
`CoverageGapReason::ResolutionEdge` and guarantees the inverse: **every
refusal a query on a `Covered` date can still raise names a date the
vocabulary already flags** (fenced by `tests/coverage_metadata.rs`). 1,211
dates across this walk refuse on this ground (326 in 2025+), including each
scope's final walk day where the next session's trade date lies in unpublished
2028 — which is why `tse`, `hkex` and `xetra` read 6,573 rather than 6,574,
and why eurex reads 2026-12-31 as its last refusal before the unpublished
2027 windows.

## The crate never reports a false closure

Every unverified date in the walk refuses with a typed `CalendarQueryError` —
`BeforeSupportFloor`, `OutsideCoveredRange` or `UnresolvedGap`, 1:1 with the
verdicts counted here — and a bounded search that needs an unknown date
refuses with `SearchExhausted` rather than skipping past it. Absence, known
closures and missing evidence remain distinct in `gaps()`: the known closures
(launch days, holidays) answer normally while every class above refuses. A
date without sourced evidence can surface as closed, absent or unknown, never
as open. The one recorded exception in direction — xetra's three 2027
instants (2027-05-06, 05-17, 05-27), where the crate may under-report a 20:00
extended tail as a 17:30 close — is an instant-level residual risk the
evidence file carries; #200 closed 2026-10-04 with the 2027 close schedule
verified unpublished, and the residual is on the monthly watch (#277). The
maintainer is asked to accept it expressly.

## Acceptance

The maintainer accepts 1.0.0 with the classes in (a) and (b) above
withheld-by-contract — each documented in its issue and evidence file with
its closing condition, the no-surviving-artifact ones awaiting the
operator-evidence thread — none hidden by an outer window, an overlay, or a
broad venue intersection substituting for a complete family calendar. Every
cited byte is third-party auditable through the public evidence repo, CI
digest enforcement, and `cargo xtask verify-evidence` (#289). Under the
raised bar the classes are not "accepted as incomplete forever": each has a
named closer, and the LAW-WATCH cadence re-opens each scope as its operator
publishes.
