# INDEX — euronext-gaps-2026-10-13 (Amsterdam derivatives floor; 2026 year-end instants; 2027 calendars)

Retrieval performed 2026-10-13T23:25Z–2026-10-14T00:10Z (UTC) from this machine.
Wayback artifacts are `id_` raw replays; the timestamp in each filename is the
capture time (UTC) and dates the observation, not the state. Live retrievals
carry their retrieval stamp in the filename. Tier: T1 throughout (operator's own
pages, press releases and portals; `nyx.com` is the then-parent operator's own
corporate site). sha256 in `SHA256SUMS.txt`; extraction with verbatim quotes in
`EXTRACTION-NOTES.md`. Mission: issue #332's three Euronext gaps.

## Amsterdam derivatives floor (`amsterdam-floor/`)

| file | document | URL | capture/retrieval (UTC) | sha256 | what it witnesses |
|---|---|---|---|---|---|
| `NYSE_Liffe_to_extend_AEX_index_futures_opening_hours.pdf` | NYSE Liffe news release, Monday 3 August 2009: "extend trading hours in its AEX index futures contract from the current close of 11.15hrs until 15.00hrs Chicago time, with immediate effect"; CAC 40/FTSE 100 futures "already trade until 15.00hrs Chicago time" (Chicago-anchored; no local instants printed) | <https://www.euronext.com/sites/www.euronext.com/files/NYSE_Liffe_to_extend_AEX_index_futures_opening_hours.pdf> | Wayback `id_` replay of capture `20181107205935`, retrieved 2026-10-13T23:32Z | `85abac4b4709e4cfec6e9e80f191bd9d18020555f89752b77773d8e23697cf07` | the first pre-floor-era operator statement of the Amsterdam derivatives day in the store: the pre-2009-08-03 AEX futures close (11.15 Chicago) and the unconditional day-level extension to 15.00 Chicago from 2009-08-03; open side not printed |
| `press-release-page.wayback-20220813094213id_.html` | the same release on euronext.com's live press-release archive (verbatim body, dateline "…, 3 August 2009") | <https://www.euronext.com/en/about/media/euronext-press-releases/nyse-liffe-extend-aex-index-futures-opening-hours> | Wayback `id_` replay of capture `20220813094213`, retrieved 2026-10-13T23:30Z | `e1436ebcb82e1aeb3f4f614e0b9466a6354075b8e44241425f62d2d57a22638f` | stable live citation for the PDF above |
| `nyseliffe-calendars-hours-nl.wayback-20111126202420id_.html` | NYSE Liffe "Calendars & Hours" page, nl locale (the parent site's "Amsterdam & Brussels Markets" view), as of 2011-11-26 | <http://globalderivatives.nyx.com/nl/nyse-liffe/trading-hours> | Wayback `id_` replay of capture `20111126202420` (the page's only 200-status capture), retrieved 2026-10-13T23:48Z | `7784547f488b954f7e46b61edefd5d5de9f86f6cd5557476bd404ea6f071c471` | 2011 derivatives holidays (Good Friday 22 Apr, Easter Monday 25 Apr, Public Holiday 26 Dec); 2011 eves: "Continental … Index Products … will be open for a full day"; links the hours-grid PDFs (`liffeconnect_tradinghours211111.pdf`, `lon3526_0.pdf`, `608001.pdf`, the 2009 trading-manuals appendix `509415_0.pdf`) — **all with zero Wayback captures**; page prints no times inline |
| `nyseliffe-calendars-hours-en.wayback-20110710100224id_.html` | the same page, en locale, as of 2011-07-10 | <http://globalderivatives.nyx.com/en/nyse-liffe/trading-hours> | Wayback `id_` replay of capture `20110710100224`, retrieved 2026-10-13T23:55Z | `b9a74e69428fa4c319eedb0787fbcedbf718bbed87e77078a5945556ee6e2081` | identical 2011 holiday/EOY prose; links the earlier hours edition `507371_1.pdf` ("LIFFE CONNECT® trading hours 01 Jul 2011") — zero captures |
| `nyx-holidays-and-hours-nyse-liffe.wayback-20120411150803id_.html` | NYSE Euronext corporate "Holidays & Hours > NYSE Liffe", as of 2012-04-11 (earliest capture of the path) | <http://www.nyx.com/en/holidays-and-hours/nyse-liffe> | Wayback `id_` replay of capture `20120411150803`, retrieved 2026-10-13T23:42Z | `a08143e3da674e244b50a9085560842ff1bdf24de2b6352e98b4b9713934555b` | 2012 derivatives holiday list; the 2012 eves instants — "the Exchange will commence the closing of its derivatives contracts from midday GMT (13.00 hours CET)" on 24/31 Dec 2012; UK-only days expressly not Amsterdam closures; routes the nl locale as "Amsterdam & Brussels Markets" |
| `nyx-holidays-and-hours-euronext.wayback-20120411182349id_.html` | NYSE Euronext corporate "Holidays & Hours > Euronext" (cash), as of 2012-04-11 (earliest capture of the path) | <http://www.nyx.com/en/holidays-and-hours/euronext> | Wayback `id_` replay of capture `20120411182349`, retrieved 2026-10-13T23:42Z | `5fa4de1febca9ee553f1e126be9587d3aaaaf10148b77cd88f2a279c74df4009` | legacy cash grid "09:00-17:30" continuous + "17:35-17:40" TAL (2012 witness — postdates the floor, corroboration only, does not meet the Amsterdam closing condition; the 07:15 row is the TCS reporting tool, not a trading phase); 2012 cash holidays; eves "close at 14:00 CET" |

