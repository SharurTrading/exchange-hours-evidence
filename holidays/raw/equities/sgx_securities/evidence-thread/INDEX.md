# sgx_securities evidence thread — #213 (2010-2013 and 2020-2024 capture gaps)

Hunt pass: 2026-10-02 UTC. Evidence file: `docs/evidence/sgx_securities.md`.
Issue: SharurTrading/exchange-hours-rs#213.

## FINDING — a 2012 operator-page capture exists on archive.today (not fetchable from here)

**`https://archive.li/20120910023452/http://www.sgx.com/wps/portal/sgxweb/home/trading/securities/trading_hours_calendar`**

Proven to exist on 2026-10-02 UTC: `archive.ph/newest/<page-url>` 302-redirected
to that exact snapshot URL (existence proof does not require reading the
snapshot). Its timestamp **2012-09-10 falls inside the 2010-2013 gap**, and it
predates the wps path's first Wayback capture (2014-08-21) — i.e. it is the
only known capture of the securities trading-hours calendar page from the
server-rendered (pre-SPA) era.

**Not fetchable from this machine/session**: archive.today serves a reCAPTCHA
interstitial to this network (tried curl 429 + in-app browser twice). **A human
opening the link in a normal browser should retrieve it** (Ctrl+S / print to PDF)
and drop it beside this note. If its bytes carry the calendar (2012/2013
closures), the 2010-2013 span's second half keys directly; the 2010-2011 part
would still need an earlier artifact.

## Checked negatives this pass (2026-10-02 UTC)

