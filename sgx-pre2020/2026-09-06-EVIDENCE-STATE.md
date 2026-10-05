# SGX equity-index evidence state, end of 2026-09-06 — what is DATED, what is BRACKETED, what is LIVE

## DATED under LAW-PRIMARY-SOURCES (new today)

**Japan T-session extension: Monday 2024-11-04.** SGX Circular No. DT/AM – 50 of 2024, 9 September
2024, "Extension of T-session for SGX Japan Derivatives and Intraday Margin Cycle 2 Timing Change",
signed Leno Lee, SVP Trading and Clearing Services, on Singapore Exchange Derivatives Trading Limited
letterhead (Co. Reg. 197802854W). Read from a verbatim member mirror — Fubon Futures (Taiwan) —
via Wayback capture 20241114183232 (the live Fubon URL now 404s). Independently re-retrieved and
text-verified by the orchestrator: raw/circulars/DTAM-50-of-2024_fubon_wayback20241114183232.pdf.
Same source class as DT/AM 15 of 2025 (CITIC mirror), which sources.md's channel-limit note already
prescribes.

Current -> Revised (Singapore time), NK/NR/ND/NU/NS/NC/EJRT/EJP:
    T   Pre-Opening 7.15–7.28  Non-Cancel 7.28–7.30  Opening 7.30 am – 2.25 pm -> 2.55 pm
        Pre-Closing 2.25–2.29 -> 2.55–2.59   Non-Cancel 2.29–2.30 -> 2.59–3.00
    T+1 Pre-Opening 2.45–2.53 -> 3.15–3.23   Non-Cancel 2.53–2.55 -> 3.23–3.25
        Opening 2.55 pm – 5.15 am -> 3.25 pm – 5.15 am
NKO: T Opening 7.30–2.30 -> 7.30–3.00; T+1 2.55 -> 3.25.
Footnote: "4 November 2024 is a Japan public holiday and its underlying cash market is closed."
Also: intraday margin cycle 2 moved 4.00pm -> 5.00pm w.e.f. Monday 21 October 2024 (not a session).

CONSEQUENCE: history.rs's "FIRST TRANSITION IS STILL UNDATED" paragraph and the Japan key's
2020..2025-04-06 sourced-intersection era are superseded. The era splits cleanly:
    2020-01-01 .. 2024-11-03   T 07:30–14:25, T+1 14:55–05:15   (calendars 2020–2024)
    2024-11-04 .. 2025-04-06   T 07:30–14:55, T+1 15:25–05:15   (DT/AM 50 Revised column, with routines)
    2025-04-07 ..              current                           (DT/AM 15)
This circular also confirms in SGX's own words that the T+1 close was already 05:15 in Sept 2024,
so rows (A) 2019 T+1 extension and (B) 2024 Japan T extension are independent.

## BRACKETED (SGX-authored artifacts only) — the 2019 T+1 close 04:45 -> 05:15

    last SGX artifact at 04:45   content-api derivatives_products_list, Wayback 20190621080419
    SGX voice, month only        Annual Report 2020 p.13: "Our extension of trading hours in
                                 November 2019 ... At 22.5 hours" (22.5 h is a DURATION, not endpoints)
    first SGX artifacts at 05:15 Mini-JGB factsheet, api2 2019-11 directory, filename "11 Nov 2019"
                                 (body says "Margins (As on 18-Oct-2019)" — filename is the bound);
                                 Titan DTDC Factsheet Dec 2019, api2 2019-12 directory
    first dated-document at 05:15  2020 Trading Calendar edition
Third parties (Henghua/Phillip/Rakuten) all say Monday 2019-11-11. Not law-admissible for a row.
Every channel that could carry an SGX-authored DAY is now closed (see t1-extension-triangulated.md).
=> Row (A) stays a sourced-intersection, changeover undated. The bracket is recorded beside it.

## LIVE, NOT LOST — the pre-2020 calendars

