## Amendment, 2026-09-17 UTC (stage 2.2 wave 5)

Two statements in this round-0 index are withdrawn. They are left in place
because a capture dates the observation, but neither governs.

1. The line "and the `.xls` twins of the PDFs above (same content, different
   container)" is **withdrawn and superseded by
   `../cme-2013-2015-fix/INDEX.md`**. CME's `.xls` holiday schedules are a
   different and richer document than the PDFs, not a container swap; the
   round-1 fix directory retrieved all 45 of them and reconciled them cell by
   cell.
2. Interpretive note 6, which states the 2015 Labor Day change categorically,
   is **superseded by the lineage recorded on the 2015-09-04
   `interest_rates+fx` row** of `../cme-2013-2015.json` and by the round-2
   reconciliation in `../cme-2013-2015-repair-r2/INDEX.md`. The change is real;
   the note's "That is CME's own printed change, not an inference" reads as
   covering more than the one capture it was read from.

The PDF half of CME's in-place revision history was retrieved and reconciled in
round 2: `../cme-2013-2015-repair-r2/INDEX.md` lists the 42 earlier captures of
this directory's cited URLs, with sha256 and the reconciliation result.

# INDEX — CME Group holiday schedules, calendar years 2013-2015 (task cme-2013-2015)

Retrieved 2026-09-12T04:26:53Z (UTC) by task `cme-2013-2015`.

