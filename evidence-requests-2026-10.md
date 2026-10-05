# Evidence requests — consolidated ask-list for the maintainer's operator thread

Prepared 2026-10-01 UTC. Refreshed 2026-10-04 UTC after the 2026-10-03 merge
wave closed three issues as data and sharpened the rest — see the amendment
record at the foot. One section per issue; sections 1, 2 and 5 are **MOOT**
(their issues closed as data; the thread must not chase them) and the live asks
are sections 3, 4 and 6-13, grouped by desk: CME (6-9), Coinbase Derivatives
(10-11), SGX (4), SIX (3), Eurex (12), Xetra (13). Every ask is phrased so a
support desk can act on it directly. An artifact posted to the thread or saved
anywhere works — the crate only needs **the bytes plus a URL and a retrieval
date**; a verbatim copy and a live link that captures it are equally
admissible. What closes a gap is the operator's own statement (tier T1) or the
operator's own machine channel (tier T2); a restatement by a vendor or news
outlet cannot key a row. Each recovered artifact lands in the research store
under `holidays/raw/` in its venue directory with a sha256 and a UTC retrieval
date, and unlocks the crate rows/windows named in its section.

---

## 1. TSX / TMX Group — issue [#221](https://github.com/SharurTrading/exchange-hours-rs/issues/221) — MOOT, closed as data 2026-10-02/03

**Do not chase this on the thread.** All three spans the ask covered closed as
operator data while the list stood:

- **2013-08-19..2014-01-01 and 2014-07-02..2016-12-31** closed in PR #255
  (2026-10-02): the release series' verbatim CNW/PR Newswire wire mirrors
  (Labour Day 2013, Thanksgiving 2013, the 2013/2014/2015/2016 year-end Holiday
  Operating Schedules), the TMX Money complete-2014 "Market Hours & Holiday"
  page (served 2014-01-09) and the tsx.com Calendar & Events page (served
  2015-03-15, capture 20150315063450) printing the complete 2015 and 2016
  lists.
- **2011-10-11..2012-01-02** — the last span, exactly the document the old ask
  chased — closed in PR #262 (2026-10-03): `TMX-REL-2011-12-12`, TMX Group's
  own Holiday (Operating) Schedule release of 2011-12-12, recovered live from
  the Mondo Visione verbatim mirror (2011-12-26/27 and 2012-01-02 closed;
  2011-12-23 the regular close, so no eve row).

Issue closed 2026-10-03. Hunt record:
`holidays/raw/equities/tsx/evidence-thread/`.

---

## 2. LSE — issue [#218](https://github.com/SharurTrading/exchange-hours-rs/issues/218) — MOOT, closed as data 2026-10-02

**Do not chase this on the thread.** Both spans closed in PR #256 (2026-10-02):
the December 2015 service announcement `live001-03122015` (capture
20170916002832 — a document class the earlier URL-name greps could not see)
points at `www.lseg.com/businessdays`, the operator group's own Business days
page, whose 89 HTTP-200 captures run continuously 2013-10-04..2020-06-14; seventeen
`id_` replays of it tile **2015-01-02..2019-12-31** and **2020-01-01..2020-08-30**
(54 new rows, including the moved VE-Day holiday 2020-05-08 and the 12:30
London-time eve closes). The audited windows re-joined into one
`2010-01-01..2027-12-31` span.

Issue closed 2026-10-02. Hunt record:
`holidays/raw/equities/lse/evidence-thread/`.

*Residual, not the issue:* the five 2025 rolling-table dates (2025-04-18,
04-21, 05-05, 05-26, 08-25) remain `Unsourced` — a business-days export dated
inside 2025-01-02..2025-12-17 would source them. The 2026-09-29 bounded search
closed negative on every channel; the rows await operator publication and ride
the same desk only if the thread happens to touch LSE.

---

## 3. SIX Swiss Exchange — issue [#212](https://github.com/SharurTrading/exchange-hours-rs/issues/212) — narrowed to 2010-2011

**Who to ask:** SIX Swiss Exchange client services / publications archive
(the team behind the download centre and the Trading Guide series on
six-group.com).

