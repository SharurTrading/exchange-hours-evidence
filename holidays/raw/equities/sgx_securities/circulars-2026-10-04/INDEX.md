# sgx_securities hunt 4 — the circulars channel — 2026-10-04 UTC — completed negative

Fourth retrieval pass on #213 (the 2011-08-01..2013-12-31 and
2020-01-02..2024-12-31 holiday capture gaps), sweeping the channels the
brief names as untried: the SGX circulars/notices library URL patterns, the
archive.today mirror forms, and the Securities Market Statistics/fact-book
family. **No operator artifact printing either span's closures surfaced; no
rows encode; #213 stands with unchanged closing conditions.** Retrieval
instants 2026-10-04 02:22-02:44 UTC. Digests in `SHA256SUMS.txt`.

## Angle 1 — the circulars/notices library (complete enumeration, all negative)

Method: complete `collapse=urlkey` CDX enumerations of every URL family the
channel could live under, across the sgx.com domain (which covers every
subdomain: www, www2, info, infopub, links, api, api2, rulebook, css, res,
corp, onlineeducation, investorrelations) plus `sgx.com.sg`, in both gap
windows. Every dump saved whole.

1. **`circular` in the urlkey, all years** (`cdx_sgx_domain_circular_all.txt`,
   2 107 urlkeys): the 2011-2013 and 2020-2024 rows are exclusively **issuer**
   documents — `listprosp.nsf` prospectus circulars,
   `1.0.0/prospectus-circulars` pages, `api.sgx.com/circulars/v1.0`
   (the prospectus/offer-documents API, verified by its captured query
   parameters: `companyname=...`, `prospectustype=...`), and
   `FileOpen/*.ashx` shareholder circulars. No member circular, no trading
   schedule, no holiday announcement.
2. **`notice` in the urlkey** (`cdx_sgx_domain_notice_all.txt`, 6 757): AGM/EGM
   notices, book-closure notices, warrant expiry notices — all issuer. A
   grep across every urlkey for
   `holiday|trading hour|trading schedule|festive|christmas|new year|cny|lunar|vesak|deepavali|hari raya|good friday|labour day|national day`
   returns one operator row: the already-cited rulebook Regulatory Notice
   8.2.1. No member circular titles survive in any URL.
3. **`schedule`** (`cdx_sgx_schedule_2010-2014.txt`, 6 rows; `..._2019-2025.txt`,
   524): margin schedules, meeting schedules, REIT earnings schedules — no
   trading calendar.
4. **`regulation`, `singapore-exchange-regulation`, `regco`,
   `circulars_notices`** (`cdx_sgx_domain_regulation_all.txt` 790,
   `cdx_sgx_singexreg.txt` 6, `cdx_sgx_regco_circnotices.txt` 860): the
   regulation site families are SPA assets, public consultations and media
   releases. `regco.sgx.com`'s archive begins 2023 (564 urlkeys,
   `cdx_regco_sgx_all.txt`) and its content API
   (`api2.sgx.com/regco/content-api`, `cdx_api2_regco.txt`, 26 rows) serves
   menus/alerts/disciplinary pages — no circulars library and no holiday
   content.
5. **`rulebook.sgx.com` complete** (`cdx_rulebook_sgx_all.txt`, 27 935): the
   2011-2013 captures are rulebook display pages and rule PDFs (Mainboard,
   Catalist, DC, DT FTR appendix); the only `circular` URLs are rule chapters
   about issuer circular requirements. No member-circular library.
