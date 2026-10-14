# OANDA UK withheld holiday rows — capture sweep and extraction record

Retrieved and checked 2026-10-13 UTC. Target: the 26 book/trade-date pairs
withheld in exchange-hours-rs#332, plus the UK TRY book's earlier history and
a dated artifact inside the Brent normal-week span 2023-06-05..2024-02-21.
Every artifact here is UK-scoped (`oanda.com/uk-en/...` or
`help.oanda.com/uk/...`, the OANDA Europe Limited pages) and is therefore a
qualifying closer class for the 26 rows; quotes below are verbatim, and rows
printed in session language are flagged. Per LAW-NO-FABRICATED-DATES each
capture dates the observation it prints, never a state.

## 1. Channel census (all checked 2026-10-13 UTC)

Wayback CDX sweeps (`web.archive.org/cdx/search/cdx`, encoded-star prefix
form; saved under `cdx/`):

| Channel | Distinct captures | Status |
|---|---|---|
| `www.oanda.com/uk-en/trading/holiday-trading-hours/` | 18 (2022-08-11..2026-06-08) | all 18 already saved in `normal-weeks/oanda-uk-wayback-audit-2026-10-11/holiday-captures/`; zero new |
| `www.oanda.com/uk-en/trading/hours-of-operation/` | 27 (2021-03-03..2026-04-11) | 19 previously saved; the 8 twice-refused 2025/2026 replays **retrieved this run** (`hours-retries/`), each byte-exact against its CDX sha1 |
| `www.oanda.com/uk-en/trading/holiday-hours-maintenance-times/` | 5 (2020-10-25..2022-05-27) | **page newly discovered** — the prior audit's `legacy-holiday-hours` query (`oanda.com/*holiday-trading-hours*`) cannot match it; all 5 **retrieved this run** (`holiday-maintenance-times/`) |
| `help.oanda.com/uk/en/faqs/hours-of-operation.htm` | 4 (2024-06-19, 2024-11-07, **2025-10-28**, **2026-05-20**) | 2 previously saved; the 2 new captures **retrieved this run** (`help-centre-new/`) |
| locale variants `oanda.com/uk/...` and `oanda.com/en-uk/...` (holiday and hours paths) | 0 | negative, `cdx/cdx-{uk,enuk}-locale-*.json` |
| any `oanda.com/uk-en/*` URL containing "hours" | exactly the three paths above | `cdx/cdx-uken-any-hours-urls.txt` — terminal for the locale tree |
| any `help.oanda.com/uk*` URL containing "hour"/"holiday" | exactly the FAQ path above | `cdx/cdx-help-uk-hours-urls.txt` |
| `oanda.com/uk-en/trading/*` full tree (5,645 rows) | no `.pdf`, no further hours/holiday path | `cdx/cdx-uken-trading-tree.json` |
| captures after 2026-06-08 (holiday page) and after 2026-04-11 (hours page) | 0 | `cdx/cdx-{holiday-after-20260608,hours-after-20260411}.json` |

The two new help-centre captures are MadCap (`api.madcapcentral.com`) page
shells whose grids load client-side; no schedule bytes are archived in any of
the four captures — only the boilerplate "trading hours are subject to change
during daylight saving time and certain public holidays". Help-centre stays a
negative channel.

The `holiday-hours-maintenance-times` captures (2020-2022) print a per-product,
per-date holiday table with exact ET close/open times for BCO/USD, UK100/GBP,
DE30/EUR, US30/USD, NAS100/USD, JP225/USD, CORN, WHEAT, SUGAR, WTI, XAU, XAG,
SG30 — including dated rows such as "01:00 GMT open (19th January 2021)". They
predate every target trade date (all 2024+), print **no TRY row and no US
Treasury row**, and close no #332 row; they are retained as the earliest
UK-scoped holiday-arrangement publication found (T1).

## 2. Per-target verdicts (26 rows — all NOT FOUND)

Legend: `UK-HOL@<ts>` = holiday page capture, `UK-HRS@<ts>` = hours page
capture; stored under `normal-weeks/oanda-uk-wayback-audit-2026-10-11/` (pre
2026-10-13 retrievals) or `hours-retries/` (this run). "Witnessed" = printed
by the cited UK artifact in session language; "Still missing" = the withheld
detail #332 lists. No artifact states the missing detail for the exact book
and trade date, and no artifact affirms normal hours for it.

### oanda_us_index_cfd / oanda_us_bond_cfd

