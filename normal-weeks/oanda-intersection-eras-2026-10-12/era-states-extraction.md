# OANDA UK hours-page era states — extraction record

Retrieved and checked 2026-10-12 UTC. This record is the derivation input for
the exchange-hours-rs witnessed-era change: every captured normal-week grid
per book, read from the audit's saved `id_` replays under
`normal-weeks/oanda-uk-wayback-audit-2026-10-11/hours-captures/`. All rows
are the operator's own page prints (T1). Grids are transcribed verbatim.

## New York-anchored books

| Capture (UTC) | All FX products | XAU/USD, XAG/USD | US index rows | US Treasury rows | US commodity rows (NG/WTI/XPT/XPD; Copper Chicago) | Brent Crude Oil |
|---|---|---|---|---|---|---|
| 2021-03-03 | no Forex table | `All gold instruments (XAU) Sun - Fri 18:00 - 17:00` / `All silver instruments (XAG)` same | `18:00 - 16:15; 16:30 - 17:00` (futures-exact) | `17:00 - 16:00` Chicago | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2021-05-08 | no Forex table | coarse `18:00 - 17:00` rows | `18:00 - 16:15; 16:30 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2021-08-04 | no Forex table | coarse rows | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2021-08-18 (x2) | no Forex table | coarse rows | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2021-12-08 | `Sun-Fri: 17:03 - 16:58*` | `Gold (XAU/USD) Sun-Fri: 18:03 - 16:58*`, silver same | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2021-12-14 | `17:03 - 16:58*` | `18:03 - 16:58`; XAG close printed `16:60` (page typo) | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2022-05-18 | `17:03 - 16:58*` | `18:03 - 16:58` (crosses `18:10 - 16:58`) | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2022-07-24 (gzip) | `17:03 - 16:58*` | `18:03 - 16:58` (crosses `18:10`) | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2022-10-02 | `17:03 - 16:58*` | `18:03 - 16:58` | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2022-11-27 | `17:03 - 16:58*` | `18:03 - 16:58` | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2023-02-01 | `17:03 - 16:58*` | `18:03 - 16:58` | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2023-03-16 (gzip) | `17:03 - 16:58*` | `18:03 - 16:58` | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2023-04-25 (gzip) | `17:03 - 16:58*` | `18:03 - 16:58` | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2023-06-05 (05:35) | `17:03 - 16:58*` | `18:03 - 16:58` | `18:00 - 17:00` | `17:00 - 16:00` | `18:00 - 17:00` | `20:00 - 18:00*` |
| 2024-02-21 (00:55) | `Sun-Fri: 17:05 - 16:59 *` | `Sun-Fri: 18:05 - 16:59` | `Sun - Fri 17:01 - 15:59` (Chicago) | `17:01 - 15:59` Chicago | NG/WTI/XPT/XPD `18:01 - 16:59`; Copper `17:01 - 15:59` | `Mon - Fri 01:01 - 22:59 †` (London) |
| 2024-05-07 | current grids (identical to 2024-02-21) | | | | | |
| 2024-06-20 | current grids | | | | | |
| 2024-09-19 | current grids | | | | | |
| 2026-10-10 live | current grids | | | | | |

## Singapore-anchored books (Times column `Singapore`)

| Capture (UTC) | China A50 | Singapore 30 |
|---|---|---|
| 2021-03-03 .. 2023-06-05 (every capture) | `Mon - Fri 09:00 - 16:30; 17:00 - 04:45` | `Mon - Fri 08:30 - 17:20; 17:50 - 04:45` |
| 2024-02-21 .. current | `Mon - Fri 09:01 - 16:29; 17:01 - 04:44` | `Mon - Fri 08:31 - 17:19; 17:51 - 05:14` |

## Derived intersections (opening-day bounds)

Opening days are keyed by each book's zone: the 2023-06-05 05:35 UTC print
lands inside the New York session opened 2023-06-04 (last legacy opening day
2023-06-04) and inside the Singapore day session of 2023-06-05 (last legacy
opening day 2023-06-05); the 2024-02-21 00:55 UTC print lands inside the New
York session opened 2024-02-20 and the Singapore day session of 2024-02-21.

| Book | Legacy (served) | Intersection (served across the undated span) | Current |
|---|---|---|---|
| `oanda_fx` | 17:03 -> 16:58 | 17:05 -> 16:58 | 17:05 -> 16:59 |
| `oanda_metals` | 18:03 -> 16:58 | 18:05 -> 16:58 | 18:05 -> 16:59 |
| `oanda_us_index_cfd` | 18:00 -> 17:00 | 18:01 -> 16:59 (= current) | 18:01 -> 16:59 |
| `oanda_us_bond_cfd` | 18:00 -> 17:00 (17:00-16:00 Chi) | 18:01 -> 16:59 (= current) | 18:01 -> 16:59 |
| `oanda_us_commodity_cfd` | 18:00 -> 17:00 | 18:01 -> 16:59 (= current) | 18:01 -> 16:59 |
| `oanda_china50_cfd` | 09:00-16:30; 17:00-04:45 | 09:01-16:29; 17:01-04:44 (= current) | 09:01-16:29; 17:01-04:44 |
| `oanda_singapore30_cfd` | 08:30-17:20; 17:50-04:45 | 08:31-17:19; 17:51-04:45 | 08:31-17:19; 17:51-05:14 |
| `oanda_brent` | 20:00 -> 18:00 New York | NOT SERVED: legacy New York anchor vs current London dagger grid are not nested (DST-disagreement weeks move the London-equivalent boundaries by an hour; the 22:05-22:59 later block is not common to both states) | London dagger grid |

## Help-centre channel (retrieved 2026-10-12)

`help-centre/` holds the two previously unretrieved Wayback replays of
`https://help.oanda.com/uk/en/faqs/hours-of-operation.htm` (captures
20240619014415 and 20241107102830) and the live page. All three print no
session grid — only the boilerplate that trading hours "are subject to change
during daylight saving time and certain public holidays". The differing
Wayback digests are layout drift. This closes the last indexed operator
channel negative; the uncollapsed CDX query of 2026-10-12 returns zero
hours-page captures between 2023-06-06 and 2024-02-20, and the audit's eight
twice-refused replays all postdate the 2024-02-21 current-grid witness.
