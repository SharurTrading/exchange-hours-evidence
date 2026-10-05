# Evidence index — task `eurex/negation-2026-10-05`

The no-changes verification for **#157**: does any operator artifact state a
German-scope (FDAX/FDXM; German equity and equity-index derivatives plus the
Xetra-based ETF/ETC derivatives) closure in 2025 or 2026 beyond the all-derivatives
rows the crate ships — and if not, does the operator's own evidence affirmatively
say so? The maintainer's 2026-10-05 instruction: "we need to capture all changes to
trading hours + all holidays. If there were no changes, this could look like a gap
and not actually be one but that needs to be verified."

**Outcome: NO GERMAN-SCOPE CLOSURE EXISTS IN 2025 OR 2026, and the operator's own
evidence says so affirmatively.** Three independent operator statements, each read
from bytes in this store:

1. **The day-by-day Holiday regulations tables state what closed, and the German
   scope is absent from every row of both years.** The page's grammar demonstrably
   carries German-scope clauses when they exist: the Wayback capture 2020-10-26 of
   the same page prints `01 June || Eurex is closed for trading and exercise in
   German equity derivatives and equity index options (trading in German equity
   index futures takes place!) as well as ETF and ETC derivatives, which are based
   on Xetra® listings. …` — the 2020 arrangement, carve-out and all. In the
   controlling 2025 state (capture 2025-09-13, `../eurex-2025-2027/`) the 54-row
   table carries no German clause anywhere: Whit Monday 09 June lists only the
   Swiss/Norwegian/Danish closures, and Unity Day 03 October has no row at all in
   the June/September states. In the live 2026 state (retrieved 2026-09-26 and
   2026-10-04, text-identical again today) the 51-row table carries no German
   clause anywhere: Whit Monday 25 May lists the Swiss, ETC/British,
   Brazilian/Canadian/U.S., USD credit-index, Norwegian and Danish closures, and
   Unity Day 03 October (a Saturday) has no row. Full-text scans of the live page:
   `German` 0, `tba` 0, `to be announced` 0, `preliminar` 0.
2. **The announcement channel that dated every 2014-2018 German-scope closure has
   produced nothing for 2025/2026** (the complete 2026-10-04 sweep:
   `../circulars-2026-10-04/` — all 170 items of 2025 and 100 of 2026-to-date
   enumerated gap-free, zero German-scope items, circular 105/2025 stating FDAX
   unaffected on 30 December 2025). Re-checked today for the windows around the
   passed candidate dates: the production newsboard over Oct-Dec 2025 carries one
   item matching "holiday" — `XEUR: Trading in Swiss Option contracts with
   expiration 02-January-2026 suspended` (24 Nov 2025, Swiss scope) — and zero
   items over 2026-01-01..2026-10-05 for either "holiday" or "reminder", two days
   after Unity Day 2026.
3. **The standing rule makes the silence dispositive of Board intent.** Conditions
   for Trading 1.2 (consolidated edition effective 2026-07-27): "Exchange Trading
   of Derivatives takes place on Business Days on which Eurex Deutschland is open
   for business („Exchange Days“). The Trading Days for the respective Derivatives
   are basically identical with the Exchange Days provided that the Management
   Board does not make other regulations for the respective Derivatives." Exchange
   Rules § 60(2) (consolidated edition effective 2026-07-07) assigns the period
   determination to the Management Board per derivative. A German-scope closure is
   exactly such an other regulation — circular 080/2014 shows Board decisions of
   that kind are published as circulars — and the complete circular enumeration
   contains none. No rulebook clause states closures happen "only by circular";
   the 1.2 baseline-plus-Board-regulation structure is what the rulebook does say,
   and it is quoted for what it is.

The pattern evidence was re-read from the stored bytes in the same session: the
2019, 2020 and 2021 editions print `(trading in German equity index futures takes
place!)` with dates `10 June, 3 October` / `1 June` / `24 May`; the 2025 edition
prints the German-language `… : tba.` and the 2026 edition the English `… : to be
announced` (extractions re-run 2026-10-05 against the hash-verified PDFs in
`../eurex-2010-2024/` and `../eurex-2025-2027/` + its `watch-2026-10-04/`).

Retrieval session: **2026-10-05T00:05–00:09 UTC** (LAW-UTC-DATES). Plain `curl`
GETs with a desktop browser User-Agent on public, unauthenticated URLs; no access
control was evaded. `web.archive.org` again refused connections intermittently;
one 2020 capture succeeded and two retries (2021/2022 captures) failed with
connection errors — the CDX listing (query succeeded) shows the 2020-10-26 capture
as the page's earliest, so no 2014-2018 capture exists to fetch.

## Files

