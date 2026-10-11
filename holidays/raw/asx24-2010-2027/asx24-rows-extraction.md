# ASX 24 / SFE Trading Calendar - extracted operator-stated arrangements, 2010-2027

Extracted from the captured artifacts in `/tmp/asx-spi-evidence/` (read-only).
One row per calendar date the captured calendar gives an arrangement for; the arrangement
recorded is the one for the futures family SPI 200 trades on - the “ASX 24” (formerly
“SFE”) Australian column of each table. The separate “NZ ASX 24” column (NZ products,
night open 3:40pm) is not the SPI family and is cited only where it matters.

## Arrangement tokens

| token | meaning |
|---|---|
| `day_closed` | Day Session Closed; night trades (normal). The pre-2017 wording “Night Session to open at 5:10pm / 5:00pm” states the night session's *normal* open time - the policy legend pairs it as “Day Session Closed / Night Session Normal Trading Hours”, so these are the same arrangement. |
| `fully_closed` | Closed day and night: “Closed”, “Non Trading Day”, or the International legend “Closed Day and Night Sessions”. |
| `night_closes_midnight` | Day session trades normal; the night session ceases trading at midnight Sydney. Used for US-policy holidays and every Day-before-Good-Friday row through 2026. |
| `day_and_night_normal`* | Both sessions normal - flagged informational (NZ-holiday and, from 2016, US-holiday rows; the operator lists them to say nothing changes). |
| `early_close_eq1430_night_closed` | Early close: “Equity Products to close at 2:30pm (Sydney Time)” [+ VIX 14:15pm in 2015-2020, 2025-2027 variants]; Interest Rate/Energy/Agriculture 12:30pm; Night Session Closed. The equity-products clause is the SPI-relevant leg - it is stated on a **generic products row** inside the ASX 24 column; no capture ever prints an SPI-named holiday row. |
| `day_normal_night_closed` | “Day Session Normal Trading Hours / Night Session Closed” (2017, and the Dec legs of 2022-2024; no product-level early close stated). |
| `day_session_open` | Verbatim “Day Session Open” (2010-12-28 only); the night-session arrangement is not stated in that cell. |

## Source-file legend

- **SFE2010** = `wb_20100128100216_sfe_trading_calendar_2010.htm (capture 2010-01-28; SYCOM/SFE-era calendar, covers 24 Dec 2009 - 27 Dec 2011)`
- **CAL2011a** = `wb_20101212100436_asx24_trading_calendar_2011.htm (capture 2010-12-12; covers Oct 2010 - Dec 2012)`
- **CAL2011b** = `wb_20110516085943_asx24-trading-calendar-2011.htm (capture 2011-05-16; covers Jan 2011 - Dec 2012)`
- **CAL2012** = `wb_20150906003836_asx24-trading-calendar-2012.htm (capture 2015-09-06; covers Jan 2012 - Dec 2013)`
- **CAL2013** = `wb_20131007091353_asx24-trading-calendar-2013.htm (capture 2013-10-07)`
- **CAL2014** = `wb_20131223094428_asx24-trading-calendar-2014.htm (capture 2013-12-23; covers 2014 + 1 Jan 2015)`
- **CAL2015** = `wb_20141130043626_asx24-trading-calendar-2015.htm (capture 2014-11-30; covers 2015 + 1 Jan 2016)`
- **CAL2016** = `wb_20151120050041_asx24-trading-calendar-2016.htm (capture 2015-11-20; covers 2016 + 2 Jan 2017)`
- **CAL2017** = `wb_20170103192507_asx24-trading-calendar-2017.htm (capture 2017-01-03)`
- **CAL2018** = `wb_20171222063723_asx24-trading-calendar-2018.htm (capture 2017-12-22)`
- **CAL2019** = `wb_20190821020021_asx24-trading-calendar-2019.htm (capture 2019-08-21)`
- **CAL2020** = `wb_20191022200826_asx24-trading-calendar-2020.htm (capture 2019-10-22)`
- **LIVE2010** = `wb_20201022124434_asx24_trading_calendar_live.htm (capture 2020-10-22; holds 2020 + 2021 tables)`
- **LIVE2101** = `wb_20210117034448_asx24_trading_calendar_live.htm (capture 2021-01-17; holds 2021 table)`
- **LIVE2207** = `wb_20220703182752_asx24_trading_calendar_live.htm (capture 2022-07-03; holds 2022 + 2021 tables)`
- **LIVE2212** = `wb_20221225022559_asx24_trading_calendar_live.htm (capture 2022-12-25; holds 2023 + 2022 tables)`
- **LIVE2312** = `wb_20231211225115_asx24_trading_calendar_live.htm (capture 2023-12-11; holds 2024 + 2023 tables)`
- **LIVE2503** = `wb_20250316225953_asx24_trading_calendar_live.htm (capture 2025-03-16; holds 2025 table)`
- **LIVECUR** = `live_asx24_trading_calendar.html (live page fetched 2026-10-11; holds 2026 + 2027 tables)`

Unreadable/irrelevant artifacts: all eight 2024-dated direct captures are Incapsula
bot-block pages (noted under 2024); the `cdx_*` files are Wayback CDX index listings;
`wb_2007*`/`wb_2008*`, the SPI contract-spec pages, and the `thc_*`/`live_hub_2026`/
`live_index_derivatives`/`trading_hours_calendar_current` pages are trading-hours or
spec pages, not trading-calendar tables, and are not mined here.

Mapped conventions: “Non Trading Day” is mapped to `fully_closed` (verbatim preserved);
weekend dates (25/26 Dec 2010, 6 Feb 2011, 25 Dec 2011, 25 Apr 2020/2021) keep their
operator-stated rows.

### 2010


