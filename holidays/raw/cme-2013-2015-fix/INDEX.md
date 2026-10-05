# INDEX — CME Group .xls holiday schedules, 2013-2015 (task `cme-2013-2015`, fixer round 1)

Retrieved 2026-09-12 UTC by the round-1 fixer for task `cme-2013-2015`.

## Why this directory exists

The round-0 result set aside CME Group's `.xls` holiday schedules with the note
"the `.xls` twins of the PDFs above (same content, different container)", and its
`missing[0]` claimed to have read "every 2013-2015 holiday PDF and XLS in the CDX
enumeration". Both statements were false. Only two `.xls` files (Columbus Day 2014 and
2015) had ever been retrieved. CME's `.xls` holiday schedules are a **different and
richer document** than the PDFs: they print Interest Rate Products and FX Products as
separate rows, distinguish a `Regular Fri. Close` column from an `Early Fri. Close`
column, and carry per-product exception rows the PDFs omit entirely. The PDFs point at
them: *"For a complete list of Globex schedules please reference the Excel version of the
Holiday calendar."*

This round enumerated the path afresh and retrieved **every** `.xls`/`.zip` holiday
document CME published for 2013-2015 (plus the 2016 New Year's file, which sources the
Dec 31 2015 lines), then reconciled them cell by cell against every PDF-sourced row.

## Enumeration

Saved as `cdx_all.json` (retrieved 2026-09-12 UTC):

```
https://web.archive.org/cdx/search/cdx?url=cmegroup.com/tools-information/holiday-calendar*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&from=2012&to=2017&collapse=digest
```

603 rows, of which 114 are `.xls`/`.xlsx`/`.zip`. The 45 in range (`2013-*`, `2014-*`,
`2015-*` and `2016-new-years-*`, status 200) are the download list `todo.tsv`; all 45 were
retrieved through `id_` raw replay, which returns the archived response body unmodified.
**Tier T1** under LAW-PRIMARY-SOURCES: the operator's own published document read as bytes
from a verbatim public mirror. cmegroup.com returns 403 to this machine and these paths are
long retired, so the archive is the only public channel.

Independent confirmation that this channel is byte-faithful: my own downloads of
`2014-columbus-day-holiday-schedule.xls@20140326160057` and
`2015-columbus-day-holiday-schedule.xls@20150326113300` reproduce, byte for byte, the
sha256 values round 0 recorded for the same two files
(`b01b4d3e1b669f6e0bbeb0818f2516782805c6d38e41c6158ad5ad102593696b`,
`5551ad52c75003ccb5caee506b4135b51f82b8da64c08f9a1f3c4aef707d66eb`).

## Reading

`.xls` files are OLE2 (BIFF8) workbooks, read with `xlrd` 2.0.2; every sheet is dumped
cell by cell to `txt/<file>.txt` by the dumper embedded in this directory's workflow, and
`compare.py` re-extracts each holiday row into `xls_records.json` keyed by
(file, sheet, product row, calendar date, column header, value). `render.py` prints a
sheet as one line per modelled family. The two `.zip` bundles are the year's schedules
packaged together and are retrieved for completeness; no row is sourced from them.

## Artifacts

`doc id` is the identifier used in `cme-2013-2015.json`'s `documents` map; `-` means the
file was retrieved and searched but no row cites it.