## 2026 year-end and 2027 watch (`year-end-2026/`)

| file | document | URL | retrieval (UTC) | sha256 | what it witnesses |
|---|---|---|---|---|---|
| `euronext_trading-hours-holidays.live-20261013T2345Z.html` | Euronext live "Trading hours & holidays" page | <https://live.euronext.com/en/resources/trading-hours-holidays> | live, 2026-10-13T23:45Z | `81434fa4d875ab8c8e4b596000bc3975efb8a799748ee38f732f15cf6b0208a7` | the "2026 end of year Trading hours" callout prints **"To be announced"** — no 2026 EOY appendix yet (extends the crate's 2026-10-09 negative); closer named in prose: "an end of year appendix to the Euronext Instructions 4-01 4-03 Trading Manuals"; **zero "2027" occurrences** — no 2027 calendar; standing "Cash markets trading hours" link = `media/1927/download` (XLSX, the current Appendix of Trading Manual 4-01, already crate-cited); "Derivatives markets trading hours" link `media/295/download` is a stale URL now serving a JPEG |
| `meff_market-notices.live-20261014T0000Z.html` | MEFF Market Notices list | <https://www.meff.es/ing/Financial-Derivatives/Market-Notices> | live, 2026-10-14T00:00Z | `42b0f5fd208b29d506baee8095ba120ac7bd2c47bebdf8d66a351bf7b5aa26c2` | complete 2026 list through 24/09/2026 (2601–2618, GEN01/02-26): **no December-hours comunicado yet**; prior editions MEFF 14/2024 (2024-06-14) and MEFF 49/2025 (2025-11-07) are banked in `meff-ibex-2026-10-11/` and date the genre's publication to ~early November |
| `meff_trading-calendar.live-20261014T0005Z.html` | MEFF Trading Calendar page | <https://www.meff.es/ing/Trading-Calendar> | live, 2026-10-14T00:05Z | `9650351f4b8e0f2c7fca604247ca4a5f6b2774f2151e1a62eceac9ba2826ac1b` | "Note: On 24 and 31 December the BME markets will trade until 14:00 hrs CET." (current-year page; three "2026" strings, zero "2027") — the derivatives-relevant year-end note live at T1 |

Banked artifacts cited but not re-fetched by this wave (already in the store,
verified during this hunt): `normal-weeks/meff-ibex-2026-10-11/bme-2026-calendar-release.html`
(canonical `bolsasymercados.es/en/media/press-releases/2025/spanish-financial-markets-2026-trading-calendar.html`,
dated 2025-11-20: "On Thursday, 24 December and Thursday, 31 December, the
market will be open until 2:00 pm." — the BME cash 2026 year-end instants),
`…/Comunicado-2414…pdf` (MEFF 14/2024) and `…/Comunicado-2549…pdf` (MEFF 49/2025,
2025-11-07, "el mercado cerrará a las 14:00h" for the 2025 eves).

## Verdicts

1. **Amsterdam derivatives floor — partial FOUND.** Floor-era session-language
   statements secured (2009-08-03 close extension with both values; 2011/2012
   derivatives holiday + year-end statements). The floor-era **normal-week
   grid** (open/local close) is NOT recovered: the operator's own grid PDFs
   (`507371_1.pdf`, `liffeconnect_tradinghours211111.pdf`, `509415_0.pdf`,
   `608001.pdf`, `lon3526_0.pdf`) are named by the archived pages but have
   zero Wayback captures. Best next channels: member-firm archives or an
   operator request for those documents; a Wayback rescan; the never-captured
   quicktabs tab content.
2. **2026 year-end instants.** Euronext: NOT YET PUBLISHED ("To be announced",
   2026-10-13 UTC) — watch the live page for the EOY appendix to Instructions
   4-01/4-03. BME cash: FOUND (banked 2025-11-20 release). MEFF: calendar note
   FOUND live ("trade until 14:00 hrs CET"); the MEFF-specific comunicado is
   expected ~early November 2026 on the Market Notices page.
3. **2027 calendars — NOT PUBLISHED** (Euronext live page zero "2027";
   MEFF calendar zero "2027"). Expected: Euronext INFO-FLASH CADE series
   mid-October–early November 2026 (per `if171020cade`/`if181018cade`/
   `IF251107CADE` naming); BME press release ~20 November 2026; then the
   MEFF calendar page turn.
