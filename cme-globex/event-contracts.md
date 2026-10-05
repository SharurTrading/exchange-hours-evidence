# event-contracts

**Products:** CME Group "Event Contracts" on futures — daily-expiring, cash-settled, European-style binary options on futures, CME/CBOT/NYMEX/COMEX Rulebook Chapter 23. Eleven Globex roots, all confirmed still listed in CME's July 2026 event-contract specification PDF:

ECES  (Event Contracts on E-mini S&P 500 futures, CME 23A, underlying ES)
ECNQ  (E-mini Nasdaq-100, CME 23B, underlying NQ)
ECRTY (E-mini Russell 2000, CME 23C, underlying RTY; clearing code truncates to ECRT — CME's own docs also mis-spell it "ERTY")
ECYM  (E-mini Dow, CBOT 23A, underlying YM)
EC6E  (Euro/U.S. Dollar FX, CME 23D, underlying 6E)
ECCL  (Light Sweet Crude Oil, NYMEX 23D, underlying CL)
ECNG  (Henry Hub Natural Gas, NYMEX 23E, underlying NG)
ECGC  (Gold, COMEX 23A, underlying GC)
ECSI  (Silver, COMEX 23B, underlying SI)
ECHG  (Copper, COMEX 23C, underlying HG)
ECBTC (Bitcoin Futures, CME chapter 23, underlying BTC — added later, see revisions)

SCOPE WARNING for the crate: CME now sells several *different* product families under the "event contract"/"Prediction Markets" umbrella, and they do NOT share this profile. Do not fold these in:
  - Swap-based economic/crypto event contracts (ECCPI, ECGDP, ECNFP, ECUNE, ECPCE, ECFD; CCB10/CCB11/CCB13/CCB15/CCB16 hourly Bitcoin/Ether) — CME Rulebook Chapter 22, listed per SER-9586RR, with a wholly different grid ("a one (1) minute trading halt each day from 5:00 P.M. ET to 5:01 P.M. ET" plus "the CME Globex maintenance period of 3:00 A.M. ET - 5:00 A.M. ET on Saturday and Tuesday").
  - Hourly Event Contracts on futures (SER-9624, Oct 15 2025): "CME Globex: Sunday 6:00 p.m. - Friday 5:00 p.m. ET with a daily maintenance period from 5:00 p.m. - 6:00 p.m. ET".
  - Sports/political event contracts (FG*/FS*/NG* team codes, CME FSPI).

**Timezone:** America/Chicago.

Verbatim, SER-8968R (launch document), Contract Specifications table: "All times are in Central Time (CT)"
Source: https://www.cmegroup.com/notices/ser/2022/08/SER-8968R.pdf

Verbatim, SER-9092 (ECBTC listing): "All times are in Central Prevailing Time (CPT)"
Source: https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2023/02/SER-9092.pdf

Verbatim, CME activetrader contract-specifications page: "CME Globex Trading Hours / All times are in central Prevailing Time (CPT)"
Source: https://web.archive.org/web/20250916234845id_/https://www.cmegroup.com/activetrader/event-contracts/contract-specifications-for-event-contracts.html

"Central Prevailing Time" = America/Chicago with US DST. The 2026 24/7 client impact assessment likewise states every boundary in "CT".

**Confidence:** high

## Reuse verdict

DIRECT ANSWER TO THE KEY QUESTION: Yes, multiple profiles are required — but the shape is NOT the one the audit assumed. The audit expected "several underlying-specific profiles pre-2026, collapsing to one 24/7 profile afterwards." That is wrong. The correct shape is SIX profiles before 2026-05-29 and SEVEN after, because only ECBTC went 24/7 and the other ten roots never collapsed into anything.

PROFILE COUNT AND MEMBERSHIP
  P1  ECES, ECNQ, ECRTY, ECYM   T=15:00:00   (ECBTC also a member 2023-03-12 .. 2026-05-28)
  P2  EC6E                       T=14:00:00
  P3  ECCL, ECNG                 T=13:30:00
  P4  ECGC                       T=12:30:00
  P5  ECSI                       T=12:25:00
  P6  ECHG                       T=12:00:00
  P7  ECBTC                      near-24/7, from 2026-05-29 only

WHY THESE CANNOT BE COLLAPSED INTO ONE ANOTHER
The six legacy profiles differ ONLY in the daily termination time T, but they differ in it by as much as three hours (12:00 vs 15:00). Every other element — the Sunday 16:00-17:00 pre-open, the Monday-Thursday 16:45-17:00 pre-open, the 17:00 open, the no-Friday-evening-reopen, the weekend close — is shared verbatim across all of them ("All Contracts: CME Globex Pre Open: Sunday 4:00 - 5:00 p.m. Monday - Thursday 4:45 - 5:00 p.m."). So they are six genuine profiles, not six coincidentally-similar ones; if the crate models a per-profile daily close, six keys are unavoidable. P5 (ECSI, 12:25:00) is the strongest argument against any merging heuristic: it sits five minutes from P4 (ECGC, 12:30:00), so any tolerance-based collapse would silently corrupt one of them.

WHY THEY CANNOT REUSE THE UNDERLYING FUTURES' PROFILES (the tempting wrong answer)
The audit's phrasing — "ECCL followed crude, ECGC followed gold" — invites reusing the crude/gold/equity-index keys. Do not. The event contract tracks the underlying's daily SETTLEMENT time, not the underlying's Globex close, and those are different instants. CME's own wording is the proof: "Daily products: trading will terminate at the end of the daily settlement period of the Underlying Futures contract." A settlement window ends hours before the underlying's Globex session does; ECES stops at 15:00 and stays dark until 17:00, whereas ES itself keeps trading past 15:00. The event contracts therefore need their OWN keys, semantically anchored to settlement times, even though the numbers were derived from the underlying complexes. (I did not re-verify the underlying futures' grids in this session — that assertion rests on the CME termination-of-trading language, not on a fresh reading of the ES/GC/CL specs.)

