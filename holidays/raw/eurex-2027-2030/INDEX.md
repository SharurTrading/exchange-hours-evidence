# Evidence index — task `eurex-2027-2030`

Primary-source retrieval keying the `eurex`, `eurex_fixed_income` and
`eurex_smi` holiday rows for **2027-2030** from Eurex's own Holiday
regulations page, whose `Non-trading days at Eurex 2026 - 2030` table states
the Eurex-wide non-trading days for those years.

Retrieval session: **2026-11-18, 08:47:32 UTC** (LAW-UTC-DATES). `curl` with a
normal desktop browser User-Agent; live operator bytes, no access control
involved.

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `eurex_holiday_regulations.live-20261118T084732Z.html` | `https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations` | 2026-11-18T08:47:32Z | `47e905aed14cabcb657e363bade142fb8d2861523c052ecfe3b4e3b6a873f8ae` | 155911 | **T1. The keying artifact for the 2027-2030 rows.** The page's `Non-trading days at Eurex 2026 - 2030` table, one row per holiday with the 2026-2030 columns, under the footnote `* No trading; clearing and settlement are open if the holiday is not on a Saturday or Sunday.` The `<h2>2026</h2>` day-by-day section beside it is the country-scope channel; it exists for 2026 only — no 2027-2030 section or panel is published. |

## Verification performed

1. **2026 cross-check (pre-condition for encoding).** The page's 2026 column
   (Thursday 01 Jan, Friday 03 Apr, Monday 06 Apr, Friday 01 May, Thursday
   24 Dec, Friday 25 Dec, Saturday 26 Dec, Thursday 31 Dec — all 2026) was
   compared against the shipped 2026 rows before anything was encoded: the
   seven weekday dates match the seven shipped rows exactly, and the one
   extra page date, Saturday 26 December 2026, is a weekend entry the shipped
   table deliberately does not carry (weekend-falling dates key no row), the
   same convention that leaves Unity Day 2026-10-03 (Saturday) with no row in
   the day-by-day section. No disagreement: encoding proceeded.
2. **Table stability.** The `Non-trading days at Eurex 2026 - 2030` table
   text in this capture is identical to the same table in the stored
   2026-09-26 capture (`../eurex-2025-2027/eurex_holiday_regulations_2026.live-20260926.html`,
   sha256 `6eaa71115aa9efd4b2c9be2c22e6f7e67d4c175af372e2d78cf68a574c677faa`):
   every 2027-2030 column value is unchanged across the two retrievals.
3. **Caveat-language scan.** Full-text scans of this capture find `preliminar`
   0 and `subject to change` 0; all 10 `indicativ` matches are navigation
   links to the separate Indicative Trading Calendars page (five distinct
   navigation targets, each printed twice by the page's desktop and mobile
   navigation), none of them text in or beside the table. The table therefore
   carries no caveat on the operator's own page; the preliminary-and-indicative
   label the crate previously read over 2027+ lives on the separate Indicative
   Trading Calendars page and governs that page's calendars only.
4. **Country-scope absence.** The page's country-scope channel is its
   day-by-day `<h2>` section; this capture carries `2026` as the only such
   section and the strings `countries` 0, `Switzerland` 0. The Swiss clause
   dates for 2026 (02 January, 14 May, 25 May) sit in that 2026 section; no
   2027-2030 country-scope section exists, so no Swiss-scope (or other
   country-scope) row beyond the Eurex-wide set is encodable for those years.
   This is the residual recorded in the four evidence files.

## Encoded rows (weekend-falling page dates key no row)

- 2027 (`EUREX-HOLREG-2027-2030`): Fri 01 Jan, Fri 26 Mar, Mon 29 Mar, Fri 24 Dec\*,
  Fri 31 Dec\* — 5 rows. Page dates with no row: Sat 01 May, Sat 25 Dec,
  Sun 26 Dec.
- 2028 (`EUREX-HOLREG-2027-2030`): Fri 14 Apr, Mon 17 Apr, Mon 01 May, Mon 25 Dec,
  Tue 26 Dec — 5 rows. Page dates with no row: Sat 01 Jan, Sun 24 Dec\*,
  Sun 31 Dec\*.
- 2029 (`EUREX-HOLREG-2027-2030`): Mon 01 Jan, Fri 30 Mar, Mon 02 Apr, Tue 01 May,
  Mon 24 Dec\*, Tue 25 Dec, Wed 26 Dec, Mon 31 Dec\* — 8 rows. Nothing falls on
  a weekend; all eight page dates ship.
- 2030 (`EUREX-HOLREG-2027-2030`): Tue 01 Jan, Fri 19 Apr, Mon 22 Apr, Wed 01 May,
  Tue 24 Dec\*, Wed 25 Dec, Thu 26 Dec, Tue 31 Dec\* — 8 rows. Nothing falls on
  a weekend; all eight page dates ship.

\* `No trading; clearing and settlement are open if the holiday is not on a
Saturday or Sunday.` Both starred dates of 2027 and 2030 fall on weekdays, so
both are full trading closures; in 2028 both starred dates fall on Sundays and
key no row.
