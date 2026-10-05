# tsx evidence thread — #221 (2010-2016 holiday calendars; spans narrowed 2026-09-30)

Hunt pass: 2026-10-02 UTC. Evidence file: `docs/evidence/tsx.md` (its
2026-09-30 update supersedes the issue body — the surviving spans are
**2011-10-11..2012-01-02**, **2013-08-19..2014-01-01** and
**2014-07-02..2016-12-31**, with the missing artifacts being per-holiday
news releases and any 2015-2016 holiday page). Issue:
SharurTrading/exchange-hours-rs#221.

## What this pass added

**Common Crawl** — the one archive never swept for TSX. The news-release
tree `tmx.com/en/news_events/news/news_releases/<year>/` was crawled by
CC-MAIN-2013-20 (May 2013: releases Jan-May 2013 including
`1-30-2013_TMXGroup-family-day.html` — the tree's CC witness), so the
index is a real channel for the missing releases. Results of the
2026-10-02 prefix queries (retry-wrapped; the CC index gateway returned
504s on roughly 4 of 5 attempts all day):

- `2011/*` in CC-MAIN-2012-05: **zero captures** — CC never crawled the
  2011 tree, so the missing Nov-Dec 2011 year-end/New Year releases are
  not in CC either. (`cc_2012-05_2011.json`, empty.)
- `2014/*` in CC-MAIN-2014-35 and CC-MAIN-2014-41: **zero captures** —
  the 2014 tree vanished from CC's 2014 crawls, so no 2014 New Year
  release there. (empty)
- Failed after 12 retries each (gateway 504, query re-runnable):
  `2013/*` in CC-MAIN-2013-48 (Nov 2013 crawl — the likeliest location of
  the missing 2013 Labour Day/Thanksgiving/Christmas releases),
  `2014/*` in CC-MAIN-2014-10 (Feb 2014 crawl), `2013/*` and `2014/*` in
  CC-MAIN-2014-49. **These four are the remaining unchecked lookups.**
- Pending in the same background batch (results to be appended below):
  `tsx.com/*` in CC-MAIN-2015-48 and CC-MAIN-2016-30 (the 2015-2016
  tsx.com-era site — the domain whose holiday page has no capture at all).

## No other new channel exists

- archive.today: no snapshot of any tmx.com/tsx.com holiday page or
  release URL was attempted beyond existence probes — the release URLs are
  date-and-slug guesses that archive.today's exact-URL index cannot match;
  its coverage of tmx.com in 2011-2016 is negligible.
- Wayback re-sweeps were the 2026-09-29/30 passes themselves (the store's
  `cdx-retry-2026-09-30/` directory holds those outputs and the recovered
  2010-2014 release captures); this pass adds nothing on Wayback, whose
  CDX was additionally 504-degraded on 2026-10-02 for domain-wide regex
  queries.

## Files here

- `cc_2012-05_2011.json`, `cc_2014-35_2014.json`, `cc_2014-41_2014.json` —
  the settled CC results (empty = no captures).
- (To be appended) the 2015-48/2016-30 tsx.com outputs and the remaining
  retry outcomes.

## Next attempt list, in order

1. The four failed CC lookups above (esp. `2013/*` in CC-MAIN-2013-48).
2. The two pending tsx.com 2015-2016 CC sweeps.
3. Human paths: TMX Group's own media archive / a written reply from the
   operator's desk naming the 2011-12 and 2013-14 year-end arrangements.

## CC batch tail (completed 2026-10-02 ~03:15 UTC, `cc-batch-2026-10-02.log` here)

- Settled OK, zero captures: `2011/*` in CC-MAIN-2012-05; `2014/*` in
  CC-MAIN-2014-35 and CC-MAIN-2014-41. CC does not hold the missing
  Nov-Dec 2011 releases or a 2014-tree New Year release.
- Failed after 12 retries each (gateway 504; the Internet Archive entered
  a "Temporarily Offline" state at ~02:45 UTC during the batch) — the
  remaining unchecked CC lookups, in priority order:
  `2013/*` in CC-MAIN-2013-48 (likeliest home of the 2013
  Labour/Thanksgiving/Christmas releases), `2014/*` in CC-MAIN-2014-10,
  `2013/*` + `2014/*` in CC-MAIN-2014-49, and the two `tsx.com/*`
  2015-2016 sweeps (CC-MAIN-2015-48, CC-MAIN-2016-30).

## Hunt pass 2, 2026-10-02 UTC — two spans CLOSED, rows shipped (PR pending)

The named-but-never-run channels found the missing operator statements. The
2013-08-19..2014-01-01 and 2014-07-02..2016-12-31 spans close; only
2011-10-11..2012-01-02 refuses.

**What closed them (all retrieved 2026-10-02 UTC, sha-pinned in SHA256SUMS.txt):**

- **The release series' verbatim wire mirrors are live on CNW/PR Newswire.**
  Wayback's tmx.com release tree ends mid-2014, but the wires still serve the
  whole series: `TMX-REL-2013-08-23` (Labour Day 2013-09-02, PRN 512833881),
  `TMX-REL-2013-10-07` (Thanksgiving 2013-10-14, CNW 513069561),
  `TMX-REL-2013-12-03` / `TMX-REL-2014-12-02` / `TMX-REL-2015-12-01` /
  `TMX-REL-2016-11-30` (the year-end Holiday Operating Schedules, CNW
  513358771 / 516597231 / 559634691 / 603757686), and the 2014 Civic/Labour/
  Thanksgiving corroborations (CNW 515176451, PRN 515357461, CNW 515686301).
  The 2015-03 and 2016 releases' own "online schedules" pointers witness the
  tsx.com calendar-page URL of the era.
- **`tsx-calendarevents.wayback-20150315063450id_.html`** — the tsx.com
  "Calendar & Events" page (`calendar-and-events`, the calendar page's 2015
  URL, visible in the prior sweep's own `cdx-tsx_com-all.json` but never
  fetched) prints the **complete 2015 and 2016 "Stock Market Holidays - Stock
  Markets Closed" lists**. That is the evidence file's named closing
  condition for 2015-2016. The prior pass's domain-wide `holiday` filter
  missed it because the URL says `calendar`.
- **`tmxmoney-market-hours.wayback-20140109054747id_.html`** — TMX Money's
  own "Market Hours & Holiday" page prints the **complete 2014 list**. The
  tmxmoney.com domain was never swept before this pass.
- **The operator's own trading-notice archives (live, 2011-2016)** corroborate
  the eve halves: notice 2013-037 (2013-12-24, 13:00:00 continuous-trading
  end; saved as `tsx-notice-2013-037...pdf`), 2012-049, and archives whose
  operating-schedule changes are the 2012 and 2013 eves only — affirmative
  evidence no other schedule change was noticed 2014-2016.

**Completed negatives this pass:** Wayback month-prefix enumeration of every
missing release month (2011-11, 2011-12, 2012-01, 2013-08..2014-01,
2014-08..2014-12 — `cdx-month-*.txt`; no holiday release exists in any);
tmxgroup.com and tsx.ca domain-wide sweeps (empty/parked — `cdx-tmxgroup-*`,
`cdx-tsxca-*`); tmxmoney.com 2008-2017 history (only the pages above —
`cdx-tmxmoney-*.txt`); PR Newswire company listing (server-side pagination
caps at 2013); Mondo Visione (JS shell live; RSS captures skip the 2011
release week — `mv-rss-20120202.xml`; article `tmx-group-holiday-operating-
schedule-2` never captured; archive.today no snapshot); the 2011-12-12
release's CNW id is unguessable (migrated ids non-chronological: 2009 =
539056321 vs 2013 = 513358771) and PRN's copy predates server-side
enumeration. The 2011 span's named closing condition stands: a capture of the
2011-12-12 release (the Common Crawl batch here retries CC-MAIN-2012 for the
2011 tree; the gateway 504-degraded through 2026-10-02 — results appended
below when settled), or the operator's re-publication.