| # | Book | Trade date | Post-date UK witnesses (45-day window unless noted) | Witnessed (verbatim, session language) | Still missing |
|---|---|---|---|---|---|
| 1,5 | index, bond | 2024-01-02 | none within ±45d (gap 2023-09-29..2024-04-18); retained rows visible from UK-HOL@20240418175746 onward | `Monday 1st January 2024` section prints only `UK100/GBP is closed / European indices are closed / Commodities are closed / Brent Crude Oil is closed / Sugar is closed / German bund is closed / UK bond is closed / AU200 is closed / HK33/HKD is closed / CHINAH/HKD is closed / SG30/SGD is closed` — no US index or US bond row; `Tuesday 2nd January 2024` prints only `Commodities open late 9:30 am / *OC only: Spot Crypto is open with regular hours` | the whole US-index and US-bond arrangement for trade date 2024-01-02 (no reopen, no close) |
| 2,6 | index, bond | 2024-01-16 | none in window; from UK-HOL@20240418175746 onward | `Monday 15th January 2024 - MLK Day`: `US index futures close early at 1 pm and reopen at 6 pm` / `US bonds close early at 1 pm and reopen at 6 pm` | the trade date's final close (the Tuesday session's close) — page states the Monday 18:00 reopen only |
| 3,7 | index, bond | 2024-02-20 | none in window; from UK-HOL@20240418175746 onward | `Monday 19th February 2024 - US Presidents Day`: same two lines as MLK | the trade date's final close |
| 8 | bond | 2024-12-24 | UK-HOL@20241213192721, UK-HOL@20241219055052 (both pre-publication: top heading `Thursday 28th November:` Thanksgiving 2024); first post-date holiday capture UK-HOL@20250326184653 contains **no December 2024 heading at all** | nothing — Christmas Eve 2024 is printed by no UK capture | the entire US-bond Christmas Eve arrangement |
| 4,9 | index, bond | 2026-05-26 | UK-HOL@20260608180629 (13 days after) | `Monday, 25 May 2026 - Memorial Day (US), Spring Bank Holiday (UK), Whit Monday (DK, CH)`: `US Indices and bonds: Early close at 12:59; reopen at 18:0` — the operator page itself truncates the minute (byte-verified: no digit follows `18:0`); same section: `Brent Crude Oil: Early close at 13:29; reopen at 20:01` | the trade date's final close, and the exact reopen minute the page leaves at `18:0` |

### oanda_brent