| File | Exact URL | Retrieved (UTC) | sha256 |
|---|---|---|---|
| `eurex_holiday_regulations.live-20261005T000545Z.html` | `https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations` | 00:05:45 | `a6e6f52f06dd008a0c6c8c974e1e563486183e52875a8a12c199627b8d0dddc8` |
| `newsboard_holiday_10012025-12312025.live-20261005T000545Z.html` | `…/production-newsboard/3486!search?query=holiday&dateFrom=10/01/2025&dateTo=12/31/2025&sort=sDate%20desc` | 00:05:45 | `eace00590e52247092292ae3adb974c2c7462ce623053d565feb477c8dd25e6d` |
| `newsboard_holiday_01012026-10052026.live-20261005T000545Z.html` | `…/production-newsboard/3486!search?query=holiday&dateFrom=01/01/2026&dateTo=10/05/2026&sort=sDate%20desc` | 00:05:45 | `553f36a30376e4bc14d790930e5a630a2ddda64ec30626d4643ce6ed26da0228` |
| `newsboard_reminder_01012026-10052026.live-20261005T000545Z.html` | `…/production-newsboard/3486!search?query=reminder&dateFrom=01/01/2026&dateTo=10/05/2026&sort=sDate%20desc` | 00:05:45 | `11b775da39b3b91ed0ccee4b356101648be935446fa3d1c0998752399e1e25d4` |
| `rules_landing.live-20261005T000639Z.html` | `https://www.eurex.com/ex-en/rules-regulations` | 00:06:39 | `aa90edcb8447a31eed2dfd10693d96966191dbd8ed32955a0a2087ecdefbbdb0` |
| `eurex_rules_regs.live-20261005T000659Z.html` | `https://www.eurex.com/ex-en/rules-regs/eurex-rules-regulations` | 00:06:59 | `1330b29a3a862c5f62f1c5f0d677900a802834e27d7539e7f9b82afff446714d` |
| `trading_hours_page.live-20261005T000659Z.html` | `https://www.eurex.com/ex-en/trade/trading-hours` | 00:06:59 | `95331792f59435facb81812e63102ada5db1486aea9c454cc288998e49952af5` |
| `exchange_rules.live-20261005T000732Z.html` | `https://www.eurex.com/ex-en/rules-regs/eurex-rules-regulations/01.-Exchange-Rules-53586` | 00:07:32 | `e69fd8918b23bdb799475fbe333b043d3783cea4f4c2f6a7534831fff54d3092` |
| `2026_07_07_eurex_d_boersenordnung_en.pdf` | `https://www.eurex.com/resource/blob/334918/a72a2163fa0bb8fac8d6c710e244bfd8/data/2026_07_07_eurex_d_boersenordnung_en.pdf` | 00:07 | `70ce32e4a374fa12da54bd7a1536e1aef745d6230e46e947f43b24a35dee7d59` |
| `2026_07_07_eurex_d_boersenordnung_en_h22.pdf` | `https://www.eurex.com/resource/blob/5366444/98fa29b651420c1fcdb488673e0e7c40/data/2026_07_07_eurex_d_boersenordnung_en_h22.pdf` | 00:07 | `b7960f09ab1a2968a88141def3ed075e8f7febcdb2b29762e71cca387dac1dc6` |
| `conditions_for_trading.live-20261005T000824Z.html` | `https://www.eurex.com/ex-en/rules-regs/eurex-rules-regulations/02.-Conditions-for-Trading-4060082` | 00:08:24 | `b7cc09d76a60fd0bb73e1fb2f98c3a9cb6ca6f900b0936deed052dcf76675a56` |
| `2026_07_27_eurex_d_handelsbedingungen_en.pdf` | `https://www.eurex.com/resource/blob/311224/9f99369a56e0d49b6ecb0038cfbf6e79/data/2026_07_27_eurex_d_handelsbedingungen_en.pdf` | 00:09 | `f799c7d1be48190d9bd5bd21a1beebcfa2758f020399c57f72e8b66c7f12d140` |
| `search_rules_tradinghours.live-20261005T000639Z.html` | circulars search, `query=Rulebook trading hours` | 00:06:39 | `2429f35a0337aecd83cadedfda2cfdb2f38fafd2981987ada33d6c456fa69e6f` |
| `holreg_wayback_20201026122009.html` | `https://web.archive.org/web/20201026122009id_/https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations` | 00:09 | `b23531c89384dacca120e9dfae1f8f65d793530e6c968c00dcec9f2fcebbc0e8` |

## Verdict

The no-changes hypothesis is **verified**. The `tba` line of the 2025/2026 Trading
Calendar editions never resolved because there was nothing to resolve: the
operator's own controlling day-by-day enumeration — in the grammar that printed the
German clause with its carve-out in 2020 — states no German-scope closure on any
date of either year, both years' candidate dates (Whit Monday 2025-06-09, Unity Day
2025-10-03, Whit Monday 2026-05-25; Unity Day 2026-10-03 a Saturday) have passed,
and the Board-regulation channel such a closure would travel is enumerated complete
and empty of it. The #157 declaration retires; 2025-01-01..2026-12-30 answers from
the shipped all-derivatives rows. Disclosed residual: if Eurex later dates a
2025/2026 German-scope closure after all, it lands as a schedule fix on the weekly
watch (the calendar editions and the Holiday regulations page are the named watch
points).
