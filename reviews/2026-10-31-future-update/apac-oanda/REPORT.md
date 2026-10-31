# APAC and OANDA future-publication scan — 2026-10-31 UTC

This bounded source scan found no additional session or holiday row ready to
encode for the reviewed existing scopes. It does not advance the crate's ledger
review dates or claim a complete historical re-audit. The parent task handles
NSE's 2026-11-08 Muhurat session separately.

## Captures and comparison

`retrieval.json` records the exact source URLs, UTC retrieval instants, HTTP
status, raw filenames, byte counts and SHA-256 digests. `SHA256SUMS` covers the
18 original artifacts. Extracted `.txt` and `.tables.json` files are inspection
helpers; original bytes govern.

| Scope | Result |
|---|---|
| OANDA Europe Limited UK books | The live UK holiday page's newest dated section remains 2026-10-30. No November/December 2026 publication extends any of the nine reached `oanda_*` keys. The normal-hours page's 76 table rows compare exactly equal to `normal-weeks/oanda-current-source-audit-2026-10-12/uk-hours.html` after HTML cell whitespace normalization. The existing publication boundary remains in force; #332 already records it. |
| ASX cash equities | The live calendar still publishes 2026 and 2027 only. Its future 2026/2027 closure and early-close dates match the existing scoped table and horizon through 2027-12-31. Current cash-hours page retains the single randomized open introduced in 2025 and Post Close. ASX Trade 24's 2028 expiry calendar is a different, unmodelled derivative scope and does not extend cash-equity coverage. |
| NZX Main Board | The migrated live hours page embeds its accordion in `__NEXT_DATA__`; `nzx-hours-nextdata.json` and `nzx-content-extracted.txt` expose that authorized page content. The holiday accordion still ends with 2027-01-01 and 2027-01-04, matching the current horizon. No 2027 full-year publication was found. Announcement 463713 is the already-known 2025/2027 memorandum whose final date is 2027-01-04. |
| TSE cash-equity venue union | The market-holiday page still publishes 2026/2027, already covered. Domestic and ToSTNeT current pages preserve the modelled normal-week envelope. The separate announced random-closing change is analyzed below. |
| HKEX securities venue union | The current hours and calendar pages retain the existing 2026/2027 arrangements. The calendar still gives 2027 half days on 02-05, 12-24 and 12-31; it does not publish 2028. The 2026-11-02 price-limit amendment changes order validation, not the accepted-order session times. |
| SGX securities | The live content API still scopes half days explicitly to 2025 & 2026, with the same six eve dates and unchanged ordinary/half-day grids. A newly present first-listing-day afternoon table is instrument-listing policy, not a venue-wide revision. No 2027 holiday treatment is published. |
| SSE cash-equity venue union | The official closure-notice list's newest schedule announcement is still the 2026-09-17 Mid-Autumn/National Day notice, already within the existing reviewed horizon. No 2027 annual calendar or new future session boundary was found. |

## New notices with no runtime change

### TSE planned random closing on 2027-10-12

The operator's strengthening page names 2027-10-12 for introduction of random
closing. Its linked May 22 outline states that the afternoon close Itayose will
occur between 15:29:30 and 15:30:00 Tokyo time; ToSTNeT closing-price and specified
VWAP trading still start at 15:30 regardless of the randomized instant. The older
outline's implementation paragraph is conditional on readiness; the living page
now gives the planned day.

No new `tse` profile row follows for the current scope: `tse.rs` models the venue
availability union, including ToSTNeT's 08:20–18:00 executable interval. The
existing Regular afternoon leg ends at 15:25. The random closing sits entirely
inside the already executable Extended envelope and moves neither that union's
boundary nor its required order-entry-only lead. This is not evidence to replace
the calendar with an arrowhead-only scope.

### OANDA TMS US-clock notice, effective 2026-11-01

The 2026-10-29 notice at `https://www.oanda.com/eu-en/news/time-change-in-usa-4`
describes Forex NZD, AU200.pro, DE30.pro and EU50.pro times from 2026-11-01.
The page identifies its operator as OANDA TMS Brokers S.A. This is a different
book from OANDA Europe Limited's UK pages that source the served keys. Its
publication cannot extend the UK holiday horizon or replace those keys' grids.

### SGX first-listing-day afternoon schedule

The fresh SGX content API adds a statement that new listings may start at 14:00
on the first day, with Pre-Open from 13:30 and the ordinary 17:16 final close.
The venue's ordinary morning sessions still run for other securities. The
consumer owns individual instrument listing windows under the charter; no
venue-wide cutover or holiday date is stated, so no runtime selector row follows.

## Unchanged completeness

No captured date is used as an exchange cutover. OANDA's post-2026-10-30
publication boundary, SGX's post-2026-12-31 boundary, and NZX's post-2027-01-04
boundary remain unchanged. No government holiday table, another OANDA entity's
publication, derivative expiry calendar, mock-test session, or third-party
restatement was substituted for operator evidence for the exact served scope.
