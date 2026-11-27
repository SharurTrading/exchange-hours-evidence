# Evidence index — `normal-weeks/eex-timetable-2026-11-14`

Capture for the current **EEX derivatives trading-hours timetable** edition,
which replaces the 2025-07-01 edition the `eex` row's evidence file cited
(`20250701_Trading_Hours_on_EEX_Derivatives_Markets_.pdf` now returns HTTP 404;
verified by GET and HEAD at retrieval).

Retrieval session: **2026-11-14 07:12 UTC** (LAW-UTC-DATES). `curl` with a desktop
browser User-Agent; no access control evaded. Sibling filename probes
(`20260101_…`, `20260401_…`, `20260701_…`, `20261001_…`, `20261101_…`,
`20270101_…`) all 404, so 2026-09-04 is the current edition.

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `20260904_Trading_Hours_on_EEX_Derivatives_Markets_.pdf` | `https://www.eex.com/fileadmin/EEX/Downloads/Trading/Trading_Hours/20260904_Trading_Hours_on_EEX_Derivatives_Markets_.pdf` | 2026-11-14T07:12:14Z | `7ab50d39b7638fe6f90a38c2116a9088bb29218fb230d6b6d5edf26167a27dab` | 170859 | **T1.** "Trading Hours on the EEX Derivatives Markets", © EEX AG, 2026, one page; the downloads page labels it 2026-09-04. The bars are vector graphics; the text layer yields the legend rows (Emission Trade Registration only until 06:45 pm CET; Gas & European Power Trade Registration only until 06:15 pm CET; Japanese Power 01:00 am CET or 02:00 am CEST – 10:00 am CET or 11:00 am CEST; Agriculture 08:55 am CET – 06:00 pm CET). Whether any bar moved relative to the 2025-07-01 edition is NOT verified — a visual comparison is the closing condition. Dormant identity: no runtime change is implied. |