All artifacts are CME Group's own published holiday-schedule PDFs, retrieved from the
Internet Archive Wayback Machine with `id_` raw replay (byte-identical mirror of the
operator's document). Tier **T1** under LAW-PRIMARY-SOURCES: the operator's own
statement read from a verbatim public mirror. cmegroup.com returns 403 to this machine
directly, so live retrieval of these (long-retired) file paths was not possible.

Text extracted with `pdftotext -layout` into `txt/`.

| # | file | original URL | replay URL | capture time (UTC) | sha256 | bytes | what it is |
|---|---|---|---|---|---|---|---|
| 1 | `pdf/2013-4th-of-july__20130623205825.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-4th-of-july.pdf | https://web.archive.org/web/20130623205825id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-4th-of-july.pdf | 2013-06-23T20:58:25Z | `52c62e72329866f12726363d762335c8dadfdd3407c3643f38d7ed74608e8eb7` | 71527 | Globex Fourth of July Holiday Schedule 2013 (Wed Jul 3 - Fri Jul 5 2013) |
| 2 | `pdf/2013-christmas__20140412062428.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-christmas.pdf | https://web.archive.org/web/20140412062428id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-christmas.pdf | 2014-04-12T06:24:28Z | `1389ade6b120383d05e8d6e8ed9c38f1e2394dd250c86b19606548618285e848` | 146485 | Globex Christmas Holiday Schedule 2013 (Tue Dec 24 - Thu Dec 26 2013) |
| 3 | `pdf/2013-columbus-day__20121119001554.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-columbus-day.pdf | https://web.archive.org/web/20121119001554id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-columbus-day.pdf | 2012-11-19T00:15:54Z | `9679853fc45be642403cf58cac17852bd267f228706a696128223f7093005d2d` | 85678 | Globex Columbus Day Holiday Schedule 2013 - 'Products listed on Globex are unaffected' |
| 4 | `pdf/2013-good-friday__20130623195925.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-good-friday.pdf | https://web.archive.org/web/20130623195925id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-good-friday.pdf | 2013-06-23T19:59:25Z | `c05e590c950581e19ac2e8ee5327ebcfb4fc111b231b506abefae44534ee9b68` | 63251 | Globex Good Friday Holiday Schedule 2013 (Thu Mar 28 - Mon Apr 1 2013); footer 'Last updated 3/14/2013' |
| 5 | `pdf/2013-labor-day__20130902170841.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-labor-day.pdf | https://web.archive.org/web/20130902170841id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-labor-day.pdf | 2013-09-02T17:08:41Z | `8f22671fa723d33fe36d58bb29e80ebd15370d3bf9000a9b45d56a0cab0608ef` | 81507 | Globex Labor Day Holiday Schedule 2013 (Fri Aug 30 - Tue Sep 3 2013) |
| 6 | `pdf/2013-memorial-day__20130623203604.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-memorial-day.pdf | https://web.archive.org/web/20130623203604id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-memorial-day.pdf | 2013-06-23T20:36:04Z | `7cc47e352ff4874614fdb583cecd41b3ac3fcf95be6199ea5d489b8b34d2afe7` | 70520 | Globex Memorial Day Holiday Schedule 2013 (Fri May 24 - Tue May 28 2013) |
| 7 | `pdf/2013-mlk__20121119001609.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-martin-luther-king.pdf | https://web.archive.org/web/20121119001609id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-martin-luther-king.pdf | 2012-11-19T00:16:09Z | `43a646480cc7ffca137890901c0fc716ed04403e0dabc1ef07749d2b21b70c4c` | 128212 | Globex Martin Luther King Holiday Schedule 2013 (Fri Jan 18 - Tue Jan 22 2013); footer 'Last updated 11/12/2012' |
| 8 | `pdf/2013-new-years__20130414194146.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-new-years.pdf | https://web.archive.org/web/20130414194146id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-new-years.pdf | 2013-04-14T19:41:46Z | `e29c2c968cdf20883d55acd13bab50e9df02c547826bca9d2867f5bf9b2df3f7` | 52390 | CME Globex New Year's 2013 Holiday Schedule (Mon Dec 31 2012 - Wed Jan 2 2013) |
| 9 | `pdf/2013-presidents-day__20130309115337.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-presidents-day.pdf | https://web.archive.org/web/20130309115337id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-presidents-day.pdf | 2013-03-09T11:53:37Z | `e1242116eec5b7f3c5748e61adbf5bf7a809f48739ad456391f1d8b4bafceff6` | 71660 | Globex President's Day Holiday Schedule 2013 (Fri Feb 15 - Tue Feb 19 2013); footer 'Last updated 1/10/2013' |
| 10 | `pdf/2013-thanksgiving__20140214062836.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-thanksgiving.pdf | https://web.archive.org/web/20140214062836id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-thanksgiving.pdf | 2014-02-14T06:28:36Z | `1f7f6428990a5bd01065f31c4388bf5aeeb12d9219e5af6d16b1cec86bbc158b` | 75026 | Globex Thanksgiving Holiday Schedule 2013 (Wed Nov 27 - Fri Nov 29 2013) |
| 11 | `pdf/2013-veterans-day__20121119001630.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-veterans-day.pdf | https://web.archive.org/web/20121119001630id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2013-veterans-day.pdf | 2012-11-19T00:16:30Z | `7e5bd54859002a29f50ef3f1eec1f46f3fd3a7d51e9aed303f189a097719252b` | 85574 | Globex Veterans Day Holiday Schedule 2013 - 'Products listed on Globex are unaffected' |
| 12 | `pdf/2014-4th-of-july__20140708015736.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-4th-of-july-holiday-schedule.pdf | https://web.archive.org/web/20140708015736id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-4th-of-july-holiday-schedule.pdf | 2014-07-08T01:57:36Z | `34faa82435c6d8bb1088593c8945b6a5faaaa67b36c6a6422a24e4a25572ba77` | 56112 | Globex Fourth of July Holiday Schedule 2014 (Thu Jul 3 - Mon Jul 7 2014) |
| 13 | `pdf/2014-christmas__20150121141000.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-christmas-holiday-schedule.pdf | https://web.archive.org/web/20150121141000id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-christmas-holiday-schedule.pdf | 2015-01-21T14:10:00Z | `8125a18c9cad9b770be39b89c3193ee419240d409e39aa510d6eb3e8eba94e25` | 54124 | Globex Christmas Holiday Schedule 2014 (Wed Dec 24 - Fri Dec 26 2014); footer 'Last updated 12/9/2014' |
| 14 | `pdf/2014-good-friday__20140326152735.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-good-friday-holiday-schedule.pdf | https://web.archive.org/web/20140326152735id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-good-friday-holiday-schedule.pdf | 2014-03-26T15:27:35Z | `4e8593e96eb42af2cde99f6ed906d4fe4a2ea8f976fc9f8d8f561f3049cc7f0e` | 105279 | Globex Good Friday Holiday Schedule 2014 (Thu Apr 17 - Mon Apr 21 2014) |
| 15 | `pdf/2014-labor-day__20140912071608.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-labor-day-holiday-schedule.pdf | https://web.archive.org/web/20140912071608id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-labor-day-holiday-schedule.pdf | 2014-09-12T07:16:08Z | `dfd92a530d114a1f1c68dd52be4315fd307d8f8cfb344d71de78334b9c73e4d6` | 60291 | Globex Labor Day Holiday Schedule 2014 (Fri Aug 29 - Tue Sep 2 2014) |
| 16 | `pdf/2014-memorial-day__20140708020155.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-memorial-day-holiday-schedule.pdf | https://web.archive.org/web/20140708020155id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-memorial-day-holiday-schedule.pdf | 2014-07-08T02:01:55Z | `a8e020149657b4e4730c2a357015d096a9fd47e2054ca59a85d6e6548ccb6023` | 60121 | Globex Memorial Day Holiday Schedule 2014 (Fri May 23 - Tue May 27 2014) |
| 17 | `pdf/2014-mlk__20140326160215.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-martin-luther-king-holiday-schedule.pdf | https://web.archive.org/web/20140326160215id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-martin-luther-king-holiday-schedule.pdf | 2014-03-26T16:02:15Z | `5069a46a6acfb69bf05261abc23097fd675d159cf55e45361fb7e1e41dc0dcd4` | 138368 | Globex Martin Luther King Holiday Schedule 2014 (Fri Jan 17 - Tue Jan 21 2014) |
| 18 | `pdf/2014-new-years__20131007205800.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-new-years.pdf | https://web.archive.org/web/20131007205800id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-new-years.pdf | 2013-10-07T20:58:00Z | `ca6da5edc26537d341b5148781c43c8ef00e33e832c8e602b97c57d6508b8f28` | 205983 | Globex New Year's 2014 Holiday Schedule (Tue Dec 31 2013 - Thu Jan 2 2014) |
| 19 | `pdf/2014-presidents-day__20140214192332.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-presidents-day-holiday-schedule.pdf | https://web.archive.org/web/20140214192332id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-presidents-day-holiday-schedule.pdf | 2014-02-14T19:23:32Z | `b689b4f8e9f62ba6f8c32bba46d35923a4017d1edbc83cc9ffcc2a85baded4fb` | 116612 | Globex President's Day Holiday Schedule 2014 (Fri Feb 14 - Tue Feb 18 2014) |
| 20 | `pdf/2014-thanksgiving__20150121145456.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-thanksgiving-holiday-schedule.pdf | https://web.archive.org/web/20150121145456id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-thanksgiving-holiday-schedule.pdf | 2015-01-21T14:54:56Z | `a90ae1f39414337f1a8600f55bf3a0a587214d987074885a47cfea307bc8054a` | 60428 | Globex Thanksgiving Holiday Schedule 2014 (Wed Nov 26 - Fri Nov 28 2014) |
| 21 | `pdf/2014-veterans-day__20141113193450.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-veterans-day-holiday-schedule.pdf | https://web.archive.org/web/20141113193450id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-veterans-day-holiday-schedule.pdf | 2014-11-13T19:34:50Z | `53ea2a8b03d8b71640a2a054eb1d4cc5dd220d4ebc0fd21f7f2890e21a55c2b6` | 97624 | Modified Daily Settlement Procedures for Interest Rate and FX Products on Veterans Day Nov 11 2014 - carries the Veterans Day Trading Hours table |
| 22 | `pdf/2015-4th-of-july__20150905222733.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-4th-of-july-holiday-schedule.pdf | https://web.archive.org/web/20150905222733id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-4th-of-july-holiday-schedule.pdf | 2015-09-05T22:27:33Z | `1013e6ebea1829591946c9aa513ec6e3f99c64d99be14814610e601bb5dcc0fb` | 122744 | Globex Fourth of July Holiday Schedule 2015 (Thu Jul 2 - Mon Jul 6 2015) |
| 23 | `pdf/2015-christmas__20151123061520.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.pdf | https://web.archive.org/web/20151123061520id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-christmas-holiday-schedule.pdf | 2015-11-23T06:15:20Z | `7fde46210798f2cb4299903400b41ef6e2cb9aa287f8d3d360ba59d835b482ec` | 54852 | Globex Christmas Holiday Schedule 2015 (Thu Dec 24 - Mon Dec 28 2015); footer 'Last updated 10/27/2015' |
| 24 | `pdf/2015-good-friday__20150905223230.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-good-friday-holiday-schedule.pdf | https://web.archive.org/web/20150905223230id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-good-friday-holiday-schedule.pdf | 2015-09-05T22:32:30Z | `67873caa987c9eee8de38d02a5c18d8f7d46fd82a486bab34821f6e6f6363e0b` | 54240 | Globex Good Friday Holiday Schedule 2015 (Thu Apr 2 - Mon Apr 6 2015) |
| 25 | `pdf/2015-labor-day__20150824023039.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-labor-day-holiday-schedule.pdf | https://web.archive.org/web/20150824023039id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-labor-day-holiday-schedule.pdf | 2015-08-24T02:30:39Z | `4aab7fdb5e57420a243bbc26be6ecfa00a6317937afe3b772dfcdd8db1dd50fd` | 107305 | Globex Labor Day Holiday Schedule 2015 (Fri Sep 4 - Tue Sep 8 2015) |
| 26 | `pdf/2015-memorial-day__20150326113938.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-memorial-day-holiday-schedule.pdf | https://web.archive.org/web/20150326113938id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-memorial-day-holiday-schedule.pdf | 2015-03-26T11:39:38Z | `4ad4398fa092393fa77cd8ed9c58ecc0f1669a41fd38a9b4cab5b05790d2dfec` | 139573 | Globex Memorial Day Holiday Schedule 2015 (Fri May 22 - Tue May 26 2015) |
| 27 | `pdf/2015-mlk__20150121141012.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-martin-luther-king-holiday-schedule.pdf | https://web.archive.org/web/20150121141012id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-martin-luther-king-holiday-schedule.pdf | 2015-01-21T14:10:12Z | `67395dcb63d86b6e1f573a5aa37269a685dfe1b17d23edd7d95449899bce090a` | 59439 | Globex Martin Luther King Holiday Schedule 2015 (Fri Jan 16 - Tue Jan 20 2015) |
| 28 | `pdf/2015-new-years__20150121141043.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-new-years-holiday-schedule.pdf | https://web.archive.org/web/20150121141043id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-new-years-holiday-schedule.pdf | 2015-01-21T14:10:43Z | `196b4ec04bcfce2cfd9783262023afe9da73bcdef1b983c8c4b464b2e115bb8a` | 59206 | Globex New Year's 2015 Holiday Schedule (Wed Dec 31 2014 - Fri Jan 2 2015) |
| 29 | `pdf/2015-presidents-day__20150121192401.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-presidents-day-holiday-schedule.pdf | https://web.archive.org/web/20150121192401id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-presidents-day-holiday-schedule.pdf | 2015-01-21T19:24:01Z | `c81b04bcf43dbfd2b7c2f7aba559992cde8bb8eee59e7b310b643b636d290b94` | 60496 | Globex President's Day Holiday Schedule 2015 (Fri Feb 13 - Tue Feb 17 2015) |
| 30 | `pdf/2015-thanksgiving__20160205162519.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-thanksgiving-holiday-schedule.pdf | https://web.archive.org/web/20160205162519id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-thanksgiving-holiday-schedule.pdf | 2016-02-05T16:25:19Z | `ef96d05289667c635f435884a0a2407bcbec63149ff96e802b719100c85c887f` | 60424 | Globex Thanksgiving Holiday Schedule 2015 (Wed Nov 25 - Fri Nov 27 2015) |
| 31 | `pdf/2015-veterans-day__20151122230920.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-veterans-day-schedule.pdf | https://web.archive.org/web/20151122230920id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-veterans-day-schedule.pdf | 2015-11-22T23:09:20Z | `50300dd36faff3b7d52128ea48a04e4c27012a78985b6c390ea9883e1696f98e` | 94646 | Modified Daily Settlement Procedures for Interest Rate and FX Products on Veterans Day Nov 11 2015 - carries the Veterans Day Trading Hours table |
| 32 | `pdf/2016-new-years__20160108203007.pdf` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-new-years-holiday-schedule.pdf | https://web.archive.org/web/20160108203007id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2016-new-years-holiday-schedule.pdf | 2016-01-08T20:30:07Z | `118196a469dd40ad6a40594da273f726f6cb3e503f9cc1b8fd2057cf2fa32c61` | 64156 | Globex New Year's 2016 Holiday Schedule (Thu Dec 31 2015 - Mon Jan 4 2016); sources the Dec 31 2015 lines |

## Enumeration method

CDX prefix search saved as `cdx_holiday_calendar.json`:

```
https://web.archive.org/cdx/search/cdx?url=cmegroup.com/tools-information/holiday-calendar*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&from=2012&to=2017&collapse=digest
```
Retrieved 2026-09-12T04:26:53Z. It enumerates every holiday document CME published under that path for
2013-2016; the per-holiday PDFs above are the complete 2013-2015 set of *trading-hours*
documents. Documents deliberately NOT used as session evidence: the
`*-settlement-times-*` / `*-settlement-procedures*` PDFs (daily-settlement methodology, not
session language — LAW-SESSION-NOT-EXPIRY), the `*floor*`/`*trading-floor*` cards (open
outcry, not Globex), the ClearPort calendars (clearing, not a matching venue), and the
`.xls` twins of the PDFs above (same content, different container).


## Addendum — Columbus Day 2014 / 2015 (.xls, no PDF was published)

| file | original URL | replay URL | capture time (UTC) | sha256 | bytes | what it is |
|---|---|---|---|---|---|---|
| `xls/2014-columbus-day__20140326160057.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-columbus-day-holiday-schedule.xls | https://web.archive.org/web/20140326160057id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2014-columbus-day-holiday-schedule.xls | 2014-03-26T16:00:57Z | `b01b4d3e1b669f6e0bbeb0818f2516782805c6d38e41c6158ad5ad102593696b` | 34304 | Globex Columbus Day Holiday Schedule, Monday, October 13 2014 - single-cell sheet 'Columbus': 'Products listed on Globex are uneffected [sic] and will run on a normal schedule' |
| `xls/2015-columbus-day__20150326113300.xls` | http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-columbus-day-holiday-schedule.xls | https://web.archive.org/web/20150326113300id_/http://www.cmegroup.com/tools-information/holiday-calendar/files/2015-columbus-day-holiday-schedule.xls | 2015-03-26T11:33:00Z | `5551ad52c75003ccb5caee506b4135b51f82b8da64c08f9a1f3c4aef707d66eb` | 34304 | Globex Columbus Day Holiday Schedule, Monday, October 12 2015 - single-cell sheet 'Columbus': 'Products listed on Globex are unaffected and will run on a normal schedule' |

Read with `xlrd`; retrieved 2026-09-12T04:29:09Z.


## Interpretive notes and residual risks

1. **Tier.** Every row is T1: CME Group's own published Globex holiday-schedule PDF (or, for
   Columbus Day 2014/2015, its own .xls), read as bytes from the Internet Archive's `id_`
   raw replay, which returns the archived response body unmodified. cmegroup.com refuses
   direct requests from this machine (403) and these 2013-2015 file paths are long retired,
   so the archive is the only public channel; `r.jina.ai` was not used for these because the
   documents are binaries no longer served at their original URLs.

