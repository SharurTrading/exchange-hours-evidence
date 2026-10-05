<!-- SPDX-License-Identifier: MIT-0 -->

# Equities holiday retrieval — NZX, ASX, SGX Securities (2025-2027)

Retrieved on **2026-09-28 (UTC)** in one bounded pass. All artifacts are the
operators' own pages or machine channels, saved as raw bytes, plus the public
Wayback Machine `id_` replays used where the live page no longer prints the
year. Per-venue digests: `SHA256SUMS.txt` beside each venue directory and the
combined file at this directory's root.

Times below are UTC, derived from the retrieval host's clock during the pass
(the host's local clock is UTC+10; both were read in the same session).

## NZX — `holidays/raw/equities/nzx/2025-2027/`

The operator's own "NZX Market Holidays & Trading Hours" page
(<https://www.nzx.com/learning/help-reference/trading-hours>; the pre-2026
redesign equivalent was
<https://www.nzx.com/investing/nzx-trading-hours>). The holiday table is a
rolling operator table covering roughly the next 13 months; the live page
(retrieved 2026-09-28 01:10 UTC) lists Waitangi Day 2026-02-06 through the Day
after New Year's Day 2027-01-04. Earlier coverage comes from Wayback `id_`
replays of the same operator page.

| Artifact | URL | Retrieved, UTC | sha256 |
|---|---|---|---|
| `live_nzx_trading_hours_and_holidays.html` | <https://www.nzx.com/learning/help-reference/trading-hours> | 2026-09-28 01:10 | `92071cd2c1186012fe977fc59af5f4b27de50a435a11b3298a078aa715391146` |
| `wayback-20241216-nzx-trading-hours.html` | <https://web.archive.org/web/20241216221746id_/https://www.nzx.com/investing/nzx-trading-hours> | 2026-09-28 01:20 | `27ead98734cede1f2b0e21d3132b20b5a4b6ea5ebd218b4fb4d17fe9394aa675` |
| `wayback-20250123-nzx-trading-hours.html` | <https://web.archive.org/web/20250123031559id_/https://www.nzx.com/investing/nzx-trading-hours> | 2026-09-28 01:19 | `982f231b435dddba2473692163a2bcb60f47f89c1005a41d1745eb520c6e715a` |
| `wayback-20251116-nzx-trading-hours.html` | <https://web.archive.org/web/20251116030142id_/https://new.nzx.com/investing/nzx-trading-hours> | 2026-09-28 01:19 | `59c3798c5ed84a2d445cfe98cb4e54ecd3256a53dd569d9fb557671d805961a7` |
| `wayback-20260203-nzx-trading-hours.html` | <https://web.archive.org/web/20260203200136id_/https://new.nzx.com/investing/nzx-trading-hours> | 2026-09-28 01:19 | `0aa0508dadd8c30aeb914bd09f6e7db96afe84533a18350e4145f7b5b8dd6215` |

Row sources: **2025-01-01 .. 2026-01-02** from `wayback-20241216`
(the 2025-01-23 replay prints the identical 2025 rows and is corroboration);
**2026-02-06 .. 2027-01-04** from `wayback-20260203` (the 2025-11-16 replay
still prints the 2025/early-2026 table and corroborates the boundary; the live
page prints the identical 2026-02-06..2027-01-04 rows and is the horizon
evidence). NZX publishes nothing past 2027-01-04 today, so the coverage
window ends there.

## ASX — `holidays/raw/equities/asx/2025-2027/`

The operator's own "Trading calendar" page under cash-market trading hours
(<https://www.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours/trading-calendar>).
The live page (retrieved 2026-09-28 01:00 UTC) server-renders the **2026** and
**2027** tables only; the **2025** table comes from a Wayback `id_` replay of
the same page captured 2025-04-16.

| Artifact | URL | Retrieved, UTC | sha256 |
|---|---|---|---|
| `live_asx_cash_market_trading_calendar.html` | <https://www.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours/trading-calendar> | 2026-09-28 01:00 | `adb2344ca5e13dcbfb8de9b0cf40334c992f4ffb660026b22bca7d21d964cd19` |
| `live_asx_trading_hours_calendar_hub.html` | <https://www.asx.com.au/markets/market-resources/trading-hours-calendar> | 2026-09-28 00:59 | `7ea4e0392e1e574c7ddf9af1ed70747e03225203803abe70f1d453984196fe2b` |
| `wayback-20250416-asx-trading-calendar.html` | <https://web.archive.org/web/20250416082951id_/https://www.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours/trading-calendar> | 2026-09-28 01:51 | `d24de6d6f6ec1864480de6f2f75cf4a3650b30f6eda8daa354fd1bfa1302d66d` |

ASX publishes the full 2027 calendar, so the coverage window reaches
2027-12-31. The 2027 sheet prints ANZAC Day (Monday 2027-04-26) as **OPEN**
("Substitute for Sunday 25 April"), so no row ships for it.

## SGX Securities — `holidays/raw/equities/sgx_securities/2025-2027/`

The live `www.sgx.com` pages are an Angular SPA shell for non-JS clients; the
shell was saved to document the channel, and the operator's content came from
SGX's own content API (`api2.sgx.com/content-api`, the CMS feed the SPA
itself renders), read as bytes with the same payload the page renders. The
securities schedule lives on the operator's "Stock Exchange — Trading" page
(<https://www.sgx.com/stock-exchange/trading>): it prints the full-day and
half-day phase tables and the half-day date table for 2025 & 2026, and states
"SGX follows the Singapore holiday calendar available on the Ministry of
Manpower website". MOM's own page (<https://www.mom.gov.sg/employment-practices/public-holidays>,
retrieved 2026-09-28 01:48 UTC, last updated 19 June 2026) prints the gazetted
2025, 2026 and 2027 dates.

| Artifact | URL | Retrieved, UTC | sha256 |
|---|---|---|---|
| `api2_content-api_stock-exchange_trading.json` | <https://api2.sgx.com/content-api?queryId=dd24dd8e5b3ef52e535a662e01b58d76471f335e%3Apage&variables=%7B%22path%22%3A%22%2Fstock-exchange%2Ftrading%22%2C%22lang%22%3A%22EN%22%7D> | 2026-09-28 01:59 | `45dbdc61d808b4f72bb8bbddb198107f08759a20b85b288271d6d5a0326facd7` |
| `live_mom_public_holidays.html` | <https://www.mom.gov.sg/employment-practices/public-holidays> | 2026-09-28 01:48 | `a4f175a7d33222b91f1c8c2f84e6d1e75f0c0b15e265addb478b73e3e65dcf3d` |
| `api2_sgx_calendar_2026.pdf` | <https://api2.sgx.com/sites/default/files/2026-01/SGX%20Calendar%202026_2.pdf> | 2026-09-28 01:36 | `178e06c2be1165d3c60debeb24637705d723c6406fc91ca9defb23d5c330aa14` |
| `live_sgx_trading_hours_holidays.html` | <https://www.sgx.com/trading-hours-holidays> (SPA shell, no holiday content server-side) | 2026-09-28 01:31 | `d87ad3e0e9c8851778037bbad57c9f67655749d3e631296154c1dc9afe949e83` |
| `wayback-20260113-sgx-trading-hours-holidays.html` | <https://web.archive.org/web/20260113032201id_/https://www.sgx.com/trading-hours-holidays> (same shell) | 2026-09-28 01:32 | `aad936ba1f7157c615553a2d23a9e649f28b912c96147ba7c92575da27c8b15b` |

`api2_sgx_calendar_2026.pdf` is SGX Group's printed desk calendar; its day
notes address derivatives contracts only and key no securities row — it is
kept as context. The securities coverage window ends at 2026-12-31: the
operator's half-day table is printed for 2025 & 2026 only, and the 2027
half-day treatment of the Chinese New Year / Christmas / New Year eves is
unpublished, so 2027 would be incomplete under the operator's own sheet.

## Channels that refused (recorded, not worked around)

- `www.sgx.com` serves an SPA shell to non-JS clients (saved above); the
  Googlebot user agent is denied by the operator's CDN (Access Denied).
  The content-API replay above is the working bytes channel.
- `api.sgx.com` (announcements/market APIs) answers 403 Forbidden without an
  operator-issued token; the token flow lives in the SPA bundle and was not
  tunnelled around.
- The Internet Archive CDX/replay endpoints returned "Temporarily Offline"
  intermittently during the pass; every query succeeded on retry.

## Row derivation summary (all rows trace to the saved bytes)

- **NZX** — window 2025-01-01..2027-01-04. 24 `Closed` rows (2025: 11,
  2026: 11, 2027: 2) and 4 abbreviated-trading days (2025-12-24, 2025-12-31,
  2026-12-24, 2026-12-31) stated as replacement blocks per the operator's own
  abbreviated grid (Normal Trading 10:00-12:45, Pre-Close 12:45-13:00,
  Adjust 13:00-13:30, closing uncross envelope 12:59:30-13:00:30).
- **ASX** — window 2025-01-01..2027-12-31. 23 `Closed` rows (8 + 8 + 7,
  including the Saturday 2026-04-25 ANZAC closure the sheet prints) and 6
  early closes at the sheet's own 14:10 footnote (2025-12-24, 2025-12-31,
  2026-12-24, 2026-12-31, 2027-12-24, 2027-12-31).
- **SGX Securities** — window 2025-01-01..2026-12-31. 19 `Closed` rows
  (9 in 2025, 10 in 2026, weekday gazetted holidays per MOM's printed list
  including the three Sunday-substituted 2026 Mondays) and 6 early closes at
  the operator's printed half-day Close of 12:16 (2025-01-28, 2025-12-24,
  2025-12-31, 2026-02-16, 2026-12-24, 2026-12-31).
