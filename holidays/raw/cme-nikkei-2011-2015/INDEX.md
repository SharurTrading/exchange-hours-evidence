# INDEX — cme-nikkei-2011-2015 (globex_nikkei_225_dollar audit wave; reuse, no new retrieval)

Wave performed 2026-09-29 (UTC) from this machine. **No bytes were retrieved:**
every artifact the `globex_nikkei_225_dollar` 2011-2015 holiday wave cites was
already in this store, retrieved 2026-09-12 (UTC) by the tasks that audited
`globex_equity_index` (`cme-2010-2012`, `cme-2013-2015`, with the `-fix`,
`-repair-r2` and `-verify*` rounds). This wave inventory-checked the store,
re-verified every cited document's sha256 against the store's bytes, re-read
each cited sheet's `Equity Products` line from the store's own `pdftotext`
extracts, and keyed the family's rows to the same document ids the sibling
evidence file uses.

## What this wave used

- `../cme-2010-2012/` — the 2010 and 2011-2012 per-holiday PDFs
  (`docs/<year>-<holiday>.pdf`), the CDX enumeration
  `cdx_holiday_calendar_2009_2014.json` (2009-2014, prefix
  `cmegroup.com/tools-information/holiday-calendar*`), and the text extracts
  (`txt/`). Cited here: `2011-new-years.pdf`, `2011-martin-luther-king.pdf`,
  `2011-presidents-day.pdf`, `2011-good-friday.pdf`, `2011-memorial-day.pdf`,
  `2011-4th-of-july.pdf`, `2011-labor-day.pdf`, `2011-thanksgiving.pdf`,
  `2011-christmas.pdf`, `2012-new-years.pdf`, `2012-martin-luther-king.pdf`,
  `2012-presidents-day.pdf`, `2012-good-friday.pdf`, `2012-memorial-day.pdf`,
  `2012-4th-of-july.pdf`, `2012-labor-day.pdf`, `2012-thanksgiving.pdf`,
  `2012-christmas.pdf`; the 2010 sheets `2010-new-years.pdf`,
  `2010-presidents-day.pdf` and `2010-christmas.pdf` are cited by the wave's
  **refusal** prose (the 2010 interval stays unaudited; the President's Day
  sheet's `Exception: USD & JY denominated Nikkei ...` lines are the reason the
  equity class line cannot be read as governing NKD in 2010).
- `../cme-2013-2015/` — the 2013-2015 per-holiday PDFs (`pdf/`), the CDX
  enumeration `cdx_holiday_calendar.json`, and the text extracts (`txt/`).
  Cited here: `2013-new-years.pdf`, `2013-martin-luther-king.pdf`,
  `2013-presidents-day.pdf`, `2013-good-friday.pdf`, `2013-memorial-day.pdf`,
  `2013-4th-of-july.pdf`, `2013-labor-day.pdf`, `2013-thanksgiving.pdf`,
  `2013-christmas.pdf`, `2014-new-years.pdf`,
  `2014-martin-luther-king-holiday-schedule.pdf`,
  `2014-presidents-day-holiday-schedule.pdf`,
  `2014-good-friday-holiday-schedule.pdf`,
  `2014-memorial-day-holiday-schedule.pdf`,
  `2014-4th-of-july-holiday-schedule.pdf`,
  `2014-labor-day-holiday-schedule.pdf`,
  `2014-thanksgiving-holiday-schedule.pdf`,
  `2014-christmas-holiday-schedule.pdf`,
  `2015-new-years-holiday-schedule.pdf`,
  `2015-martin-luther-king-holiday-schedule.pdf`,
  `2015-presidents-day-holiday-schedule.pdf`,
  `2015-good-friday-holiday-schedule.pdf`,
  `2015-memorial-day-holiday-schedule.pdf`,
  `2015-4th-of-july-holiday-schedule.pdf`,
  `2015-labor-day-holiday-schedule.pdf`,
  `2015-thanksgiving-holiday-schedule.pdf`,
  `2015-christmas-holiday-schedule.pdf`.
- `../cme-2013-2015-fix/` — the 45 `.xls` workbooks and their reconciliation;
  its INDEX's finding 7 ("No Nikkei line and no cryptocurrency line exists
  anywhere in the `.xls` corpus") is one of the two channel searches this
  wave's interpretive step rests on. The other is this wave's own grep across
  every extracted PDF text of both eras (same result: no `Nikkei` line).

## Re-verification, 2026-09-29

All 48 document ids the wave cites (47 shared with the sibling evidence file
plus `2011-new-years.pdf @2011-11-01T14:39:45Z`) were re-hashed from the
store's bytes on 2026-09-29: 48 of 48 sha256s reproduce. The digests live in
`docs/evidence/globex_nikkei_225_dollar.md`'s `### Documents (2011-2015)`
table, which carries the same id/window/sha triples as the sibling file's
tables (the repository-wide fences require the identities to agree).

## Bounded-search record for 2010

The 2010 sheets survive complete in `../cme-2010-2012/` and are read: one PDF
per holiday plus the consolidation PDF, the Veterans Day and Columbus Day
sheets (both regular for equity), and the later Christmas revision. The wave
still leaves 2010-01-01..2011-01-11 outside every declared holiday window,
because the sheets carve the Nikkei out of the equity class line where it
differed (the 2010 President's Day exceptions) and govern the sourced-but-
unmodelled 2010 grid, so neither silence nor the class line supports an
audited-normal claim. Closing conditions are in the evidence file; the
follow-up is tracked on the repository as an issue (LAW-FOLLOW-UPS-ARE-ISSUES).
