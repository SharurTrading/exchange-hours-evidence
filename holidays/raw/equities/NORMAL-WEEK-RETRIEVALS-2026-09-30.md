# Normal-week horizon retrievals, 2026-09-30 UTC

Wave C2: the equities/softs carried normal-week grids, sourced back toward the
2010-01-01 floor. Each directory below holds the fetched operator artifacts;
every digest was computed on the saved bytes at retrieval. All Wayback fetches
are `id_` replays of the capture named in the filename (the NYSE PDF was
located through the `20120812` shorthand replay whose redirect named
`20120812235441`; the two Nasdaq PDFs are the plain replay of their capture —
the `id_` form returned empty bytes for the `ftp.nasdaqtrader.com` URL and the
plain replay of a PDF serves the original file).

## equities/hkex/normal-week/

| Capture (UTC) | File | Original URL | sha256 |
|---|---|---|---|
| `20100503120005` | `hkex_nont10.wayback-20100503120005id_.html` | `http://www.hkex.com.hk/eng/market/sec_tradinfo/tradcal/nont10.htm` (Holiday Schedule, updated 24/07/2009) | `e2885ce0c70e1338da2f1c8de83952cc610861c770fe6208f87971be790b3c15` |
| `20100524085427` | `hkex_tradcal_1.wayback-20100524085427id_.html` | `http://www.hkex.com.hk/eng/market/sec_tradinfo/tradcal/tradcal_1.htm` (Trading Hours, footer `Updated: 23/03/2009`) | `5b5c556465d3c9b8db07a074709db03964a0190478fbc5c5b544a82ff153edf5` |
| `20101219233021` | `hkex_tradcal_1.wayback-20101219233021id_.html` | same URL — the last pre-change observation | `14772b65160765b7aaaceaf0fd006daacf205de3090446a3f06f3d5cbf3f6239` |
| `20110309232522` | `hkex_tradcal_1.wayback-20110309232522id_.html` | same URL — first post-Phase-One state (Current / Effective 5 March 2012 columns) | `a281b6810551fdaf5000a53e562a2d69fc0ec636997e7c9e434cfbe48e3cdd4e` |
| `20100525123656` | `hkex_tradcal_6.wayback-20100525123656id_.html` | `.../tradcal/tradcal_6.htm` (typhoon arrangements; keys no row) | `1ed1cefcbaa74dd8015b76d1e535d629f4bc564775d7453193bf9a4819d5304a` |

CDX capture history of `tradcal_1.htm` 2009-2011: `20100524085427` (digest
FYOYO…), then `20100628233229`, `20100818073934`, `20101219233021`,
`20110119131654` (all digest SQZY…, identical bytes), then `20110309232522`
onward (digest 6JIG…, the Phase-One page). The session-table text is identical
at every pre-change observation; the 2010-05-24 page's whole-file digest differs
from the later ones (page chrome, not the table).

## equities/sgx_securities/normal-week/

| Capture (UTC) | File | Original URL | sha256 |
|---|---|---|---|
| `20090514003555` | `sgx_securities_trading_hours.wayback-20090514003555id_.html` | `http://www.sgx.com:80/wps/wcm/connect/mp_en/site/trading_on_sgx/securities_market/securities_trading_and_settlement/Trading+Hours?` | `0dd72053814bf349b1177d300027cd4bfae160cc4fd75c22afa824d5f7099bf1` |

The only surviving capture of the securities Trading Hours page (checked again
2026-09-30 UTC). It prints: "Trading sessions are held daily from Mondays to
Fridays between 9.00am – 12.30pm and 2.00pm - 5.00pm. In addition, there is an
Pre-Open Routine (8.30am – 9.00am) and Pre-Close Routine (5.00pm – 5.06pm)."
Pre-floor: it dates no 2010-2011 day, so it corroborates the carried baseline's
instants without moving the horizon.

## equities/borsa_istanbul/normal-week/

| Capture (UTC) | File | Original URL | sha256 |
|---|---|---|---|
| `20100325232952` | `imkb_stockmarket_transaction_hours.wayback-20100325232952id_.html` | `http://www.imkb.gov.tr/Markets/StockMarket/TransactionHours.aspx` | `f09a1962671b53fde20f02edb86bee6de72d22f98ca719c94bb02d05a33277a2` |
| `20110727072510` | `imkb_stockmarket_transaction_hours.wayback-20110727072510id_.html` | same URL | `c0815e3e31fecbb9bbf6b4c88514e7b6de82688dd7e2a03fd9b3af26bbbb0e23` |

