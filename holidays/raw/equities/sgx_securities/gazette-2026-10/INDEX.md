# sgx_securities — the rulebook/gazette derivation attempt — 2026-10-05 UTC — operator leg absent, state leg retrieved and validated

Fifth retrieval pass on #213 (the 2011-08-01..2013-12-31 and
2020-01-02..2024-12-31 holiday capture gaps), this time on the untried
derivation-by-reference angle the maintainer set on 2026-10-05: find an
unconditional operator rulebook clause closing the securities market on
Singapore's gazetted public holidays, then let the state's own dated holiday
publications supply the dates (the LAW-PRIMARY-SOURCES lineage pattern for
cross-references).

**Verdict: the operator leg does not exist, so nothing encodes.** The SGX-ST
rulebook — checked in the operator's own dated artifacts from inside both gap
eras and in the live consolidated text — never closes the market on public
holidays; it delegates the trading calendar to SGX-ST's own publications, which
is exactly the channel the four earlier hunts proved unsurveyed for the gap
years. The state leg (the gazetted holiday lists for every gap year and every
validation year) is retrieved here in full, and the derivation it would key is
validated exactly against the crate's sourced 2014-2019 years, so a future
operator-leg find keys rows immediately from this store. Retrieval instants
2026-10-05 00:11-01:35 UTC. Digests in `SHA256SUMS.txt`.

## 1. The operator leg — negative, verified from the operator's own words

What the rulebook actually says about the securities trading calendar, quoted
verbatim:

- **SGX-ST Rules Rule 8.2.1** (live consolidated rulebook,
  `sgx_st_rules_consolidated_live-20261005.html`, read 2026-10-05 UTC; the
  rule carries no amendment markers): `The trading hours and the application
  of the market phases are as published by SGX-ST. SGX-ST may vary the trading
  hours and application of the market phases. Refer to Practice Note 8.2.1.`
- **Practice Note 8.2.1 as amended 2011-08-01** (operator PDF,
  `sgx_st_rules_2011-08-01.pdf`, served live by rulebook.sgx.com; dated inside
  the 2011-2013 gap): `Rule 8.2.1 says the trading hours and the application
  of the market phases are as published by SGX-ST.` and `Rule 8.2.2 says
  SGX-ST may vary the trading hours and application of the market phases.`
- **Practice Note 8.2.1 as amended 2013-04-15** (operator amendment PDF,
  `sgx_st_rules_2013-04-15.pdf`, Wayback `id_` replay of capture
  20211130082137; dated inside the 2011-2013 gap): the same two delegation
  sentences verbatim.
- **SGX-ST Rules definitions** (live consolidated text): `"Market Day"` is
  defined circularly — `A day on which SGX-ST is open for trading in
  securities and/or futures contracts` — and the word `holiday` appears
  exactly once in the whole live SGX-ST Rules, in Rule 9.1A.3, about
  *settlement-currency* holidays, not the trading calendar.
- **The seven SGX-ST Directives** (live rulebook listing): directorship,
  remisiers, designated market-makers, audit trails, systems, ADRs, one
  deleted — none concerns trading days or holidays.
- **The `8.2 Trading Hours` rulebook display page, captured 2021-12-08**
  (inside the 2020-2024 gap; `rulebook_82_trading_hours_capture-20211208.html`):
  a JS shell whose served bytes carry no rule text and no holiday content —
  no different from the wps SPA shells.
- **By contrast, the derivatives rulebook does carry the pattern** — the live
  Futures Trading Rules (`sgx_futures_trading_rules_live-20261005.html`)
  define `"Business Day"` as `any day other than a Saturday, Sunday or public
  holiday in Singapore` — but that is the SGX-DT rulebook's administrative
  term for deadline counting, not the securities market's calendar, and the
  SGX-ST rules have no counterpart clause.

