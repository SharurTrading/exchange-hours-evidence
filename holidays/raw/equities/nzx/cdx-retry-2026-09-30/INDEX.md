# Evidence index — `equities/nzx/cdx-retry-2026-09-30`

The CDX-service-back retry of issue #209's 2016-04-26..2017-10-22 span,
run 2026-09-30 ~02:25-02:40 UTC (LAW-UTC-DATES). Verbatim CDX outputs in
`cdx-*.json` (`SHA256SUMS.txt` has the digests):

- `cdx-nzx_span-all.json` — domain-wide nzx.com, captures 2016-04-26..2017-10-22,
  1 256 collapsed url keys with statuscode 200. The only trading-hours pages
  in the span are `https://www.nzx.com/markets/nzsx/trading_hours`
  (capture `20170623165321`, already cited as `NZX-SX-2017-06-23`) and
  `https://nzx.com/Derivatives/trading_hours` (capture `20170718122509`) —
  the new row-bearing artifact below. No key-dates, NZAX, NZDX-path, investing
  or hours-boards page, no holiday-named PDF, and no ajax/data endpoint is
  captured inside the span.
- `cdx-nzx_keydates-all.json` — domain-wide `key.date` filter: the key-dates
  family's captures are 2008-2009 and 2023 only; nothing in or reprinted over
  the gap.
- `cdx-nzx_holiday.json` / `cdx-nzx_Holiday.json` — domain-wide
  `holiday`/`Holiday` filters: one hit, the 2010-12-05 announcement
  `NZX-Trading-Hours-during-the-Holiday-Period` (inside the already-audited
  2010-2011 era).

| File | Capture | Retrieved (UTC) | sha256 | What it states |
|---|---|---|---|---|
| `nzx-derivatives-hours-2017-07.wayback-20170718122509id_.html` | `20170718122509` | 2026-09-30T02:25:08Z | `03f91bbe1706d7b2a3f050a134725891027f48a34ccdd64f239ada7ebb54580c` | The NZX Derivatives trading-hours page — the operator's own `Market Closed or Abbreviated Trading` table printing, retrospectively, `14/04/2017 Good Friday Closed`, `17/04/2017 Easter Monday Closed`, `25/04/2017 Anzac Day Closed`, `05/06/2017 Queens Birthday Closed`, then `23/10/2017 Labour Day Closed` and the 2017-2018 arrangement on (agreeing with `NZX-SX-2017-06-23` on every shared date). The table's first row is 2017-04-14: the roll reaches back only this far, so 2016-04-26..2017-04-13 stays unsourced. |
