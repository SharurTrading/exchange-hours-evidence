# DECISION 2026-09-06: SGX's Derivatives Products Description change log is admitted as a primary source for effective days

Delegated by the maintainer ("make the best correctness and architectural decision and log it").
Implemented in PR #68 (branch sgx-changelog-dates, commit 8827420). Closes #45.

## The decision
Accept. Under LAW-NO-FABRICATED-DATES as written ("a primary source states an unconditional, day-level
effective date"), SGX's own dated, SGX-authored product-parameter log meets the test. Refusing it would
elevate document genre over the law's criterion, at the cost of under-reporting the overnight leg for
eight weeks on four keys and SiMSCI's bounds for four months.

## The rows it changes
- Singapore: 2019-02-06 (intersection) + 2019-06-11 (witness) -> ONE dated cutover, Monday 2019-06-10
  (v6.1, issued 2019-05-21: "Amended trading hours for SGP, SGPO and ST eff 10 Jun" — one cell).
- Japan, China, Singapore, NTR (USD): the 05:15 T+1 close, Monday 2020-01-06 -> Monday 2019-11-11
  (v6.9, issued 2019-10-07: "Effective 11 Nov:" / "(T+1) session Closing hours to 5:15am all T+1
  traded contracts" — a header row scoping the items in one border-partitioned entry).
- Taiwan: unaffected (launch 2020-07-20 already at 05:15).
Both days are Mondays SGX chose; no Monday-rounding applies.

## The convention, now in AGENTS.md ("Modeling conventions")
An operator's own dated change log is a primary source for an effective day when: (1) the entry is
the operator's — authored and issue-dated in the document; (2) the effective day is stated inside the
same entry — same cell, or a header row scoping items within one file-encoded entry that is the
operator's recurring convention; (3) session language; (4) calibrated against at least one cutover the
crate already holds from a circular. Excluded: logs a reader must date from formatting; days inferred
from a month/filename/directory; member firms' summaries.

## Why the 2026-09-05 rule-out was wrong
It called the entry's structure "cell-border formatting". Parsing the OOXML: mergeCells = 0; multi-row
entries are runs of rows with borderId 2 (top) / 68 (middle) / 67 (bottom, carrying the date) — the
document's own structure, like a table row. The year is fixed by the entry's issue date and the
adjacent entries. Calibration: "(eff 4 Nov)" = DT/AM 50; "(eff 7 Apr)" = DT/AM 15.

## Residual risk, stated
The v6.9 scoping step. Bounded: even if the header did not govern the line, the SGX-artifact bracket
(content API 2019-06-21 at 04:45; api2 2019-11 and 2019-12 factsheets at 05:15; AR2020 "November 2019")
confines the day to November 2019, and three independent broker notices name 11 Nov.

## Where it is logged in the repository
AGENTS.md (convention bullet); src/.../sgx_equity_index/history.rs ("2019-06-10 AND 2019-11-11"
paragraph); docs/schedules/verification.md (five rows); docs/schedules/sources.md (APAC-SGX-DERIVATIVES);
CHANGELOG.md (Fixed); issue #45 (closing PR).