The 2010 page prints, for Ulusal Pazar and the other stock markets: 1. Seans
09:30-12:30 (Açılış Seansı 09:30-09:50: Emir Toplama 09:30-09:45, Açılış
Fiyatının Belirlenmesi ve Açılış İşlemleri 09:45-09:50; Sürekli Müzayede
09:50-12:30); 2. Seans 14:00-17:30 (Açılış Seansı 14:00-14:20: Emir Toplama
14:00-14:15, Açılış Fiyatının Belirlenmesi 14:15-14:20; Sürekli Müzayede
14:20-17:30). The 2011 page prints the same bounds with method detail added.

## equities/tadawul/normal-week/

| Capture (UTC) | File | Original URL | sha256 |
|---|---|---|---|
| `20100112091155` | `tadawul_tradingtimes_ar.wayback-20100112091155id_.html` | `http://www.tadawul.com.sa/static/pages/ar/TradingTimes/tradingtimes.html` | `8d5a8681b99bad99873fec880bb97e4d70528d6c1bb9b7d756d638fcf4b44262` |
| `20110429234359` | `tadawul_tradingtimes.wayback-20110429id_.html` | `http://www.tadawul.com.sa/static/pages/en/TradingTimes/tradingtimes.html` | `d4bf474d42d80e8b2de33be783e834f9357cef7550162bdabcb9fb2ba0c578de` |

Arabic 2010 page: "أوقات التداول للسوق المالية السعودية (تداول) هي: من السبت
إلى الأربعاء فترة واحدة فقط من الساعة 11:00 صباحاً إلى الساعة 03:30 عصراً" —
Saturday to Wednesday, one session, 11:00 a.m. to 3:30 p.m. English 2011 page:
"Trading Days: One session, Saturday through Wednesday except official
holidays. Trading in Equities and ETFs: 11:00 am - 03:30 pm. Trading in Sukuk &
Bonds: 11:30 am - 03:30 pm." English-page CDX captures: 2007-2008 (2 KB
earlier-site states), `20110429234359`, `20110703101441`, `20110903170945`,
then `20140603012846` (post-change).

## equities/asx/normal-week/

| Capture (UTC) | File | Original URL | sha256 |
|---|---|---|---|
| `20130916140725` | `asx_trading_hours.wayback-20130916140725id_.html` | `http://www.asx.com.au/about/trading-hours.htm` | `a02cbf558a9519dd467afabc94189362a71404c55442421ba76231498354ca34` |
| `20160120000651` | `asx_trading_hours.wayback-20160120000651id_.html` | same URL — last capture (40 captures 2013-09-16..2016-01-20) | `6e260285e884be0068d85e8db60d3d3a19358fe3efbf19f1ba172263a500c4d6` |
| `20201022120436` | `asx_cash_market_trading_hours.wayback-20201022120436id_.html` | `https://www2.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours` | `c12675d67c4615b7565b94566c31227e59ab55289137ea0971dfc063f73631e8` |

