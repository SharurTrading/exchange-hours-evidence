# Evidence index — `equities/tsx/2025-2027`

Primary-source retrieval for the `tsx` identity (Toronto Stock Exchange cash equities).
The operator's holiday statement is TMX Group's "Calendar" page,
`tsx.com/en/trading/calendars-and-trading-hours/calendar`, which lists
"YYYY Stock Market Holidays - Stock Markets Closed" per year for TSX/TSXV, with a
Christmas Eve footnote `* Closing at 1:00 PM (TSX/TSXV) and 1:30 (ALPHA/ALPHA X/DRK)`.

Retrieval session: **2026-09-28, 01:06 UTC** (LAW-UTC-DATES). `curl` with a desktop browser
User-Agent; no access control evaded. The page was found through the tsx.com sitemap
(`https://www.tsx.com/sitemap.xml` lists `/en/trading/calendars-and-trading-hours/calendar`).

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `calendars-and-trading-hours_calendar.live.html` | `https://www.tsx.com/en/trading/calendars-and-trading-hours/calendar` | 2026-09-28T01:06:13Z | `983d3108683e59f3b6045ffd862e699113316a14960f54880ef33a627718e7d2` | 65262 | **T1, controlling for 2025 and 2026.** Server-rendered HTML (no JS needed). "2026 Stock Market Holidays - Stock Markets Closed": New Year's Day 01-01, Family Day 02-16, Good Friday 04-03, Victoria Day 05-18, Canada Day 07-01, Civic Holiday 08-03, Labour Day 09-07, Thanksgiving Day 10-12, Christmas Eve 12-24 `*` (closing 1:00 PM), Christmas Day 12-25, In Lieu of Boxing Day 12-28. "2025 Stock Market Holidays - Stock Markets Closed": New Year's Day 01-01, Family Day 02-17, Good Friday 04-18, Victoria Day 05-19, Canada Day 07-01, Civic Holiday 08-04, Labour Day 09-01, Thanksgiving Day 10-13, Christmas Eve 12-24 `*`, Christmas Day 12-25, Boxing Day 12-26. |

## Retrieval findings

- **2027 is not published.** The page carries only 2026 and 2025 sections (plus "Settlement
  Schedule" links for 2026/2025). TMX historically publishes the next year's calendar in
  Q4. Coverage therefore stops at 2026-12-31 for this identity; closing condition is the
  operator's 2027 calendar page.
- The "U.S. Holidays" block (MLK Day, Memorial Day, Juneteenth, Independence Day in lieu,
  U.S. Thanksgiving) is footnoted `** U.S. Holidays with Special Settlement for Issues
  trading in USD` — a settlement arrangement, **not** a TSX trading closure, and it is not
  encoded (LAW-SESSION-NOT-EXPIRY).
- No early close is stated for any date except Christmas Eve (1:00 PM TSX/TSXV). The 1:30 PM
  half of the footnote applies to ALPHA/ALPHA X/DRK book systems, which are outside this
  identity's Toronto Stock Exchange cash-equity scope.
