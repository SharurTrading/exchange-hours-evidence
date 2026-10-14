# Evidence index — `ice-history-2026-10-13` (three ICE-family historical gaps, #332)

Retrieval session: **2026-10-13 23:24–24:00 UTC** (`date -u`). All times below are UTC (LAW-UTC-DATES).
Wave targets, from the maintainer's consolidated historical-research ask (exchange-hours-rs#332):

1. **ice_us_sugar pre-August-2011 normal-week baseline** (carried, not sourced; master-table gap),
2. **IFEU Trading Schedule editions 2015–2020** (store held only 2021-10 onward plus the 2026 editions),
3. **the 2009 NYSE Liffe notice zip** (the zip that carries 2010's arrangements; the store held 2010–2014).

Two of the three targets close as data this wave; the third (sugar) gains its first in-gap operator
witness plus new in-gap dated rows, and its residual is re-scoped. Machine-readable copy of the
digest table: `INVENTORY.tsv`; the verification fence is `SHA256SUMS.txt` (covers this directory and,
with repo-root-relative paths, the two zip artifacts placed beside their siblings in
`holidays/raw/ice-europe-gilts-2010-2027/`). Derived `*.txt` files are `pdftotext -layout` extractions
of the PDF beside them; the `.txt` mtime is the extraction time, not a second retrieval.

## A. IFEU Trading Schedule editions 2013–2020 (target 2 — CLOSED for 2015/2016/2017/2019/2020; 2018 bracketed)

The document class is the operator's annual **"20XX Trading Schedule"** (the same document as the
store's `holidays/raw/ice-europe-gilts-2010-2027/20211022183728_Trading_Schedule.pdf`), and its
companion **"Trading Schedule — Migrated Liffe Contracts"** for the ex-NYSE Liffe fixed income and
equity contracts (the gilts/STIRs family). Every edition self-dates in its header ("Last Update: …"),
so a capture dates the edition it prints (LAW-NO-FABRICATED-DATES) and the capture-time URL is
recorded per row. All fetched as Wayback `id_` raw replays — no artifact rewritten. The store's
channel control holds: the 2021-10-22 replay of `ice.com/publicdocs/Trading_Schedule.pdf`
(`LCDVDBKK…`) is byte-identical to the stored `20211022183728_Trading_Schedule.pdf`.

| # | File | Wayback capture of | Retrieved (UTC) | sha256 (see `INVENTORY.tsv`) | Edition witnessed |
|---|---|---|---|---|---|
| A1 | `20130513190254_Trading_Schedule.pdf` | https://www.theice.com/publicdocs/Trading_Schedule.pdf @20130513190254 | 2026-10-13 23:41:00 | `3dcbfff4…` | `2013 Trading Schedule` — `Last Update: April 2013` (pre-gap context) |
| A2 | `20140707113835_Trading_Schedule.pdf` | same URL @20140707113835 | 23:41:04 | `dc618d46…` | `2014 Trading Schedule` — `Last Update: June 2014` (pre-gap context) |
| A3 | `20150321171128_Trading_Schedule.pdf` | same URL @20150321171128 | 23:41:08 | `ee2a6f3d…` | **`2015 Trading Schedule` — `Last Update: February 2015`** (first 2015 edition) |
| A4 | `20150920010827_Trading_Schedule.pdf` | same URL @20150920010827 | 23:41:12 | (INVENTORY) | **`2015 Trading Schedule` — `Last Update: September 2015`** |
| A5 | `20160419011939_Trading_Schedule.pdf` | same URL @20160419011939 | 23:41:20 | `5115f132…`(pdf) | **`2016 Trading Schedule` — `Last Update: January 2016`** |
| A6 | `20160728161527_Trading_Schedule.pdf` | same URL @20160728161527 | 23:41:26 | `dd1899e4…`(pdf) | Same printed January-2016 edition, later capture; delta vs A5 is additive **ICE Containerised White Sugar** rows (`ICE Containerised White Sugar early close at 17:00 UK (12:00 ET)`), the holiday spine is unchanged |
| A7 | `20161221110112_Trading_Schedule.pdf` | same URL @20161221110112 | 23:41:31 | (INVENTORY) | **`2016 Trading Schedule` — `Last Update: December 2016`** |
| A8 | `20170126164933_Trading_Schedule.pdf` | same URL @20170126164933 | 23:46 | (INVENTORY) | **`2017 Trading Schedule` — `Last Update: January 2017`** |
| A9 | `20170217174821_Trading_Schedule.pdf` | same URL @20170217174821 | 23:46 | (INVENTORY) | **`2017 Trading Schedule` — `Last Update: February 2017`** |
| A10 | `20170707170018_Trading_Schedule.pdf` | same URL @20170707170018 | 23:46 | (INVENTORY) | **`2017 Trading Schedule` — `Last Update: April 2017`** (last witness before the 2018 hole) |
| A11 | `20190103162112_Trading_Schedule.pdf` | same URL @20190103162112 | 23:52 | (INVENTORY) | **`2019 Trading Schedule` — `Last Update: January 2019`** (first witness after the 2018 hole) |
| A12 | `20190526200737_Trading_Schedule.pdf` | same URL @20190526200737 | 23:55 | (INVENTORY) | **`2019 Trading Schedule` — `Last Update: May 2019`** |
| A13 | `20190703215853_Trading_Schedule.pdf` | same URL @20190703215853 | 23:52 | (INVENTORY) | **`2019 Trading Schedule` — `Last Update: June 2019`** |
| A14 | `20200629160511_Trading_Schedule.pdf` | same URL @20200629160511 | 23:52 | (INVENTORY) | **`2020 Trading Schedule` — `Last Update: January 2020`** |
| A15 | `20201231184142_Trading_Schedule.pdf` | same URL @20201231184142 | 23:55 | (INVENTORY) | **`2020 Trading Schedule` — `Last Update: December 2020`** |
| A16 | `20150919192106_Trading_Schedule_Migrated_Liffe_Contracts.pdf` | https://www.theice.com/publicdocs/futures/Trading_Schedule_Migrated_Liffe_Contracts.pdf @20150919192106 | 23:42:54 | `617d8116…` | **`IFEU Fixed Income and Equity Contracts: Trading Days in 2015`** — first line `ICE Futures Europe will be closed on the following days:` followed by the 2015 closure list (the ex-Liffe gilt/STIR holiday rows for 2015) |
| A17 | `20160419003940_…Migrated….pdf` | same URL @20160419003940 | 23:43:00 | (INVENTORY) | **`IFEU Fixed Income and Equity Contracts: Trading Days in 2016`** |
| A18 | `20161003081013_…Migrated….pdf` | same URL @20161003081013 | 23:43:08 | (INVENTORY) | **`…: Trading Days in 2016`** (October edition, distinct digest) |
| A19 | `20161221101055_…Migrated….pdf` | same URL @20161221101055 | 23:43:16 | (INVENTORY) | **`…: Trading Days in 2016`** (December edition, distinct digest) |
| A20 | `20170126164934_…Migrated….pdf` | same URL @20170126164934 | 23:46 | (INVENTORY) | **`…: Trading Days in 2017`** |
| A21 | `20170707160915_…Migrated….pdf` | same URL @20170707160915 | 23:46 | (INVENTORY) | **`…: Trading Days in 2017`** (July edition, distinct digest) |

**Gap years after this wave: none for the annual spine except 2018.** 2015 (Feb+Sep editions),
2016 (Jan×2, Dec; Migrated Apr/Oct/Dec), 2017 (Jan/Feb/Apr; Migrated Jan/Jul), 2019 (Jan/May/Jun),
2020 (Jan+Dec) all witnessed. **2018 has no capture anywhere**: the CDX record below enumerates every
archived capture of every `Trading_Schedule*` URL on theice.com and ice.com 2015–2022, and nothing
falls between the 2017-07-07 and 2019-01-03 captures; the Common Crawl 2018 indexes were queried and
the service answered 502/504 for all nine (recorded as **inconclusive**, `cdx/cdx_sweeps_2026-10-13.txt`
query 8). 2018's arrangement is therefore bracketed by the April-2017 and January-2019 editions only —
the crate's `HolidayWindowsBridged` doctrine, not a witnessed edition.

## B. Sugar No. 11 pre-August-2011 (target 1 — first in-gap operator witness; gap re-scoped, not closed)

The prior sweeps (2026-08-31, 2026-09-01, 2026-09-30 in the crate's evidence file; the 2026-10-06
domain-lineage pass in `holidays/raw/iceus/domain-lineage-2026-10-06/`) closed every archived edition
of the master hours table, the rulebook chapters, the productguide contract-spec family, the
marketdata calendar pages and nybot.com. This wave swept the **name-level** channels those passes had
not: a `filter=original:.*[Ss]ugar.*` host query 2008–2012 (`cdx/cdx_theice_sugar_0812.txt`,
13 rows — every sugar-named artifact the archive holds), the brochure/product-guide/softs notice name
sweeps, the `product_guide` underscore variant, `productguide/ContractSpecs.shtml`, the
`futures_us` path, and the early Common Crawl indexes. Results in section D.

**The find: the operator's own Sugar No. 11 / No. 16 brochure, PDF-created 2010-03-22, printing the
Sugar No. 11 `HOURS` row 03:30–14:00 EST — the carried baseline, witnessed from inside the carried
span.** This is the first operator statement of the softs electronic grid dated between the January-2010
floor and the August-2011 master table.

| # | File | Wayback capture of | Retrieved (UTC) | Contents |
|---|---|---|---|---|
| B1 | `sugar-pre2011/ice_ICE_Sugar_Brochure.wayback-20111121015738.pdf` | https://www.theice.com/publicdocs/ICE_Sugar_Brochure.pdf @20111121015738 | 2026-10-13 23:3x | **"SUGAR NO. 11® AND SUGAR NO. 16"**, ICE Futures U.S. brochure. PDF `CreationDate D:20100322164205-04'00'`, `ModDate D:20100322164326-04'00'` (Adobe InDesign CS3) — the document's own date is **22 March 2010**, inside the carried span; the archive's first and only capture of this generation is 2011-11-21 (digest `HWP5PLLL…`; three generations exist, see B2). Under `ICE FUTURES U.S. SUGAR CONTRACTS / The ICE Futures U.S. Sugar No. 11 sugar futures contract … The key specifications are:` it prints the row **`HOURS␣␣0330 EST TO 1400EST`** — session language, a spec-table `HOURS` row (the `TRADING HOURS`-row class of LAW-SESSION-NOT-EXPIRY), **03:30–14:00 EST**, exactly the crate's carried baseline (`SUGAR_REGULAR_BASELINE`, open 03:30, close 14:00 NY). The Sugar No. 16 table in the same document prints **`HOURS␣␣0900 EST to 1400 EST`**. No printed issue date inside; the contract-cycle note `MARCH - MAY - JULY - OCTOBER (JANUARY STARTING WITH JANUARY 2010)` is consistent with the March-2010 creation date. Tier T1 (the operator's own published document), document date from the PDF's own metadata. **What it changes:** the 2010-01..2011-08 interval is no longer sourced on neither flank — the March-2010 brochure and the August-2011 master table now witness **the same grid at both ends**, so under the crate's sourced-intersection/bridged-residual doctrine the carried grid is no longer a bare carry-back; what remains genuinely unwitnessed is only January–March 2010 and the holiday layer (the brochure states no holiday data and no order-entry phases). |
| B2 | `sugar-pre2011/ice_ICE_Sugar_Brochure.wayback-20120610134716.pdf` | same URL @20120610134716 | 23:5x | Second brochure generation (PDF created `D:20120514113110+01'00'`, 14 May 2012). Sugar No. 11 spec now prints **`Hours␣␣0130 Eastern Standard Time (0230 Eastern Daylight when applicable) to 1400 Eastern Standard Time.`** and Sugar No. 16 **`Hours␣␣0900 Eastern Standard Time to 1400 Eastern Standard Time.`** — the post-2012-01-30 grid the module already carries, corroborated from a second T1 document five weeks after the change. Documents the succession B1→B2. |
| B3 | `sugar-pre2011/ice_Sugar_Introduction_Chinese.wayback-20120610022724.pdf` | https://www.theice.com/publicdocs/Sugar_Introduction_Chinese.pdf @20120610022724 | 23:5x | Operator's Chinese-language Sugar No. 11 introduction, printed in-document **2011年12月12日 (12 December 2011)**, by Tim Berry (ICE). Prints **`交易时段: 3:30 a.m. – 2:00 p.m. 美国东部时间（期货与期权采用电子交易）`** (electronic session 03:30–14:00 US Eastern for futures and options) and **`场内交易时段: 8:00 a.m. 至 1:30 p.m. 美国东部时间`** (floor session 08:00–13:30 ET) — a second operator witness that the Aug-2011 master-table grid held through December 2011 (the last observation before the 2012-01-30 change), plus an explicit operator statement of the floor session (context; the crate models the electronic session). Tier T1. |
| B4 | `sugar-pre2011/ice_Rule409_SugarNo11_Options_PostClose.wayback-20101014003530.pdf` | https://www.theice.com/publicdocs/futures_us/exchange_notices/AmendmentstoRule409-SugarNo11OptionsPostClose.pdf @20101014003530 | 23:3x | ICE Futures U.S. Exchange Notice dated **March 19, 2010**: amendments to **Floor** Trading Rule 4.09, `Effective Monday, March 22, 2010` — the post-close trading session for Sugar No. 11 **options** (ring) begins five minutes after the closing period instead of fifteen. An operator notice dated inside the carried span; it witnesses the notice genre and the existence of floor trading in 2010, and states no electronic-session bound, so it keys no row. Tier T1. |
| B5 | `sugar-pre2011/ice_ExNot041111_SoftsOpen.wayback-20111213005119.pdf` | https://www.theice.com/publicdocs/futures_us/exchange_notices/ExNot041111SoftsOpen.pdf @20111213005119 | 23:5x | Exchange Notice dated **April 11, 2011**: `Due to UK banking holiday on Monday, May 2, 2011, ICE Futures U.S. will delay the start of electronic trading in Sugar No. 11, Coffee "C" and Cocoa futures and options contacts until 7:30 am NY time.` (`contacts` sic — the notice's own typo for contracts). A **dated, unconditional in-gap exception row: 2011-05-02 Sugar No. 11 late open 07:30 ET** — new holiday-layer data *before* the family's current audited window. It also states `This change to the start time for these products does not affect` `floor trading hours, end of day times or settlement times` — confirming fixed end-of-day times existed in April 2011 without stating them. Tier T1. |
| B6 | `sugar-pre2011/ice_Sugar11_Swap_Contract.wayback-20111213004841.pdf` | https://www.theice.com/publicdocs/futures_us/Sugar11_Swap_Contract.pdf @20111213004841 | 23:3x | Cleared-Only Sugar No.11 Swap Contract specification, printed **february 22, 2009** (sic). `Trade Submission Hours … can be submitted only during trading hours for the related, traded futures contract` — references the futures session without stating it. No hours row. Tier T1; keys nothing. |
| B7 | `sugar-pre2011/ice_11-019_Sugar_Delivery_Notices.wayback-20110222140721.pdf` | https://www.theice.com/publicdocs/clear_us/notices/11-019_Sugar_Delivery_Notices.pdf @20110222140721 | 23:3x | Clearing notice 11-019 (January 31, 2011): eCOPS delivery-notice rollout for the March 2011 sugar cycle. Procedural; keys nothing. Tier T1. |
| B8 | `sugar-pre2011/ice_ExNot091211_Sugar16_Rate.wayback-20111213005836.pdf` | https://www.theice.com/publicdocs/futures_us/exchange_notices/ExNot091211Sugar16Rate.pdf @20111213005836 | 23:3x | Exchange Notice September 12, 2011: Sugar No. 16 stevedoring rate to $15.00/long ton from October 1, 2011. Not session data. Tier T1. |
| B9 | `sugar-pre2011/ice_Sugar_No11_Chinese.wayback-20120610023511.pdf` | https://www.theice.com/publicdocs/Sugar_No11_Chinese.pdf @20120610023511 | 23:5x | Chinese rulebook-chapter translation, PDF created `D:20111010222719` (10 October 2011). No trading-hours provision (consistent with the 2026-09-01 finding that the rulebooks carry no hours). Tier T1. |
| B10 | `sugar-pre2011/ice_Monthly_Softs_Fast_Facts.wayback-20111120210045.pdf` | https://www.theice.com/publicdocs/futures_us/ICE_Monthly_Softs_Fast_Facts.pdf @20111120210045 | 23:5x | "Monthly Softs Fast Facts" — a **J. Ganes Consulting newsletter distributed "compliments of ICE Futures U.S."**, PDF created 2011-11-15. Prints an "ICE Futures US Thanksgiving Holiday Trading Schedule" table (open-outcry and electronic columns; Thu Nov 24 2011 closed; Fri Nov 25 early close 12:45 PM ET with settlement windows). **Tier T3/T4 — a vendor restatement that does not mirror an operator document verbatim, so it dates nothing and keys nothing (LAW-PRIMARY-SOURCES)**; kept as residual-risk context only. It does corroborate that open outcry still ran alongside electronic trading in November 2011. |

## C. The 2009 (and 2008) NYSE Liffe notice zips (target 3 — CLOSED)

The live operator host serves the historical-notice archive one year beyond the store's set. The page
the store already holds (`normal-weeks/ice-gilts-2026-10-11/ice-eu-historial-notices.html`, the live
`https://www.ice.com/futures-europe/liffe-resources/handbook/notices`) links 2010–2014; the same
`/publicdocs/nyse_liffe/historical_notices/<year>.zip` path also serves **2006, 2007, 2008 and 2009**
(200-status), while 2015/2016 return 404 (`cdx/live_zip_probes.txt`). Channel control: the live
`2010.zip` is **byte-identical** to the store's `nyse_liffe_2010.zip`
(`31a87b7d07e69a40fbf89e7f13ca730286c48c2d349ec04e20a56a27d953271b`), validating the live channel
exactly as the iceus wave validated its replay channel. Neither zip was ever archived (CDX query 17:
empty), so live retrieval was the only channel.

Placed beside their siblings in `holidays/raw/ice-europe-gilts-2010-2027/`:

| # | File | Source URL | Retrieved (UTC) | sha256 | Bytes | Contents |
|---|---|---|---|---|---|---|
| C1 | `nyse_liffe_2009.zip` | https://www.ice.com/publicdocs/nyse_liffe/historical_notices/2009.zip | 2026-10-13 23:58:13 | `b9c6610cf544bee19d4d2005c4dd3fe204fefb60f902dc56d79d29776ae8dbd1` | 6755189 | **127 notices, LON3111–LON3238** (`2009/` members, zip entry mtimes 2015-04-24 — the same 2015 packaging as the stored 2010–2014 zips), continuous with the 2010 zip's LON3239 start. Key members: **LON3203** (issue 13 October 2009, effective 1 January 2010, "TRADING DAYS IN 2010" — the 2010 full-year notice the store's STATUS recorded as the archive gap): `The London market will be open on Monday to Friday throughout 2010 except on the following days: Friday 1 January 2010 (New Year's Day) / Friday 2 April 2010 (Good Friday) / Monday 5 April 2010 (Easter Monday)`; `On the following UK Bank Holidays, NYSE Liffe's sterling based products and UK-based commodity products will not be made available, but other products will be available: Monday 3 May 2010 / Monday 31 May 2010 / Monday 30 August 2010 / Monday 27 December 2010 / Tuesday 28 December 2010`; and `On Friday 24 December 2010 and Friday 31 December 2010, trading hours will be aligned with those of underlying and, where appropriate, related markets. On these days the Exchange will commence the closing of its derivatives contracts from midday GMT (1.00 pm CET).` — **LON3220** (issue 13 November 2009, effective 24 December 2009, "TRADING HOURS: 24 DECEMBER 2009 TO 1 JANUARY 2010"): 24 Dec 2009 and 31 Dec 2009 `Half day trading, with Contracts closing by 13:00 hours (GMT) (14:00 hours CET)`, 25 Dec 2009 `Closed.`, 1 January 2010 `Closed.`, 28 Dec 2009 sterling/UK-commodity unavailability, with per-contract attachment hour tables (Long Gilt among them). **LON3226** (issue 30 November 2009): confirms LON3203 announced the 2010 trading days and that the precise 2010 trading hours were published on `www.nyx.com/liffeholidays` "as at 30 November 2009". Extraction notes beside the key notices: `liffe-notices/LON3203.txt`, `liffe-notices/LON3220.txt`, `liffe-notices/LON3226.txt`. |
| C2 | `nyse_liffe_2008.zip` | https://www.ice.com/publicdocs/nyse_liffe/historical_notices/2008.zip | 2026-10-13 23:58:13 | `0b4884b94ad4a778d8d3c932772b96a61914a50c415904d9c01bf833d88c1e31` | 4435670 | The 2008 notice year (context across the support floor). Key member **LON3073** (issue 26 September 2008, effective 1 January 2009, "TRADING DAYS IN 2009") — the same notice genre one year earlier; witness of the pre-floor arrangements and of the notice-numbering continuity (`liffe-notices/LON3073.txt`). |
| C3 | `liffe-notices/LON3203.txt`, `LON3220.txt`, `LON3226.txt`, `LON3073.txt`, `nyse_liffe_200{8,9}.zip.listing` | derived (`pdftotext -layout`; `unzip -l`) | 2026-10-13 24:00 | see `SHA256SUMS.txt` | Extraction notes and zip member listings; the PDFs themselves live inside the zips. |

LAW-NO-FABRICATED-DATES care for C1: LON3203's EFFECTIVE DATE 1 January 2010 with issue 13 October
2009 is the operator's own unconditional day-level statement — it can key 2010 rows directly.
LON3220's precise half-day hours witness 24/31 **December 2009** and the 1 January 2010 closure only;
they are not a January-2010 baseline claim.

## D. Channel record (negative and inconclusive probes)

All queries saved or summarized in `cdx/cdx_sweeps_2026-10-13.txt`; per-file digests in
`SHA256SUMS.txt`.

- **`product_guide` (underscore) on theice.com, any year** — CDX prefix returns empty; the path does not exist in the archive. (The mission's URL-pattern suggestion checked and closed.)
- **`theice.com/productguide/ContractSpecs.shtml`** — no captures at all; the contract-spec pages the 2026-10-06 sweep found were the `DelayedData.shtml?specId=N` family (2011-11-20 onward, post-gap).
- **`theice.com/futures_us*` 2008–2012** — only `futures_us.jhtml` (302s; one 200-status capture 2011-10-16, post-August-2011). No in-gap product page under the modern path.
- **Early Common Crawl (CC-MAIN-2008-2009, CC-MAIN-2009-2010, CC-MAIN-2012)** — "No Captures found" for theice.com under any sugar filter; the earliest crawls hold no theice.com pages at all.
- **`theice.com/publicdocs*` + mimetype:application/pdf, 2009–2011** — the CDX query returned empty twice (timing out server-side); **failed query, inconclusive**, superseded for sugar by the successful name-level sweeps (queries 9/13) and the 2026-10-06 domain-lineage pass.
- **Common Crawl 2018 indexes for `theice.com/publicdocs/Trading_Schedule.pdf`** — all nine 2018 indexes answered 502/504 (service outage during this session). **Inconclusive, not negative**; the only way 2018 could still gain a witnessed edition.
- **liffe.com / nyse.com / nyx.com domain-wide `Trading_Schedule` CDX sweeps** — 504 Gateway Time-out (query failed); superseded for the target by theice.com/ice.com successes above, which hold the document class across the whole era.
- **Sugar-name host sweep 2008–2012** (positive, 13 rows) — every sugar-named theice.com artifact in the archive is fetched or assessed above (B1–B10). Nothing else in the archive carries "sugar" in the URL for the gap era.

## What this wave changes for the crate (coordinator summary)

1. **IFEU 2015–2020 (target 2):** editions for 2015, 2016, 2017, 2019 and 2020 witnessed from the
   operator's own self-dated Trading Schedule and Migrated-Liffe documents (A1–A21). Only **2018**
   remains unwitnessed (bracketed April-2017 → January-2019; CC 2018 inconclusive). Best next
   channel: the Common Crawl 2018 indexes when the service recovers (exact URL:
   `theice.com/publicdocs/Trading_Schedule.pdf`), then a desk ask for the 2018 edition PDF.
2. **2009 zip (target 3):** closed. LON3203 is the 2010 full-year notice; LON3220 carries the
   Christmas/New-Year 2009-10 hours tables. The live host also serves **2006–2008 zips** (C2 keeps
   2008; 2006/2007 left in place, probe logged) — the same path should be re-checked for the crate's
   other Liffe-era needs.
3. **Sugar baseline (target 1):** the gap's shape changes. The carried 03:30–14:00 NY grid is now
   **witnessed at March 2010** by the operator's own brochure (B1) and re-witnessed at December 2011
   (B3), so the span is bracketed by agreeing operator states on both flanks instead of carried blind;
   the remaining unwitnessed residue is January–March 2010 plus the holiday/phase layer, and the
   crate's evidence file and `SUGAR_REGULAR_BASELINE` comment should be updated to cite B1/B3 (with
   B5's new 2011-05-02 late-open row) as a normal schedule change. The "terminal answer" language in
   `docs/evidence/ice_us_sugar.md` (no in-gap document can exist) is superseded by this find and needs
   the same update.
