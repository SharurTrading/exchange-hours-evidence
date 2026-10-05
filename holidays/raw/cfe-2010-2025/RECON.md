# CFE holiday retrieval — channel recon, 2026-09-19/21 UTC (stage 2.3, venue 2)

## Correction

An earlier version of this file concluded that CFE's holiday history below 2021 was unreachable
and recommended starting the table at 2021 with a gap. **That conclusion was wrong and is
withdrawn.** It rested on three mistakes:

1. It probed a handful of URL *prefixes* (`cboe.com/us/futures/hours*`, `.../notices*`,
   `cboe.com/about/hours*`) and never ran the query that answers the question — a **domain-wide
   CDX filtered on the URL**.
2. It queried `cdn.cboe.com/resources/regulation/circulars*` for the circulars and concluded they
   start in 2019. The pre-2019 CFE circulars are on a **different host**
   (`cfe.cboe.com/publish/CFEinfocirc/`), so that was a wrong-channel result, not a negative one.
3. At least one probe returned an **empty response body** — a failed request — which was recorded
   as "no captures". `cboe.com/us/futures/notices*` was never actually answered.

The lesson is the one this stage keeps re-teaching: a channel that returns nothing is not a
channel that was asked.

## What the domain-wide probe found

`https://web.archive.org/cdx/search/cdx?url=cboe.com&matchType=domain&filter=urlkey:.*holiday.*`
(saved as `cdx_cboe_holiday.json`, 209 URLs) plus the follow-ups `cdx_cfe_subdomain.json`,
`cdx_schedule_update.json` and `cdx_cfe_holidaycal.json`:

### 1. A CFE holiday-calendar page, captured continuously 2017-04 .. 2019-12

`cfe.cboe.com/about-cfe/holiday-calendar` — **91 captures**, 2017-04-10 through 2019-12-19 (301s
from 2020 as the site migrated). Fetched and saved here as
`cfe_holiday_calendar_20190412.html` (60,070 bytes). It is **T1 and it is session language**:

- Regular `8:30 a.m. to 3:15 p.m.` CT; extended `5:00 p.m. (previous day) to 8:30 a.m.` and
  `3:30 p.m. to 4:00 p.m.`
- *"Domestic Holidays Always Observed on Mondays"* — Martin Luther King Jr. Day, Presidents' Day,
  Memorial Day, Labor Day: holiday Monday Regular `None`, extended to `10:30 a.m.*`
- *"Thanksgiving"* — holiday Thursday Regular `None`, extended `5:00 p.m. (Wednesday)* to 10:30
  a.m.`; Friday Regular `8:30 a.m. to 12:15 p.m.`
- *"Floating Holidays and Good Friday"* — New Year's Day, Good Friday, Independence Day, Christmas
  Day, with the observed-day rules **stated** (Saturday → previous Friday, except New Year's Day;
  Sunday → next Monday), and *"The Exchange will typically close at 12:15 p.m. on July 3 … and
  December 24"*
- Footnote: *"Holiday trading sessions are not separate Business Days and are part of the next
  Business Day. Trading in VX futures is suspended between sessions of extended trading hours on
  the calendar day of a holiday."*

Because this is a **rules page** rather than a per-holiday notice, one document covers every
holiday in the years it was in force — a far better source than the per-holiday PDFs the 2026
table was built from.

### 2. A per-year operator notice archive at `cdn.cboe.com/resources/schedule_update/<YEAR>/`

177 URLs, directories **2013-2026**. The 2013-2016 files are BATS/Cboe *equities* notices; the
**CFE** holiday notices start in **2017** and run through 2026, including
`CFE-Modified-Trading-Hours-for-…` for MLK, Presidents' Day, Good Friday, Memorial Day,
Independence Day, Thanksgiving, Christmas and New Year, plus `Cboe-Holiday-Reminder-…` companions.
Example captures: 2018 Presidents' Day, 2019 Good Friday and Independence Day, 2020 Memorial Day
and Labor Day, 2021 all five, 2022 all seven, 2023 eight, 2024 five.

### 3. Cboe's own holiday-schedule press releases on `ir.cboe.com`

