# Independent source review of OANDA correction PR #334

Reviewed on 2026-10-11 UTC. Head: `e04163cd8c6993d1c0ddba6dc9d61e742317efb1`;
base: `e17d5b88963548e7d1b747abb1773a4f4a712483`. Verdict: **reject pending corrections**.
This reviewer did not write the correction. No approval of a later head is implied.

## Method and scope

A detached checkout at the exact head was used. Every changed file was classified:
six source-data files (one normal-week module and five holiday tables), eight
narrative evidence files, five public records/watch files, seven API/registration/
query-engine files and seven tests/golden fixtures. No charter or plan changed.
The two official UK pages were independently fetched by HTTPS; the 437 normalized
holiday heading/list events match the cited capture. The supplied PDF was extracted
with Poppler and the index/footnote layout inspected. The undated static operator
PDF was separately fetched; its SHA256 reproduces the cited digest. Its page 2 was
rendered and visually inspected, including the explicit US DST Australia 200 row.

The five changed holiday tables contain **142** rows: index 29, Treasury 30,
commodity 27, spot metals 32 and Brent 24. Every row's date, kind, instant, tier,
source group and event-date to trade-date conversion was compared with the cited
operator HTML. Replacement opens were checked against the previous dated event;
normal closes and Brent late blocks were checked against the independent ordinary
grid. ET/London conversions were recomputed using the five-hour offset on each
actual exception date. All rows cite the operator's own document, T1. No dated
cutover was added from an undated guide or a capture time.

Python independently counted ledger cells and macro tuples (saved JSON): 141
identities = 97 Exchanges + 44 keys; 74 Primary, 65 Partial (36 order-entry and
29 executable), two synthetic; 36 served and 105 dormant; 50 holiday-bearing.
The existing table/README fences derive the same identity counts. OANDA data
counts in the ledger do not: the incorrect index 28 / Treasury 29 counts must change.

The US Treasury registration, normal profile alias and holiday routing were read
independently; only the normal-week profile is shared. The isolated private
consumer map was read without modification and maps USB02Y/USD, USB05Y/USD,
USB10Y/USD and USB30Y/USD to the new Treasury key. This review does not certify
all private consumer scopes or its tested patch's integration.

## Blocking findings

1. `src/calendar/schedules/holidays/oanda_us_bond_cfd.rs:61,63`: 2025-07-03
   closes Treasury CFDs at 13:15 and reopens them at 18:00 for Jul 4. The UK
   source's Jul 3 section names only US index futures. Its Jul 4 section explicitly
   closes bonds at 13:00. The copied index-only exception has no bond evidence.
2. `docs/evidence/oanda_us_index_cfd.md:90` and the bond counterpart: a claim
   that normal 18:01 remains the common sourced interval for Memorial Day 2026
   is unsupported. The UK source prints the incomplete token `18:0`; its missing
   digit might place the reopen after 18:01. The following 2026-05-26 trade date
   needs a typed withholding absent a same-scope operator correction. Preserve
   May 25's sourced 12:59 close. Other OANDA legal entities do not establish UK hours.
3. `docs/evidence/oanda_fx.md:49-50`: the 16:59–17:05 break is described as a
   same-trade-date Closed gap. Adjacent daily sessions have different trade dates;
   the engine classifies their six-minute gap Maintenance under the charter's
   policy. The published break is sourced; the wrong state claim must change.
4. `docs/evidence/oanda_us_commodity_cfd.md:49-50`: Christmas Eve 2025 is said
   to print an 18:04 reopen. The UK artifact prints a 13:44 close. The 18:04
   statement belongs to New Year's Day 2025 alone.
5. `docs/evidence/oanda_metals.md:81,88`: closed-date cells quote Forex 17:05
   as the printed basis for metals. The artifact has separate Metals 18:01 rows.
   Runtime closures/reopens are consistent with the actual metals statement;
   the source cells must cite that statement instead.
6. `docs/evidence/oanda_metals.md:16-18`: the universal one-minute-inside-
   futures hedge rationale is not established for the newly preserved 2025
   13:00/14:30 exceptions. Remove it or qualify against explicit sourced facts.
7. `docs/schedules/verification.md` index and Treasury basis counts are 28/29,
   while exact-head modules have 29/30 rows. The initially repeated review total
   was corrected after Python counted the actual macro tuples; the amended PR
   review records this correction. Source/data prose counts are merge blockers.

