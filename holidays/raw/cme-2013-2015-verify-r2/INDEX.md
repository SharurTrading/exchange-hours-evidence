# INDEX — adversarial verifier round 2, task `cme-2013-2015`

Retrieved 2026-09-12 UTC. Bytes fetched through the Internet Archive `id_` raw replay
(byte-identical mirror of the operator's response). Tier **T1** — CME Group's own
published Globex holiday schedules.

| file | original URL | replay URL | capture (UTC) | sha256 | bytes | what it is |
|---|---|---|---|---|---|---|
| `new/2013-4th-of-july-done__20130717050333.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-4th-of-july-done.pdf | https://web.archive.org/web/20130717050333id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-4th-of-july-done.pdf | 2013-07-17T05:03:33Z | `768c7813542459dbc5443e79e514bb12fd511d93284beeb880af167f6049e0f0` | 73249 | CME's LATER revision of the 2013 Independence Day Globex schedule, footer 'Last updated 7/2/2013'. Supersedes the 6/4/2013 revision the task cites as D13J4. |
| `new/2014-4th-of-july-holiday-schedule__20140326153233.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-4th-of-july-holiday-schedule.pdf | https://web.archive.org/web/20140326153233id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-4th-of-july-holiday-schedule.pdf | 2014-03-26T15:32:33Z | `61ef891b5f43164317814b0d5de6619337e1e11f5df1251b0ced886a7193827b` | 113700 | Earlier revision of the 2014 Independence Day PDF, footer 'Last updated 2/26/2014'; superseded by the 7/1/2014 revision (D14J4). |
| `new/2015-4th-of-july-holiday-schedule__20150326113353.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-4th-of-july-holiday-schedule.pdf | https://web.archive.org/web/20150326113353id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-4th-of-july-holiday-schedule.pdf | 2015-03-26T11:33:53Z | `664f4b885e090fccfe15152781ba62014aaa1650d1dfdf41564483d457d4ce2b` | 112477 | Earlier revision of the 2015 Independence Day PDF, footer 'Last updated 12/29/2014'; superseded by the 6/1/2015 revision (D15J4). |
| `cdx/cdx-2013-files.json` | https://web.archive.org/cdx/search/cdx?url=cmegroup.com%2Ftools-information%2Fholiday-calendar%2Ffiles%2F2013*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&collapse=digest | (CDX API) | 2026-09-12 | `92da29d09d7c4c911fab26b573544c96a2d55e3c91c3e735331581f71d751fca` | 14103 | Fresh CDX enumeration, 2013 files. |
| `cdx/cdx-2014-files.json` | https://web.archive.org/cdx/search/cdx?url=cmegroup.com%2Ftools-information%2Fholiday-calendar%2Ffiles%2F2014*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&collapse=digest | (CDX API) | 2026-09-12 | `6185ec4c9c2db0a838a55950bc228367bb9328b8cbc8b51259c9de148e774aa3` | 12502 | Fresh CDX enumeration, 2014 files. |
| `cdx/cdx-2015-files.json` | https://web.archive.org/cdx/search/cdx?url=cmegroup.com%2Ftools-information%2Fholiday-calendar%2Ffiles%2F2015*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&collapse=digest | (CDX API) | 2026-09-12 | `5502160deea11c6e95b06efc95d192ad3e13a027782c23ed5cae232481fb5bd2` | 12253 | Fresh CDX enumeration, 2015 files. |

## txt/

`pdftotext -layout` renderings of the three PDFs above.

## refetch/

Ten documents already held by the task, re-fetched independently from their replay URLs
on 2026-09-12 UTC and compared byte for byte against the saved copies. All ten matched:
`2015-cme-group-holiday-schedule@20150320071217`, `2014-cme-group-holiday-schedule@20140826204712`,
`2013-good-friday-presidents-day@20130623203632`, `2015-labor-day-holiday-schedule@20150905221329`,
`2015-labor-day-holiday-schedule@20150326073728`, `2015-thanksgiving-holiday-schedule@20151203081209`,
`2015-4th-of-july@20150905222733`, `2013-4th-of-july@20130623205825`, `2014-4th-of-july@20140708015736`,
`2015-veterans-day@20151122230920`.

## Why these bytes exist

`2013-4th-of-july-done.pdf` is the finding: it sits in *both* the round-0 and the round-1
saved CDX enumerations (row `20130717050333 ... 200 application/pdf`), was never retrieved by
either round, and is CME's later revision of the 2013 Independence Day schedule. Under
`Wednesday, July 3` it prints `1200 CT – Early close for Dairy`, `1200 CT – Early close for
Lumber`, `1202 CT – Early close for Lumber Options` and `1215 CT – Early close for Livestock
Futures & Options`, where the cited 6/4/2013 revision leaves all three products in the
`Regular Close - Per each product schedule:` bullet list. The two other PDFs are earlier
revisions retrieved to show that the unexamined PDF revision history carries real changes.

