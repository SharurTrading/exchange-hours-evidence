# CDE late-2026 notices — verbatim operative lines

Coinbase Derivatives, LLC (CDE). Every quotation below is read from the `pdftotext -layout` dump of the
PDF saved beside this file (`pdf/`, dumps in `txt/`). The dumps are whitespace-wrapped, so a quote is
compared after collapsing whitespace runs; nothing else is altered. Retrieval session
**2026-09-26 07:18 UTC** (all times UTC, LAW-UTC-DATES).

Scope: the four notices the earlier store (`../cde-2021-2025/`) recorded as **not retrieved**, plus the
two notices published after 26-36. These are the documents that change how the late-2026 and 2027
holiday/maintenance picture reads.

---

## 26-25 — Removal of Weekly 1-Hour Friday Maintenance Window

- **Document:** `pdf/CDE_Market_Notice_26-25_Removal_of_Weekly_1-Hour_Friday_Maintenance_Window.pdf`
- **Listing row:** 26-25 · Market · published 05/20/2026 · effective 07/24/2026 · Maintenance
- **PDF header:** `Notice: 26-25` / `Date: 05/20/2026` / `Subject: Removal of Weekly 1-Hour Friday Maintenance Window`

Verbatim, Summary (p.1):

> Effective July 24, 2026 at 17:00 CT, Coinbase Derivatives, LLC ("CDE" or "Exchange") will
> remove the weekly 1-hour Friday maintenance window currently observed from Friday 16:00
> CT to Friday 17:00 CT for 24x7 enabled products. The final Friday maintenance will occur July
> 24, 2026 from 16:00 to 17:00 CT.

> After this date, CDE deployments/releases will occur during market hours ("Open" trading state)
> and will be announced via https://status.cde.coinbase.com/.

Verbatim, Customer Impact (p.1):

> - The weekly 1-hour Friday trading close will no longer occur after July 24, 2026.
> - 24x7 enabled products previously affected by the Friday 16:00 - 17:00 CT break will now
>   trade continuously throughout the week, subject only to the scheduled maintenance
>   windows listed below.
> - **The trade date will roll Friday at 16:00 CT, and all trades executed after the roll will clear
>   on the next trading date.**
> - Customers should ensure that internal systems, trading applications, and connectivity
>   processes are updated to reflect the new schedule.
> - Products that are not 24x7 enabled are unaffected by this change and will continue to
>   observe their existing trading schedules.

Verbatim, New Maintenance Window Schedule (p.2):

> To support the transition away from the weekly 1-hour Friday maintenance window, CDE will
> introduce additional weekend maintenance windows. The schedule below reflects the planned
> maintenance dates for the next year, during which all CDE products will be unavailable.

> Each maintenance window will be three (3) hours in duration, with one (1) extended
> maintenance window annually to accommodate the FIA Disaster Recovery (DR) exercise.
> Additional start times will be communicated closer to the event.

> - July 25, 2026 @ 9:00AM CT — Standard Weekend Maintenance
> - September 12, 2026 — Standard Weekend Maintenance
> - October 24, 2026 — Standard Weekend Maintenance & FIA DR
> - December 12, 2026 — Standard Weekend Maintenance
> - February 13, 2027 — Standard Weekend Maintenance
> - April 10, 2027 — Standard Weekend Maintenance
> - June 12, 2027 — Standard Weekend Maintenance

**Superseded in part.** 26-33 (below) states that it "revises the Production date in 26-25"; the
July 24, 2026 removal did not stand. The 2027 dates in the list above are weekend maintenance
windows, not holiday closures.

---

## 26-33 — 24x7 Transition: Rolling Gateway Deploys and Final Friday Maintenance Windows

- **Document:** `pdf/CDE_Market_Notice_26-33_24x7_Transition__Rolling_Gateway_Deploys_and_Final_Friday_Maintenance_Windows.pdf`
- **Listing row:** 26-33 · Market · published 07/13/2026 · effective 09/14/2026 · Maintenance
- **PDF header:** `Notice: 26-33` / `Date: 07/13/2026`

Verbatim, Summary (p.1):

> The revised weekly Friday maintenance windows (16:00–16:50 CT, removal effective 17:00 CT)
> are:
> - Integration (UAT): Friday, July 24, 2026
> - Production: Friday, September 11, 2026

> After each environment's final Friday window, TRUE_24X7 products will remain OPEN and
> trade continuously, subject only to the scheduled weekend maintenance windows.

> At the final Friday window in each environment, all products that currently support weekend
> trading (the weekend trading set, comprising all crypto futures plus Gold and Silver futures)
> transition to a TRUE_24X7 trading schedule and trade continuously thereafter, subject only to
> scheduled weekend maintenance windows (see market notices). Products that do not trade on
> weekends currently are unaffected.

> This Market Notice supersedes 26-13 and **revises the Production date in 26-25**.

Verbatim, In Scope table, final row (p.2):

