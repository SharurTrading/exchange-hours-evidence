# Channel `66-2016-notice` — hunting the DAY of the 2016 SGX equity-index hours revision

Issue #66. The move from the 02:00-close grid (portal capture 20130820090335) to the 04:45-close
grid (portal capture 20170705000242) is undated. SGX's own Derivatives Products Description change
log brackets it into 2016 without a day. This channel hunts an **SGX-authored artifact that states
the effective DAY**.

All retrievals 2026-09-06 (UTC timestamps are in the file names). `fetch.sh` / `cdx.sh` are the
retry-with-backoff helpers used throughout (Wayback was intermittently 500/504-ing).

**RESULT: NARROWS, does not close.** No SGX-authored, publicly reachable artifact states the day.
Two new SGX-authored artifacts narrow the bracket and one new member-mirror channel is identified.
Broker material (inadmissible for a row) independently names two days — 11 July 2016 and
14 November 2016 — and names the SGX documents that would carry them.

---

## 1. SGX-AUTHORED ARTIFACTS RETRIEVED (admissible)

### 1.1 `MIRROR-kgi-LIVE-20260906T035953Z-SGXDerivativesTradingCalendar2016_AUG.pdf` — 811,805 bytes
**SGX Derivatives Market — TRADING CALENDAR 2016.** Verbatim SGX document (SGX cover, SGX
copyright boilerplate, "Singapore Exchange … 2 Shenton Way #02-02 SGX Centre 1 Singapore 068804"),
hosted on the site of **KGI Futures (Singapore) Pte Ltd**, an SGX-DT Trading and Clearing Member.

* URL (LIVE, fetched 2026-09-06 04:00 UTC): `https://www.kgieworld.sg/docs/SGXDerivativesTradingCalendar2016_AUG.pdf`
* HTTP `last-modified: Sat, 30 Sep 2017 13:16:48 GMT` (see `kgi_cal2016_headers.txt`)
* PDF `/CreationDate (D:20160831175512+08'00')`, `/ModDate (D:20160831175519+08'00')`,
  `/Creator (Adobe InDesign CC 2015 (Macintosh))`
* **The document's own as-of statement, verbatim:** "All dates and information are accurate as of
  24 December 2015."
* Not in the Wayback Machine (per `cdx_kgi_docs.json`, 32 rows for `kgieworld.sg/docs/`, none is
  this file); it is served live.

