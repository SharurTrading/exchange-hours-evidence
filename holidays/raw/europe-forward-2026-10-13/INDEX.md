# Europe forward-publication wave — 2026-10-13/14 UTC

Fourth forward-monitoring sweep over the European operators (after the
2026-09-27/28/29 wave, the 2026-10-02/03 re-checks and the 2026-10-09/10/11
negatives). Eight operators were read live on 2026-10-13 23:27–23:35 UTC; every
artifact below is the operator's own page or machine channel, saved with its
sha256 in `SHA256SUMS.txt`. Crate-side baselines were read from
`exchange-hours-rs` main (docs/evidence + holiday tables) before each check.

## Per-operator verdicts

### LSE — 2028 rows are now published (NEW)

The live business-days API
(`api.londonstockexchange.com/api/v1/pages?path=equities-trading/business-days`)
now prints a 27-row table running **2026-08-31 through 2029-01-01**. The
shipped table (`lse.rs`) cites `LSE-BUSDAYS-2025-12-18` (the 2025-12-18
capture) and its audited window ends **2027-12-31**. Row-by-row:

- **2026 rows — no diffs.** 2026-08-31 Summer Bank Holiday (closed),
  2026-12-24 half day (12:30 London), 2026-12-25, 2026-12-28 (substitute),
  2026-12-31 half day — every cell matches the shipped rows byte for byte.
- **2027 rows — no diffs.** 2027-01-01, 2027-03-26, 2027-03-29, 2027-05-03,
  2027-05-31, 2027-08-30, 2027-12-24 half day, 2027-12-27 (substitute),
  2027-12-28 (substitute), 2027-12-31 half day — all ten match.
- **NEW — 2028 (10 rows) and 2029-01-01, printed with the same session
  language as prior years** (`NON-trading day. Also GBX/GBP NON-settlement
  day in EUI` / `Markets closing process commences from 12:30 London time.
  Standard settlement day.`):
  - 2028-01-03 New Year's Day (substitute) — closed (2028-01-01 is a Sunday)
  - 2028-04-14 Good Friday — closed
  - 2028-04-17 Easter Monday — closed
  - 2028-05-01 Early May Bank Holiday — closed
  - 2028-05-29 Spring Bank Holiday — closed
  - 2028-08-28 Summer Bank Holiday — closed
  - 2028-12-22 Christmas Holiday half day — early close 12:30 London
  - 2028-12-25 Christmas Day — closed
  - 2028-12-26 Boxing Day — closed (its EUI service cell reads `To be
    confirmed`; that column is service availability, not the trading
    arrangement, which prints `NON-trading day.`)
  - 2028-12-29 New Year's Holiday half day — early close 12:30 London
  - 2029-01-01 New Year's Day — closed

  Full live row list: `lse/lse_live_rows_extraction-20261013.txt`.

### Nasdaq — still 2026-only (negative)

The `nasdaqtrader.com` calendar page still answers its Incapsula JS challenge
to a plain client (HTTP 200 challenge stub, byte-identical sha256
`d0203228…` to the 2026-10-03 stub); rendered through the public reader it
carries `U.S. Equity and Options Markets Holiday Schedule 2026` and zero 2027
dates. The `nasdaq.com` holiday-schedule page was fetched directly this time
(the table is server-rendered in its HTML): twelve 2026 rows whose cells match
the shipped `nasdaq.rs` 2026 rows exactly (nine closures plus 2026-11-27 and
2026-12-24 early closes at 1:00 p.m. ET), zero `2027` strings anywhere in the
174 KB page. No errata. Closing condition unchanged: the operator's 2027
schedule page.

### ICE Futures U.S. — no new holiday notice (negative)

The T2 notices listing service (POST
`/api/sitesearchservice/v1/search/websitenotices?searchCollections=futures_us_exchange_notice`)
answers 123 notices for 2026 and **zero for 2027**. The newest 2026 notices
since the crate's 2026-10-09 re-check are listing/margin items (2026-10-13
livestock listing, 2026-10-05 margin and product-delay, 2026-10-02 spot-month
reminder) — none holiday- or hours-related. The 2026 Christmas/Boxing Day
hours notice has still not issued, so `IFUS-CAL-2026`'s 2026-12-28 `open1`
cell keeps withholding; the 2027 calendar ships already (`IFUS-CAL-2027`) and
nothing supersedes it.

### ICE Futures Europe — editions unchanged since the August baseline; Excel carries preliminary 2027 (no diff)

