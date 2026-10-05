<!--
Copyright (C) 2026 Kevin Monaghan. All rights reserved.

This file is proprietary and confidential.
Unauthorized copying, use, modification, distribution, or disclosure of this file,
via any medium, is strictly prohibited except under a written agreement with the
copyright owner.
-->

# GLBX market-hours profile audit

## Decision summary

- Databento exchange-code coverage is complete. Missing product-family evidence now selects the disclosed listing-exchange fallback; it is not an unknown-exchange condition.
- Source definition window: Databento GLBX.MDP3, latest seven distinct days ending 2026-04-29. The pre-remediation audit contained 1,797 excluded roots.
- Schedule window: CME `TradingSessionList.dat` published for the week of 2026-08-30. It contains 1,364 security-group rows; 1,316 contain status 17 (`Ready to Trade`).
- Join requested: Databento `(market_segment_id, group)` → CME `(tag 1300, tag 1151)`.
- Result from the April-key/August-schedule join: 1,371 non-test roots in 41 exact full transition signatures. Four signatures share an already-authored electronic envelope; 37 are new current transition shapes.
- The published seven-day V1 hours policy maps 30 directly proven roots to existing product-family keys and removes `ZR` from the incorrect grain key. After the independent admission policy excludes 426 roots (17 explicit test and 409 synthetic/no-ready), the regenerated census contains 1,342 listing-exchange fallback roots. The four separately excluded internal-monitoring roots were already outside that valid-root census.
- **Do not treat this as a time-aligned root schedule.** The two source weeks are four months apart. Of the 1,201 audit roots found as current outrights in the 2026-08-28 CME product sheet, 1,154 retained exactly the same route, 46 changed route, and 1 overlaps old/new routes. The joined row is exact for what that security-group key means in August, but not necessarily for what the April root means in August.
- The schedule feed publishes Pre-Open, Ready, Halt, Not Available, Close and Post Close. It does **not** publish the Regular-versus-Extended classification used by `MarketHoursKey`, so an equal electronic envelope alone cannot prove two semantic profiles interchangeable.

## Corrected mapping defect

- `ZR` (Rough Rice, CME route `70/ZR`) was mapped to `GlobexGrains`, but the 2026-08-30 schedule is Ready `19:00–21:00 CT`, Halt, then Ready `08:30–13:20 CT`. The existing grain profile is Ready `19:00–07:45 CT`, then `08:30–13:20 CT`. `ZR` now carries no authored selector and uses the disclosed CBOT fallback until exchange-hours supplies a sourced `GlobexRoughRice` profile/history.

## Applied existing-key additions

- `GlobexLivestock`: `PRK`.
- `GlobexCryptocurrency`: `ADA,BFF,BTE,EBM,EBR,EEM,ETE,LNK,MCA,MLN,MSL,MXL,MXP,SOL,XLM,XRP`. Current August truth also places `1OZ` on `74/G1` with the same 24/7 transitions; its April route was `78/GC`, so handle it as a dated route/product change rather than trusting the cross-time join.
- `GlobexInterestRates`: `Z3N,MTN,TWE,MWN,2YY,5YY,10Y,30Y` (Treasuries/yield micros already inside the key’s declared family).
- `GlobexGrains`: `MZC,MZW,MZS,MZM,MZL` are the strongest additions. Do not fold `XC,XK,XW,MKC` into the existing key: mini grains had a distinct 2012–2022 history even though today’s envelope converges.
- Not applied by this audit: ordinary FX roots use the current `17:00–16:00 CT` standard FX envelope, but still need a complete root-level family review. `6EB` and `6EP` are BTIC and excluded from that statement; `TRL` has a current product-sheet/session-list route disagreement and must wait.

## Exact 41 current schedule signatures

