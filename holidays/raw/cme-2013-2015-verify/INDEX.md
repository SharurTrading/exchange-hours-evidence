# INDEX — adversarial verification of task `cme-2013-2015`

Verification run 2026-09-12 (UTC, `date -u`) by task `cme-2013-2015.verify`.
All bytes retrieved from the Internet Archive `id_` raw replay of cmegroup.com
(cmegroup.com returns 403 to this machine directly). Tier T1: CME Group's own
published documents read from a verbatim public mirror.

## `refetch/` — independent re-fetches of documents cited by cme-2013-2015

Ten of the task's 34 cited artifacts were re-fetched from their replay URLs and hashed.
**All ten are byte-identical to the copies saved under `raw/cme-2013-2015/`.**

| file | replay URL | sha256 | bytes |
|---|---|---|---|
| refetch_2013-good-friday__20130623195925.bin | https://web.archive.org/web/20130623195925id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-good-friday.pdf | c05e590c950581e19ac2e8ee5327ebcfb4fc111b231b506abefae44534ee9b68 | 63251 |
| refetch_2013-thanksgiving__20140214062836.bin | https://web.archive.org/web/20140214062836id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-thanksgiving.pdf | 1f7f6428990a5bd01065f31c4388bf5aeeb12d9219e5af6d16b1cec86bbc158b | 75026 |
| refetch_2013-veterans-day__20121119001630.bin | https://web.archive.org/web/20121119001630id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-veterans-day.pdf | 7e5bd54859002a29f50ef3f1eec1f46f3fd3a7d51e9aed303f189a097719252b | 85574 |
| refetch_2014-mlk__20140326160215.bin | https://web.archive.org/web/20140326160215id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-martin-luther-king-holiday-schedule.pdf | 5069a46a6acfb69bf05261abc23097fd675d159cf55e45361fb7e1e41dc0dcd4 | 138368 |
| refetch_2014-christmas__20150121141000.bin | https://web.archive.org/web/20150121141000id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-christmas-holiday-schedule.pdf | 8125a18c9cad9b770be39b89c3193ee419240d409e39aa510d6eb3e8eba94e25 | 54124 |
| refetch_2014-columbus-day__20140326160057.bin | https://web.archive.org/web/20140326160057id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-columbus-day-holiday-schedule.xls | b01b4d3e1b669f6e0bbeb0818f2516782805c6d38e41c6158ad5ad102593696b | 34304 |
| refetch_2015-good-friday__20150905223230.bin | https://web.archive.org/web/20150905223230id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-good-friday-holiday-schedule.pdf | 67873caa987c9eee8de38d02a5c18d8f7d46fd82a486bab34821f6e6f6363e0b | 54240 |
| refetch_2015-labor-day__20150824023039.bin | https://web.archive.org/web/20150824023039id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-labor-day-holiday-schedule.pdf | 4aab7fdb5e57420a243bbc26be6ecfa00a6317937afe3b772dfcdd8db1dd50fd | 107305 |
| refetch_2015-new-years__20150121141043.bin | https://web.archive.org/web/20150121141043id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-new-years-holiday-schedule.pdf | 196b4ec04bcfce2cfd9783262023afe9da73bcdef1b983c8c4b464b2e115bb8a | 59206 |
| refetch_2016-new-years__20160108203007.bin | https://web.archive.org/web/20160108203007id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-new-years-holiday-schedule.pdf | 118196a469dd40ad6a40594da273f726f6cb3e503f9cc1b8fd2057cf2fa32c61 | 64156 |

## `new/` — operator documents the verified task did NOT retrieve

These are CME Group's own Excel holiday schedules. The task's INDEX dismissed the
`.xls` files as "the `.xls` twins of the PDFs above (same content, different container)".
They are not: they carry per-product exception rows the PDFs omit, split Interest Rate
from FX, and at least one earlier revision states a different instant.