All three print the same pre-SR15 cash-market timetable: Pre-opening 7:00 am;
Opening Phase in five groups (10:00:00 / 10:02:15 / 10:04:30 / 10:06:45 /
10:09:00 am, each +/- 15 secs — "group 1 may open at any time between 9:59:45
am and 10:00:15 am"); Normal Trading 10:00 am to 4:00 pm; Pre-CSPA 4:00-4:10
pm; CSPA 4:10-4:11 pm (*Random + 60 secs; the 2013/2016 page prints the same
envelope as "4:10pm - 4:12pm"); Adjust from 4:12 pm.

## equities/nzx/normal-week/

| Capture (UTC) | File | Original URL | sha256 |
|---|---|---|---|
| `20091204184203` | `nzx_key_dates_trading_hours.wayback-20091204184203id_.html` | `http://www.nzx.com/markets/key-dates/trading-hours` | `f5a8c3f622dbcf6adf8c48f688988e8392ef0542d8a56ac54e29d63f5b033b54` |

Corroboration only (pre-floor): the same grid the 2010-01-05 capture prints.
The in-interval artifact is the store's existing `NZX-KD-2010-01-05`
(`../2010-2024/wb_20100105003154_key_dates_trading_hours.html`,
`c01569901faa64d89de1ecb5e4f1ab319d3ad7ee13735389989e8813e5da0294`).

## equities/nyse/normal-week/

| Capture / retrieval (UTC) | File | Original URL | sha256 |
|---|---|---|---|
| `20120812235441` | `nyse_historical_trading_hours.wayback-20120812235441id_.pdf` | `http://www.nyse.com/pdfs/historical_trading_hours.pdf` ("NYSE ARCHIVES — HISTORICAL NOTE", "As of January 26, 2005") | `a6a2c630a28f57b89bb3063d85ac82108fe8c2c92c906bd1c2cae31e339ff4e5` |
| retrieved 2026-09-30 | `FR_2014_05_06_2014-10288.txt` | `https://www.federalregister.gov/documents/full_text/text/2014/05/06/2014-10288.txt` | `e13f9c062ebdbdc3450df45c166f839ca44a3b06e7c5ded1ffaf501f7d4841fd` |
| retrieved 2026-09-30 | `FR_2014_07_11_2014-16191.txt` | `https://www.federalregister.gov/documents/full_text/text/2014/07/11/2014-16191.txt` | `09c7d00d6058c76921e73b0e98141f46135fb00994ad29af86f93dfd49a4c561` |
| retrieved 2026-09-30 | `FR_2015_09_09_2015-22603.txt` | `https://www.federalregister.gov/documents/full_text/text/2015/09/09/2015-22603.txt` | `ae8a260edadc86e89c08ced442805fbd290ca945d29a1d2b62d2dcaec8088364` |
| retrieved 2026-09-30 | `FR_2017_08_09_2017-16742.txt` | `https://www.federalregister.gov/documents/full_text/text/2017/08/09/2017-16742.txt` | `2ccdeebb3325915685473a09eaac321cdb141537fecddd599a0b0c0c4672e21f` |
| `20140822120652` | `nyse_hours_calendars.wayback-20140822.html` | `https://www.nyse.com/markets/hours-calendars` — JS shell, keys no row | `66574b928a7fdd11565a07a55c88905c256661c2da3b38273d52debea95a1445` |

The historical note's trading-hours timeline: Sept. 30, 1985 — "9:30 a.m. – 4
p.m."; June 13, 1991 — "Regular trading, 9:30 a.m. – 4 p.m."; June 15, 2004 —
"Regular trading remained unchanged, 9:30 a.m. – 4 p.m."; header "As of January
26, 2005". URL-specific CDX also holds 30 captures 2004-12-09..2007-03-16 of
the same PDF. The FR texts are NYSE LLC's own SEC-filing statements of Rule 51 /
the trading session (quotations in the evidence file).

## nyse-nasdaq/nasdaq/normal-week/

| Capture (UTC) | File | Original URL | sha256 |
|---|---|---|---|
| `20100101193510` | `nasdaq_sys_hours.wayback-20100101193510id_.pdf` | `http://nasdaqtrader.com/content/TechnicalSupport/nasdaq_sys_hours.pdf` | `57a5d35d99f03690814c2c74157fc5a2b2417b964e03cd3a1adae2803f4d8c81` |
| `20101230180554` | `nasdaq_sys_hours.wayback-20101230180554id_.pdf` | `http://ftp.nasdaqtrader.com/content/TechnicalSupport/nasdaq_sys_hours.pdf` | `062e5fda19370bdf65abc22f2de32147df8b68566c4888355fcfa10cd5d80799` |

Both print, for THE NASDAQ STOCK MARKET: "Support Hours: 7:00 a.m. – 8:00 p.m.;
Market Hours: 9:30 a.m. – 4:00 p.m." (© 2010 The NASDAQ OMX Group; doc code
Q10-0079 for the December edition). Both digests reproduce their exact
`id_` replays at the named captures. The 07:00-20:00 window is labelled **support**
hours — the support desk, not a trading session — so neither PDF states the
pre-market trading open and neither keys a horizon move. Negative results,
2026-09-30 UTC: no Wayback capture of the nasdaqtrader TradingHours page in
2010-2013; no capture of `TraderNews.aspx?id=ETA2013-21`; EDGAR full-text and
Federal Register exact-phrase searches for the pre-2013 07:00 System-Hours open
returned nothing admissible.

## equities/euronext_paris/normal-week/

| Capture (UTC) | File | Original URL | sha256 |
|---|---|---|---|
| `20181111124550` | `calendar_of_cash_business_days_15_oct_2009.wayback-20181111124550id_.pdf` | `https://www.euronext.com/sites/www.euronext.com/files/calendar_of_cash_business_days_15_oct_2009.pdf` | `0cc923a604d6e263348d77b88953dce05cd885f91bbd692dbf7933b9a83229cb` |

The operator's Calendar of Cash Business Days 2010 (notice
`PAR_20091015_05039_EUR`, dated 15/10/2009) — the earliest 2010-scope Euronext
document, previously believed uncaptured. It states the 2010 closures and the
eves' 2:00 p.m. CET close but prints no weekday timetable, so the horizon
closing condition stands.