The roots column is complete. “Existing” means the August electronic transition envelope is present on an authored root; it does not by itself establish compatible RTH classification or history. The exact raw FIX transitions and SHA-256 signature are retained in [`market-hours-electronic-envelope-candidates.tsv`](market-hours-electronic-envelope-candidates.tsv).

| # | Proposed profile/family | Roots | Security groups | Existing envelope | Exact roots |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | shared 17:00–16:00 envelope (semantic split required) | 1146 | 184 | globex_energy,globex_equity_index,globex_fx,globex_interest_rates,globex_nikkei_225_dollar | `0A, 0B, 0C, 0E, 10Y, 1D0, 1D1, 1D2, 1D4, 1E, 1G6, 1H, 1H0, 1H1, 1H2, 1H3, 1H4, 1H5, 1H6, 1H7, 1HQ, 1HR, 1HS, 1HW, 1LP, 1NA, 1NM, 1OZ, 1S, 1T, 1Y, 1ZA, 20U, 22, 23, 25U, 26, 27, 2D, 2FW, 2JW, 2K0, 2K1, 2K2, 2K3, 2K4, 2K5, 2K6, 2K7, 2KP, 2KQ, 2KR, 2KS, 2KW, 2YY, 2ZW, 30U, 30Y, 33K, 35U, 3G0, 3G1, 3G2, 3G4, 3G6, 3K0, 3K1, 3K2, 3K3, 3K4, 3K5, 3K6, 3K7, 3KP, 3KQ, 3KS, 3KW, 3L, 3NA, 3NB, 3P, 3V, 3XW, 3ZW, 40U, 45U, 4C, 4D0, 4D1, 4D2, 4D4, 4G6, 4GC, 4H0, 4H1, 4H2, 4H3, 4H4, 4H5, 4H6, 4H7, 4HQ, 4HR, 4HS, 4HW, 4LP, 4V, 4XW, 50U, 51, 55U, 5L, 5Y, 5YY, 60U, 63, 65U, 6EP, 6H, 6L, 6Z, 70U, 7D, 7F, 7IF, 7IS, 7N, 7V, 7X, 88, 8D, 8W, 9Q, A0D, A0F, A1D, A1G, A1L, A1M, A1P, A1R, A1U, A1V, A1W, A1X, A32, A33, A38, A3C, A3G, A3M, A3N, A3Q, A3R, A42, A43, A4L, A4M, A4Q, A4R, A55, A58, A59, A5C, A6L, A6V, A6W, A6X, A7E, A7G, A7I, A7L, A7Q, A7Y, A81, A8B, A8C, A8G, A8I, A8J, A8K, A8L, A8M, A8O, A91, A9N, AA3, AA4, AA5, AA6, AA7, AA8, AA9, AB6, AB7, ABH, ABI, ABS, ABT, ABX, ABY, AC0, ACB, ACD, ACS, ACU, AD0, ADB, AE5, AEB, AEP, AET, AEZ, AFE, AFF, AFH, AFI, AFK, AFY, AGA, AGE, AGT, AGX, AH3, AHJ, AHL, AHM, AI1, AI2, AI3, AI4, AI5, AI6, AI7, AI9, AJ, AJ1, AJ9, AJB, AJJ, AJL, AJR, AJS, AJY, AK1, AKL, AKR, AKS, AKX, AKZ, AL9, ALA, ALB, ALI, ALM, ALY, AM1, AML, AN1, ANE, ANL, ANT, AO1, AOB, AOH, AOJ, AP1, AP2, AP3, AP4, AP5, AP7, AP8, AP9, APA, APS, AQ5, AQA, AQK, AR0, AR1, AR4, AR6, ARE, ARY, ASD, ASP, AT0, ATP, ATU, ATY, AU2, AU3, AU4, AU5, AU6, AUB, AUF, AUH, AUI, AUJ, AUP, AUS, AUW, AV0, AVK, AVL, AVU, AVZ, AW2, AWJ, AWQ, AXB, AY, AYV, AYX, AZ0, AZ1, AZ5, AZ7, B0, B1, B1S, B2K, B7H, B8, BB, BCH, BCR, BDB, BDT, BEB, BEF, BFR, BG1, BG2, BG3, BHO, BIO, BK, BKB, BKT, BOO, BPA, BPU, BR7, BUC, BWH, C2E, C4Z, CBB, CC5, CCM, CFB, CFC, CGB, CHP, CJ, CJY, CLD, CMB, CMF, CMS, CNH, COB, COH, COL, CPB, CPD, CPO, CPP, CPV, CRB, CS1, CS2, CS3, CS4, CS5, CS6, CSX, CU, CUP, CY, CZK, D0, D0X, D0Z, D1, D1N, D1X, D1Z, D2, D2L, D2X, D2Z, D3L, D4, D4L, D4X, D4Z, DAB, DAX, DAZ, DBB, DBL, DBT, DBZ, DCB, DCL, DCW, DEB, DEP, DFN, DHA, DHB, DHY, DLB, DRS, DTF, DTH, DVE, E1S, E3G, E6, E6M, E7, E9X, EAA, EAB, EAC, EAD, EAE, EAW, EBE, ECD, ECF, ECK, EDP, EFF, EFM, EGB, EGN, EHB, EHF, EHL, EHR, EI, EJL, EL, EL1, EMC, EN, ENK, ENP, ENS, ENY, ENZ, EO1, EOB, EP1, EPN, EPZ, EQ1, ERL, ES1, ES2, ESB, ESG, ESK, ESR, ESS, EUB, EUS, EVC, EWB, EWF, EWG, EWN, EXR, F1S, F3, FAL, FBD, FBT, FCB, FCN, FEF, FEW, FL, FLB, FLJ, FLP, FO, FOA, FOM, FOR, FRC, FRS, FSF, FSS, FT5, FTL, FVB, G0, G02, G0K, G0N, G1, G12, G1K, G1N, G2, G22, G2K, G2N, G4, G42, G4K, G4N, G6, G62, G6K, G6N, G6X, G6Z, GBB, GBR, GCB, GCC, GCG, GCI, GCM, GCU, GD, GDL, GEO, GES, GFC, GIE, GKS, GMB, GMS, GNB, GNL, GNO, GNS, GOC, GSW, GUD, GWT, GY, GZ, H0, H0X, H0Z, H1, H1X, H1Z, H2, H2L, H2O, H2X, H2Z, H3, H3X, H3Z, H4, H4X, H4Z, H5, H5B, H5F, H5G, H5L, H5X, H5Z, H6, H6X, H6Z, H7, H7X, H7Z, HBX, HCS, HDG, HGB, HGS, HH, HHW, HIA, HIL, HJC, HLT, HOA, HOB, HP, HPD, HPE, HQ, HQX, HQZ, HR, HRC, HRP, HRX, HRZ, HS, HSX, HSZ, HTA, HTB, HTT, HUF, HVG, HVO, HW, HWA, HWX, HWZ, HYB, IBS, IBV, IDL, IDR, ILS, IPC, IPF, IPO, IPS, IQB, IQL, IQS, IQY, ITB, ITP, J7, JA, JBK, JBT, JCB, JCC, JCY, JE, JET, JFB, JFC, JKB, JKD, JKF, JKM, JKY, JLC, JNC, JNL, JPK, JPT, JSB, JTB, K0, K0K, K0N, K1, K1K, K1N, K2, K2K, K2L, K2N, K3, K3K, K3L, K3N, K4, K4K, K4L, K4N, K5, K5K, K5N, K6, K6K, K6N, K7, K7K, K7N, KP, KPK, KPN, KQ, KQK, KQN, KR, KRK, KRN, KRW, KS, KSK, KSN, KT, KW, KWK, KWN, LAF, LAP, LBU, LCS, LED, LEL, LHV, LL, LNG, LP, LPE, LPX, LPZ, LSW, LT, LTC, LTH, M1B, M35, MAA, MAB, MAC, MAE, MAF, MAS, MBA, MBB, MBC, MBE, MBL, MBM, MBO, MBR, MBS, MCB, MCD, MCE, MCF, MCN, MCS, MDB, ME, MEB, MEE, MEF, MEO, MEW, MFB, MFC, MFD, MFP, MFR, MGB, MGE, MGF, MGH, MGN, MGS, MH, MHE, MHO, MIP, MIR, MJB, MJC, MJN, MJP, MJY, MM, MMC, MMF, MMO, MMP, MMR, MNB, MNC, MNI, MNK, MNS, MNT, MO, MOI, MOX, MPE, MPS, MPX, MQ, MQA, MRB, MRI, MRT, MSB, MSC, MSD, MSF, MSG, MT2, MTB, MTH, MTI, MTN, MTS, MUD, MWN, MXB, MXR, N1B, N1S, N3P, NA2, NA3, NBB, NBD, NBO, NBP, NCD, NCO, NCP, NDA, NEO, NEP, NFC, NFD, NFG, NFO, NGO, NHH, NHO, NHP, NIE, NIY, NJY, NLS, NMO, NMP, NN, NNE, NNP, NOD, NOK, NOO, NOT, NPG, NRO, NRP, NRR, NSK, NSO, NSP, NTP, NWD, NWM, NWO, NWP, NYF, NYP, NZC, OAD, OFF, OMM, OMN, OOD, OPF, OPO, PAC, PAD, PAM, PAU, PBT, PCD, PDL, PEX, PFP, PGG, PHF, PJY, PLM, PLN, PMF, PNF, PNK, POB, POG, PPP, PPW, PR4, PR6, PSF, PSK, PTL, QBTC, QC, QCN, QCS, QDOW, QETH, QH, QI, QNDX, QO, QRTY, QSOL, QSPX, QU, QXRP, R2G, R2V, R4B, R53, R5B, R5E, R5F, R5M, R5O, R6B, RBB, RBF, RBM, RDA, RF, RGF, RGI, RKA, RLX, RMB, RME, RN3, RN4, RN6, RP, RS1, RSG, RSV, RT, RVR, RX, RY, S1S, S53, S5B, S5F, S5M, S5O, SBM, SCB, SCT, SD, SDA, SDI, SE, SEK, SF1, SF3, SFB, SG, SGB, SGC, SGD, SGF, SGO, SGU, SHR, SIC, SIR, SJY, SMC, SMU, SOX, SPM, SR5, SRB, SSW, STI, STR, STS, STY, SU, SXB, SXI, SXO, SXR, SXT, T1B, T1S, T2B, T2D, T2M, T3B, T3L, T4B, T4D, T5B, T5C, T6B, T7C, T7K, T8B, T8C, TB2, TBF3, TBK, TC1, TC6, TC7, TCS, TD3, TD8, TDM, TEF, TF2, TFB, TFU, TH, THAI, THB, THD, TI3, TIE, TIL, TIO, TK, TKB, TL, TLB, TLD, TM, TMB, TMD, TPD, TPY, TRL, TT, TTB, TTD, TTE, TTF, TTG, TTH, TTI, TTP, TW, TWE, U7, U9, UA, UCD, UCG, UCM, UCO, UCR, UCS, UFB, UFE, UFV, UHC, UHT, UKG, ULB, UME, UN, UNO, UP5, UPB, UPM, UR, USC, USE, UV, UX, V7, VR, VV, W0, WBR, WBX, WCW, WDB, WHB, WHD, WHT, WMB, WMD, WMR, WNB, WNT, WS, WTB, WTD, WTI, WTL, WTT, X0, X6, X7, X9, XAB, XAE, XAF, XAI, XAK, XAP, XAR, XAU, XAV, XAY, XAZ, XER, XEU, XPP, XTB, XTT, XUB, XUK, YHE, YHF, YIA, YIB, YIC, YID, YIE, YII, YIL, YIO, YIT, YIW, YIY, YNO, YO, YRP, YRW, YUE, YVB, YWE, YWF, YWK, Z1B, Z3N, Z4, Z6, ZAL, ZGL, ZJL, ZKU, ZNC` |
| 2 | equity/credit BTIC 17:00–15:00 | 51 | 42 | new | `2GT, 2VT, A2T, ADT, AQT, ART, ASPT, AST, BIT, BOT, DLBT, EGT, EIT, EMT, EST, EWFT, HYBT, IPCT, IPT, IQBT, IQLT, IQST, IQYT, IST, NQT, R1T, RET, REX, RGT, RKT, RLT, RVT, SGT, SMET, SMT, SOT, SUT, SWT, TRB, XBT, XET, XFT, XIT, XKT, XPT, XRT, XUT, XVT, XYT, XZT, YMT` |
| 3 | commodity-index day 08:15–13:30 | 18 | 18 | new | `AW, AWT, BAG, BAT, BEN, BET, BGR, BGT, BLI, BLT, BME, BMT, BPE, BPR, BPT, BST, CCI, CCT` |
| 4 | crypto 24/7 (existing GlobexCryptocurrency) | 16 | 9 | globex_cryptocurrency | `ADA, BFF, BTE, EBM, EBR, EEM, ETE, LNK, MCA, MLN, MSL, MXL, MXP, SOL, XLM, XRP` |
| 5 | grain grid (existing envelope; mini history differs) | 15 | 12 | globex_grains | `CWD, CWR, HRS, KWD, MKC, MZC, MZL, MZM, MZS, MZW, OSF, RSO, XC, XK, XW` |
| 6 | crypto BTIC New York | 15 | 8 | new | `BFB, BNB, CNB, CYB, ENB, EYB, LNB, LYB, MYB, ONB, RNB, SNB, XNB, XYB, YLB` |
| 7 | housing 08:15–15:00 | 11 | 1 | new | `BOS, CHI, CUS, DEN, LAV, LAX, MIA, NYM, SDG, SFR, WDC` |
| 8 | crypto BTIC London | 9 | 4 | new | `BLB, BTB, EMB, ETB, MIB, OLB, RLB, SLB, XLB` |
| 9 | crypto TAS | 8 | 4 | new | `TBM, TBT, TEM, TET, TMS, TMX, TSL, TXP` |
| 10 | crude/refined TAS 13:30 | 6 | 1 | new | `BBT, BZT, CLT, HOT, MCT, RBT` |
| 11 | grain TAS 13:15 | 6 | 3 | new | `KET, SBT, ZCT, ZLT, ZMT, ZWT` |
| 12 | dairy (Fri 13:55 close) | 6 | 3 | new | `CB, CSC, DC, DY, GDK, GNF` |
| 13 | Treasury TAS 14:00 | 6 | 6 | new | `TNT, UBT, ZBT, ZFT, ZNS, ZTT` |
| 14 | crypto BTIC APAC | 5 | 2 | new | `ABB, AHB, AMB, ATB, BAB` |
| 15 | gold TAS 12:30 | 4 | 1 | new | `1OT, GCT, MGT, QOT` |
| 16 | energy TAM London 10:30 | 4 | 1 | new | `BZL, CLL, HOL, RBL` |
| 17 | equity TMAC 15:00 | 4 | 4 | new | `ESX, NQX, RTX, YMX` |
| 18 | copper TAS 12:00 | 3 | 1 | new | `HG0, HGT, MHT` |
| 19 | equity TACO 08:30 | 3 | 3 | new | `ESQ, NQQ, RTQ` |
| 20 | commodity-index BTIC 13:30 | 3 | 3 | new | `DRT, GDT, GIT` |
| 21 | livestock TAS 13:00 | 3 | 1 | new | `GFT, HET, LET` |
| 22 | natural-gas TAS 13:30 | 3 | 1 | new | `HHT, NGT, NNT` |
| 23 | Nikkei BTIC 01:30 | 2 | 2 | new | `NIT, NKT` |
| 24 | Europe-equity BTIC 10:30 | 2 | 2 | new | `DVT, E3T` |
| 25 | silver TAS 12:25 | 2 | 1 | new | `MST, SIT` |
| 26 | lumber 09:00–15:05 | 2 | 1 | new | `LBR, SYP` |
| 27 | TOPIX BTIC 01:30 | 2 | 1 | new | `TPB, TPT` |
| 28 | Dutch-gas TAS 10:05 | 2 | 1 | new | `TAS, TTS` |
| 29 | energy TAM Singapore 03:30 | 2 | 1 | new | `BZS, CLS` |
| 30 | energy TAM Shanghai 02:00 | 1 | 1 | new | `CLC` |
| 31 | FTSE-China BTIC 03:00 | 1 | 1 | new | `FTC` |
| 32 | Santos soy 08:30–13:20 | 1 | 1 | new | `SAS` |
| 33 | platinum TAS 12:05 | 1 | 1 | new | `PLT` |
| 34 | EUR BTIC 09:40 | 1 | 1 | new | `6EB` |
| 35 | pork cutout (existing GlobexLivestock) | 1 | 1 | globex_livestock | `PRK` |
| 36 | gold TAM 09:02 | 1 | 1 | new | `GCD` |
| 37 | European gasoil TAS 10:30 | 1 | 1 | new | `7FT` |
| 38 | palladium TAS 12:00 | 1 | 1 | new | `PAT` |
| 39 | urea 08:30–14:30 | 1 | 1 | new | `MFV` |
| 40 | Black Sea wheat 19:00–13:20 | 1 | 1 | new | `CVB` |
| 41 | copper TAM 12:00 | 1 | 1 | new | `HGF` |