**What changed:** the 2018-2019 half closed as data on 2026-10-03 (PR #270) —
the operator's own live education-path Trading Guide of 28 May 2018 carries
"Trading Calendar 2018" and "Trading Calendar 2019" sections whose twelve month
grids, read cell by cell, shipped 24 `Closed` rows. The mechanism that closed
it is exactly what this ask names: a guide edition reprinting the year's grids.
**2010 and 2011** remain unaudited (730 refused dates).

**The dates the evidence must cover, exact:** calendar years **2010 and 2011**
only — the operator's own Trading Calendar for each year, i.e. the days on
which there is no trading on SIX Swiss Exchange.

**The exact ask:**

> Could you send me copies of the SIX Swiss Exchange Trading Calendar PDFs for
> 2010 and 2011 — the per-year "trading calendar" documents (e.g.
> `trading_calendar_2011.pdf`), or the Trading Guide edition of 11 January 2010
> (`trading_guide_2010_01_11_en.pdf` and its dated part editions — your own
> archived guides index pages name it), which would print those years' twelve
> month grids marking the no-trading days? A PDF or scan from your own archive,
> for either year, is exactly what I need.

**Secondary route (human, seconds):** the Swiss National Library's web
archive (e-helvetica.nb.admin.ch → Webarchiv search) has no machine-reachable
query surface (SPA, probed 2026-10-04 UTC, record in
`holidays/raw/equities/six/e-helvetica-probe-2026-10-04/`), but a GUI browse
for swx.com / six-swiss-exchange.com captures of 2010-2011 may hold the
named URLs.

**What closes it:** the operator's own per-year Trading Calendar PDF (or a
Trading Guide edition reprinting the year's twelve month grids with the
"Market Holiday — Market Closed" shading), retrieved from SIX's own channels
or a copy the desk stands behind. **Not** the settlement calendar or the
Currency Holiday Calendar — those are national-bank/currency settlement
documents and key nothing. Lands in
`holidays/raw/equities/six/2010-2011-recovered/` (sha256 + retrieval date).
Unlocks the `Closed` rows in `src/calendar/schedules/holidays/six.rs` and
re-joins the audited windows across the **2010-2011** span. Hunt record:
`holidays/raw/equities/six/` (`2010-2024/`, `hunt-3-2026-10-03/`,
`evidence-thread/probes-2026-10-02/`, `edu-2010-2011-2026-10-04/` — the
index pages naming the 11-January-2010 edition — and
`messages-2010-2011-2026-10-04/` — all 96 captured official notices read,
none calendar-bearing).

---

## 4. SGX — issue [#213](https://github.com/SharurTrading/exchange-hours-rs/issues/213)

**Who to ask:** SGX (Singapore Exchange) client services / equities market
data — the desk behind the securities trading-hours calendar page and the
annual "Trading Hours, Trading Days and Holidays" member notices.

**The dates the evidence must cover, exact:**
- **2010-01-01 .. 2013-12-31** — the securities market's holiday calendar for
  each of 2010, 2011, 2012 and 2013.
- **2020-01-02 .. 2024-12-31** — the same for 2020 (from 2 January; New Year's
  Day 2020 is already witnessed) through 2024.

**The exact ask:**

> Could you send me the SGX securities market trading calendar / holiday
> schedules as published for 2010-2013 and 2020-2024 — the annual
> "trading hours, trading days and holidays" notices or the trading-hours
> calendar page as it stood in those years? PDFs or page exports are perfect;
> any one year helps.

**What closes it:** an operator artifact **at T1** printing the span's
closures — any era of the operator's own securities calendar page (the
`marketplace` portal, the `wps/portal/sgxweb` page, the current content-API
page) captured or exported, or an annual securities trading-schedule notice.
Lands in `holidays/raw/equities/sgx_securities/<year-span>/` (sha256 +
retrieval date). Unlocks the `Closed` rows in
`src/calendar/schedules/holidays/sgx_securities.rs` and re-joins the audited
windows (`2014-01-01..2019-12-31` and `2025-01-01..2026-12-31` today). Hunt
record: `holidays/raw/equities/sgx_securities/` (`evidence-thread/`,
`2010-2013-retry/`, `2020-2024-retry/`, `hunt-3-2026-10-03/`).

