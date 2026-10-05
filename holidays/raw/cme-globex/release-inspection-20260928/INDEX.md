# INDEX — Stage 7 release-month re-inspection, CME Group (cme/cbot/comex/nymex + the Globex families)

Retrieval session: **2026-09-27 19:16–19:44 UTC** (`date -u`), one inspection pass (LAW-BOUNDED-WORK).
`cmegroup.com` 403s this machine (proved negative, prior waves), so live reads went through the public
reader `https://r.jina.ai/<url>`; digests are of the saved files. Prior holdings: `holidays/raw/cme-2025-2027/`
(live capture 2026-09-12, through CME-SVC-2027-12-22 plus the NY2028 window file).

`[THBP-A]` = `https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true`
with `&fromEventDate=<d1>&toEventDate=<d2>` (same ten product groups and parameter shape as the stored wave).

## What is NEW versus the store

1. **2028 material is now published.** The T2 service returns the MLK 2028 arrangement
   (`thbp_mlk2028.raw`, window 2028-01-15..18) event-for-event in the established MLK shape —
   Sunday 2028-01-16 preopen 16:00/open 17:00 CT assigned to trade date 2028-01-18, Monday
   2028-01-17 preopen 12:00 (ES/ZN; grains open 19:00), first close Tuesday 16:00. The T1 page
   (`trading-hours-live-20260927.md`) now carries a "2028 Holidays" section with New Year's Day only
   and its TAS note. The NY2028 window (`thbp_ny2028.raw`, 2027-12-30..2028-01-02) is content-identical
   to the stored 2026-09-12 capture (checked programmatically) — no errata there.
2. **Two new unconditional Saturday maintenance-window extensions for the 24/7 markets**, Globex notice
   20260921: **Saturday 2026-10-03** 02:00–05:00 CT, and **Saturday 2026-10-24** 02:00–15:30 CT (FIA
   industry disaster-recovery exercise; a ~13.5 h gap — the crate's 4-hour `Maintenance` bound will not
   hold it, so the row shape needs a release-PR decision). Both revert to the 02:00–04:00 standard after.
3. **Three new Globex notices read** (none carries a served-family session change):
   20260817 (100-oz Silver 4S to 24/7 effective trade date 2026-08-31, weekend trading from Friday
   2026-09-11 16:30 CT — the consumer maps root `SIL` to the Comex venue/`globex_energy` family, whose
   scope excludes differently specified products, so this is recorded as a consumer-routing observation,
   not crate data; FSPI sports indexes channel 271/335 — excluded family), 20260907 (silver go-live
   restatement; Friday 2026-09-11 daily maintenance extended 16:00–16:30 CT once; livestock MDP-channel
   migration effective 2026-09-14 — market data only, no session change; restates the Sep-19 window),
   20260914 (restates the Sep-19 extension "this week"), 20260921 (the two October extensions above).
   Notice 20260928 does not exist yet (404 probe); the newest notice as of retrieval is 20260921.
