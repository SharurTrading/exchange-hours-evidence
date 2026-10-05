# Eurex LAW-WATCH re-check — 2026-10-04 UTC (#157: the 2027 edition + the tba revision)

Fourth forward re-check of the eurex.com trading-calendar surface (after the
2026-09-12 retrieval, the 2026-09-26 `eurex-2025-2027/` wave and the 2026-10-03
live sweep). Retrievals 00:12–00:22 UTC 2026-10-04; digests in `SHA256SUMS.txt`.

**Outcome: NOT-YET on both halves.**

**(a) `Trading calendar 2027` — not published.**
- `eurex_trading_calendar_hub.live-20261004T001200Z.html` — the live hub offers only
  `tradingcalendar_2026_en.pdf` (blob 4873184/0ca7669a…); zero `2027` strings.
- `eurex_trading_calendar_archive.live-20261004T001300Z.html` — the live archive lists
  editions 2012-2026 (fifteen `tradingcalendar_20xx_en.pdf` blobs); zero `2027` strings.
- `cdx_eurex_tradingcalendar-20261004T002200Z.txt` — Wayback CDX of
  `eurex.com/resource/blob/*` filtered `tradingcalendar`, 2025-10-01..2026-10-05,
  `collapse=digest`, with CDX digests: no `tradingcalendar_2027` URL exists in the archive.
  The 2026 edition appears under three blob-hash variants (captures 2026-01-14, 2026-02-14,
  2026-09-08); the current variant the operator's own pages link is `0ca7669a…`.

**(b) German-scope line of the 2025/2026 editions — unrevised (still `tba` / `to be announced`).**
- `Eurex_Trading_Calendar_2025.live-20261004T001800Z.pdf` — live fetch of
  `…/blob/4242284/1c8da6dc2702d508ee2a4740654ea77d/data/tradingcalendar_2025_en.pdf`:
  sha256 `d51053a39e786022db3fa2f12e00d9646145db10aa308ea1bd4446ed0cd16614`, 161061 bytes —
  byte-identical to the stored edition (`../Eurex_Trading_Calendar_2025.pdf`), whose page 2
  carries the `… : tba.` German-scope line.
- `Eurex_Trading_Calendar_2026.live-20261004T001900Z.pdf` — live fetch of
  `…/blob/4873184/0ca7669a8cb9a2f917d99a801fb3f2de/data/tradingcalendar_2026_en.pdf`:
  sha256 `b0796b42819b38c0757d727d9b789360ba84cd0d45cea215544f86342158ac65`, 160721 bytes —
  byte-identical to the stored edition, whose page 2 carries the `…: to be announced` line.
- `Eurex_Trading_Calendar_2026.wayback-20260908135122.pdf` — Wayback `id_` replay of capture
  `20260908135122` of the same 2026 URL: byte-identical to the live fetch (`cmp` clean), so the
  served bytes are the operator's state since at least 2026-09-08.
- `eurex_holiday_regulations.live-20261004T001400Z.html` — the live Holiday regulations page:
  only the site-chrome Dynatrace agent line differs from the 2026-09-26 capture
  (`../eurex_holiday_regulations_2026.live-20260926.html`); still a 2026-only day-by-day
  section plus the "Non-trading days at Eurex 2026 - 2030" table. Hub and archive diffs are
  the same chrome-only pattern (agent tag; one logo URL made absolute).

Next check: 2026-10-11, weekly through the season; the 2026 edition was linked by a
2025-10-29 Wayback capture, so the 2027 edition is due in the coming weeks — 2026-10-29 is
the expected-notice horizon. Tracked as #157.