| doc id | file | original URL | replay URL | capture time (UTC) | sha256 | bytes |
|---|---|---|---|---|---|---|
| `X13GFPD` | `xls/2013-good-friday-presidents-day__20130623203632.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-good-friday-presidents-day.xls | https://web.archive.org/web/20130623203632id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-good-friday-presidents-day.xls | 2013-06-23T20:36:32Z | `47950a6efe58edd74924c802a2eb50a820bf21ce104b83f7c18544f679f44987` | 162304 |
| `-` | `xls/2013-holiday-calendars__20140326193052.zip` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-holiday-calendars.zip | https://web.archive.org/web/20140326193052id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-holiday-calendars.zip | 2014-03-26T19:30:52Z | `4a568d6fb668fd54f9362554f62a4e101074698e6d7429c014fb2f6676724648` | 1658093 |
| `-` | `xls/2013-martin-luther-king__20130309115301.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-martin-luther-king.xls | https://web.archive.org/web/20130309115301id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-martin-luther-king.xls | 2013-03-09T11:53:01Z | `99de0cc03e1195fc8dd6b6a5db43aba78f7d338a9d1144b84ba0d3470002272d` | 79872 |
| `-` | `xls/2013-presidents-day__20130623204106.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-presidents-day.xls | https://web.archive.org/web/20130623204106id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-presidents-day.xls | 2013-06-23T20:41:06Z | `39ac098a4f0d36d4b8726fb5317cb79b6b1367a4ce0e79f456a7ec362f4c776c` | 62976 |
| `-` | `xls/2014-4th-of-july-holiday-schedule__20140326153914.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-4th-of-july-holiday-schedule.xls | https://web.archive.org/web/20140326153914id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-4th-of-july-holiday-schedule.xls | 2014-03-26T15:39:14Z | `c2f5c019da747ec87088f83e93baa6a3f08d027ce1ce87a46ce8e49c14db78af` | 79360 |
| `X14J4` | `xls/2014-4th-of-july-holiday-schedule__20140708032115.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-4th-of-july-holiday-schedule.xls | https://web.archive.org/web/20140708032115id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-4th-of-july-holiday-schedule.xls | 2014-07-08T03:21:15Z | `b2de5f4f96832cf2b4f790c6dbbe9980fd9165d4bb7b4a303f975baa01a9d1cb` | 76800 |
| `X14XM` | `xls/2014-christmas-holiday-schedule__20140326153306.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-christmas-holiday-schedule.xls | https://web.archive.org/web/20140326153306id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-christmas-holiday-schedule.xls | 2014-03-26T15:33:06Z | `5e8fa3559e2215f2a417c77253c27a3ea29a80ab59bb1f7639728cc5a36252b6` | 51200 |
| `X14ANN` | `xls/2014-cme-group-holiday-schedule__20140826204712.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-cme-group-holiday-schedule.xls | https://web.archive.org/web/20140826204712id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-cme-group-holiday-schedule.xls | 2014-08-26T20:47:12Z | `8bdfb8274bea78b2ebe5189523abc27a977b26390ee884f6b02bc6e2f46b09ae` | 442368 |
| `-` | `xls/2014-columbus-day-holiday-schedule__20140326160057.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-columbus-day-holiday-schedule.xls | https://web.archive.org/web/20140326160057id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-columbus-day-holiday-schedule.xls | 2014-03-26T16:00:57Z | `b01b4d3e1b669f6e0bbeb0818f2516782805c6d38e41c6158ad5ad102593696b` | 34304 |
| `-` | `xls/2014-good-friday-holiday-schedule__20140326154346.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-good-friday-holiday-schedule.xls | https://web.archive.org/web/20140326154346id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-good-friday-holiday-schedule.xls | 2014-03-26T15:43:46Z | `d776a65e23bdc4a0f635c633325b0df4ce420642947b478095c2d9d4fcf17a10` | 65536 |
| `X14GF` | `xls/2014-good-friday-holiday-schedule__20140708024127.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-good-friday-holiday-schedule.xls | https://web.archive.org/web/20140708024127id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-good-friday-holiday-schedule.xls | 2014-07-08T02:41:27Z | `f8c32e4cf7f261224d2b7edb950dcd172439c7e91659105e1c9a8ad8916c3d88` | 65536 |
| `-` | `xls/2014-holiday-calendars__20150326121739.zip` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-holiday-calendars.zip | https://web.archive.org/web/20150326121739id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-holiday-calendars.zip | 2015-03-26T12:17:39Z | `fdf7349901f9da3496477bc20e96534b694fcca1c9b110530a415c371f453317` | 997267 |
| `X14LD` | `xls/2014-labor-day-holiday-schedule__20140326220207.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-labor-day-holiday-schedule.xls | https://web.archive.org/web/20140326220207id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-labor-day-holiday-schedule.xls | 2014-03-26T22:02:07Z | `53d30f6b1b0033e11958f5418b1d1f25cfd8383f1093ed8a63f24931c535e2fd` | 76288 |
| `X14MLK` | `xls/2014-martin-luther-king-holiday-schedule__20140326155006.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-martin-luther-king-holiday-schedule.xls | https://web.archive.org/web/20140326155006id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-martin-luther-king-holiday-schedule.xls | 2014-03-26T15:50:06Z | `41649bcb888601efda5889878e5420cc4d844716a5897568228c267f02f06417` | 90112 |
| `-` | `xls/2014-memorial-day-holiday-schedule__20140326153812.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-memorial-day-holiday-schedule.xls | https://web.archive.org/web/20140326153812id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-memorial-day-holiday-schedule.xls | 2014-03-26T15:38:12Z | `1497cd702ac4330aab89005fd44274d01ef8770117bfaf4b2a0773a1dbd78a2e` | 77824 |
| `X14MD` | `xls/2014-memorial-day-holiday-schedule__20140708022003.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-memorial-day-holiday-schedule.xls | https://web.archive.org/web/20140708022003id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-memorial-day-holiday-schedule.xls | 2014-07-08T02:20:03Z | `c96d0d6bc16110dede3c609930024617c9f488d4b38cdb2eb293105009b256b3` | 81920 |
| `X14PD` | `xls/2014-presidents-day-holiday-schedule__20140326153120.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-presidents-day-holiday-schedule.xls | https://web.archive.org/web/20140326153120id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-presidents-day-holiday-schedule.xls | 2014-03-26T15:31:20Z | `ef76bc22b61f969710a1379538d3e7713bc43f3f4e3f7d3ad81b7ccbe5b7ebe9` | 91136 |
| `-` | `xls/2014-thanksgiving-holiday-schedule__20140326153109.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-thanksgiving-holiday-schedule.xls | https://web.archive.org/web/20140326153109id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-thanksgiving-holiday-schedule.xls | 2014-03-26T15:31:09Z | `069a0f0a090164bb452760d5820d6e51359f5677030bc1438fc87225f70e2eb6` | 72192 |
| `X14TG` | `xls/2014-thanksgiving-holiday-schedule__20140708015206.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-thanksgiving-holiday-schedule.xls | https://web.archive.org/web/20140708015206id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-thanksgiving-holiday-schedule.xls | 2014-07-08T01:52:06Z | `ddee18248add634c544c3933296a310b190b2d58d16ac9e142af639cec1301e1` | 72192 |
| `X14VET` | `xls/2014-veterans-day-holiday-schedule__20140326155155.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-veterans-day-holiday-schedule.xls | https://web.archive.org/web/20140326155155id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-veterans-day-holiday-schedule.xls | 2014-03-26T15:51:55Z | `36d20fcca3acb30490d1b9158e8e12c2919b238ac3ca54c5a7382c3d26d66541` | 24576 |
| `X15J4M` | `xls/2015-4th-of-july-holiday-schedule__20150326113453.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-4th-of-july-holiday-schedule.xls | https://web.archive.org/web/20150326113453id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-4th-of-july-holiday-schedule.xls | 2015-03-26T11:34:53Z | `3020257e49706c7911837b20a26c143801c5d895d35c3c7bf6a0c9bc31054648` | 85504 |
| `X15J4S` | `xls/2015-4th-of-july-holiday-schedule__20150905224045.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-4th-of-july-holiday-schedule.xls | https://web.archive.org/web/20150905224045id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-4th-of-july-holiday-schedule.xls | 2015-09-05T22:40:45Z | `382273ad9829edef36afc3a7ddf7262dbc71da9e0825227a1fa81126c49889ae` | 86016 |
| `X15XMM` | `xls/2015-christmas-holiday-schedule__20150326080923.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.xls | https://web.archive.org/web/20150326080923id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.xls | 2015-03-26T08:09:23Z | `fb33039101440c8c525312b5b60d94910e97945e0c51d002e726f2ecf0894d01` | 53248 |
| `-` | `xls/2015-christmas-holiday-schedule__20150905223328.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.xls | https://web.archive.org/web/20150905223328id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.xls | 2015-09-05T22:33:28Z | `8d61cf29f2424103b619fb54f0dd5efe1bedf182db25bd694fa9be36a1a719f6` | 50176 |
| `-` | `xls/2015-christmas-holiday-schedule__20151203081205.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.xls | https://web.archive.org/web/20151203081205id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.xls | 2015-12-03T08:12:05Z | `947c8e7a67dbd07aedf678593b0e30f136e888f90e138b310853bf11b95e13bf` | 55296 |
| `X15XMF` | `xls/2015-christmas-holiday-schedule__20160205173603.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.xls | https://web.archive.org/web/20160205173603id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.xls | 2016-02-05T17:36:03Z | `c6ce2a98b1462e987814d760bfc91df54427876c2eb2dfd017a75e4a69c7eefd` | 55296 |
| `X15ANN` | `xls/2015-cme-group-holiday-schedule__20150320071217.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-cme-group-holiday-schedule.xls | https://web.archive.org/web/20150320071217id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-cme-group-holiday-schedule.xls | 2015-03-20T07:12:17Z | `13baef016ecc2d3b089273c53d767f2e6a795f3dbc9a8dfde1d196addda4af8f` | 345088 |
| `-` | `xls/2015-columbus-day-holiday-schedule__20150326113300.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-columbus-day-holiday-schedule.xls | https://web.archive.org/web/20150326113300id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-columbus-day-holiday-schedule.xls | 2015-03-26T11:33:00Z | `5551ad52c75003ccb5caee506b4135b51f82b8da64c08f9a1f3c4aef707d66eb` | 34304 |
| `-` | `xls/2015-good-friday-holiday-schedule__20150326081240.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-good-friday-holiday-schedule.xls | https://web.archive.org/web/20150326081240id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-good-friday-holiday-schedule.xls | 2015-03-26T08:12:40Z | `fe4c208aa2f2fd0f9196a66829a295099dc606874d3db138363bb7c08b63db11` | 69632 |
| `X15GF` | `xls/2015-good-friday-holiday-schedule__20150905223558.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-good-friday-holiday-schedule.xls | https://web.archive.org/web/20150905223558id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-good-friday-holiday-schedule.xls | 2015-09-05T22:35:58Z | `617ff197e9da9dc6289ed2193a8a6f9f23b99add3aafa79d2ed56f227eac5349` | 69632 |
| `-` | `xls/2015-holiday-calendars__20160808150227.zip` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-holiday-calendars.zip | https://web.archive.org/web/20160808150227id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-holiday-calendars.zip | 2016-08-08T15:02:27Z | `645d47a26dd76c3cc7bc65b3eecab3c3d14caf3684b92d7b4892d4261fa23905` | 826564 |
| `X15LDM` | `xls/2015-labor-day-holiday-schedule__20150326073728.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-labor-day-holiday-schedule.xls | https://web.archive.org/web/20150326073728id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-labor-day-holiday-schedule.xls | 2015-03-26T07:37:28Z | `c459c0607789b795803c9e95664e4c97577b8d57a453290957ae4f059408b747` | 88064 |
| `X15LDS` | `xls/2015-labor-day-holiday-schedule__20150905221329.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-labor-day-holiday-schedule.xls | https://web.archive.org/web/20150905221329id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-labor-day-holiday-schedule.xls | 2015-09-05T22:13:29Z | `209fa866f40ad289354ff9e97c80981d9d29136f6dfd5c20358e5f96a2436157` | 88064 |
| `X15MLK` | `xls/2015-martin-luther-king-holiday-schedule__20150326081057.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-martin-luther-king-holiday-schedule.xls | https://web.archive.org/web/20150326081057id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-martin-luther-king-holiday-schedule.xls | 2015-03-26T08:10:57Z | `dff154f0051afdee5001472a303cb41d0439aa7b25794e0f9744e0d27ac2406e` | 86528 |
| `-` | `xls/2015-memorial-day-holiday-schedule__20150326080234.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-memorial-day-holiday-schedule.xls | https://web.archive.org/web/20150326080234id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-memorial-day-holiday-schedule.xls | 2015-03-26T08:02:34Z | `f00ff750e75a0417756a9a8518fc84470e655c958ffe43a11e7f38b4f21c3390` | 88576 |
| `X15MD` | `xls/2015-memorial-day-holiday-schedule__20150905222827.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-memorial-day-holiday-schedule.xls | https://web.archive.org/web/20150905222827id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-memorial-day-holiday-schedule.xls | 2015-09-05T22:28:27Z | `64ab9a8647046a943c26b2d30eb06ac41d4a7a53db3723be0ad232cfa9333f6c` | 89088 |
| `X15NYX` | `xls/2015-new-years-holiday-schedule__20140326160333.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-new-years-holiday-schedule.xls | https://web.archive.org/web/20140326160333id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-new-years-holiday-schedule.xls | 2014-03-26T16:03:33Z | `6035f45f690c5ec3046b490ea4213ba3a99f40821a7e7efbcf5638647b0e978c` | 54272 |
| `X15PD` | `xls/2015-presidents-day-holiday-schedule__20150326113344.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-presidents-day-holiday-schedule.xls | https://web.archive.org/web/20150326113344id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-presidents-day-holiday-schedule.xls | 2015-03-26T11:33:44Z | `f2394e57a42615512bc972e44998eea153241c3d32a47d9ba1a3c458b55ea00b` | 90112 |
| `X15TGM` | `xls/2015-thanksgiving-holiday-schedule__20150326081728.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-thanksgiving-holiday-schedule.xls | https://web.archive.org/web/20150326081728id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-thanksgiving-holiday-schedule.xls | 2015-03-26T08:17:28Z | `2bc766d3b4144a9bf4d6c0c04888919aafa99e9da7f709e830f6a90be4241a63` | 79872 |
| `-` | `xls/2015-thanksgiving-holiday-schedule__20150905223959.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-thanksgiving-holiday-schedule.xls | https://web.archive.org/web/20150905223959id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-thanksgiving-holiday-schedule.xls | 2015-09-05T22:39:59Z | `3b8e13e520544e4976ecaab8dccfeb70950760cd23f325ed2e15b56f811586f4` | 78336 |
| `X15TGD` | `xls/2015-thanksgiving-holiday-schedule__20151203081209.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-thanksgiving-holiday-schedule.xls | https://web.archive.org/web/20151203081209id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-thanksgiving-holiday-schedule.xls | 2015-12-03T08:12:09Z | `7f78617538977426111decfd71cf68cbca2b4c86b007b6a1839ced16cbf050a2` | 86016 |
| `X15VETX` | `xls/2015-veterans-day-holiday-schedule__20150326113806.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-veterans-day-holiday-schedule.xls | https://web.archive.org/web/20150326113806id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-veterans-day-holiday-schedule.xls | 2015-03-26T11:38:06Z | `b70878c2288fd0536ca8f73649dc1e89625910dd5c382cef3c00298799719c98` | 24576 |
| `X16NYM` | `xls/2016-new-years-holiday-schedule__20150326121932.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-new-years-holiday-schedule.xls | https://web.archive.org/web/20150326121932id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-new-years-holiday-schedule.xls | 2015-03-26T12:19:32Z | `080c2feba48226304f80e2da37834d1bc55a0d2255d3d7549a8d1b7d734de688` | 55808 |
| `-` | `xls/2016-new-years-holiday-schedule__20150905223948.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-new-years-holiday-schedule.xls | https://web.archive.org/web/20150905223948id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-new-years-holiday-schedule.xls | 2015-09-05T22:39:48Z | `22798c8ca3416db8c17cd5e993d58030f2d3ef8b27e862a923ce771f5ced94bd` | 52224 |
| `X16NYD` | `xls/2016-new-years-holiday-schedule__20151203081729.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-new-years-holiday-schedule.xls | https://web.archive.org/web/20151203081729id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-new-years-holiday-schedule.xls | 2015-12-03T08:17:29Z | `ed036f1fb8a9724f3e2bdbe3681606dbe8169bc9e48911ca047537d24a66327e` | 57856 |

