# NSE Muhurat forward confirmation — issue #374

**Confirmed 2026-10-31 UTC. No runtime discrepancy found.** The merged
`2026-11-08` replacement schedule remains supported by the operator's live
capital-market circular and the checked later circular channel. This completes
the requested confirmation before the 2026-11-07 confirm-by deadline. It is an
observation of a published future arrangement, not a claim that the session has
occurred or that later notices cannot amend it.

## Fresh primary retrieval

- Source: <https://nsearchives.nseindia.com/content/circulars/CMTR76941.pdf>.
- Document: NSE/CMTR/76941, circular 149/2026, issued October 19, 2026,
  Capital Market Segment; special live session on Sunday, November 8, 2026.
- Retrieval completed: **2026-10-31T23:19:09.653909Z**, HTTP 200,
  **161272 bytes**. The resolved URL is the requested URL.
- SHA-256:
  `ce94ee1c54d98eccdf3c30fa0673ae2b6a49ea4ed4a72fb83d826f4359f71d58`.
- The fresh PDF is byte-identical to the document used by merged PR #375.
  The server's Last-Modified header is 2026-10-19 10:27:08 GMT; that header is
  retrieval metadata rather than an effective trading date.

`FETCH.json` records exact requested/resolved URLs, start and completion UTC
times, HTTP status, size, content type and SHA-256 for each fetched artifact.
`CMTR76941.pdf` holds the primary bytes, and `CMTR76941.layout.txt` is the
`pdftotext -layout` extraction read against the timing table. The original
2026-10-31 22:06 UTC retrieval entry in the crate's Documents table is preserved.

## Merged phase comparison

The comparison applies to merged crate head
`d3f6b21db8f4f7523f0c79b786c16c6852c4678c`, specifically
`src/calendar/schedules/holidays/nse_india.rs`. All times below are IST
(`Asia/Kolkata`), and closes remain end-exclusive.

| Merged kind | Interval | Primary phase and derivation |
|---|---|---|
| Extended | 13:50–14:05 | Printed block-deal session |
| Order entry | 14:05–14:13 | Pre-open starts 14:05; the 14:10–14:15 limit-order period randomly closes in its last two minutes, so 14:13 is the earliest possible matching onset |
| Extended | 14:13–14:20 | Existing conservative pre-open envelope; the source nominally prints matching 14:15–14:17 and buffer 14:17–14:20 |
| Regular | 14:20–15:30 | Continuous trading starts 14:20; CAS securities leave at 15:15, while the source explicitly keeps non-CAS securities continuous to 15:30 |
| Extended | 15:30–15:35 | CAS matching and confirmation continue after the non-CAS continuous close; CAS random collection closure does not remove the other securities' executable union |
| Extended | 15:50–16:00 | Printed post-close session |

The 15:35–15:50 CAS transition is closed. IPO/relisting special pre-open
14:05–14:50, its normal-market interval 15:05–15:30, and the illiquid-call
session 14:25–15:10 remain inside the venue envelope. The 16:15 trade
modification cutoff is administrative and does not extend the executable or
new-order session. The source states settlement obligations for the special
live trades. All six block day offsets remain zero, and the replacement row's
trade date is Sunday, 2026-11-08, rather than the following Monday.

`check-merged.py` independently validates every extracted time cell in source
order, derives the six blocks from those cells and the source's random-closure
footnote, parses the merged Rust block expressions, and compares each kind,
offset and endpoint. `merged-check.json` records the source/module digests,
merged head, derived and shipped blocks, and PASS result. This check does not
derive expectations from the shipped block constants or the existing test's
expected boundary list.

## Superseding and amending circular search

After an ordinary browser-user-agent/cookie warm-up, the operator's live API
was fetched successfully:

<https://www.nseindia.com/api/circulars?index=CM&fromDate=19-10-2026&toDate=31-10-2026>

