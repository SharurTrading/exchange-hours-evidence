# 1.0.0 release gate — maintainer acceptance under the raised bar

Refreshed 2026-10-05 UTC at main `a144b5b` (SharurTrading/exchange-hours-rs);
coverage walk executed 2026-10-05 after the convention wave merged
(#282 the 2027 horizon ruling, #284 the sourced-intersection residual
convention closing #79/#123/#259, #285 the #283 intersection). Supersedes
every earlier refresh: each number below is a fresh derivation at `a144b5b`.

The maintainer's bar: **all supported scopes complete — holidays AND market
hours — back to 2010 or earliest listing, and forward to 2026/2027/2028 where
operators have published — plus every open issue resolved** (closed as data,
proven externally blocked, or awaiting the maintainer's operator-evidence
thread). The maintainer signs this at the Stage 7 gate (RELEASING.md: "An
unresolved in-window gap blocks this gate"); each residual class below names
its closing condition and tracker.

## How these numbers were derived (probe method)

A temporary integration test (the reviewers' probe pattern; deleted after the
walk) resolved each of the 33 served scopes the verification ledger names
through the public constructors only — `calendar_for_exchange` /
`calendar_for_market_hours_key`, matched by canonical `as_str()` name over
`Exchange::ALL` and `MarketHoursKey::ALL`, filtered to the rows the ledger's
service-tier column marks **served** (132 identities ship; 99 are dormant and
refuse by contract — they are not the gate's subject) — and walked the
**public coverage surface only**: `coverage_on(date)` day by day over
**2010-01-01..2027-12-31** (6,574 venue-local dates per scope, 216,942
scope-days) plus a sub-walk over **2025-01-01..2027-12-31** (1,095 dates).
Two wire names are shared between an `Exchange` and a `MarketHoursKey`
(`eurex`, `sgx`); the ledger's tier selects which identity a name means here.
Per scope the probe counted the verdicts `Covered` / `OutsideCoveredRange` /
`UnresolvedGap`, bucketed every `gaps()` record by reason and declaring issue
(exact maximal spans), and asserted two invariants for every scope: the
verdict counts sum to the walk, and the `gaps()` spans partition exactly the
refused days — both held for all 33 scopes. A census walked `holiday_on(date)`
over 2009-01-01..2029-12-31 for the shipped-table row counts and the
`Unsourced` row counts the metadata reports. Raw output:
`gate-probe-2026-10-05-a144b5b.tsv` beside this file. No number below is
copied from any document; every count is this walk's output.

## Headline

- **Full supported domain, 2010-01-01..2027-12-31:** 178,784 of 216,942
  scope-days (82.4%) answer `Covered`; 38,158 refuse, and every refusal is
  the typed error contract (`OutsideCoveredRange` 37,633 + `UnresolvedGap`
  525), never an open/closed claim. Under the 2026-10-04 horizon ruling the
  required window is each operator's PUBLISHED horizon — the unpublished-2027
  class (≈2,900 of the refusals) is out of the requirement by the
  maintainer's ruling, taken when published on the weekly watch.
- **Gate window, 2025-01-01..2027-12-31:** 30,435 of 36,135 scope-days
  (84.2%) answer `Covered`; 5,700 refuse (≈2,900 of them the
  not-required unpublished-2027 class).
- Refusal mass by reason (2010-2027): outside audited holiday windows 29,725;
  declared phase gaps 8,147 (#79 5,126; #123 2,699; the #259 grains regime
  322); #157 unpublished-closure declarations 730 — the whole-domain
  declaration re-scoped to the tba era by #271; carried normal week
  5,968; resolution reach 1,109 (#151); `Unsourced` 525 verdicts — exactly
  1:1 with 525 shipped `Unsourced` rows.
- **The post-close trade-date label class (#152) is extinct** — 7,115 refused
  days at the 2026-10-02 refresh, 0 now: the charter's Post-Close trade-date
  convention (#266) resolved the divergence and retired both declarations,
  restoring 4,205 grains days and 2,910 livestock days to `Covered`.
- 2025+ refusal mass: windows 4,491; #79+#123 1,096; #157 730; resolution
  reach 319; withheld 154; carried 0 (extinct inside the gate window).
- 72.4% (2026-10-02) → 78.7% (2026-10-03 waves: #209/#221/#152/#271/#270)
  → **82.4%** (2026-10-04/05 convention wave: the #79/#123/#259 sourced-
  intersection retirements +8,043 days, the #283 intersection, and the
  horizon ruling reclassifying the unpublished-2027 class out of the
  requirement). **Twenty-five of 33 scopes read complete at their published
  horizons; eight carry named in-window gaps with live closers.**

## Per-identity coverage table (2010-01-01..2027-12-31 through the public surface)

All 33 served scopes in ledger order. "2025+" is the gate window
(covered/1,095). "carried" = below the identity's sourced normal-week horizon;
"windows" = outside every audited holiday window; "withheld" = `Unsourced`;
"edge" = the #151 resolution reach (answering the date completely needs a
neighbouring date the identity does not answer).

| identity | covered | refused | unres. | 2025+ | dominant refusals |
|---|---|---|---|---|---|
| nasdaq | 6,190 | 380 | 4 | 724 | windows 2027 (365); edge 11 (neighbours of the withheld dates + 2026-12-31); 4 withheld (2010-11-26, 2011-11-25, 2012-10-30, 2025-01-09) |
| nyse | 6,574 | 0 | 0 | 1,095 | complete 2010-2027 — the raised bar's first fully closed served scope |
| cme | 5,348 | 1,042 | 184 | 905 | #79 Sundays (734); withheld 184 (45 in 2025+); edge 308 |
| cbot | 5,924 | 448 | 202 | 955 | withheld 202 (58 in 2025+); edge 375; carried ≤2010-03-14 (73) |
| comex | 4,957 | 1,611 | 6 | 1,011 | carried ≤2012-05-10 (861); #79 (732); edge 12; withheld 6 |
| nymex | 4,957 | 1,611 | 6 | 1,011 | carried 861; #79 (732); edge 12; withheld 6 |
| cfe | 3,547 | 3,026 | 1 | 729 | windows 2010-01-01..2017-04-09 (2,656) + 2027 (365); withheld 1 (2017-07-03); edge 4 |
| coinbase_derivatives | 1,892 | 4,680 | 2 | 614 | pre-launch 2010-01-01..2021-06-27 (4,196) + #155 horizon 2026-09-08..2027-12-31 (480); withheld 2 (2022-11-24/25); edge 2 |
| eurex | 5,479 | 1,095 | 0 | 0 | the tba era (#157) 2025-01-01..2026-12-30 (730) + 2027 windows (365) — the 2014-2018 German-scope closures encode since #271 |
| iceus | 945 | 5,588 | 41 | 945 | windows ≤2024-12-31 (5,479); withheld 41 (2025+); edge 109 |
| asx | 5,218 | 1,356 | 0 | 1,094 | carried ≤2013-09-15 (1,354); edge 2 |
| nzx | 6,203 | 371 | 0 | 729 | windows 2027-01-05..2027-12-31 (361); carried ≤2010-01-04 (4); edge 6 — the 2016 span (#209) closed as data 2026-10-03 |
| tse | 6,573 | 1 | 0 | 1,094 | edge 2027-12-31 (the next session lies in unpublished 2028) |
| nse_india | 5,417 | 1,143 | 14 | 720 | windows 2012 + 2018 + 2027 (1,096); 14 Muhurat dates withheld; edge 33 |
| hkex | 6,573 | 1 | 0 | 1,094 | edge 2027-12-31 — the ten #208 eves and the 2011-03-02 carried era closed as data |
| sgx_securities | 2,917 | 3,657 | 0 | 728 | #213 gaps 2011-08-01..2013-12-31 (884) + 2020-01-02..2024-12-31 (1,826); 2027 (365); carried ≤2011-07-31 (577); edge 5 |
| sse | 5,840 | 734 | 0 | 729 | windows 2010 unrecovered (365) + 2027 (365); edge 4 |
| lse | 6,555 | 14 | 5 | 1,076 | withheld 5 (2025-04-18, 04-21, 05-05, 05-26, 08-25); edge 9 + the withheld dates' own 5 — the #218 capture eras closed as data |
| xetra | 6,573 | 1 | 0 | 1,094 | edge 2027-12-31 — but see the #200 three-instant call below |
| six | 5,841 | 733 | 0 | 1,094 | windows 2010-2011 (730, the #212 remainder) + 2027 (2); edge 1 — the 2018-2019 span closed as data by #270 |
| euronext_paris | 5,842 | 730 | 2 | 723 | carried ≤2010-12-23 (357); windows 2027 (365); 2 withheld (2026-12-24, 2026-12-31); edge 6 |
| borsa_istanbul | 5,414 | 1,160 | 0 | 729 | windows 2010-03-25..2012-03-01 (708, unaudited era) + 2027 (365); carried ≤2010-03-24 (83); edge 4 |
| tsx | 6,208 | 366 | 0 | 729 | windows 2027 (365; 2027 unpublished); edge 2026-12-31 — the 2011 span (#221) closed as data 2026-10-03 |
| tadawul | 2,553 | 4,021 | 0 | 1,094 | windows 2010-01-12..2020-12-31 (4,007, unaudited era); carried ≤2010-01-11 (11); edge 3 |
| b3 | 5,841 | 733 | 0 | 729 | windows 2010 unrecovered (365) + 2027 (365); edge 3 |
| globex_equity_index | 5,824 | 744 | 6 | 1,011 | #79 (732); edge 6; withheld 6 — carried era closed by #237 |
| globex_energy | 4,957 | 1,611 | 6 | 1,011 | carried ≤2012-05-10 (861); #79 (732); edge 12; withheld 6 |
| globex_grains | 6,164 | 406 | 4 | 1,094 | the #259 regime queues (322, 2012-05-20..2013-04-07); carried ≤2010-03-14 (73); withheld 4; edge 7 — the #152 label class retired by the charter decision |
| globex_fx | 4,964 | 1,604 | 6 | 1,011 | carried ≤2012-05-02 (853); #79 (732); edge 13; withheld 6 |
| globex_interest_rates | 5,827 | 743 | 4 | 1,011 | #79 (732); edge 7; withheld 4 — sourced from the 2010 floor |
| globex_livestock | 6,551 | 17 | 6 | 1,094 | withheld 6 (June 2019/2020 + 2023 closures); edge 11 — the #152 label class retired by the charter decision |
| globex_cryptocurrency | 581 | 5,987 | 6 | 581 | windows before the 2019-01-01 five-day era (3,281); #123 (2,699; 513 in 2025+); withheld 6; edge 1 |
| globex_nikkei_225_dollar | 6,492 | 62 | 20 | 1,090 | 20 withheld 2019-2024; edge 42 — the 2010-2011 unaudited era closed as data (#243) |

Every row's covered+refused sums to 6,574 and every 2025+ pair to 1,095
(asserted in-probe). Complete across the whole gate window: **nyse**.
Complete but for the 2027-12-31 walk-end edge (the operator's next annual
publication): **asx, tse, hkex, xetra, six, tadawul, globex_grains,
globex_livestock**. Near-complete: **globex_nikkei_225_dollar** 1,090 (20
withheld dates), **lse** 1,076 (5 withheld dates).

## What changed since the 2026-10-02 refresh (`dbe5115` → `c7482ac`)

Merged 2026-10-03 UTC: **#261** (nzx 2016 span — the operator's own
derivatives-site memorandum `NZX-DD-2015-11-20`, closes #209), **#262** (tsx
2011 Christmas span — the Mondo Visione verbatim mirror `TMX-REL-2011-12-12`,
closes #221), **#263** (#259's citation outcome — the regime gap's closing
condition re-cited from the closed #116 to the live #259), **#265** (the
`SessionState::Halt` state removed — the maintainer ruled halts out of scope;
same-trade-date gaps classify `Closed`; no coverage-verdict effect), **#266**
(the charter's Post-Close trade-date convention, closing #152 — the
`PostCloseQueueTradeDateLabel` declarations retired from grains and
livestock, the divergence resolved as decided policy pinned by new fences).

- **Effect on the walk**: covered 157,091→164,528 (+7,437); nzx
  5,954→6,203; tsx 6,120→6,208; globex_grains 1,966→6,164;
  globex_livestock 3,649→6,551. The #152 label class shrank 7,115→0;
  the windows class 30,780→30,455. 2025+ covered 27,876→29,348.
- **Counter-movements (honesty, not regression)**: the resolution-reach class
  1,107→1,113 (new edges at the re-joined windows); cme's refused cell
  1,226→1,042 and cbot's 650→448 purely from the stricter sum invariant this
  walk asserts (withheld verdicts counted once, in the `unres.` column).
- The maintainer's operator-evidence thread continues; the consolidated
  ask-list is `evidence-requests-2026-10.md` in this store. **Its TSX, LSE and
  NZX sections are now MOOT** — #221, #218 and #209 all closed as data
  2026-10-02/03 (see Findings 3).

## The waiver list under the raised bar

What remains is every class still refusing, with its tracker. The 12 open
issues classify as follows.

### (a) Retrieval-narrowed gaps awaiting the operator-evidence thread

| issue | scope(s) | remaining span (this walk) | closing condition |
|---|---|---|---|
| #213 | sgx_securities | 2,710 dates (2011-08-01..2013-12-31 + 2020-01-02..2024-12-31) | surviving SGX securities calendar captures or annual notices (ask-list §4) |
| #212 | six | 730 dates (2010-2011 only — the 2018-2019 half closed as data by #270) | a captured copy of the operator's Trading Calendar for 2010 or 2011 — the per-year PDF or a guide edition reprinting the year's grid |
| #79 | cme, comex, nymex, globex_equity_index, globex_energy, globex_fx, globex_interest_rates | 5,126 refused Sundays (734 cme + 732 each; 583 in 2025+) | a written CME desk reply or an ordinary-week artifact inside the 2012 bracket (ask-list §6; the desk route is the sanctioned one — cmegroup.com is blocked to automated access) |

### (b) Operator-condition issues (the operator has not published / not dated)

| issue | scope(s) | remaining span (this walk) | closing condition |
|---|---|---|---|
| #157 | eurex | 730 dates — the declaration re-scoped to the tba era (2025-01-01..2026-12-30) by #271; the 2014-2018 closures answer | an Eurex edition dating the German equity / equity-index closures for 2025-2026; a 2027 edition would also extend the window bound |
| #155 | coinbase_derivatives | 480 dates (2026-09-08..2027-12-31) | the operator's next quarterly publication |
| #123 | globex_cryptocurrency | 2,699 dates (2019-01-01..2026-05-28 era; 513 in 2025+) | a CME artifact stating the era's Pre-Open in session language on a day-level effective date |
| #259 | globex_grains | 322 dates (2012-05-20..2013-04-06 regime queues) | a CME document stating those queue times in session language on a day-level effective date — this issue is the gap's live closing condition (re-cited by #263, reopened 2026-10-03 after being closed with the citation fix by mistake) |
| #112 | coinbase_derivatives | 2 withheld dates (2022-11-24/25 — notice 22-10 unreachable); notice 24-12's IN DRAFT heading is a provenance disclosure, not a refusal | a recovered 22-10 PDF / non-draft 24-12 copy |
| #200 | xetra | no refusal — three 2027 instants (2027-05-06, 05-17, 05-27) answer `Covered` where the operator may close at 20:00 | the operator's next per-year page edition or `Trading calendar 2027` PDF (re-checked monthly per LAW-WATCH) |
| #162 | globex_nikkei_225_dollar | no refusal — five 2025 merged trade dates answer from the shared CME grid without an NKD/NIY-specific witness | an NKD/NIY-specific row from CME's trading-hours service (not yet in the ask-list) |
| — | cme, cbot, and the small family markers | withheld rows: cme 184, cbot 202, nikkei 20, iceus 41, nse_india 14, nasdaq 4, comex/nymex/energy/eqidx/fx/crypto/livestock 4-6 each, lse 5, paris 2, cfe 1, coinbase 2 — 525 total (154 in 2025+) | each family's own per-holiday sheet or the trading-hours service; #223's 2026-09-29 bounded search closed negative on every channel, so these await operator publication |
| — | cfe, sse, b3, borsa_istanbul, sgx_securities, tsx, eurex, nzx (+ each scope's walk-end day) | unpublished 2027: 365 dates each (nzx 361, eurex 365); the 2027-12-31 walk-end edge (tse, hkex, xetra) | each operator's next annual publication; LAW-WATCH cadence per ledger row |
| — | sse, b3 | 365 dates each (2010 unrecovered first years) | a surviving artifact for the venue's 2010 grid |
| — | asx 1,354; comex/nymex/globex_energy 861 each; globex_fx 853; sgx_securities 577; euronext_paris 357; borsa_istanbul 83; cbot 73; tadawul 11; nzx 4 | 5,968 scope-days of carried normal week below the sourced horizon — 0 inside the 2025+ window | dated operator baselines where the archive allows; otherwise acceptance that the served window opens at the sourced horizon (recorded per ledger row) |

### (c) Plan trackers (close at the release, not before it)

| issue | what it is | closing condition |
|---|---|---|
| #118 | Stage 6: migrate SharurPlatform to complete scoped calendars | the consumer repin to the tagged 1.0.0 release |
| #119 | Stage 7: verify and release | the release itself — this gate |

### (d) Tracked refactors

None open.

## Findings this walk surfaced

1. **#259 was closed with its citation fix and had to be reopened.** The
   2026-10-02 refresh's required outcome 2 made #259 the regime gap's LIVE
   closing condition; closing it with #263 (which landed the re-citation)
   recreated the exact defect the issue described. Reopened 2026-10-03 UTC
   with the explanation on the issue; the walk fence and this document keep
   naming it until the data lands.
2. **The `Unsourced` verdict/row census remains exactly 1:1 (525 = 525)** —
   no withheld row sits below a carried horizon.
3. **The ask-list's TSX, LSE and NZX sections are moot.** #221, #218 and #209
   all closed as data on 2026-10-02/03 — the thread's asks for those spans
   are answered; only the SGX (§4), SIX (§3) and CME desk (§6) asks remain
   live, plus #112's Coinbase notices. Narrowing `evidence-requests-2026-10.md`
   before the thread's next pass would make it cheaper.
4. **Carried normal weeks remain on four CME family scopes** — comex, nymex,
   globex_energy (861 each) and globex_fx (853) — 3,436 of the 5,968 carried
   scope-days, the largest single data class left against the bar's "back to
   2010" clause. #237's Globex-notice method is the pattern that closed the
   other three families.
5. **cme retains the largest withheld mass (184 rows, 45 in 2025+)** — the
   routed-family intersection disputes the venue-clock re-derivation left
   standing. Its closing condition (the families' own per-holiday sheets /
   the trading-hours service) is the same CME channel the ask-list §6 desk
   reply already names.

## The resolution-edge fix (#151/#244) — metadata and queries now agree

The engine change this gate depends on most: a `Covered` date's **resolution
reach** — the neighbouring dates every question about its instants consults
(the previous session day whose wrapped leg a midnight lands in, the next
session day, its trade date) — must itself answer. Before #244, metadata
called a date `Covered` while a query on it could refuse naming an
unanswerable neighbour; the fix refuses such dates as
`CoverageGapReason::ResolutionEdge` and guarantees the inverse: **every
refusal a query on a `Covered` date can still raise names a date the
vocabulary already flags** (fenced by `tests/coverage_metadata.rs`). 1,113
dates across the walk refuse on this ground (319 in 2025+), including each
scope's final walk day where the next session's trade date lies in unpublished
2028 — which is why `tse`, `hkex` and `xetra` read 6,573 rather than 6,574.

## The crate never reports a false closure

Every unverified date in the walk refuses with a typed `CalendarQueryError` —
`BeforeSupportFloor`, `OutsideCoveredRange` or `UnresolvedGap`, 1:1 with the
verdicts counted here — and a bounded search that needs an unknown date
refuses with `SearchExhausted` rather than skipping past it. Absence, known
closures and missing evidence remain distinct in `gaps()`: the known closures
(launch days, holidays) answer normally while every class above refuses. A
date without sourced evidence can surface as closed, absent or unknown, never
as open. The one recorded exception in direction — xetra's three 2027
instants, where the crate may under-report a 20:00 extended tail as a 17:30
close — is an instant-level residual risk the evidence file carries with a
closing condition (#200), and the maintainer is asked to accept it expressly
(class b above).

## Acceptance

The maintainer accepts 1.0.0 with the classes in (a) and (b) above
withheld-by-contract — each documented in its issue and evidence file with
its closing condition, the no-surviving-artifact ones awaiting the
operator-evidence thread — none hidden by an outer window, an overlay, or a
broad venue intersection substituting for a complete family calendar; (c)
closes at the release itself. Under the raised bar the classes are not
"accepted as incomplete forever": each has a named closer, and the LAW-WATCH
cadence re-opens each scope as its operator publishes.
