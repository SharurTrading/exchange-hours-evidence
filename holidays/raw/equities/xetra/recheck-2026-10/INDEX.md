# xetra live re-check — 2026-10-03 UTC

The #200 re-check wave's artifacts. All retrievals 08:59-09:28 UTC 2026-10-03
unless the filename says otherwise; digests in `SHA256SUMS.txt`.

- `db_trading_calendar_page.live-20261003T085958Z.html` — the live trading-calendar page
  (byte-identical to the 2026-10-02 read except one site-chrome script tag)
- `eurexgroup_xetra_trading_calendar_page.live-20261003T090213Z.html` — the operator group's
  own 2025-vintage mirror, live
- `db_circulars_listing.live-20261003T090407Z.html` + the three `db_circulars_listfeed*`
  files — the circulars channel (no 2025 holiday-hours item)
- `wayback_xetra_page_2025*.html` (four) — the 2025-era editions the narrowing rests on
  (Wayback 2025-08-06, 2025-09-13, 2025-10-29 EN; 2025-10-04 DE; the 2025-04-22 capture
  pre-exists under the 2010-2024 directory)
- `cdx_cashmarket_trading_calendar-20261003T092819Z.txt` — CDX enumeration of every
  `trading-calendar` PDF on both hosts (2003-2026 only, no 2027)