Source: SFE2010
- **SFE2010** = `wb_20100128100216_sfe_trading_calendar_2010.htm (capture 2010-01-28; SYCOM/SFE-era calendar, covers 24 Dec 2009 - 27 Dec 2011)`

SFE/SYCOM era - rows are prefixed “SFE:”; the SFE column is the family SPI 200 trades on.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2010-01-01 | New Years Day | `fully_closed` - verbatim: “SFE: Closed” | SFE2010 |
| 2010-01-04 | New Year Holiday (NZ) | `day_and_night_normal`\* - verbatim: “SFE: Normal Trading Hours” | SFE2010 |
| 2010-01-18 | Martin Luther King Day (US) | `night_closes_midnight` - verbatim: “SFE: Night session to cease trading at mid-night” | SFE2010 |
| 2010-01-26 | Australia Day | `day_closed` - verbatim: “SFE: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | SFE2010 |
| 2010-02-06 | Waitangi Day | `fully_closed` - verbatim: “SFE: Non Trading day”. Note: Saturday; verbatim “Non Trading day” | SFE2010 |
| 2010-02-15 | Presidents Day (US) | `night_closes_midnight` - verbatim: “SFE: Night session to cease trading at mid-night” | SFE2010 |
| 2010-04-01 | Day before Good Friday | `night_closes_midnight` - verbatim: “SFE: Night session to cease trading at mid-night” | SFE2010 |
| 2010-04-02 | Good Friday | `fully_closed` - verbatim: “SFE: Closed” | SFE2010 |
| 2010-04-05 | Easter Monday | `fully_closed` - verbatim: “SFE: Closed” | SFE2010 |
| 2010-04-26 | Anzac Day | `day_closed` - verbatim: “SFE: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | SFE2010 |
| 2010-05-31 | Memorial Day (US) | `night_closes_midnight` - verbatim: “SFE: Night session to cease trading at mid-night” | SFE2010 |
| 2010-06-07 | Queen’s Birthday (NZ) | `day_and_night_normal`\* - verbatim: “SFE: Normal Trading Hours” | SFE2010 |
| 2010-06-14 | Queen’s Birthday (ex WA) | `day_closed` - verbatim: “SFE: Day Session Closed / Night session to open at 5:10pm” | SFE2010 |
| 2010-07-05 | Independence Day (US) | `night_closes_midnight` - verbatim: “SFE: Night session to cease trading at mid-night” | SFE2010 |
| 2010-08-02 | Bank Holiday (NSW) | `day_and_night_normal`\* - verbatim: “SFE: Normal Trading Hours” | SFE2010 |
| 2010-09-06 | Labor Day (US) | `night_closes_midnight` - verbatim: “SFE: Night session to cease trading at mid-night” | SFE2010 |
| 2010-10-04 | Labour Day (NSW) | `day_and_night_normal`\* - verbatim: “SFE: Normal Trading Hours” | SFE2010 |
| 2010-10-11 | Columbus Day (US) | `day_and_night_normal`\* - verbatim: “SFE: Normal Trading Hours” | SFE2010 |
| 2010-10-25 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “SFE: Normal Trading Hours” | SFE2010 |
| 2010-11-11 | Veteran’s Day (US) | `day_and_night_normal`\* - verbatim: “SFE: Normal Trading Hours” | SFE2010 |
| 2010-11-25 | Thanksgiving Day (US) | `night_closes_midnight` - verbatim: “SFE: Night session to cease trading at mid-night” | SFE2010 |
| 2010-12-24 | Christmas Eve | `early_close_eq1430_night_closed` - verbatim: “SFE: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | SFE2010 |
| 2010-12-25 | Christmas Day | `fully_closed` - verbatim: “SFE: Non Trading Day”. Note: Saturday | SFE2010 |
| 2010-12-26 | Boxing Day | `fully_closed` - verbatim: “SFE: Non Trading Day”. Note: Sunday | SFE2010 |
| 2010-12-27 | Christmas Day 'Holiday' | `fully_closed` - verbatim: “SFE: Closed” | SFE2010 |
| 2010-12-28 | Boxing Day 'Holiday' | `day_session_open` - verbatim: “SFE: Day Session Open”. Note: night-session arrangement not stated in the SFE cell; NZ: Day Session Closed, Night to open 3:40pm | SFE2010 |
| 2010-12-31 | New Years Eve | `early_close_eq1430_night_closed` - verbatim: “SFE: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | SFE2010 |

