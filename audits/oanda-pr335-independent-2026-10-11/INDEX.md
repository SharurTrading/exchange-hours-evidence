<!-- SPDX-License-Identifier: MIT-0 -->

# Independent PR #335 review — 2026-10-11 UTC

Exact library head: `a0d1479b7d8d5ef391cb918598c94d160d12e41a`.
`report.md` records the source, scope and current-star interpretation review,
resolved findings, complete gates, mutation and remaining qualifications.
`verification-result.json` and `nextest-final.log` record the completed chain;
`public-regressions.log` and `evidence-fence.log` record the separate checks.

`recompute.py <library> <evidence> <head>` reproduces the ledger/table counts
and current source comparison in `recomputed-counts.json`.
`source-witnesses.py <evidence> <head>` reproduces the raw source digests,
Carter context and independent UTC samples in `source-witnesses.json`.

`mutation.log`, `cache-bad-clean.log` and `cache-conditions.json` preserve the
negative mutation, recovered bad clean-run log and cache conditions tracked
under exchange-hours-rs#336. The fresh 13/13 run is `public-regressions.log`;
no upstream fault is asserted. The full chain uses a separate, unmutated
Carter target that records exact-head compilation, not a globally unused target.

Original operator artifacts remain in their source directories. Additional
legacy FIX context is retained separately under
`normal-weeks/oanda-legacy-fix-context-2026-10-11/`; it establishes no cutover
or complete UK baseline. SHA256SUMS.txt fences every artifact here except itself.
Complete OANDA coverage and release obligations remain exchange-hours-rs#332.
