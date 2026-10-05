# Evidence index — `equities/tsx/cdx-retry-2026-09-30`

The CDX-service-back retry of issue #221's 2010-2016 span, run
2026-09-30 01:04-01:19 UTC (LAW-UTC-DATES). The domain-wide sweeps of
`tsx.com` (2010-2016, 5 910 collapsed url keys) and `tmx.com` (2010-2016,
15 931 collapsed url keys), the all-time `news_releases` filter sweep of
`tmx.com` (1 789 captures), and the per-URL sweeps of `tmxgroup.com`,
`tsx.ca` and `mx-group.com` (all empty) are saved verbatim as the
`cdx-*.json` files here. The sweeps surfaced TMX Group's and TSX's own
**per-holiday closure news releases** and **Holiday (Operating) Schedule**
releases for 2009-2014 under `tmx.com/en/news_events/[news/]news_releases/` —
thirty-two of them fetched as Wayback `id_` replays and sha-pinned below,
each stating Toronto Stock Exchange closures in session language with
unconditional dates. `rel-*.html` names carry the release's publication
date; the `wayback-<stamp>` segment is the capture the replay was taken
from.

The two `tmx-calendartmx*.js`/`tmx-events_calendar.js` fetches are Wayback
interstitial stubs (no content replay exists at those stamps), kept to
record the negative. `tmx-trading-calendar.wayback-20120512063841id_.html`
is the 2012 "Releases and Events Calendar" page — event data, no holiday
grid. `rel-2012-07-12-stampede...` is a market-close ceremony release,
checked and ruled out as a closure statement. `tmxgroup-holidayschedule-
2010-11-08` is the TMX-Group-named twin of the TSX release of the same
day (corroboration, not row-bearing here).

