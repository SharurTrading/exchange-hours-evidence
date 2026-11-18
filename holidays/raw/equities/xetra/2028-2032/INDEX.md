# Xetra (Deutsche Börse cash market) holiday artifacts, 2028-2032

Retrieved 2026-11-18 UTC by the four-European-identity holiday-horizon
extension. Every artifact is the operator's own page or calendar (T1) read
from cashmarket.deutsche-boerse.com, live.

| Artifact | Source URL | Capture / replay | Retrieved (UTC) | Tier | sha256 |
|---|---|---|---|---|---|
| `db_trading_calendar_page.live-20261118T084732Z.html` | <https://www.cashmarket.deutsche-boerse.com/cash-en/trading/trading-calendar-and-trading-hours> | live | 2026-11-18 08:47:32 | T1 | `4e798de0c07cea88328e4a267767441732eb3e8b8e7da28664d8170fbf0ae400` |
| `deutsche-boerse-trading-calendar-2027.pdf` | <https://www.cashmarket.deutsche-boerse.com/resource/blob/5674438/fb6e22c77930acea97641cf7d65ef78a/data/deutsche-boerse-trading-calendar-2027.pdf> | live, linked from the page above ("Trading Calendar 2027") | 2026-11-18 08:47:32 | T1 | `5c62bf0a78afb8f6123638d6e7b9a30c864799e2c2210b73b13bcdb6e9a64cf2` |

## Reading notes

- The page's `Non-trading days at Frankfurter Wertpapierbörse (FWB®, the
  Frankfurt Stock Exchange) (Xetra and Börse Frankfurt) are*:` table covers
  **2026-2032**, one row per holiday with seven year columns. This capture is
  the artifact that keys the **2028-2032** rows (`DB-TC-PAGE-2028-2032`); the
  2025-2027 rows keep their existing keying (`DB-TC-PAGE-2025`, `DB-TC-PAGE`).
- **Table stability.** The table's text in this capture is byte-for-byte the
  same as in the stored 2026-09-28 live edition
  (`../2025-2027/live_cashmarket_trading-calendar-and-trading-hours.html`,
  sha256 `d70a8f5d54cb529103bf674ea8382702a3510800dac8b48965a43aa08ae4bca4`):
  the 2026-2032 columns are unchanged across the two retrievals, so the
  2028-2032 columns were already printed by the operator for weeks before this
  capture.
- **2027 cross-check (pre-condition for encoding).** The page's 2027 column
  (Friday Jan 01, Friday Mar 26, Monday Mar 29, Saturday May 01, Friday Dec
  24\*\*, Saturday Dec 25, Sunday Dec 26, Friday Dec 31\*\*) agrees with the
  five shipped 2027 weekday rows exactly; the three weekend dates (Sat 01 May,
  Sat 25 Dec, Sun 26 Dec) key no row under the weekend convention, as the
  shipped table already records. No disagreement: encoding proceeded.
- Footnotes, verbatim: `* The overview is for information purposes only.
  Changes for future years are not excluded.` — recorded as a residual risk in
  `docs/evidence/xetra.md` (the operator expressly reserves changes). And
  `** No trading but settlement is open if the holiday is not on a Saturday or
  Sunday.` — full closures for the market clock, not early closes; the
  weekend qualifier added to the footnote leaves every shipped weekday `**`
  row (2025-2027) unchanged because none of those dates falls on a weekend.
- The named trading-holiday note is still scoped to `in the year 2026`
  (Ascension Day 14 May 2026, Whit Monday 25 May 2026, Corpus Christi
  4 June 2026; `Trading of shares and Exchange traded products on Frankfurt
  and Xetra ends ... at 20:00 CET`), so no early close is sourced for
  2028-2032 and none is encoded; the `#200` watch for named 2027+ holiday
  hours stands.
- The page still links the Final trading session 2026 notice, the Trading
  Calendar 2027 PDF and the Trading calendar 2026 PDF; the 2027 PDF fetched
  here is **byte-identical** to the `DB-TC-PDF-2027` edition retrieved
  2026-10-31 (same sha256), confirming the 2027 basis unchanged. It is banked
  in this directory as the 2027 basis beside the 2028-2032 keying artifact.

## Encoded rows (weekend-falling page dates key no row)

- 2028: Fri 14 Apr (Good Friday), Mon 17 Apr (Easter Monday), Mon 01 May
  (Labor Day), Mon 25 Dec (Christmas Day), Tue 26 Dec (Boxing Day) — 5 rows.
  Page dates with no row: Sat 01 Jan, Sun 24 Dec\*\*, Sun 31 Dec\*\*.
- 2029: Mon 01 Jan, Fri 30 Mar, Mon 02 Apr, Tue 01 May, Mon 24 Dec\*\*,
  Tue 25 Dec, Wed 26 Dec, Mon 31 Dec\*\* — 8 rows; nothing falls on a weekend.
- 2030: Tue 01 Jan, Fri 19 Apr, Mon 22 Apr, Wed 01 May, Tue 24 Dec\*\*,
  Wed 25 Dec, Thu 26 Dec, Tue 31 Dec\*\* — 8 rows; nothing falls on a weekend.
- 2031: Wed 01 Jan, Fri 11 Apr, Mon 14 Apr, Thu 01 May, Wed 24 Dec\*\*,
  Thu 25 Dec, Fri 26 Dec, Wed 31 Dec\*\* — 8 rows; nothing falls on a weekend.
- 2032: Thu 01 Jan, Fri 26 Mar, Mon 29 Mar, Fri 24 Dec\*\*, Fri 31 Dec\*\* —
  5 rows. Page dates with no row: Sat 01 May, Sat 25 Dec, Sun 26 Dec.

\*\* `No trading but settlement is open if the holiday is not on a Saturday or
Sunday.` Every starred date encoded above falls on a weekday, so each is a
full trading closure.
