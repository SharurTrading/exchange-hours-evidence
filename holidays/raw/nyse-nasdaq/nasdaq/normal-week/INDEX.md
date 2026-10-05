<!-- SPDX-License-Identifier: MIT-0 -->

# nasdaq/normal-week — the SEC-filing and archived-page sweep (2026-09-30 UTC)

Closes the nasdaq half of #231: the carried 07:00–20:00 grid below 2013-03-18
is sourced from the operator's own statements in its SEC rule filings
(Federal Register full texts), the operator's own filing PDF for
SR-NASDAQ-2013-033 (which prints the marked Rule 4120(b)(4)(B) text and the
implementation day), and the operator's own pre-2013 nasdaqomx.com Trading
Hours page. Every artifact below was retrieved on 2026-09-30 UTC; sha256 as
shown. Evidence rows live in `docs/evidence/nasdaq.md` (`### Documents`).

## Keyed (cited by a Documents row)

| Store file | Document | Release / file no. | What it states | sha256 |
|---|---|---|---|---|
| `FR_2010_02_23_2010-3394.txt` | FR 2010-02-23, SR-NASDAQ-2010-008 | 34-61521 | The operator's quoted in-force rulebook text: IM-5250-1 states "Nasdaq market hours (7 a.m. to 8 p.m. ET)" four times (the filing's purpose statement repeats it once) — the floor-era envelope, in force at the 2010-01-15 filing | `8773a28b348bfcca3730a4229fba69516f937ae0a4da5dc6357a6636cfbcfe12` |
| `FR_2012_01_24_2012-1285.txt` | FR 2012-01-24 | — | Operator footnote citing Nasdaq Rule 4120(b)(4): the three sessions, Pre-Market 7 a.m.–9:30 a.m., Regular 9:30–4 p.m. (or 4:15), Post-Market to 8 p.m. | `c986d71f5581694b153d114ba7687086414485006cd3b3735dccf4b6f850c6b6` |
| `FR_2012_03_06_2012-5367.txt` | FR 2012-03-06 | — | Same 4120(b)(4) footnote (order granting approval) | `72e8461f11b44c14e999e51f177e27c3a563b3cbcba2b3423f8058daa2ab6c76` |
| `FR_2012_09_05_2012-21815.txt` | FR 2012-09-05 | — | Same 4120(b)(4) footnote, "Eastern time" wording | `dc16205617f178dd2ea1f56d8ced9489acb86d9ea2cacce3bb5c4b9f28935829` |
| `FR_2012_10_25_2012-26253.txt` | FR 2012-10-25 | — | Same 4120(b)(4) footnote, "7:00 a.m." wording (order approving) | `67bac20d532718052b3b5a79d23e2b04812ec46a4e9a5690349fa74d4fb8d5fa` |
| `nasdaqomx_tradinghours_wayback-20120325161230id_.html` | nasdaqomx.com Trading Hours page | — | "The NASDAQ Stock Market Trading Sessions (Eastern Time) Pre-Market Trading Hours from 7:00 a.m. to 9:30 a.m. Market Hours from 9:30 a.m. to 4:00 p.m. After-Market Hours from 4:00 p.m. to 8:00 p.m. Quote and order-entry from 7:00 a.m. to 8:00 p.m." | `a79bb35c8fd5dd04a1dc450297df8f89afc00da17bc8c0035306539f70b77d10` |
| `nasdaqomx_tradinghours_wayback-20120506131531id_.html` | same page, capture 2012-05-06 | — | identical grid | `a1b8c6dc6ef6f8976cbbc6fb8815b216c27eba146a76ef26095d3ad4d684d6ae` |
| `nasdaqomx_tradinghours_wayback-20120922200838id_.html` | same page, capture 2012-09-22 | — | identical grid | `aea6d39bf6d8ef5f86adca4e75310cbe53200d5e10d67b07c3f611302bc6eaf3` |
| `nasdaqomx_tradinghours_wayback-20120924001331id_.html` | same page, capture 2012-09-24 | — | identical grid | `5b8b945d0f280e9a7e78261f9e31893b48d547d490e93a2f4bb20679453afb4c` |
| `nasdaqomx_tradinghours_wayback-20121005120912id_.html` | same page, capture 2012-10-05 | — | identical grid | `a0edbe4d3d3b57a9deddf466c7197224337cf355e83cb546be4b517998eb14c6` |
| `FR_2013_02_28_2013-04614.txt` | FR 2013-02-28 | — | Same 4120(b)(4) footnote (order approving), three weeks before the cutover | `3bcf140b8fff571c2bd18ec77286cd244e8328f3f81650540629f36155093ef5` |
| `FR_2013_03_21_2013-06479.txt` | FR 2013-03-21, SR-NASDAQ-2013-033 ("the 4 a.m. Filing") | 34-69151 | The Exchange's own Background: "the pre-market session which runs from 7:00 a.m. to 9:29:59 a.m.; the regular session which runs from 9:30 a.m. to 4:00 p.m.; and the post-market session which runs from 4:00:00:01 p.m. to 8:00 p.m."; filed 2013-03-05, effective upon filing | `41d83bdf0e3ad7c70efc66a9de79877b64632487709d142126eb6b3221f94c72` |
| `SR-NASDAQ-2013-033_wayback-20210115152527id_.pdf` | the operator's own 19b-4 filing PDF | SR-NASDAQ-2013-033 | "NASDAQ will implement this proposal on March 18, 2013"; Exhibit 5 marks Rule 4120(b)(4)(B) "[7:00] 4:00 a.m. and continues until 9:30 a.m.", and (C)/(D) state Post-Market "4:00 p.m. or 4:15 p.m. … until 8:00 p.m." and Regular "from 9:30 am. until 4:00 p.m. or 4:15 p.m."; Rule 4420(i)(7) carries the per-series "as specified by Nasdaq" 4:15 designation | `fe71e4f64fff33fbe6d4fb54619b60a261570b4ccf209f15eef3825c570cafc8` |
| `FR_2013_06_13_2013-13998.txt` | FR 2013-06-13 | — | Conforming filing to "the 4 a.m. Filing": rule 4120(c)(7)(B) "7 a.m." to "4:00 a.m." — no new boundary (bounded-search record) | `db82e74989cc1950a094ef217b751b3f1cd0a0d4b5735cbeabfa612f20f06e90` |

