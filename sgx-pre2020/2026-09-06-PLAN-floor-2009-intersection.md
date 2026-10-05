# PLAN (follow-on PR after #68 merges): the SGX floor eras must intersect with SGX's own 2009 specification pages

Source of the change: issue #65's retrieval (raw/65-spec-leaves/, all states independently re-read in the
workflow's verify stage and spot-checked by the orchestrator from the saved bytes).

## The new sourced state (SGX psv contract-specification pages, captured Feb–Mar 2009; never again)
    Nikkei 225 (NK; NU/NS same T)   T  Pre-Opening 7.30–7.43 / Non-Cancel 7.43–7.45 / Opening 7.45 am – 2.25 pm /
                                       Pre-Closing 2.25–2.29 / Non-Cancel 2.29–2.30
                                    T+1 Pre-Opening 3.15–3.28 / Non-Cancel 3.28–3.30 / Opening 3.30 pm – 10.55 pm
    MSCI Singapore (SiMSCI) & STI   T  Pre-Opening 8.15–8.28 / Non-Cancel 8.28–8.30 / Opening 8.30 am – 5.10 pm /
                                       Pre-Closing 5.10–5.14 / Non-Cancel 5.14–5.15
                                    T+1 Pre-Opening 6.00–6.13 / Non-Cancel 6.13–6.15 / Opening 6.15 pm – 10.55 pm
    FTSE Xinhua China A50           T  Pre-Opening 9.00–9.13 / Non-Cancel 9.13–9.15 / Opening 9.15–11.35, 1.00–3.05
                                    T+1 Pre-Opening 3.35–3.38 / Non-Cancel 3.38–3.40 / Opening 3.40 pm – 10.55 pm
    (NK page also prints "Mutual Offset Trading with CME 7.00 pm - 5.15 am / 5.30 am - 6.30 am" — CME MOS, out of scope.)
    Also SGX-authored PDFs: WB-20090220073739 NK futures contract specifications; WB-20090306074153 SiMSCI specs.

## Why this changes the floor rows (law)
The floor..2013-08-20 interval now has SOURCED ENDPOINTS at two values for the T+1 leg (2009: close 22:55;
2013: close 02:00) and the changeovers are undated by SGX (third-party press: 22:55→01:00 effective
2010-01-11; 01:00→02:00 on 2010-08-30 — inadmissible for a row, recordable as risk). "Prefer the sourced
intersection to omission" applies: serve what holds under every sourced state. The 2009 pages are below the
January-2010 floor, but the changes they bound fall INSIDE the audit window, and the earliest sourced state
is the one the floor carries. The current floor rows (02:00 close carried back from 2013) over-report the
T+1 leg by up to three hours for Jan–Aug 2010 against SGX's own page — the residual risk (1) is now sourced,
not third-party.

## Proposed rows
JAPAN
  floor (baseline)  regular [(7,45,14,25),(15,30,22,55)]  extended [(14,25,14,30)]  order_entry [(7,30,7,45),(15,15,15,30)]
                    T+1 open 15:30 = narrowest across 2009 (15:30) / 2013 (15:15) — widens at the boundary.
                    15:15–15:30 is oe under 2009 and regular under 2013 → the common phase is order entry.
  2013-08-26 (Mon)  regular [(7,45,14,25),(15,15,2,0)]    extended [(14,25,14,30)]  order_entry [(7,30,7,45)]
                    The 2013-08-20 table's state; keyed to the following Monday because it LENGTHENS the wrapping
                    overnight close (22:55→02:00) — AGENTS.md's Monday rule. T+1 queue length unstated in 2013 →
                    withheld (the 2013 Notes assert a queue exists; length unknown) — or carry 15:00–15:15 by the
                    13+2 anchor argument? NO: anchor moved (15:30→15:15); withhold.
  2017-07-10 …      unchanged.