## Full-day envelope requires semantic splitting

The 1,146-root `17:00–16:00 CT` signature is not one safe product family. At minimum split and source:

- `GlobexWeather` (179 roots): same current envelope but a distinct 2025 close-time history.
- `GlobexSpotQuoted` (eight tradable roots: `QSPX,QNDX,QDOW,QRTY,QBTC,QETH,QSOL,QXRP`): five-day 17:00–16:00, deliberately not the cryptocurrency 24/7 key.
- Standard FX (ordinary pairs) can reuse `GlobexFx`; BTIC roots cannot.
- U.S. Treasury/yield micros can reuse `GlobexInterestRates`; Eris/OIS swaps, deliverable swaps, UMBS/mortgage, credit and non-U.S. rates need separate history/RTH proof before mapping.
- Ordinary NYMEX/COMEX energy/metals match `GlobexEnergy` today, and the pinned dependency records a venue-wide 2015 COMEX/NYMEX close change. Keep TAS/TAM/BTIC and explicitly different specifications separate; review power, softs and alternative commodity families before bulk mapping.
- International/sector equity indexes share the electronic envelope but the schedule feed cannot prove their RTH classification or historical grid. Do not bulk-map them to `GlobexEquityIndex` from this join alone.
- `H2O`, BMD partner `CPV`, and miscellaneous CBOT agricultural full-day products need their own family evidence even though their current electronic envelope matches.