Ten captured PDFs under `ir.cboe.com/~/media/Files/C/CBOE-IR-V2/press-release/<YEAR>/holiday-
schedule-…` for **2014-2017** (Memorial Day, Good Friday, Independence Day, Labor Day, Presidents'
Day, MLK, Thanksgiving, Christmas/New Year).

### 4. The pre-2019 CFE circulars do exist

`cfe.cboe.com/framed/PDFframed.aspx?content=/publish/CFEinfocirc/CFEIC15-033.pdf` and siblings
(`CFEIC15-039`, `CFEIC16-001`, `CFEIC16-005`, `CFEIC16-008`, `CFEregcirc/CFERG16-001`,
`CFEregcirc/CFERG14-018`) are captured through 2015-2016, so the `IC-CFE-YYYY-NNN` series is
reachable on the old host.

## Revised conclusion

**Do (b). The CFE holiday table can be built well below 2021**, with the holiday-calendar page
covering the rules and the per-year notice archive covering 2017-2026 at T1. The floor question
narrows to **2010-2012**, which none of the four channels above reaches yet; that deserves a
bounded probe of its own (the `schedule_update` root shows the site published per-year notices
before 2017, just not CFE ones under that path, and the holiday-calendar page may have a
predecessor under the old Sitefinity paths).

## Modelling warning for whoever writes the CFE PR

The holiday-calendar page's rules are **richer than the 2026 table's**. It describes holiday
sessions that keep an extended leg running to 10:30 CT while the Regular session is `None`, states
that such a session belongs to the **next** Business Day, and notes VX suspensions *between*
extended sessions that are expressly not halts. That is not a scalar `EarlyClose` in every case,
and the 2010-2012 era has **no extended session at all** (`CFE_PROFILE_AT_2010_FLOOR`), so a rule
that reads "extended to 10:30" has nothing to shorten before 2010-12-10. Read the venue's dated
`revisions!` timeline before deriving a single row, and expect at least one date whose topology the
scalar vocabulary cannot state.

## Coverage map, derived (2026-09-21 UTC)

Counting what is actually captured, so the next round plans against it rather than against the
number of URLs:

| Year | Strongest channel | What it gives |
|---|---|---|
| 2017 | holiday-calendar page (19 captures), CFE notices in `schedule_update/2017` | the rules in force, plus per-holiday notices |
| 2018 | holiday-calendar page (45 captures), `schedule_update/2018` (3 CFE-named + Cboe reminders) | the rules in force, plus per-holiday notices |
| 2019 | holiday-calendar page (27 captures), `schedule_update/2019` | the rules in force, plus per-holiday notices |
| 2020 | `schedule_update/2020` (the richest directory, 25 files incl. MLK, Presidents, Good Friday, Memorial, Independence, Thanksgiving, Christmas reminders) | per-holiday notices; the page itself is a 301 |
| 2021 | `schedule_update/2021` (31 files) | per-holiday notices, essentially complete |
| 2022-2024 | `schedule_update/<year>` | per-holiday notices |
| 2025-2026 | `schedule_update/<year>` + the live page/CSV | per-holiday notices and the current table |

**Below 2017 the picture thins**, and this is the part not to overstate:

- **2014-2016**: `ir.cboe.com` holiday-schedule press releases (10 captured PDFs, 2014-2017) and
  the old-host CFE circulars (`CFEIC15-*`, `CFEIC16-*`, `CFERG14-018`, `CFERG16-001`). Partial:
  a few holidays per year, and none of it is the rules page.
- **2010-2013**: **nothing found yet.** The holiday-calendar page's earliest capture is 2017-04-10,
  the `schedule_update` directories hold only BATS/Cboe *equities* notices for 2013-2016, and the
  `cfe.cboe.com` capture set is densest from 2012 onward but no hour/calendar/holiday URL appears
  before 2017 under the paths probed.

So the honest statement is: **the CFE holiday table can go back to at least 2017 from the strongest
channel, and probably to 2014 from partial ones; 2010-2013 is still unproven.** That is a real
improvement on the withdrawn "2021 floor" recommendation, and it is not the same as "the floor is
reachable". The next round should probe two specific things before setting the window: whether
`cfe.cboe.com` had an earlier holiday/calendar page under the Sitefinity paths its 2010-2013
captures use, and whether the CFE rulebook's trading-hours chapter states holidays at all — a
rulebook is a far better floor source than a page whose captures start in 2017.

