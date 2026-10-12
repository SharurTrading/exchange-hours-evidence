<!-- SPDX-License-Identifier: MIT-0 -->
# Independent Nordic current holiday review — 2026-10-12 UTC

Accepted source head: `cc1ca9cdf3c9a3299425f62e3f54c584785eef99`.
The reviewer did not write this change. Fresh primary retrieval of
https://www.nasdaq.com/european-market-activity/trading-hours on 2026-10-12
reproduced the named 2026/2027 equity columns and half-day clock language.
The cited saved extraction hash reproduces exactly; the artifact is correctly
labelled tool-extracted text, not original HTML.

Independent parser `check_rows.py` selects the source page's equity column,
not the fixed-income column, and reproduces all 67 rows: Copenhagen20,
Helsinki19, Stockholm28, including ten Stockholm replacements. Every row's
date, kind, source ID and T1 tier were checked. The source states all clocks
local; Stockholm half days reserve the final five minutes for closing call,
with a nominal13:00 edge and post-trading to13:30. Replacement blocks preserve
the existing opening and extended phase classifications. Normal modules are
unchanged; these tables do not establish pre-2026 holiday history.

Changed-file classes: five data/routing modules (three tables and two registrations),
three evidence files, tests, ledger, README and CHANGELOG. No charter/plan
change. Actual holiday windows, row counts, identities, dormant/on-demand
status and public documentation fences agree. Unsupported earlier and later
dates remain explicit errors. No expiry, settlement or fixed-income date is
imported.

Full exact-head chain in a detached review worktree using the immutable
research checkout passed: fmt, strict all-target Clippy, 1354 nextest tests,
zero skips, three doctests, rustdoc warnings denied, cargo deny, and MSRV1.95.
An earlier run failed because the integrator switched the mutable research
checkout during the digest fence; the successful complete replay uses frozen
source head1c28ebb and checks every cited digest. No source assertion weakened.

Meaningful mutation: shorten Stockholm half-day final edge13:30 to13:29.
The public boundary test failed (exit100); restored source passed both new
Nordic tests. Final checkout is clean. Prose/ledger/count fences also pass.
