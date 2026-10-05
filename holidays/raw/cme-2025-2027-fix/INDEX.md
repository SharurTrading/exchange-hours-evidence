# INDEX — cme-2025-2027-fix (round-1 fixer evidence)

Task: `cme-2025-2027`, fixer round 1. Evidence gathered **2026-09-12 (UTC; `date -u`)**.
This directory holds only the artifacts retrieved in the fix round. The round-0 evidence, unchanged,
is in `../cme-2025-2027/` with its own INDEX.md.

All CME times are U.S. Central Time, per the operator's own statement quoted verbatim from
https://www.cmegroup.com/trading-hours.html: "Trading hours are subject to change and are in U.S. Central Time unless otherwise stated."

cmegroup.com returns HTTP 403 to this machine directly, so live service calls were read through the public
reader `https://r.jina.ai/<url>`; historical states were read from the Wayback Machine with `id_` replay.
Wayback `id_` replay of this endpoint returns the **gzip-compressed original bytes**; both the compressed
original (`.json.gz`) and its decompression (`.json`) are saved, and the `.json` is what was parsed.

## Artifacts

| file | what it is | url | capture / retrieval (UTC) | sha256 |
|---|---|---|---|---|
| `cdx/cdx_thbp_all_fix.json` | fresh CDX enumeration of the service endpoint (688 rows after `collapse=digest`), used to settle which window has which captures | `https://web.archive.org/cdx/search/cdx?url=cmegroup.com/services/trading-hours-by-product*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&collapse=digest&limit=100000` | retrieved 2026-09-12T07:42Z | `4c8c9760a3a711cba88f1fc6980f5850aec8afb01fc7482111d688bafc0da942` |
| `arc/thbp_2025-11-26_2025-11-28_20260129012309.json.gz` | **D09** — trading-hours service response, Thanksgiving 2025 window, latest of the 45 captures of this window and taken two months after the holiday (original gzip bytes) | `https://web.archive.org/web/20260129012309id_/https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-11-26&toEventDate=2025-11-28&isProtected&_t=1769649789739` | captured 2026-01-29T01:23:09Z | `ab8342bd5dbc6dd78f4f6efe599b6448d47a0adffe1bd8baafa5337d49c08062` |
| `arc/thbp_2025-11-26_2025-11-28_20260129012309.json` | the same, decompressed — the bytes the 2025-11-26/27/28 rows are quoted from | (gunzip of the row above) | captured 2026-01-29T01:23:09Z | `6c4c598791058dd9a11aff0ddb072c761a436c6d1054b891def74c6935f020f1` |
| `arc/thbp_2025-12-24_2025-12-26_20260129012309.json.gz` | Christmas 2025 window at the LATEST capture of that window, fetched to check D10 was not stale (original gzip bytes) | `https://web.archive.org/web/20260129012309id_/https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-12-24&toEventDate=2025-12-26&isProtected&_t=1769649789742` | captured 2026-01-29T01:23:09Z | `6944a2dd28359cea6a47194c6e74ef9f8808229fd1411482025b962f87290cb2` |
| `arc/thbp_2025-12-24_2025-12-26_20260129012309.json` | the same, decompressed — **byte-identical to the saved D10 artifact** (`322a2be9…`), so D10 needed no change | (gunzip of the row above) | captured 2026-01-29T01:23:09Z | `322a2be989b67f5f4cc0ec12fd63a393383d574badd4aacc87a0c9637533d386` |
| `arc/thbp_2025-12-31_2026-01-02_20260722114222.json.gz` | New Year 2026 window at the LATEST capture of that window, fetched to check D11 was not stale (original gzip bytes) | `https://web.archive.org/web/20260722114222id_/https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2025-12-31&toEventDate=2026-01-02&isProtected&_t=1784720542553` | captured 2026-07-22T11:42:22Z | `d2823ea03baa58a787cd616e2f10d1dae533bd76cf602ea2ce27589812f493b0` |
| `arc/thbp_2025-12-31_2026-01-02_20260722114222.json` | the same, decompressed — not byte-identical to D11 (product order differs) but identical schedule for schedule across all 30 (product, eventDate) pairs, so D11 needed no change | (gunzip of the row above) | captured 2026-07-22T11:42:22Z | `d32b0725642cee7de8f36abc390d5231d90a70952bab183462d47bd87465fcdc` |
| `live/thbp_2026-11-27_2026-11-29.md` | **D52** — reader-rendered live service response, window 2026-11-27..2026-11-29 (the Saturday after Thanksgiving 2026) | `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-11-27&toEventDate=2026-11-29` | retrieved 2026-09-12T07:47Z | `fa86b557e92404a833114029169836f9bce1578abf266d1b6389be3909a3eefa` |
| `live/thbp_2026-11-27_2026-11-29.json` | the JSON body extracted verbatim from the row above | (extract of the row above) | retrieved 2026-09-12T07:47Z | `31c724b033b249fd746592021cea57bbd30a99cf3effb8d3454af68c18bdcdfb` |
| `live/thbp_2027-11-26_2027-11-28.md` | **D53** — reader-rendered live service response, window 2027-11-26..2027-11-28 (the Saturday after Thanksgiving 2027) | `https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2027-11-26&toEventDate=2027-11-28` | retrieved 2026-09-12T07:47Z | `913a2d302f1b16ea6c0252ee52b7e3983c998595ed02c3014c7dddbdb9cc366c` |
| `live/thbp_2027-11-26_2027-11-28.json` | the JSON body extracted verbatim from the row above | (extract of the row above) | retrieved 2026-09-12T07:47Z | `61d57229aa58577c78ea094ddb839b2da336a4c4be2df37b6c3bd0382f93f46f` |
| `REFETCH.tsv` | derived: the exact one-step Wayback `id_` replay URL for each of the 25 archived service artifacts in `../cme-2025-2027/arc/`, rebuilt from `cdx/cdx_thbp_all_fix.json`. Repairs the re-fetch path that INDEX.md broke by dropping the `&isProtected&_t=<epoch>` suffix | (derived in this round) | 2026-09-12 | `c5288e5a2c7de8c02a0dd87ea99409448b57a21c0b405a9b4379cd1269c627c7` |
| `MANIFEST-cme-2025-2027.sha256` | derived: sha256 of every one of the 180 files on disk under `../cme-2025-2027/`, not just the 72 that INDEX.md lists | (derived in this round) | 2026-09-12 | `47139c0def9b3abfa5e62f8abfc8787935dfc24bac6f54011ca6be283bce1d8e` |
| `/Users/agedvagabond/Developer/exchange-hours-research/holidays/cme-2025-2027.json` | this round's structured output (supersedes `cme-2025-2027.r0.json`) | (derived in this round) | 2026-09-12 | `6bc718e5fbaea70c01f3bf54ccab156028eef9c28ce24357a5217c633b5d5771` |
| `/Users/agedvagabond/Developer/exchange-hours-research/holidays/cme-2025-2027.r0.json` | the round-0 output, kept verbatim | (round 0) | 2026-09-12 | `4cd4706a8e989cd0d59abe1279e4a03f3aee9b0b80c99476d2fe49466584bd50` |

