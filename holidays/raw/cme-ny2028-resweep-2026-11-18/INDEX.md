# INDEX — cme-ny2028-resweep-2026-11-18 (CME Globex New Year 2028 window verification)

Task: decide from the operator's own `trading-hours-by-product` bytes whether
New Year 2028 (New Year's Day falls on **Saturday 2028-01-01**) constitutes any
schedule deviation for the CME family clocks. Sweep run 2026-11-18 (UTC,
`date -u`). Verdict: **no deviation for any family clock** — the printed
2027-12-31 .. 2028-01-03 arc is each family's ordinary week, so no holiday row
ships and no coverage window moves. All times below are U.S. Central Time.

## Channels used

1. **Wayback CDX enumeration** of the trading-hours service captures carrying
   `fromEventDate=2027-12-31` (2026 captures):
   `https://web.archive.org/cdx/server/cdx?url=cmegroup.com/services/trading-hours-by-product*&from=2026&to=2026&output=json&filter=urlkey:.*fromeventdate=2027-12-31.*`
   -> `cdx/cdx_thbp_fromeventdate-2027-12-31_year-2026.json`. It lists five
   captures: four of the ten-product A set
   (`id=316,133,425,300,58,437,22,8478,5201,10191`, window
   `fromEventDate=2027-12-31&toEventDate=2028-01-02`) at 2026-09-13T07:47:38Z,
   2026-10-06T06:07:49Z, 2026-11-11T06:23:10Z and 2026-11-14T03:28:18Z, and one
   of a nine-product equity set (`id=133,146,318,8667,8668,8670,5224,10142,10037`,
   same window) at 2026-10-15T06:08:23Z. No other capture set carries this
   window: the archive holds **no capture with the B-set/Nikkei ids** for
   2027-12-31..2028-01-02.
2. **Byte-exact `id_` replays** of all five captures (each replayed with the
   full archived URL including its `&_t=` cache-buster; the archive stores the
   payloads gzipped, and the replay returns the stored bytes verbatim — the
   `.json.gz` files below are those replay bytes, the `.json` files their
   gunzipped content). CDX digests confirm the first two A-set captures are the
   same archived object (`2MPZSS6RVDJJUQBDSDN2D7THPCJNQ7FV`); the 11-11 and
   11-14 digests differ **only because the service reorders its `products`
   array between responses** — every product's events are identical in all
   four A-set payloads and in the equity set.
3. **cmegroup.com/trading-hours.html**, capture 2026-11-16T04:55:18Z
   (CDX also lists 2026-11-16T04:22:31Z; both 200) — replayed byte-exact.
4. **Direct live call** to the service — blocked; see
   `live-direct-2026-11-18.txt` (TLS handshake ok against the genuine
   `CN=cmegroup.com` certificate, then HTTP/2 INTERNAL_ERROR / HTTP/1.1 read
   timeout; no HTTP status returned at all on 2026-11-18; the 2026-09-12
   sweep recorded HTTP 403 for the same host).

## What the captures print (per product group, window 2027-12-31 .. 2028-01-02)

Compared against the stored ordinary-week baseline
(`holidays/raw/cme-2025-2027/live/normal/normalweek_main.json`, week
2026-10-18..24) and the stored live retrieval of the overlapping window
2027-12-30..2028-01-02 (`holidays/raw/cme-2025-2027/live/thbp/
thbp_2027-12-30_2028-01-02.json` and `.../live/extra/extra_2027-12-30_
2028-01-02.json`, retrieved 2026-09-12; **event-for-event identical** with the
2026-11-14 archived payload on all 30 shared (product, eventDate) pairs —
re-checked 2026-11-18):

- **ZN 316 (rates), ES 133 (equity), CL 425 (energy), GC 437 (metals),
  6E 58 (fx)** — Friday eventDate 2027-12-31: `16:00 closed` for CME trade
  date 2027-12-31 (the ordinary Friday final close). eventDate 2028-01-01
  (Saturday): no events. eventDate 2028-01-02 (Sunday):
  `16:00 preopen; 17:00 open` carrying CME trade date 2028-01-03 (the
  ordinary Sunday reopen, `16:00`, not the weekday-evening `16:45`).
  The equity-set capture prints the same shape for NQ 146, YM 318,
  MES 8667, MNQ 8668, MYM 8670, MGC 5224, MCL 10037 and MHG 10142.
- **ZC 300 (grains)** — Friday 2027-12-31 prints the ordinary grains arc
  (`07:45 paused; 08:00 preopen; 08:30 open; 13:20 paused; 13:30 closed;
  14:30 pcp; 16:00 closed`); Saturday empty; Sunday `16:00 preopen; 19:00 open`
  for trade date 2028-01-03 (the grains' ordinary Sunday reopen). The stored
  live B-set capture adds soybeans ZS 320 and wheat ZW 323 with the same arcs,
  and the dairy lines — cheese CSC 5201 and milk DC 27 — print their ordinary
  Friday `13:55 closed` and the ordinary Sunday `16:00/17:00` reopen.
- **LE 22 (livestock)** — Friday prints the ordinary arc (`08:00 preopen;
  08:30 open; 13:05 closed; 14:30 pcp; 16:00 closed`); Saturday and Sunday
  empty (the family has no Sunday session). Lean hogs HE 19 agree.
- **BTC 8478 (crypto, BF group)** — the ordinary 24x7 weekend block: Friday
  eventDate carries `16:00 closed` for trade date 2027-12-31 then
  `16:01 preopen; 16:02 open` carrying trade date 2028-01-03; Saturday
  eventDate 2028-01-01 carries `02:00 closed; 03:45 preopen; 04:00 open`
  for trade date 2028-01-03 (the ordinary Saturday maintenance window the
  crate already models); Sunday empty.
- **LBR 10191 (lumber)** — ordinary Friday `06:00 preopen; 09:00 open;
  15:05 closed`; Saturday and Sunday empty.
- **Nikkei** — no Nikkei id is reachable in any archived capture of this
  window (the A set and the equity set carry none). The family's non-event
  stands on the stored live B-set capture of 2027-12-30..2028-01-02
  (retrieved 2026-09-12, sha256s in that directory's INDEX), which prints
  NIY 167 and NKD 168 with the ordinary Friday `16:00 closed`, an empty
  Saturday and the ordinary Sunday `16:00 preopen; 17:00 open` for trade
  date 2028-01-03.

No printed instant deviates from the ordinary week on 2027-12-31 .. 2028-01-03
for any family clock: no early Friday close, no cancelled or shifted Sunday
reopen, no changed Saturday window. New Year's Day is a Saturday that carries
no session, exactly as the normal week does.

## The trading-hours page, capture 2026-11-16

The page contains exactly two literal `2028` occurrences:

1. The **2027 Settlement Notices** table row (verbatim):
   `<tr><td>New Year’s Eve</td><td>31 December 2027 - 3 January 2028</td><td><a class="cmeIcon-file-pdf" href="/tools-information/holiday-calendar/files/2027/new-years-eve-holiday-settlement-times-2027.pdf">New Year's Eve</a></td></tr>`
   — a pointer at the settlement-times PDF, settlement-department information,
   not session language.
2. The **`2028 New Year's Day Notes`** component, whose text is the ordinary
   order-cycle clarification: "Day orders entered after a product’s
   Pre-opening(s) on Thursday , December 30th are for trade date Friday,
   December 31 st and can continue working until their Friday, December 31 st
   Globex close. December 29th TAS: Regular close per each product schedule"
   (the sibling `2027 New Year's Day Notes` component carries the same shape
   one weekday earlier). Neither states an early close, a late open or a
   closure. The page's 2026-edition Globex holiday-hours table ends at
   "New Year’s 31 December 2026 - 1 January 2027"; no 2028 Globex holiday row
   exists on the page.

## Artifacts

| file | what it is | url | capture / retrieval (UTC) | sha256 |
|---|---|---|---|---|
| `cdx/cdx_thbp_fromeventdate-2027-12-31_year-2026.json` | CDX enumeration of 2026 captures carrying `fromEventDate=2027-12-31` (5 rows) | see Channels 1 | query run 2026-11-18 | `48787627faa690aa20fb71641d054c875e922b4923711388b01b99bc3df6bdbf` |
| `cdx/cdx_trading-hours_year-2026.json` | CDX enumeration of 2026 `trading-hours.html` captures (31 rows) | `https://web.archive.org/cdx/server/cdx?url=cmegroup.com/trading-hours.html&from=2026&to=2026&output=json&filter=statuscode:200` | query run 2026-11-18 | `e9c644b067ff3007656da2e02241a01f557eed1a72503de539d5705dd19aa6a0` |
| `arc/aset_thbp_2027-12-31_2028-01-02_20260913074738.json` | A-set service payload, window 2027-12-31..2028-01-02 | `https://web.archive.org/web/20260913074738id_/https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2027-12-31&toEventDate=2028-01-02&isProtected&_t=1789285657344` | capture 2026-09-13T07:47:38Z | `d5a7c4306b6caa22f1ab22a1dd7cb27f903621bb039b5eac3abdaabf4fc5f621` |
| `arc/aset_thbp_2027-12-31_2028-01-02_20261006060749.json` | A-set service payload, same window; byte-identical to the 09-13 capture (same CDX digest) | WA:`20261006060749id_/` + same URL with `&_t=1791266868961` | capture 2026-10-06T06:07:49Z | `d5a7c4306b6caa22f1ab22a1dd7cb27f903621bb039b5eac3abdaabf4fc5f621` |
| `arc/aset_thbp_2027-12-31_2028-01-02_20261111062310.json` | A-set service payload, same window; identical events, reordered products | WA:`20261111062310id_/` + same URL with `&_t=1794378189915` | capture 2026-11-11T06:23:10Z | `5766e1a90bc12a57d7bd0da399a0663fb8cd1be16295a03a25bf631de19fcce3` |
| `arc/aset_thbp_2027-12-31_2028-01-02_20261114032818.json` | A-set service payload, same window; identical events, reordered products | WA:`20261114032818id_/` + same URL with `&_t=1794626897683` | capture 2026-11-14T03:28:18Z | `b6df20e13547ea02ab9b4070180142e661bb8b9e1c1c31fe644dae705ab85add` |
| `arc/equity_thbp_2027-12-31_2028-01-02_20261015060823.json` | nine-product equity-set service payload, same window (ES 133, NQ 146, YM 318, MES 8667, MNQ 8668, MYM 8670, MGC 5224, MCL 10037, MHG 10142) | `https://web.archive.org/web/20261015060823id_/https://www.cmegroup.com/services/trading-hours-by-product?id=133,146,318,8667,8668,8670,5224,10142,10037&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2027-12-31&toEventDate=2028-01-02&isProtected` | capture 2026-10-15T06:08:23Z | `77b71ac069fbb37b9f90f295a8b1f868112f895fb17ed1c2c55893e216aa32db` |
| `page/trading-hours_20261116045518.html` | cmegroup.com/trading-hours.html, archived page (238,383 bytes gunzipped) | `https://web.archive.org/web/20261116045518id_/https://www.cmegroup.com/trading-hours.html` | capture 2026-11-16T04:55:18Z | `63acf18a2542ca24492d4bbe7cb052245feb86eff5181a01ae8da7f79a9e9a03` |
| `live-direct-2026-11-18.txt` | transcript of the blocked direct cmegroup.com probes | https://www.cmegroup.com/services/trading-hours-by-product (direct) | attempted 2026-11-18 | (text file; no archived original) |

Each `arc/*.json.gz` and `page/*.html.gz` file is the raw `id_` replay as the
archive served it (gzip); its sha256: A-set 09-13 and 10-06
`f3e92828951479669ed0dfc4ef7fbead450a5c6bc13dc5053e92c2710dd39dda` (both),
11-11 `f234e8a42660ed488eb2c12ea778b11b116ca38650740b1e901e6c923cef1659`,
11-14 `696b5e14d52653f3cb0820d022aff41bec17b083fdf97497d6b88ad6eb697352`,
equity `2c5e8c74e6c1205a9269d0b40f48b7f6130bd056bbd0d00ccae145ee16898a5a`,
page `2a9a7efd45d1c89461bd509e23f28e707c717c735d19c7d9ad9f5901545fb010`.

sha256 note: the payload hashes above are of the gunzipped archived bytes —
the convention the crate's `### Documents` tables use (verified against
`holidays/raw/cme-2025-2027/arc/thbp_2024-12-31_2025-01-02_20241220155340.json`,
whose sha256 reproduces the `CME-SVC-2024-12-31` row's hash).

## Outcome

No deviation: **no family needs a New Year 2028 row, and no coverage window
moves.** The last encoded trade date stays 2027-12-31; 2028-01-01 (Saturday)
carries no session exactly as the normal week does; the 2028-01-03 trade date
remains inside the unaudited span before the first 2028 window (the window
prints only the 2028-01-03 *open*, not that date's full session). The notes
this sweep adds to the crate's family evidence files cite this directory.