*The standing human-side item, recorded by the 2026-10-02 hunt:* the archive.today
snapshot **`https://archive.li/20120910023452/http://www.sgx.com/wps/portal/sgxweb/home/trading/securities/trading_hours_calendar`**
— the only known capture of the securities trading-hours calendar page from the
server-rendered (pre-SPA) era, and its timestamp falls inside the 2010-2013
gap. All four mirrors serve a reCAPTCHA interstitial to the agents' network, so
**the maintainer opens it in a normal browser** (Ctrl+S / print to PDF) and
drops the bytes beside the note in `evidence-thread/`. If they carry the
calendar, the span's second half (the 2012/2013 closures) keys directly; the
2010-2011 part still needs an earlier artifact.

*Two smaller asks, same desk, same issue:* (a) the **2014, 2015 and 2016**
editions if they show the half-day (shortened-session) treatment — the
archived sheets print no half-day markers, so the eves' treatment is unstated;
(b) any post-June-2019 artifact printing the **half-day grid as it stood after
the 2019-06-03 Trade-at-Close launch** — it pins the 2019-12-24 and
2019-12-31 eve close instants (currently held at the last printed grid,
12:36).

---

## 5. NZX — issue [#209](https://github.com/SharurTrading/exchange-hours-rs/issues/209) — MOOT, closed as data 2026-10-02/03

**Do not chase this on the thread.** The 2017 half of the span had already
re-joined from the operator's 2016/2017 memorandum (PR #251), and the residual
**2016-04-26..2016-12-22** span closed in PR #261 (2026-10-03):
`NZX-DD-2015-11-20` — *"NZX Dairy Derivatives Market Holidays – 2015/2016"*,
recovered from the download system of the operator's own derivatives site
(`nzxfutures.com`) via Wayback capture 20170520051811 — prints Queen's Birthday
2016-06-06 and Labour Day 2016-10-24 in session language, corroborated by the
series' `NZX-DD-2015-01-16` and `NZX-DX-2013-09-17` editions. The audited
windows re-joined into one `2010-01-01..2027-01-04` span.

Issue closed 2026-10-03. Hunt record:
`holidays/raw/equities/nzx/evidence-thread/`.

---

## 6. CME Group — issue [#79](https://github.com/SharurTrading/exchange-hours-rs/issues/79) — sharpened: only the 2012 Sunday Pre-Open switch date

**Who to ask:** CME Group Global Command Center (+1 312 456 2391) or CME
Group Client Services — in writing. Note: the crate-side automated access to
cmegroup.com is blocked by the operator's own data-use controls, so a **human
desk reply is the sanctioned route here**, not another scrape; this is the
closing condition the issue's own record names "best first".

