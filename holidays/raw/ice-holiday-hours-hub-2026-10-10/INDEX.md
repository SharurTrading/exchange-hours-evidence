# INDEX — `ice-holiday-hours-hub-2026-10-10` (Channel E: the ICE trading-hours page's new home)

Retrieval session: **2026-10-10 02:05–02:15 UTC** (`date -u`). All times UTC (LAW-UTC-DATES).

`https://www.ice.com/futures-us/trading-hours` (and `https://www.ice.com/trading-hours`) 404 live.
The current-schedule monitoring entry point moved: the live `https://www.ice.com/futures-us`
navigation carries a **`/holiday-hours`** item ("Holiday Hours") beside a
`/productguide/Search.shtml?tradingHours=` item, and **`https://www.ice.com/holiday-hours`** answers
200. The page is a hub of the operator's own schedule PDFs — it prints no holiday-hours table
inline — and its ICE Futures U.S. entry is
`https://www.ice.com/publicdocs/futures/IFUS_Trading_Hours_Holiday_Calendar.pdf`, re-fetched live on
2026-10-10 and **byte-identical** (sha256 `da97503545a3fb7607948367d30896685e220b36abed24aa02bbe1a21acb2817`,
113821 bytes) to the 2026-edition copy the store already holds
(`holidays/raw/cfe-eurex-ice-cde-smfe-2026-2027/IFUS_Trading_Hours_Holiday_Calendar.pdf`), so the
hub's calendar has not changed since the 2026-09-12 retrieval and this channel contributes no new
hours. The documents this wave worked up arrived through the notices listing service instead (see
`../iceus-notices-service-2026-10-09/INDEX.md`).

| file | sha256 | bytes | source url | captured (UTC) | what it is |
|---|---|---|---|---|---|
| `holiday-hours-2026-10-10.html` | `74d96322b35f27c6fbabb85cd4086a794f686b1bdb36bc8b5da0237119ac22cd` | 96326 | https://www.ice.com/holiday-hours | 2026-10-10 02:07 | The new hub page: links to `IFUS_Trading_Hours_Holiday_Calendar.pdf`, `Trading_Schedule.pdf` (Europe), `IFEu_Christmas_New_Year_Trading_Hours_2025.pdf`, `IFSG`, `IFAD`, Endex, Swap Trade schedules. No inline tables. |
| `futures-us-home-2026-10-10.html` | `54848ece3c50f0db18c0cd68c848588673be7028d4c2861a53396dab640150ec` | 141163 | https://www.ice.com/futures-us | 2026-10-10 02:05 | The live section home whose navigation names `/holiday-hours` — the provenance of the new entry point. |
