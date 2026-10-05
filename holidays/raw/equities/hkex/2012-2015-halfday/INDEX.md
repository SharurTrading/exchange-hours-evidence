# HKEX 2012-2015 half-day close retrieval (2026-09-30 UTC)

Closes #208. The operator's own Securities Trading Information "Trading Hours"
page (`www.hkex.com.hk/eng/market/sec_tradinfo/tradcal/tradcal_1.htm`) prints,
at every capture below, the Phase-Two grid (Pre-opening 9:00-9:30 a.m.;
Morning Session 9:30 a.m. to 12:00 noon; Extended Morning Session 12:00 noon
to 1:00 p.m.; Afternoon Session 1:00 p.m. to 4:00 p.m.) and the eve
arrangement in session language:

> There is no Extended Morning Session and Afternoon Session on the eves of
> Christmas, New Year and Lunar New Year. There will be no Extended Morning
> Session if there is no Morning Session.

So each calendar-named half-day trading day of the era closes at the end of
the Morning Session, 12:00 noon venue-local. Captures (Wayback `id_` replays):

| capture | file | role |
|---|---|---|
| 20110721T125749Z | wayback_hkex_tradcal1_capture-20110721T125749Z.html | Phase-1 grid with the same eve sentence (12:00-13:30 extended morning) |
| 20121213T083938Z | wayback_hkex_tradcal1_capture-20121213T083938Z.html | Phase-2 grid, 11 days before the 2012-12-24 eve |
| 20130218T094843Z | wayback_hkex_tradcal1_capture-20130218T094843Z.html | 2013 bracket |
| 20131204T062020Z | wayback_hkex_tradcal1_capture-20131204062020.html | 20 days before the 2013-12-24 eve |
| 20140204T043814Z | wayback_hkex_tradcal1_capture-20140204043814.html | bracket for the 2014-01-30 LNY eve |
| 20141130T110157Z | wayback_hkex_tradcal1_capture-20141130110157.html | before the 2014-12 eves |
| 20150201T145531Z | wayback_hkex_tradcal1_capture-20150201145531.html | bracket for the 2015-02-18 LNY eve |
| 20151102T025014Z | wayback_hkex_tradcal1_capture-20151102025014.html | before the 2015-12 eves |
| 20160120T022906Z | wayback_hkex_tradcal1_capture-20160120022906.html | era-end bracket (CAS launch 2016-07-25 ends the era) |

All captures byte-identical apart from Wayback rewriting (14557 bytes each);
the CDX digests for the page are identical (`NUPGGY77O6LAABFVD53274CQS63WV225`)
from 2012-03-02 through 2014-06-14 and the content matches at every later
capture through 2016-01-20.
