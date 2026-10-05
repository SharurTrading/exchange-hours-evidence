# INDEX — Stage 7 release-month re-inspection, CFE (Cboe Futures Exchange)

Retrieval session: **2026-09-27 19:31–19:36 UTC** (`date -u`). Direct retrieval from www.cboe.com worked.
Prior holdings: `holidays/raw/cfe-eurex-ice-cde-smfe-2026-2027/` (2026-09-12) and `cfe-2010-2025/`.

## Verdict: NOTHING NEW for 2027 — the horizon stands at 2026-12-31

- `https://www.cboe.com/us/futures/holidays/csv/` re-generated today (header `# Generated: 2026:09:27
  11:08:14`) still lists **2026 rows only** — New Year's Day (closed), MLK 10:30, Presidents' 10:30,
  Good Friday 08:30, Memorial 10:30, Juneteenth 10:30, Independence Observed 10:30, Labor 10:30,
  Thanksgiving 10:30 + Friday 08:30–12:15, Christmas Eve 08:30–12:15, Christmas Day closed.
  Digest differs from the stored CSV only because of the generated-at header; the row content matches
  the stored `cc98e21e…` capture and every shipped `cfe` 2026 row.
- `https://www.cboe.com/about/hours/us-futures` still carries exactly one "2026 Futures Holiday
  Schedule" heading; no 2027 section (its only "2027" text is an RMC conference link).
- Circulars listing (reader render): nothing newer than CFERG26-004 touching a 2027 holiday calendar.
- **All shipped 2026 rows reconfirmed against today's CSV** (the Scheduled-marker spot check): no
  forward-dated row has slipped.

## Artifacts

| file | url | retrieved (UTC) | sha256 |
|---|---|---|---|
| `cboe_us_futures_holidays.csv` | https://www.cboe.com/us/futures/holidays/csv/ | 2026-09-27 19:32:20 | `f9397d2d8d5e0c63e434adc5ab1280ee5e0290dd4451d090299d97f8955e47a2` |
| `cboe_hours_us_futures.html` | https://www.cboe.com/about/hours/us-futures | 2026-09-27 19:32 | `d5a0b862e0a82f91b8dafcc13d1607256ee8914bca39aefa09eba65105c31a3f` |
| `cfe_circulars.md` | https://www.cboe.com/us/futures/regulation/circulars/ (reader) | 2026-09-27 ~19:35 | see SHA256SUMS.txt |
| `cfe_circulars.html` / `cfe_notices.html` | same two pages direct — client-rendered shells (136/162 bytes), kept to show the direct channel renders nothing | 2026-09-27 ~19:34 | see SHA256SUMS.txt |
