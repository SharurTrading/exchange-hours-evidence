# Evidence index — task `eurex/circulars-2026-10-04`

The untried channel for **#157**: Eurex circulars, readiness newsflashes and the public
production newsboard, swept for any operator statement that dates the German-scope
closures the 2025/2026 Trading Calendar editions declare `tba` / `to be announced`.

**Outcome: NEGATIVE — the channel carries no dated German-scope closure for 2025 or 2026.**
The operator's own announcement mechanism for these closures is proven real (the 2014-2018
circulars, one read in full below) and produces nothing for the `tba` era: every circular
and newsflash of 2025 and 2026-to-date is enumerated below, the only "no trading"
announcements in either year are KOSPI-scope, and the newsboard carries zero holiday
reminders over the whole era (against explicit reminders for the 2018 and 2019 German
holidays). #157 stays open; the closing condition remains an operator artifact that dates
the German-scope closures.

Retrieval session: **2026-10-04T01:31–02:01 UTC** (LAW-UTC-DATES). All fetches were plain
`curl` GETs with a desktop browser User-Agent on public, unauthenticated URLs; no access
control was evaded. In-file timestamp labels mark the fetch batch; the final batch is
exact (`20261004T020001Z`, generated from the machine clock). Digests for every file are
in `SHA256SUMS.txt` beside this index.

## What the channel is, and what it shows

- The circular search is the site's own server-rendered database:
  `https://www.eurex.com/ex-en/find/circulars/1720!search?query=<term>&pageNum=<n>&hitsPerPage=50&sort=sDate desc`,
  with `dateFrom`/`dateTo` in **MM/DD/yyyy** (the datepicker's own format string, read
  from the page). It covers circulars back to 2008 and the current numbered series without
  gaps: 2025 enumerates `001/2025`..`119/2025` complete, 2026 enumerates `001/2026`..`064/2026`
  complete to date (verified by number; no gaps), plus every Readiness Newsflash.
- **Full-year enumeration (not keyword search) is the decisive negative.** All 170 items of
  2025 and all 100 items of 2026-to-date were listed by date and scanned by title: no
  trading-calendar circular, no holiday-regulation circular, no German-scope closure, and
  no trading-hours notice for Whit Monday 2025 (9 June), German Unity Day 2025 (3 October)
  or Whit Monday 2026 (25 May). The only "no trading" circulars of 2025/2026 are
  `004/2025` and `043/2025` (Eurex KOSPI / USD-KRW derivatives — not this identity's
  scope). The only "Trading hours at Eurex Exchange on …" circular of the era is
  `105/2025` (30 December 2025 year-end hours; read in full below; it is not a
  German-scope item).