Page "Trading Hours of SGX Futures and Options Contracts", verbatim rows (T SESSION # / T+1 SESSION #):

```
SGX Nikkei 225 Index Futures                            7.45am to 2.25pm    3.15pm to 2.00am
SGX Mini Nikkei 225 Index Futures                       7.45am to 3.25pm    4.15pm to 2.00am
SGX USD Nikkei 225 Index Futures                        7.45am to 2.25pm    3.15pm to 2.00am
SGX Nikkei 225 Index Options                            7.45am to 2.30pm    3.15pm to 2.00am
SGX Nikkei Stock Average Dividend Point Index Futures   7.45am to 5.55pm    6.45pm to 2.00am
SGX FTSE China A50 Index Futures                        9.00am to 3.55pm    4.40pm to 2.00am
SGX MSCI Singapore Index Futures                        8.30am to 5.10pm    6.15pm to 2.00am
SGX MSCI Singapore Index Options                        8.30am to 5.15pm    6.15pm to 2.00am
SGX Straits Times Index Futures                         8.30am to 5.10pm    6.15pm to 2.00am
SGX MSCI Taiwan Index Futures                           8.45am to 1.45pm    2.35pm to 2.00am
SGX MSCI Taiwan Index Options                           8.45am to 1.50pm    2.35pm to 2.00am
```

and the same footnote the later editions carry, verbatim:

```
# Timings exclude pre-opening and pre-closing routines, the respective non-cancel periods as well
  as the respective order-cancellation session states where applicable. For detailed timings, visit
  sgx.com/derivativestradingcalendar
```

**Bearing.** This is state **S0** exactly as the 2013-08-20 portal page states it, now carried on an
SGX document whose own accuracy date is **24 December 2015** — two years and four months later than
the previous latest S0 witness. It also contains a "Calendar 2017" look-ahead page, i.e. it is the
edition SGX was still publishing into 2017 (KGI's own calendar page still linked it on 2017-01-26,
capture `20170126110327`).

**Caveat that must travel with it.** The file was *generated* 2016-08-31 but declares its content
accurate as of 2015-12-24, and broker material below attests that the Nikkei T open had already
moved to 7.30am on 11 July 2016. So this artifact may be read **only at its own as-of date**, never
at its creation date — a second worked instance of "a capture (or creation) date dates the
observation, never the state".

### 1.2 `LIVE-20260906T035456Z-contentapi-page-titan-dt-dc-portal.json` — 56,028 bytes
SGX's own content API payload for the **Titan DT/DC Portal** page, i.e. the public document index.

* `https://api2.sgx.com/content-api/?queryId=09434be8973b96b28894aefc57aff9e6c1f8f9c6:page&variables=%7B%22path%22%3A%22%2Ftitan-dt-dc-portal%22%2C%22lang%22%3A%22EN%22%7D`
* Parsed to `titan_portal_document_index.tsv` (143 rows: title, version, release date, URL).

The 2016 rows, verbatim (title / version / release date):

```
Titan DTDC Newsletter - Self Trade Prevention and Mass Quote Protection        1.0   18 Jul 2016
Titan DTDC Newsletter - Extended Trading Hours, Price Limits and Trade at Settlement   1.0   27 Jul 2016
Titan DTDC Newsletter - Combo Leg Pricing                                      1.0   10 Aug 2016
Titan DTDC Newsletter - ITCH and OUCH protocol                                 1.0   30 Aug 2016
Titan DTDC Newsletter - Important Updates                                      1.0   06 Oct 2016
Titan DTDC Newsletter - Technical Bulletin                                     1.0   14 Oct 2016
Titan DTDC Newsletter - Important Updates to Go-Live Date                      1.0   21 Oct 2016
Titan DTDC Newsletter - Key Information for Clearing Members                   1.0   21 Oct 2016
Titan Members Engagement #5 - Technical Briefing 2 - 27 Jan 2016                1.0   27 Jan 2016
Titan Members Engagement #6 - Market Access & Migration - 14 Mar 2016           1.0   14 Mar 2016
Titan Members Engagement #7 - Preparation for IWT - 21 Jul 2016                 1.0   21 Jul 2016
Titan Members Engagement #8 - Go-Live Briefing - 21 Sep 2016                    1.0   21 Sep 2016
Titan Members Engagement #9 - Go-Live Updates - 26 Oct 2016                     1.0   26 Oct 2016
```

**Bearing.** SGX's own index dates a member communication titled **"Extended Trading Hours, Price
Limits and Trade at Settlement" to 27 July 2016**, inside the change log's 2016 bracket. Under
LAW-PUBLIC-SOURCES its *existence and publication date* may be cited as evidence that a change
occurred; its contents are not a data source (see 1.3).

### 1.3 The four 2016 Titan PDFs — downloaded, encrypted, empty-password check FAILS
`LIVE-20260906T035527Z-titan-newsletter-ExtendedTradingHours-27Jul2016.pdf` (111,272 B)
`LIVE-20260906T035527Z-titan-members-engagement-7-IWT-21Jul2016.pdf` (199,720 B)
`LIVE-20260906T035527Z-titan-members-engagement-8-golive-briefing-21Sep2016.pdf` (793,558 B)
`LIVE-20260906T035527Z-titan-members-engagement-9-golive-updates-26Oct2016.pdf` (132,057 B)

All four: `%PDF-1.3`, `/Encrypt`, `/V 2 /R 4 /Length 128 /CFM /V2 /P -1028`, `/EncryptMetadata true`
(RC4-128, user password). `pdftotext <file> -` returns, verbatim:

```
Command Line Error: Incorrect password
```

on every one. **Empty-password check done, no further attempt made.** These are out of scope as a
data source under LAW-PUBLIC-SOURCES.

### 1.4 `WB-20170617052619-titan-dtdc-home.html` — 38,751 bytes
SGX's own **Titan DTDC Members Portal** page as it stood on 17 June 2017 — public, no login.
`https://web.archive.org/web/20170617052619id_/https://www.sgx.com/wps/portal/titan-dtdc/home/dt-home/`

It lists the same 2016 newsletters under their then-titles ("Titan DTDC Newsletter - New Feature
Overview 2 | 1.0 | 27 Jul 2016" is today's "Extended Trading Hours, Price Limits and Trade at
Settlement"), and it links **"SGX Derivatives Product Catalogue - Updated 1 June 2017 | 2.8 |
01 Jun 2017"** at
`/wps/wcm/connect/7e185e25-0256-440f-8fac-2532be2074af/Derivatives+Products+Description+Final+v2.8.xlsm`.
Every one of the 65 `wps/wcm/connect/...` document URLs on that page is extracted to
`titan_doc_urls.txt`; `titan_doc_cdx.txt` / `titan_doc_cdx2.txt` record the per-URL Wayback CDX
result (67 URLs checked; 22 returned `[]`, 42 timed out at a 20 s budget, 1 — a stylesheet,
`SGX_WCM_20090517a.css` — is archived). `titan_doc_cdx3_key.txt` re-runs the six that matter at a
100 s budget and **all six return `[]`**: the 27-Jul-2016 newsletter (`New Feature Overview 2`),
`Derivatives+Products+Description+Final+v2.8.xlsm`, Members Engagement #7/#8/#9 and the
`Titan-DTDC Environment Document 16112016 V3.3`. All of them return the 14,850-byte modern SPA
shell live. So no
pre-2020 edition of the product catalogue — the workbook whose contracts_data sheet would carry the
2016 hours against the change log's own v1.1 / v1.2 issue dates — is reachable.

### 1.5 `rulebook_ftr.html` — 1,220,771 bytes
SGX Futures Trading Rules, live 2026-09-06, `https://rulebook.sgx.com/rulebook/futures-trading-rules`.
**30 occurrences of "14 November 2016"** as an "Amended on" / "Added on" annotation — SGX's own
rulebook records a market-wide cutover that day (the amendments replace QUEST-era wording with
"the Trading System": e.g. Rule 2.10.2, 3.3.25, 3.4.8, 4.1.9, 4.1.10, 4.1.23, Regulatory Notice
4.1.6). **None of them is Rule 4.1.5 (Trading Hours, Opening and Closing Routines and Closing
Range)** — consistent with `2026-09-06-rulebook-channel-ruled-out.md`: hours are delegated to the
Contract Specifications and are structurally incapable of appearing as a rule amendment. The
rulebook therefore dates the *system* cutover to 14 November 2016 and says nothing about hours.

### 1.6 `MIRROR-kgi-LIVE-20260906T042954Z-Circular-DTAM-103-of-2020.pdf` — 466,929 bytes
Retrieved only to establish the channel. `https://www.kgieworld.sg/futures/resources/ck/files/docs/Circular%20DTAM%20103%20of%202020-%20Launch%20of%20SGX%20FTSE%20Equity%20Index%20Futures.pdf`
First lines, verbatim:

```
Circular
9 November2020
Circular No. DT/AM – 103 of 2020
Launch of SGX FTSE Equity Index Futures
The Exchange is pleased to announce that it will launch the following SGX FTSE Equity Index Futures
contracts ("Contracts") on SGX Titan DT on Monday, 23 November 2020.
```

**Bearing.** `kgieworld.sg` is a **third verbatim SGX-circular member mirror**, alongside CITIC
(DT/AM 15 of 2025) and Fubon (DT/AM 50 of 2024) — worth adding to `docs/schedules/sources.md`'s
channel-limit note. It hosts SGX-letterheaded circulars at
`/futures/resources/ck/files/docs/` and verbatim SGX calendars at `/docs/`. It does **not** hold a
2016 circular (§3).

---

## 2. BROKER MATERIAL — NAMES THE DAYS, INADMISSIBLE FOR A ROW
Recorded because it identifies exactly which SGX documents would close #66.

### 2.1 `MIRROR-phillip-WB-20170517064304-ann.html` (and `…-20160821061930-…`)
Phillip Futures Pte Ltd announcement, page-dated **"Friday, 1 July 2016"**, headed
"Change Of Trading Hours For SGX Nikkei Derivatives On 11 July 2016". Body verbatim:

```
With effect from 11 July 2016, the opening of the T session of the following SGX Nikkei derivatives
will be brought forward to 7.30am from the current 7.45am (Singapore time):
SGX Yen Nikkei 225 Index Futures (NK)
SGX USD Nikkei 225 Index Futures (NU)
SGX Options on Yen-denominated Nikkei 225 Index Futures (NKO)
SGX Mini Nikkei 225 Index Futures (NS)
For the updated trading hours, you may click here to refer to the respective exchange website.
```
(The "here" link is `http://www.sgx.com/` — no document.)
`https://web.archive.org/web/20170517064304id_/http://www.phillipfutures.com.sg:80/investors/support/announcements/387-change-of-trading-hours-for-sgx-nikkei-derivatives-on-11-july-2016`

### 2.2 `MIRROR-phillip-WB-20170131160819-list.html`
Phillip Futures announcements listing, capture 2017-01-31. Two items, verbatim:

```
Launch of Titan DT/DC, SGX's New Derivatives Trading & Clearing Platform
Friday, 11 November 2016
SGX will be launching a new derivatives trading and clearing platform on Monday, 14 November 2016.
This new platform will replace QUEST and SGXClear.
```
```
Key Changes to SGX Trading hours and Price Limit Following SGX Titan Launch
Wednesday, 16 November 2016
Do note that with the launch of Titan DTDC, SGX has made key changes to the trading hours and price
limits of several key contracts. Please click here to view the changes.
```
The "here" is Phillip's own `http://www.phillipfutures.com.sg/downloads/data/Titan%20Launch%20-%20Key%20Changes.pdf`
— zero Wayback captures, domain now NXDOMAIN.
`https://web.archive.org/web/20170131160819id_/http://www.phillipfutures.com.sg:80/investors/support/announcements?start=10`

### 2.3 `MIRROR-kgi-WB-20170504204711-blog600-revision-trading-hours-14nov2016.html`
KGI Futures (Singapore) news item, title verbatim
**"Revision of the trading hours for SGX derivatives contracts with effect from 14 November 2016"**.
Body verbatim:

```
Kindly note that with the launch of SGX's Titan DT/DC1, the trading hours for SGX derivatives
contracts’ will be revised with effect from 14 November 2016.
Click here for the list of contracts and their revised trading hours.
```
```
With reference to SGX Circular no. DT/AM – 76 of 2016 dated 24 October 2016, selected SGX-DT
contracts will be open for trading in the T and T+1 sessions on all onshore public holidays except
for New Years’ Day holiday in lieu on 2 January 2017 (unless otherwise specified).
```
`https://web.archive.org/web/20170504204711id_/http://www.kgieworld.sg:80/en/news-events/blog-2/item/600-revision-of-the-trading-hours-for-sgx-derivatives-contracts-with-effect-from-14-november-2016`

**The first "Click here" resolves to `/images/EDMimages/DTAM80of2016TradingCalendarAppendix1v07.pdf`**
— i.e. KGI is pointing at **Appendix 1 of SGX Circular DT/AM 80 of 2016** as "the list of contracts
and their revised trading hours". That is the same file SGX itself linked from its own portal page
(`/wps/wcm/connect/620b6dca-1cb5-4102-92b3-2b1bfcd97f16/DTAM+80+of+2016+Trading+Calendar_Appendix+1_v07_AK+%281%29.pdf`).
**Both copies are gone** (§3.3). *That file is the artifact that would close #66.*

---

## 3. HARD NEGATIVES — verified this session, not assumed

### 3.1 2016 is still a hole on SGX's own hours pages, re-verified with a wider net
`cdx_wps_2016_to_apr2017.json` — every `www.sgx.com/wps/` URL captured 2016-01-01 → 2017-04-30,
collapse=urlkey: **316 URLs in sixteen months**. Filtering for trading/derivatives/hours/calendar
leaves 17, and the only hours-shaped one is
`20160128081756 http://www.sgx.com/wps/portal/marketplace/mp-en/trading_on_sgx/derivatives_market/derivatives_trading_hours_and_calendar`.
Retrieved as `WB-20160128081756-marketplace-deriv-hours-calendar.html` (153,119 B): it is a
**navigation shell only** — zero occurrences of "Nikkei", "A50", "MSCI", "2.00am", "4.45",
"Trading Hours*"; its only content links are back to the two `trading_hours_calendar` portal pages.

`cdx_deriv_alltime.json` (in `../portal-hours-page/`) and `cdx_sgxwebch_trading.json` confirm the
English portal page jumps 2013-08-20 → 2017-09-27 and the **Chinese `sgxweb_ch` tree was crawled
only on 2017-07-04/05**. The `mp_en` WCM `Trading+Hours` leaf has exactly one content-bearing
capture, 2018-07-11. `cdx_wcm_connect_hours_all.json` enumerates every archived
`www.sgx.com/wps/wcm/connect/...` URL matching hours / trading_on_sgx / derivatives_market
(46 rows, all-time): the `mp_ch` tree exists but only for 2009 securities pages; **no derivatives
hours page in any tree for any date in 2016**.

`WB-20170314234738-portal-derivatives-at-a-glance.html` (a March-2017 SGX "Derivatives › At a
Glance" page found in the same sweep) carries no hours table — checked, zero "am to" strings.

### 3.2 No SGX 2016 news release on trading hours
`cdx_newsreleases_all.json` — 412 unique URLs under
`www.sgx.com/wps/wcm/connect/sgx_en/home/higlights/news_releases/`, all time. Nothing on Titan
go-live or trading hours; the only Titan-adjacent item is
`sgxs-next-generation-derivatives-trading-and-clearing-platform-to-use-nasdaq-technology`
(the 2013 vendor-selection release). SGX's home page captures of 2016-10-24 and 2016-11-01
(`WB-20161024022918-sgxpage.html`, `WB-20161101015423-sgxpage.html`) mention "Titan DT & DC" only
as a login-menu entry.

### 3.3 Every `wps/wcm/connect/…` document is dead live and unarchived
Tested live + per-URL CDX (`b8lh74lxu` transcript; all `[]`, all live responses the 11,792/14,850-byte
SPA shell):
* `…/bce57650-845d-4680-b286-691d46e4efa1/SGX+Derivatives+Trading+Calendar+2016_Oct+end+Update_FA.PDF`
* `…/5da48629-63a4-41ee-8fa9-b208bfdfe961/SGX+Derivatives+Trading+Calendar+2015_Aug+Update_FA.PDF`
* `…/e036cd33-309f-4dec-b753-3a18ac6aeaf9/SGX+Derivatives+Trading+Calendar+2014+-+Oct+2014+update_D1.pdf`
* `…/9e0bc7d0-1c90-4a39-a5db-c2e2c08ca7f0/DTAM+80+of+2016+Year+End+Trading+Schedule_v06.pdf`
* `…/620b6dca-1cb5-4102-92b3-2b1bfcd97f16/DTAM+80+of+2016+Trading+Calendar_Appendix+1_v07_AK+%281%29.pdf`
* `…/71c3c9b6-5b50-48b7-8a6b-fb690486e743/DTAM+80+of+2016+Trading+Calendar_Appendix+2_v07_AK.pdf`
* `…/1b90517a-09f3-4af2-a1cc-1501d6725a8c/DTAM+85+of+2016+Full+Year+Calendar_2017_v05.pdf`
* `…/05a51d36-0cc1-4eaa-aba4-bfddd7a14866/DTAM+85+of+2016+Full+year+calendar_Appendix+1_v05.pdf`
* the whole Titan document set including `Derivatives+Products+Description+Final+v2.8.xlsm` (§1.4)

KGI's own mirror of the two DT/AM 80 appendices
(`https://www.kgieworld.sg/images/EDMimages/DTAM80of2016TradingCalendarAppendix{1,2}v07.pdf`)
is **404 live and has zero Wayback captures** (checked under `www.`, bare and `:80` forms).

Guessed api2 paths for the 2016 Oct-end calendar, the 2017 calendar, DT/AM 80/85 of 2016 and
catalogue v1.2 all return **404** (`https://api2.sgx.com/sites/default/files/<YYYY-MM>/…`).
`https://api2.sgx.com/sites/default/files/2018-12/` is not listable (404).

### 3.4 Other channels closed
* **regco.sgx.com/circulars** — `regco_circulars.html`: the SPA's `CIRCULARS_API_URL` /
  `V1_PROSPECTUS_CIRCULARS_DATA_URL` serve **prospectus and offer circulars for listed issuers**
  (links.sgx.com), not DT/AM member circulars. The `page` query for `/circulars` on the content API
  returns `{"data":{"route":null}}`.
* **SGX content API `media_centre_list`** is not served by the current CMS version
  (`{"errors":[{"message":"The persisted query loader must return query string …"}]}`);
  `market_updates_list` works and was pulled in full
  (`LIVE-20260906T035852Z-contentapi-market_updates_list.json`, 1,743 items) — its **earliest item is
  2017-03-16**, so the market-updates channel does not reach 2016 at all.
* **CFTC FBOT docket for SGX-DT** (`cftc.gov/IndustryOversight/IndustryFilings/ForeignBoardsofTrade/23713`)
  — Order of Registration 2015-01-22; **no 2016 filings**.
* **Fubon Futures bulletin archive** — `cdx_fubon_bulletin.json`: 14 rows, 12 PDFs, earliest 2020.
  The 2016 bulletins are not archived and the live tree does not expose them.
* **kgieworld.sg** — `cdx_kgi_all.json` (20,000 rows, capped), `cdx_kgi_circulars.json` (130 rows),
  `cdx_kgi_docs.json`, `cdx_kgi_futuresdocs.json`, `cdx_kgi_edmimages.json` (empty),
  `cdx_kgi_news.json` (41 rows). The only 2016-hours item is the blog page of §2.3; the
  `/images/EDMimages/` directory is not archived at all.
* **phillipfutures.com.sg** — `cdx_phillip_ann.json` (57 announcement URLs),
  `cdx_phillip_downloads.json` (48). Items 350/352 (Titan) are listed but not archived as pages, and
  the Titan key-changes PDF is not archived.

### 3.5 The change log itself, re-read from the OOXML — still no day
`../catalogue/v17.6/…v17.6 eff 20260824, 20260907.xlsm`, sheet `read_me`, parsed cell by cell:

```
row 25  B=42419 (2016-02-19)  C=1    E=First Version
row 26  B=42482 (2016-04-22)  C=1.1  E=Added NLT MVT & NLT Tick / New Products updated /
                                       Equity Index & Dividend Index products T/T+1 gap increased to 15mins /
                                       Amendments to LTT, market code, session states / SOD to start from 6.15am
row 27  B=42566 (2016-07-15)  C=1.2  E=Amendments to NK suite, CH, CHO and CN trading hours / …
row 48  B=43013 (2017-10-05)  C=3.3  E=Change of Trading Hours / Amended Typo in FEF Carry/Non-Carry
```

Neither 2016 entry states an effective day; every later hours entry in the same sheet does
("(eff 10 Jun)", "Effective 11 Nov:", "(eff 4 Nov)", "(eff 7 Apr)"). The 2016 entries predate SGX's
adoption of the "(eff …)" convention, which first appears at row 53 (2018-03-06).

---

## 4. WHAT THIS DOES TO #66

* **No cutover row may be added.** No SGX-authored, publicly reachable document states the day, so
  the 2017-07-10 knowledge boundary on the Japan, China and Singapore keys **stands**, and the
  2016 bracket stays a bracket.
* **The bracket narrows on SGX-authored evidence alone**, from
  `(2013-08-20 portal capture, 2017-07-05 portal capture)` to
  `(2015-12-24, the 2016 calendar's own as-of date, 2017-07-05)` — with the change log's
  2016-04-22 and 2016-07-15 entries and the Titan newsletter of 2016-07-27 all inside it.
* **Residual risk (2) in `history.rs` is partly retired.** "The 2014-2016 calendar editions lived in
  a WCM store that is in neither the archive nor the live site, so states between S0 and A are
  unwitnessed" is no longer wholly true: the **2016 edition survives on a member mirror** and states
  S0 unchanged as of 24 December 2015. The 2014, 2015 and 2016-Oct-end editions remain unrecovered.
* **New channel for `docs/schedules/sources.md`:** `kgieworld.sg` — verbatim SGX-DT circulars at
  `/futures/resources/ck/files/docs/`, verbatim SGX calendars at `/docs/`.
* **Follow-ups to open (LAW-FOLLOW-UPS-ARE-ISSUES).** Two named SGX documents would close #66 and
  neither is currently reachable: **DT/AM 80 of 2016, Appendix 1** ("Trading Calendar Appendix 1
  v07"), which KGI itself describes as the list of contracts and their revised trading hours, and
  the **Titan DTDC newsletter of 27 July 2016**. A third, **DT/AM 76 of 2016 dated 24 October 2016**,
  is named by KGI and governs holiday-session scope (LAW-HOLIDAY-SCOPE, not this row). Broker
  material attests two days that are **not** admissible and must be recorded only as residual risk:
  Nikkei T open 07:45 → 07:30 on **Monday 11 July 2016** (Phillip Futures, 1 July 2016) and a
  market-wide hours revision at the Titan DT/DC launch on **Monday 14 November 2016** (KGI, and
  Phillip on 11 and 16 November 2016). If the first were ever SGX-sourced, the Japan key's floor row
  would split at 2016-07-11 (a daytime open, so the artifact's own date); if the second were, all
  three keys' 2017-07-10 knowledge boundaries would become a cutover keyed to Monday 2016-11-14
  (which lengthens a wrapping overnight close and is already a Monday).

---

## 5. FILE LIST

| file | what |
|---|---|
| `MIRROR-kgi-LIVE-20260906T035953Z-SGXDerivativesTradingCalendar2016_AUG.pdf` / `.layout.txt` | **SGX Derivatives Trading Calendar 2016** (verbatim, KGI mirror). §1.1 |
| `kgi_cal2016_headers.txt` | HTTP headers for the above |
| `LIVE-20260906T035456Z-contentapi-page-titan-dt-dc-portal.json` | SGX content-API payload, Titan DT/DC portal. §1.2 |
| `titan_portal_document_index.tsv` | parsed 143-row document index from the above |
| `LIVE-20260906T035527Z-titan-*.pdf` (4 files) | the four 2016 Titan PDFs — RC4-128 encrypted, empty password fails. §1.3 |
| `WB-20170617052619-titan-dtdc-home.html` | SGX Titan DTDC Members Portal, 2017-06-17. §1.4 |
| `titan_doc_urls.txt`, `titan_doc_cdx.txt`, `titan_doc_cdx2.txt`, `titan_doc_cdx3_key.txt` | the 65 Titan `wcm/connect` doc URLs and their CDX results (all empty bar a stylesheet; the six that matter re-checked at a 100 s budget) |
| `rulebook_ftr.html` | SGX Futures Trading Rules, live. 30 × "14 November 2016". §1.5 |
| `MIRROR-kgi-LIVE-20260906T042954Z-Circular-DTAM-103-of-2020.pdf` | channel exemplar: KGI hosts verbatim SGX circulars. §1.6 |
| `MIRROR-phillip-WB-20170517064304-ann.html`, `MIRROR-phillip-WB-20160821061930-ann.html` | Phillip, 11 July 2016 Nikkei T-open change. §2.1 |
| `MIRROR-phillip-WB-20170131160819-list.html`, `MIRROR-phillip-WB-20160823094211-list.html` | Phillip announcement listings incl. the two Titan items. §2.2 |
| `MIRROR-kgi-WB-20170504204711-blog600-revision-trading-hours-14nov2016.html` | KGI, "with effect from 14 November 2016". §2.3 |
| `MIRROR-kgi-WB-2016*/2017*/2018*-sgx-trading-calendar.html`, `MIRROR-kgi-WB-20160516043323-44-2016.html`, `MIRROR-kgi-LIVE-sgx-trading-calendar-page.html` | KGI calendar/news pages, showing which SGX calendar edition KGI linked when |
| `WB-20160128081756-marketplace-deriv-hours-calendar.html` | the only 2016 SGX hours-shaped capture — nav shell, no grid. §3.1 |
| `WB-20161024022918-sgxpage.html`, `WB-20161101015423-sgxpage.html`, `WB-20161022124114-sgxpage.html` | SGX home / newsflash, Oct-Nov 2016 — nothing on hours |
| `WB-20170314234738-portal-derivatives-at-a-glance.html` | SGX "Derivatives › At a Glance", Mar 2017 — no hours table |
| `LIVE-20260906T035852Z-contentapi-market_updates_list.json` | full SGX market-updates list, 1,743 items, earliest 2017-03-16 |
| `regco_circulars.html` | regco SPA shell — circulars route is prospectus/offer circulars |
| `cdx_*.json` | every CDX enumeration run, kept so the negatives are reproducible |
| `fetch.sh`, `cdx.sh` | retry-with-backoff helpers |