| Document id | File | Original URL | Capture | Retrieved (UTC) | What it states |
|---|---|---|---|---|---|
| `TSX-REL-2009-12-02` | `tsx-holidayschedule-2009-12-02.wayback-20100102012424id_.html` | `http://tmx.com/en/news_events/news_releases/12-2-2009_TSX-HolidaySchedule.html` | `20100102012424` | 2026-09-30T01:08:53Z | TSX/TSXV/MX closed 2009-12-25, 2009-12-28 and **2010-01-01** (New Year's Day); 2009-12-24 open until 1 p.m. EST. Row-bearing for 2010-01-01. |
| `TSX-REL-2010-02-08` | `rel-2010-02-08-tsx-familyday.wayback-20101201061455id_.html` | `http://tmx.com/en/news_events/news_releases/2-8-2010_TSX-FamilyDay.html` | `20101201061455` | 2026-09-30T01:13:06Z | TSX/TSXV closed for Family Day **2010-02-15**. |
| `TSX-REL-2010-03-26` | `rel-2010-03-26-tsx-goodfriday.wayback-20101201055224id_.html` | `http://tmx.com/en/news_events/news_releases/3-26-2010_TSX-GoodFriday.html` | `20101201055224` | 2026-09-30T01:13:12Z | TSX/TSXV/MX closed **2010-04-02** (Good Friday). |
| `TSX-REL-2010-05-17` | `rel-2010-05-17-tsx-victoriaday.wayback-20101201061525id_.html` | `http://tmx.com/en/news_events/news_releases/5-17-2010_TSX-VictoriaDayHoliday.html` | `20101201061525` | 2026-09-30T01:13:15Z | TSX/TSXV/MX closed **2010-05-24** (Victoria Day). |
| `TSX-REL-2010-07-27` | `rel-2010-07-27-tsx-civicholiday.wayback-20101201060128id_.html` | `http://tmx.com/en/news_events/news_releases/7-27-2010_TSX-CivicHoliday.html` | `20101201060128` | 2026-09-30T01:13:17Z | TSX/TSXV/MX closed **2010-08-02** (Civic Holiday). |
| `TSX-REL-2010-09-01` | `rel-2010-09-01-tsx-labourday.wayback-20101201055935id_.html` | `http://tmx.com/en/news_events/news_releases/9-1-2010_TSX-LabourDay.html` | `20101201055935` | 2026-09-30T01:13:20Z | TSX/TSXV/MX closed **2010-09-06** (Labour Day). |
| `TSX-REL-2010-10-01` | `rel-2010-10-01-tsx-thanksgiving.wayback-20101201055415id_.html` | `http://tmx.com/en/news_events/news_releases/10-1-2010_TSX-Thanksgiving.html` | `20101201055415` | 2026-09-30T01:13:23Z | TSX/TSXV/MX closed **2010-10-11** (Thanksgiving). |
| `TSX-REL-2010-11-08` | `tsx-holidayschedule-2010-11-08.wayback-20101201004014id_.html` | `http://tmx.com/en/news_events/news_releases/11-8-2010_TSX-HolidaySchedule.html` | `20101201004014` | 2026-09-30T01:08:57Z | TSX/TSXV closed **2010-12-27** (in lieu of Christmas), **2010-12-28** (in lieu of Boxing), **2011-01-03** (in lieu of New Year); 2010-12-24 open until 1:00 p.m. EST. |
| `TMX-REL-2011-02-16` | `rel-2011-02-16-familyday.wayback-20111010045533id_.html` | `http://tmx.com/en/news_events/news/news_releases/2011/2-16-2011_TMXGroup-familyday.html` | `20111010045533` | 2026-09-30T01:13:50Z | TSX/TSXV/MX closed for Family Day **2011-02-21**. |
| `TMX-REL-2011-04-14` | `rel-2011-04-14-goodfriday.wayback-20111010050037id_.html` | `http://tmx.com/en/news_events/news/news_releases/2011/4-14-2011_TMXGroup-goodfriday.html` | `20111010050037` | 2026-09-30T01:13:53Z | TSX/TSXV/MX closed **2011-04-22** (Good Friday). |
| `TMX-REL-2011-05-18` | `rel-2011-05-18-victoriaday.wayback-20111010030017id_.html` | `http://tmx.com/en/news_events/news/news_releases/2011/5-18-2011_TMXGroup-victoriaday.html` | `20111010030017` | 2026-09-30T01:13:55Z | TSX/TSXV/MX closed **2011-05-23** (Victoria Day). |
| `TMX-REL-2011-06-22` | `rel-2011-06-22-canadaday.wayback-20111010023004id_.html` | `http://tmx.com/en/news_events/news/news_releases/2011/6-22-2011_TMXGroup-canada_day_june11.html` | `20111010023004` | 2026-09-30T01:13:58Z | TSX/TSXV/MX closed **2011-07-01** (Canada Day). |
| `TMX-REL-2011-07-25` | `rel-2011-07-25-civicholiday.wayback-20110814063225id_.html` | `http://www.tmx.com/en/news_events/news/news_releases/2011/7-25-2011_TMXGroup-closed_civic_holiday.html` | `20110814063225` | 2026-09-30T01:14:01Z | TSX/TSXV/TMX Select/MX closed **2011-08-01** (Civic Holiday). |
| `TMX-REL-2011-08-30` | `rel-2011-08-30-labourday.wayback-20111010050329id_.html` | `http://tmx.com/en/news_events/news/news_releases/2011/8-30-2011_TMXGroup-ClosedLabourDay.html` | `20111010050329` | 2026-09-30T01:14:04Z | TSX/TSXV/TMX Select/MX closed **2011-09-05** (Labour Day). |
| `TMX-REL-2011-09-30` | `rel-2011-09-30-thanksgiving.wayback-20111010050414id_.html` | `http://tmx.com/en/news_events/news/news_releases/2011/9-30-2011_TMXGroup-thanksgiving_closure.html` | `20111010050414` | 2026-09-30T01:14:06Z | TSX/TSXV/TMX Select/MX closed **2011-10-10** (Thanksgiving). |
| `TMX-REL-2012-02-13` | `rel-2012-02-13-familyday.wayback-20120519053604id_.html` | `http://www.tmx.com/en/news_events/news/news_releases/2012/2-13-2012_TMXGroup-family_day_closed.html` | `20120519053604` | 2026-09-30T01:14:22Z | TSX/TSXV/MX/TMX Select closed for Family Day **2012-02-20**. |
| `TMX-REL-2012-03-30` | `rel-2012-03-30-goodfriday.wayback-20120519054000id_.html` | `http://www.tmx.com/en/news_events/news/news_releases/2012/3_30_2012_TMX_market_closed_good_friday.html` | `20120519054000` | 2026-09-30T01:14:24Z | TSX/TSXV/MX/TMX Select closed **2012-04-06** (Good Friday). |
| `TMX-REL-2012-05-14` | `rel-2012-05-14-victoriaday.wayback-20120920075441id_.html` | `http://tmx.com/en/news_events/news/news_releases/2012/5-14-2012_TMXGroup-closed_victoria_day.html` | `20120920075441` | 2026-09-30T01:14:27Z | TSX/TSXV/TMX Select/MX closed **2012-05-21** (Victoria Day). |
| `TMX-REL-2012-06-22` | `rel-2012-06-22-canadaday.wayback-20120920080159id_.html` | `http://tmx.com/en/news_events/news/news_releases/2012/6-22-2012_TMXGroup-closed_canada_day.html` | `20120920080159` | 2026-09-30T01:14:30Z | TSX/TSXV/TMX Select/MX closed **2012-07-02** (Canada Day in lieu of the Sunday). |
| `TMX-REL-2012-07-31` | `rel-2012-07-31-civicholiday.wayback-20120920075800id_.html` | `http://tmx.com/en/news_events/news/news_releases/2012/7-31-2012_TMXGroup-CivicHoliday.html` | `20120920075800` | 2026-09-30T01:14:34Z | TSX/TSXV/TMX Select/MX closed **2012-08-06** (Civic Holiday). |
| `TMX-REL-2012-08-24` | `rel-2012-08-24-labourday.wayback-20120920080314id_.html` | `http://tmx.com/en/news_events/news/news_releases/2012/8-24-2012_TMXGroup-LabourDay.html` | `20120920080314` | 2026-09-30T01:14:37Z | TSX/TSXV/MX/TMX Select/Alpha closed **2012-09-03** (Labour Day). |
| `TMX-REL-2012-09-28` | `rel-2012-09-28-thanksgiving.wayback-20121102153750id_.html` | `http://www.tmx.com/en/news_events/news/news_releases/2012/9-28-2012_TMXGroup-Thanksgiving.html` | `20121102153750` | 2026-09-30T01:14:40Z | TSX/TSXV/MX/TMX Select/Alpha closed **2012-10-08** (Thanksgiving). |
| `TMX-REL-2012-11-28` | `tmxgroup-holidayoperating-2012-11-28.wayback-20121211200307id_.html` | `http://tmx.com/en/news_events/news/news_releases/2012/11-28-2012_TMXGroup-TMX-Group-Holiday-Operating-Schedule.html` | `20121211200307` | 2026-09-30T01:09:01Z | TSX/TSXV/TMX Select/Alpha/MX closed **2012-12-25**, **2012-12-26**, **2013-01-01**; 2012-12-24 open until 1:00 p.m. EST; 2012-12-31 open. |
| `TMX-REL-2013-01-30` | `rel-2013-01-30-familyday.wayback-20130818173444id_.html` | `http://tmx.com/en/news_events/news/news_releases/2013/1-30-2013_TMXGroup-family-day.html` | `20130818173444` | 2026-09-30T01:16:19Z | TSX/TSXV/MX/TMX Select/Alpha closed **2013-02-18** (Family Day). |
| `TMX-REL-2013-03-20` | `rel-2013-03-20-goodfriday.wayback-20130818193156id_.html` | `http://tmx.com/en/news_events/news/news_releases/2013/3-20-0-2013_TMXGroup-GoodFridayMarketClosed.html` | `20130818193156` | 2026-09-30T01:16:19Z | TSX/TSXV/MX/TMX Select/Alpha closed **2013-03-29** (Good Friday). |
| `TMX-REL-2013-05-13` | `rel-2013-05-13-victoriaday.wayback-20130818195457id_.html` | `http://tmx.com/en/news_events/news/news_releases/2013/5-13-2013_TMXGroup-VictoriaDay.html` | `20130818195457` | 2026-09-30T01:16:36Z | TSX/TSXV/MX/TMX Select/Alpha closed **2013-05-20** (Victoria Day). |
| `TMX-REL-2013-06-24` | `rel-2013-06-24-canadaday.wayback-20130818165636id_.html` | `http://tmx.com/en/news_events/news/news_releases/2013/6-24-2013_TMXGroup-CanadaDay.html` | `20130818165636` | 2026-09-30T01:16:36Z | TSX/TSXV/TMX Select/MX/Alpha closed **2013-07-01** (Canada Day). |
| `TMX-REL-2013-07-26` | `rel-2013-07-26-civicholiday.wayback-20130806002842id_.html` | `http://tmx.com/en/news_events/news/news_releases/2013/7-26-2013_TMXGroup-Civic-Holiday.html` | `20130806002842` | 2026-09-30T01:16:37Z | TSX/TSXV/TMX Select/Alpha/MX closed **2013-08-05** (Civic Holiday). |
| `TMX-REL-2014-02-07` | `rel-2014-02-07-familyday.wayback-20140209142427id_.html` | `http://tmx.com/en/news_events/news/news_releases/2014/02-07-2014_TMXGroup-ClosedFamilyDay.html` | `20140209142427` | 2026-09-30T01:16:49Z | TSX/TSXV/MX/TMX Select/Alpha closed **2014-02-17** (Family Day). |
| `TMX-REL-2014-04-09` | `rel-2014-04-09-goodfriday.wayback-20140714210509id_.html` | `http://tmx.com/en/news_events/news/news_releases/2014/04-09-2014_TMXGroup-GoodFriday.html` | `20140714210509` | 2026-09-30T01:17:05Z | TSX/TSXV/MX/TMX Select/Alpha closed **2014-04-18** (Good Friday). |
| `TMX-REL-2014-05-13` | `rel-2014-05-13-victoriaday.wayback-20140714225156id_.html` | `http://tmx.com/en/news_events/news/news_releases/2014/05-13-2014_TMXGroup-VictoriaDay.html` | `20140714225156` | 2026-09-30T01:17:08Z | TSX/TSXV/MX/TMX Select/Alpha closed **2014-05-19** (Victoria Day). |
| `TMX-REL-2014-06-23` | `rel-2014-06-23-canadaday.wayback-20140629102827id_.html` | `http://tmx.com/en/news_events/news/news_releases/2014/06-23-2014_TMXGroup-CanadaDayClosing.html` | `20140629102827` | 2026-09-30T01:17:09Z | TSX/TSXV/TMX Select/Alpha/MX closed **2014-07-01** (Canada Day). |

Non-row-bearing: `tmxgroup-holidayschedule-2010-11-08.wayback-20101130201452id_.html`
(the TMX Group twin of `TSX-REL-2010-11-08`, capture `20101130201452`,
retrieved 2026-09-30T01:09:05Z, corroboration only),
`tmx-trading-calendar.wayback-20120512063841id_.html` (event calendar),
`rel-2012-07-12-stampede.wayback-20120826025740id_.html` (ceremony,
ruled out), and the three `tmx-*.js` stubs.

Every file's sha256 is recorded in `SHA256SUMS.txt`.
