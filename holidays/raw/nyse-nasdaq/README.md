# nyse + nasdaq holiday corpus (2010-2027), retrieved 2026-09-27 UTC

Operator-corpus for the `nyse` and `nasdaq` holiday tables
(`activate-nyse-nasdaq`, equities wave 1 PR 1). Every artifact below is the
operator's own page or notice, read live or through a Wayback `id_` replay
(verbatim public mirror, LAW-PRIMARY-SOURCES T1), saved with its sha256 in the
`manifest.json` beside it. Retrieval date for everything here is
**2026-09-27 UTC** unless the manifest says otherwise.

## Layout

- `cdx/` — the Wayback CDX query dumps, kept so the archive search itself is
  reproducible.
- `nyse/live/` — the live `nyse.com/trade/hours-calendars` page (states 2026,
  2027 and 2028).
- `nyse/wayback-2010-2025-pages/` — one replay per NYSE holiday-page era
  (2010, late-2010, 2011, 2014, 2015-2025); the 2011 replay states the 2012
  and 2013 tables too, so no separate 2012/2013 captures exist.
- `nyse/notices/` — NYSE/Euronext and ICE press releases: Hurricane Sandy
  closures (2012-10-29, 2012-10-30) and the National Day of Mourning
  (2025-01-09). The extra `nyse_press_*` files in the Sandy window are the
  sibling releases fetched to identify the closure statements; only
  `1351243418010` (close Oct 29) and `1351243421978` (close Oct 30) key rows.
- `nasdaq/live/` — live `nasdaqtrader.com` calendar page and system-hours PDF,
  the live `nasdaq.com` holiday-schedule page and 2026 holiday PDF, and the
  per-year Nasdaq trading calendar PDFs 2021-2025 (corroboration only: their
  holiday marks are graphical, not text).
- `nasdaq/wayback-2010-2025-pages/` — one replay per year of the
  `nasdaqtrader.com` "U.S. Equity and Options Markets Holiday Schedule" page
  (2010-2025), plus the 2025-era `nasdaq.com` holiday-schedule capture
  (`nasdaq_holidaysched_2025MID.html`).
- `nasdaq/alerts/` — Nasdaq Trader alerts: `ETA2012-44` (Hurricane Sandy,
  closes 2012-10-29, keys a row) and home/RSS page captures that document the
  search; `ETA2011-49` and the 2011 home page are search negatives.
- `nasdaq/mics-2010-2017/` — **rejected corpus, kept as a rejection record**:
  87 "ISE Market Information Circulars". These are the International
  Securities Exchange's *options* circulars, not The Nasdaq Stock Market's
  cash-equity schedule, so nothing here keys a `nasdaq` row. Do not re-chase
  this directory for the equities table.

## Recorded refusals (channel discipline)

1. **Nasdaq cash-equity early-close times for 2010-11-26 and 2011-11-25.**
   The operator's own year pages print `Early Market Close* TBA` for the Nasdaq
   Stock Market (the options columns carry times; the cash market defers to
   "alerts"). Two attempts to recover those alerts (TraderNews alert ids via
   CDX, home-page headline captures) found nothing archived. Those two dates
   ship as `Unsourced`, not as invented 1:00 p.m. rows.
2. **Nasdaq Hurricane Sandy 2012-10-30 confirmation.** `ETA2012-44` states the
   2012-10-29 closure unconditionally but calls 10-30 "likely ... will
   confirm"; the confirming alert (`ETA2012-45` era) is not archived (4
   attempts: TraderNews ids, MFQS news page, home page, Market System Status).
   2012-10-30 ships as `Unsourced` for `nasdaq`.
3. **Nasdaq National Day of Mourning 2025-01-09 notice.** Six attempts
   (ECA/DN/ETA alert ids, nasdaqtrader home and RSS Jan 2025, nasdaq.com press
   center Dec 2024-Jan 2025, the operator's own 2025 holiday-schedule page
   captures, the 2025 trading calendar PDF text layer) recovered nothing that
   states it: even the operator's own 2025 sheet omits the day. 2025-01-09
   ships as `Unsourced` for `nasdaq`.

NYSE needs no refusal rows: Sandy (both press releases) and the mourning day
(ICE press release naming the New York Stock Exchange) were recovered, and
every early close 2010-2027 is printed on the operator's own pages.
