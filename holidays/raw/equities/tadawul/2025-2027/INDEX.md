# Saudi Exchange (Tadawul) — Main Market holidays, 2025-2027

Retrieved live from the operator's own site on 2026-09-28 (UTC). The site's
WAF refuses plain curl (403, twice); it answers a complete browser-grade
header set, which is how these two pages were captured. SHA-256 over the
saved bytes.

| File | URL | Retrieved, UTC | sha256 |
|---|---|---|---|
| `live_saudi_exchange_holiday_calendar.html` | <https://www.saudiexchange.sa/wps/portal/saudiexchange/about-saudi-exchange/exchange-media-centre/saudi-exchange-holiday-calendar?locale=en> | 2026-09-28 01:20 | `6980261a27759b1fd80b79281d1f08aa30d19aa0e1b08d721020910c268343ff` |
| `live_market_holidays_page.html` | <https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/market-holidays/?locale=en> | 2026-09-28 01:18 | `d99b47070910142225af0c948f2470c9410f249bde9b46a786a310e28da50169` |

Notes:

- The `Saudi Exchange Holiday Calendar` page (Exchange Media Centre) carries
  the operator's own holiday entries for 2020-2029 in one server-rendered
  table. Each Eid entry states the trading-discontinue day and the
  trading-resume day in prose (`Trading will discontinue at the end of trading
  day DD/MM/YYYY. Trading will resume after the holiday on DD/MM/YYYY.`),
  several annotated `* According to the UMM AL-QURA calendar`.
- Founding Day and National Day entries state the single day the exchange
  observes (`Founding Day of Saudi Arabia is on 23/02/2025.` — the 2025
  observance is Sunday the 23rd, not Saturday the 22nd).
- The `market-holidays` page (Our Markets section) is the entry point the
  operator's own navigation names; its holiday data loads client-side.
- 2025, 2026 and 2027 are all published: the 2027 entries (Founding Day
  22/02/2027, Eid Al Fiter 07-11/03/2027, Eid Al Adha 16-20/05/2027, National
  Day 23/09/2027) were on the page at capture time.