## Common Crawl batch 2 (2026-10-02, `cc2-batch-2026-10-02.log` here) — CHANNEL UNAVAILABLE

- The CC index gateway served two light probes at ~08:19-08:20 UTC (a
  control `nzx.com/*` query in CC-MAIN-2016-50 returned rows; a real
  `nzx.com/announcements/*` query in the same collection returned its
  settled "No Captures found" zero — recorded on the NZX side) and then
  degraded: every collection 2013-20..2017-22 now 504s on even a trivial
  one-row query (probes repeated 09:1x-09:2x UTC; 10.6 s server-side
  timeouts). CC-MAIN-2012's index endpoint answers 502 persistently — the
  legacy collection is not served by the current gateway at all, so the 2011
  news tree is unreachable in CC today by construction, not by crawl gap.
- Every named lookup therefore remains **re-runnable, not settled**: the
  2013-48 `2013/*`, 2014-10 `2013/*`+`2014/*`, 2014-49 `2013/*`+`2014/*`,
  2015-48/`2016-30` tsx.com sweeps, and the calendar-and-events Q4-state
  sweep. The query lists and the retry-wrapped runner are preserved at
  `/private/tmp/hunt-tsx-nzx/{tsx,nzx}-queries.txt, cc-batch.sh`. This does
  not affect the encoded rows: the recovered wire mirrors and page states
  are live-retrieval T1 artifacts independent of CC.

