# Evidence index — `equities/euronext_paris/forward-2027`

Forward-horizon captures for the Euronext cash and derivatives holiday calendars.
Two retrieval sessions produced the four artifacts below.

**Session 1 — 2026-09-29T22:33Z (negative sweep).** The live page still published
only 2026 and 2025; 2027 was nowhere on `live.euronext.com` or `www.euronext.com`,
which is why the crate's coverage stopped at 2026-12-31.

**Session 2 — 2026-11-14 07:12 UTC (LAW-UTC-DATES).** The operator published the
**2027 Holiday Calendar for Euronext's Cash and Derivatives markets** (notice dated
**06 November 2026**) and both hours pages now render the 2027 per-market table.
`curl` with a desktop browser User-Agent; no access control evaded;
`www.euronext.com/en/media/16439/download` served the PDF directly.

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `euronext_trading_hours_holidays.live-20260929T223334Z.html` | `https://live.euronext.com/en/resources/trading-hours-holidays` | 2026-09-29T22:33:34Z | `37ca43262e820df8f2b46fde7c9f5e4f3b878042892cae2341d0a7bf7710dbbb` | 542603 | **T1, session 1.** The page as it stood before the 2027 publication: newest calendar 2026, no 2027 content — the negative witness for the earlier horizon decision. |
| `euronext_2027-holiday-calendar-cash-derivatives.live.pdf` | `https://www.euronext.com/en/media/16439/download` | 2026-11-14T07:12:03Z | `199618806d085c381a373449588495e5ba11e6ea96d1c8d7f77361fc6f18035e` | 175109 | **T1, controlling for the 2027 rows.** "2027 Holiday Calendar for Euronext's Cash and Derivatives markets", 3 pages, Date block `06 November 2026`. Per-market columns for the served markets: Amsterdam/Brussels/Lisbon/Paris `Closed` on Friday 1 January (New Year's Day), Friday 26 March (Good Friday) and Monday 29 March (Easter Monday); `*Half Trading Day` on Friday 24 December (Christmas Eve) and Friday 31 December 2027; `Full Trading Day` on every other printed row, including Maundy Thursday 25 March, Ascension 6 May and Whit Monday 17 May. Notes state the half-day hours "will be announced in an end-of-year appendix to the Euronext Instructions 4-01 4-03 Trading Manuals" and that TAH will be open in 2027 on 2 June, all August business days, 1 November, 7 and 8 December, with "no TAH on Friday 24 and Friday 31 December". |
| `trading-hours-holidays.www.live-20261114.html` | `https://www.euronext.com/en/trading/trading-hours-holidays` | 2026-11-14T07:12:05Z | `936665412c34d9df104214ebeb0e82d6b32bf42e24172edba546fb26fd133ef4` | 562077 | **T1, corroboration.** The corporate hours page now rendering the 2027 table (24 `2027` occurrences, "2027 Holiday Calendar" header present) and the end-of-year appendix footnote. |
| `trading-hours-holidays.live-20261114.html` | `https://live.euronext.com/en/resources/trading-hours-holidays` | 2026-11-14T07:12:06Z | `20f722ae1d664576defa88e803142cde22da9ee8657cdbccec93403658a52bbe` | 347982 | **T1, corroboration.** The customer-portal hours page rendering the 2027 table (18 `2027` occurrences, "2027 Holiday Calendar" header present); still prints "2026 end of year Trading hours To be announced", so the 2026 half-day rows' closing condition is unchanged. |

## Retrieval findings

- The 2027 notice is the same artifact class as the 2026 INFO-FLASH (`IF251107…`):
  one calendar for the cash and derivatives markets with per-market columns, rows
  stated as `Closed` / `*Half Trading Day` / `Full Trading Day` per market.
- The two 2027 half days carry the same announced-but-unstated instants the 2026
  eves carried at their publication, so both dates are `Unsourced` rows with the
  closing condition "the 2027 end-of-year appendix to the Euronext Instructions
  4-01/4-03".
- No 1 May, 25 December or 26 December 2027 rows exist (all three fall on a
  weekend); the 3 May and 27 December special rows are Dublin/Athens-only and
  print `Full Trading Day` for the served markets.
