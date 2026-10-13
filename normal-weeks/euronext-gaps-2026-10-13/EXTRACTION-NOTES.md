# Extraction notes — the Euronext gap wave (Amsterdam derivatives floor; 2026 year-end instants; 2027 calendars)

Retrieved 2026-10-13T23:25Z–2026-10-14T00:10Z (UTC) from this machine. Every
Wayback artifact is an `id_` raw replay; the wayback timestamp in each filename
is the **capture** time (UTC) and dates the observation it prints, never a
state (LAW-NO-FABRICATED-DATES). Live retrievals are stamped in their
filenames. Tier: T1 throughout — every artifact is the operator's own page,
press release or portal (euronext.com, globalderivatives.nyx.com, nyx.com,
meff.es), including the corporate parent's own holidays-and-hours pages.

---

## Target 1 — the Amsterdam (AEX) derivatives grid at/near the 2010 floor

### 1.1 `amsterdam-floor/NYSE_Liffe_to_extend_AEX_index_futures_opening_hours.pdf`

- Source URL: `https://www.euronext.com/sites/www.euronext.com/files/NYSE_Liffe_to_extend_AEX_index_futures_opening_hours.pdf`
- Wayback `id_` replay of capture `20181107205935`, retrieved 2026-10-13T23:32Z.
- sha256 `85abac4b4709e4cfec6e9e80f191bd9d18020555f89752b77773d8e23697cf07`.

What it witnesses (session language throughout — "extend trading hours",
"close of 11.15hrs", "trade until"):

> NEWS RELEASE — For immediate release — Monday 3 August 2009
> NYSE LIFFE TO EXTEND AEX INDEX FUTURES OPENING HOURS
> Contract can now be traded throughout the US trading day

> "NYSE Liffe, the Europe-based derivatives business of NYSE Euronext (NYX),
> has announced that it will extend trading hours in its AEX index futures
> contract from the current close of 11.15hrs until 15.00hrs Chicago time,
> with immediate effect, enabling US-based customers to trade the contract
> throughout their normal working day."

> "The 3 ¾ hour extension will bring the contract's closure into line with
> NYSE Liffe's FTSE 100 and CAC 40 index futures which already trade until
> 15.00hrs Chicago time."

Reading, strictly bounded:

- **Pre-floor close witnessed:** as of 3 August 2009 the AEX index futures
  trading day closed at **11.15hrs Chicago time** — the operator's own
  statement, dated six months before the 2010 floor. All times in this
  document are **Chicago-anchored**; no Amsterdam-local instant is printed,
  and none is derived here (a Chicago-to-Amsterdam conversion depends on the
  DST alignment of each specific date, which the document does not address).
- **Dated change:** "with immediate effect" on a release dated **Monday
  3 August 2009** — an unconditional day-level operator statement (the
  extension takes effect that day), so the close moves to 15.00hrs Chicago
  time from 2009-08-03 if the change is encoded.
- **Alignment clause:** from that day the AEX futures closure matches the
  FTSE 100 and CAC 40 index futures, which "already trade until 15.00hrs
  Chicago time" — the operator's own statement that the Paris index-futures
  close was already at that value before August 2009.
- The **open side of the Amsterdam derivatives day is not printed** by this
  document; the floor-era open remains unsourced by this wave.

### 1.2 `amsterdam-floor/press-release-page.wayback-20220813094213id_.html`