## The two probes, run (2026-09-21 UTC)

**Probe 1 — does the CFE Rule Book state holidays? No.** The live rule book is at
`cdn.cboe.com/resources/regulation/rule_book/cfe-rule-book.pdf` (fetched, 2,043,583 bytes, 395
pages, PDF title "CBOE FUTURES EXCHANGE, LLC"). Rule 402 "Trading Hours" **delegates** rather than
states:

> (a) The Exchange shall from time to time determine (i) on which days the Exchange shall be
> regularly open for business in any Contract ("Business Days") and (ii) during which hours trading
> … may regularly be conducted on such days ("Trading Hours").
> (b) The Exchange may modify its regular Business Days, Trading Hours, and Daily Settlement
> Times, including to not be open for business or to have shortened trading hours, in connection
> with a holiday or a period of mourning.

Its amendment line reads "Amended July 26, 2005 (05-20); April 6, 2011 (11-09); October 17, 2012
(12-26); August 13, 2013 (13-30); June 22, 2026 (26-012)" — so the rule was touched in 2011-2013,
but it names no holiday and no holiday hours. This matches the holiday-calendar page's own words:
*"Holiday closures and shortened holiday trading hours will be announced by circular."*

**Probe 2 — do the pre-2017 circulars carry the holiday schedules? From 2015 only.** The live CFE
general circular index (`cboe.com/us/futures/regulation/circulars/cfe/general/`, 64 PDFs) begins at
`CFE-IC-2017-001`. The **archived** series on the old host,
`cfe.cboe.com/publish/CFEinfocirc*` (55 URLs, 39 fetched here into `infocirc/`), runs back to
2005 — and scanning all 39 for holiday content:

| Circular | What it is |
|---|---|
| `CFEIC15-028` | "RE: CFE Closed for Independence Day Holiday … Friday, July 3, 2015" |
| `CFEIC15-039` | "RE: Modified Trading Hours for Labor Day Holiday … Monday, September 7, 2015" |
| `CFEIC17-054` | "RE: Modified Trading Hours for Christmas Holiday … Sunday, December 24, 2017" |
| `CFEIC17-055` | "RE: Modified Trading Hours for New Year's Day Holiday … Sunday, December 31, 2017" |

Every other circular mentioning "holiday" does so incidentally, inside a contract's final-settlement
date definition (`CFEIC07-021`, `CFEIC08-004`, `CFEIC12-005`) — not as a session statement. **No
pre-2015 circular that states holiday hours survives**, and the pre-2015 circular set itself is only
a handful (05-07, 06-*, 07-021, 08-004, 12-004/005/038/071).

## Window decision

Combining this with the coverage map above:

- **2010-2014 is not reachable.** The rule book delegates, the rules page's earliest capture is
  2017-04, the live circular index starts at 2017, and no pre-2015 holiday circular survives. The
  plan's assumed **2010-01-01 floor cannot be met**, and this is now a evidenced negative rather
  than an unasked question: three distinct channel families were each taken to their limit.
- **2015-2016 is partial.** Two 2015 holidays are sourced (`CFEIC15-028`, `CFEIC15-039`), from a
  circular archive that is demonstrably incomplete — so a window over those years would claim
  audited-normal days the archive cannot support.
- **2017 onward is the candidate floor**, but 2017 itself must be counted before it is claimed:
  `schedule_update/2017` holds only 3 files. The window should be set from the per-year holiday
  count, not assumed.

**So the CFE PR's first step is the count**: fetch every CFE holiday notice and circular from 2015
on, bucket by year, and set the window at the first year whose holiday list is complete. 2010-2014
then ships as a named gap with its closing condition (a pre-2015 CFE holiday circular or an
earlier rules page), and — because `cfe` is served — as an issue.

**One more honest note.** Three times in this stage a negative turned out to be an unasked
question, and this time it did not: the rule book genuinely delegates, the pre-2015 circulars
genuinely are not there, and the archive was genuinely down for part of the probing (it returned
503 "Internet Archive: Temporarily Offline" and 504 before recovering). The difference is that
this conclusion names what was tried and how far each channel was taken.

## Retrieval phase 1 — the corpus is in (2026-09-21 UTC)

Fetched into this directory:

- **77 CFE/Cboe holiday notices** from `cdn.cboe.com/resources/schedule_update/<YEAR>/`, all via
  status-200 archive replays (`notices/`, indexed in `notices_index.json`). Sixteen needed a second
  pass: `collapse=urlkey` had handed back one capture per URL and for those it was a **301**, so the
  retry queried each URL for its own status-200 capture. That is the same trap as before in
  miniature — a capture that exists is not a capture that serves.
- **43 CFE Information Circulars** (`infocirc/`), 2005-2017, from
  `cfe.cboe.com/publish/CFEinfocirc*`.
- The **holiday-calendar rules page** (`cfe_holiday_calendar_20190412.html`), which states the
  Monday-holiday, Thanksgiving, floating-holiday and Good Friday rules in session language.
- The **CFE Rule Book** (`cfe-rule-book.txt`) and **CFE Policies and Procedures**, for the Rule 402
  negative above.

### Indicative per-year cover — NOT yet a window basis

A first pass matching each fetched notice's text against the ten-holiday CFE set:

| Year | Holidays seen | Note |
|---|---|---|
| 2017 | 3 | Christmas, New Year, Thanksgiving only |
| 2018 | 5 | |
| 2019 | 4 | |
| 2020 | 9 | looks complete |
| 2021 | 8 | Labor Day not matched |
| 2022 | 7 | Independence, Juneteenth, Labor not matched |
| 2023 | 9 | Labor not matched |
| 2024 | 8 | |
| 2026 | — | already shipped from the live page and CSV |

**Do not set the window from this table.** It is a regex over file names and notice text, not a
derivation: "Labor not matched" may mean the notice is absent *or* that its subject carries a date
rather than the word, and a year that shows nine is not proved complete until each holiday is
resolved to a notice and the unobliged dates are confirmed normal. That is the phase-2 job, and it
is exactly the step where a shortcut would put an invented floor under a served identity.

**Phase 2, in order:** (1) resolve each of the ten holidays per year to a specific notice, listing
which are absent; (2) settle 2024 and 2025 against the live year-filtered
`cboe.com/us/futures/notices/schedule-update` index, whose filter reaches back to 2017 and which
was not yet read year by year; (3) set the window at the first year every holiday is either sourced
or explicitly audited normal; (4) record 2010-2014 — and any partial year below the floor — as a
named gap with its closing condition, and as an issue, since `cfe` is served.

## Phase 2, step 1 — the archive is far thinner than the file counts suggested

**A correction to the "Retrieval phase 1" section above, which must not be used.** The
`Cboe-Holiday-Reminder-*` files in `schedule_update/<YEAR>/` are **not CFE sources**. Read one:
`2024_Cboe-Holiday-Reminder-Modified-Trading-Hours-on-Memorial-Day.pdf` says *"The table below
outlines the modified trading schedules for the Cboe Options Exchanges (Cboe Options … Equities) in
observance of Memorial Day. All times referenced in this notice are ET."* — SPX/VIX/equities, ET,
nothing to do with CFE's Chicago futures session. Filtering to files that are actually CFE
(`CFE-*`, the ones that read "Cboe Futures Exchange, LLC (CFE) will have modified trading hours")
leaves **28 notices, not 77**.

Bucketed by the **holiday year each notice governs** (the directory year is the publication year,
and the New Year and MLK notices for year *N* sit in directory *N-1*), those 28 cover:

| Holiday year | CFE holidays sourced | Which |
|---|---|---|
| 2018 | 3 | Labor, Presidents, Thanksgiving |
| 2019 | 4 | Good Friday, Independence, Labor, MLK |
| 2020 | 2 | Labor, Memorial |
| 2021 | 5 | Good Friday, Independence, MLK, Memorial, Presidents |
| 2022 | 6 | Christmas, MLK, Memorial, New Year, Presidents, Thanksgiving |
| 2023 | 2 | MLK, Memorial |
| 2024 | 1 | Thanksgiving |
| 2025 | 1 | MLK |
| 2026 | 1 | Good Friday (2026 already ships from the live page and CSV) |

**No year is complete. Not one.** The best is 2022 at six of ten. The `schedule_update` archive on
its own therefore cannot put a floor under this identity at any year, which is the opposite of what
the previous section's table implied — and the reason that table is now marked unusable.