The response completed at **2026-10-31T23:19:15.913908Z**, HTTP 200,
**122282 bytes**, SHA-256
`2fca4df6da8070501675e43a44aa09761fdbae450d0fe82e762e59951b567076`.
It returns the requested from/to dates, **275 records covering 235 distinct
artifact URLs**. Returned publication dates span October 19–31. Despite the
`index=CM` parameter, records include other departments, so the search inspected
the actual department and document identifiers rather than assuming every row
is a capital-market session notice.

Every returned CMTR artifact was checked: seven distinct circulars, the original
149/2026 and the six later circulars 150/2026 through 155/2026. Their actual
PDF contents, including the main PDF and PDF annexures in CMTR77188.zip, do
not amend the November 8 live schedule:

| Circular | Published | Checked scope |
|---|---|---|
| CMTR76941 | October 19 | Original live Muhurat schedule; unchanged primary bytes |
| CMTR77047 | October 22 | October 24 mock session, with no fund pay-in/pay-out obligation |
| CMTR77182 | October 30 | October 31 eOFS mock session; mock bids carry no funds/securities obligation |
| CMTR77188 | October 30 | Tender-offer interoperability and operating guidelines; go-live to be shared separately, no Muhurat amendment |
| CMTR77196 | October 30 | October 31 BCP/DR mock session, with no fund pay-in/pay-out obligation |
| CMTR77210 | October 30 | ANLON SME market-lot corporate-action adjustment |
| CMTR77217 | October 30 | NNF/Algo-ID order validation effective November 23; no session-hour change |

Subjects of all 275 records were also inspected for Muhurat, Diwali, session,
auction and references to 76941. `circular-candidates.json` preserves that
broader candidate set. Three later notices relevant to the capital-market
Muhurat date were fetched and read in full:

- **ISC77098, October 26:** explicitly references CMTR76941, reiterates the
  November 8 session, and adds the UCC-compliance cutoff at 22:00 on November 7.
  This controls client eligibility, not venue operating hours.
- **CMPT77037, October 21:** capital-market clearing, trade modification,
  reporting, collateral and settlement administration for the November 8 trades;
  it does not extend or amend the trading session.
- **CMPL77195, October 30:** client-collateral segregation reporting dates,
  explicitly referencing the November 8 session; no trading-hours amendment.

Other returned Muhurat notices belong to derivatives, debt/RFQ, electronic gold
receipts or securities lending/borrowing; their metadata was checked for scope,
and their schedules were not applied to this capital-market venue. The sole
October 31 record is NCL/CMPT/77222, an equity-derivatives client-position-limit
file update, not a live cash-session notice. The latest returned CMTR date is
October 30.

This negative result is bounded to the live date-filtered circular response,
its returned metadata, the unchanged primary PDF and the later artifacts
explicitly identified above. It does not certify an independently complete
inventory of every NSE publication channel, nor any notice issued after the
recorded retrieval times. No refused channel was bypassed or repeatedly probed.

## Changes and checks

The crate edit is confined to `docs/evidence/nse_india.md`: the pending
confirm-by sentence becomes a dated completed confirmation with the fresh
retrieval time/digest and evidence location. Historical Documents retrieval
information, runtime blocks, tiers, document IDs and coverage windows remain
unchanged. Parent owns combined issue/PR updates and final repository checks.

Subtask validation passed: independent source-to-block comparison,
`cargo xtask verify-evidence NSE-CIRC-2026-149`, the existing
`nse_muhurat_2026_preserves_published_phases_and_weekend_trade_date` public
boundary test (**1 passed**, the remaining 353 tests in that binary excluded
by the explicit filter), Markdown lint, and `git diff --check`. All twelve
HTTP-200 captures reproduce their manifest sizes and digests. A direct
comparison with HEAD confirms the historical NSE-CIRC-2026-149 Documents row
is byte-for-byte unchanged. Logs are retained beside this report.

Artifacts and reports live only under
`reviews/2026-10-31-confirm-374/nse/`. `SHA256SUMS.txt` covers the subtree files
other than itself. No commit, push, external post or runtime edit was made by
this subtask.