WHY P7 MUST BE ITS OWN KEY AND MUST NOT BE REUSED FROM CRYPTO
ECBTC's post-2026 grid is superficially "24/7 like the crypto complex" and the notices explicitly say the technology and timeline align with the cryptocurrency migration. Resist reusing a crypto key on that basis. ECBTC's daily maintenance is 15:00:00-16:02:00 — it inherited the 15:00 close from its old equity-index-settlement group, not from crypto — and its Saturday extended window is 02:00-04:00. A crypto key derived from the Cryptocurrency Futures and Options 24/7 migration is a different document with different boundaries; I did not read it and cannot vouch that the numbers match. Semantically ECBTC is a Chapter 23 event contract whose close is a settlement-time artifact, so it deserves its own key regardless of envelope coincidence.

ON THE "DON'T JUSTIFY REUSE FROM A MATCHING CURRENT ENVELOPE" RULE
P1 and P2 currently differ, so no temptation arises there. But note the trap in the other direction: from 2023-03-12 to 2026-05-28 ECBTC's envelope was IDENTICAL to ECES/ECNQ/ECRTY/ECYM, and CME's own specification page listed them on one line ("ECES; ECNQ; ECRTY; ECYM; ECBTC | Sunday 5:00 p.m. - Friday 3:00 p.m."). A crate that assigned ECBTC the P1 key on that evidence would have been silently wrong from 2026-05-29 onward. ECBTC's underlying is Bitcoin futures, a product family CME was always going to move to weekend trading; that product-family semantics, not the matching envelope, is what should have driven the key. Give ECBTC its own key across its whole history (2023-03-12 onward), with a revision at 2026-05-29 — do not alias it to P1 for the first three years and then fork it.

HISTORY FLOOR
Not engaged. The family's first sourced listing is 2022-09-18, well above the crate's January-2010 floor, so no floor-clamping question arises. ECBTC's own history must begin 2023-03-12, the first date a primary source lists that product.

## Current grid

TIMEZONE America/Chicago throughout. Closes are END-EXCLUSIVE below. As of today (2026-09-05) the family splits into SEVEN grids: ECBTC on a near-24/7 grid since 2026-05-29, and six legacy grids that are UNCHANGED since the 2022-09-18 launch.