| # | Trade date | Post-date UK witnesses | Witnessed (verbatim) | Still missing |
|---|---|---|---|---|
| 10 | 2024-04-01 | UK-HOL@20240418175746, UK-HOL@20240507233633 | `1st April 2024 - Easter`: `Sugar has late open 07:30. UK index future is closed. Australian index is closed. HK33 & CHINAH are closed. All European index futures are closed. German bund is closed. UK bund is closed.` — no Brent row (contrast `29th March 2024 - Good Friday`, which prints `BCO is closed`) | Brent's Easter Monday arrangement |
| 11 | 2024-05-28 | UK-HOL@20240909192149 (81d after, nearest) | `Monday 27th May 2024 - Spring Holiday and Memorial Day`: `US index futures close early at 1 pm and reopen at 6 pm / US bonds close early at 1 pm and reopen at 6 pm / US energies and metals close early at 2.30 pm and reopen at 6 pm / Brent Crude Oil close early at 1:30 pm / Commodities have late opening at 8 pm / Sugar is closed / UK index future is closed / UK gilt (UK10YB/GBP) is closed` | Brent's reopen (the Monday print states the early close but no reopen; the separate `Commodities` line is ambiguous book membership) |
| 12 | 2024-06-20 | UK-HOL@20240909192149 | `Wednesday 19th June 2024 - Juneteenth Holiday`: `... Brent Crude Oil close early at 1:30 pm / Commodities have late opening at 8 pm ...` | Brent's reopen |
| 13 | 2024-07-03 | UK-HOL@20240909192149 | `Wednesday 3rd July 2024`: `US index futures close early at 1:15 pm and reopen at 6 pm` — indices only | Brent's whole arrangement |
| 14 | 2024-07-05 | UK-HOL@20240909192149 | `Thursday 4th July 2024 - Independence Day`: `... Brent Crude Oil close early at 1:30 pm / Commodities are closed ...` | Brent's reopen |
| 15 | 2024-08-26 | UK-HOL@20240909192149 | `Monday 26th August 2024 - Summer Bank Holiday`: `UK index future is closed / UK gilt (UK10YB/GBP) is closed / Sugar opens late at 07:30 am` — no Brent row | Brent's whole arrangement |
| 16 | 2024-09-03 | UK-HOL@20240909192149 | `Monday 2nd September 2024 Labor Day Holiday`: `... Brent Crude Oil close early at 1:30 pm / Commodities have late opening at 8 pm ...` | Brent's reopen |
| 17 | 2025-01-09 | UK-HOL@20250326184653 (76d after, nearest) | `Thursday 9th January 2025 - Carter's Day of Mourning`: `US index close early at 9:30 and reopen at 18:00 / US bonds close early at 13:15 and reopen at 18:00 / Commodities close early at 13:15 and reopen at 20:00` — no Brent row | Brent's whole arrangement |
| 18 | 2025-04-17 | UK-HOL@20250719220103 | `Thursday 17th April 2025`: `US index futures close early at 17:00 ET. / US bonds close early at 17:00 ET. / US energies and metals close early at 17:00 ET. / Commodities close early at 14:20 ET. / Japan 225 closes early at 17:00 ET. / Australian index closes early at 10:00 ET.` — no Brent row | Brent's Holy Thursday arrangement |
| 19 | 2025-04-21 | UK-HOL@20250719220103 | `21st April 2025 - Easter Monday`: `Sugar opens late at 07:30 ET. / UK index future is closed. / Australian index is closed. / HK33 & CHINAH open late at 21:15 ET. / All European index futures are closed. / German bund is closed. / UK bund is closed.` — no Brent row | Brent's Easter Monday arrangement |
| 20 | 2025-07-03 | UK-HOL@20250719220103 | `Thursday, 3rd July 2025`: `US index futures close early at 1:15 pm and reopen at 6 pm / Commodities close early at 2:20 pm / US Share CFDs close early at 1:00 pm` — no Brent row (the next day's section prints `Brent Crude Oil close early at 1:30 pm`, also without reopen) | Brent's Independence-eve arrangement |
| 21 | 2025-08-25 | UK-HOL@20250719220103, UK-HOL@20251118074941 | `Monday, 25 August 2025 - UK Summer Bank Holiday`: `UK100 Index: Closed / UK 10Y Gilt: Closed / UK Share CFDs: Closed / Sugar: Opens late at 07:30 AM` — no Brent row | Brent's whole arrangement |
| 22 | 2025-11-26 | UK-HOL@20251222073046 (decoded), UK-HOL@20260217213704 | `27 November 2025 – Thanksgiving Day` section: `Wednesday, 26 November 2025:` lists exactly `Agricultural commodities: Close at 2:20 PM ET`; the Thursday list prints `Brent Crude Oil: Close early at 1:30 PM, reopen at 8:00 PM` (for the 27th, not the 26th); Friday prints `Brent Crude Oil: Close early at 3:00 PM` | Brent's Thanksgiving-eve (Wednesday 26th) arrangement |
| 23 | 2026-04-06 | UK-HOL@20260608180629 | `Monday, 6 April 2026 - Easter Monday`: `AU200: Open at 19:51 ET / CHINAH, HK33: Closed / CH20, ESPIX, FR40, NL25: Closed / UK100: Open 20:01 ET / DE30, EU50: Open at 20:16 ET / DE10YB: Open at 20:16 ET / UK10YB: Closed / Sugar: Late open at 07:31 ET / UK and European Shares CFDs: Closed` — no Brent row (contrast Maundy Thursday 2 April: `Brent Crude Oil: Close at 17:59`, and Good Friday 3 April: `Brent Crude Oil: Closed`) | Brent's Easter Monday arrangement |
| 24 | 2026-05-01 | UK-HOL@20260608180629 | `Friday, 1 May 2026 - Labour Day`: `CHINAH, HK33: Closed / CH20, DE30, ESPIX, EU50, FR40, NL25: Closed / DE10YB: Closed / BE, DE, ES, FI, FR, NL, PT, SE Share CFDs: Closed` — no Brent row | Brent's whole arrangement |
| 25 | 2026-05-04 | UK-HOL@20260608180629 | `Monday, 4 May 2026 - Early May Bank Holiday (UK)`: `UK100: Closed until 20:01 reopen / Sugar: Late open at 7:31 / UK 10Y Gilt: Closed / UK Share CFDs: Closed` — no Brent row | Brent's whole arrangement |
| 26 | 2026-08-31 | **none** — zero captures within ±45 days and none after 2026-06-08 anywhere (CDX `cdx/cdx-holiday-after-20260608.json` empty; hours page likewise ends 2026-04-11) | nothing | everything; a future capture of the holiday page taken after the operator publishes the 2026 Summer Bank Holiday arrangement is the named closer |

Every witnessed line above is the operator's own close/open/reopen language
(session language at T1). "Silence about Brent" occurs inside sections that do
name other books, so it is operator silence for the exact book, not a page
absence — no row may be closed by inference from it.

## 3. TRY record (secondary target)

- All 18 holiday-page captures and all 5 `holiday-hours-maintenance-times`
  captures print **no TRY row** (only "Try demo" chrome matches).
- All 19 previously-known hours-page captures (2021-03-03..2024-09-19) print
  no TRY row.
- New observations from this run's `hours-retries/`:
  - UK-HRS@20250120083642: `Forex Instrument ... All FX Products | New York |
    100,000 | Sun-Fri: 17:05 - 16:59 *` — no TRY carve-out.
  - UK-HRS@20250419172608, UK-HRS@20250506101210, UK-HRS@20250708202954:
    `All FX products | New York | Sun-Fri: 17:05 - 16:59*` — no TRY carve-out.
  - UK-HRS@20251115023204, UK-HRS@20251213234655, UK-HRS@20260209190304,
    UK-HRS@20260411231933: **first TRY prints on the UK hours page**:
    `All FX products (except TRY Pairs) | New York | Sun-Fri: 17:05 - 16:59*`
    and `TRY Pairs | Central Europe | 100,000 | Mon-Fri: 08:00 - 17:00`
    (verbatim, session language).
- Verdict: the TRY carve-out is witnessed between 2025-07-08 and 2025-11-15.
  Neither bound is an effective day and no operator statement dates the
  changeover, so under LAW-NO-FABRICATED-DATES this records two dated
  observations with an undated changeover — it does **not** key a cutover.
  Earlier TRY history (before 2025-11-15) remains unproved by any UK artifact;
  these prints do not carry the historical claim backward.

## 4. Brent normal-week span 2023-06-05..2024-02-21 (secondary target)

- CDX 2023-06-06..2024-02-20 for the hours page: **zero captures**
  (`cdx/cdx-hours-of-operation-prefix.json`; uncollapsed query re-run this
  date). Negative — the bracket has no in-bracket normal-week witness.
- The only UK operator artifact captured strictly inside the span is holiday
  page UK-HOL@20230929043012 (2023-09-29), whose prose still prints Brent
  ET-anchored holiday lines (e.g. `Brent Crude Oil close early at 1:30 pm`
  under `Monday 4th September 2023 - Labour Day`). It is holiday prose, not a
  normal-week grid, so it does not close the normal-week bracket.
- help-centre and maintenance-times channels have no capture inside the span.

## 5. New dated normal-week observations for Brent (from `hours-retries/`)

These narrow later Brent history and are verbatim T1 prints (session
language); they date observations, not effective days:

| Capture | Brent row (verbatim) | Timezone column | Dagger footnote |
|---|---|---|---|
| UK-HRS@20250120083642 | `Mon - Fri 01:01 - 22:59` | `London` | `† Brent Crude oil: Starts at 23:01 London time on a Sunday / Closes at 21:59 London time Friday / has a break from 21:59- 22:05 London time Mon-Thu` |
| UK-HRS@20250419172608 / @20250506101210 / @20250708202954 | `Mon - Fri 01:01 - 22:59` | `New York` | same short footnote |
| UK-HRS@20251115023204 / @20251213234655 / @20260209190304 / @20260411231933 | `Sun - Fri 23:01 - 21:59` | `New York` | `†Brent Crude Oil starts at 23:01 London time on Sunday and closes at 21:59 London time on Friday. There will be a six-minute break from 21:59 - 22:05 London time Mon-Thu, and two-hours break from 22:59 - 01:01 London time Mon-Thu.` |

The row shape and the footnote's two-hours-break sentence change together
between 2025-07-08 and 2025-11-15; the changeover day is unstated by any
artifact (a disclosed undated changeover, not a cutover).

## 6. Closing conditions

- Rows 1-3, 5-7 (index/bond final closes): a UK artifact printing the
  trade-date session's close (e.g. a Tuesday section, or holiday prose naming
  the next trade date's session end) closes them.
- Row 8: any UK capture printing a Christmas Eve 2024 section closes it; none
  exists in the archive.
- Rows 4, 9: a capture printing the Memorial 2026 line with an untruncated
  reopen (or a separate book line) closes them; the truncation is in the
  operator's own current print.
- Rows 10-25: a capture whose section prints a Brent line for the exact civil
  date (or affirms `Brent Crude Oil ... regular hours` for it) closes each.
- Row 26: the first holiday-page capture taken after the operator publishes
  the 31 August 2026 arrangement.
- TRY history: only a pre-2025-11-15 UK artifact printing TRY (row or
  carve-out) moves the earlier bound; the sweep found none.
- Brent span: only a UK hours-page capture (or PDF asset) taken between the
  two endpoint captures closes it; the locale-tree census shows no such URL
  exists in the archive.