## Note codes added or defined in this round

The round-0 INDEX.md defines `N1`..`N16` and `EC`. `N17` was used on three rows but never defined; `N18` is new.

- `N17` no day session on the holiday: the family publishes only a 16:00 CT pre-open and a 17:00 CT open, both
  already carrying the next business day's trade date. Verified against D01: on 2025-01-01 ES, ZN, CL, 6E, GC,
  BTC and CSC each publish exactly `16:00 preopen /TD 2025-01-02; 17:00 open /TD 2025-01-02`, while ZC, LE and
  LBR publish nothing at all.
- `N18` the published event TIMES equal the family's normal grid for that weekday, but the re-open carries a
  trade date that skips the following closed holiday, so the date does carry a holiday trade-date roll.
  Used once: BTC on Thursday 2027-12-23, whose `16:01 preopen / 16:02 open` carry trade date 2027-12-27,
  skipping the closed Friday 2027-12-24. In the reference week (live/normal/normalweek_main.json) only the
  Friday row rolls to Monday; Mon-Thu roll to the next calendar day.

## What the Thanksgiving-2025 re-sourcing changed

D09 (2026-01-29T01:23:09Z, post-holiday) against D09P (2024-12-20T15:53:40Z, pre-holiday). Both were parsed
here; the comparison is over all 30 (product, eventDate) pairs in the window.

