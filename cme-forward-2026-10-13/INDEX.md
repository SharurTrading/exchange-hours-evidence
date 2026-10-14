# INDEX — cme-forward-2026-10-13 (CME Group forward-monitoring wave: 2027 calendar, 2026 errata, hours-change notices)

Retrieval performed 2026-10-13T23:29..23:38Z from this machine. Unlike every
earlier CME wave, **cmegroup.com was read directly through a real browser
session** (the site's Akamai block is IP/fingerprint-level and still refuses
curl from this machine, but the in-app browser passes), so these are the
operator's own live bytes at tier T1 (pages, notices) and T2 (the
`trading-hours-by-product` service), saved verbatim. This closes the
"re-verify from a direct retrieval when one becomes possible" condition
recorded in `docs/schedules/sources.md` (US-CME-GROUP channel limit notes).

Baseline compared against: exchange-hours-rs branch `close_gaps` at `908b7f3`
(the 1.1.0 release), whose CME-family tables ship audited holiday windows
through **2027-12-31** sourced from live retrievals of the same service on
2026-09-12 (`CME-SVC-*` rows in `docs/evidence/cme.md`).

## Verdict summary

1. **2027 calendar: published, and already captured by the crate.** The
   operator's holiday & trading-hours calendar page
   (`/tools-information/holiday-calendar.html`, which redirects to
   `/trading-hours.html`) publishes the 2027 Globex calendar as Holiday Notes
   for every 2027 holiday plus the interactive per-date table fed by the same
   T2 service the crate cites. All fourteen re-pulled service windows
   (remaining 2026 plus every 2027 holiday window) are **byte-identical** to
   the 2026-09-12 retrievals the crate's evidence files record — zero errata.
   Spot semantic checks (Juneteenth 2027, Christmas 2027) reproduce the shipped
   venue rows.
2. **New beyond the crate's horizon: the operator's first 2028 statement.** A
   fifteenth window, `2027-12-31..2028-01-02`, plus T1 "2028 New Year's Day
   Notes" on the page. It shows an undisturbed normal grid: Friday
   2027-12-31 regular 16:00 CT close, Saturday 2028-01-01 no session, Sunday
   2028-01-02 normal reopen (16:45 preopen / 17:00 open carrying the Monday
   2028-01-03 trade date), and "December 29th TAS: Regular close per each
   product schedule" in the notes. One window is not a calendar; recorded as
   the first 2028 witness, not encoded.
3. **2026 errata: none.** Remaining-2026 windows byte-identical; the page's
   "2026 CME Globex Trading Schedule" annual table matches the shipped windows
   date for date.
