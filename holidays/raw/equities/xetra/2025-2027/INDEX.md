# Xetra (Deutsche Börse cash market) holiday artifacts, 2025-2027

Retrieved 2026-09-28 UTC by the hkex/xetra/six holiday-window activation.
Every artifact is the operator's own page or calendar (T1) read from
cashmarket.deutsche-boerse.com / xetra.com, live or through a Wayback `id_`
replay of the same URL.

| Artifact | Source URL | Capture / replay | Retrieved (UTC) | Tier | sha256 |
|---|---|---|---|---|---|
| `live_cashmarket_trading-calendar-and-trading-hours.html` | <https://www.cashmarket.deutsche-boerse.com/cash-en/trading/trading-calendar-and-trading-hours> | live | 2026-09-28 01:28 | T1 | `d70a8f5d54cb529103bf674ea8382702a3510800dac8b48965a43aa08ae4bca4` |
| `live_deutsche-boerse-trading-calendar-2026.pdf` | <https://www.cashmarket.deutsche-boerse.com/resource/blob/4481276/1b643791fcb4d60bdd7f25efad3f4626/data/deutsche-boerse-trading-calendar-2026.pdf> | live, linked from the page above ("Trading calendar 2026") | 2026-09-28 01:28 | T1 | `1edfc7b737ae1f5fe93179bfa9af59223b3c9d11cc8deddd127b386fb87e44b6` |
| `wayback_xetra_trading-calendar-and-trading-hours_capture-20250422T181518Z.html` | <https://www.xetra.com/xetra-en/trading/trading-calendar-and-trading-hours> | Wayback `id_` replay of capture `20250422181518` | 2026-09-28 01:28 | T1 | `44b6b2783375a17ac736ebc1c0247e0bae011f1a64c9ae125c602fea9ab41918` |
| `wayback_xetra-trading-calendar-2025.pdf` | <https://www.xetra.com/resource/blob/4064968/4079a2d5a9fec324905942b807b398ed/data/xetra-trading-calendar-2025.pdf> | Wayback `id_` replay (2025 archive of the PDF linked from the capture above) | 2026-09-28 01:28 | T1 | `84c71bed702dd753f4272939f9c65d87ebd9afdfc89ff7917d545b66c3f8a8e5` |

## Reading notes

- The page's `Non-trading days at Frankfurter Wertpapierbörse (FWB)` table is
  the operator's own list of closures for Xetra and Börse Frankfurt; the
  2025-04-22 capture carries the 2025 column, the live edition the 2026-2032
  columns. The per-year PDF calendars restate each year's closures in one
  sentence.
- `**` rows (Christmas Eve, New Year's Eve): "No trading but settlement is
  open" — full closures for the market clock, not early closes.
- The live page names 2026's trading holidays — Ascension Day (14 May 2026),
  Whit Monday (25 May 2026), Corpus Christi (4 June 2026) — and states:
  "Trading of shares and Exchange traded products on Frankfurt and Xetra ends
  on public holidays (Germany and State of Hesse) where trading takes place
  according to the FWB trading calendar at 20:00 CET." The 2025 capture words
  the same note over "Börse Frankfurt" only, so no 2025 Xetra early close is
  sourced.
- "On December 30, 2026, deviating trading hours may apply" is conditional;
  the 2026 PDF marks Dec 30 with `*)` "Trading hours may differ from normal
  trading days". Nothing is encoded from it.
- The 2027 early closes on German trading holidays are not yet named by any
  retrieved artifact (the page's named list is scoped to "the year 2026");
  only the page's 2027 closure column is encoded.