**What changed:** the 2026-10-03 bracket re-reads (PR #268) closed every
archive-side candidate, so the missing evidence is now only the **effective
date of the 2012 change** on which the Sunday market pause/pre-open moved from
**16:15:00 to 16:00:00 CT**. CME's own trading-hours captures bracket it to
**2012-05-28..2012-06-07** — both endpoints are saved bytes now (the 2012-05-28
index prints 16:15 platform-wide across the equity, FX, STIR, metals and energy
sections; the 2012-06-07 index prints 16:00 —
`holidays/raw/cme-bracket-rereads/`), and the only Sunday inside the bracket
(2012-06-03) must **not** be assumed. Advisory 20120518, the one candidate
dating document, states only the grain matching hours and never the
queues/Pre-Open; its detail document `globex/files/newtradinghours.pdf` is
proven never-archived — exactly one Wayback capture, a 404, and Common Crawl's
2012 index of that directory (127 rows) does not list it.

**The exact ask:**

> Could you confirm, in writing, the effective date of the change, back in
> 2012, when the Sunday market pause/pre-open moved from 16:15:00 to 16:00:00
> CT (between 28 May and 7 June 2012) — for the E-mini equity index products
> and the metals Trade-at-Settlement (TAS) groups? A Globex notice, market-data
> advisory, MRAN edition or Global Command Center bulletin dated at the time
> would be ideal. If your archive holds the detail PDF
> (`globex/files/newtradinghours.pdf`) linked from the 18 May 2012 market-data
> advisory, its content answers the same question. The current Sunday Pre-Open
> time for an ordinary week (for example Sunday 4 January 2026) in the same
> reply is welcome corroboration.

**What closes it:** a written desk reply or a dated CME artifact in the
operator's own session language — a Globex notice, a market-data advisory, an
MRAN edition, a Global Command Center one-pager (the 2013 grain notice of the
same class proves the genre exists), or the current service's own response for
an ordinary week, **checked for `hasEvents: true`** before it is treated as
evidence. One dated answer closes all four keys the issue names
(`globex_equity_index`, `globex_gold_tas`, `globex_silver_tas`,
`globex_copper_tas`) — whoever dates one dates all four rows — and lifts the
same withholding on the further Globex scopes the thread records as masked by
it (energy, FX, interest rates; 5,126 refused Sundays across the walk). Lands
in `holidays/raw/cme-bracket-rereads/` (or beside the existing
`cme-2025-01-05-spn/` bundle; sha256 + retrieval date; the desk email kept
verbatim). Unlocks the withheld **16:00-16:15 CT** Sunday quarter-hour in the
shared CME module (`src/calendar/schedules/futures/us/cme_group.rs`) and
resolves the bracket-era declaration recorded in `docs/evidence/globex_equity_index.md`
and the three TAS evidence files. Hunt record: `holidays/raw/cme-bracket-rereads/`
plus the advisory at `cme-globex/trade-types/raw/metals-tas-history/`.

---

## 7. CME Group — issue [#123](https://github.com/SharurTrading/exchange-hours-rs/issues/123) — the five-day era's Pre-Open onset for cryptocurrency futures

**Who to ask:** the same CME desk, same reply thread as section 6.

**The dates the evidence must cover, exact:** the five-day era — from the
sourced 2017-12-17 launch to the 2026-05-29 bridge — specifically a
**day-level effective date** for the era's Sunday and weekday **Pre-Open**
(order-entry) queues. An `order_entry` gap: no trade prints in the omitted
window, but 2,699 dates refuse on it (513 inside the 2025-2027 gate window).

**What the record shows:** SER-8051R (2017-12-14) dates the listing and states
matching hours only ("CME Globex and CME ClearPort: 5:00 p.m. to 4:00 p.m.,
Sun-Fri. (Central Time)"); the launch-week Globex notices of 2017-11-27,
2017-12-04 and 2017-12-11 date the listing and print no hours at all; the
Globex Product Reference Sheet whose file metadata dates it 2018-10-01 lists
"Bitcoin Futures BTC" and carries **no hours and no Pre-Open columns at all**;
the 2019/2020/2021 specification captures print the matching grid only. PR
#268 re-read every one of these at the byte level — a definitive negative is
on file, so a further archive sweep is not the closing move.

**The exact ask:**

> Do your notice archives or client-systems wiki hold anything stating when
> the Sunday and weekday Pre-Open (order-entry) queues began for Bitcoin
> futures — and the cryptocurrency family generally — under the five-day
> 17:00-16:00 CT grid that ran from December 2017? We need an effective date
> stated in session language (for example "a Pre-Open from X to Y CT,
> effective \<date\>"), not just the matching hours.

**What closes it:** a CME artifact that states the Pre-Open **in session
language** on a **day-level effective date** (LAW-PRIMARY-SOURCES,
LAW-NO-FABRICATED-DATES) — a Globex notice, an SER, a product-specification
page carrying the Pre-Open, or a client-systems wiki revision. It keys the
era's order-entry rows and retires the `NormalWeekPhaseWithheld` declaration
that cites #123. Hunt record: `holidays/raw/cme-bracket-rereads/`
(SER-8051R, the reference sheet, the CDX dumps) and
`cme-globex/trade-types/raw/metals-tas-history/notices1718/`.

---

## 8. CME Group — issue [#259](https://github.com/SharurTrading/exchange-hours-rs/issues/259) — the 2012-05-20..2013-04-06 grains regime's queues and switch-on day

**Who to ask:** the same CME desk, same reply thread as section 6.

**The dates the evidence must cover, exact:** the 21-hour regime between the
dated 2012-05-20 matching expansion and the dated 2013-04-07 revision — its
**queue/PCP times and the switch-on date**. The states themselves are known
from CME's own trading-hours captures (Sunday Pre-Open 16:00, weekday
"14:30-16:00, 16:45-17:00"), but they are bracket observations, not operator
statements on a day: the switch is bracketed **2012-05-11..2012-05-28**
(2012-05-11 prints the old grid, 2012-05-28 the new states), and advisory
20120518 — the regime's own dated row — states only the new matching hours,
never the queue times. Same bracket era, same never-archived detail document
(`globex/files/newtradinghours.pdf`) as section 6.

**The exact ask:**

> The same 2012 archive question, for grains: does anything in your archive
> state the Sunday Pre-Open and the weekday queue/PCP times for the CBOT grain
> and oilseed futures under the expanded 17:00-14:00 CT hours that took effect
> around Sunday 20 May 2012 — and the exact day they took effect? The detail
> PDF linked from the 18 May 2012 market-data advisory
> (`globex/files/newtradinghours.pdf`) would answer this if your archive holds
> it; a Global Command Center one-pager of the kind you issued on 22 March
> 2013 for the next revision would too.

**What closes it:** a CME document that states those queue times **in session
language on a day-level effective date** — it keys the queue revision row and
retires the `grains_omitted_regime_queues` declaration (322 refused dates,
2012-05-20..2013-04-06). #259 is the gap's **live closing condition**
(re-cited by #263 after #116 closed without landing the data). Hunt record:
`holidays/raw/cme-bracket-rereads/`; evidence record in
`docs/evidence/globex_grains.md`.

**Rider, 2026-10-04 UTC — #283 rides the same ask.** The pre-regime span has
the same shape and the same closer: the grain PCP start moved 13:15:30 → 14:30
and the 16:45 weekday evening Pre-Open appeared somewhere inside
**2010-04-19..2012-05-11** (notice 20100405 dates the 13:15:30 start; the
2012-05-11 capture prints "14:30-16:00, 16:45, 08:00"), and no dated artifact
separates them — the archived 2008-2011 weekly notices were text-scanned for
the span and the only candidate touching the evening slot is the generic
2010-10-18/2010-10-25 notice ("CME, CBOT, KCBT and MGEX products", 16:45 from
2010-11-15), which enumerates no family and cannot key a grain row against
the March-2010 family-specific table. The crate serves the sourced
intersection (PCP 14:30-16:00, no evening queue) with the disputed remainders
disclosed as the residual. One dated answer to §8's question that also states
the pre-regime PCP start and evening Pre-Open closes #283's residual as a
normal schedule fix.

---

## 9. CME Group — issue [#162](https://github.com/SharurTrading/exchange-hours-rs/issues/162) — NEW ask: NKD/NIY on the five 2025 merged trade dates

**Who to ask:** the same CME desk. This section is new — the issue predates
this list but was never in it, and the 2026-10-03 re-check (PR #269) is what
made the ask desk-shaped.

**The dates the evidence must cover, exact:** the five 2025 merged trade dates
**2025-01-21, 2025-02-18, 2025-05-27, 2025-06-20, 2025-09-02** — the
day-after-holiday dates on which CME assigns the Sunday- or
Wednesday-evening-through-holiday span to the *following* business day. The
family ships twelve merged dates with their own `NKD`(168)/`NIY`(167) witness
bytes; these five have none, and the crate answers them from the shared CME
grid, shipping `early_close(12:00)` rows on the preceding days instead.

**What the record shows:** the trading-hours service **definitively carries no
NKD/NIY events for those five dates** — the 2026-10-03 re-check tried every
query shape live (the THBP-A set, single-product `id=168`, and wider THBP-B
windows through each merged day) and every one returned `hasEvents:false` /
zero events for every product, while a positive control (2025-11-26..29)
returned `hasEvents:true` with the full NKD/NIY schedules — the channel is
healthy; the events are simply not in it. Today's live channel cannot restate
windows before Thanksgiving 2025, and no archived capture of that id set
exists for the windows.

**The exact ask:**

> Do Nikkei (USD) and Nikkei (Yen) futures carry their own session schedules
> on the merged trade dates — the days after a US holiday when the Sunday or
> Wednesday evening Globex session is assigned to the following business day?
> Specifically for 21 January, 18 February, 27 May, 20 June and 2 September
> 2025: did NKD/NIY run their own sessions on those trade dates, and if so,
> what were the open, close and Pre-Open instants? (Our copies of the
> trading-hours service carry no events at all for those windows — a service
> retention limit, since the same queries over late November 2025 return the
> full schedules.)

**What closes it:** a desk statement at T1 — either the five merged-day
sessions **with their instants** (keys the five rows the family is missing), or
a confirmation that NKD/NIY follow the shared CME grid on those dates (the
evidence file records it and the witness gap closes with the shipped answers
standing). The issue's artifact form: a THBP-B response
(`id=168,167,320,323,19,27`) carrying an NKD or NIY event on any of the five
dates. Hunt record: `holidays/raw/cme-nikkei-witness-recheck-2026-10/` and the
original edge-B captures in `holidays/raw/cme-2025-2027-repair/json/`.

---

## 10. Coinbase Derivatives — issue [#112](https://github.com/SharurTrading/exchange-hours-rs/issues/112) — sharpened: notice 22-10 does not exist in the operator's own CMS

**Who to ask:** Coinbase Derivatives client services / market operations (the
desk behind the Market Notices listing at
`coinbase.com/derivatives/market-notices`; the operator was FairX in 2022).

**What the record shows (2026-10-03, PR #269):** the live listing embeds PDF
hrefs for many notice rows, but notice **22-10**'s title cell is plain text
with no address — as are some twenty older rows' (21-01..21-07, 22-01..22-09,
26-19, 24-20) — so the operator's current CMS holds no 22-10 asset to link.
The archive is negative: CDX sweeps over the whole ctfassets asset space
(`.*22-10.*` and `.*[Tt]hanksgiving.*`), the `trade.ledgerx.com` predecessor
channel (no announcement pages at all), and fresh web-search shapes all came
back empty. Notice 22-11's PDF (retrieved from the operator's CDN) restates
only Christmas. Consequence: trade dates **2022-11-24 and 2022-11-25** ship
`HolidayKind::Unsourced`.

**The exact ask:**

> Could you send me a copy of Market Notice 22-10, "Market Notice -
> Thanksgiving Holiday Schedule 2022" (posted 12/12/2022)? Your current market
> notices listing names it, but the PDF no longer resolves anywhere. A copy of
> the notice as issued is exactly what I need. Separately, if you can re-issue
> notice 24-12 (Juneteenth 2024) without the "IN DRAFT" watermark, that closes
> a second provenance question on the same table.

**What closes it:** any surviving copy of notice 22-10 (keys 2022-11-24/25),
or a final-state/non-draft copy of notice 24-12 (confirms the 2024-06-19
closure's provenance). Lands in `holidays/raw/cde/` (sha256 + retrieval date).
Hunt record: `holidays/raw/cde/recheck-2026-10-03/` +
`holidays/raw/coinbase-derivatives-2022-2024/cdx_*.txt` + the original
`holidays/raw/cde-2021-2025/`.

---

## 11. Coinbase Derivatives — issue [#155](https://github.com/SharurTrading/exchange-hours-rs/issues/155) — the next holiday notice

**Who to ask:** the same desk; this one is mostly a watch, not a question.

**What the record shows:** the newest holiday notice is still **26-36**
(effective 2026-09-07); the newest notices overall are 26-33.3/26-37 (posted
09/24/2026, Maintenance — 26-37 is the Q4 quarterly-maintenance notice). This
operator announces holidays **per notice, a few weeks ahead** — there is no
annual calendar — and its 2025 pattern put the Thanksgiving notice at ~10/30
(notice 25-37 posted 10/30/2025), so the 2026 Thanksgiving notice is expected
around **2026-10-30**.

**The exact ask:**

> When your next holiday schedule notice posts (Thanksgiving/Christmas 2026 by
> last year's pattern), could you post the PDF here, or a link to it? And one
> standing second item: notice 26-33.1 defers the 24x7 transition's production
> date to "October 2026 (date to be announced)" — when that date is stated
> unconditionally, the same notice would be welcome.

**What closes it:** the operator's next holiday notice extends the audited
window past 2026-09-07 (480 dates refuse today, 2026-09-08..2027-12-31, and
`is_open` already fails from 2026-09-07T06:00Z); the unconditional 24x7
production-date notice closes the issue's other blocked item. Hunt record:
`holidays/raw/cde/recheck-2026-10-03/`.

---

## 12. Eurex — issue [#157](https://github.com/SharurTrading/exchange-hours-rs/issues/157) — re-scoped to the tba era

**Who to ask:** Eurex client services / the publications desk behind the
"Eurex trading calendar" PDFs on eurexgroup.com.

**What changed:** PR #271 (2026-10-03) encoded the German-scope closures the
2014-2018 editions date (8 rows) and re-scoped the declaration to the **tba
era**. The 2025 edition says "Kein Handel und keine Ausübung in deutschen
Aktien- und Aktienindex-derivaten …: tba." and the 2026 edition says "closed
for trading and exercise in German equity and equity index derivatives …: to
be announced" — the operator declares the closures and dates none of them.

**The dates the evidence must cover, exact:** the German equity /
equity-index (and Xetra-based ETF/ETC) closure days for **2025 and 2026** —
dated by an Eurex edition, or stated to be none — plus the **`Trading
calendar 2027`** edition when it publishes (2027 currently lies outside the
audited windows).

**The exact ask:**

> Your trading calendar 2025 and 2026 editions declare "no trading in German
> equity and equity index derivatives … based on Xetra listings" but give the
> days only as "tba" / "to be announced". Could you tell me which days that
> covered in 2025 and 2026 — or confirm there were none — and send the 2027
> edition of the trading calendar when it is published?

**What closes it:** an Eurex announcement, circular or Trading Calendar
edition that either dates the German-scope closures or states a year has none
(730 refused dates in the tba era, 2025-01-01..2026-12-30), and the 2027
edition extends the window bound. Hunt record: `holidays/raw/eurex-2025-2027/`
and `holidays/raw/eurex-2010-2024/`.

---

## 13. Xetra / Deutsche Börse — issue [#200](https://github.com/SharurTrading/exchange-hours-rs/issues/200) — the 2027 edition only

**Who to ask:** Deutsche Börse / Xetra market data services — the desk behind
the cash-market Trading Calendar page and its per-year PDFs.

**What changed:** the 2025 half closed on 2026-10-03 (PR #269) — six 2025-era
operator editions each affirmatively name the four 2025 Xetra holidays while
wording the 20:00 holiday-close note over Börse Frankfurt only, which is the
confirmation the issue named; the scope answers its whole walk but for the
walk-end edge. What remains is the **2027 close schedule**, unpublished: no
artifact names 2027 trading-holiday hours, and three 2027 instants (2027-05-06,
2027-05-17, 2027-05-27) answer `Covered` where the operator may yet close at
20:00 — the instant-level residual risk the evidence file carries. Re-checked
monthly per LAW-WATCH.

**The exact ask:**

> Could you send me the "Trading calendar 2027" PDF (or the per-year page
> edition) when it publishes — the one naming the 2027 trading holidays and
> their early-close treatment? The 2026 edition is live on your page today;
> the 2027 one is all I still need.

**What closes it:** the operator's next per-year page edition or the
`Trading calendar 2027` PDF. Hunt record:
`holidays/raw/equities/xetra/recheck-2026-10/`.

---

## Closing note

Artifacts posted to the thread or saved anywhere work — the crate only needs
the **bytes plus a URL and a retrieval date**. A verbatim copy, an email
attachment, a link the desk stands behind, or an archive capture are all
admissible; the maintainer records each artifact's sha256 and UTC retrieval
date in the research store beside the venue's existing provenance discipline
(`INDEX.md` + `SHA256SUMS.txt`). What cannot key a row: a vendor or news
restatement, a settlement/currency calendar standing in for a trading
calendar, or a date inferred from a coverage bracket. When evidence lands,
the affected schedule module, its evidence file, the per-year test tallies
and the ledger row move together in the issue's own change.

---

## Amendment 2026-10-04 UTC — the 2026-10-03 merge wave changed this list

The 2026-10-02/03 merge waves reshaped every section; the list above already
reflects all of it.

- **Sections 1, 2 and 5 are moot.** #221 closed via #255 (the 2013-2016 spans,
  wire mirrors and operator pages) and #262 (the 2011-12-12 TMX release from
  the Mondo Visione verbatim mirror); #218 closed via #256 (the lseg.com
  Business days page's 2013-2020 capture run); #209 closed via #261
  (`NZX-DD-2015-11-20`, the operator's derivatives-site memorandum). The
  thread should not chase these.
- **PR #268** landed definitive byte-level negatives for #79/#123/#259
  (`holidays/raw/cme-bracket-rereads/`), so sections 6-8 are now sharp: the
  only missing evidence on each is an operator statement — the 2012 Sunday
  switch date (bracket 2012-05-28..2012-06-07, both endpoints saved bytes),
  the five-day-era Pre-Open onset, the grains regime's queue times and
  switch-on day (bracket 2012-05-11..2012-05-28) — each pointing at the desk
  or the never-archived `newtradinghours.pdf`.
- **PR #269** closed #200's 2025 half (the confirmation landed), re-verified
  the #155/#112 listings, and made #162's negative definitive with a positive
  control — #162 enters this list as a new ask (section 9) and #112 is
  sharpened (section 10).
- **PR #270** closed #212's 2018-2019 half as data (the 28 May 2018 Trading
  Guide's own grids — the mechanism section 3 asks for), and landed the
  sgx/six hunt-3 records behind sections 3 and 4.
- **PR #271** encoded the eurex German-scope closures 2014-2018 and re-scoped
  #157 to the tba era — section 12.
- Section 4 gains the standing human-side item the 2026-10-02 hunt recorded:
  the archive.today snapshot of 2012-09-10, which only the maintainer's
  browser can fetch.
- Net effect: the live ask count went from six to ten, grouped per desk —
  CME (6-9), Coinbase Derivatives (10-11), SGX (4), SIX (3), Eurex (12),
  Xetra (13).


## Amendment 2026-10-04 UTC (second) — the negative-record hunts finished the machine angles

Every machine-reachable channel for every live ask has now been worked to an
exhaustive, artifact-backed negative; the asks above are final unless an
operator replies:

- **§6 CME (#79)** — the archived trading-hours tree holds exactly the two
  bracket endpoints (2012-05-28/301+200 pair, 2012-06-07); no in-bracket
  witness exists in Wayback, Common Crawl (2012 crawled February only),
  archive.today (429), arquivo.pt or Memento. The desk reply is the closer.
- **§7 CME (#123)** — the cryptocurrency product/landing/FAQ/spec pages carry
  no trading-hours content in ANY archived capture from the 2017-12-17 launch
  onward (93-capture product page, byte-verified CC fetch, 18-sheet 2019
  holiday workbook — whose Bitcoin rows print the queue's times, but holiday
  data cannot date the normal week). The desk reply is the closer.
- **§8 CME (#259)** — unchanged; same bracket, same definitive negatives.
- **§9 CME (#162)** — the trading-hours service provably carries no NKD/NIY
  events for the five dates (every query shape, live, with a positive
  control). The desk confirmation ask stands.
- **§4 SGX (#213)** — hunt 4 complete: the member-circulars channel cannot
  carry the calendar (complete enumerations; the 2022 sitemap.xml — the
  operator's own — names no securities calendar page, the calendar was an SPA
  route whose feed the archive shows empty until 2026). The archive.today
  snapshot `20120910023452` (human fetch) is the sole remaining lead for
  2010-2013; the 2020-2024 half has no known lead.
- **§3 SIX (#212)** — the closing condition is now NAMED BYTES: the Trading
  Guide edition of 11 January 2010 (`trading_guide_2010_01_11_en.pdf`), named
  by the operator's own archived guides index pages; all 96 captured official
  notices read, none calendar-bearing; Common Crawl's early indices remain
  504-outage-blocked (re-runnable). The desk ask above names the edition.
- **§12 Eurex (#157)** — the circular database is completely enumerated: all
  170 items of 2025 and all 100 of 2026, gap-free, none a German-scope
  closure — while circular 080/2014 proves the channel carries exactly that
  mechanism day-level. The `tba` era is unresolved at the operator; the 2027
  Trading Calendar edition (due this window) and a desk ask are the closers.

The thread's expected yield is unchanged: any ONE of these artifacts closes
its issue as data the day it arrives.
