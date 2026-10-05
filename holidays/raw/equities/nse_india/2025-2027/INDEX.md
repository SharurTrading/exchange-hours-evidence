# NSE India raw artifacts, 2025-2027

Retrieved 2026-09-28 UTC. T1: the operator's own published holiday-list banners; the JSON notes are the operator's own machine channel (T2) replayed verbatim from the archive.

| File | Source URL | Retrieved, UTC | sha256 |
|---|---|---|---|
| `wayback_20241223_nse_holiday_banner.jpg` | Wayback `id_` replay of <https://nsearchives.nseindia.com/web/sites/default/files/2024-12/Holiday%20List%20Web%20Banner.jpg> at capture `20241223224845` ("NSE Holiday List 2025") | 2026-09-28 | `22e29e5a236591c9dd64e9bf1788703da77d9d4934dbbc617668618668e3a115` |
| `wayback_20260108_nse_trading_holiday_list_banner.jpg` | Wayback `id_` replay of <https://nsearchives.nseindia.com/web/banner/2025-12/TradingHolidayList_636x555__final_20251218152820.jpg?w=1200> at capture `20260108142249` ("Trading Holiday List for Equity & Equity Derivatives — Calendar Year 2026") | 2026-09-28 | `4920fdb026e210d0badc135577871cd6383559fe82d93d164c830b9ffd04a89e` |
| `wayback_20250821_nse_cmsNote_equities.json` | Wayback `id_` replay of <https://www.nseindia.com/api/cmsNote?url=exchange-communication-holidays-equities> at capture `20250821072044` (market-timings note; gzip-compressed as replayed) | 2026-09-28 | `cb5f2beb9e685a58b4ba9cc1ad177912983ef88057c4aaac205c8eb256888a66` |
| `wayback_20260916_nse_getNotes20_equities.json` | Wayback `id_` replay of <https://www.nseindia.com/api/getNotes20?url=/resources/exchange-communication-holidays-equities> at capture `20260916045525` (post-CAS market-timings note; gzip-compressed as replayed) | 2026-09-28 | `20c69a1ca6fd37a969c3bb54e665bacb9b4844ffad4b1b7236feae7dbbd13f49` |

- The live `nseindia.com` web/API channel refused twice (homepage HTTP 403, `holiday-master` empty body, 2026-09-28); Wayback is the verbatim public mirror channel that worked.
- `holiday-master?type=CM` capture `20260909065333` holds an empty payload (digest of the empty string) and is not used. No `type=capital` captures exist.
- The two banners are the operator's own published trading-holiday lists for the capital-market/equities envelope. Both carry the Muhurat-Trading footnote with timings "notified/subsequently" — the special-session instants are unpublished in these artifacts.
- No 2027 list exists as of retrieval: NSE publishes the next year's list around December (the 2026 list was uploaded 2025-12-18). Closing condition: NSE's "Trading Holiday List — Calendar Year 2027" publication.
