# European source scan — 2026-10-31 UTC

`captures.json` records each retrieval URL, time, byte count and SHA-256.

## Runtime update

`xetra-final-session-2026.pdf`, the operator's final-session notice for
2026-12-30, gives the XETR DAX-share phase timetable unconditionally. The
crate now uses a complete replacement: pre-trading 07:00–08:00 CET,
retail/opening auction 08:00–09:00:30, regular 09:00:30–13:00,
intraday auction 13:00–13:02:30, regular 13:02:30–14:00,
closing auction/Trade-at-Close 14:00–14:10, post-trading 14:10–15:00.
Opening/intraday conservative uncrosses are retained from the normal profile;
the notice changes their starts, not their ordinary durations. XETR and XFRA
are separate sections; XFRA and off-book services are excluded.

## Other checks

- `xetra-2027.pdf` confirms the five existing 2027 weekday closures. Its four
  asterisks mean only that hours may differ and provide no final intraday
  times. The existing #200 watch item remains a source-hours question.
- Euronext live 2026 year-end section still states “To be announced”. The
  normal-hours appendix effective 19 October 2026 was compared with the
  previous captured publication (header effective 3 August 2026). All 80
  continuous-equity groups on Paris/Amsterdam/Brussels/Lisbon have unchanged
  opening, continuous, closing and TAL phase cells. Exact comparison:
  `euronext-principal-equities-comparison.json`.
- Nordic Market Model 2026:05 section 3.1 preserves the supported principal-share
  phases and five-second randomized opening. This newer model does not alter
  the existing grids.
- BME's current calendar still publishes 2026 and the shorthand 14:00 eves;
  no 2027 calendar or detailed 2026 principal-share half-day schedule was located.
- Eurex archive still links a 2026 annual calendar; its broader future non-trading
  table is not a new complete per-product annual audit. No changed scoped
  benchmark/fixed-income hours were verified.
- SIX 2027 calendar and current hours were re-retrieved; no new published
  in-scope exception was identified.
- LSE business-days wrapper was retrieved. Its live content API refused with
  HTTP 403, so later years were not certified from that wrapper or inferred.

This is a bounded announcement scan, not an advancement of all ledger review
dates. No unchanged horizon or completeness claim was upgraded.
