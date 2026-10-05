# Evidence index — `equities/six/cdx-retry-2026-09-30`

The CDX-service-back retry of issue #212's 2010-2011 and 2018-2019 spans,
run 2026-09-30 ~01:30-02:20 UTC (LAW-UTC-DATES). Verbatim CDX outputs saved
as `cdx-*.json`:

- `cdx-six-swiss_trading_calendar.json` — domain-wide `trading_calendar`
  filter of six-swiss-exchange.com: the per-year PDF series starts at
  `trading_calendar_2012.pdf` (capture 20111210134722); no 2010 or 2011
  edition at any URL.
- `cdx-six-group_trading-calendar.json` — domain-wide `trading-calendar`
  filter of six-group.com: the dam-path series starts at
  `trading-calendar-2020.pdf` (capture 20201128083137); no 2018 or 2019
  edition.
- `cdx-six-group_calendar.json` / `cdx-six-group-exchanges-calendar.json`
  (47 116 bytes / 46 rows) — domain-wide and `/exchanges/` prefix calendar
  sweeps: the only 2019-era operator calendar pages are the
  `trading_and_settlement_calendar_*.html` set (shares 2019-04-11, bonds
  2019-04-10/08-20, funds 2019-03-27, ETP 2019-08-22, participants
  2019-07-06), the 2019-10-18 landing page, and the Currency Holiday grids
  (`funds .../calendar/2019/grid_en.pdf` 2019-11-14, `shares .../2019/`
  2019-11-15).
- `cdx-six-swiss_calendar-all.json` (266 url keys) — domain-wide `calendar`
  filter of six-swiss-exchange.com: for 2010-2011 only the per-segment
  Currency Holiday grids (`shares|bonds|funds|exchange_traded_products
  /trading[_ calendar]/calendar/2010|2011/grid_*.html|pdf`); the ajax
  `trading-calendar.json` T2 feed survives only as 2024-era 301s.

Row-bearing candidate fetches, all ruled out:

| File | Capture | Retrieved (UTC) | sha256 | What it is |
|---|---|---|---|---|
| `six-grid-2010.wayback-20100131011433id_.html` | `20100131011433` | 2026-09-30T02:09:38Z | `7193224de1631a09b1a060c9bd509b380cba857fe61ca96c7c10c6a40d2e12f9` | shares Currency Holiday grid 2010 — the page's own sentence: *The SIX Swiss Exchange settlement calendar shows the days on which national banks are closed for a public holiday ... There is no settlement on these days.* Settlement data, not trading closures. |
| `six-grid-2011.wayback-20101115080111id_.html` | `20101115080111` | 2026-09-30T02:09:39Z | `6ec1cb92aa42b5ab243300c1646e2d04aca2385594c004edc17a2d85ffc6de9e` | shares Currency Holiday grid 2011 — same instrument. |
| `six-shares-grid-2019.wayback-20191115200708id_.pdf` | `20191115200708` | 2026-09-30T02:15:00Z | `5ac21f0f46051e6ee7497f135afdc3a2ec053b6250f537a5dcc487186d2a0931` | *Currency Holiday Calendar 2019* PDF — *Any dates not included in the settlement calendar are considered normal trading days*. Settlement data, not trading closures. |
| `six-tsc-shares-2019-04.wayback-20190411184205id_.html` | `20190411184205` | 2026-09-30T02:15:01Z | `986b126fcb3f9c19aa4f7515a8202e28c08b411aec80163b474a18bab989311d` | shares Trading and Currency Holiday Calendar page: *The trading calendar 2019 [pdf] shows on which days there is no trading* — links `/exchanges/download/participants/regulation/trading_guides/trading_calendar_2019.pdf`, a file no capture holds. |
| `six-tsc-participants-2019-07.wayback-20190706073518id_.html` | `20190706073518` | 2026-09-30T02:15:02Z | `5d937e18f3c0a6dc7b1bc2e193b0f9b7667ea9707da04444121a60baaad84a51` | participants variant of the same page, same link. |
| `six-tsc-landing-2019-10.wayback-20191018155838id_.html` | `20191018155838` | 2026-09-30T02:17:47Z | `fcee1eb6ffd692143991e48f9838d6e53e2dc29c1428706de730d6efe99aa2d0` | the 2019-10-18 landing page, linking the same 2019 trading-calendar PDF. |

Live checks 2026-09-30 ~02:20 UTC: `/exchanges/download/.../trading_calendar_2019.pdf`
and `..._2018.pdf` return 301 to the products-services home page;
`dam/...trading-guides/trading-calendar-2019.pdf` and `-2018.pdf` return 404.
Full sha256s in `SHA256SUMS.txt`.