The one operator statement that does adopt the state calendar is the current
`/stock-exchange/trading` page's designation sentence (`SGX follows the
Singapore holiday calendar available on the Ministry of Manpower website`),
read 2026-09-28 UTC and later — but the crate's own 2025-2026 precedent
(`docs/evidence/sgx_securities.md`, `SGX-ST-SCHED`) reads that designation as
scoped to the sheet's printed years (the window stops at 2026-12-31 even
though MOM has gazetted 2027), and a capture dates the observation, never the
state: a 2026 sentence sources no day in 2011-2013 or 2020-2024.

Also retrieved: `sgx_st_rules_2012-10-25.pdf` (Wayback replay of capture
20210924050410 — practice-note amendments of 25 October 2012, none touching
trading hours or holidays; the 3-page amendment set, not a consolidated
edition) and `sgx_st_rules_2019-06-03.pdf` (the 3 June 2019 edition, Wayback
replay of capture 20211027110927 — the capture truncates at 1,048,576 bytes
and keys nothing; the live consolidated text above carries the current rule).
`sgx_rn_821_live-20261005.html` is the live Regulatory Notice 8.2.1 page.

## 2. The state leg — retrieved in full for every gap and validation year

Singapore's gazetted public-holiday lists, as the state's own dated
publications (MOM press releases, MOM pages, MOM iCalendar feeds). All Wayback
`id_` replays resolved to their true capture timestamps (the 2015 ICS request
at 20150810214816 redirected to capture 20150908035127, which is what is
saved).

| Year | Artifact | Capture (UTC) | Notes |
|---|---|---|---|
| 2011 | `mom_press_release_holidays_2011_capture-20100424232617.html` | 2010-04-24 | press release of 21/22 Apr 2010 printing the 2011 table with `*` substitution sentences; Deepavali 26 Oct almanac-pending, never changed |
| 2011 | `mom_public_holidays_sg_2011_ics_capture-20100709130200.ics` | 2010-07-09 | 10 events; no in-lieu events (substitutions by MOM's own sentences) |
| 2012 | `mom_public_holidays_2012_capture-20110408071834.html` | 2011-04-08 | page last updated 2011-04-04 printing the 2012 table with `*` sentences |
| 2012 | `mom_public_holidays_sg_2012_ics_capture-20110411030539.ics` | 2011-04-11 | 10 events |
| 2012 | `mom_public_holidays_2012_capture-20130125021017.html` | 2013-01-25 | in-2013 re-print confirming Deepavali 13 Nov 2012 `as previously announced` |
| 2013 | `mom_public_holidays_2013_capture-20130124140621.html` | 2013-01-24 | page last updated 2013-01-21; Deepavali pending the Indian Almanac |
| 2013 | `mom_public_holidays_2013_final_capture-20131103004641.html` | 2013-11-03 | page last updated 2013-09-04: HAB moved Deepavali to **Saturday 2 November 2013** and states `4 November 2013 (Monday) will not be a public holiday` |
| 2014 | `mom_public_holidays_sg_2014_ics_capture-20150908074325.ics` | 2015-09-08 | carries the HAB-corrected Deepavali 22 Oct 2014 |
| 2015 | `mom_public_holidays_2015_ics_capture-20150908035127.ics` | 2015-09-08 | carries SG50, the National-Day in-lieu, Polling Day; **only one CNY event** |
| 2015 | `mom_public_holidays_2015_capture-20141230015837.html` | 2014-12-30 | print-page capture printing **both CNY days 19+20 Feb 2015** |
| 2016 | `mom_public_holidays_sg_2016_ics_capture-20150908074329.ics` | 2015-09-08 | carries the Labour-Day and Christmas in-lieu events; **only one CNY event** |
| 2016 | `mom_public_holidays_2016_capture-20160103151342.html` | 2016-01-03 | in-2016 capture printing **both CNY days 8+9 Feb 2016** and the 2 May / 26 Dec in-lieu sentences |
| 2017 | `mom_public_holidays_sg_2017_ics_capture-20160413111331.ics` | 2016-04-13 | carries all three in-lieu events |
| 2018 | `mom_public_holidays_sg_2018_ics_capture-20170409050351.ics` | 2017-04-09 | 11 events |
| 2019 | `mom_public_holidays_sg_2019_ics_capture-20180430074830.ics` | 2018-04-30 | 11 events; the three Sunday holidays carry no in-lieu events |
| 2020 | `mom_public_holidays_sg_2020_ics_capture-20190720113906.ics` | 2019-07-20 | pre-announcement: **no Polling Day 2020-07-10** |
| 2020 | `mom_public_holidays_2020_capture-20200627213513.html` | 2020-06-27 | in-2020 page: carries **Polling Day 10 July 2020** (Parliamentary Elections Act s.35) and the 27 Jan / 25 May / 10 Aug in-lieu sentences |
| 2021 | `mom_public_holidays_sg_2021_ics_capture-20200925162357.ics` | 2020-09-25 | in-span |
| 2022 | `mom_public_holidays_sg_2022_ics_capture-20210421140625.ics` | 2021-04-21 | in-span |
| 2023 | `mom_public_holidays_sg_2023_ics_capture-20220519084930.ics` | 2022-05-19 | carries the **unshifted** CNY pair 22+23 Jan (Sun+Mon) |
| 2024 | `mom_public_holidays_sg_2024_ics_capture-20230608051247.ics` | 2023-06-08 | in-span |
| live | `mom_public_holidays_live-20261005.html` | 2026-10-05 | the current MOM page (context) |

## 3. The validation — the derivation reproduces the sourced years exactly

Rule: gazetted holiday dates from the state's own artifacts + MOM's own
Sunday-substitution sentences (`The following Monday will be a public
holiday`), keeping weekdays only — compared against the crate's shipped
sourced closures (recomputed from
`src/calendar/schedules/holidays/sgx_securities.rs` at origin/main a144b5b):

- **2014: exact (9/9).** Includes the HAB-corrected Deepavali 22 Oct (state
  ICS captured post-correction) and the Hari Raya Haji in-lieu Monday 6 Oct
  (state ICS omits the event; MOM's own page sentence supplies it — the
  in-2016 page above prints `Monday, 6 Oct 2014 will be a public holiday`).
- **2015: exact (13/13)** — SG50 7 Aug, Polling Day 11 Sep and the National
  Day in-lieu 10 Aug are all gazetted state holidays, matching the SGX sheet.
  The ICS alone under-covers CNY (one event); the state page prints both days.
- **2016: exact (9/9)** — same ICS CNY defect, same page-level correction.
- **2017, 2018, 2019: exact (10/10, 10/10, 11/11)** — including the three
  2019 in-lieu Mondays (20 May, 12 Aug, 28 Oct) the ICS omits.
- **2020-01-01: exact** (the one sourced 2020 date is the state's New Year's
  Day).

So for every year the crate holds a sourced operator sheet, the state's own
gazetted list plus its substitution sentences reproduces the operator's
closures date for date, with no exchange-specific extra closure and no
gazetted weekday the operator ignored. The derivation is validated; only the
operator-side adoption dated inside a gap span is missing.

## 4. The state-side weekday sets for the gap years (working aid, NOT encoded)

Derived as above; held here so a future operator-leg find keys rows without
re-retrieval. The two `*`-marked dates in 2023 need MOM's in-year page to
confirm the observed CNY pair, which the 2023 ICS leaves unshifted.

- 2011: 3 Feb, 4 Feb, 22 Apr, 2 May, 17 May, 9 Aug, 30 Aug, 26 Oct, 7 Nov,
  26 Dec (10 dates: CNY Thu+Fri; Labour/HRH/Christmas Sundays -> Mondays
  2 May / 7 Nov / 26 Dec).
- 2012: 2 Jan, 23 Jan, 24 Jan, 6 Apr, 1 May, 9 Aug, 20 Aug, 26 Oct, 13 Nov,
  25 Dec (10).
- 2013: 1 Jan, 11 Feb, 12 Feb, 29 Mar, 1 May, 24 May, 8 Aug, 9 Aug, 15 Oct,
  25 Dec (10; Deepavali Saturday 2 Nov closes no weekday and 4 Nov is
  expressly not a holiday).
- 2020: 1 Jan, 27 Jan, 10 Apr, 1 May, 7 May, 25 May, 10 Jul (Polling Day),
  31 Jul, 10 Aug, 25 Dec (10).
- 2021: 1 Jan, 12 Feb, 2 Apr, 13 May, 26 May, 20 Jul, 9 Aug, 4 Nov (8).
- 2022: 1 Feb, 2 Feb, 15 Apr, 2 May, 16 May, 9 Aug, 24 Oct, 26 Dec (8).
- 2023: 2 Jan, *23 Jan*, *24 Jan*, 7 Apr, 1 May, 29 Jun, 9 Aug, 13 Nov,
  25 Dec (9; the observed CNY pair Mon 23 + Tue 24 per the Holidays Act
  next-day shift).
- 2024: 1 Jan, 12 Feb, 29 Mar, 10 Apr, 1 May, 22 May, 17 Jun, 9 Aug, 31 Oct,
  25 Dec (10).

## Net

The derivation-by-reference path is closed on the operator side and open on
the state side: #213 stays open with a sharpened closing condition — a
surviving **operator** artifact dated inside a gap span that either prints
the closures or adopts the gazetted calendar (the designation sentence's
equivalent from inside the span, e.g. a member notice or a readable calendar
page). The state-side dates are held and validated above; the operator leg
alone would complete the composite. The archive.today 2012-09-10 snapshot
remains the one human-side lead for the 2011-2013 span.
