# SIX — forward-horizon re-check, 2026-10-03 UTC

Second forward re-check (after the 2026-09-29 check). Three findings:

1. **No 2028 edition exists.** The `trading-guides/trading-calendar-2028.pdf`
   and `trading-guides-upcoming/trading-calendar-2028.pdf` URLs both return
   the operator's own 404 page, and the download centre's rendered document
   list carries no calendar beyond 2025. Coverage stays at 2027-12-31.
2. **The shipped rows' cited live URLs for 2026 and 2027 have been withdrawn
   since the last check.** `trading-guides/trading-calendar-2026.pdf` and
   `.../trading-calendar-2027.pdf` — which served the bytes the crate holds
   (sha256 `70d1b87d…` and `cd2fdca6…`) on 2026-09-28 and answered
   byte-identically on 2026-09-29 — now both return the operator's 404 page.
   This is a watch-channel change, not a data change: the row bytes stand as
   retrieved and digested in the store's `2025-2027/` directory, and the wayback
   CDX holds captures of the 2026 URL through 2026-04-20 (none of the 2027
   URL). Whether SIX is rotating the editions or restructuring the DAM is
   unknown from here; the monthly re-check watches for the reappearing or
   successor editions.
3. The 2025 PDF the store already holds (`trading-guides-upcoming/
   trading-calendar-2025.pdf`, sha256 `0729de0a…`) is still live and
   byte-identical to the shipped capture (re-fetched this pass).

| File | URL | Retrieved (UTC) | sha256 |
|---|---|---|---|
| `six_trading_calendar_2027_404.live-20261003T000653Z.html` | <https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2027.pdf> (HTTP 404 page) | 2026-10-03 00:06 | `81a8d5d7f6a57b568f7733e0d230d763a19e36ccac74905753002294a497153a` |
| `six_download_centre.live-20261003T000653Z.html` | <https://www.six-group.com/en/products-services/the-swiss-stock-exchange/trading/download-center.html> | 2026-10-03 00:06 | `4589effa1142d594e96aa6b59cef4ecb0c64c082ac13eeb3ea143e0ab201428d` |
| `six_trading_currency_holiday_calendar_page.live-20261003T000653Z.html` | <https://www.six-group.com/en/market-data/news-tools/trading-currency-holiday-calendar.html> | 2026-10-03 00:06 | `046a65422e1d62d49d7e966aced203647267146b65fe49a086c881c1945e06bf` |