- 2025-11-26 — identical for all ten products.
- 2025-11-27 — identical for all ten products.
- 2025-11-28 — identical for LE (`08:00 preopen; 08:30 open; 12:05 closed`) and CSC (no events); differs for
  the other eight:

| product | D09P (pre-holiday) | D09 (post-holiday, now quoted) |
|---|---|---|
| ES | `12:15 closed` | `07:00 preopen; 07:30 open; 12:15 closed` |
| ZN | `12:15 closed` | `07:00 preopen; 07:30 open; 12:15 closed` |
| 6E | `13:45 closed` | `07:00 preopen; 07:30 open; 13:45 closed` |
| CL | `13:45 closed` | `07:00 preopen; 07:30 open; 13:45 closed` |
| GC | `13:45 closed` | `07:00 preopen; 07:30 open; 13:45 closed` |
| BTC | `13:45 closed` | `07:00 preopen; 07:30 open; 13:45 closed` |
| ZC | `08:30 open; 12:05 closed` | `07:00 preopen; 08:30 open; 12:05 closed` |
| LBR | `06:00 preopen; 09:00 open; 12:05 closed` | `06:00 preopen; 07:00 preopen; 09:00 open; 12:05 closed` |

Every trade date in the window is 2025-11-28 on that date in both publications, and **every early-close
instant — 12:15 CT, 13:45 CT, 12:05 CT — is identical in both**. The change is an added morning
pre-open/open pair, not a changed close.

## Capture counts behind the residual-risk statement

From `cdx/cdx_thbp_all_fix.json`, per service window (captures after `collapse=digest`; "latest" is the
capture whose timestamp is greatest):

| window | holiday | captures | latest capture |
|---|---|---|---|
| 2024-12-31 .. 2025-01-02 | New Year 2025 | 2 | 2024-12-20T15:53:40Z |
| 2025-01-19 .. 2025-01-21 | MLK 2025 | 1 | 2024-12-20T15:53:40Z |
| 2025-02-16 .. 2025-02-18 | Presidents' 2025 | 1 | 2024-12-20T15:53:40Z |
| 2025-04-17 .. 2025-04-19 | Good Friday 2025 | 1 | 2024-12-20T15:53:40Z |
| 2025-05-25 .. 2025-05-27 | Memorial 2025 | 1 | 2024-12-20T15:53:40Z |
| 2025-06-18 .. 2025-06-20 | Juneteenth 2025 | 1 | 2024-12-20T15:53:40Z |
| 2025-07-03 .. 2025-07-05 | Independence 2025 | 1 | 2024-12-20T15:53:40Z |
| 2025-08-31 .. 2025-09-02 | Labor 2025 | 1 | 2024-12-20T15:53:40Z |
| 2025-11-26 .. 2025-11-28 | Thanksgiving 2025 | 45 | 2026-01-29T01:23:09Z |
| 2025-12-24 .. 2025-12-26 | Christmas 2025 | 45 | 2026-01-29T01:23:09Z |
| 2025-12-31 .. 2026-01-02 | New Year 2026 | 51 | 2026-07-22T11:42:22Z |

No archived window anywhere in the enumeration satisfies `fromEventDate <= 2025-11-29 <= toEventDate`; the
only November-2025 window captured at all is 2025-11-26..2025-11-28. That is the Saturday gap now recorded
in `missing[]`.

## Saturday check, from D52 / D53

On Saturday 2026-11-28 and Saturday 2027-11-27 the service publishes **no events at all** for ZN, ES, CL, ZC,
6E, GC, LE, CSC or LBR. Only BTC appears, with its ordinary 24/7 Saturday grid — 2026-11-28:
`02:00 closed /TD 2026-11-30; 03:45 preopen /TD 2026-11-30; 04:00 open /TD 2026-11-30`; 2027-11-27:
`02:00 closed /TD 2027-11-29; 03:45 preopen /TD 2027-11-29; 04:00 open /TD 2027-11-29`. So CME ran no
post-Thanksgiving Saturday session in either year. This is mitigation for the unchecked 2025 Saturday, not
proof about it.
