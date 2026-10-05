# INDEX — Stage 7 release-month re-inspection, ICE Futures U.S. (iceus venue + softs/index/dollar-index families)

Retrieval session: **2026-09-27 19:36–19:55 UTC** (`date -u`). The ice.com notices listing is
client-rendered, so the listing went through `https://r.jina.ai/`; PDFs were fetched directly from
`www.ice.com/publicdocs/…` (which serves this machine). Prior holdings: `holidays/raw/iceus-2025-2027/`
and `cfe-eurex-ice-cde-smfe-2026-2027/` (2026-09-12, whose newest notice was Columbus Day 2026-08-28).

## Verdict: TWO NEW T1 notices, both sufficiently specified and unconditional — release-PR material

1. **`ICE_Futures_US_2026_Thanksgiving_Holiday_20260923.pdf`** (notice dated September 23, 2026;
   sha256 `f153d1066d398ee1a65a598ed8fada26f95e7ad24b26e43b1ba720e073e6d28c`; text at
   `ifus_thanksgiving_2026.txt`). 2026 Thanksgiving per product group, NY time, with settlement
   windows: Sugar No. 11/16, Coffee C, Coffee C Metric, Cotton No. 2, Cocoa, FCOJ — **Thu Nov 26
   Closed**, Fri Nov 27 late open for Cotton 8:00 am, early close Cotton and FCOJ 1:30 pm, Cotton/FCOJ
   TAS end 1:25 pm, regular hours for Sugar/Coffee/Cocoa; Canola regular all three days; NYSE/FTSE/MSCI
   Bond/ICE Mortgage/Bond/SOFR index groups — Thu Nov 26 early close **1:00 pm** (no TAS), Fri Nov 27
   early close **1:15 pm** (TAS ends 1:00 pm); MSCI Stock Index same; Economic Indicator 1:00 pm both
   days. The softs/index disagreement on Nov 26-27 is exactly the shape the `iceus` venue intersection
   withholds (`Unsourced`), but the **family-level** rows can now be stated from this notice.
2. **`ICE_Futures_US_DST_End2026_20260925.pdf`** (notice dated September 25, 2026; sha256
   `2fe4ac40c6bf93ddc2bcee8e15356e86b12cb7e001d60345ca9bd52070632a5e`; text at `ifus_dst_end_2026.txt`).
   Temporary opening-time changes **for trade dates Monday 2026-10-26 through Friday 2026-10-30**
   (BST ends Oct 25, US DST ends Nov 1): Sugar No. 11 opens 4:30 am NY, Coffee C / Coffee C Metric
   5:15 am NY, Cocoa 5:45 am NY; Coffee settlement window 1:23–1:25 pm, Cocoa 12:48–12:50 pm; TAS ends
   move accordingly; Pre-Open, Daily Close and the Sugar settlement window unchanged. Unconditional,
   day-level, session language — date-exception rows for the three softs families.

## Unchanged / confirmed

- **Master calendar `IFUS_Trading_Hours_Holiday_Calendar.pdf`**: sha256
  `da97503545a3fb7607948367d30896685e220b36abed24aa02bbe1a21acb2817` — **byte-identical** to the stored
  June-2026 edition (2026 calendar; states 2027-01-01). Not republished.
- The 2027 calendar remains `ICE_Futures_US_Exchange_Notice-2027_Holiday_Calendar_20260604.pdf`
  (stored digest `d2e39a2d…`); nothing newer supersedes it.
- Notices listing (`ifus_notices.md`): between Aug 28 and Sep 28 2026 the only new items are
  Sep 17 new-products listing, Sep 23 Thanksgiving, Sep 25 margin rates, Sep 25 DST notice, Sep 28
  Block Trade FAQ (administrative) — no other holiday/schedule items.
- **The two unretrieved 2025 notices (#168): not re-chased** per the plan; today's listing still only
  reaches back to Feb 2026, so no new channel appeared.

## Artifacts

| file | url | retrieved (UTC) | sha256 |
|---|---|---|---|
| `ifus_notices.md` | https://www.ice.com/futures-us/notices (reader) | 2026-09-27 ~19:37 | see SHA256SUMS.txt |
| `ICE_Futures_US_2026_Thanksgiving_Holiday_20260923.pdf` | https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_2026_Thanksgiving_Holiday_20260923.pdf | 2026-09-27 ~19:39 | `f153d1066d398ee1a65a598ed8fada26f95e7ad24b26e43b1ba720e073e6d28c` |
| `ifus_thanksgiving_2026.txt` | pdftotext -layout of the above | 2026-09-27 ~19:39 | see SHA256SUMS.txt |
| `ICE_Futures_US_DST_End2026_20260925.pdf` | https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_DST_End2026_20260925.pdf | 2026-09-27 ~19:40 | `2fe4ac40c6bf93ddc2bcee8e15356e86b12cb7e001d60345ca9bd52070632a5e` |
| `ifus_dst_end_2026.txt` | pdftotext -layout of the above | 2026-09-27 ~19:40 | see SHA256SUMS.txt |
| `IFUS_Trading_Hours_Holiday_Calendar.pdf` | https://www.ice.com/publicdocs/futures/IFUS_Trading_Hours_Holiday_Calendar.pdf | 2026-09-27 ~19:41 | `da97503545a3fb7607948367d30896685e220b36abed24aa02bbe1a21acb2817` (= stored) |
| `ifus_master_calendar.txt` | pdftotext -layout of the above | 2026-09-27 ~19:41 | see SHA256SUMS.txt |