2. **Zones as printed.** 2013 documents print CT only for CME/CBOT sections and
   `CT / ET` for the NYMEX/COMEX/DME section. From the January-2014 documents onward CME
   prints `CT / ET / UTC` for every section. Both are recorded exactly as printed.

3. **Operator errors preserved, not corrected.**
   - 2014 MLK schedule, Interest Rate & FX, Friday Jan 17: `1515 CT / 1615 ET / 2215 UTC`.
     1515 CT is 2115 UTC; CME's UTC column is wrong on that line. Recorded verbatim with the
     discrepancy flagged in `close_instant`.
   - 2014 MLK schedule, Livestock/Lumber reopen lines are headed "Tuesday, Jan 22"; the
     trade date in question is Tuesday Jan 21 2014 (Jan 22 2014 was a Wednesday).
   - 2014 Columbus Day .xls reads "uneffected"; 2015's reads "unaffected".
   - 2014 Christmas, Livestock/Dairy/Lumber, reads "Wednesday, Dec, Dec 24".
   - 2014 Memorial Day, Dairy, reads "Dairy markets pen for trade date Tuesday, May 27".

4. **The "trading halt" days.** On a Monday holiday (and on Thanksgiving Day and
   Independence Day when it falls midweek) CME does not close Globex: the session that
   carries the *next* business day's trade date runs from the prior 1700 CT open, halts at a
   stated instant during the holiday, and the products resume at the regular 1700 CT open.
   Those days are recorded as `early_close` with `close_instant` = the stated halt instant
   and `open_instant` = the stated resume instant, because that is what the operator states.

