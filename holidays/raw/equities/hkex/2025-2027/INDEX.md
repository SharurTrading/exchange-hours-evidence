# HKEX holiday artifacts, 2025-2027

Retrieved 2026-09-28 UTC by the hkex/xetra/six holiday-window activation.
Every artifact is the operator's own page (T1) read from hkex.com.hk, live or
through a Wayback `id_` replay of the same URL.

| Artifact | Source URL | Capture / replay | Retrieved (UTC) | Tier | sha256 |
|---|---|---|---|---|---|
| `live_hkex_trading-calendar-and-holiday-schedule_2026-2027.html` | <https://www.hkex.com.hk/Services/Trading/Derivatives/Overview/Trading-Calendar-and-Holiday-Schedule?sc_lang=en> | live ("Updated 31 Jul 2026") | 2026-09-28 01:28 | T1 | `c460176b89fa6bbcfc77393e0013cc27bf03de9cb660367a1e2990b657d87f47` |
| `wayback_hkex_trading-calendar-and-holiday-schedule_capture-20251007T115724Z.html` | same URL | Wayback `id_` replay of capture `20251007115724` ("Updated 21 Aug 2025") | 2026-09-28 01:28 | T1 | `9914f794f9df82e35b83d0d4b2abd120e5cb524655e9ff16857b6319828a2390` |
| `wayback_hkex_trading-calendar-and-holiday-schedule_capture-20260213T065549Z.html` | same URL | Wayback `id_` replay of capture `20260213065549` ("Updated 16 Jan 2026") | 2026-09-28 01:28 | T1 | `a88c8d316588eab88f1597dbb018e3d6cbc0e5b0e471edd1036936b3dd2b0b68` |
| `live_hkex_securities-market_trading-hours.html` | <https://www.hkex.com.hk/Services/Trading-hours-and-Severe-Weather-Arrangements/Trading-Hours/Securities-Market?sc_lang=en> | live ("Updated 16 Sep 2017") | 2026-09-28 01:28 | T1 | `9faebf6ae87c7c21f83fc906a0709416f213ccf08147931cff6a03693d4b3e6c` |

## Reading notes

- The `Trading Calendar and Holiday Schedule` page is HKEX's own market
  holiday schedule; its `Holiday Schedule` table names every day the markets
  are closed (`Holiday (no trading)`) and the `Notes` block names every
  shortened eve (`no afternoon and after-hours trading session`) for 2025,
  2026 and 2027.
- The Oct-2025 capture governs the 2025 rows; the live edition (31 Jul 2026)
  governs 2026 and 2027; the Jan-2026 capture corroborates 2026 unchanged.
- The securities-market hours page carries the half-day schedule with its own
  times: Closing Auction Session `12:00 noon to a random closing between
  12:08 p.m. and 12:10 p.m.`, and the note that there is no Extended Morning
  Session and Afternoon Session on the eves of Christmas, New Year and Lunar
  New Year.
- Severe-weather halts (typhoon signals) are conditional and appear nowhere in
  these rows. The live page's `Derivatives Holiday Trading` product scope and
  the `#` MSCI after-hours footnotes are derivatives-only and do not touch the
  securities envelope.
- The 2026 table ends at `25/12/2026 (Friday) Christmas Day` in all three
  editions retrieved: no `28/12/2026` row ships.