=====================================================================
CRITICAL FINDING — the audit's premise is only one-eleventh true.
=====================================================================
The 2026-05-29 "24/7" transition applied to ECBTC ONLY. The other ten roots did NOT collapse into a 24/7 profile and still run their original underlying-specific closes.

VERBATIM (CME Client Systems Wiki, "Event-Based Contracts Expansion to 24-7 Trading", section "Product Scope"):
  "With this launch, only the below event contracts on Bitcoin on channel 329 will migrate to weekend trading. Other event contracts will continue on the current schedule."
and the Product Scope table under that sentence contains exactly ONE row:
  "Event contracts on Bitcoin Futures | ECBTC | VB | 329 | 74"
URL (public, no auth, HTTP 200 with a browser UA and no cookies):
  https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Event-Based+Contracts+Expansion+to+24-7+Trading

Note the wording tension I resolved: the 2026-03-30 Globex Notice said "CME Group will expand event contracts to 24/7 trading, including event contracts on Bitcoin futures" (reads as all of them); the 2026-05-25 Globex Notice, flagged "Update", narrowed it to "expand the event contracts MDP channel (id=329) to 24/7 trading"; the client impact assessment (revised April 22, 2026) settles it to ECBTC alone. I confirmed no later reversal through the CME Globex Notice of 2026-08-17, the most recent I read.

=====================================================================
GRID 1 — ECBTC (in force since 2026-05-29 16:00 CT)
=====================================================================
VERBATIM (same wiki, section "Event-Based Contract Maintenance Windows and Market Hours" — "This section outlines schedule impacts for all clients trading event-based contracts and currently applicable to Bitcoin event-based contracts."), table rows exactly as published:

  "Saturday | Extended Maintenance Window | Close: 2:00 a.m. to 3:45 a.m. CT | Pre-open: 3:45:00 a.m. to 4:00:00 a.m. CT  No cancel: 3:59:30 a.m. to 4:00:00 a.m. CT  Open: 4:00 a.m. CT"

  "Monday through Friday | Daily Maintenance Window (with Trade Date roll) | Close: 3:00:00 p.m. to 4:01:00 p.m. CT | Pre-open: 4:01:00 p.m. to 4:01:30 p.m. CT  No cancel: 4:01:30 p.m. to 4:02:00 p.m. CT  Open: 4:02:00 p.m. CT"

  "The CME Globex Sunday startup will be eliminated for event contracts."
  "Sequence numbers for iLink, Drop Copy, and market data will reset to 1 during the new Saturday startup."
URL: https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Event-Based+Contracts+Expansion+to+24-7+Trading

Derived model (seconds since venue-local midnight):
  regular (executable), Mon-Fri: 57720 (16:02:00) -> next day 54000 (15:00:00)   [wraps midnight]
  regular (executable), Sat:     14400 (04:00:00) -> Sun 86400, continuing Sun 0 -> Mon 54000  [no 15:00 halt Sat or Sun; the daily-maintenance row is scoped "Monday through Friday"]
  regular (executable), Fri eve: 57720 (16:02:00) -> Sat 7200 (02:00:00)
  order_entry, Mon-Fri: 57660 (16:01:00) -> 57720 (16:02:00)   [pre-open 16:01:00-16:01:30 + no-cancel 16:01:30-16:02:00 - both are non-matching queue]
  order_entry, Sat:     13500 (03:45:00) -> 14400 (04:00:00)   [pre-open 03:45:00-04:00:00 + no-cancel 03:59:30-04:00:00]
  final daily close: YES, Mon-Fri only, at 54000 (15:00:00).
  weekend close: NO. ECBTC trades across Saturday and Sunday.

Corroboration that 16:02:00 CT is the real reopen for this market segment: CME Globex Notice, August 17, 2026, on 100-Ounce Silver futures migrating to the same channel 329 / market segment 74: "All subsequent Friday trading sessions will open at their regular time of 4:02 p.m. CT."
URL: https://www.cmegroup.com/notices/electronic-trading/2026/08/20260817.html

