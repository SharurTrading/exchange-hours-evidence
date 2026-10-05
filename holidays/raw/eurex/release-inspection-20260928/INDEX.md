# INDEX — Stage 7 release-month re-inspection, Eurex (eurex venue; eurex_fixed_income dormant)

Retrieval session: **2026-09-27 19:16–19:47 UTC** (`date -u`). Direct retrieval from www.eurex.com worked.
Prior holdings: `holidays/raw/eurex-2025-2027/` and `cfe-eurex-ice-cde-smfe-2026-2027/` (2026-09-12).

## Verdict: NOTHING NEW — the 2027 Trading Calendar edition still does not exist; the German tba line persists

- **Calendar archive page** (`tc_archive_page.html`, https://www.eurex.com/ex-en/trade/trading-calendar):
  contains `2027` **zero times**; the only calendar edition offered for download is
  `tradingcalendar_2026_en.pdf`. Identical state to PR #180's check earlier on 2026-09-27 — the
  `eurex_fixed_income` bound at 2027-01-01 stands.
- **Holiday regulations page** (`holiday_regulations.html`): normalized text 99.97% identical to the
  stored 2026-09-12 capture; the only added tokens are a nav item ("Quantitative Brokers"). Its
  "Non-trading days at Eurex 2026 - 2030" table was **already in the stored capture** (2027 ×8, 2030 ×11)
  — it is not new material; the evidence file's #157 record already reflects the page (which never
  carries the German tba note at all). `tba`/`to be announced` count on the page: 0, as stored.
- **Indicative calendars CSV 2027–2036**: re-fetched, sha256 `47b416226cf98a38fb2b02380c36a668b92cc0297bebfb36ff6e167c6cfe8c48`
  — **byte-identical** to the stored copy; still the operator's "preliminary and indicative … subject
  to change" publication, which cannot key rows (LAW-NO-FABRICATED-DATES).

## Artifacts

| file | url | retrieved (UTC) | sha256 |
|---|---|---|---|
| `tc_archive_page.html` | https://www.eurex.com/ex-en/trade/trading-calendar | 2026-09-27 19:47 | `229ed22b5fadc979fe125ed1d824370dedc9efdaec0e3b21c5a7de51f34125bd` |
| `holiday_regulations.html` | https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations | 2026-09-27 19:47 | `57a0f70e601e833da20add2cfea3c3f435f97498061b865887a95dccce1b3057` |
| `eurex_indicative_trading_calendars_2027-2036.csv` | https://www.eurex.com/resource/blob/5098674/ecf1bc8a3930b953bb90cc2b0a95b1e1/data/indicative-trading-calendars.csv | 2026-09-27 ~19:47 | `47b416226cf98a38fb2b02380c36a668b92cc0297bebfb36ff6e167c6cfe8c48` (= stored) |