## What the reconciliation found

1. **The `interest_rates+fx` grouping is confirmed, not assumed.** The `.xls` prints
   `Interest Rate Products` and `FX Products` (2013: `CME Group Interest Rate` and
   `CME Group FX`) as two separate rows. Across all 45 files and every date in range the
   two rows carry **identical values in every column**. The round-0 grouping survives on
   evidence rather than on the PDFs' shared section heading.

2. **Eleven family rows carry a superseded operator statement.** In every one the
   PDF-sourced value is CME's later statement, so no recorded status or instant changed.
   Two generations account for all eleven:
   - *CME's March 2015 draft generation* — the annual master `2015-cme-group-holiday-schedule.xls`
     captured 2015-03-20 and the per-holiday twins captured 2015-03-26 — superseded by the
     September/December 2015 revisions of the same URLs and by the PDFs. It covers
     2015-07-02 (Equity `12:15 Early Close` → `16:15 Regular Close`), 2015-09-04
     (Interest Rate and FX `15:15 Early Fri. Close` → `16:00 Regular Fri. Close`),
     2015-11-25 and 2015-12-28 and 2015-12-31 (Equity and Energy `16:15` → `16:00`),
     2015-11-27 and 2015-12-24 (Grains `12:00` → `12:05`), and 2015-12-31 Livestock /
     Dairy / Lumber (`16:00 Regular Close` → `13:55 (early)`).
   - *The 2014 annual master workbook* captured 2014-08-26, whose `July 4`, `Christmas`
     and `New Years` sheets embed revisions **older** than the per-holiday files published
     alongside them — its July 4 sheet still uses the 2013-era section labels and the
     `Independance` title typo, and gives Equity a `10:30` close and NYMEX/COMEX/DME
     `12:15 CT / 13:15 ET` where both captures of the per-holiday file and the PDF give
     `12:00`. Its Christmas and New Years sheets give Interest Rate and FX a `16:15` close
     on 2014-12-26 and 2015-01-02 where the per-holiday files and the PDFs give `16:00`.
     For that pair the lineage rests on the PDFs' own `Last updated` footers (12/9/2014 and
     10/7/2014), not on capture order; that reasoning is recorded in `missing[]` so a reader
     who rejects it can treat the pair as an open T1-vs-T1 conflict.

   This also softens round-0 interpretive note 6. The pre-holiday 1515 CT Interest Rate &
   FX early close did not simply vanish from the 2015 Labor Day schedule: CME carried it in
   the March 2015 draft and removed it by the 7/20/2015 PDF revision. It is a lineage, not a
   categorical absence.