=====================================================================
GRIDS 2-7 — the other ten roots (UNCHANGED since 2022-09-18)
=====================================================================
VERBATIM (SER-8968R, Aug 25 2022, "Trading Hours" row of the Contract Specifications table):

  "All Contracts: CME Globex Pre Open: Sunday 4:00 - 5:00 p.m. Monday - Thursday 4:45 - 5:00 p.m."
  "ECES; ECNQ; ERTY; ECYM: Sunday 5:00 p.m.- Friday 3:00 p.m. - Next day's Event Contract will list at 5:00 p.m."
  "EC6E: Sunday 5:00 p.m.- Friday 2:00 p.m. - Next day's Event Contract will list at 5:00 p.m."
  "ECGC: Sunday 5:00 p.m.- Friday 12:30 p.m. - Next day's Event Contract will list at 5:00 p.m."
  "ECSI: Sunday 5:00 p.m.- Friday 12:25 p.m. - Next day's Event Contract will list at 5:00 p.m."
  "ECHG: Sunday 5:00 p.m.- Friday 12:00 p.m. - Next day's Event Contract will list at 5:00 p.m."
  "ECCL: ECNG: Sunday 5:00 p.m.- Friday 1:30 p.m. - Next day's Event Contract will list at 5:00 p.m."
URL: https://www.cmegroup.com/notices/ser/2022/08/SER-8968R.pdf

And, defining WHY the closes differ by underlying (verbatim, CME activetrader contract-specifications page, "Termination of Trading"):
  "Daily products: trading will terminate at the end of the daily settlement period of the Underlying Futures contract. Contract listed on the Principal Contract Month of the Underlying Futures."
URL: https://web.archive.org/web/20221201010119id_/https://www.cmegroup.com/activetrader/event-contracts/contract-specifications-for-event-contracts.html