Findings 1, 2 and 5 have inline PR comments; the remaining findings are in the
outside-diff review summary. The cited holiday artifact is
`holidays/raw/oanda-uk-holiday-hours-2026-10-10/oanda-uk-holiday-trading-hours.html`,
SHA256 `c7137ce3da4cc19d0431955feedc10fb6b9731214ad3cfc7966160e72f8559da`.

## Validation

The evidence fence passed: 2970 Documents rows across 47 files, 838 distinct
SHA256 digests. A separate mutation checkout changed the Good Friday 2026 bond
close from 11:14 to 11:13; the public boundary test failed as required. The mutation
was restored and that checkout removed. The chronological query changes were read
for bounded work and error propagation; the public forward/backward fixtures
exercise ordering over normal and replacement candidates.

Full exact-head quality and MSRV verification passed on e041: formatting, strict all-target clippy, all 1335 integration tests (906.897 seconds), three doctests, warning-free rustdoc, cargo deny and MSRV 1.95. Dependency checks emitted only unused license-allowance warnings. The source-defect verdict remains reject despite these passing tests.
Test fixtures are boundary regressions; the source comparison above supplies their
independent evidence. A copied static fixture list alone does not prove source truth.

## Unresolved broader release scope

This correction leaves OANDA identities dormant/Partial. The six absent derivative
families, current Australia 200 seasonal selector, historical normal-week/holiday
spans, TRY holiday scope and Carter/Brent source ambiguities remain #332 obligations.
Passing checks or merging this correction cannot certify the entire OANDA programme.


## Corrected pushed head source acceptance

The author pushed `e32843fba07d7b9580cd96860d253ccbe3e00315`. Its changes were
independently re-read against the same UK operator bytes; all seven findings
above are addressed. No remaining source or implementation blocker was found
within this correction's documented dormant/Partial scope. This is a source
acceptance pending the fresh full verification chain, not final merge approval.
The final diff contains 34 files (the original 33 plus a second affected test
fixture file); no plan/charter changed. The five tables now contain 143 rows:
30 index, 30 Treasury, 27 commodity, 32 spot metals and 24 Brent. Other identity,
service-tier and basis counts remain the ones recomputed above.

The 12 public correction tests and full Documents fence pass on the pushed
corrected head. A second isolated mutation changed the new bond May 26
Unsourced row to Closed; the typed-gap regression failed. That mutation was
restored and its checkout removed. The source uncertainty is now surfaced as a
typed refusal and does not masquerade as either ordinary trading or a closure.

The older research note's HKEX “Complete evidence base” assertion is qualified
by its own missing later cutover circulars. The MEFF note records unavailable
2010–2016 interim grids and 2012–2013 holidays; the Long Gilt note records
2015–2020 and full-year 2010 archive gaps. They establish research/build input,
not full sourced OANDA calendars. An additive STATUS verdict records these
limitations; the earlier notes are preserved as history.


## Corrected-head final verdict — 2026-10-11 UTC

**Pass within the documented dormant/Partial correction scope**, exact pushed
head `e32843fba07d7b9580cd96860d253ccbe3e00315`. The reviewer did not write
the change. All seven source/data/prose findings above are corrected on the
pushed commit and its affected checks were rerun. No outstanding merge-blocking
defect was found within this PR's stated correction.

The full fresh-head Verification chain completed successfully: formatting,
strict all-target clippy, all 1337 integration tests in 916.922 seconds (zero
skipped), three doctests, warning-free rustdoc, cargo deny and MSRV 1.95. Cargo
deny emitted only unused license-allowance warnings. The 12 affected public
regressions and full evidence fence also passed; the latter checked 2970
Documents rows across 47 files and 838 distinct digests. Both isolated mutation
checks failed the intended public regressions and were restored.

All 143 changed holiday rows and their literal source basis were independently
reviewed. The independent parser reproduces 30 index, 30 Treasury, 27 commodity,
32 metals and 24 Brent rows; all 437 normalized operator holiday events match
the cited capture. The final report is a correction review, not a certificate
of complete served OANDA history, seasonal selectors, all planned families or
release readiness. Those remaining obligations are tracked under #332.