3. **41 rows gained an instant the PDF withheld.** Where a PDF says only
   `Regular close - Per each product schedule`, the `.xls` names the clock time per product
   line (Grains `14:00` in 2013 and `13:15`, later `13:20`, from 2014; Livestock / Dairy /
   Lumber `13:55` before a Monday holiday, `16:00` before a midweek one). Those are attached
   as `corroborating` statements; no recorded status or instant changed.

4. **The 2014 MLK PDF's `Tuesday, Jan 22` reopen heading is a typo**, independently
   confirmed: `2014-martin-luther-king-holiday-schedule.xls` and the 2014 master both put
   the Livestock `09:05` and Lumber `09:00` reopens under the calendar-date header
   `Tuesday, January 21`.

5. **2015-07-06 was missing** and is now recorded. D15J4 prints, under `Monday, July 6`,
   `0700 CT - MGEX Apple Juice opens`, `0800 CT - pre-open`, `0830 CT - reopen`,
   `900 CT - Lumber market open` and `905 CT - Livestock markets open`; the per-holiday
   `.xls` prints the same instants in its `Pre-opening**` and `Open` columns.

6. **Veterans Day 2014 and 2015 now have a purpose-published Globex document.**
   `2014-veterans-day-holiday-schedule.xls` and `2015-veterans-day-holiday-schedule.xls`
   are one-cell sheets stating *"Products listed on Globex are uneffected \[2015: unaffected\]
   and will run on a normal schedule"* with the date in the cell. They are attached as
   corroborating statements beside the settlement-procedures PDFs round 0 cited, whose
   two-dimensional Trading Hours table is now explicitly marked as a render rather than a
   quotation.

7. **No Nikkei line and no cryptocurrency line exists anywhere in the `.xls` corpus.**
   `grep -il nikkei txt/*.txt` and `grep -il 'bitcoin\|crypto' txt/*.txt` both return nothing
   across all 43 dumped workbooks, including the two annual masters. The round-0 conclusion
   holds; only its statement of the channels tried was false, and `missing[0]` is rewritten
   to describe the channels actually read.

## Residual risks

- The `.zip` bundles (`2013/2014/2015-holiday-calendars.zip`) were retrieved but not
  unpacked as evidence; no row is sourced from them. They are the year's schedules
  packaged together and are expected to duplicate the individual files.
- `xlrd` reads BIFF8 cell values, not cell formatting. Merged-cell headers are recovered by
  forward-filling the calendar-date row, which is how CME lays these sheets out; a cell
  whose header column was mis-assigned would be visible as a nonsensical calendar date, and
  none appeared.
- The September 2015 capture of `2015-thanksgiving-holiday-schedule.xls` prints the sheet
  note `All times are Central Time ET +1 UTC +5` for a November holiday, where the December
  capture prints `UTC +6`. That is CME's own error in the earlier revision. It is one reason
  the December capture is the one cited.