| file | original URL | replay timestamp (UTC) | sha256 | bytes |
|---|---|---|---|---|
| master2015.xls | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-cme-group-holiday-schedule.xls | 2015-03-20T07:12:17Z | 13baef016ecc2d3b089273c53d767f2e6a795f3dbc9a8dfde1d196addda4af8f | 345088 |
| master2014.xls | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-cme-group-holiday-schedule.xls | 2014-08-26T20:47:12Z | 8bdfb8274bea78b2ebe5189523abc27a977b26390ee884f6b02bc6e2f46b09ae | 442368 |
| labor_20150326073728.xls | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-labor-day-holiday-schedule.xls | 2015-03-26T07:37:28Z | c459c0607789b795803c9e95664e4c97577b8d57a453290957ae4f059408b747 | 88064 |
| labor_20150905221329.xls | (same URL, later revision) | 2015-09-05T22:13:29Z | 209fa866f40ad289354ff9e97c80981d9d29136f6dfd5c20358e5f96a2436157 | 88064 |
| vet2015.xls | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-veterans-day-holiday-schedule.xls | 2015-03-26T11:38:06Z | b70878c2288fd0536ca8f73649dc1e89625910dd5c382cef3c00298799719c98 | 24576 |
| x_2015-4th-of-july-holiday-schedule.xls | .../2015-4th-of-july-holiday-schedule.xls | 2016-02-05T19:18:36Z | 382273ad9829edef36afc3a7ddf7262dbc71da9e0825227a1fa81126c49889ae | 86016 |
| x_2015-christmas-holiday-schedule.xls | .../2015-christmas-holiday-schedule.xls | 2016-02-05T17:36:03Z | c6ce2a98b1462e987814d760bfc91df54427876c2eb2dfd017a75e4a69c7eefd | 55296 |
| x_2015-good-friday-holiday-schedule.xls | .../2015-good-friday-holiday-schedule.xls | 2016-02-05T18:18:07Z | 617ff197e9da9dc6289ed2193a8a6f9f23b99add3aafa79d2ed56f227eac5349 | 69632 |
| x_2015-martin-luther-king-holiday-schedule.xls | .../2015-martin-luther-king-holiday-schedule.xls | 2016-02-05T17:50:46Z | dff154f0051afdee5001472a303cb41d0439aa7b25794e0f9744e0d27ac2406e | 86528 |
| x_2015-memorial-day-holiday-schedule.xls | .../2015-memorial-day-holiday-schedule.xls | 2016-02-05T16:32:49Z | 64ab9a8647046a943c26b2d30eb06ac41d4a7a53db3723be0ad232cfa9333f6c | 89088 |
| x_2015-presidents-day-holiday-schedule.xls | .../2015-presidents-day-holiday-schedule.xls | 2016-02-05T15:43:52Z | f2394e57a42615512bc972e44998eea153241c3d32a47d9ba1a3c458b55ea00b | 90112 |
| x_2015-thanksgiving-holiday-schedule.xls | .../2015-thanksgiving-holiday-schedule.xls | 2016-02-05T19:08:43Z | 7f78617538977426111decfd71cf68cbca2b4c86b007b6a1839ced16cbf050a2 | 86016 |

## Fresh CDX enumerations

- `cdx2015.json` — `https://web.archive.org/cdx/search/cdx?url=cmegroup.com/tools-information/holiday-calendar*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&from=2015&to=2016&collapse=urlkey&limit=5000`, retrieved 2026-09-12 UTC.
- `xls2015.json` — same host/path filtered to `2015-*.xls`, from=2015 to=2017, retrieved 2026-09-12 UTC.

## Key quotations from the unretrieved documents

`labor_20150326073728.xls`, sheet `Labor`, row 9 `Interest Rate Products`, column 2, whose
header (row 3, column 2) reads `Early Fri. Close`, under the calendar-date header
`Friday, September 4`: **15:15**. Row 11 `FX Products`, same column: **15:15**.
`master2015.xls`, sheet `Labor`, identical.
`labor_20150905221329.xls` (the later revision of the same URL) moves both to
column 1 `Regular Fri. Close`: **16:00**, agreeing with the PDF the task used
(`2015-labor-day-holiday-schedule.pdf`, footer `Last updated 7/20/2015`).

`master2015.xls`, sheet `Independence`, row 4 `Equity Products`, column 2 `Early Close`
under `Thursday, July 2`: **12:15**, with row 6 `Big Equity Indexes (SP,ND,MD & SMP)`
column 1 `Regular Close` **08:15**. The later `x_2015-4th-of-july-holiday-schedule.xls`
and the PDF (`Last updated 6/1/2015`) both print a 16:15 regular close on July 2.
Both are earlier-revision divergences, not errors in the recorded final state.