**Counts (27 rows):** day_closed=3, fully_closed=7, night_closes_midnight=7, day_and_night_normal=7, early_close_eq1430_night_closed=2, day_session_open=1.
- ONO (options-only) footnote rows in the same capture: night of Fri 25 Jan 2010 (Australia Day trade date Tue 26 Jan), Fri 23 Apr 2010 (ANZAC Day trade date Mon 26 Apr), Fri 11 Jun 2010 (Queen's Birthday trade date Mon 14 Jun) - bond ONOs unavailable; no SPI futures session change.
- Policy legend: Australian = Day Session Closed / Night Session Normal Trading Hours; US = Day Session Normal Trading Hours / Night Session to cease trading at midnight; International = Closed Day and Night Sessions.
- “Night Session to open at 5:10pm” is the SYCOM night session's normal open time - the same arrangement the legend calls “Night Session Normal Trading Hours” (mapped day_closed).

### 2011


Source: CAL2011a + CAL2011b
- **CAL2011a** = `wb_20101212100436_asx24_trading_calendar_2011.htm (capture 2010-12-12; covers Oct 2010 - Dec 2012)`
- **CAL2011b** = `wb_20110516085943_asx24-trading-calendar-2011.htm (capture 2011-05-16; covers Jan 2011 - Dec 2012)`

ASX 24 era - rows are prefixed “ASX 24:”; NZ family printed as a separate “NZ ASX 24” cell.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2011-01-03 | New Year's Day 'Holiday' | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2011a+CAL2011b |
| 2011-01-04 | Day after New Year's Day 'Holiday' (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2011a+CAL2011b |
| 2011-01-17 | Martin Luther King Day | `night_closes_midnight` - verbatim: “ASX 24: night session to cease trading at midnight” | CAL2011a+CAL2011b |
| 2011-01-26 | Australia Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | CAL2011a+CAL2011b |
| 2011-02-06 | Waitangi Day (NZ) | `fully_closed` - verbatim: “ASX 24: Non Trading Day”. Note: Sunday | CAL2011a+CAL2011b |
| 2011-02-21 | Presidents Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2011a+CAL2011b |
| 2011-04-21 | Day before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2011a+CAL2011b |
| 2011-04-22 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2011a+CAL2011b |
| 2011-04-25 | ANZAC Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2011a+CAL2011b |
| 2011-04-26 | Easter Monday Substitute Holiday | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to Open at 5:10pm (Sydney Time)”. Note: CAL2011a (Dec-2010 capture) printed “ASX 24: Closed”; corrected by the later CAL2011b capture (May-2011) | CAL2011b |
| 2011-05-30 | Memorial Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2011a+CAL2011b |
| 2011-06-06 | Queen’s Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2011a+CAL2011b |
| 2011-06-13 | Queen’s Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to Open at 5:10pm (Sydney Time)” | CAL2011a+CAL2011b |
| 2011-07-04 | Independence Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2011a+CAL2011b |
| 2011-08-01 | Bank Holiday | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2011a+CAL2011b |
| 2011-09-05 | Labour Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2011a+CAL2011b |
| 2011-10-03 | Labour Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2011a+CAL2011b |
| 2011-10-10 | Columbus Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2011a+CAL2011b |
| 2011-10-24 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2011a+CAL2011b |
| 2011-11-11 | Veteran’s Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2011a+CAL2011b |
| 2011-11-24 | Thanksgiving Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2011a+CAL2011b |
| 2011-12-23 | Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2011a+CAL2011b |
| 2011-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Non Trading Day”. Note: Sunday | CAL2011a+CAL2011b |
| 2011-12-26 | Christmas Day ‘Holiday’ | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2011a+CAL2011b |
| 2011-12-27 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2011a+CAL2011b |
| 2011-12-30 | Last Business Day before New Year’s Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2011a+CAL2011b |

**Counts (26 rows):** day_closed=3, fully_closed=7, night_closes_midnight=7, day_and_night_normal=7, early_close_eq1430_night_closed=2.
- Two duplicate captures exist for 2011 (CAL2011a captured 2010-12-12, CAL2011b captured 2011-05-16). A word-level diff of their IDO tables shows exactly one differing 2011 cell: 26 April (Easter Monday Substitute Holiday) - CAL2011a “Closed” vs CAL2011b “Day Session Closed / Night Session to Open at 5:10pm”. The later capture is used.
- ONO (options-only) footnote rows: Tue 25 Jan 2011 (Australia Day trade date Wed 26 Jan), Fri 10 Jun 2011 (Queen's Birthday NSW trade date Mon 13 Jun); plus 2012 dates. Bond ONOs unavailable; no SPI futures session change.

### 2012


Source: CAL2012
- **CAL2012** = `wb_20150906003836_asx24-trading-calendar-2012.htm (capture 2015-09-06; covers Jan 2012 - Dec 2013)`

ASX 24 era.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2012-01-02 | New Year’s Day 'Holiday' | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2012 |
| 2012-01-03 | New Year’s Day 'Holiday' (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2012 |
| 2012-01-16 | Martin Luther King Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2012 |
| 2012-01-26 | Australia Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to Open at 5:10pm (Sydney Time)” | CAL2012 |
| 2012-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2012 |
| 2012-02-20 | Presidents Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2012 |
| 2012-04-05 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2012 |
| 2012-04-06 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2012 |
| 2012-04-09 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2012 |
| 2012-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | CAL2012 |
| 2012-05-28 | Memorial Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2012 |
| 2012-06-04 | Queen’s Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2012 |
| 2012-06-11 | Queen’s Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to Open at 5:10pm (Sydney Time)” | CAL2012 |
| 2012-07-04 | Independence Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2012 |
| 2012-08-06 | Bank Holiday | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2012 |
| 2012-09-03 | Labour Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2012 |
| 2012-10-01 | Labour Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2012 |
| 2012-10-08 | Columbus Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2012 |
| 2012-10-22 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2012 |
| 2012-11-12 | Veteran’s Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2012 |
| 2012-11-22 | Thanksgiving (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2012 |
| 2012-12-24 | Christmas Eve | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2012 |
| 2012-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2012 |
| 2012-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2012 |
| 2012-12-31 | New Year’s Eve | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2012 |

**Counts (25 rows):** day_closed=3, fully_closed=5, night_closes_midnight=7, day_and_night_normal=8, early_close_eq1430_night_closed=2.
- The Jan-Dec 2012 rows printed in CAL2011a/CAL2011b match CAL2012 (only a case difference “open”/“Open” on 26 Jan 2012).
- ONO (options-only) footnote rows: Wed 25 Jan 2012, Tue 24 Apr 2012, Fri 8 Jun 2012 (plus 2013 dates).

### 2013


Source: CAL2013
- **CAL2013** = `wb_20131007091353_asx24-trading-calendar-2013.htm (capture 2013-10-07)`

ASX 24 era. This capture adds CFD-only sub-rows on some US-holiday rows (CFD family is not the SPI family).

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2013-01-01 | New Year's Day 'Holiday' | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2013 |
| 2013-01-02 | Day after New Year's Day 'Holiday' (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2013 |
| 2013-01-21 | Martin Luther King Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight”. Note: CFD-only extra rows: “CFD ASX 24 - IU - Closed”, “CFD ASX - IQ - Day Session Open, Night Session Closed” | CAL2013 |
| 2013-01-28 | Australia Day | `day_closed` - verbatim: “Day Session Closed / Night Session to open at 5:10pm (Sydney Time)”. Note: ASX 24 prefix omitted on this row in the capture; NZ cell: “Normal Trading Day” | CAL2013 |
| 2013-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours”. Note: NZ cell reads “Non Trading Day” in this capture | CAL2013 |
| 2013-02-18 | Presidents Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2013 |
| 2013-03-28 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2013 |
| 2013-03-29 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2013 |
| 2013-04-01 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2013 |
| 2013-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | CAL2013 |
| 2013-05-27 | Memorial Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2013 |
| 2013-06-03 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2013 |
| 2013-06-10 | Queen's Birthday (ex WA) | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | CAL2013 |
| 2013-07-04 | Independence Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2013 |
| 2013-08-26 | Bank Holiday (NSW) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2013 |
| 2013-09-02 | Labour Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight / Night session to cease trading at midnight (Sydney Time)”. Note: “NZ ASX 24” prefix missing on the second line in the capture | CAL2013 |
| 2013-10-07 | Labour Day NSW | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2013 |
| 2013-10-14 | Columbus Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours”. Note: CFD-only extra rows present | CAL2013 |
| 2013-10-28 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2013 |
| 2013-11-11 | Veteran's Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours”. Note: CFD-only extra rows present | CAL2013 |
| 2013-11-28 | Thanksgiving (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2013 |
| 2013-12-24 | Christmas Eve / Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed; CFD ASX 24: CFD products to close at 2:00pm (Sydney Time), Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2013 |
| 2013-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2013 |
| 2013-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2013 |
| 2013-12-31 | New Year's Eve / Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed; CFD ASX 24: CFD products to close at 2:00pm (Sydney Time), Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2013 |

**Counts (25 rows):** day_closed=3, fully_closed=5, night_closes_midnight=7, day_and_night_normal=8, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows: Fri 25 Jan 2013, Wed 24 Apr 2013, Fri 7 Jun 2013.
- CAL2012's 2013 rows agree with CAL2013 on every ASX 24 cell (CAL2012 omits the CFD sub-rows and the occasional wording quirks).

### 2014


Source: CAL2014
- **CAL2014** = `wb_20131223094428_asx24-trading-calendar-2014.htm (capture 2013-12-23; covers 2014 + 1 Jan 2015)`

ASX 24 era.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2014-01-01 | New Year's Day 'Holiday' | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2014 |
| 2014-01-02 | Day after New Year's Day 'Holiday' (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2014 |
| 2014-01-20 | Martin Luther King Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2014 |
| 2014-01-27 | Australia Day 'Holiday' | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | CAL2014 |
| 2014-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2014 |
| 2014-02-17 | Presidents Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2014 |
| 2014-04-17 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2014 |
| 2014-04-18 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2014 |
| 2014-04-21 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2014 |
| 2014-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | CAL2014 |
| 2014-05-26 | Memorial Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2014 |
| 2014-06-02 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2014 |
| 2014-06-09 | Queen's Birthday (ex WA) | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | CAL2014 |
| 2014-07-04 | Independence Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2014 |
| 2014-08-04 | Bank Holiday (NSW) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2014 |
| 2014-09-01 | Labour Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2014 |
| 2014-10-06 | Labour Day NSW | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2014 |
| 2014-10-13 | Columbus Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2014 |
| 2014-10-27 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2014 |
| 2014-11-11 | Veteran's Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2014 |
| 2014-11-27 | Thanksgiving (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2014 |
| 2014-12-24 | Christmas Eve / Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2014 |
| 2014-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2014 |
| 2014-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2014 |
| 2014-12-31 | New Year's Eve / Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2014 |

**Counts (25 rows):** day_closed=3, fully_closed=5, night_closes_midnight=7, day_and_night_normal=8, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows: Fri 24 Jan 2014, Thu 24 Apr 2014, Fri 6 Jun 2014.

### 2015


Source: CAL2015
- **CAL2015** = `wb_20141130043626_asx24-trading-calendar-2015.htm (capture 2014-11-30; covers 2015 + 1 Jan 2016)`

ASX 24 era.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2015-01-01 | New Year's Day 'Holiday' | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2015 |
| 2015-01-02 | Day after New Year's Day 'Holiday' (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2015 |
| 2015-01-19 | Martin Luther King Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2015 |
| 2015-01-26 | Australia Day 'Holiday' | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | CAL2015 |
| 2015-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2015 |
| 2015-02-16 | Presidents Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2015 |
| 2015-04-02 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2015 |
| 2015-04-03 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2015 |
| 2015-04-06 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2015 |
| 2015-04-27 | ANZAC Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours”. Note: capture footnote: “ANZAC Day falls on Saturday 25 April, 2015, with no substitute holiday declared in Australia. Normal trading hours apply for ASX 24. Day session closed for NZ ASX 24.”; NZ cell: Non Trading Day, Night to open 3:40pm | CAL2015 |
| 2015-05-25 | Memorial Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2015 |
| 2015-06-01 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2015 |
| 2015-06-08 | Queen's Birthday (ex WA) | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)” | CAL2015 |
| 2015-07-03 | Independence Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2015 |
| 2015-08-03 | Bank Holiday (NSW) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2015 |
| 2015-09-07 | Labour Day (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2015 |
| 2015-10-05 | Labour Day NSW | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2015 |
| 2015-10-12 | Columbus Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2015 |
| 2015-10-26 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2015 |
| 2015-11-11 | Veteran's Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2015 |
| 2015-11-26 | Thanksgiving (US) | `night_closes_midnight` - verbatim: “ASX 24: Night session to cease trading at midnight” | CAL2015 |
| 2015-12-24 | Christmas Eve / Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close at 14:15pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2015 |
| 2015-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2015 |
| 2015-12-28 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2015 |
| 2015-12-31 | New Year's Eve / Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close at 14:15pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2015 |

**Counts (25 rows):** day_closed=2, fully_closed=5, night_closes_midnight=7, day_and_night_normal=9, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows: Fri 23 Jan 2015, Fri 5 Jun 2015; ONO note repeats: ANZAC Day fell Saturday 25 April 2015, no substitute holiday in Australia, “Normal SFE trading hours”.

### 2016


Source: CAL2016
- **CAL2016** = `wb_20151120050041_asx24-trading-calendar-2016.htm (capture 2015-11-20; covers 2016 + 2 Jan 2017)`

ASX 24 era; capture taken 2015-11-20. US holidays from 2016 carry no midnight close - both sessions normal.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2016-01-01 | New Year's Day 'Holiday' | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2016 |
| 2016-01-04 | Day after New Year's Day 'Holiday' (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-01-18 | Martin Luther King Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-01-26 | Australia Day 'Holiday' | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:00pm (Sydney Time)”. Note: verbatim 5:00pm (post-Feb-2016 normal night open) | CAL2016 |
| 2016-02-08 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-02-15 | Presidents Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-03-24 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2016 |
| 2016-03-25 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2016 |
| 2016-03-28 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2016 |
| 2016-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:00pm (Sydney Time)”. Note: verbatim 5:00pm | CAL2016 |
| 2016-05-30 | Memorial Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-06-06 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-06-13 | Queen's Birthday (ex WA) | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session to open at 5:10pm (Sydney Time)”. Note: capture prints 5:10pm here, inconsistent with the 5:00pm rows of Jan/Apr - verbatim | CAL2016 |
| 2016-07-04 | Independence Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-08-01 | Bank Holiday (NSW) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-09-05 | Labour Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-10-03 | Labour Day NSW | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-10-10 | Columbus Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-10-24 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-11-11 | Veteran's Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-11-24 | Thanksgiving Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2016 |
| 2016-12-23 | Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close at 14:15pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2016 |
| 2016-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2016 |
| 2016-12-27 | Christmas Day Holiday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2016 |
| 2016-12-30 | Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close at 14:15pm (Sydney Time); Interest Rate, Energy, Environmental and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2016 |

**Counts (25 rows):** day_closed=3, fully_closed=5, night_closes_midnight=1, day_and_night_normal=14, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows: Mon 25 Jan 2016, Fri 22 Apr 2016, Fri 10 Jun 2016.

### 2017


Source: CAL2017
- **CAL2017** = `wb_20170103192507_asx24-trading-calendar-2017.htm (capture 2017-01-03)`

ASX 24 era, “DATES FOR 2017” format; day-holiday rows print “Night Session Normal Trading Hours”.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2017-01-02 | New Year's Day "Holiday" | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2017 |
| 2017-01-03 | Day after New Year's Day "Holiday" (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2017 |
| 2017-01-26 | Australia Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2017 |
| 2017-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2017 |
| 2017-02-20 | Presidents Day (US) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2017 |
| 2017-04-13 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2017 |
| 2017-04-14 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2017 |
| 2017-04-17 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2017 |
| 2017-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2017 |
| 2017-06-05 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2017 |
| 2017-06-12 | Queen's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2017 |
| 2017-10-23 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2017 |
| 2017-12-22 | Last Business Day before Christmas Day | `day_normal_night_closed` - verbatim: “ASX 24: Day Session Normal Trading Hours / Night Session Closed”. Note: no product-level early close stated (unlike 2015-2016); NZ same | CAL2017 |
| 2017-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2017 |
| 2017-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2017 |
| 2017-12-29 | Last Business Day before New Year's Day | `day_normal_night_closed` - verbatim: “ASX 24: Day Session Normal Trading Hours / Night Session Closed”. Note: no product-level early close stated | CAL2017 |

**Counts (16 rows):** day_closed=3, fully_closed=5, night_closes_midnight=1, day_and_night_normal=5, day_normal_night_closed=2.
- ONO (options-only) footnote rows: Wed 25 Jan 2017, Mon 24 Apr 2017, Fri 9 Jun 2017.

### 2018


Source: CAL2018
- **CAL2018** = `wb_20171222063723_asx24-trading-calendar-2018.htm (capture 2017-12-22)`

ASX 24 era, “DATES FOR 2018” format.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2018-01-01 | New Year's Day "Holiday" | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2018 |
| 2018-01-02 | Day after New Year's Day "Holiday" (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2018 |
| 2018-01-26 | Australia Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2018 |
| 2018-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2018 |
| 2018-03-29 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2018 |
| 2018-03-30 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2018 |
| 2018-04-02 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2018 |
| 2018-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2018 |
| 2018-06-04 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2018 |
| 2018-06-11 | Queen's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2018 |
| 2018-10-22 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2018 |
| 2018-12-24 | Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close 14:15pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2018 |
| 2018-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2018 |
| 2018-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2018 |
| 2018-12-31 | Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close 14:15pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2018 |

**Counts (15 rows):** day_closed=3, fully_closed=5, night_closes_midnight=1, day_and_night_normal=4, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows present in capture (Australia Day, ANZAC Day, Queen's Birthday eves).

### 2019


Source: CAL2019
- **CAL2019** = `wb_20190821020021_asx24-trading-calendar-2019.htm (capture 2019-08-21)`

ASX 24 era, “DATES FOR 2019” format.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2019-01-01 | New Year's Day "Holiday" | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2019 |
| 2019-01-02 | Day after New Year's Day "Holiday" (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2019 |
| 2019-01-28 | Australia Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2019 |
| 2019-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2019 |
| 2019-04-18 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2019 |
| 2019-04-19 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2019 |
| 2019-04-22 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2019 |
| 2019-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2019 |
| 2019-06-03 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2019 |
| 2019-06-10 | Queen's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2019 |
| 2019-10-28 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2019 |
| 2019-12-24 | Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close 14:15pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2019 |
| 2019-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2019 |
| 2019-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2019 |
| 2019-12-31 | Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close 14:15pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2019 |

**Counts (15 rows):** day_closed=3, fully_closed=5, night_closes_midnight=1, day_and_night_normal=4, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows: Fri 25 Jan 2019, Wed 24 Apr 2019, Fri 7 Jun 2019.

### 2020


Source: CAL2020 (+ LIVE2010 for 27 April)
- **CAL2020** = `wb_20191022200826_asx24-trading-calendar-2020.htm (capture 2019-10-22)`
- **LIVE2010** = `wb_20201022124434_asx24_trading_calendar_live.htm (capture 2020-10-22; holds 2020 + 2021 tables)`

ASX 24 era, “DATES FOR 2020” format.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2020-01-01 | New Year's Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2020 |
| 2020-01-02 | Day after New Year's Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2020 |
| 2020-01-27 | Australia Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2020 |
| 2020-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2020 |
| 2020-04-09 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | CAL2020 |
| 2020-04-10 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2020 |
| 2020-04-13 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2020 |
| 2020-04-25 | ANZAC Day | `fully_closed` - verbatim: “ASX 24: Closed”. Note: Saturday | CAL2020 |
| 2020-04-27 | ANZAC Day (Observed in NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Open”. Note: row present only in the Oct-2020 live capture (absent from CAL2020) | LIVE2010 |
| 2020-06-01 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2020 |
| 2020-06-08 | Queen's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / Night Session Normal Trading Hours” | CAL2020 |
| 2020-10-26 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | CAL2020 |
| 2020-12-24 | Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close 14:15pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); NZ ASX 24: Interest Rate and Energy Products to close 10:00am (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2020 |
| 2020-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2020 |
| 2020-12-28 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | CAL2020 |
| 2020-12-31 | Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); VIX to close 14:15pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); NZ ASX 24: Interest Rate and Energy Products to close 10:00am (Sydney Time); Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | CAL2020 |

**Counts (16 rows):** day_closed=2, fully_closed=6, night_closes_midnight=1, day_and_night_normal=5, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows: Fri 24 Jan 2020, Fri 5 Jun 2020.

### 2021


Source: LIVE2101 (also in LIVE2010 and LIVE2207)
- **LIVE2010** = `wb_20201022124434_asx24_trading_calendar_live.htm (capture 2020-10-22; holds 2020 + 2021 tables)`
- **LIVE2101** = `wb_20210117034448_asx24_trading_calendar_live.htm (capture 2021-01-17; holds 2021 table)`
- **LIVE2207** = `wb_20220703182752_asx24_trading_calendar_live.htm (capture 2022-07-03; holds 2022 + 2021 tables)`

ASX 24 era.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2021-01-01 | New Year's Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2101 |
| 2021-01-04 | Day after New Year's Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2101 |
| 2021-01-26 | Australia Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2101 |
| 2021-02-08 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2101 |
| 2021-04-01 | Day Before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | LIVE2101 |
| 2021-04-02 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2101 |
| 2021-04-05 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2101 |
| 2021-04-25 | ANZAC Day | `fully_closed` - verbatim: “ASX 24: Closed”. Note: Sunday | LIVE2101 |
| 2021-04-26 | ANZAC Day substitute (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal trading hours” | LIVE2101 |
| 2021-06-07 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2101 |
| 2021-06-14 | Queen's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2101 |
| 2021-10-25 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2101 |
| 2021-12-24 | Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30 pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); ASX 24/NZ: Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | LIVE2101 |
| 2021-12-27 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2101 |
| 2021-12-28 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2101 |
| 2021-12-31 | Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30 pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); ASX 24/NZ: Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | LIVE2101 |

**Counts (16 rows):** day_closed=2, fully_closed=6, night_closes_midnight=1, day_and_night_normal=5, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows: Mon 25 Jan 2021, Fri 11 Jun 2021.
- The 2021 table is identical in LIVE2010 (Oct 2020 capture), LIVE2101 (Jan 2021) and LIVE2207 (Jul 2022).

### 2022


Source: LIVE2207 (revised by LIVE2212)
- **LIVE2207** = `wb_20220703182752_asx24_trading_calendar_live.htm (capture 2022-07-03; holds 2022 + 2021 tables)`
- **LIVE2212** = `wb_20221225022559_asx24_trading_calendar_live.htm (capture 2022-12-25; holds 2023 + 2022 tables)`

ASX 24 era, “2022 holiday schedule for ASX24 products”.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2022-01-03 | New Year's Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2207 |
| 2022-01-04 | Day after New Year's Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2207 |
| 2022-01-26 | Australia Day holiday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2207 |
| 2022-02-07 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2207 |
| 2022-04-14 | Day before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | LIVE2207 |
| 2022-04-15 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2207 |
| 2022-04-18 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2207 |
| 2022-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2207 |
| 2022-06-06 | Queen's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2207 |
| 2022-06-13 | Queen's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2207 |
| 2022-06-24 | Matariki (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours”. Note: first Matariki holiday | LIVE2207 |
| 2022-09-22 | National Day of Mourning for Her Majesty the Queen | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours”. Note: absent from the Jul-2022 capture (LIVE2207); added in the Dec-2022 capture after the proclamation | LIVE2212 |
| 2022-09-26 | National Day of Mourning for Her Majesty the Queen (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours”. Note: absent from LIVE2207 | LIVE2212 |
| 2022-10-24 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2207 |
| 2022-12-23 | Last Business Day before Christmas Day | `day_normal_night_closed` - verbatim: “ASX 24: Day Session Normal Trading Hours / ASX 24: Night Session Closed”. Note: LIVE2207 printed “ASX 24: Normal Trading Hours” (no night closure); revised in the Dec-2022 capture | LIVE2212 |
| 2022-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2207 |
| 2022-12-27 | Christmas Day substitute | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2207 |
| 2022-12-30 | Last Business Day before New Year's Day | `day_normal_night_closed` - verbatim: “ASX 24: Day Session Normal Trading Hours / ASX 24: Night Session Closed”. Note: LIVE2207 printed “ASX 24: Normal Trading Hours”; revised in the Dec-2022 capture | LIVE2212 |

**Counts (18 rows):** day_closed=4, fully_closed=5, night_closes_midnight=1, day_and_night_normal=6, day_normal_night_closed=2.
- ONO (options-only) footnote rows: Tue 25 Jan 2022, Fri 22 Apr 2022, Fri 10 Jun 2022.

### 2023


Source: LIVE2212 (identical 2023 table in LIVE2312)
- **LIVE2212** = `wb_20221225022559_asx24_trading_calendar_live.htm (capture 2022-12-25; holds 2023 + 2022 tables)`
- **LIVE2312** = `wb_20231211225115_asx24_trading_calendar_live.htm (capture 2023-12-11; holds 2024 + 2023 tables)`

ASX 24 era.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2023-01-02 | New Year's Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2212 |
| 2023-01-03 | Day after New Year's Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2212 |
| 2023-01-26 | Australia Day holiday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2212 |
| 2023-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2212 |
| 2023-04-06 | Day before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | LIVE2212 |
| 2023-04-07 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2212 |
| 2023-04-10 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2212 |
| 2023-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2212 |
| 2023-06-05 | King's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours”. Note: first King's Birthday (NZ) | LIVE2212 |
| 2023-06-12 | King's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours”. Note: first King's Birthday (AU) | LIVE2212 |
| 2023-07-14 | Matariki (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2212 |
| 2023-10-23 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2212 |
| 2023-12-22 | Last Business Day before Christmas Day | `day_normal_night_closed` - verbatim: “ASX 24: Day Session Normal Trading Hours / ASX 24: Night Session Closed” | LIVE2212 |
| 2023-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2212 |
| 2023-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2212 |
| 2023-12-29 | Last Business Day before New Year's Day | `day_normal_night_closed` - verbatim: “ASX 24: Day Session Normal Trading Hours / ASX 24: Night Session Closed” | LIVE2212 |

**Counts (16 rows):** day_closed=3, fully_closed=5, night_closes_midnight=1, day_and_night_normal=5, day_normal_night_closed=2.
- ONO (options-only) footnote rows: Wed 25 Jan 2023, Mon 24 Apr 2023, Fri 9 Jun 2023.

### 2024

**Capture status:** All direct 2024 captures (wb_20240207120927, wb_20240311055832, wb_20240317201155, wb_20240530023509, wb_20240804213819, wb_20240810062830, wb_20241016192729, wb_20241107053705) are Incapsula bot-block pages (212-944 bytes) and unreadable; 2024 data comes from the Dec-2023 capture of the live calendar.


Source: LIVE2312
- **LIVE2312** = `wb_20231211225115_asx24_trading_calendar_live.htm (capture 2023-12-11; holds 2024 + 2023 tables)`

ASX 24 era, “Dates for 2024”.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2024-01-01 | New Year's Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2312 |
| 2024-01-02 | Day after New Year's Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2312 |
| 2024-01-26 | Australia Day holiday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2312 |
| 2024-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2312 |
| 2024-03-28 | Day before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | LIVE2312 |
| 2024-03-29 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2312 |
| 2024-04-01 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2312 |
| 2024-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2312 |
| 2024-06-03 | King's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2312 |
| 2024-06-10 | King's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2312 |
| 2024-06-28 | Matariki (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2312 |
| 2024-10-28 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2312 |
| 2024-12-24 | Last Business Day before Christmas Day | `day_normal_night_closed` - verbatim: “ASX 24: Day Session Normal Trading Hours / ASX 24: Night Session Closed” | LIVE2312 |
| 2024-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2312 |
| 2024-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2312 |
| 2024-12-31 | Last Business Day before New Year's Day | `day_normal_night_closed` - verbatim: “ASX 24: Day Session Normal Trading Hours / ASX 24: Night Session Closed” | LIVE2312 |

**Counts (16 rows):** day_closed=3, fully_closed=5, night_closes_midnight=1, day_and_night_normal=5, day_normal_night_closed=2.
- ONO (options-only) footnote rows: Thu 25 Jan 2024, Wed 24 Apr 2024, Fri 7 Jun 2024.

### 2025


Source: LIVE2503
- **LIVE2503** = `wb_20250316225953_asx24_trading_calendar_live.htm (capture 2025-03-16; holds 2025 table)`

ASX 24 era, “Dates for 2025”. The capture holds no 2026 dates table.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2025-01-01 | New Year's Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2503 |
| 2025-01-02 | Day after New Year's Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2503 |
| 2025-01-27 | Australia Day holiday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2503 |
| 2025-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2503 |
| 2025-04-17 | Day before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | LIVE2503 |
| 2025-04-18 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2503 |
| 2025-04-21 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2503 |
| 2025-04-25 | ANZAC Day | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2503 |
| 2025-06-02 | King's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2503 |
| 2025-06-09 | King's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVE2503 |
| 2025-06-20 | Matariki (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2503 |
| 2025-10-27 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVE2503 |
| 2025-12-24 | Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); ASX 24 / NZ: Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | LIVE2503 |
| 2025-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2503 |
| 2025-12-26 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVE2503 |
| 2025-12-31 | Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); ASX 24 / NZ: Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | LIVE2503 |

**Counts (16 rows):** day_closed=3, fully_closed=5, night_closes_midnight=1, day_and_night_normal=5, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows: Fri 24 Jan 2025, Thu 24 Apr 2025, Fri 6 Jun 2025.
- Dec-2024 rows in LIVE2312 said Day-normal/Night-closed; Dec-2025 rows return to the product-level early close (equity 2:30pm) - verbatim as captured.

### 2026


Source: LIVECUR
- **LIVECUR** = `live_asx24_trading_calendar.html (live page fetched 2026-10-11; holds 2026 + 2027 tables)`

ASX 24 era, “Dates for 2026”.

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2026-01-01 | New Year's Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVECUR |
| 2026-01-02 | Day after New Year's Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVECUR |
| 2026-01-26 | Australia Day holiday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVECUR |
| 2026-02-06 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVECUR |
| 2026-04-02 | Day before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: Night Session to cease trading at midnight” | LIVECUR |
| 2026-04-03 | Good Friday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVECUR |
| 2026-04-06 | Easter Monday | `fully_closed` - verbatim: “ASX 24: Closed” | LIVECUR |
| 2026-04-27 | ANZAC Day | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours / ASX 24: Night Session Normal Trading Hours”. Note: ANZAC Day falls Saturday 25 April 2026; the table gives no 25-April row and no Australian substitute day session closure - only the NZ-observed Monday carries an arrangement (NZ day closed) | LIVECUR |
| 2026-06-01 | King's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVECUR |
| 2026-06-08 | King's Birthday | `day_closed` - verbatim: “ASX 24: Day Session Closed / ASX 24: Night Session Normal Trading Hours” | LIVECUR |
| 2026-07-10 | Matariki (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVECUR |
| 2026-10-26 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: Normal Trading Hours” | LIVECUR |
| 2026-12-24 | Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); ASX 24 / NZ: Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | LIVECUR |
| 2026-12-25 | Christmas Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVECUR |
| 2026-12-28 | Boxing Day | `fully_closed` - verbatim: “ASX 24: Closed” | LIVECUR |
| 2026-12-31 | Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); ASX 24 / NZ: Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | LIVECUR |

**Counts (16 rows):** day_closed=2, fully_closed=5, night_closes_midnight=1, day_and_night_normal=6, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows for 2026: Fri 23 Jan 2026, Fri 5 Jun 2026 - no April ONO entry, consistent with the absent 25-April row.

### 2027


Source: LIVECUR
- **LIVECUR** = `live_asx24_trading_calendar.html (live page fetched 2026-10-11; holds 2026 + 2027 tables)`

ASX 24 era, “Dates for 2027” (cells in lower case in this table - verbatim preserved).

| ISO date | occasion | arrangement | source |
|---|---|---|---|
| 2027-01-01 | New Year's Day | `fully_closed` - verbatim: “ASX 24: closed” | LIVECUR |
| 2027-01-04 | Day after New Year's Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: normal trading hours” | LIVECUR |
| 2027-01-26 | Australia Day holiday | `day_closed` - verbatim: “ASX 24: day session closed / ASX 24: night session normal trading hours” | LIVECUR |
| 2027-02-08 | Waitangi Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: normal trading hours” | LIVECUR |
| 2027-03-25 | Day before Good Friday | `night_closes_midnight` - verbatim: “ASX 24: night session to cease trading at midnight” | LIVECUR |
| 2027-03-26 | Good Friday | `fully_closed` - verbatim: “ASX 24: closed” | LIVECUR |
| 2027-03-29 | Easter Monday | `fully_closed` - verbatim: “ASX 24: closed” | LIVECUR |
| 2027-04-26 | ANZAC Day (*NSW substitute only) | `day_and_night_normal`\* - verbatim: “ASX 24: normal trading hours / ASX 24: night session normal trading hours”. Note: ANZAC Day falls Sunday 25 April 2027; no 25-April row; Monday 26 April is the NSW-only substitute - ASX 24 normal; NZ day closed | LIVECUR |
| 2027-06-07 | King's Birthday (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: normal trading hours” | LIVECUR |
| 2027-06-14 | King's Birthday | `day_closed` - verbatim: “ASX 24: day session closed / ASX 24: night session normal trading hours” | LIVECUR |
| 2027-06-25 | Matariki (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: normal trading hours” | LIVECUR |
| 2027-10-25 | Labour Day (NZ) | `day_and_night_normal`\* - verbatim: “ASX 24: normal trading hours” | LIVECUR |
| 2027-12-24 | Last Business Day before Christmas Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); ASX 24 / NZ: Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | LIVECUR |
| 2027-12-27 | Christmas Day | `fully_closed` - verbatim: “ASX 24: closed” | LIVECUR |
| 2027-12-28 | Boxing Day | `fully_closed` - verbatim: “ASX 24: closed” | LIVECUR |
| 2027-12-31 | Last Business Day before New Year's Day | `early_close_eq1430_night_closed` - verbatim: “ASX 24: Equity Products to close at 2:30pm (Sydney Time); Interest Rate, Energy and Agriculture Products to close at 12:30pm (Sydney Time); ASX 24 / NZ: Night Session Closed”. Note: early close; equity leg is the SPI-relevant one (generic products row) | LIVECUR |

**Counts (16 rows):** day_closed=2, fully_closed=5, night_closes_midnight=1, day_and_night_normal=6, early_close_eq1430_night_closed=2.
- ONO (options-only) footnote rows for 2027: Mon 25 Jan 2027, Fri 11 Jun 2027.

## Grand totals 2010-2027
day_closed=50, fully_closed=96, night_closes_midnight=54, day_and_night_normal=117, early_close_eq1430_night_closed=28, day_normal_night_closed=8, day_session_open=1; total rows=354.