The repo believed "no edition earlier than 2020 survives". The ARCHIVE negative is true (CDX on
api2.sgx.com/sites/default/files/2019* is empty), but the documents are STILL SERVED LIVE:
    2018 (Apr) Trading Calendar   api2, PDF CreationDate 2018-04-11, served since 2018-05-21;
                                  text carries boilerplate "accurate as of 26 December 2017"
    2019 Trading Calendar         api2, "accurate as of 15 January 2019", HTTP last-modified 2019-01-23
Both retrieved 2026-09-06 (raw/intermediate-2019-state/). Both state the 04:45 grid.
FINDINGS.md's "RECONCILE BEFORE USE" flag on the 2019-01 calendar is resolved in favour of the calendar.

## THE PRE-2020 SOURCED STATES (equity index), and the ordering problem

    G2  "legacy"   Nikkei T 07:45–14:25 / T+1 15:15–02:00; A50 09:00–15:25 / 16:10–02:00;
                   SiMSCI 08:30–17:10 / 18:15–02:00; MSCI Taiwan 08:45–13:45 / 14:35–02:00
                   ONE witness: the wcm/connect fragment captured 2018-07-11. Content undated and
                   evidently stale (still names "S&P CNX Nifty", "FTSE Xinhua", "MSCI Asia Apex 50").
    A   "04:45"    Nikkei 07:30–14:25 / 14:55–04:45; A50 09:00–16:30 / 17:00–04:45;
                   SiMSCI 08:30–17:10 / 17:40–04:45; MSCI Taiwan 08:45–13:45 / 14:15–04:45;
                   NTR (USD) 07:25–18:30 / 19:00–04:45 (from the 2018 Apr calendar on; absent from
                   the 2017 portal grid)
                   Witnesses: portal 2017-07-05 & 2017-09-27 (no NTR), 2018 Apr calendar, 2019
                   calendar, content-api 2019-01-16 & 2019-02-04.
    B   "04:45 +SiMSCI 17:20/17:50"  identical to A except SiMSCI T close 17:10->17:20, T+1 open
                   17:40->17:50. Witness: content-api 2019-06-11 (revisit 06-21).
    C   "05:15"    = B with T+1 close 05:15. Witness: content-api 2020-01-09; 2020 calendar.

The 02:00 state (G2) was CAPTURED a year AFTER the 04:45 state (A) was captured; SGX ran two
content trees and the wcm fragment was unrefreshed. A capture date dates the observation, never the
state. So G2 cannot be placed after A, and cannot be dated at all from SGX artifacts. Third-party
press (mondovisione 2010-01-08, thetradenews 2010-08-17) attests 01:00 -> 02:00 on 30 Aug 2010;
inadmissible for a row, recordable as residual risk.

Contract-set facts that bind knowledge boundaries (per family):
    Japan      Nikkei 225 futures present in every state             -> extendable
    China      "FTSE Xinhua China A50" (G2) / "FTSE China A50" (A+)  -> same contract, renamed index
    Singapore  "MSCI S'pore"/"MSCI Singapore Free" throughout        -> extendable (modelled family
                                                                        is SiMSCI + STI)
    Taiwan     only MSCI Taiwan before 2020; FTSE Taiwan is the modelled family -> NOT extendable,
               stays sessionless before the 2021 edition (existing boundary stands)
    NTR (USD)  first listed in the 2018 (Apr) calendar (two contracts) -> boundary there, not 2020

OPEN QUESTION for the synthesis pass (do not decide by hand): the era table per family under the
carry-back + sourced-intersection laws, given that G2 is undated and possibly older than the floor
region, and that A->B (SiMSCI) and B->C (T+1 close) are undated. Candidate shape for Japan:
    floor .. <A first sourced>   G2 ∩ A  = T 07:45–14:25, T+1 15:15–02:00
    <A first sourced> .. 2020    A ∩ B ∩ C = T 07:30–14:25, T+1 14:55–04:45
with "<A first sourced>" being a knowledge boundary (not a claimed change) at the earliest SGX
artifact stating A — and whether that may be a capture date (2017-07-05) or must be a document
date (2018-04-11) is exactly what the synthesis must argue from AGENTS.md.
