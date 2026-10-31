# Independent NSE early review — 2026-10-31 UTC

Scope: source/interpretation and focused tests for the in-progress NSE changes. This is not the final exact-commit worktree review or full quality verification.

Second retrieval: operator PDF CMTR76941.pdf, 161272 bytes, SHA-256 `ce94ee1c54d98eccdf3c30fa0673ae2b6a49ea4ed4a72fb83d826f4359f71d58`, matches implementation evidence. Retrieval metadata and raw PDF are beside this report.

## Source-derived result

Circular149/2026 issued2026-10-19 unconditionally states a capital-market special session on Sunday2026-11-08. Venue union is: extended13:50–14:05 block trades; order-entry14:05–14:13; executable pre-open envelope14:13–14:20; regular14:20–15:30; extended15:30–15:35 CAS match; closed15:35–15:50; extended15:50–16:00 post-close. Times IST. The14:13 boundary is14:15 minus the printed2-minute random-closure range and uses the crate's established NSE immediate-match/conservative-envelope convention. Non-CAS continuous trading preserves the regular venue union until15:30 even when CAS securities enter price calculation and collection.16:15 is trade modification, not a trading close. IPO and illiquid-call subsegments add no union edge. The Sunday itself is the trade date.

Independent regex count over holiday rows:231 total=216Closed+9ReplacementBlocks+6Unsourced. The original231=216+8+7. Coverage windows are byte-identical to HEAD; six historical refused dates remain2011-10-26,2012-11-13,2013-11-03,2014-10-23,2017-10-19,2019-10-27. Historical negative hunt statements,2018 gap and2021undated-footnote disclosure remain in the evidence file.

## In-progress defects reported to author

1. NSE-CIRC-2026-149 Documents metadata row inserted in2025holiday table rather than Documents table.
2. TABLE doc still states8replacement days/7withheld and omits2026circular.
3. Ledger NSE row says6withheld but still adds2026banner date.
4. Evidence residual paragraph near former line445 ends 'remaining seven withheld dates'.
5. Yearly-count test expected2026tuple still(2026,15,1,0), should be(2026,15,0,1).
6. Coverage inventory's date-level incomplete count still7rather than6.
7. Advisory: several stripped module doc introductions are dangling sentence fragments.

The ISSUE_CONFIRMATION placeholder is known to the parent and excluded from these early defects.

## Focused validation

`cargo nextest` is not installed. Ran `. /home/agent/.cargo/env && cargo test --test venue_sessions holidays_tse_sse_nse::`:22passed,1failed, solely yearly-count expectation item5. The new2026phase/trade-date test passed.

Ran `. /home/agent/.cargo/env && cargo test --test schedule_documentation coverage_inventory::`:6passed,5failed. NSE-specific failure is item6. Four other failures concern concurrent ICEus row/prose counts and globexcryptocurrency revision-count prose, outside this review scope; parent notified.

No source-time/runtime-phase defect found. The listed prose/count/fence defects must be corrected and affected checks rerun before acceptance. No crate files were edited by this review.
