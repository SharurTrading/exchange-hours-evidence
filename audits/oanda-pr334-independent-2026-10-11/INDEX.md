<!-- SPDX-License-Identifier: MIT-0 -->

# Independent OANDA PR #334 review — 2026-10-11 UTC

This audit independently re-retrieved the official UK operator pages and reviewed
all changed holiday rows and source claims. `review.md` records the original
head rejection and the corrected head's review. `capture.json` records retrieval
instants and source URLs. Captures are preserved byte for byte; `SHA256SUMS.txt`
fences every artifact in this audit directory.

| Artifact | Purpose |
|---|---|
| `current-holidays.html` | Independent HTTPS capture of the UK holiday page |
| `current-hours.html` | Independent HTTPS capture of the UK normal-hours page |
| `holiday-events.json` | Own parser's normalized heading/list events for source comparison |
| `recompute.py` | Independent immutable-head macro/ledger count and source comparison helper |
| `recomputed-counts-e041.json` | Original-head counts, including the incorrect ledger basis counts |
| `recomputed-counts-e328.json` | Corrected-head counts: 143 holiday rows |
| `mutation.log` | Original-head one-minute bond-close mutation fails the public regression |
| `mutation-e328.log` | Corrected-head Unsourced-to-Closed mutation fails the typed-gap regression |
| `affected-e328.log` | Twelve affected public correction tests pass |
| `evidence-e328.log` | All 2970 Documents rows/838 digests across 47 files verify |
| `nextest-e041.log` | Original-head full suite: 1335 passing tests |
| `nextest-e328.log` | Corrected-head full suite: 1337 passing tests, no skips |
| `verification-e328.json` | Exact corrected-head full Verification result and evidence/mutation counts |

The supplied PDF and existing cited holiday capture stay at their established
locations/digests; this audit does not silently revise them. The undated static
operator guide was independently fetched and reproduced digest
`778ea39e0f71005015a111963061cd86f8d7fce7b589af0279316992239244ba`.

The correction remains limited to the documented dormant/Partial scopes. Broader
OANDA completeness remains exchange-hours-rs issue #332; wave-2 source/build plans
and passing tests do not close its historical and selector gaps.