## Route drift / no direct current join

- Material route drift: `1OZ 78/GC → 74/G1` (standard metals → 24/7); `E3G 68/EU → 68/EQ`; `E3T 68/EQ → 68/EU`; `HGF 78/TR → 78/HT`; `HHT/NGT/NNT 78/NA → blank` in the current product sheet. There are 46 changed roots total and one overlapping route (`POB`).
- Thirteen current product rows do not directly match an August schedule key: `ART,HHT,JCB,JCC,JLC,NGT,NNT,TRL,TTP,UCD,UCG,UCR,UCS`. Do not infer their current hours from the April key without resolving this source inconsistency.
- Event-contract roots (`ECES,ECNQ,ECRTY,ECYM,ECBTC,EC6E,ECCL,ECNG,ECGC,ECSI,ECHG`) are not recoverable as current tradable schedules from this join: their April key now describes a no-Ready synthetic group. Their pre-2026 underlying-specific closes and the 2026-05-29 24/7 transition require primary-notice-backed profiles.

## Existing GLBX keys in pinned exchange-hours

`GlobexEquityIndex`, `GlobexEnergy`, `GlobexGrains`, `GlobexFx`, `GlobexInterestRates`, `GlobexLivestock`, `GlobexCryptocurrency`, `GlobexNikkei225Dollar` at revision `74e23ec65790b5aed0a471b00887f6e79bfde686`.