> 4.1 (GoLive) — Final Friday maintenance window. All 24x7-enabled products (crypto futures plus
> Gold and Silver) flip to TRUE_24X7 and trade continuously. — Friday, Sept 11, 2026 16:00-16:50

Internal inconsistency, quoted so it is not lost: the milestone bullet reads "24x7-enabled
products (crypto, gold and silver) trade continuously beginning Friday, Sept 18" while the
table above puts the GoLive flip on **Friday, Sept 11, 2026 16:00-16:50**. Both dates were
later withdrawn (see 26-33.1, 26-33.2).

---

## 26-33.1 — Updated Dates on 24x7 Transition

- **Document:** `pdf/CDE_Market_Notice_26-33.1_Updated_Dates_on_24x7_Transition__Rolling_Gateway_Deploys_and_Final_Friday_Maintenance_Windows.pdf`
- **Listing row:** 26-33.1 · Market · published 08/05/2026 · effective 08/14/2026 to Oct 2026 · Maintenance
- **PDF header:** `Notice: 26-33.1` / `Date: 08/05/2026`

Verbatim, Summary (p.1):

> This notice amends Market Notice 26-33 (published 07/13/2026) to reflect a revised event
> schedule and updated final Friday maintenance windows.

> The revised weekly Friday maintenance windows (16:00–16:50 CT, removal effective 17:00 CT)
> are:
> - Integration (UAT): September 2026 (date to be announced)
> - Production: October 2026 (date to be announced)

> After each environment's final Friday window, TRUE_24X7 products will remain OPEN and
> trade continuously, subject only to the scheduled weekend maintenance windows.

Verbatim, Key Milestones by Service (p.1–2):

> - Event 3.0 (date to be announced): first event to include Drop Copy; use
>   EventResendRequest to recover missed ExecutionReports from this date forward.
> - Event 4 / GoLive (**Early Q4 2026, date TBA**): final Friday maintenance window. After this,
>   rolling deploys may occur any time during trading hours, and 24x7-enabled products
>   (crypto, gold and silver) trade continuously thereafter.

---

## 26-33.2 — Updated dates and scope on 24x7 Transition

- **Document:** `pdf/CDE_Market_Notice_26-33.2_Updated_Dates_on_24x7_Transition_-_Rolling_Gateway_Deploys_and_Final_Friday_Maintenance_Windows.pdf`
- **Listing row:** 26-33.2 · Market · published 09/10/2026 · effective 09/11/2026 · Maintenance
- **PDF header:** `Notice: 26-33.2` / `Date: 09/10/2026`

Verbatim, Summary (p.1):

> This notice amends Market Notice 26-33.1 (published 08/05/2026) to revise the Production
> rolling-deploy schedule, describe hourly rolling deploys in Integration, and confirm that
> remaining dates will be announced in subsequent market notices. Subsequent market notices
> will be published for:
> - FIX Order Entry
> - Drop Copy
> - **Updated final GoLive date for removal of the Friday maintenance window**

> At the final Friday window in each environment, all products that currently support weekend
> trading (the weekend trading set, comprising all crypto futures plus Gold and Silver futures)
> transition to a TRUE_24X7 trading schedule and trade continuously thereafter, subject only to
> scheduled weekend maintenance windows (see market notices). Products that do not trade on
> weekends currently are unaffected.

Verbatim, Key Milestones by Service — Production (p.2):

> - Friday, Sept 11, 2026: Market Data and SBE Order Entry (B-side only)*
> - Friday, Sept 18, 2026: Market Data and SBE Order Entry (B-side only)*
> - Friday, Sept 25, 2026: Market Data and SBE Order Entry Full (B-side then A-side)*

> After Friday, Sept 25, 2026, through GoLive: clients should plan for Market Data and SBE Order
> Entry Full (B-side then A-side) each Friday at approximately 14:30 CT. This includes Fridays
> that still have the weekly 16:00–16:50 CT maintenance window.

> TradingSessionID (336) is enabled in Production per Market Notice 26-32. The value flips to
> TRUE_24X7 for 24x7-enabled instruments at the final Friday window (not on the rolling-deploy
> dates above).

> A reminder that the Saturday maintenance scheduled for Saturday, Sept 12, 2026 is canceled.

Verbatim, Products Transitioning to TRUE_24X7 (p.4):

> The following 48 products currently support weekend trading and will transition to a TRUE_24X7
> schedule at the final Friday window in each environment. All other products retain their current
> trading hours and are unaffected.

(The 48 products are tabulated on pp. 4–5 of the PDF: 1k Shib Fut SHB 1776 … Zcash Perp ZEC
11666, including Gold Futures GOL 1587 and Silver Futures SLR 2141.)

---

## 26-33.3 — amendment to 26-33.2 and 26-25 (listed, PDF not retrieved)

