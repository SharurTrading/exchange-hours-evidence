# INDEX — wave-c2-2012-notices (the 2012 leg of the carried-normal-week no-changes sweeps)

Retrieval performed 2026-10-05 (UTC) from this machine, as Internet Archive
`id_` raw replays of `http(s)://www.cmegroup.com/tools-information/lookups/advisories/electronic-trading/<yyyymmdd>.html`
(the operator's own weekly CME Globex Notices channel; cmegroup.com serves an
anti-scraping block directly). The wayback timestamp is the capture time (UTC);
the notice's own date is its filename. Tier: T1 throughout. sha256 in
`SHA256SUMS.txt`. Purpose: the 2026-10-05 carried-class no-changes verification
(the maintainer's directive of that date) — the interval 2012-01-01..2012-05-28
swept for **any declared trading-hours change** to the energy/metals, FX and
grain families (the 2010-2011 leg of the sweep is `wave-c1/cme-notices/`, the
2026-09-30 retrieval, re-scanned in the same pass).

## Files

25 of the 26 weekly notice files of 2012-01-02..2012-05-28 are held and were
text-scanned in full (title sweep + per-family keyword sweep + full reading of
every hours-titled section). One is unread: `20120221.html` — the archive holds
exactly one capture (20190822132019), which replays to an HTTP 302 whose target
serves zero bytes in every form tried (the 2026-10-05 sweep and two retries).
Its week is covered by the readable `20120220.html` (the notices repeat
standing content across adjacent weeks throughout the series).

## What the sweep found (all of it already encoded or out of family scope)

- `20120326`/`20120402`/`20120409` — "Trading At Settlement (TAS) Pre-Open
  Timing Changes" effective **Sunday, April 15** (trade date Monday, April 16):
  market pause at 16:15:00 Sunday and 16:45:00 Mon-Thu; TAS groups pre-open
  Sundays 16:15:00-16:16:00 CT, Mon-Thu 16:45:00-16:46:00 CT. TAS products are
  excluded from the served family scopes; the notice is the dated market-state
  statement of the old Sunday 16:15 / weekday 16:45 platform pre-open values
  already cited by the #79 record.
- `20120507`/`20120514`/`20120518`/`20120521` — "Expanded Trading Hours on
  CBOT Commodity, KCBT, and MGEX Grain and Oilseed Futures and Options",
  effective Sunday 2012-05-20 (trade date Monday 2012-05-21) — the grains
  family's dated 2012-05-20 revision, already encoded.
- No notice in the window declares any change to the NYMEX/COMEX energy and
  metals or the standard-grid FX futures normal week (every product-complex hit
  is a listing rule, symbol change, match-algorithm change or fee/filing item,
  none of which is session language).