- **links.sgx.com** (the operator's corporate-announcement PDF host):
  unfiltered CDX dump `url=links.sgx.com*&from=2019&to=2025&collapse=urlkey`
  returned 40 000 urlkeys (the query's limit — truncated) and **zero**
  matches for `calendar|holiday` in them
  (`cdx_links_sgx_all.txt` here). A filtered query 504s. An annual
  securities trading-schedule announcement on that host is not ruled out by
  the truncated dump, but none surfaced. Retriable when the CDX service is
  less loaded, page-by-page with `showResumeKey`.
- **`sgx.com/wps/wcm/connect/mp_en/site/trading_on_sgx/securities_market/*`**
  (the marketplace-portal predecessor tree) 2010-2013 CDX: **zero captures**
  (`cdx_sgx_mpen_securities_2010-2013.txt` here) — confirms the issue's
  statement at tree granularity rather than domain-wide guesswork.
- archive.today: no snapshots of `sgx.com/stock-exchange/trading`,
  `api2.sgx.com/content-api`, `www2.sgx.com/securities/trading-hours-calendar`
  (404s). The only snapshot ever found for the venue is the 2012-09-10 one
  above.
- Common Crawl domain queries for sgx.com 2013-2024 with
  `filter=url:.*(trading_hours|calendar|holiday).*`: pending in the
  background batch (CC index heavily 504-degraded 2026-10-02); to be
  appended.

## Channel notes for the next attempt

- The current page renders its content through
  `api2.sgx.com/content-api?queryId=dd24dd8e...&variables={"path":"/stock-exchange/trading","lang":"EN"}`
  (per the evidence file). The 2020-2024 content-API history is a Wayback-free
  zone; CC capture of the API URL is the only archive channel left to check
  (queued).
- The 2019-05-14 trade-at-close announcement PDF on links.sgx.com witnesses
  the announcement-PDF URL shape
  (`links.sgx.com/1.0.0/corporate-announcements/<HASH>/<date>_<title>.pdf`) —
  hash IDs are unguessable, so only enumeration can find a calendar
  announcement there.

## Common Crawl (2026-10-02, `cc-batch-2026-10-02.log` here)

Domain queries `sgx.com` with `filter=url:.*(trading_hours|calendar|holiday).*`
in CC-MAIN-2013-20, CC-MAIN-2013-48 and CC-MAIN-2020-34: **all zero
captures**. CC-MAIN-2022-05 failed after retries (gateway 504; the Internet
Archive entered a "Temporarily Offline" state ~02:45 UTC) — re-runnable,
covers the 2022 slice of the second gap.

## Second pass addendum (2026-10-02 ~17:20-17:55 UTC)

Raw artifacts of this pass: `retry-2026-10-02/` (SHA256SUMS inside).

1. **The 2012-09-10 archive.today snapshot — completed negative from this
   network.** All four mirrors (`archive.li`, `archive.ph`, `archive.vn`,
   `archive.is`) 302-redirect `/newest/` for the wps securities
   trading-hours calendar URL to the same `20120910023452` snapshot
   (existence re-proven this pass), and every mirror serves the same reCAPTCHA
   interstitial (HTTP 429, ~59 KB "One more step" page) to this datacenter
   network. Tried beyond last pass: full browser-grade header set
   (Accept/Sec-Fetch/Referer=google), a delayed single-shot retry, and a
   mobile iOS Safari UA — all identical captcha pages
   (`at_*.html` here are the interstitials). Per the hunt charter the captcha
   was not circumvented; **a human browser is still the only known reader**
   of the only pre-SPA capture of this page.
2. **links.sgx.com — now a COMPLETE negative.** The unfiltered CDX
   enumeration was re-run to exhaustion with pagination (`showResumeKey`,
   5 000 rows/page, 47 pages, **231 640 urlkeys, 2010-2025** — 5.8x last
   pass's 40 000-row truncated dump): `cdx_links_sgx_full_2026-10-02.txt.gz`
   (+ per-page tar) here. Grep across every urlkey for
   calendar/holiday/trading-hours/trading-schedule/market-hours/half-day/
   clearing-calendar: the only hits are **issuer** announcements (MBL/SG
   Issuer HK/JP public-holiday notices, a company-holidays notice, an AGM
   scheduling note, a shipyard half-day halt) — none is an SGX operator
   trading-calendar artifact. The host's 148 182 `1.0.0/corporate-announcements`
   rows carry readable slugs in their urlkeys; none names a trading calendar.
   An annual SGX securities trading-schedule announcement does not survive on
   links.sgx.com in the archive.
3. **The wps securities page's pre-2014 absence, verified at row
   granularity** (`cdx_wps_sec_cal_2010-2016_full.txt.gz` here): uncollapsed
   CDX for the exact URL 2010-2016 returns exactly the three captures the
   crate already holds (2014-08-21, 2015-09-24, 2016-01-08). The issue's
   "no 2010-2013 capture survives" claim holds with no hidden revisit/dedup
   records.
4. **Common Crawl CC-MAIN-2022-05 re-run**: still 504-degraded at write time
   for both the exact wps URL and the `api2.sgx.com/content-api/*` prefix
   (`cc2022_wps_exact.json` holds the last error); retry loop left running.
   The 2013-20/2013-48/2020-34 zeros of last pass stand.

Net: no operator artifact surfaced this pass. The 2010-2013 and 2020-2024
spans remain gaps with unchanged closing conditions (a human-side retrieval
of the 2012-09-10 snapshot is the one concrete lead that would close half of
the first span if its bytes carry the calendar).

## Second-pass close-out (2026-10-02 ~18:10 UTC)

- **arquivo.pt** (independent Portuguese web archive, open API): zero captures
  of the wps securities trading_hours_calendar URL and zero text-search hits
  for trading_hours_calendar+sgx — checked live 2026-10-02 (no artifact
  saved; both responses were empty result sets).
- **Memento TimeTravel aggregator** (`timetravel.mementoweb.org`): host does
  not resolve from this network — unreachable, not a checked negative.
- **api2.sgx.com Wayback history**: the domain's captures are root health
  checks (text/plain 200, ~270-510 B, 2021-02..2026-01) and `.well-known`
  404s; the `/content-api` prefix row-granularity query could not complete
  before the Internet Archive re-entered its "Temporarily Offline" state
  (2026-10-02 ~17:55 UTC). The prior pass's single 2022-09-13 content-api
  capture (the 23-byte `{"data":{"route":null}}` shell, in
  `2020-2024-retry/`) remains the only known content-api record; the zone
  stays Wayback-free for 2020-2024 holiday content.
- **CC-MAIN-2022-05**: retry loop exhausted, 504-degraded throughout — same
  state as last pass. The CC index for pre-2023 collections has now been
  504-degraded across two hunt passes; treat any future re-run as a fresh
  attempt, not a completion.

Both named spans close only with new operator bytes: the 2012-09-10
archive.today snapshot (human browser) for 2010-2013's back half, and any
2020-2024 operator artifact if one ever surfaces. Search exhausted on every
channel reachable from here.

## Third addendum (2026-10-02 ~18:05-18:20 UTC) — the content-API archive, row-granularity characterized

The Internet Archive recovered at ~18:00 UTC and the `api2.sgx.com/content-api*`
CDX prefix query completed: **1 291 rows, 2020-01..2026-07**
(`cdx_api2_contentapi_all.txt` here; sha256 in SHA256SUMS.txt). This replaces
the issue's "the 2020-2024 content-API history is a Wayback-free zone"
characterization — the zone is far from empty, and its emptiness of holiday
content is now provable at row level:

- The API's captured traffic is health checks, navigation (`all_menus`,
  `page_tiles`), alerts, and derivatives product lists (the sgx-pre2020
  catalogue channel). No securities trading-hours or holiday query exists in
  the archive before 2026.
- Exactly two `page`-query captures exist for the trading-calendar family:
  path `/wps/portal/sgxweb/home/trading/securities/market` (2022-08-12) and
  path `/wps/portal/sgxweb/home/trading/securities/trading_hours_calendar`
  (2022-09-13, the row behind the known 23-byte file). **Both serve
  `{"data":{"route":null}}`** — fetched this pass
  (`wb_20220812183049_contentapi_wps-sec-market.json` here; the 2022-09-13
  file was already in `2020-2024-retry/`). The wps paths were already
  orphaned in the API when first captured; no capture exists from while they
  were live.
- The only large (40 KB+) page payloads are 2026-era (`/stock-exchange/trading`
  2026-07-25, `/securities/trading` 2026-02-24), matching the live-fetch era
  already audited.
- A 2021-11-23 `page_tiles` capture for `/securities/retail-investor` was
  fetched as the era's only non-menu page-content candidate: navigation
  tiles, no holiday/hours strings
  (`wb_20211123031006_contentapi_page_tiles.json` here).
- CC-MAIN-2022-05's `api2.sgx.com/content-api/*` query succeeded on the
  loop's last run: **"No Captures found"** — Common Crawl never crawled the
  content-API either (`cc2022_api2.json` here).

Net for #213: the 2020-2024 span now rests on a complete, named enumeration
of every operator API capture in both archives, plus the exhausted
links.sgx.com host and the row-granularity wps-page check above. Every
channel reachable without a human browser is exhausted; the archived API
history begins only after the calendar page had already moved behind
route:null.