6. **`info.sgx.com` complete for 2010-2014** (`cdx_info_sgx_2010-2014.txt`,
   7 682): the Lotus-app host's captured apps are corporate announcements
   (`webcorannc*`), prospectuses (`listprosp`), listing manual (`SGXRuleb`),
   clearing (`SGXWeb_DC`, incl. a 404'd `Trading_Calendar_2003` node) and
   session-directory apps. `SGXWeb_ST.nsf`/`SGXWeb_DT.nsf` have one 404'd row
   each. No trading-calendar or circulars app captured.
7. **Holiday names in the urlkey** — the Eurex complete-enumeration pattern
   applied to filenames (`cdx_sgx_holidaynames_2010-2015.txt` 23 rows,
   `cdx_sgx_holidaynames_2019-2025.txt` 97 rows, filter
   `christmas|lunar|vesak|deepavali|raya|puasa|haji|festive|polling|good-friday|good_friday|cny`):
   issuer hash collisions, warrant tickers (`CNYW`), a Christmas wallpaper
   JPG, AGM polling results. No operator document named by a holiday.
8. **`sgx.com.sg`** (`cdx_sgxcomsg_circnotice.txt`, 2 rows): two 2001-2002 GIF
   navigations. Nothing.
9. **The marketplace-portal WCM tree is dead as a content channel.** The
   complete `mp_en/site/trading_on_sgx*` inventory
   (`cdx_wcm_mpen_trading_on_sgx_all.txt`, 31 urlkeys) shows the securities
   tree's last real content captures are May 2009 and the derivatives tree's
   are 2018-2025 — but the 2021/2025/2026 captures are the **current site's
   SPA catch-all serving 200 text/html for the old WCM URLs**, not WCM
   renders (`wb_20210925_mpen_dt_trading_hours.html`,
   `wb_20251211_mpen_dt_2008_schedule.html`,
   `wb_20260224_mpen_sec_trading_hours.html` — each carries the
   GTM/Akamai-boomerang/sgxembed shell markers and zero schedule content).
   A live probe of the 2009-known URL
   `wps/wcm/connect/mp_en/site/trading_on_sgx/securities_market/
   securities_trading_hours_and_calendar/2009+public+holidays`
   (`live_mpen_2009_public_holidays.html`) returns the same shell, so the
   per-year-children probe (`2010+public+holidays` … `2024+public+holidays`,
   both the `publicholidays` and `public+holidays` spellings) cannot
   distinguish existing from absent WCM nodes and was not tunnelled. This
   closes the route the late-capture rows had seemed to open.
10. **The operator's own sitemaps.** `www.sgx.com/sitemap.xml` captured
    2022-06-24 (`wb_20220624_sitemap.xml`, 489 914 bytes, 1 227 `<loc>`
    URLs): the complete site inventory inside the 2020-2024 window names
    **no securities trading-hours/holiday calendar page at any URL** — the
    closest pages are `/securities/trading` (SPA), `/derivatives/trading`,
    regulation memberships, prospectus circulars and the rulebook. The
    2020-08-06 `/sitemap` HTML page (`wb_20200806_sitemap.html`) is a
    browser-upgrade shell. This upgrades the 2020-2024 gap record: the
    operator's own mid-window enumeration proves the calendar page existed
    only as an SPA route whose data feed (`api2.sgx.com/content-api`) the
    archive already characterizes as route-null until 2026.

## Angle 2 — archive.today mirrors (the standing human-side item)

The exact snapshot named by the human item:
`https://archive.li/20120910023452/http://www.sgx.com/wps/portal/sgxweb/home/trading/securities/trading_hours_calendar`.
One attempt per mirror form, short timeout, browser UA, 2026-10-04 ~02:35 UTC:
`archive.ph`, `archive.is`, `archive.md`, `archive.li` — **all four 302 to
the `archive.li/20120910023452` snapshot URL and serve the identical
reCAPTCHA interstitial (HTTP 429, ~59 KB "One more step" page)**
(`at_archive_ph.html`, `at_archive_is.html`, `at_archive_md.html`,
`at_archive_li.html`). Existence re-proven; content still unreadable from
this network. The redirects converged on `archive.li` from every mirror
tried, including `archive.md`, which earlier passes had not tried. **The
human-side item stands unchanged.**

## Angle 3 — the Securities Market Statistics / fact-book family (one pass)

Complete `statistic|factbook|fact-book|fact_book` urlkey enumeration
(`cdx_sgx_statistics_factbook_all.txt`, transfer truncated by the CDX at 426
rows; re-run bounded 2011-2026, `cdx_sgx_statistics_2011-2026.txt`, 366 rows
— the two overlap completely in the gap years). The family is:

- **SGX Monthly Market Statistics Report / Monthly Statistics Report** PDFs
  under `api2.sgx.com/sites/default/files/` — the editions captured as
  `200 application/pdf` are: April 2020, June 2020, Sep 2020, Nov 2020 (two
  files), Dec 2020, Feb 2021, Mar 2021, Apr 2021, June 2021, July 2021, Aug
  2021, Sep 2021, Oct 2021, Nov 2021, Dec 2021, Jan 2022, Feb 2022, Mar
  2022, Apr 2022, May 2022, June 2022, July 2022, Aug 2022, Sep 2022, Oct
  2022, Nov 2022, Dec 2022, Jan 2023, Feb 2023, Mar 2023, Apr 2023, May
  2023, June 2023, Sep 2023, Oct 2023, Nov 2023, Dec 2023, Jan 2024, Feb
  2024 (2025-2026 editions exist but fall outside the gaps), plus two
  pre-gap editions (Dec 2018, Feb 2019) and a Jan 2020 file whose only
  capture is a 301. A May 2021 edition is absent from the archive. 2016-2019
  monthly-report news releases also appear, and
  `SGX+Monthly+Statistics+(April+2012).pdf` whose captures are all
  `200 text/html` — the SPA shell, not the PDF bytes; no pre-2015 edition
  survives as PDF.
- **Genre baseline, read in the window:** the December 2020 report
  (`mmsr_dec2020.pdf`, capture 20211027073834, 36 pages,
  `mmsr_dec2020.txt` is the pdftotext extraction) carries no market-holidays
  appendix — the only holiday-adjacent content is the
  `Number of Trading Days (Securities)` count. Trading-day counts state no
  closure in session language and key no row. The genre cannot print the
  spans' closures.

## Net

The circulars channel is a complete negative: every URL family the library
could have lived under is enumerated, and nothing operator-authored naming
either span's closures exists in the Wayback index, Common Crawl (prior
passes), the content APIs, the live WCM tree, or the operator's own sitemap.
The statistics/fact-book genre is negative on its premise. The archive.today
snapshot remains the one lead for the 2011-2013 span's back half and stays
with the maintainer. #213's closing conditions are unchanged; the research
store holds the complete dumps so any future re-check starts from this
enumeration rather than repeating it.
