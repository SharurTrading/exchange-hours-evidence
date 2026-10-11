<!-- SPDX-License-Identifier: MIT-0 -->

# Independent review of library PR #335

Review date: 2026-10-11 UTC. Exact pushed head:
`a0d1479b7d8d5ef391cb918598c94d160d12e41a`.

Verdict: **PASS within the documented dormant/Partial correction scope.**

## Scope and source reproduction

The reviewer did not write the library correction. This review covers the
Carter exception, current starred interpretation and index-scope correction;
it does not certify complete OANDA history or release readiness.

Changed files were classified as one holiday data module, one public key
reference, three evidence files, the source watch list, the verification
ledger, the changelog and two public integration-test files. No charter or
plan changed. Existing source captures were independently read and hashed
rather than accepting PR prose or copied fixture lists as source evidence.

All 31 rows in the touched index table were checked against the operator's
literal statements, kinds, dates and event-to-trade-date derivations. Unchanged
rows resolve to the current UK holiday capture; the two Carter rows resolve to
the archived March 2025 UK page, corroborated by the February 2026 replay.
The two archive digests reproduce, as does the supplied current PDF digest.
The source says `9:30`, without a meridiem; its dated Eastern-Time section,
adjacent 24-hour statements and close-before-18:00-reopen sequence support
09:30. This is a contextual derivation, not a fabricated literal `09:30` or
`AM` quotation. Independent Python `zoneinfo` conversion yields a January 9
14:30 UTC close, January 9 23:00 UTC reopening and January 10 21:59 UTC
ordinary close. The reopening belongs to the January 10 trade date.

The current PDF labels both the named exchange timezone and local exchange
hours. Its *** instruction advances only the marked endpoint by one local
hour during that named zone's daylight time: Sydney close 06:59 -> 07:59;
Frankfurt opening 01:16 -> 02:16. Unmarked endpoints retain their local values
and all endpoints still receive ordinary IANA conversion. FX's * and metals'
** describe different breaks; the conditional Shares/ETF wording does not
establish an unconditional extra shift. The older static guide's explicit
US-season Australian rule belongs to its different older grid. No archive
capture is treated as an unconditional effective day.

The generic US-index notices do not prove that Japan 225's two listings belong
to every holiday arrangement. Matching normal clocks and explicitly named
Christmas/New Year rows establish only those observations. Final public key,
ledger, evidence and changelog restrict the exact scope to US SPX 500, US Nas
100, US Russ 2000 and US Wall St 30; Japan requires an operator definition or
its own exact calendar under #332. A read-only check of the isolated,
uncommitted consumer snapshot confirms the four-root route and typed Japan
refusal under that earlier policy. The Japan guard and seven OANDA internal cases were independently
rerun successfully; that is a narrow prose check, not a committed-head consumer
release review. No proprietary source is reproduced in this public record.

## Counts and resolved findings

The independent parser reads immutable-head module tuples and ledger cells;
it reproduces 31 index, 30 Treasury, 27 commodity, 32 metals and 24 Brent rows
(144 across those five tables), 141 ledger identities, 74 Primary, 65 Partial,
two Synthetic, 36 served and 105 dormant identities, and 50 holiday-bearing
ledger rows. The index holiday window remains 2025-01-01..2026-10-30 and the
normal-week witnessed horizon remains 2024-02-21. All OANDA keys remain dormant
with the existing Partial basis and on-demand cadence. All 437 independently
normalized current holiday events agree with the cited capture.

Earlier review blockers were corrected on pushed heads: the Good Friday label
still described an obsolete index/bond intersection; broad six-listing index
scope inferred Japan membership from clock equality; source-index and Treasury
cross-references retained those superseded readings. The final source prose
and counts agree with the artifact and registration surface. Earlier whole-chain
runs were stopped when the author pushed corrections and do not count as
passes for the final head.

Remaining historical normal-week and holiday gaps, Memorial's incomplete
18:0 reopening, Brent's silent dates, TRY holiday scope, six absent derivatives
families and Japan's exact holiday scope remain #332. The prior complete-wave-2
research language remains historical; review record #21 qualifies it. The
current named-zone reading resolves current *** interpretation, not the old/current
transition date or missing runtime families.

## Additional historical context preserved

The newly retrieved FIX specification is preserved separately under
`normal-weeks/oanda-legacy-fix-context-2026-10-11/`. Its 857,213 PDF bytes
reproduce SHA256 `8f91517f619c116ee0ee5c2b1aca6d5eeaf51e5e840538b29cec3e9de7f89074`.
The reviewer independently extracted text (identical to the saved derivative)
and rendered page 8. The cover names a November 25, 2011 last update; the
Wayback observation is August 16, 2012. Page 8's continuous-week currency
statement and typical Friday 17:00 Eastern maintenance are historical context.
The adjacent DAY-order expiry is lifecycle data, not a session boundary.
Nothing establishes full week endpoints, the UK-specific 2010 baseline or an
unconditional effective day. The four exact CDX results are saved without
turning three empty results into a claim that all research angles are exhausted.
Nine hashes fence the seven original files and added README/retrieval metadata.
No broker contact occurred.

## Validation cache observation — #336

The restored mutation and clean review worktrees initially reused a target
directory. The subsequent clean suite did not recompile the library (0.05s)
and retained the mutation's 09:31 behavior, producing 12 passes and one Carter
failure. This bad clean log was recovered verbatim from the recorded tool-output
read before the retry overwrote its original path. A fresh target directory
passed all 13 public tests. The full exact-head chain uses a separate target
that never received the Carter mutation, and that test passes there.

`cache-conditions.json`, `cache-bad-clean.log`, `mutation.log` and
`public-regressions.log` preserve the observed conditions and mitigation.
The internal investigation is exchange-hours-rs#336 under PROC-DEP-DECIDE;
no exact cache root cause or upstream fault is asserted, and no upstream
contact occurred. This workflow observation does not alter source values.

## Final pushed-head validation

The pristine detached a0d1479 worktree completed the entire charter Verification
chain in order with exit code zero: formatting, strict all-target clippy,
1,337 integration tests in 987.508 seconds (zero skipped), three doctests,
warning-denied rustdoc and cargo deny, followed by all-target MSRV 1.95 check.
Cargo deny reports only the existing unmatched-license-allowance warnings.
The separate 13 public publication regressions pass. The full evidence fence
verifies 2,972 Documents rows across 47 files and 840 distinct digests.

The final-head mutation moved Carter's close from 09:30 to 09:31 in a separate
worktree and failed the intended public end-exclusive boundary assertion.
The mutated file was restored and the mutation worktree removed. The full
chain target is reused from earlier verification builds, not globally fresh;
it is separate from the Carter mutation target. Its log records compilation
of the exact clean final-head library, and the Carter regression passes.
No source edits or simultaneous mutations occurred in the final review worktree.

There is no remaining source/data/prose blocker within this correction.
This pass does not establish complete OANDA history, every product/holiday
scope, the six unbuilt families, consumer activation or release readiness.
Those obligations remain #332; the mitigated cache investigation is #336.

The consumer snapshot and Japan guard describe the policy reviewed before the
operator requested separate holiday inheritance. Subsequent consumer policy
choices are outside this exact-head source verdict; an adopted assumption is
not certified here as independently sourced OANDA coverage (#332).