### What that leaves

The strongest CFE source is not the notices at all: it is the **holiday-calendar rules page**
(`cfe_holiday_calendar_20190412.html`), captured 2017-04 .. 2019-12, which states the *holiday set*
and the *hours for each holiday type* outright — Monday-observed holidays (MLK, Presidents,
Memorial, Labor) with Regular `None` and ETH to 10:30; Thanksgiving with the Friday
`8:30 a.m. to 12:15 p.m.`; and the floating set (New Year's, Good Friday, Independence, Christmas)
with its observed-day rules. That is a complete, deterministic holiday schedule for the years it
was in force, and the 28 notices corroborate individual dates within 2018-2019.

So the honest candidate window is **the span the rules page covers, 2017-2019**, with 2010-2016 a
gap. That is narrower than "2017 onward", and it is where the evidence actually is rather than
where the file counts pointed.

### Not yet done, and why it matters before a window is set

1. **The live year-filtered index was never read year by year.** `cboe.com/us/futures/notices/
   schedule-update` filters back to 2017 and its listing is client-rendered, so the CFE notices for
   2020-2025 may be live even though the archive holds few. If they are, the window widens
   substantially; if they are not, it stays 2017-2019.
2. **The rules page's own predecessor is unchecked.** Every capture found is 2017-04 or later, so
   the page cannot be carried below 2017 — but a Sitefinity-era equivalent under `cfe.cboe.com`
   has not been searched for directly.
3. **Juneteenth is absent from the rules page.** It was added to CFE's observed set in 2022, and
   the page as captured predates that, so a window reaching 2022+ needs the notice set, not the
   page.

## Phase 2, step 2 — the live CDN serves the notices, so the archive is not the limit

The three "not yet done" items above are now resolved, and one of them moves the plan.

**The live CDN serves `schedule_update` files directly.** Earlier attempts returned 403, which I
read as a block; re-testing with a browser user-agent and follow-redirects returns **200**:

```
200  30,425b  cdn.cboe.com/resources/regulation/circulars/general/CFE-IC-2017-001.pdf
200  34,486b  cdn.cboe.com/resources/schedule_update/2026/CFE-Modified-Trading-Hours-for-the-Good-Friday-Holiday.pdf
200  38,482b  cdn.cboe.com/resources/schedule_update/2024/CFE-Modified-Trading-Hours-for-the-Thanksgiving-Day-Holiday.pdf
200 2,043,583b cdn.cboe.com/resources/regulation/rule_book/cfe-rule-book.pdf
```

So the 403 was transient, and **live retrieval is available for these paths** — which is better
than the archive replay on every axis: it is the operator serving its own file, it needs no capture
date argument, and it does not depend on the Internet Archive, which went down mid-probe.

**What that means for the window.** The 28-notice archive ceiling is a property of the *archive*,
not of the operator. The CFE notices for the years the archive is missing are very likely live at
`cdn.cboe.com/resources/schedule_update/<YEAR>/<name>.pdf`. The one thing still missing is the
**enumerated filenames**: the live index is client-rendered and exposes no JSON endpoint I could
find (`/api/notices/schedule_update` is a 404; the only API reference on the page is
`cdn-api.cboe.com/api/global/system_status/system_status.json`), so the listing must be pulled from
the rendered page or the filenames derived from the established pattern and confirmed by a 200.

**Revised position on the floor.** This is the third revision of this file's conclusion, and the
direction has consistently been "more is reachable than the last survey said", so treat the floor
as **open above 2010 and probably above 2015** until the live enumeration is done. Do not write the
window from the archive counts. The two facts that are settled and will not change:

1. **2010-2014 has no source.** The rule book delegates (Rule 402), no pre-2015 holiday circular
   survives, and the rules page's earliest capture is 2017-04. Three families, each to its limit.
2. **The rules page is the strongest CFE document**, not the notices: captured 2017-04 .. 2019-12
   and stating the holiday set and per-type hours outright. Any window should be built page-first
   and notice-corroborated.

**Next, one step:** render the live `cboe.com/us/futures/notices/schedule-update` year by year (or
enumerate its filenames from the page's script payload), fetch every CFE notice live, and only then
count holidays per year and set the window.

## Phase 2, step 3 — the live listing settles the window: floor **2018-01-01**

The listing enumerates at a **path**, `cboe.com/markets/us/futures/notices/schedule-update/<YEAR>`
(the `?year=` query is ignored, and `/us/futures/notices/schedule-update` is a *different* page —
the System Status notices, which is what sent me wrong twice). Rendered headlessly for 2010-2027:

| Year | PDFs listed | CFE holiday notices |
|---|---|---|
| 2010-2017 | 0 | **0** |
| 2018 | 27 | 4 |
| 2019 | 18 | 8 |
| 2020 | 27 | 7 |
| 2021 | 28 | 10 |
| 2022 | 19 | 10 |
| 2023 | 23 | 10 |
| 2024 | 19 | 10 |
| 2025 | 11 | 10 |
| 2026 | 6 | 6 (year in progress) |
| 2027 | 0 | 0 |

**109 notice PDFs fetched live** (all of them, `live/`, indexed in `live_index.json` with URL and
sha256) and bukketted by the holiday each governs:

| Holiday year | Sourced | Missing |
|---|---|---|
| 2018 | 9 | Juneteenth |
| 2019 | 9 | Juneteenth |
| 2020 | 9 | Juneteenth |
| 2021 | 10 | — |
| 2022 | 10 | — |
| 2023 | 9 | New Year (the notice sits in the 2022 listing and governs 2023-01-02) |
| 2024 | 10 | — |
| 2025 | 10 | — |
| 2026 | 7 | Christmas, New Year, Thanksgiving (year in progress) |

Juneteenth is missing for 2018-2020 because **CFE did not observe it until 2022** — it became a US
federal holiday in 2021 and entered CFE's set the following year — so those years are complete for
the holiday set then in force, which the block must state rather than treat as a gap.

**The window is `2018-01-01 .. 2026-12-31`**, and **2010-2017 is the gap**: the live listing holds
no CFE notice before 2018, the rules page's earliest capture is 2017-04, and the archive's 2017
holdings are two notices (Christmas/New Year, Thanksgiving) — nowhere near a year. Together with
the Rule 402 negative and the absent pre-2015 circulars, 2010-2017 is an evidenced gap with a
closing condition, not an unfinished search.

`cfe` is served, so that gap becomes an issue, and the `Holidays` cell's floor is 2018-01-01 rather
than the identity's 2010-01-01 session horizon.

**Remaining for the CFE PR:** derive each notice's traded hours (they are per-product tables with
ETH/RTH columns, and the early closes differ by product), build the block, verify it independently,
encode the module, write the evidence file with the fixed `### Documents` shape, extend
`tests/futures_family_boundaries/holidays_cfe_vix.rs`, move the two ledger rows (`cfe`, `cfe_vix`),
and update the CHANGELOG and the plan note.

## Phase 2, step 4 — the derivation rule, validated against the rows already shipped

Every CFE holiday notice has the same shape: an **"observed on \<Weekday\>, \<Month d, yyyy\>"**
line, then a day-column table whose sub-columns are `ETH Start / ETH Close / ETH Start / RTH Start
/ RTH Close / ETH Close`, then a `Trade Date` row naming the trade date of the **last** column.

The product label for the crate's family drifts and must be matched loosely — 2024 reads
`Volatility Index Futures*`, 2026 reads `Volatility and Equity Index Futures*` (VX, VXT, VXM, VXMT,
MGTN). A parser keyed on the exact string silently returns nothing for half the corpus; this is the
same failure that produced the "no text" rows in `notices_digest.txt`.

**The rule, confirmed by reproducing the shipped 2026 rows:**

| Holiday | CFE session on the holiday trade date | crate kind |
|---|---|---|
| Monday-observed (MLK, Presidents, Memorial, Labor) | ETH 17:00 prior day → **10:30** holiday; RTH `None` | `EarlyClose(10:30 CT)` |
| Juneteenth, Independence Day (Fri or observed) | as above | `EarlyClose(10:30 CT)` |
| Good Friday | overnight leg ends at the regular open, no RTH | `EarlyClose(08:30 CT)` |
| Thanksgiving Day | ETH 17:00 Wednesday → **10:30** Thursday; RTH `None` | `EarlyClose(10:30 CT)` |
| Friday after Thanksgiving | ETH 17:00 Thursday → **12:15** Friday | `EarlyClose(12:15 CT)` |
| Christmas Eve / New Year's Eve half days | **12:15** | `EarlyClose(12:15 CT)` |
| Christmas Day, New Year's Day | no session | `Closed` |

Worked check against the module already in `main`: the Juneteenth 2026 notice (observed Friday
June 19) prints `ETH Start 5:00 PM` under THURSDAY, `ETH Close 10:30 AM` under FRIDAY, and its
`Trade Date` row names Monday June 22 — so trade date **2026-06-19 closes at 10:30 CT**, which is
exactly the `early_close(10 * 3_600 + 30 * 60)` row that ships. The same reading of the MLK 2025
and Thanksgiving 2024 notices reproduces their rows too.

**Two grid facts the derivation must respect.** The venue's own RTH close moved **15:15 → 15:00 CT
at the 2021-12-06 revision** and the extended topology changed at 2010-12-10, 2011-09-26,
2013-10-28, 2013-11-04, 2014-06-22 and 2018-02-25 — so a holiday row only *ships* when the notice's
hours differ from the grid in force for that date. Read `src/calendar/schedules/futures/us/cfe.rs`'s
dated `revisions!` before deciding that a row moves anything, exactly as the CDE PR had to.

**Remaining work, all mechanical given the above:** parse the 109 notices into `(holiday date, VX
row)`; drop the rows the era's grid already states; build the block; verify it independently; encode
`src/calendar/schedules/holidays/cfe.rs` for a window of `2018-01-01 .. 2026-12-31`; write
`docs/evidence/cfe.md` and `cfe_vix.md` in the fixed `### Documents` shape; extend
`tests/futures_family_boundaries/holidays_cfe_vix.rs`; move the `cfe` and `cfe_vix` `Holidays` cells;
add the CHANGELOG entry and the plan note; open the PR with the 2010-2017 gap as issue #113-style
follow-up.

## Phase 2, step 5 — derivation state, honestly (2026-09-21 UTC)

I built the extractor on exact word coordinates (`pdftotext -bbox`) and **validated it against the
rows already in `main`**: it reproduces all six 2026 CFE notice rows exactly —
Good Friday `early_close(08:30)`, and MLK, Presidents, Juneteenth, Independence, Memorial and Labor
at `early_close(10:30)`. That validation is the reason to trust it at all, and it is reproducible
with `parse_cfe.py` + `derive_cfe.py` in this directory.

What it derives cleanly:

| Year | Rows | Complete? |
|---|---|---|
| 2023 | 10 | **yes** — every CFE holiday |
| 2024 | 10 | **yes** |
| 2025 | 9 | missing Christmas Day |
| 2026 | 8 | Jan-Sep; Nov/Dec come from the live CSV, which already ships |
| 2022 | 2 | only Independence and Labor |

**Good Friday varies by year and the parser gets it right**: 2023 and 2026 print an 08:30 close,
while 2024 and 2025 have *no* VX times in the holiday column at all — a full closure. I checked the
2024 notice by eye after assuming it was a bug; the parser was correct and my assumption was wrong.

**The blocker is layout, not logic.** The CFE notices come in at least three table layouts:

1. **Modern** (2023-2024, most of 2025-2026): a day-header row over six `ETH/RTH Start/Close`
   sub-columns. Parsed and validated.
2. **Pre-2022** (2018-2022): the table carries **no `ETH`/`RTH` labels and no `Trade Date` row at
   all** — a different, simpler layout. 36 notices.
3. **Stacked sub-headers** (the 2025 Christmas notice): the sub-column labels are broken across
   several lines, so a sub-header *line* does not exist to read.

Handling (2) and (3) is a second and third parser, not a tweak. That is where this stands, and it
is a PDF-extraction problem rather than an evidence problem — the artifacts are all saved with
URL and sha256 in `live_index.json`.

**Consequence for the window.** The window cannot honestly be wider than the years whose holidays
are all derived. On today's state that is **2023 and 2024**, with 2025 one notice short — which is
much narrower than the `2018-01-01` floor the listing supports. The corpus is complete to 2018; it
is the *extraction* that is incomplete, and the difference matters: this is "not yet worked up",
not "no source exists".
