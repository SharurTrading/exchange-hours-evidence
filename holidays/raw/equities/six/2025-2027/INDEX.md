# SIX Swiss Exchange holiday artifacts, 2025-2027

Retrieved 2026-09-28 UTC by the hkex/xetra/six holiday-window activation.
Every artifact is the operator's own Trading Calendar PDF (T1) read from
six-group.com, live or through a Wayback `id_` replay of the same URL.

| Artifact | Source URL | Capture / replay | Retrieved (UTC) | Tier | sha256 |
|---|---|---|---|---|---|
| `live_six-trading-calendar-2026.pdf` | <https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2026.pdf> | live (download centre, "Entry into force date: Jan 1, 2026") | 2026-09-28 01:28 | T1 | `70d1b87db3e65d487159f660e9daec2fc68c6cb53385483c0af7bf99591c9390` |
| `live_six-trading-calendar-2027.pdf` | <https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides/trading-calendar-2027.pdf> | live (download centre, "valid as of 1 July 2026") | 2026-09-28 01:28 | T1 | `cd2fdca6f0083709bd9100d30b10415b2f0fce0b0b74b54b7e73f901fb318037` |
| `wayback_six-trading-calendar-2025_capture-20250505T133302Z.pdf` | <https://www.six-group.com/dam/download/the-swiss-stock-exchange/trading/trading-provisions/regulation/trading-guides-upcoming/trading-calendar-2025.pdf> | Wayback `id_` replay of capture `20250505133302` | 2026-09-28 01:28 | T1 | `0729de0a843ee2e22d50271d2bbc6fef8b031a133d392cd700f7db38878b1ed2` |

## Reading notes

- Each PDF is one A4 page of twelve month grids with a legend: light blue
  `Saturday — Market Closed`, lighter blue `Sunday — Market Closed`, dark blue
  `Market Holiday — Market Closed`. The dark cells were resolved from the PDF
  vector fills (fill rgb ≈ (0.0, 0.17, 0.37)) with the day number read from
  the word inside the same cell rect.
- Marked (weekday) holidays: 2025 — Jan 1, Jan 2, Apr 18, Apr 21, May 1,
  May 29, Jun 9, Aug 1, Dec 24, Dec 25, Dec 26, Dec 31 (12); 2026 — Jan 1,
  Jan 2, Apr 3, Apr 6, May 1, May 14, May 25, Dec 24, Dec 25, Dec 31 (10, the
  Aug 1 and Dec 26 holidays falling on Saturday); 2027 — Jan 1, Mar 26,
  Mar 29, May 6, May 17, Dec 24, Dec 31 (7, the Jan 2, May 1, Aug 1, Dec 25
  and Dec 26 holidays falling on a weekend).
- The calendars print closures only: no early close and no late open anywhere
  in the three years, so no scalar row other than `Closed` is sourced.