Common shape for all six groups (T = that group's daily termination time):
  Sunday:        order_entry 57600 (16:00:00) -> 61200 (17:00:00); then regular opens 61200
  Mon-Thu:       regular runs 61200 (17:00:00) -> next day T  [wraps midnight]; on close at T the market is dark until 60300
                 order_entry 60300 (16:45:00) -> 61200 (17:00:00); then regular opens 61200
  Friday:        regular ends at T. NO Friday-evening reopen (the pre-open row lists Sunday and Monday-Thursday only).
  final daily close: YES, at T. weekend close: YES, from Friday T to Sunday 16:00:00.

The six T values (this is the whole reason multiple profiles are required):
  GRID 2  T = 54000 (15:00:00)  ECES, ECNQ, ECRTY, ECYM      [equity-index settlement]
  GRID 3  T = 50400 (14:00:00)  EC6E                          [FX settlement]
  GRID 4  T = 48600 (13:30:00)  ECCL, ECNG                    [NYMEX energy settlement]
  GRID 5  T = 45000 (12:30:00)  ECGC                          [COMEX gold settlement]
  GRID 6  T = 44700 (12:25:00)  ECSI                          [COMEX silver settlement]
  GRID 7  T = 43200 (12:00:00)  ECHG                          [COMEX copper settlement]

Persistence of these six grids to the end of CME's own publication of them — the last archived capture of the specs page, 2025-09-16, is byte-identical in the hours table to the 2024-03-30 capture:
  "ECES; ECNQ; ECRTY; ECYM; ECBTC | Sunday 5:00 p.m. - Friday 3:00 p.m. | Next Day's Event Contract will list at 5:00 p.m."
  "EC6E | Sunday 5:00 p.m. - Friday 2:00 p.m."
  "ECSI | Sunday 5:00 p.m. - Friday 12:25 p.m."
  "ECHG | Sunday 5:00 p.m. - Friday 12:00 p.m."
  "ECCL; ECNG | Sunday 5:00 p.m. - Friday 1:30 p.m."
  "All Contracts: CME Globex Pre Open: Sunday 4:00 - 5:00 p.m. Monday - Thursday 4:45 - 5:00 p.m."
URL: https://web.archive.org/web/20250916234845id_/https://www.cmegroup.com/activetrader/event-contracts/contract-specifications-for-event-contracts.html

=====================================================================
RTH vs ETH: NOT SOURCEABLE. See `unsourced`. No CME document I retrieved classifies any part of this family's session as Regular vs Extended; every source publishes a single undifferentiated "CME Globex Trading Hours" window plus a pre-open. I have therefore placed the entire executable window in `regular` and only the pre-open / no-cancel queues in `order_entry`. That placement is a modelling default, not a sourced fact.

## Dated revisions

### 2022-09-18 — LAUNCH of the family (ten roots: ECES, ECNQ, ECRTY, ECYM, EC6E, ECCL, ECNG, ECGC, ECSI, ECHG) with six distinct underlying-specific daily closes and a shared pre-open. Grid: pre-open Sunday 16:00:00-17:00:00 and Monday-Thursday 16:45:00-17:00:00; executable Sunday 17:00:00 through Friday T, dark each day from T to 16:45:00, no Friday-evening reopen, weekend close from Friday T to Sunday 16:00:00. T = 15:00:00 for ECES/ECNQ/ECRTY/ECYM; 14:00:00 for EC6E; 13:30:00 for ECCL/ECNG; 12:30:00 for ECGC; 12:25:00 for ECSI; 12:00:00 for ECHG. All times America/Chicago.

- Citation: https://www.cmegroup.com/notices/ser/2022/08/SER-8968R.pdf
- Verbatim: Effective Sunday, September 18, 2022, for trade date Monday, September 19, 2022, and pending all relevant CFTC regulatory review periods, Chicago Mercantile Exchange Inc. (“CME”), The Board of Trade of the City of Chicago, Inc. (“CBOT”), New York Mercantile Exchange, Inc. (“NYMEX”) and Commodity Exchange, Inc. (“COMEX”) (collectively the “Exchanges”) will list Event Contracts (“Event Contracts”) on certain CME Group futures contracts as listed in Table 1. for trading on the CME Globex electronic trading platform (“CME Globex”).

### 2023-03-12 — ECBTC (Event Contracts on Bitcoin Futures) added to the family, joining the 15:00:00 close group alongside ECES/ECNQ/ECRTY/ECYM. Identical grid: pre-open Sunday 16:00:00-17:00:00 and Monday-Thursday 16:45:00-17:00:00; executable Sunday 17:00:00 through Friday 15:00:00 with the same daily T=15:00:00 termination and 17:00:00 relist. Per LAW, the event-contracts family's history for ECBTC begins here, not at the 2022 launch.

- Citation: https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2023/02/SER-9092.pdf
- Verbatim: Effective Sunday, March 12, 2023, for trade date Monday, March 13, 2023, and pending all relevant CFTC regulatory review periods, Chicago Mercantile Exchange Inc. (“CME” or “Exchange”) will list Event Contracts on Bitcoin Futures (“Event Contracts”) for trading on the CME Globex electronic trading platform (“CME Globex”) as more specifically described below. ... CME Globex Trading Hours: CME Globex Pre-Open: Sunday 4:00 – 5:00 p.m. Monday – Thursday 4:45 – 5:00 p.m. / CME Globex: Sunday 5:00 p.m.- Friday 3:00 p.m. - Next day's Event Contract will list at 5:00 p.m.

### 2026-05-29 — ECBTC ONLY moves to near-24/7 weekend trading, starting 16:00 CT that Friday. ECBTC splits out of the 15:00:00-close group into its own profile: continuous trading with a Monday-Friday daily maintenance halt 15:00:00-16:02:00 (pre-open 16:01:00-16:01:30, no-cancel 16:01:30-16:02:00) and a Saturday extended maintenance halt 02:00:00-04:00:00 (pre-open 03:45:00-04:00:00, no-cancel 03:59:30-04:00:00); weekend close ELIMINATED; Sunday startup eliminated. The other ten roots are explicitly out of scope and keep their existing grids unchanged.

- Citation: https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Event-Based+Contracts+Expansion+to+24-7+Trading
- Verbatim: Starting at 4 p.m. Central Time on Friday, May 29, 2026, CME Group will expand event contracts to 24/7 trading, including event contracts on Bitcoin. ... With this launch, only the below event contracts on Bitcoin on channel 329 will migrate to weekend trading. Other event contracts will continue on the current schedule. ... Saturday | Extended Maintenance Window | Close: 2:00 a.m. to 3:45 a.m. CT | Pre-open: 3:45:00 a.m. to 4:00:00 a.m. CT No cancel: 3:59:30 a.m. to 4:00:00 a.m. CT Open: 4:00 a.m. CT ... Monday through Friday | Daily Maintenance Window (with Trade Date roll) | Close: 3:00:00 p.m. to 4:01:00 p.m. CT | Pre-open: 4:01:00 p.m. to 4:01:30 p.m. CT No cancel: 4:01:30 p.m. to 4:02:00 p.m. CT Open: 4:02:00 p.m. CT

### 2026-05-29 — SECOND CITATION for the same cutover, from the CME Globex Notice of 2026-05-25 (the last weekly notice before the change, carrying an 'Update' flag that narrowed the scope from the original 2026-03-30 announcement's 'expand event contracts' to 'expand the event contracts MDP channel (id=329)'). The item is absent from the 2026-06-01a notice, consistent with completion. Recorded as a separate row only to preserve the second independent primary citation for the same effective day; it is NOT a second grid change.

- Citation: https://www.cmegroup.com/notices/electronic-trading/2026/05/20260525.html
- Verbatim: Starting at 4 p.m. Central Time on this Friday , May 29 , CME Group will expand the event contracts MDP channel (id=329) to 24/7 trading. The technology and timeline align with the upcoming Cryptocurrency futures and options migration to 24/7 trading . The event contracts on Bitcoin futures will trade continuously on CME Globex with at least a two-hour weekly maintenance period over the weekend.

## Unsourced / open

- RTH vs ETH classification - NOT SOURCEABLE ANYWHERE for this family. SER-8968R, SER-9092, the CME activetrader specification page (all captures 2022-12-01 through 2025-09-16) and the 2026 client impact assessment each publish exactly one undifferentiated 'CME Globex Trading Hours' window plus a pre-open. Not one of them uses the words 'Regular Trading Hours', 'Extended Trading Hours', RTH or ETH in connection with event contracts. I searched every retrieved document. Putting the whole executable window in `regular` is therefore a modelling default, not a sourced fact - flag it as such in the crate.
- ECGC's close is missing from CME's own web specification page for that page's entire archived life. Across all ten captures (2022-12-01 .. 2025-09-16) the hours table has only five product rows and NEVER names ECGC. The first four captures instead carry a garbled row 'ECGE | Sunday 5:00 p.m. - Friday 3:00 p.m.' which, by 2024-03-30, CME silently replaced with 'EC6E | Sunday 5:00 p.m. - Friday 2:00 p.m.' - and gold was simply dropped. SER-8968R is authoritative and unambiguous ('ECGC: Sunday 5:00 p.m.- Friday 12:30 p.m.'), so I used it. DO NOT source ECGC from the web page.
- The 'ECGE 3:00 p.m.' -> 'EC6E 2:00 p.m.' change between the 2023-12-07 and 2024-03-30 captures of the specification page MUST NOT be recorded as a dated revision. It is a typo correction on a marketing page, not a rule change: SER-8968R, dated 2022-08-25 and effective at launch, already states 'EC6E: Sunday 5:00 p.m.- Friday 2:00 p.m.' and 'ECGC: Sunday 5:00 p.m.- Friday 12:30 p.m.'. There is no notice dating any EC6E or ECGC hours change, and per LAW-NO-FABRICATED-DATES a capture date may not date a cutover.
- SER-8968 (March 30, 2022) - the lead supplied in the task - is PRELIMINARY and states no effective day ('Preliminary Information Regarding the Upcoming Listing'). It is expressly superseded ('SER 8968R supersedes SER 8968 dated March 30, 2022'). It also omits the pre-open row entirely. It may corroborate the six close times but MUST NOT be used to date the launch. Working URL: https://www.cmegroup.com/notices/ser/2022/03/SER-8968.pdf
- No CME source published AFTER 2026-05-29 restates the grid for the ten non-Bitcoin roots. The specification page that carried it now 301-redirects: https://www.cmegroup.com/activetrader/event-contracts/contract-specifications-for-event-contracts.html resolves to https://www.cmegroup.com/markets/prediction-markets.html (verified live in a browser, and in the 2026-07-07 archive capture whose canonical tag is the prediction-markets URL). That landing page carries NO trading hours. CME's current event-contract-specifications PDF (https://www.cmegroup.com/markets/prediction-markets/files/event-contract-specifications.pdf, 2026-07-07 capture) still lists all eleven roots under 'Events on Futures' but contains NO trading-hours field at all. So the current non-BTC grid rests on SER-8968R (still the operative listing document) plus the client impact assessment's forward statement 'Other event contracts will continue on the current schedule.' It is not independently re-confirmed by a post-cutover CME hours publication.
- MDP channel assignment for the ten non-Bitcoin roots - NOT SOURCED. The client impact assessment places ECBTC on channel 329 / market segment 74 / SecurityGroup VB. The CME Globex Notice of 2026-06-01a shows a separate channel 333 named 'Event Contracts II'. No document I retrieved maps ECES, ECNQ, ECRTY, ECYM, EC6E, ECCL, ECNG, ECGC, ECSI or ECHG to any channel. This matters because the 2026-05-25 notice framed the change as channel-scoped ('expand the event contracts MDP channel (id=329)'); I resolved the scope from the impact assessment's explicit product table instead, which is the stronger statement, but I could not independently verify that the other roots are off channel 329.
- Whether ECBTC has a 15:00:00 halt on Saturday and Sunday - NOT STATED. The impact-assessment table scopes the daily maintenance window to 'Monday through Friday' and gives Saturday only the 02:00-04:00 extended window. Nothing addresses Sunday. I modelled no weekend 15:00 halt, following the table's literal scoping, but CME does not say so affirmatively.
- No post-hoc 'completed' notice for the 2026-05-29 ECBTC cutover was found. The item is present and dated in the 2026-03-30 and 2026-05-25 notices and simply absent from 2026-06-01a onward. Archive coverage of CME Globex notices ends at 2026-07-06; I read the live 2026-08-17 notice to confirm no later reversal, but the notices of 2026-06-29 through 2026-08-10 and 2026-08-24 onward were not read.
- SER-9587RR (Nov 26, 2025), effective Sunday December 7, 2025 for trade date Monday December 8, 2025, amends contract size and minimum price increment for this family ($100 -> $1.00 range; MPI 1.00 -> 0.01). I read it in full: it contains NO trading-hours change. Deliberately excluded from `revisions`. The governing rulebook text it reproduces delegates hours entirely - CME Rule 2302.A. Trading Schedule: 'Event Contracts shall be listed for Expiration on such dates and shall be scheduled for trading during such hours as may be determined by the Exchange.' So the rulebook can never supply a grid for this family; only SERs and CME product pages can. URL: https://www.cmegroup.com/notices/ser/2025/11/ser-9587rr.pdf
- An earlier contract-size change ($20 -> $100) is visible between the 2023-12-07 and 2024-03-30 captures of the specification page. I did not locate the SER that dates it. It is not hours-relevant, so I did not pursue it, but noting it so nobody later mistakes the capture gap for an hours event.
- Retrieval note for reproducibility: cmegroup.com returns HTTP 403 with a 602-byte JSON anti-bot body to plain curl. The PDFs ARE public and unauthenticated - they return HTTP 200 with a full desktop-Chrome User-Agent plus Accept / Accept-Language / Referer / Sec-Fetch-* / Upgrade-Insecure-Requests headers (SER-8968R downloaded at 151,726 bytes; SER-9092 at 110,316 bytes). The .html notices still 403 to curl but load normally in a real browser. Archive mirrors used where helpful: 2026-03-30 notice at https://web.archive.org/web/20260403130146id_/https://www.cmegroup.com/notices/electronic-trading/2026/03/20260330.html and 2026-05-25 notice at https://web.archive.org/web/20260529132331id_/https://www.cmegroup.com/notices/electronic-trading/2026/05/20260525.html . Both archive copies are gzip-encoded and must be decompressed. The Atlassian client-systems wiki needs no special headers and no auth.
