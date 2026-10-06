# iceus — domain-lineage sweep, 2026-10-06 UTC

The maintainer's domain-lineage ask for the ICE Futures U.S. block: the
January-2010..July-2011 baseline gap (six ice_us* keys; the master hours
table's earliest surviving edition is AUGUST 2011, captured 2011-12-12) swept
across the lineage's untried domains. **Verdict: NEGATIVE — the terminal-answer
conclusion in `docs/evidence/ice_us_sugar.md` stands; no artifact dated inside
the carried span states any softs hours.**

## Domains enumerated (CDX, collapse=urlkey, saved below)

- **theice.com** `trading_hours|tradinghours|trading-hours` urlkey filter,
  2009-2013 (12 rows): the known master table (`ICE_Futures_US_Regular_Trading_Hours.pdf`,
  first capture 2011-12-12), the two dated hours-change notices already cited,
  the USGrains (Europe) hours PDF, Canada member notices, and the marketdata
  `Calendar{List,View}.shtml?...calendar=SpecialTradingHours&markets=ICE+Futures+U.S.`
  pages (captures 2011-10-16, 2011-12-08, 2011-12-13).
- **theice.com** `hours` urlkey filter, 2009-2013 (22 rows): adds
  `productguide/Search.shtml?tradingHours=` (2011-10-16, an empty-search
  shell), the productguide `Hours.2` 404s, and
  `publicdocs/regulatory_filings/12-1_Sugar_trading_Hours.pdf` — the CFTC
  submission no. 12-1 of 2012-01-10 for the 2012-01-30 sugar hours change
  (fetched; corroborates the existing 2012-01-30 revision row, post-dates the
  master table, keys nothing for the carried span) and the 12-8 DST weekly
  notification.
- **theice.com/productguide/** prefix, 2009-2013 (5,000-row cap hit): the
  contract-spec family. `DelayedData.shtml?specId=N` product pages first
  appear 2011-11-20; `products/*.jhtml` (the 2026-09-30 sweep's finding) first
  appear 2012-06-10. The ONLY pre-2011-08 productguide captures are
  `ExpiryDates.shtml?specId={0}` template-URL crawls (2011-05..2011-07) whose
  URLs carry a literal `{0}` — no real product page. No spec or hours page
  survives dated inside 2010-01..2011-07.
- **theice.com** `contract|spec` urlkey filter, 2009-2012 (3,000-row cap):
  images, 404 shells and the marketdata calendar rows above; nothing new.
- **nybot.com** `hours|trading` urlkey filter 2007-2014 (18 rows) AND the full
  domain enumeration 2009-2013 (218 rows): the 2007-era
  `marketInfo/tradingSchedule/indexTradingSchedule{,Electronic}.htm` pages are
  pre-floor observations (2007-02; a capture dates the observation, never the
  state), and **every 2009-2013 nybot.com row is a 301/302 redirect or an
  image — zero 200-status captures in the whole window**. The nybot.com
  channel is dead in the gap era.

## Fetches (all Wayback `id_` replays, 2026-10-06 UTC)

- `ice_12-1_Sugar_trading_Hours.wayback-20120610064849.pdf` — CFTC submission
  12-1 (2012-01-10), Change of Electronic Trading Hours for Sugar No. 11:
  restates the 2012-01-30 move to a 01:30 NY open the module already carries.
  sha256 in SHA256SUMS.txt.
- `ice_marketdata_CalendarList.wayback-20111016123256.html` and
  `ice_marketdata_CalendarView.wayback-20111213000240.html` — the operator's
  own Holiday/Special-Trading-Hours calendar pages: the captured bytes carry
  the navigation shell only; the event data renders client-side, so no
  2010-2011 special-hours event survives in them.
