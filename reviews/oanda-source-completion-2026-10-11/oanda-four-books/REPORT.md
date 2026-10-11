Posted by an AI agent running as `gpt-6.1-sol` (`Codex`), using the maintainer's GitHub login.

Independent source review accepted for exact head `3e0e5b9a9a15357cc461b54269ff39e831af0281` (PR #337).

The independent OANDA verdict covers four books I did not author: `oanda_us_index_cfd`, `oanda_us_bond_cfd`, `oanda_us_commodity_cfd` and `oanda_brent`, their data/evidence, corresponding ledger prose and related shared normal-grid/test/metadata claims. I authored the earlier FX/metals change `8f4f87f`; those books, their authored files and my added FX/metals test regions are excluded from this independent verdict. Executing a shared integration harness does not expand that verdict. TRY and the full combined quality/MSRV chain belong to the other reviewer.

Fresh primary retrievals on 2026-10-11 UTC: Carter captures `20250326184653` and `20260217213704`, normal-hours capture `20240221005503`, and the current UK holiday and normal-hours pages. Each returned HTTP 200. Both Carter archives and the February 2024 normal-hours archive exactly reproduce the cited SHA256. The freshly retrieved live HTML differs in transient bytes from the cited capture, but my own HTML parser reproduces exactly the same 74 dated holiday sections from both. URLs, retrieval timestamps and hashes are in `retrieval.json`; independently downloaded bytes and fresh text extractions are in `evidence/`.

My standard-library HTML parser extracts source sections independently of the change's tests and constants. `derive.py` compares each shipped row with its same-date operator statement or preceding evening-reopen statement, retaining those source facts in `row-proof.json`. Every table has fewer than 100 rows, so every row was reviewed rather than sampled. All 190 rows compare successfully:

| Book | Closed | Early close | Late open | Replacement | Unsourced | Total |
|---|---:|---:|---:|---:|---:|---:|
| US index CFDs | 7 | 24 | 2 | 15 | 4 | 52 |
| US bond CFDs | 7 | 23 | 2 | 13 | 5 | 50 |
| US commodity CFDs | 7 | 20 | 2 | 12 | 0 | 41 |
| Brent | 7 | 18 | 0 | 5 | 17 | 47 |

The 2024 index/bond windows are 2024-01-01..2024-12-31 plus 2025-01-01..2026-10-30. Commodity and Brent windows are 2024-02-21..2026-10-30. Those windows do not waive the independent normal-week coverage gate or turn withheld dates into audited normal sessions. Ledger counts, documented book members, literal minutes, scope and publication horizons match the tables. Earlier normal weeks/holiday history remain disclosed activation gaps; no invented historical cutover was added.

The six pre-February-witness reopen rows—2024-01-02, 2024-01-16 and 2024-02-20 in each of index and bonds—correctly remain Unsourced. Their preceding holiday sections state 18:00 ET reopens but not the final closes. The February 21 normal-hours observation cannot establish an earlier final close. The older holiday closures and printed early closes remain separately recorded without claiming the entire preceding normal week is sourced.

The February 2024 hours bytes independently identify four US index listings, four US Treasury CFD listings and the five energy/commodity-metals listings. Chicago 17:01–15:59 converts to New York 18:01–16:59; New York listings print that latter grid directly. Spot metals' 18:05 opening is not borrowed. General US-index wording does not establish Japan 225 scope. Bond Carter/Good Friday closes remain distinct from indices, and index-only Independence Eve statements do not silently change the bond book.

All complete replacements were independently checked against their source reopen and full final close: literal 18:00 ET reopens remain 18:00 rather than being rounded to the normal 18:01; Independence/Thanksgiving replacements preserve the following date's printed close; Holy Thursday 2025 keeps the explicitly stated 17:00 close through a replacement rather than clipping to normal 16:59. Carter's dated 24-hour context selects 09:30 ET before the stated 18:00 reopen, with bonds independently 13:15 ET. The incomplete 2026 Memorial reopen `18:0` remains withheld on the following trade date.

For Brent, I independently converted each scalar ET instant with IANA `America/New_York` and `Europe/London` at its actual civil date. All shipped scalar conversions have a five-hour offset. Literal 20:00 ET reopens become 01:00 London on the following civil/trade date. Weekday replacements retain both the 01:00–21:59 segment and the 22:05–22:59 segment; Friday has no later segment; Thanksgiving retains the printed 20:00 London final close. The current operator dagger note independently supports Sunday 23:01, Friday 21:59 and both weekday breaks. No agricultural reopen is attributed to Brent.

Findings fixed before acceptance:

1. Six source-silent UK/local holiday sections lacked the same withholding treatment already applied to equivalent 2024 sections: 2025-04-21, 2025-08-25, 2026-04-06, 2026-05-01, 2026-05-04 and 2026-08-31. Each now has an Unsourced row and a public refusal test. The May 2026 sections were checked individually: May 25 explicitly prints a Brent arrangement and remains sourced; May 1/4 do not. Comparable May 2024/2025 sections explicitly affirm BCO open.
2. Brent's 2026-09-07 source prints only its 13:29 ET close; 20:01 belongs to agricultural commodities. The incorrect Brent reopen assertion was removed from evidence and module citation; the already correct runtime close is unchanged.
3. Brent's stale four-withheld-date prose and counts now describe 17 withholdings (seven in 2024, six in 2025, four in 2026) and 47 rows. The commodity ledger now describes the formerly missing MLK close as restored, rather than missing.

Independent exact-head checks: 20/20 publication integration tests and the golden-grid test pass. All 74 documentation/source/digest fences previously passed at source-identical head `5a460904bc7a4d2b76f6867aae4347dceccd5d6a`. The later head changes only four unrelated coverage-inventory prose counts; my reviewed source/evidence/ledger/test/metadata hashes remain identical. That inventory correction and the full fresh final quality chain belong to the other reviewer. Affected strict clippy, formatting and diff checks pass. I changed the single shipped Carter index close from 09:30 to 21:30 in the detached review worktree: its public regression fails as expected. The mutation was restored and all 20 publication tests pass again. Logs are retained here; the checkout is clean at the reviewed head. This report does not claim the other reviewer's full quality/MSRV result.

BME acceptance carried to this head: my earlier independent source acceptance was for exact author `3dc4df688adc7a59ed5bb085723e6ffd7f70d120`, following the auction-call repair. The normal profile, holiday module, evidence file and both affected BME test files are byte-identical at this integrated head, as recorded in `reviewed-hashes.json`. All 27 independently retrieved BME PDFs, complete row proof and earlier mutation evidence remain in `/tmp/bme-independent-review/`. The later golden-only author change `b026e527e7fb35fcb45cba53d9427c129ddaa92f` also matches the integrated BME golden lines. Its executable weekly total is independently recomputed from Circular 1/2001 plus Circular 1/2023: five times (30,570 regular seconds + 30 opening-uncross seconds + 600 closing-uncross/TAL-union seconds) = 156,000 seconds. Opening/closing calls are order entry and contribute no executable seconds. The golden regression passes.

No unresolved source/data/prose defect remains in this review's scope. This is an acceptance of honestly partial published calendars, not a claim that their activation gaps or all OANDA history are complete.

Final-head verification: the detached checkout is clean at `3e0e5b9a9a15357cc461b54269ff39e831af0281`. The Carter mutation was repeated at this exact head, failed, and was restored; 20 publication tests and the golden regression pass again. All reviewed source hashes reproduce.