The pre-existing `nasdaq_sys_hours.wayback-*.pdf` pair (the 2010 systems-hours
help-desk negative, `NASDAQ-SYS-2010-A`/`-B`) lives here from the 2026-09-30
bounded search; its rows are unchanged.

## Unkeyed bycatch (sweep records, no row cites them)

- `FR_2010_05_24_2010-12422.txt` (S&P 500 trading-pause filing, LULD pilot),
  `FR_2010_06_28_2010-15543.txt` (Rule 4120(a)(11) pause), `FR_2010_07_07_2010-16408.txt`
  (Russell 1000 halt list), `FR_2010_12_10_2010-31051.txt`,
  `FR_2011_08_17_2011-20905.txt`, `FR_2011_10_20_2011-27136.txt` — Nasdaq LLC
  rule filings of the era that restate no session hour (negative sweep).
- `FR_2011_03_25_2011-7109.txt` — NASDAQ OMX BX's parallel 8 a.m.→7 a.m.
  start-time filing (BX Rule 4120(b)(4)(B) marked text). Corroborates the
  already-keyed `nasdaq_bx` 2011-04-18 row; keys nothing here.
- `FR_2012_02_09_2012-2994.txt`, `FR_2012_03_30_2012-7516.txt` — cite Rule
  4120 without printing the grid.

## Negative channels swept (2026-09-30 UTC)

- Federal Register full-text API, 2010-01-01..2013-12-31: "pre-market session",
  "post-market session", "extend the pre-market", "Rule 4120", "three trading
  sessions on the Exchange" — the only session-hour change language in the
  window is SR-NASDAQ-2013-033 itself plus its conforming filing 2013-13998.
  The 4120(b)(4)-footnote practice begins 2012-01-24 (2012-1285); no earlier
  FR document states the interior grid.
- EDGAR full-text search ("pre-market session", any form, 2010-01-01..2013-06-30):
  0 hits — the Nasdaq 10-K channel states no market-hours session text in the era.
- nasdaqtrader `TradingHours` page and `ETA2013-21`: still no 2010-2013
  captures (the 2026-09-30 PAGE-channel negative stands).
- nasdaqomx.cchwallstreet.com (the electronic manual the filings mark against):
  asset-only captures; no rule content.
- Wayback CDX for the nasdaqomx.com Trading Hours page: five captures
  2012-03-25..2012-10-05 (all fetched); none before 2012-03-25, so the page
  witnesses from March 2012 and the floor statement is the 2010-008 quoted
  rulebook text.