4. **One NEW unmodelled arrangement for served families:** Globex notice
   20261005 (October 5, 2026) adds a **Saturday 2026-10-31 one-day extension
   of the 24/7 markets' maintenance window to 05:00 CT** (reverting to the
   02:00–04:00 standard). The crate ships the 2026-08-01, 2026-08-29,
   2026-09-19 (notices 20260727/20260824/20260831) and 2026-10-03 and
   2026-10-24 (notice 20260921) extensions for `globex_cryptocurrency` and
   `globex_event_contracts_btc`; 2026-10-31 is absent from both shipped
   tables and both evidence files. Forward-dated row candidate (the crate's
   own pattern: the two October rows from 20260921 ship forward-dated on the
   operator's statement).
5. **Hours change for an unserved product set:** Bloomberg Commodity Index and
   Subindex futures/options move to the standard Globex grid effective Sunday
   2026-10-11 (trade date Monday 2026-10-12) — SER-9808, announced in Globex
   notices 20260928 and 20261005. No crate key routes BCOM; watch-item only.
6. **Notice sweep coverage:** every CME notice published 2026-09-01 through
   2026-10-13 (index pages 1–3, 90 results) was listed; the only
   session-hours items are item 4 and item 5. Everything else is margin,
   position limits, listing/catalog or regulation business.

## Artifacts

### Operator calendar page (`trading-hours-page.html`)

| file | document | URL | retrieval (UTC) | sha256 |
|---|---|---|---|---|
| `trading-hours-page.html` | "CME Group Holiday and Trading Hours" — holiday-calendar.html redirect target; carries the 2026+2027 Globex Holiday Notes, the "2026 CME Globex Trading Schedule" annual table, the GME/FX Spot+/EBS/BrokerTec sections, and the interactive holiday table (fed by the T2 service below) | <https://www.cmegroup.com/tools-information/holiday-calendar.html> (serves <https://www.cmegroup.com/trading-hours.html>) | 2026-10-13T23:29:20Z | `a9b3c7f928c55774df09a6e2aa03732e86f342ec9b2c457c452c42f1612e6cb5` |

Note: the page states "with the 2026 and 2027 calendar year the CME Group will
be providing downloadable holiday calendars for Globex and incorporating with
Regular Trading hours into one location." No per-holiday Globex trading-hours
PDFs exist on the page; the 35 PDFs it links under
`/tools-information/holiday-calendar/files/2026/` are clearing advisories,
settlement-time tables and OTC files (clearing scope, not Globex session
hours). The Globex "downloadable calendar" is the page's own tables plus the
service JSON below. The page also carries the operator's caveat: "This
schedule is subject to change. Trading hours are usually finalized
approximately two weeks prior to the holiday."

### T2 trading-hours service re-pulls (`service/`)

Ten representative products per call (`id=316,133,425,300,58,437,22,8478,5201,10191` —
ZN, ES, CL, Corn, 6E, GC, LE, Cheese, BTC, Lumber), the exact product set the
crate's `CME-SVC-*` rows cite. Retrieval 2026-10-13T23:31Z for every file.
URL form:
`https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=<from>&toEventDate=<to>&isProtected`

| file | window (fromEventDate..toEventDate) | sha256 | matches crate's 2026-09-12 hash |
|---|---|---|---|
| `CME-SVC-2026-09-06.json` | 2026-09-06..2026-09-08 | `01fb78ffaac10eac466fed53674214222f05aed518b9d93a4b42cf8957147bca` | yes (`cme.md` row `CME-SVC-2026-09-06`) |
| `CME-SVC-2026-11-25.json` | 2026-11-25..2026-11-27 | `e1f35a5623b3c5d15e7468b2cb4119e587411a9714f920605dab11bf688756d1` | yes |
| `CME-SVC-2026-12-22.json` | 2026-12-22..2026-12-24 | `c8c0267da8cf171409ad8ca188082b3aa326e8d04a89d12503dcf9f57bf3b7ab` | yes |
| `CME-SVC-2026-12-24.json` | 2026-12-24..2026-12-26 | `bdc1fe831adb794bcf8aeb7e99baf6af2009d1ff9969d0a48b18b2ebc2e1e829` | yes |
| `CME-SVC-2026-12-31.json` | 2026-12-31..2027-01-02 | `7162652821c16f1bd05e3ec533bd5b82af03833c7186a64c7734b0b650364dcd` | yes |
| `CME-SVC-2027-01-17.json` | 2027-01-17..2027-01-19 | `7155c4b7ee8b299b3033eb3daf002b6ceecf0fbd53f6f98a7036048022275743` | yes |
| `CME-SVC-2027-02-14.json` | 2027-02-14..2027-02-16 | `41f5aa8cde3879f8b10490386c134a294a0f1509edde2022a22ec3ffcaed1183` | yes |
| `CME-SVC-2027-03-25.json` | 2027-03-25..2027-03-27 | `9bd7225d440e00139f30892f3914c9b38beb8bf29d4272039b6cd8f2de926880` | yes |
| `CME-SVC-2027-05-30.json` | 2027-05-30..2027-06-01 | `1283649724c30163fa08ba7ab02d1230fa9a7dd0613b8b4b3d96cd1d9dc4febd` | yes |
| `CME-SVC-2027-06-17.json` | 2027-06-17..2027-06-19 | `60c9a2f5106d61039a616986b463cd852861ee4d3b91b11fac8badfa1b97b01c` | yes |
| `CME-SVC-2027-07-04.json` | 2027-07-04..2027-07-06 | `93ff8232886435c94be682bf968aa30749011cdf8dadeb7d2425a3b0b9e0bf71` | yes |
| `CME-SVC-2027-09-05.json` | 2027-09-05..2027-09-07 | `aa08a3bd102812928e69cf1ea4c8a84f738eaa5d14f967acee7d2571e74aedb9` | yes |
| `CME-SVC-2027-11-24.json` | 2027-11-24..2027-11-26 | `6aa7c0fd701a02480dabeac1fbae1a69b56e77643a29e3a9b2223c56e822ce9f` | yes |
| `CME-SVC-2027-12-22.json` | 2027-12-22..2027-12-25 | `5edc4dd588a32faa74f841494c10a3df48692dca29843c3581bad3e18c30fef9` | yes |
| `CME-SVC-2027-12-31.json` | 2027-12-31..2028-01-02 | `d5a7c4306b6caa22f1ab22a1dd7cb27f903621bb039b5eac3abdaabf4fc5f621` | **new window** — not in the crate |

The URL the page itself fetches for the Christmas 2027 window is
`toEventDate=2027-12-24`; the crate's recorded window extends to 2027-12-25.
The wider window was pulled here so the hash compares against the crate's own
record; both agree.

### Globex notices and the notice index (`notices/`)

The notice search index is served by
`https://www.cmegroup.com/content/cmegroup/en/notices/jcr:content/main-content-section/section/section-elements/search_sort_filter_d.ssfajax.<page>.0.<from>.<to>.json`
(public, unauthenticated, same Akamai gate). Three pages cover 2026-09-01
through 2026-10-13 (90 results, sorted newest first).

| file | document | URL | retrieval (UTC) | sha256 |
|---|---|---|---|---|
| `notices-index-2026-09-01_2026-10-13.json` | notice index page 0 (newest 30) | see URL form above, page 0 | 2026-10-13T23:34:26Z | `50287f178cc008435dbdcbc370160ef3c3e044232a70a1c2a79f30b954236e03` |
| `notices-index-p2-2026-09-01_2026-10-13.json` | notice index page 1 | page 1 | 2026-10-13T23:36Z | `cb230b96790bcf5162c02b7e4b9c74305d8551b255763d60d50678043912aad8` |
| `notices-index-p3-2026-09-01_2026-10-13.json` | notice index page 2 | page 2 | 2026-10-13T23:37Z | `223e5e3534e32ca66fb2ad6b1387bdf411a0552384d5ee8eb33cc64bbdc9e4c6` |
| `globex-notice-20260914-full.html` | CME Globex Notice: September 14, 2026 — Sep 19 extension only (already shipped, notice 20260824's restatement) | <https://www.cmegroup.com/notices/electronic-trading/2026/09/20260914.html> | 2026-10-13T23:37:44Z | `72f7a6618bce6d8c77fc8fa1405a5cc9b6d0423083e4c1e5c4cd317392dcdda2` |
| `globex-notice-20260928-full.html` | CME Globex Notice: September 28, 2026 — Oct 3 + Oct 24 extensions (shipped, notice 20260921's restatements); first BCOM announcement | <https://www.cmegroup.com/notices/electronic-trading/2026/09/20260928.html> | 2026-10-13T23:37:23Z | `6dd5f8cd45b4b77f3de1abfb7bcdaf61bd65d68a6692abd68e52e5700222ad6a` |
| `globex-notice-20261005-full.html` | CME Globex Notice: October 5, 2026 — **NEW Oct 31 extension; BCOM amendment restated**; Nikkei risk-range, spread-type and catalog items | <https://www.cmegroup.com/notices/electronic-trading/2026/10/20261005.html> | 2026-10-13T23:37:17Z | `1b55ce441928c79bccce889f86750f5c0ecd570dae2c44434b0f977b591ae893` |

The extraction note is `diff-report.md`.
