# Rough Rice (ZR) — verified by me, not just by the agent

Two independent verifications done in-session on 2026-09-05.

## 1. CBOT Submission 18-001 — the divergence (PDF fetched and read)
`raw/cbot-18-001.pdf`, 3 pages, from
https://web.archive.org/web/20240314032026id_/https://www.cmegroup.com/content/dam/cmegroup/market-regulation/rule-filings/2018/01/18-001.pdf
(live: https://www.cmegroup.com/content/dam/cmegroup/market-regulation/rule-filings/2018/01/18-001.pdf)

Verbatim, lines 71-82 of the extracted text:
> certifying the reduction of the extended trading hours on the CME Globex electronic trading
> platform for the Rough Rice Futures and Rough Rice Options contracts (the "Contracts")
> **effective on Sunday, January 21, 2018 for trade date Monday, January 22, 2018**.
>
> Rough Rice Futures  ZR  17
> Rough Rice Options  OZR 17A
>
> | Current Extended Trading Hours | Extended Trading Hours Effective on Trade Date January 22, 2018 |
> | Sunday - Friday, 7:00 p.m. - 7:45 a.m. CT | Sunday - Thursday, 7:00 p.m. - 9:00 p.m. CT |

This states the effective day explicitly, names the products and rulebook chapters, and CME's own
column heading classifies the evening leg as EXTENDED. Fully compliant with LAW-PRIMARY-SOURCES
and LAW-NO-FABRICATED-DATES.

## 2. Live CME product spec — the current grid (read in a browser; curl gets 403)
https://www.cmegroup.com/markets/agriculture/grains/rough-rice/specs — read 2026-09-05, verbatim:

```
TRADING HOURS
CME Globex:
Sunday - Thursday, 7:00 p.m. - 9:00 p.m. CT
Pre-Open Sunday: 4:00 p.m. - 7:00 p.m. CT

Monday - Friday:  8:30 a.m. - 1:20 p.m. CT
Pre-Open Monday - Thursday: 4:45 p.m. - 7:00 p.m. CT
```
Page also confirms: PRODUCT CODE "CME Globex: ZR", EXCHANGE RULEBOOK "CBOT 17".

**No morning pre-open is listed.** Standard grains carry an 08:00-08:30 CT morning Pre-Open
(SER-9049); ZR's spec page does not. Do NOT model one for ZR — omitting an order-entry window
under-reports queueing, which is the safe direction and the lower-cost error under the repo's
"executable windows are the priority" rule.

## The encoding this supports
```
regular      MON_FRI  08:30 - 13:20     (unchanged by 18-001; from grains' SER-7395R lineage)
extended     SUN_THU  19:00 - 21:00     (18-001, no midnight wrap from 2018-01-21)
order_entry  SUN      16:00 - 19:00     (live spec)
order_entry  MON_THU  16:45 - 19:00     (live spec)
```

## Timeline: ZR == standard grains until 2018-01-21, then one divergence
The crate's existing `GlobexGrains` revisions are 2010-04-19, 2011-12-27, 2012-05-20, 2013-04-07,
2013-08-18, 2015-07-05. The research confirms ZR followed the CBOT grain/oilseed reorganisations
throughout (ZR is named in the product lists of CBOT Submissions 12-144 and the 2013/2015 filings).
So `GlobexRoughRice` = the grains chain plus a 2018-01-21 revision.

## Open items deliberately NOT encoded
- ZR morning pre-open: not stated by any CME source retrieved. Left unmodelled.
- Pre-open history for the 2010/2012/2013/2015 eras: unsourced for ZR specifically.
- RTH/ETH split for 2012-05-20 -> 2013-04-07 (one continuous 17:00-14:00 session): unsourced.
  The existing grains profile already makes a reviewed choice here; ZR follows it for consistency,
  and the fact that it is an inherited inference must be stated in the profile comment.