## Sources and integrity

- CME Globex Market Schedule File Overview (updated 2024-12-26): <https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457704103/CME+Globex+Market+Schedule+File+Overview> — defines the Sunday-published weekly file, join fields and status values.
- CME production directory: <https://www.cmegroup.com/ftp/SBEFix/Production/>
- CME Globex Product Reference Sheet, internal sheet date 2026-08-28: <https://www.cmegroup.com/globex/files/globex-product-reference-sheet.xls>
- Mini-grain history: <https://www.cmegroup.com/tools-information/lookups/advisories/market-data/20120910.html> ; <https://www.cmegroup.com/tools-information/lookups/advisories/market-data/20130311.html> ; <https://www.cmegroup.com/notices/electronic-trading/2022/09/20220905.html>
- Weather change effective 2025-04-14: <https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2025/03/ser-9519.pdf>
- Event-contract original grids: <https://www.cmegroup.com/notices/ser/2022/03/SER-8968.pdf> ; 24/7 transition effective 2026-05-29: <https://www.cmegroup.com/notices/electronic-trading/2026/03/20260330.html>
- Local SHA-256: `TradingSessionList` `b80f0df46207ac4c67a0e42bcc5c5c8b585776414798a4f194cd5b71fce49070`; product sheet `4bfb8f7e150d91a36129065a59b47a8cc8c47755e139c0709c7a9522e3e5bd57`.
- Selected Databento Definition SHA-256 values: `20260422` `52cc005d70df174c48bcb632883a7d6021ae21562667e3e4485281e645aa6c0e`; `20260423` `30f60486fe4ca7ea3e19b22506b527f6388fdd1201e0a4fed90e8a9bcfa3155a`; `20260424` `83e14d4ba9b95788ef12535890652464c130ab6b119762b9e5b72fffb910810f`; `20260426` `46353bde3e04d5b093da297180207946f30000df0bb77156825aa69d18eb3743`; `20260427` `209266b51a95b2bb7383071e0261098a5906078d0c84f0aa9f65ec3bf4108b11`; `20260428` `70bdcec57026cb14623dc7b3d129b535f2e68a5eff277a5ba40eee24d2bcff28`; `20260429` `ce7c2e991cb722ef8a3e91831761b8f3d58312d5dbf28d5cac480252b20a33c6`.

## Non-tradable/test rows

No `MarketHoursKey` should be invented for no-Ready synthetic/reference groups or CME test products. The exact pre-remediation 1,797-root disposition and evidence are in [`market-hours-root-classification.tsv`](market-hours-root-classification.tsv), with grouped test/synthetic evidence in [`market-hours-nontradable-groups.tsv`](market-hours-nontradable-groups.tsv). The identified synthetic/no-Ready and explicit-test roots are now rejected by the independent source-cited `glbx-definition-exclusions.toml`, rather than by absence from the hours map. Because of the four-month mismatch, an August synthetic description proves the August key state, not automatically the April root’s identity; sentinel and literal test evidence remain safe exclusions.
