# sgx_securities — domain-lineage sweep, 2026-10-06 UTC

The maintainer's domain-lineage ask for #213's two spans (2011-2013 and
2020-2024): the untried predecessor domains. **Verdict: NEGATIVE — no operator
artifact dated inside either span surfaces on any of them.**

## Domains enumerated (CDX, 2026-10-06 UTC, outputs saved below)

- **ses.com.sg** (the pre-SGX Stock Exchange of Singapore name) — the
  `holiday|calendar|trading` urlkey filter, 1998-2016: exactly three rows,
  all year-2000 SES-era pages (`html/dtTradingInf.htm`, `sgxdtTradingInfo.htm`,
  `sgxdtTradingSys.htm`, captures 2000-05/08). Pre-floor observations of a
  predecessor market; nothing inside or near either span.
- **info.sgx.com** — full domain enumeration 2000-2016 (8,000-urlkey cap):
  the Lotus-Notes application family (`serviceapp.nsf` 4,987 keys —
  derivatives service app; `listprosp.nsf` 2,450 — issuer prospectuses;
  `webcorannc*.nsf` — corporate announcements; `agmcalendar.nsf` — company
  AGMs; `DT-EventsCal.nsf` — derivatives-seminar events). The
  `holiday|calendar|trading` urlkey filter (76 rows, saved) shows the
  trading-calendar documents the channel once carried:
  `SGXWeb_DC.nsf/.../$FILE/Trading%20Calendar%202009.pdf` (capture
  2009-01-26 — fetched below; a **derivatives-market** calendar, per-product
  day codes) and `SGXWeb_ST.nsf/DOCNAME/ST_Trading_Calendar` (2007-05, the
  securities-trading calendar page). **No calendar-named artifact in
  2011-2013** (the domain's latest capture is 2013-10-29, a prospectus PDF)
  and nothing at all in the 2020s.
- **sgx.com/others/** — prefix enumeration: **zero captures**.
- The WCM sibling trees were already exhaustively filtered in the store's
  `hunt-3-2026-10-03/` pass (35 status-coded rows, all accounted for); this
  pass adds no new row.

## Sharpened closing condition (unchanged in substance)

The derivatives-scoped genre finding is new: SGX's own Lotus doc channel
carried `Trading Calendar <year>.pdf` documents through 2009 and they print
per-product derivatives day codes — so a calendar PDF that closed #213 would
have to be an SGX-ST securities-market schedule; the group's derivatives
calendars, even if an edition surfaced for 2011-2013 or 2020-2024, would not
key securities rows. The ask remains one **securities-market** operator
artifact dated inside a span (the #213 record's wording).

## Fetch

- `sgx_info_TradingCalendar2009.wayback-20090126233130.pdf` — "SGX Derivatives
  Market Trading Calendar" (15 pages, Dec-2008/2009 grids), retrieved from the
  Wayback `id_` replay of capture 20090126233130. Pre-floor, derivatives
  scope; keys nothing; genre witness. sha256 in SHA256SUMS.txt.
