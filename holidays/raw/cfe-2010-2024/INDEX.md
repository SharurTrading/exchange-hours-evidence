# CFE 2010-2024 holiday backfill — new artifacts (2026-09-29 UTC)

Phase 2 of the release plan: extending the `cfe` holiday table below its 2025 window.
The per-holiday notices for holiday years 2018-2024 were already fetched live from the
operator's CDN in the 2026-09-21 pass and live under
`holidays/raw/cfe-2010-2025/live/` (URLs and sha256 in that directory's
`live_index.json`; the pass is recorded at day granularity, 2026-09-21 UTC, in
`cfe-2010-2025/RECON.md`). This pass adds the rules-page captures that carry the
complete holiday calendar for the pre-notice era and the derivation notes.

## Rules-page captures (this pass, retrieved 2026-09-29T03:38:58Z)

All three are `id_` replays of `cfe.cboe.com/about-cfe/holiday-calendar` (T1 via the
verbatim Wayback mirror; the operator's own CFE Holiday Schedule page).

| File | Capture stamp | sha256 |
|---|---|---|
| `rulespage/cfe_holiday_calendar_20170410210429.html` | `20170410210429` | `e21e574eb0a960337a855c323d314304cf58dc45b5afc135dbb813e32e2212d1` |
| `rulespage/cfe_holiday_calendar_20170626003649.html` | `20170626003649` | `041bfa10177880270b2057d50c4bf7674937268638437e5d25929cb64c62d327` |
| `rulespage/cfe_holiday_calendar_20171113014035.html` | `20171113014035` | `c3a6a1a715002766918063a0fe1870a41e6799a0d6e43d8e5e1ff2a25c093f05` |
| `rulespage/cfe_holiday_calendar_20171229070624.html` | `20171229070624` | `4e803f6358871afc1f71d5c0f481e812255761612600b958ecaa8bbf29f3d5f8` |
| `rulespage/cfe_holiday_calendar_20191215133022.html` | `20191215133022` | `938c104860a164f051aa3b0429c39273ddea1525bea205dfdd7fd16a9ce8f6cf` |

Each 2017 row cites the latest capture that precedes its holiday (April 10 for Good
Friday and Memorial Day, June 26 for the Independence pair and Labor Day, November
13 for Thanksgiving and Christmas, December 29 for 2018-01-01); the five captures
print the same 2017 calendar and the same hours tables, so the bracketing captures
also witness the rules' continuity across 2017.

The April and December 2017 captures both print the complete **2017 CFE Holiday
Calendar** (nine dates, New Year's Day observed Monday 2017-01-02 through Christmas
Monday 2017-12-25) and the full holiday-hours tables (Monday-observed holidays to
10:30 a.m. CT with Regular `None`; Thanksgiving to 10:30 with the Friday
`8:30 a.m. to 12:15 p.m.`; the floating set with its observed-day rules; New
Year's/Christmas Monday-Thursday printing no holiday-day session and reopening at
5:00 p.m. on the holiday). The December 2019 capture carries the same page evolved
(post-migration grid, U.S./International labels) with the 2019 and 2020 calendars,
corroborating the 2019/2020 notice set.

The one date the page leaves open is **2017-07-03**: it prints `The Exchange will
typically close at 12:15 p.m. on July 3 (the day before Independence Day) and
December 24 (Christmas Eve)` and then `Holiday closures and shortened holiday
trading hours will be announced by circular`. Whether 2017 was a 12:15 year is
stated by no surviving artifact (no CFE notice or circular for 2017 survives; the
2017 `schedule_update` directory holds only options-exchange reminders), while 2018
is witnessed as a normal-trading July 3 by its notice's own leg structure
(`5:00 p.m. (Tuesday) to 10:30 a.m.`) and 2019/2023/2024 as 12:15 years by their
notices. 2017-07-03 therefore ships `Unsourced`.

## Notices (already in the store, cited from `cfe-2010-2025/live/`)

The `Documents` rows for holiday years 2018-2024 cite the notice PDFs under
`holidays/raw/cfe-2010-2025/live/` with the URLs and digests in that directory's
`live_index.json`. All were retrieved from `cdn.cboe.com/resources/schedule_update/<year>/`
in the 2026-09-21 UTC pass. Normal-trading witnesses without a row of their own:
`2021__Cboe-Juneteenth-Trading-Schedule-Update.pdf` (C2021061701: CFE unadjusted
Friday 2021-06-18 and Monday 2021-06-21) and
`2021__Cboe-Schedule-for-New-Year-s-Holiday-2021-Notice.pdf` (C2021121601: CFE
normal hours Friday 2021-12-31).

## Gap-era witnesses (already in the store, cited from `cfe-2010-2025/infocirc/`)

| File | Wayback stamp | sha256 |
|---|---|---|
| `CFEIC15-028.pdf` | `20150905155207` | `b66e3fcb24c71e7b4a93c20a03629eb7b20005147a9923e6db04af92fa639e6c` |
| `CFEIC15-039.pdf` | — (see `cfe-2010-2025/infocirc_index.json`) | `c1597245abcc35a3a7c3ed8f9c057088acd261c8230ecf48a806f06f853ec346` |

IC15-028 (June 17, 2015): CFE closed for trading in all products Friday, July 3,
2015, with the normal 3:15 p.m. CT close Thursday, July 2. IC15-039: modified hours
for Labor Day Monday, September 7, 2015. Both are T1 and both are quoted in the
evidence file's gap prose only — 2010-2016 and January-March 2017 are unaudited
because no year's complete notice set or rules page survives.

## Derivation notes

- Rows keyed by venue-local trade date in `US/Central` (design memo D1). For the
  Monday/Thursday and mid-week floating holidays the holiday trade date's own
  session is the leg that opened 17:00 CT the previous evening and stops at 10:30
  (`early close 10:30`), exactly the 2025/2026 shape; Regular `None` on the
  holiday.
- Independence/Christmas eves: 2019-07-03, 2023-07-03 and 2024-07-03 are 12:15
  half days stated by their own notices; 2018-07-03 is audited normal (the 2018
  notice's holiday leg opens 5:00 p.m. Tuesday, so Tuesday traded its evening);
  2020-07-02 audited normal (the notice states normal hours).
- December eves: 2018-12-24, 2019-12-24, 2020-12-24 close 12:15 (notices); 2021
  Christmas observed Friday 2021-12-24 is closed outright with the Thursday-evening
  leg deleted (notice); 2022-12-23 and 2023-12-29 are normal (notices print the
  normal 3:00/4:00 PM closes); 2024-12-24 is the 12:15 half day and 2024-12-25 is
  closed (notice).
- New Year's: 2018-01-01 (rules page, Monday-Thursday chart) closed; 2019-01-01,
  2020-01-01, 2021-01-01, 2024-01-01 closed with the prior evening deleted
  (notices); 2022 New Year's Eve Friday 2021-12-31 normal (C2021121601); 2023-01-02
  closed (notice); 2022-12-31 Saturday no session.
- Good Fridays: 2018, 2019, 2020, 2022, 2024 closed (notices); 2021 and 2023 early
  close 08:30 (notices: the Thursday-evening leg stops at 8:30 a.m., Regular
  `None`).
- Juneteenth: first observed 2022 (2022-06-20, 10:30). 2021 unadjusted
  (C2021061701) — audited normal, no row.
- The pre-migration era's coarser rules-page cells (`3:30 p.m. (Wednesday)` on the
  Thanksgiving chart) and the notices' `5:00 p.m. (Wednesday)` disagree only on
  which calendar-day instants are lumped into one cell; at the crate's trade-date
  key both state the same trade-date boundary (leg to 10:30, Regular `None`).
