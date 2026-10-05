# The SGX Derivatives Products Description change log DOES date the 2019 T+1 extension — verified from the OOXML

Orchestrator verification 2026-09-06, on the workbook downloaded live from
https://api2.sgx.com/sites/default/files/2026-08/Derivatives+Products+Description+v17.6 eff 20260824, 20260907.zip
inner file sha256 bbc3b60e22a3b62fe0d9ee56b3249d5171332992bc73474a80476d116c8b69ce (matches the chase agent's
copy and the earlier sweep's). Saved: raw/catalogue/v17.6/.

## What the file encodes (parsed with zipfile + ElementTree, not a renderer)

Sheet "read_me" (xl/worksheets/sheet1.xml). Header row 24:
    B24 "Issue Date (mm/dd/yyyy)"   C24 "Version Number"   D24 "Authors"   E24 "Change Description"
167 dated rows (Excel date serials), 2016-02-19 onward. mergeCells: 0.
Multi-row entries are runs of rows sharing explicit cell border styles: borderId 2 (top thin, no bottom),
68 (no top, no bottom), 67 (no top, bottom thin) — the bottom row carries the Issue Date / Version /
Authors. Single-row entries use borderId 1. That partition is data in the file.

    r83  E "Effective 21 Oct:"                                                     borderId 2
    r84  E "Amend, insert '4 Routes' in PV, PVF, CPV, PPV, CPVF, PPVF contract name" 68
    r85  B 43739 = 2019-10-01  C 6.8  D SGX  E "Add PW, PWF, CPW, PPW, CPWF, PPWF"    67
    r86  E "Editorial housekeeping/standardisation contract name on Freight contracts" 2
    r87  E "Effective 11 Nov:"                                                     68
    r88  E "Editorial change Contracts_mainmenu:"                                  68
    r89  E "(T+1) session Closing hours to 5:15am all T+1 traded contracts"        68
    r90  B 43745 = 2019-10-07  C 6.9  D SGX  E "Editorial change session_mainmenu: SURV_INT to 5:15,
         REMOVE_DAY_ORDERS to 5:20, SERIES_GEN to 5:22, CLS_CLEAR to 5:25 and CLOSE to 5:30 all T+1
         traded contracts"                                                          67
    r91  B 43777 = 2019-11-08  C 7.0  D SGX  E "Add MF5, MF5F, LSF, LSFF effective 18 Nov / Add VN & NVN
         effective 02 Dec"                                                          1

Six "Effective <day> <Mon>:" headers exist in the log (rows 60, 61, 62, 79, 83, 87). In rows 60/61/62/79
the header and the items it governs are the SAME cell, newline-separated ("Effective 25 Jun:\nAdded NJY
..."). In v6.8 and v6.9 SGX put the header on its own row inside the bordered entry. Same convention.

## Calibration against circulars we hold
    v14.2  issued 2024-11-04  "Amend trading hours of SGX Nikkei Derivatives ... (eff 4 Nov)"  = DT/AM 50 of 2024
    v14.9  issued 2025-03-19  "Amend T+1 session trading hours ... (eff 7 Apr)"                = DT/AM 15 of 2025

## The reading, and why the 2026-09-05 rule-out was too strict
Yesterday's ruling: "'Effective 11 Nov:' sits in a cell with no date and no version, bound to an issue
date only by cell-border formatting, with the year needing a second inference on top." Corrections:
- the binding is an OOXML border-style partition with zero merges — the document's own structure,
  like a table row — not a rendering artefact;
- the year is fixed by the entry's own Issue Date (2019-10-07) and the adjacent entry (issued
  2019-11-08, dating its items 18 Nov / 02 Dec): "Effective 11 Nov" in an entry issued 7 Oct 2019 can
  only be Monday 11 November 2019.
LAW-NO-FABRICATED-DATES as written requires that "a primary source states an unconditional, day-level
effective date". SGX's own product-parameter change log, in an SGX-authored entry, states one, in session
language ("(T+1) session Closing hours to 5:15am"). The one interpretive step is scoping a header row to
the items below it inside one file-encoded entry.

## What this does NOT change
- The 04:45 close state stands: five SGX artifacts verified today print "2.55 pm to 4.45 am" (portal
  2017-07/09, 2018 Apr calendar, 2019 calendar, content-api 2019-01/02/06). The workbook's log simply
  has no entry for the earlier 02:00 -> 04:45 move (it starts 2016-02-19; the 2017 portal already shows
  04:45). The chase agent's "positively doubtful" aside is answered by those artifacts.
- The 2019 DT/AM circular itself is still unfound; the workbook is a different SGX primary.

## Status
DECISION PENDING with the maintainer: accept the workbook entry as the day-level primary for row (A)
(2019-11-11, T+1 close 04:45 -> 05:15) and reverse the 2026-09-05 ruling recorded on issue #45 — or keep
the stricter reading and serve the intersection. The conservative table is being built either way; the
dated row is a strict refinement on top of it.