## Hunt round 3, 2026-10-03 UTC — the 2011 span CLOSES; rows shipped

The **2011-10-11..2012-01-02 span closes**. The untried angles found the
release.

**The recovery.** Mondo Visione's current CMS re-imports its pre-2025
articles under date-suffixed slugs (`<slug>-<YYYYMMD>`, e.g. the 2010
schedule at `tmx-group-holiday-operating-schedule-2011124`), while the old
slugs (`...schedule-2`) serve identical 15 590-byte JS shells. The site's own
paginated news index still reaches December 2011 (`?page=14956` holds
12/12/2011) and names the re-imported edition at
`tmx-group-holiday-operating-schedule-1-20111212` — served **live with the
release text in full**:

> TMX Group Holiday Operating Schedule. Date 12/12/2011. Toronto Stock
> Exchange, TSX Venture Exchange, Montréal Exchange and TMX Select will be
> closed on Monday, December 26, 2011 in lieu of Christmas Day, Tuesday,
> December 27, 2011 in lieu of Boxing Day, and Monday, January 2, 2012 in
> lieu of New Year's Day. … Friday, December 23, 2011 Open until 4:00 p.m.
> (EST) (TMX Select will be open until 5:00 p.m. EST) …

Saved as `mv-tmx-rel-2011-12-12.live-2026-10-03.html` (sha in
SHA256SUMS.txt). **Verbatim-ness pinned**: the same site's 2016-11-30 edition
(Wayback `20161201141300` capture, `mv-tmx-rel-2016-11-30.wayback-*.html`)
reads word-for-word against the operator's own CNW wire mirror
`cnw-tmx-rel-2016-11-30-...-603757686.html`. Dec 23's printed 4:00 p.m. close
is the regular close, so no early-close row exists for 2011.

**Completed negatives this round (all 2026-10-03 UTC):**

- Common Crawl for the `-2` article URL (`matchType` prefix): settled
  "No Captures" in CC-MAIN-2013-20, 2013-48, 2014-10, 2014-35, 2014-41,
  2014-49, 2015-48, 2016-30, 2021-10, 2021-31, 2022-33, 2023-50;
  CC-MAIN-2021-49, 2022-05, 2023-14 stay gateway-dead
  (`cc-mv-probe-2026-10-03.log`).
- Wayback domain-wide `tmx.*holiday.*` variant sweep and Nov-2011..Mar-2012
  domain census (`cdx-mv-domain-nov2011-mar2012.txt`): the MV article family
  `-7..-12`, `-2025123` and `tmx-group-thanksgiving-holiday-market-closures-*`
  are captured WITH content; `-2`..`-6`, the unsuffixed schedule and every
  slug variant of the 2011 edition are not.
- Mondo Visione live: `-2`, `-7`, `-12` serve byte-identical 15 590-byte
  shells (content removed site-wide after the 2021-11-30 `-12` capture);
  Googlebot UA returns the same shell; no article-body AJAX endpoint exists
  in `_js/dev.js`/`_js/javascript.js`.
- CNW date-ranged site search ("TMX Group Holiday", 2011-12-01..2012-01-31):
  "No result". PR Newswire's own copies: id 284455561 = the 2014-12-02
  edition (saved); the 2011 edition is not indexed under any guessable id.
- investors.tmx.com (the Q4 IR site, live since 2022, Cloudflare-blocked to
  non-browsers): its `news-details` family and s21.q4cdn.com host the 2016+
  editions; no 2011 page is indexed or captured (`cdx-investors-tmx-all.txt`,
  `cdx-ir-newsdetails.txt`). TMX Group's 2011 annual report carries no
  trading calendar (financial document; also unreachable on SEDAR+ without a
  browser session).
- Search-engine corroboration only (T4, recorded here, keys nothing): the
  search index snippet for the `-2` URL printed the same sentence the
  recovered mirror states.

Files added this round: `mv-tmx-rel-2011-12-12.live-2026-10-03.html`,
`mv-tmx-rel-2016-11-30.wayback-20161201141300id_.html`,
`mv-tmx-rel-2021-11-30.wayback-20211130145249id_.html`,
`mv-tmx-rel-2011-12-12.oldslug-shell.live-2026-10-03.html`,
`cdx-mv-domain-nov2011-mar2012.txt`,
`mv-news-index-p14956.live-2026-10-03.html`, `cc-mv-probe-2026-10-03.log`,
`cdx-investors-tmx-all.txt`, `cdx-ir-newsdetails.txt`,
`prn-tmx-rel-2014-12-02-284455561.wayback-20150426172357id_.html`.