- Source URL: `https://www.euronext.com/en/about/media/euronext-press-releases/nyse-liffe-extend-aex-index-futures-opening-hours`
- Wayback `id_` replay of capture `20220813094213`, retrieved 2026-10-13T23:30Z.
- The live euronext.com press-release archive's page for the same release —
  found via a CDX host sweep for `.*hour.*` on `www.euronext.com` (the files-dir
  PDF above and this page are two lives of one document). Its body repeats the
  1.1 sentences verbatim ("from the current close of 11.15hrs until 15.00hrs
  Chicago time, with immediate effect"; "already trade until 15.00hrs Chicago
  time"; dateline "Amsterdam, Brussels, Lisbon, London, Paris, New York,
  3 August 2009"). It is the stable live citation for the PDF.

### 1.3 `amsterdam-floor/nyseliffe-calendars-hours-nl.wayback-20111126202420id_.html`

- Source URL: `http://globalderivatives.nyx.com/nl/nyse-liffe/trading-hours`
- Wayback `id_` replay of capture `20111126202420` (the page's **only** 200-status
  capture; all later captures are 302s), retrieved 2026-10-13T23:48Z.
- Page title path: "NYSE Liffe > Market Information > Exchange Trading Calendar
  and Hours", heading "Calendars & Hours". This is the operator's own NYSE
  Liffe derivatives calendar-and-hours page (the nl locale — the locale the
  parent site's NYSE Liffe holidays page labels "Amsterdam & Brussels
  Markets", see 1.5).

What it witnesses:

- **2011 derivatives holiday list** (session-day language "will be open"):
  > "NYSE Liffe's Derivatives markets will be open Monday to Friday throughout
  > 2011 except on the following days: 2011 — Good Friday 22 April — Easter
  > Monday 25 April — Public Holiday 26 December 2011"
- **2011 year-end derivatives treatment** (session language "will be
  available for trading", "will be open for a full day"):
  > "On Friday, 23 December 2011 and Friday, 30 December 2011, trading on the
  > Cash markets will close at 5.35 pm CET. In line with the underlying cash
  > markets, contracts on the Derivatives market will be available for trading
  > as follows: … and Continental and U.S. Individual Equity Futures and
  > Options contracts and Index Products (excluding the FTSE 100 and FTSE 250
  > Index contracts) will be open for a full day."

  AEX index futures are the Continental market's "Index Products", so the
  operator states **a full trading day** for them on both 2011 eves — a
  derivatives-leg year-end witness (the 2011 cash rows in the crate close at
  17:35 CET; the derivatives leg prints no early close for Amsterdam).
- **The documents the page links for the actual hours grids** — every one of
  them has **zero Wayback captures** (checked per URL and via a domain-wide
  `*.pdf` CDX sweep of `globalderivatives.nyx.com`, 387 urlkeys; see the
  search record below):
  - "LIFFE CONNECT® trading hours — 21 Nov 2011" →
    `…/files/liffeconnect_tradinghours211111.pdf`
  - "Trading Hours: 23 December 2011 to 2 January 2012 — 09 Nov 2011" →
    `…/files/lon3526_0.pdf` (London Notice No. 3526)
  - "London Notice No. 3351 — Trading hours: 24 December to 3 January 2011" →
    `…/files/608001.pdf`
  - "Appendix aan de trading manuals NSC (datum van inwerkingtreding: 1 juni
    2009) en Universal Trading Platform (datum van inwerking 21 Jul 2009)" →
    `…/files/509415_0.pdf` — a **2009** trading-manuals appendix, i.e. exactly
    the genre that could state the floor-era grid, unarchived.
- The page prints **no times inline** (a grep for `\d\d:\d\d` over the raw
  bytes returns nothing); the grid lived entirely in the PDFs above.

### 1.4 `amsterdam-floor/nyseliffe-calendars-hours-en.wayback-20110710100224id_.html`

- Source URL: `http://globalderivatives.nyx.com/en/nyse-liffe/trading-hours`
- Wayback `id_` replay of capture `20110710100224` (200-status; the en locale
  has 20110710, 20110908, 20111109, 20120612, 20140727 captures), retrieved
  2026-10-13T23:55Z.
- Same page generation as 1.3, five months earlier. The holiday/EOY prose is
  **word-for-word the 2011 text** quoted in 1.3. It links the **earlier
  edition** of the hours document: "LIFFE CONNECT® trading hours — 01 Jul
  2011" → `…/files/507371_1.pdf` — also **zero Wayback captures**. Same
  notices list (3351/3372/3395).

### 1.5 `amsterdam-floor/nyx-holidays-and-hours-nyse-liffe.wayback-20120411150803id_.html`

- Source URL: `http://www.nyx.com/en/holidays-and-hours/nyse-liffe`
- Wayback `id_` replay of capture `20120411150803` (earliest capture of this
  path; 200 status), retrieved 2026-10-13T23:42Z.
- The parent operator's (NYSE Euronext's own corporate site) NYSE Liffe
  holidays-and-hours page. What it witnesses:

- **2012 derivatives holiday list**:
  > "NYSE Liffe's Derivatives markets will be open Monday to Friday throughout
  > 2012 except on the following days: 2012 — Good Friday Friday 6 April —
  > Easter Monday Monday 9 April — Labour Day 1 Tuesday 1 May — Christmas Day
  > Tuesday 25 December — Boxing Day Wednesday 26 December 2012"
- **2012 year-end derivatives instants** (session language "trading will be
  aligned", "the Exchange will commence the closing of its derivatives
  contracts from"):
  > "On Monday 24 December 2012 and Monday 31 December 2012 trading will be
  > aligned with those of the underlying and, where appropriate, related
  > markets. On these days the Exchange will commence the closing of its
  > derivatives contracts from midday GMT (13.00 hours CET)."

  This is a derivatives-leg year-end instant for 2012-12-24 and 2012-12-31:
  the closing of derivatives contracts **commences at 13:00 CET** (midday GMT
  as printed) — earlier than an ordinary day and stated as a commencement
  time, not an order-entry cutoff or a per-product expiry.
- **UK-only holiday carve-out** (negative rows for Amsterdam: those days are
  expressly sterling/London-commodity-only):
  > "On 2 January, 7 May, 4 June, 5 June and 27 August 2012, which are public
  > holidays in the United Kingdom, it is anticipated that NYSE Liffe's
  > sterling-based products and London-based Commodity contracts will not be
  > made available for trading, but other products will be available."
- **Per-market pointers** (the labels are the parent site's own routing):
  > "For more information please see: Amsterdam & Brussels Markets —
  > http://globalderivatives.nyx.com/nl/nyse-liffe/trading-hours; Lisbon
  > Market — …/pt-pt/…; London Market — …/en/…; Paris Market — …/fr/…"
  This is what fixes the nl-locale pages 1.3/1.4 as the Amsterdam (& Brussels)
  view of the derivatives calendar.

### 1.6 `amsterdam-floor/nyx-holidays-and-hours-euronext.wayback-20120411182349id_.html`

- Source URL: `http://www.nyx.com/en/holidays-and-hours/euronext`
- Wayback `id_` replay of capture `20120411182349` (earliest capture of this
  path; 200 status), retrieved 2026-10-13T23:42Z.
- The parent operator's Euronext cash holidays-and-hours page. What it
  witnesses (2012 — after the floor, so it **corroborates** the legacy grid
  between the floor and 2013 but does **not** meet the crate's stated closing
  condition, which requires a document dated in or before January 2010):

  > "Official Trading Hours (CET) — Continuously-traded securities 09:00-17:30
  > — Trading at Last (TAL) Phase 17:35-17:40 — Double auction-traded
  > securities - Brussels, Lisbon, Paris and Amsterdam 11:30-16:30* — Trade
  > Confirmation System (TCS) reporting tool for off-order book trades
  > 07:15-19:00 — Note: *For auction-traded securities, orders are managed
  > through an order book that operates continuously from 07:00 to 18:00, but
  > are matched just twice daily."

  Caution flags for any consumer of this print: the "09:00-17:30" /
  "17:35-17:40" rows are the continuous-trading and TAL phases of the legacy
  cash grid (matching `euronext_amsterdam`'s ledger basis); the **07:15 row is
  the Trade Confirmation System reporting tool — a reporting window, not a
  trading phase** (LAW-SESSION-NOT-EXPIRY: it must not be read as the
  pre-opening); the "07:00 to 18:00" in the note is the double-auction order
  book's management window, with matching only twice daily.
- **2012 cash holidays and the 2012 eves** (session language "will close at"):
  > "NYSE Euronext European Cash Markets are open from Monday to Friday
  > throughout the year, except for the days listed below: 2012 — Good Friday
  > April 6 — Easter Monday April 9 — Labour Day May 1 — Christmas Day
  > December 25 — Boxing Day December 26"
  > "On Christmas Eve, Monday 24 December 2012, and New Year's Eve, Monday 31
  > December 2012, the markets will close at 14:00 CET."

  The 14:00 CET eve close agrees with the crate's 2012 rows
  (`EURONEXT-TC-2012`) — corroboration only; those rows already key from the
  operator's notice.

### 1.7 Verdict for Target 1

- **FOUND (partial):** floor-era **derivatives** session-language statements —
  the 2009-08-03 AEX index futures close (both values, unconditional
  day-level change) and the 2011/2012 derivatives year-end and holiday
  statements (1.1–1.5). The 2009 document is the first artifact this store
  holds that is **dated inside the pre-floor era** and speaks to the
  Amsterdam derivatives day.
- **NOT FOUND:** the Amsterdam derivatives **normal-week grid** (open time and
  local-day close) at/near the floor. The operator's own grid documents are
  named by the archived pages (1.3/1.4) but are absent from the archive:
  `507371_1.pdf` (2011-07-01), `liffeconnect_tradinghours211111.pdf`
  (2011-11-21), `509415_0.pdf` (the 2009 trading-manuals appendix),
  `608001.pdf`/`lon3526_0.pdf` (London Notices 3351/3526). Closers, in order
  of promise: (a) the LIFFE CONNECT trading-hours PDF editions or the 2009
  trading-manuals appendix, from any member-firm archive or the operator on
  request; (b) a Wayback rescan — the archive grows; (c) the parent site's
  per-market "Trading hours / products groups" tab content, which the
  quicktabs URLs suggest existed but which was never captured.
- The cash-side closing condition of `euronext_amsterdam.md` (a document dated
  in or before January 2010 printing the legacy 07:15/09:00/17:30/17:40 grid)
  remains unmet: the earliest normal-grid witness this wave could find is the
  2012-04-11 nyx page (1.6), which corroborates the 09:00-17:30/TAL
  17:35-17:40 phases but postdates the floor by two years and does not print
  a pre-opening phase.

---

## Target 2 — the December 2026 year-end instants (Amsterdam/Paris; BME/Madrid)

### 2.1 Euronext — NOT YET PUBLISHED (fresh negative, 2026-10-13 UTC)

- Artifact: `year-end-2026/euronext_trading-hours-holidays.live-20261013T2345Z.html`
- Source URL: `https://live.euronext.com/en/resources/trading-hours-holidays`
- Retrieved live 2026-10-13T~23:45Z; sha256
  `81434fa4d875ab8c8e4b596000bc3975efb8a799748ee38f732f15cf6b0208a7`.
- The page carries a dedicated view titled **"2026 end of year Trading
  hours"** whose callout body prints **"To be announced"** — the 2026
  end-of-year appendix has not published. The page's standing prose names the
  closer and the channel:
  > "End of year trading hours, including half day trading, will be announced
  > in an end of year appendix to the Euronext Instructions 4-01 4-03 Trading
  > Manuals."
- No appendix link exists in the 2026 view (its only document links are the
  standing "Cash markets trading hours" (`euronext.com/en/media/1927/download`,
  an XLSX — the current Appendix of Trading Manual 4-01, already cited by the
  crate under its `2026-07/appendix…xlsx` path) and "Derivatives markets
  trading hours" (`euronext.com/media/295/download` — **a stale URL that now
  serves a JPEG**, recorded so nobody cites it as the derivatives grid).
- This extends the crate's 2026-10-09 re-check (Paris evidence file) by four
  days. The 2024 and 2025 appendices the crate already holds were published as
  `media/12642/download` and `media/14656/download`; the watch action is to
  re-read this page for a new "2026 end of year" download link (and to sweep
  `euronext.com/media/<n>/download` growth) — in recent years the appendix
  existed well before the eves, but no earlier-than-October publication is
  witnessed by the artifacts this store holds.

### 2.2 BME cash — FOUND (already banked; identified and quoted here)

- Artifact (pre-existing store artifact, not re-fetched by this wave):
  `normal-weeks/meff-ibex-2026-10-11/bme-2026-calendar-release.html`
- Page identity (from its own canonical/og:url tags):
  `https://www.bolsasymercados.es/en/media/press-releases/2025/spanish-financial-markets-2026-trading-calendar.html`,
  H1 "Spanish Financial Market's 2026 Trading Calendar", page-dated
  **2025-11-20**. Session language ("open until"):
  > "On Thursday, 24 December and Thursday, 31 December, the market will be
  > open until 2:00 pm."
  Both eves are weekdays in 2026 (Thu), so the BME cash envelope for
  2026-12-24 and 2026-12-31 is the printed 14:00 local close.

### 2.3 MEFF (BME derivatives) — calendar note FOUND live; the MEFF EOY
comunicado NOT YET PUBLISHED

- `year-end-2026/meff_trading-calendar.live-20261014T0005Z.html`
  (`https://www.meff.es/ing/Trading-Calendar`, retrieved live
  2026-10-14T~00:05Z; sha256
  `9650351f4b8e0f2c7fca604247ca4a5f6b2774f2151e1a62eceac9ba2826ac1b`) — the
  operator's own derivatives-market calendar page for the current year prints:
  > "Note: On 24 and 31 December the BME markets will trade until 14:00 hrs
  > CET."
  Session language ("will trade until 14:00 hrs CET"). The page carries **no
  year label beyond 2026 references** (three "2026" strings, zero "2027"), so
  the note is read as covering the calendar the page serves (2026).
- `year-end-2026/meff_market-notices.live-20261014T0000Z.html`
  (`https://www.meff.es/ing/Financial-Derivatives/Market-Notices`, retrieved
  live 2026-10-14T~00:00Z; sha256
  `42b0f5fd208b29d506baee8095ba120ac7bd2c47bebdf8d66a351bf7b5aa26c2`) — the
  full 2026 notice list (notices 2601–2618 plus GEN01/02-26, newest
  24/09/2026) contains **no** "Horario de las sesiones 24 y 31 de diciembre"
  comunicado yet. The genre and its timing are witnessed by the two banked
  prior editions: MEFF 14/2024 (2024-06-14) and MEFF 49/2025 (**2025-11-07**),
  each printing "el mercado cerrará a las 14:00h" for the two eves. Expected
  publication: **early November 2026**; watch the Market Notices page.

---

## Target 3 — the 2027 holiday calendars

### 3.1 Euronext — NOT PUBLISHED (fresh negative, 2026-10-13 UTC)

- Artifact: the same live read as 2.1. The string **"2027" does not occur
  anywhere** in the served HTML (zero occurrences); the newest calendar the
  page links is the 2026 one ("2026 Holiday Calendar for Euronext's Cash and
  Derivatives markets"). This re-confirms the crate's 2026-09-29 negative.
- Channel and expected timing: the operator publishes the next year's
  "Holiday Calendar for Euronext's Cash and Derivatives markets" as an
  INFO-FLASH of the CADE series that lands on this page; the operator's own
  file naming dates the series at **mid-October to early November** of the
  preceding year (banked editions `if171020cade` = 2017-10-20 and
  `if181018cade` = 2018-10-18 in the store's holiday raw set;
  `IF251107CADE…2026 Holiday Calendar…` = published path `2025-11/`). So the
  2027 calendar is due **within days to weeks** of this read; watch the live
  page and the `connect2.euronext.com/sites/default/files/2026-10|2026-11/`
  INFO-FLASH store.

### 3.2 BME/MEFF — NOT PUBLISHED

- The live MEFF Trading Calendar read (2.3) has **zero "2027"** occurrences;
  the banked BME press-release series dates the "Spanish Financial Market's
  20XX Trading Calendar" release at **~20 November of the preceding year**
  (the 2026 edition: 2025-11-20). Expected: a
  `bolsasymercados.es/en/media/press-releases/2026/…2027-trading-calendar…`
  release around late November 2026, and a MEFF calendar page turn.

---

## Search record (channels checked, bounded, 2026-10-13T23:25Z–2026-10-14T00:10Z UTC)

Negatives recorded so the next hunter does not re-walk them:

- `nyseeuronext.com` (domain, 2007-2014): 13 urlkeys, all 302 redirects or
  404s — the domain never served archived content.
- `euronext.nl` (domain, 2009-2013): 12 urlkeys, all 302s.
- `liffe.com` (domain, 2009-2013, 659 urlkeys): content pages are data-file
  specifications (the 2009 spec-index page prints settlement/price-history
  file layouts only); the 2009 homepage meta-refreshes to
  `http://www.euronext.com/derivatives`. No trading-hours grid page.
- `euronext.com/derivatives/`: a single 2008-06-18 capture that replays as the
  site's error page.
- Old-site trader portal (`euronext.com/trader…`, ~1,500 200-status urlkeys):
  instrument quote pages only; no static hours pages.
- `euronext.com/sites/www.euronext.com/files` (full paginated CDX sweep,
  13,465 urlkeys incl. all late captures): the hours-named PDFs are only the
  six under `.*trading_hours.*` (fund-service, cash, warrants & certificates
  for 24/31 Dec 2010; 2013 cash eves; 2018 UTP all-markets; 2018/19
  derivatives eves `no181204de`) — no derivatives normal-week grid before
  2013. The derivatives-leg holiday-calendar genre starts at
  `if131210cade` (the 2014 cash + continental-derivatives calendar).
- `globalderivatives.nyx.com` trading-hours pages: nl/en/fr locales captured
  2011-2014 (list in INDEX); every hours PDF they link has zero captures;
  the `?quicktabs_…` tab variants of the trading-hours pages were never
  captured; `nyx.com` mirror paths for those PDFs: absent.
- `nyx.com/en/holidays-and-hours/…`: earliest captures of the `/euronext`
  and `/nyse-liffe` children are 2012-04-11 (both banked above); the parent
  `/en/holidays-and-hours` earliest is 2012-04-07.
- `nyx.com` domain sweep for `.*hours.*`: the pages above plus US-venue
  children only; no European hours page beyond these.
- Live `euronext.com/media/295/download` ("Derivatives markets trading
  hours" card): serves a JPEG — stale link, do not cite it as the
  derivatives grid.
