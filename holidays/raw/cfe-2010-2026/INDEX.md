# CFE 2010-2026 below-window retrieval — 2026-10-06 UTC

Artifacts for the 2010-01-01..2017-04-09 unaudited-span hunt on the `cfe`
venue / `cfe_vix` key. Everything here is the operator's own document read
through a Wayback `id_` replay (or, for RG-CFE-2014-020, the operator's live
CDN), saved as bytes; digests in `SHA256SUMS.txt`.

## ir/ — CBOE Holdings holiday press releases naming CFE (T1)

| File | Replay URL | Capture | Content |
|---|---|---|---|
| ir2014-christmas-newyear.pdf | web.archive.org/web/20150906051018id_/http://ir.cboe.com/~/media/Files/C/CBOE-IR-V2/press-release/2014/CBOE%20Holdings%20Holiday%20Schedule%20-%20Christmas%20and%20New%20Years.pdf | 20150906051018 | dated 2014-12-16; CFE 12/24 early close 12:15 (VX), 12/25 closed, 12/26 leg from 17:00 12/25; 12/31 regular 15:15, 1/1 closed, 1/2 leg from 17:00 1/1 |
| ir2015-presidentsday.pdf | .../20150406221225id_/.../2015/holiday-schedule-presidents-day.pdf | 20150406221225 | dated 2015-02-04; 2/16 halt 10:30, resumes 17:00 for business day 2/17 |
| ir2015-goodfriday.pdf | .../20150905235922id_/.../2015/holiday-schedule-good-friday4-3-15.pdf | 20150905235922 | dated 2015-03-26; VIX closes 8:15 a.m. 4/3; corroborates IC15-011 |
| ir2015-memorialday.pdf | .../20150906083145id_/.../2015/Holiday-Schedule-Memorial-Day-5-25-15.pdf | 20150906083145 | dated 2015-05-14; 5/25 halt 10:30, resumes 17:00 for business day 5/26 |
| ir2015-independence.pdf | .../20150905190749id_/.../2015/holiday-schedule-independence-day-7-4-15.pdf | 20150905190749 | dated 2015-06-24; 7/3 closed, normal Sunday reopen |
| ir2015-laborday.pdf | .../20150905081723id_/.../2015/holiday-schedule-labor-day-8-31-15.pdf | 20150905081723 | dated 2015-08-31; 9/7 halt 10:30, resumes 17:00 for business day 9/8 |
| ir2015-thanksgiving.pdf | .../20151129061924id_/.../2015/holiday-schedule-thanksgiving-11-17-15.pdf | 20151129061924 | dated 2015-11-17; 11/26 halt 10:30, resumes 17:00; 11/27 early close 12:15 |
| ir2015-christmas-newyear.pdf | .../20160422065335id_/.../2015/holiday-schedule-christmas-and-new-years-12-17-15.pdf | 20160422065335 | dated 2015-12-17; 12/24 early close 12:15, 12/25 closed; 12/31 regular 15:15, 1/1 closed; names IC15-055 |
| ir2016-mlk.pdf | .../20160422005008id_/.../2016/holiday-schedule-martin-luther-king-jr-day-1-11-16.pdf | 20160422005008 | dated 2016-01-11; 1/18 halt 10:30, resumes 17:00 for business day 1/19 |
| ir2017-memorialday.pdf | .../20170629055727id_/.../2017/holiday-schedule-memorial-day-5-23-17.pdf | 20170629055727 | dated 2017-05-23; corroborates the shipped 2017-05-29 row |

## circ/ — CFE information circulars (T1)

Holiday-titled: CFEIC15-011 (Good Friday 2015: VIX holiday session Thu 15:30 -
Fri 08:15, Sat None, Sun 17:00 - Mon 08:30, Mon regular), CFEIC15-023
(Memorial Day 2015: Mon EC 10:30, Tue from 17:00 Mon), CFEIC15-028
(Independence 2015: closed 7/3, Thursday close 15:15, normal Sunday),
CFEIC15-039 (Labor Day 2015: Mon EC 10:30, Tue from 17:00 Mon),
CFEIC17-054 (Christmas 2017 corroboration), CFEIC17-055 (New Year 2018
corroboration). The rest of the fetched circulars are product/technical and
key no row (negative witnesses). RG-CFE-2014-020.pdf is the live-CDN copy of
the June-2014 hours circular (continuous 15:30 beginning for the next
business day, Sunday 17:00 week open); CFERG14-018.pdf is the same circular's
framed-page wrapper (no PDF bytes) kept only to document the wrapper channel.

## su2017/ — Cboe-Holiday-Reminder PDFs (T1; corroboration)

Cboe-Holiday-Reminder-Christmas-and-New-Years-Day-2017.pdf covers CFE
(12/24, 12/25, 12/31 closed, resumes 17:00 for 12/26 and 1/2) and
corroborates the shipped 2017-12-25 / 2018-01-01 rows;
Cboe-Holiday-Reminder-Thanksgiving-Day-2017.pdf is options/equities only
(names no CFE schedule).

## oldpages/ — negative witnesses

cboe_holidayCalendar_20101221.html (replay of
web.archive.org/web/20101221064822id_/http://www.cboe.com/AboutCBOE/holidayCalendar.aspx)
— the options-exchange holiday page; no CFE schedule.

## CDX sweep records

cdx_cfecom_all.json (cfe.com domain: unrelated site, no Cboe content),
cdx_cfecom_holiday.json / cdx_cfecom_hours.json (empty), cdx_showdoc.json,
cdx_aboutcfe_all.json (old-site news docs: only 2004-2007 holiday docs),
cdx_infocirc_full.txt (complete CFEinfocirc capture list),
cdx_framed.txt (framed-page titles; the only holiday-titled circulars ever
framed are the captured ones), cdx_wwwcfepublish.txt, cdx_microsite.txt
(empty), cdx_su2017.txt.