4. **Errata: none.** Every held post-2026-05-29 capture re-fetched and compared event-for-event:
   Thanksgiving 2026, Christmas 2026 (both), Labor Day 2027, Thanksgiving 2027, Christmas 2027 and
   NY2028 — all identical. The only diff found was against the 2026-03-10 capture of Christmas 2026,
   which predates the crypto 24/7 transition and shows the old five-day-era crypto cells (already
   modelled by #123/#177). The filters payload's 14-holiday forward list (2026-09-07 .. 2028-01-01,
   New Year's Day 2028 endPeriod 2027-12-30..2028-01-02) is unchanged except an additive new
   "Sports Indexes" asset class (id 17) in the filter metadata.
5. **Elapsed forward-dated row confirmed effective:** Saturday 2026-09-19 extension to 08:00 CT
   (`thbp_sep2026_sat.raw`: BF closed@02:00, preopen@07:45, open@08:00 → trade date 2026-09-21), matching
   notices 20260824/20260831/20260907/20260914.

## Artifacts

| file | url (via `https://r.jina.ai/` prefix when noted) | retrieved (UTC) | sha256 |
|---|---|---|---|
| `filters.r.jina.txt` / `filters.json` | https://www.cmegroup.com/services/trading-hours-filters (reader; .json is the extracted payload) | 2026-09-27 ~19:17 | `9bf08a69…` / `6251b850…` |
| `thbp_ny2028.raw` / `.json` | [THBP-A]&fromEventDate=2027-12-30&toEventDate=2028-01-02 | 2026-09-27 ~19:18 | `5ea5ef19…` / `caa86332…` |
| `thbp_mlk2028.raw` / `.json` | [THBP-A]&fromEventDate=2028-01-15&toEventDate=2028-01-18 | 2026-09-27 ~19:18 | `5b574b87…` / `1483f03a…` |
| `thbp_sep2026_sat.raw` / `.json` | [THBP-A]&fromEventDate=2026-09-18&toEventDate=2026-09-22 | 2026-09-27 ~19:21 | `c8800cd5…` / `e7d61211…` |
| `thbf_tg2026.raw` / `.json` | [THBP-A]&fromEventDate=2026-11-25&toEventDate=2026-11-28 | 2026-09-27 ~19:21 | `80f82107…` / `639d134b…` |
| `thbp_today_2026-12-23_26.raw` | [THBP-A]&fromEventDate=2026-12-23&toEventDate=2026-12-26 | 2026-09-27 ~19:23 | `fd88e1de…` |
| `thbp_today_2027-09-05_07.raw` | [THBP-A]&fromEventDate=2027-09-05&toEventDate=2027-09-07 | 2026-09-27 ~19:23 | `7cf37dd5…` |
| `thbp_today_2027-11-24_26.raw` | [THBP-A]&fromEventDate=2027-11-24&toEventDate=2027-11-26 | 2026-09-27 ~19:23 | `ffad16db…` |
| `thbp_today_2027-12-22_25.raw` | [THBP-A]&fromEventDate=2027-12-22&toEventDate=2027-12-25 | 2026-09-27 ~19:23 | `83e87994…` |
| `notice_20260817.md` | https://www.cmegroup.com/notices/electronic-trading/2026/08/20260817.html (reader) | 2026-09-27 ~19:25 | `bf594642…` |
| `notice_20260907.md` | https://www.cmegroup.com/notices/electronic-trading/2026/09/20260907.html (reader) | 2026-09-27 ~19:25 | `d4fa1696…` |
| `notice_20260914.md` | https://www.cmegroup.com/notices/electronic-trading/2026/09/20260914.html (reader) | 2026-09-27 ~19:30 | `2925fced…` |
| `notice_20260921.md` | https://www.cmegroup.com/notices/electronic-trading/2026/09/20260921.html (reader) | 2026-09-27 ~19:31 | `47387659…` |
| `notice_20260928_check.md` | …/2026/09/20260928.html — 404 probe (does not exist yet) | 2026-09-27 ~19:33 | `7f52e85a…` |
| `notice_20261005_probe.md` | …/2026/10/20261005.html — 404 probe | 2026-09-27 ~19:32 | `445b1a12…` |
| `trading-hours-live-20260927.md` | https://www.cmegroup.com/trading-hours.html (reader) — T1 page; carries the 2026/2027 holiday tables and a new 2028 Holidays section (New Year's Day only) | 2026-09-27 ~19:34 | `907f3d28…` |
| `SHA256SUMS.txt` | digests of every file in this directory | 2026-09-27 19:40 | — |

## Channels refused / not pursued

- Direct cmegroup.com: 403 (proved negative in prior waves; not re-chased).
- Wayback CDX enumeration of `cmegroup.com/tools-information/holiday-calendar/files/*`: two timeout
  refusals this session — channel ended per the twice-refused rule. The route adds nothing the thbp
  service and the T1 page have not already stated (the files route carries clearing/settlement
  advisories, and every page link points at /trading-hours.html).