The market-resources page links the same four schedule documents. The
Oil/Utilities/Agricultural schedule PDF was created 2026-07-14 (the July
edition); the Fixed Income/Equity & Indices (Migrated Liffe contracts)
schedule PDF was created 2026-08-13 (`pdf:Keywords` `July 2026`) — the
August-2026 baseline, nothing newer. The Excel trading schedule
(`Excel_Trading_Schedule.xlsx`, workbook created/modified 2026-07-08, "Last
Updated" serial 46211 = 2026-07-08) carries its calendar to **2027**, with the
operator's own note that beyond-PDF dates "should be taken as preliminary
unless otherwise" — so its 2027 cells are preliminary under the operator's
own label and key no row (LAW-NO-FABRICATED-DATES). The Change Tracker's
newest entries (tail extracted to `iceeu/iceeu_change_tracker_tail-20261013.txt`):
2026-02-11 "2025 removed (2027 added)"; 2026-04-13 Japanese Power settlement
window (circular 26051) and all-Utilities extended trading hours (circular
26006); 2026-05-06 CORSIA options (26049), the European/Global Interest Rates
renames (26056), Christmas/New Year's Eve settlement change (26045);
2026-06-17 TONA regular close 22:00 London; undated new-products entries
(circular 26075) and Gilt/SONIA extended hours (circular 26063). None touches
the Brent scope the `iceeu`/commodities identities serve.

### Eurex — TC 2027 still unpublished; the 2027 conflict stands; TC 2026 byte-identical (negative)

The Trading Calendar archive page still contains the string `2027` zero times
and still links `tradingcalendar_2026_en.pdf` as its newest edition. The
`Holiday regulations` page still prints its `Non-trading days at Eurex
2026 - 2030` table with the 2027 column uncaveated (New Year Friday
01 Jan 2027, Good Friday 26 Mar 2027, Easter Monday 29 Mar 2027, Labour Day
Saturday 01 May 2027, Christmas Eve Friday 24 Dec 2027, Christmas Day
Saturday 25 Dec 2027, Boxing Day Sunday 26 Dec 2027, New Year's Eve Friday
31 Dec 2027; the five `preliminar/indicativ` matches on the page are all
navigation links) while the `Indicative trading calendars` page still opens
"provided on a preliminary and indicative basis for the years 2027 to 2036 …
and are subject to change". The conflict recorded in the crate's evidence
stands; coverage stops at 2026-12-31 and the closing condition (a Trading
Calendar 2027 edition, or the preliminary label dropped) is still open. The
TC 2026 PDF re-downloaded **byte-identical** (sha256 `b0796b42…`, equal to the
crate's cited digest), so the Swiss-scope lines the SMI family reads carry no
errata.

### Euronext — 2027 still unpublished (negative)

The live trading-hours-and-holidays page carries only the 2026 calendar (one
21-row table, all seven market columns); every one of its 24 `2027` strings
is "Innovate for Growth 2027" strategy material. The page still links only
the **2025** end-of-year appendix (`/media/14656/download`), so the two
`Unsourced` 2026-eve rows (2026-12-24, 2026-12-31) keep their closing
condition. The 2026 table cells agree with the shipped arrangement (Paris:
closures 01-01, 04-03, 04-06, 05-01, 12-25; half days 12-24 and 12-31). No
2027 calendar rows, no errata. Closing condition unchanged: Euronext's 2027
calendar.

### BME / MEFF — no 2026 horarios timetable, no 2027 calendar (negative)

The public Regulation Renta Variable index (4 587 document URLs, retrieved
live) contains: the newest session-calendar instruction remains
`2025-65-io-calendario-de-sesiones-2026.pdf`; **no** `2026-…-horarios-24-y-31`
detailed timetable for the two 2026 eves (the 2024 and 2025 editions were
`2024-47-io-horarios-24-y-31.pdf` and `2025-64-io-horarios-24-y-31.pdf`,
both issued late in their year); and **zero** paths or titles mentioning 2027.
The two `Unsourced` 2026-eve rows and the 2026-12-31 window end stand; both
closing conditions (the detailed 2026 `ACCIONES (EQ)` timetable; the 2027
annual cash calendar) are still open. MEFF's own calendar page
(`meff.es/esp/Calendario`) carries 2026 only, no 2027 link — recorded as
context for the moved-domain watch note; the crate's `bme` family is the SIBE
cash scope and inherits nothing from MEFF.

### SIX Swiss Exchange — no change; withdrawn URLs restored byte-identically (negative)

The `trading-guides/` 2026 and 2027 trading-calendar PDF URLs, which answered
the operator's 404 page at the 2026-10-03 re-check, are **serving again** and
their bytes are **byte-identical** to the shipped artifacts: 2026 sha256
`70d1b87d…` and 2027 sha256 `cd2fdca6…`, both equal to the crate's cited
`SIX-TC-2026`/`SIX-TC-2027` digests. No 2028 edition exists (`trading-guides/`
and `trading-guides-upcoming/` both 404). The horizon stays 2027-12-31; this
is a watch-channel restoration, not a data change.

## Artifacts

All bytes retrieved 2026-10-13 23:27–23:35 UTC from the operator channels
below; sha256 in `SHA256SUMS.txt`.

| File | URL | Retrieved (UTC) |
|---|---|---|
| `lse/lse_business_days_api.live-20261013T232722Z.html` | <https://api.londonstockexchange.com/api/v1/pages?path=equities-trading/business-days&parameters=> | 2026-10-13 23:27 |
| `lse/lse_live_rows_extraction-20261013.txt` | extraction of the above | 2026-10-14 (written) |
| `nasdaq/nasdaqtrader_calendar.live-20261013T232811Z.html` | <https://www.nasdaqtrader.com/Trader.aspx?id=TradingCalendar> (Incapsula challenge stub) | 2026-10-13 23:28 |
| `nasdaq/nasdaq_holiday_schedule.live-20261013T232814Z.html` | <https://www.nasdaq.com/market-activity/stock-market-holiday-schedule> | 2026-10-13 23:28 |
| `iceus/iceus_notices_service_2026.live-20261013T232857Z.json` | POST <https://www.ice.com/api/sitesearchservice/v1/search/websitenotices?searchCollections=futures_us_exchange_notice&year=2026> | 2026-10-13 23:28 |
| `iceus/iceus_notices_service_2027.live-20261013T232857Z.json` | same service, `year=2027` | 2026-10-13 23:28 |
| `iceeu/iceeu_market_resources.live-20261013T233004Z.html` | <https://www.ice.com/futures-europe/market-resources> | 2026-10-13 23:30 |
| `iceeu/iceeu_excel_trading_schedule.live-20261013T233009Z.xlsx` | <https://www.ice.com/publicdocs/futures/Excel_Trading_Schedule.xlsx> | 2026-10-13 23:30 |
| `iceeu/iceeu_trading_schedule_oil.live-20261013T233009Z.pdf` | <https://www.ice.com/publicdocs/Trading_Schedule.pdf> | 2026-10-13 23:30 |
| `iceeu/iceeu_trading_schedule_liffe.live-20261013T233009Z.pdf` | <https://www.ice.com/publicdocs/futures/Trading_Schedule_Migrated_Liffe_Contracts.pdf> | 2026-10-13 23:30 |
| `iceeu/iceeu_change_tracker_tail-20261013.txt` | extraction from the xlsx Change Tracker sheet | 2026-10-14 (written) |
| `eurex/eurex_trading_calendar_archive.live-20261013T233105Z.html` | <https://www.eurex.com/ex-en/trade/trading-calendar> | 2026-10-13 23:31 |
| `eurex/eurex_holiday_regulations.live-20261013T233107Z.html` | <https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations> | 2026-10-13 23:31 |
| `eurex/eurex_indicative_trading_calendars.live-20261013T233109Z.html` | <https://www.eurex.com/ex-en/trade/trading-calendar/indicative-trading-calendars> | 2026-10-13 23:31 |
| `eurex/eurex_trading_calendar_2026.live-20261013T233142Z.pdf` | <https://www.eurex.com/resource/blob/4873184/0ca7669a8cb9a2f917d99a801fb3f2de/data/tradingcalendar_2026_en.pdf> | 2026-10-13 23:31 |
| `euronext/euronext_trading_hours_holidays.live-20261013T233200Z.html` | <https://www.euronext.com/en/trading/trading-hours-holidays> | 2026-10-13 23:32 |
| `bme/bme_renta_variable_regulation_index.live-20261013T233315Z.json` | <https://www.bolsasymercados.es/es/bme-exchange/regulacion/renta-variable/_jcr_content/root/containers/container/assetstaxonomyfilter.results.json> | 2026-10-13 23:33 |
| `bme/meff_calendario.live-20261013T233358Z.html` | <https://www.meff.es/esp/Calendario> | 2026-10-13 23:33 |
| `six/six_trading_calendar_2026.live-20261013T233442Z.pdf` | <https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2026.pdf> | 2026-10-13 23:34 |
| `six/six_trading_calendar_2027.live-20261013T233444Z.pdf` | <https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2027.pdf> | 2026-10-13 23:34 |
