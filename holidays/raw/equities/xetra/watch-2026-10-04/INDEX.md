# xetra LAW-WATCH re-check — 2026-10-04 UTC (#200, the `Trading calendar 2027` edition)

Fourth forward re-check (after the 2026-09-29 wave, the 2026-10-02
`forward-2027` re-check and the 2026-10-03 `recheck-2026-10` wave). Retrievals
00:01–00:09 UTC 2026-10-04; digests in `SHA256SUMS.txt`.

**Outcome: NOT-YET.** The `Trading calendar 2027` edition is not published.

- `db_trading_calendar_page.live-20261004T000300Z.html` — the live trading-calendar page
  (`https://www.cashmarket.deutsche-boerse.com/cash-en/trading/trading-calendar-and-trading-hours`,
  the same URL the 2026-10-02/03 reads used). Content-identical to the 2026-10-03 state: the
  only calendar PDF linked is
  `/resource/blob/4481276/1b643791fcb4d60bdd7f25efad3f4626/data/deutsche-boerse-trading-calendar-2026.pdf`,
  the named trading-holiday list is still scoped to `in the year 2026` (Ascension Day
  14 May 2026, Whit Monday 25 May 2026, Corpus Christi 4 June 2026 — no 2027 named list), the
  `On December 30, 2026, deviating trading hours may apply` note is unchanged, and the
  non-trading-days grid still carries the 2025-2031 columns.
- `xetra_com_trading_calendar_page.live-20261004T000130Z.html` — the xetra.com path
  (`https://www.xetra.com/xetra-en/trading/trading-calendar-and-trading-hours`) now 302s to the
  cash-market section root (`https://www.cashmarket.deutsche-boerse.com/cash-en/`); saved as the
  redirect-target read. The canonical page above is the operative artifact.
- `eurexgroup_xetra_trading_calendar_page.live-20261004T000200Z.html` — the operator group's
  mirror (`https://www.eurexgroup.com/xetra-en/trading/trading-calendar-and-trading-hours`),
  still the 2025-vintage edition (links only the 2025 and 2026 PDFs; one `2027` string, the
  non-trading-days column).
- `cdx_xetra_trading_calendar-20261004T000600Z.txt` — Wayback CDX of `xetra.com/resource/blob/*`
  filtered `trading-calendar`, `collapse=urlkey`: 15 rows, editions 2015-2026, newest capture
  2025-10-04 (the 2026 edition). No 2027 URL.
- `cdx_cashmarket_trading_calendar-20261004T000900Z.txt` — Wayback CDX of
  `cashmarket.deutsche-boerse.com/resource/blob/*` filtered `trading-calendar`: 27 rows, the
  URL set byte-identical to the 2026-10-03 dump (`diff` clean), newest capture 2026-04-18.
  No 2027 URL.

Next check: 2026-10-11 (weekly during the German publication season; the 2026 edition first
appeared in a Wayback capture dated 2025-10-04, so the 2027 edition is due this window).
Tracked as #200.