SINGAPORE
  floor (baseline)  regular [(8,30,17,10),(18,15,22,55)]  extended [(17,10,17,15)]  order_entry [(8,15,8,30),(18,0,18,15)]
                    T+1 open 18:15 identical in 2009 and 2013; the T+1 queue 18:00–18:15 is stated in 2009 and its
                    anchor did not move → carry (the same argument #65 makes for the T queue).
  2013-08-26 (Mon)  regular [(8,30,17,10),(18,15,2,0)]    extended [(17,10,17,15)]  order_entry [(8,15,8,30),(18,0,18,15)]
  2017-07-10 …      unchanged.
CHINA
  floor (baseline)  regular [(9,15,11,35),(13,0,15,5),(17,0,22,55)]  extended []  order_entry [(9,0,9,15)]
                    T = intersection of 2009 (9.15–11.35, 1.00–3.05) with W/2013 (09:00–15:25/15:55): the lunch
                    break is withheld. T+1 open held at 17:00 (narrowest across 2009 15:40 / W 16:10 / 2013 16:40 /
                    2017 17:00). 09:00–09:15 is oe under 2009 and regular under W/2013 → order entry.
                    The 15:25–15:30 closing routine is closed under 2009 (T ends 15:05) → withheld.
  2013-08-26 (Mon)  regular [(9,0,15,55),(17,0,2,0)]  extended [(15,55,16,0)]  order_entry [(8,45,9,0)]
                    (replaces the current 2013-08-20 row: the daytime widening AND the overnight lengthening now
                    share one boundary, keyed to the Monday. Costs four trading days of the 15:55 close.)
  2017-07-10 …      unchanged.
TAIWAN, NTR       unchanged (families did not exist).
W ordering caveats to record: W's STI open (07:55) and A50 grid (no lunch break) post-date March 2009 —
W is not uniformly the oldest state row by row; the W-before-S0 ordering rests on the A50 holiday tables.

## #64 comment updates (same PR)
history.rs ROUTINES: "carried forward (#64)" → "sourced through the interval: all 22 archived content-API
captures 2021-01-05..2024-10-07 reproduce the 2020-01-09 routines to the minute (raw/64-contentapi-2021-2024/)".
DT/AM 50 corroboration from SGX's own server-rendered product pages: nikkei225futuresoptions?cc=NK at
20241007180652 still 7.30–2.25 / 2.55; ?cc=NU at 20241114152443 prints the Revised column routine by routine;
China/Singapore/Taiwan/NTR pages unchanged across 2024-11-04. Add the URLs beside SGX_JAPAN_FROM_2024_11_04.

## Tests
Both sides of 2013-08-26 on three keys (Fri 2013-08-23: T+1 closes 22:55, i.e. 23:30 closed; Mon 2013-08-26
evening leg runs to Tue 02:00); floor T+1 close 22:55 (2012-06-20 23:30 closed); Japan floor T+1 open 15:30
(15:20 OrderEntry, 15:35 open); China floor lunch break withheld (12:00 closed) and oe 09:00–09:15; Singapore
floor oe 18:00–18:15. Rewrite the existing floor tests accordingly.

## Ledger / docs
Five rows' floor paragraphs; the residual-risk (1) sentence becomes sourced; CHANGELOG Fixed; sources.md gains
the psv channel (sgx.com/psv/…, captured 2006–2009-03-27) and the product-page channel. Closes #64, #65.

## Addendum (orchestrator check)
The two SGX-authored 2009 contract-specification PDFs in raw/65-spec-leaves/ (NK 2009-02-20, SiMSCI 2009-03-06)
state NO clock times — their "2.1 Trading Months and Hours" delegates to "such hours as may be determined by the
Exchange", exactly as the rulebook does. The hours source for the 2009 state is the psv HTML specification
pages (NK 20090308012135: "T+1 Session: Pre -Opening 3.15 pm - 3.28 pm / Non -Cancel Period 3.28 pm - 3.30pm /
Opening 3.30 pm - 10.55 pm"; SiMSCI 20090308120909; STI 20090220005028; A50 20090227040521; NU 20090227035122;
NS 20090307011353), each re-read from the saved bytes by the orchestrator 2026-09-06.