5. **Grain / Livestock / Dairy / Lumber on Monday holidays** genuinely have *no* trade date:
   CME states a Sunday pre-open for the Tuesday trade date and a Monday-evening open for the
   Tuesday trade date. Those are recorded as `closed` with `open_instant` naming the stated
   reopen and the trade date it carries.

6. **The pre-holiday 1515 CT Interest Rate & FX early close** appears on the Friday before
   MLK, Presidents' Day, Memorial Day and Labor Day from 2013 through Memorial Day 2015, and
   is *absent* from the 2015 Labor Day schedule (Friday Sep 4 2015 prints
   `1600 CT / 1700 ET / 2100 UTC - Regular close`). That is CME's own printed change, not an
   inference.

7. **Good Friday 2015 is the outlier**: Equity Products closed early at
   `0815 CT / 0915 ET / 1315 UTC` and Interest Rate & FX at `1015 CT / 1115 ET / 1515 UTC`
   on Friday April 3 2015, while Energy/Metals, Grain/Oilseed and Livestock/Dairy/Lumber were
   fully closed. Good Friday 2013 and 2014 were full Globex closures for every group.

8. **The equity/energy holiday halt moved from 1030/1215 CT to 1200 CT** between the
   President's Day 2014 schedule (1030 CT equity, 1215 CT energy/metals) and the Memorial Day
   2014 schedule (1200 CT for all three). Again CME's own printed change.