- **The mechanism is real.** Eurex Circular 080/2014 ("Trading calendar: Holiday
  regulation for 3 October 2014 ('German Unification Day')"), read in full below, states
  the exact T1 shape a `tba` resolution takes: the FWB Exchange Council's no-trading
  decision for Frankfurt, and "accordingly, the Management Board of Eurex Deutschland …
  decided to suspend trading on this day for the following products", naming FDAX, FDXM's
  family (MDAX/TecDAX/DivDAX index futures) and the German equity derivatives explicitly,
  day-level, in session language. Every pre-2019 German-scope closure has such a circular
  (080/2014, 164/2014, 004/2016, 128/2016, 148/2017, 055/2018 — all still retrievable
  through the same search). For 2025/2026 the operator has published none: the `tba`
  note is unresolved **at the operator**, not merely unretained by the archive.
- **Newsboard (T2) corroborates.** The public production-newsboard search
  (`/ex-en/trade/production-newsboard/3486!search`) carries explicit holiday reminders for
  past German-scope closures ("Holiday reminder 03.10.2019", "Reminder: Holiday regulation
  for 21st of May 2018") but **zero** holiday/reminder items over
  2025-01-01..2026-10-04.
- **Angles tried and negative**: keyword searches (EN: German Unity Day, Unity, Whit
  Monday, Whitsun, Ascension, Corpus Christi, Pentecost, holiday regulation, public
  holiday, trading calendar, 3 October, no trading, closed for trading; DE: Feiertag,
  Tag der Deutschen Einheit, Pfingstmontag — the database is English-only, all zero or
  pre-2019 hits); Wayback CDX of `eurex.com/ex-en/find/circulars*` for 2025-2026 (1598
  unique URLs) and four windows around each candidate holiday; external web search EN+DE
  (only T3/T4 vendor noise); `/ex-de/` circulars path (HTTP 404 — no German-language
  channel on the current site); `deutsche-boerse.com` newsroom paths (HTTP 404, no Eurex
  hours notices found via site search); `eurexgroup.com` (301 to `eurex.com` — the group
  site is retired; its notices live where the sweep already went).

## Files

| File | Exact URL (pattern) | Retrieved (UTC) | What it contains |
|---|---|---|---|
| `cdx_eurex_circulars_2025-2026.txt` | `http://web.archive.org/cdx/search/cdx?url=eurex.com/ex-en/find/circulars*&from=2025&to=2026&fl=timestamp,original,statuscode&collapse=urlkey&limit=3000` | 01:33 | Wayback CDX sweep, 1598 unique URLs. Contains the 2014/2015/2018 German holiday circular slugs (channel precedent) and no 2025/2026 German-holiday slug. |
| `circulars_page.live-20261004T013300Z.html` | `https://www.eurex.com/ex-en/find/circulars` | 01:33 | The channel's landing page, server-rendering the newest circulars and the search/filter form this sweep drives. |
| `circular-5552956.live-20261004T013400Z.html` | `https://www.eurex.com/ex-en/find/circulars/circular-5552956` | 01:34 | One detail page as a channel probe: circular 060/2026 (position limits), server-rendered body. |
| `search_german_unity_day.live-20261004T013600Z.html` | `…/1720!search?query=German%20Unity%20Day&hitsPerPage=50` | 01:36 | 1 hit: circular 055/2018 only. No 2025/2026 item. |
| `search_q_*.live-20261004T013800Z.html` | `…/1720!search?query=<term>&hitsPerPage=50` for Whit Monday, Whitsun, Ascension, Corpus Christi, public holiday, holiday regulation, trading calendar, 3 October, Unity Day, German equity, German holiday, Feiertag, Tag der Deutschen Einheit, Pfingstmontag | 01:37–01:39 | The keyword sweeps. German terms: 0 hits (English-only database). The latest trading-calendar/holiday-regulation circular in any result is No. 095/2018-era; the 2025/2026 hits of the broad terms are product/technology circulars matching incidentally. |
| `newsflash_updates_october_2025.live-20261004T014000Z.html` | `https://www.eurex.com/ex-en/find/circulars/Eurex-Readiness-Newsflash-Updates-October-2025-4706806` | 01:40 | The monthly newsflash published two days before Unity Day 2025: no German-scope item. |
| `search_3october_hpp200.live-20261004T014100Z.html` | `…/1720!search?query=3%20October&hitsPerPage=200` | 01:41 | Backend caps the page; superseded by the paginated sweep below. |
| `search_3october_p0..p3.live-20261004T014300Z.html` | `…/1720!search?query=3%20October&pageNum=0..3&hitsPerPage=50&sort=sDate desc` | 01:43 | All 152 hits of "3 October", date-sorted: no Unity Day circular for 2025 or 2026. |
| `search_tradinghours_p0..p4.live-20261004T014400Z.html` | paginated "Trading hours at Eurex Exchange" with a stale `state` token | 01:44 | Failed attempt (stale state param); kept for the record. Superseded by `search_th_on_p*`. |
| `search_th_on_p0..p5.live-20261004T014500Z.html` | `…/1720!search?query=Trading%20hours%20at%20Eurex%20Exchange%20on&pageNum=0..5&hitsPerPage=50&sort=sDate desc` | 01:45 | The complete year-end-circular series 2009..2025, one per year, latest `105/2025`. None is a German-scope item. |
| `circular_105_2025.live-20261004T014700Z.html` | `https://www.eurex.com/ex-en/find/circulars/circular-4795408` | 01:47 | **T1, read in full.** Circular 105/2025, "Trading hours at Eurex Exchange on 30 December 2025": year-end early closes for derivatives on Xetra/Vienna underlyings; states explicitly that German index futures (e.g. FDAX) are *not* affected and keep regular times. Not a German-scope closure item. |
| `newsflash_updates_june_2025.live-20261004T014700Z.html` | `…/Eurex-Readiness-Newsflash-Updates-June-2025-4492364` | 01:47 | The month containing Whit Monday 2025 (9 June): the 09 Jun entries are contract-spec/LP items; the only no-trading entry is KOSPI 03 Jun. No German-scope item. |
| `newsflash_updates_september_2025.live-20261004T014700Z.html` | `…/Eurex-Readiness-Newsflash-Updates-September-2025-4652028` | 01:47 | The month before Unity Day 2025 (3 October, a Friday): no German-scope item. |
| `newsflash_updates_october_2026.live-20261004T014700Z.html` | `…/Eurex-Readiness-Newsflash-Updates-October-2026-5605940` | 01:47 | The month containing Unity Day 2026 (3 October, a Saturday — no weekday session): no German-scope item. |
| `circular_080_2014.live-20261004T014900Z.html` | `https://www.eurex.com/ex-en/find/circulars/Trading-calendar-Holiday-regulation-for-3-October-2014-German-Unification-Day--174240` | 01:49 | **T1, read in full — the channel's mechanism, stated by the operator.** Circular 080/2014: the FWB Exchange Council's no-trading decision for 3 October 2014, and "accordingly, the Management Board of Eurex Deutschland and the Executive Board of Eurex Zürich AG likewise decided to suspend trading on this day for the following products: … Index Futures of the DAX® family, i.e. DAX® (FDAX), MDAX® (F2MX), TecDAX® (FTDX) and DivDAX® (FDIV). All other products will be traded on 3 October 2014, as before." This is the shape no 2025/2026 artifact takes. |
| `listing_2025_p0.live-20261004T015100Z.html`, `listing_2025_star_p0`, `listing_2025_e_p0` | `…/1720!search?query=…&dateFrom=2025-01-01…` (ISO date format) | 01:51–01:52 | Failed listing attempts: ISO `YYYY-MM-DD` dates return an empty result set. Kept to document the trap; the working format is the datepicker's `MM/DD/yyyy`. |
| `listing_2025_all_p0.live-20261004T015300Z.html` | `…/1720!search?query=*&dateFrom=01/01/2025&dateTo=12/31/2025&pageNum=0&hitsPerPage=50&sort=sDate asc` | 01:53 | First successful full-year listing page. |
| `newsboard_q_Unity/holiday/German.live-20261004T015400Z.html` | `https://www.eurex.com/ex-en/trade/production-newsboard/3486!search?query=<term>&submit=Search` | 01:54 | Newsboard keyword probes. "holiday" 30 hits (latest German-holiday reminder 2019-10-02; KRX Easter 2025 item is scope-specific), "German" 11 hits (latest German-scope item 2020-03-19), "Unity" 0. |
| `eurexgroup_home.live-20261004T015600Z.html` | `https://www.eurexgroup.com/` | 01:56 | HTTP 301 body redirecting to `https://www.eurex.com/ex-en/` — the group site is retired; no separate notice channel. |
| `listing_2025_p0..p3.live-20261004T020001Z.html` | `…/1720!search?query=*&dateFrom=01/01/2025&dateTo=12/31/2025&pageNum=0..3&hitsPerPage=50&sort=sDate asc` | 02:00:01 exact | **The decisive negative, raw.** All 170 circulars/newsflashes of 2025, ascending. |
| `listing_2026_p0..p1.live-20261004T020001Z.html` | `…/1720!search?query=*&dateFrom=01/01/2026&dateTo=12/31/2026&pageNum=0..1&hitsPerPage=50&sort=sDate asc` | 02:00:01 exact | **The decisive negative, raw.** All 100 circulars/newsflashes of 2026 to date, ascending. |
| `newsboard_holiday_01012025-12312025`, `newsboard_reminder_01012025-12312025`, `newsboard_holiday_01012026-10042026`, `newsboard_reminder_01012026-10042026` | `…/production-newsboard/3486!search?query=<term>&dateFrom=…&dateTo=…&sort=sDate desc` | 02:00:01 exact | **T2 negative.** Zero holiday/reminder items over the whole `tba` era (against "Holiday reminder 03.10.2019" and "Reminder: Holiday regulation for 21st of May 2018" the same channel carries for the pre-2019 closures). |
| `listing_2025_all.live-20261004T021200Z.txt`, `listing_2026_all.live-20261004T021200Z.txt` | derived (this directory) | 02:00 | The two enumerations as plain text (release date + title per line), machine-diffed against the raw pages above: 170 and 100 rows, exact match. Derived from the operator's pages; cite the pages, not these files. |
| `eurex-facelift.js`, `on-site-search.js` | `…/resource/themes/eurex-facelift/js/…` | 01:36 | Site JS bundles fetched while locating the search endpoint (the latter is the site's 404 fallback page — the module name was a guess). Kept for the record; not evidence. |

## Negatives recorded beyond the files

- `https://www.eurex.com/ex-de/find/circulars` and `…/ex-de/find/circulars/1720!search?query=Pfingstmontag` — HTTP 404: the current site has no German-language circulars channel (the German-language circular titles quoted by search engines belong to the retired `eurexchange.com` tree).
- `https://www.deutsche-boerse.com/dbg-en/media/newsroom` and `…/media/newsroom/press-releases` — HTTP 404; a site-restricted web search surfaced no Deutsche Börse group notice about Eurex trading hours or the German-scope closures in 2025/2026. The operator's own circular channel above is where such a notice would live, and it is fully enumerated.
- External web search (English and German) for German-scope holiday statements 2025/2026: only T3/T4 vendor calendars and speculation, none citing an operator artifact that dates a closure. Nothing keyable (LAW-PRIMARY-SOURCES).

## Verdict

NEGATIVE for the circulars/newsboard channel. The 2025/2026 `tba` German-scope closures
remain operator-undated after complete enumeration of the operator's announcement
channels through 2026-10-04T02:01 UTC. No row ships on this evidence; the #157
declaration's span and closing condition are unchanged by this sweep, and the sweep
result itself is recorded in `docs/evidence/eurex.md` (the repo's evidence file) so the
channel is not re-tried blind.