- **Listing row:** 26-33.3 · Market · **published 09/24/2026** · **effective 09/25/2026** · Maintenance
- **Title as published:** `Amendment to 26-33.2 and 26-25: Rolling Gateway Deploys Postponed and Upcoming Maintenance Windows`
- **URL:** not obtainable on 2026-09-26 (see `INDEX.md`, "Access"). The listing page carries the href in
  its embedded Contentful payload; only the rendered text could be retrieved, so the
  `assets.ctfassets.net/...` address of the PDF is unknown.
- **Why it matters:** it amends both 26-33.2 (the rolling-deploy schedule) and 26-25 (the Friday
  maintenance window), and its effective date 2026-09-25 is the Friday the 26-33.2 schedule called
  for a "Market Data and SBE Order Entry Full (B-side then A-side)" rolling deploy at ~14:30 CT.

## 26-37 — Q4 quarterly maintenance (listed, PDF not retrieved)

- **Listing row:** 26-37 · Market · **published 09/24/2026** · **effective 10/24/2026** · Maintenance
- **Title as published:** `CDE Q4 Quarterly Maintenance Window & FIA DR Testing - Details`
- **URL:** not obtainable on 2026-09-26 (same cause as 26-33.3).
- **Why it matters:** 2026-10-24 is the date 26-25 lists as "Standard Weekend Maintenance & FIA DR".

---

## Holiday notices after 26-36

**None published as of 2026-09-26.** The newest holiday-category row in the operator's own listing is
**26-36 (published 08/25/2026, effective 09/07/2026, "2026 Labor Day")**. There is no Thanksgiving 2026,
no Christmas 2026 and no 2027 holiday notice on the listing yet. (Calendar precedent: 25-37
"2025 Thanksgiving Schedule" was published 2025-10-30 and 25-41 "2025 Christmas" on 2025-11-25, so the
2026 equivalents are not yet due.)

## Baseline market-hours page

`https://docs.cdp.coinbase.com/derivatives/introduction/market-hours` retrieved 2026-09-26 07:16:40 UTC
(`cdp_derivatives_market_hours_20260926.html`, 1,040,125 bytes). Compared sentence-by-sentence against the
store's 2026-09-12 capture (`../cfe-eurex-ice-cde-smfe-2026-2027/cde_market_hours.md`): **no substantive
change**. The operative lines cited by the crate are identical in both:

> To allow participants and vendors to deploy updates, CDE will have a weekly 50-minute downtime
> where all markets, including 24x7 futures products, are closed Friday* at 4:00 PM CT until 4:50 PM CT.
> ... *In the event of a Friday holiday, the maintenance window is pushed up to Thursday.

> Sequence numbers on Gateways (FIX Market Data, FIX Order Entry, FIX Drop Copy) are automatically
> reset by CDE every Friday at 4:05 PM CT.

> Trades executed Friday after 5:00 PM CT through Sunday will be recorded with a Monday trading date.
> If a market holiday occurs, trades will clear on the next trading day.

**Read against the notices.** The page still describes the pre-transition grid (a 50-minute Friday
window, 4:00–4:50 PM CT). 26-25 described the window as a full hour (16:00–17:00 CT) and 26-33/26-33.1/
26-33.2 as "16:00–16:50 CT, removal effective 17:00 CT". The removal has no announced date: it is
"October 2026 (date to be announced)" / "Early Q4 2026, date TBA". **No date for the removal is encodable.**

---

## Supplementary: the operator's status feed (T2)

`https://status.cde.coinbase.com/` retrieved 2026-09-26 07:23:32 UTC, saved as
`cde_status_page_20260926.html` / `.txt`. It is fetchable directly (no block) and links notice 26-33.2's
PDF, so it corroborates the copy held here. Two entries bear on the late-2026 grid:

1. **The Friday window was still running on 2026-09-25.** Past Incidents lists "Friday Maintenance
   Window 260925": *Scheduled* 2026-09-25 19:11 UTC, *In progress* 21:05 UTC, *Completed* 22:00 UTC
   (= 16:00–17:00 CT). So the removal described in 26-25 had not taken effect, and 26-33.3's
   "Rolling Gateway Deploys Postponed" is consistent with the same day showing no in-market-hours
   rolling deploy.
2. **The window's length is stated inconsistently across the operator's own channels.** The status
   feed's 2026-09-18 entry reads: *"The rolling deployment maintenance during market hours has been
   canceled. Our standard 1-hour weekly downtime from 17:00 to 18:00 ET will proceed as scheduled."*
   (17:00–18:00 ET = 16:00–17:00 CT, one hour). The CDP market-hours page says 50 minutes
   (4:00–4:50 PM CT) and 26-33/26-33.1/26-33.2 say "16:00–16:50 CT". For a `Maintenance` gap the
   difference is one ten-minute slice at the end of the window, and LAW-PRIMARY-SOURCES' conflict rule
   applies: serve the window both statements agree on, withhold the disputed remainder, and record both.

