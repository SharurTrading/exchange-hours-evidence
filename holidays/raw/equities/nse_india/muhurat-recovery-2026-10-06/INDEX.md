# nse_india — Muhurat recovery sweep, 2026-10-06 UTC

Second pass over the capital-market circular channel after the same-day
domain-lineage recovery of the 2020/2022/2023/2024/2025 circulars. Method:
full CDX prefix sweeps of the `CMTR`/`cmtr` circular directories on all four
hosts (`nseindia.com`, `www.nseindia.com`, `www1.nseindia.com`,
`archives.nseindia.com`, `nsearchives.nseindia.com`; 510 unique captured
CMTR PDFs), each capture cross-referenced against the download-number range
of every Muhurat issuance window, anchored by the dated circulars the
recovered bytes themselves state (16062=2010-10-20, 16348=2010-12, 19075=
2011-10-05, 19431=2011-11-24, 19539=2011-12-09, 19982=2012-02-09, 20561=
2012-04-17, 25324=2013-12-28, 28337=2014-12-12, 31047=2015-10-30, 31297=
2015-12-07, 33424=2016-10-17, 42877=2019-12-11, 46230=2020-11-02).

## Recovered (key rows)

| Date | Circular | Capture (host) | sha256 (file in pdf/) |
|---|---|---|---|
| 2010-11-05 (Fri) | CMTR16062 — circular 121/2010, dated 2010-10-20 | 20101122005959 (nseindia.com) | 0e39bfe8... |
| 2015-11-11 (Wed) | CMTR31047 — circular 65/2015, dated 2015-10-30 | 20160216033210 (www.nseindia.com) | 060afe66... |
| 2016-10-30 (Sun) | CMTR33424 — circular 56/2016, dated 2016-10-17 | 20170224214712 (www.nseindia.com) | 9e11622e... |
| the 2012 list | CMTR19539 — circular 66/2011, dated 2011-12-09, "Trading holidays for the calendar year 2012" | 20131001001639 (www.nseindia.com) | 4f798db9... |

The 2012 list prints fifteen weekday holidays (2012-11-13 "Diwali – Laxmi
Pujan*" carries the Muhurat footnote with no instants, so the date ships
`Unsourced` like its sibling years) and five Saturday/Sunday holidays that
key no rows. This re-opens the 2012 audited window.

## Corroboration (keys no row)

- CMTR42877 — "Trading holidays for the calendar year 2020", dated
  2019-12-11 (capture 20250903152140, nsearchives): corroborates the shipped
  2020 rows date-for-date, twelve weekday rows plus the weekend list, and
  footnotes Muhurat against Saturday 2020-11-14.
- CMTR16348 — "Trading holidays for the calendar year 2011" (capture
  20110902133106): byte-identical (sha256 d5283622...) to the store's
  `2010-2024/` copy of `NSE-CIRC-2011-126` (eq_holidays.pdf, capture
  20131021135725) — the same document replayed from a second capture.
- CMTR19075 (2011-10-05) and CMTR19431 (2011-11-24): negative witnesses in
  the 2011 issuance window (neither is the Muhurat circular NSE/CMTR/19187).

## Negatives after this pass

- **2011**: NSE/CMTR/19187 has no capture at any host (prefix sweeps on all
  four hosts, upper- and lower-case paths). Its issuance number sits between
  19075 (2011-10-05) and 19431 (2011-11-24); neither neighbour is it.
- **2013**: issuance window ≈ 24200-24700 (between 23588/24121 of
  2013-09 and 25324 of 2013-12-28): no captures.
- **2014**: issuance window ≈ 27000-27500 (between 26919 of 2014-07 and
  28337 of 2014-12-12): no captures.
- **2017**: issuance window ≈ 33770-34100 (after 33746 of ~2017-06/07): the
  only captures in the range are 302 wrappers and 404s; no PDF bytes.
- **2019**: the archive's September-2019 bulk capture ends at CMTR42070
  (2019-09-23) and the next capture is 42877 (2019-12-11); the Muhurat
  issuance window (Diwali 2019-10-27) falls in between: no captures.
- **2018**: the annual list (issued 2017-12, numbers ≈ 33950-34200) has no
  captures; the annual page URL remains uncaptured in 2018 (prior hunt).
- **2026**: not yet issued — Diwali 2026-11-08; the 2025 edition issued
  2025-09-22 for a 2025-10-21 Diwali, so the 2026 circular's issuance window
  was still opening at the 2026-10-06 sweep. Publication-season watch, not a
  gap.

## CDX sweep records

cdx_www1_cmtr.txt / cdx_www1_cmtr_lc.txt (934 rows each), cdx_www_cmtr_lc.txt,
cdx_archives_cmtr.txt / _lc.txt, cdx_nsearchives_cmtr.txt / _lc.txt,
cdx_nseindia_cmtr.txt / _lc.txt, cdx_holidayszip.txt (HOLIDAYS.zip: only the
2010-01-02 capture already cited), cdx_nseindia_diwali.txt.