9. **No Nikkei-specific line exists** on any CME Group holiday schedule for 2013, 2014 or
   2015. `grep -il nikkei txt/*.txt` returns nothing. Nikkei 225 (dollar) futures sit under
   the "CME & CBOT Equity Products" / "Equity Products" heading with no separate treatment.
   The only per-product equity exceptions CME prints in this era are USD-Ibovespa futures and,
   for the day after Thanksgiving 2013, the "Big Equities (SP, MD, ND, SMP, ZD)".

10. **No cryptocurrency line exists**: CME listed no cryptocurrency product before Bitcoin
    futures (2017-12-18), so there is nothing to source for 2013-2015.

11. **Documents deliberately excluded as session evidence** (saved in CDX, not quoted as
    schedule): `*-settlement-times-*` and `*-settlement-procedures*` PDFs describe daily
    settlement methodology, which is not session language (LAW-SESSION-NOT-EXPIRY); the
    Chicago / New York trading-floor holiday cards describe open outcry, not Globex; the
    ClearPort holiday calendars describe clearing windows. The Veterans Day 2014/2015 PDFs are
    settlement-procedure documents, but each carries an explicit "Veterans Day Trading Hours"
    table stating "Electronic (CME Globex): Normal Hours", which *is* session language, so
    they are used for the Veterans Day rows only.

12. **DME** (Dubai Mercantile Exchange) shares CME's Energy/Metals section heading throughout
    this era. It is not modelled separately here.
