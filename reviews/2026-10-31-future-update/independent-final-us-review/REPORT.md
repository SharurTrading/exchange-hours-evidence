# Independent CME and ICE source review — 2026-10-31 UTC

Verdict: **no blocking defects found in the reviewed CME/ICE change set**.

Data commit: `5dff8b606ab856da657c0a8d368ad34186fe5bc0`.
Base: `02a3c89495c4f7f9b51fab833fd04d2bc815f456`.
Verified successor: `72dff410dbab364ba9ab90c934af4abd7de8d7c4` differs only in `docs/schedules/updating.md`, restoring the pinned MRX checklist heading and moving its Q1 target into the body. No reviewed data or evidence changes, so the source verdict carries forward. The lead reviewer owns full quality/MSRV/markdown verification; this review runs targeted tests and two meaningful mutations.

## Independent evidence and derivation

Fresh second retrievals are indexed in `INVENTORY.json`, including URL, UTC retrieval, status, byte count, digest and comparison with the implementation captures. All three CME service JSONs and the ICE Christmas PDF exactly match their cited captures. The raw CME notice HTML differs only in embedded Akamai script values; its visible document text is byte-equivalent after script/style exclusion, including the quoted 02:00–05:00 CT statement. The current ICE master hours table (September 2026) and the original 2018 PCPO notice were also independently retrieved.

`rederive.py` is this reviewer's independent parser, not the implementation author's derivation. `INDEPENDENT-DERIVATION.json` records all comparisons.

- CME: the raw product 8478 / group BF events derive three Monday trade dates (October 5, October 26, November 2) and all 21 blocks. Friday 16:01 pre-open and 16:02 matching, Saturday 02:00 close and the sourced replacement queue/reopen, uninterrupted Sunday, and Monday 16:00 close agree exactly with the two static arrays. Monday-relative offsets are -3/-2/-1/0. The November 2 replacement includes the entire DST-fold Sunday; both UTC copies are explicitly tested.
- All 98 upstream CME holiday rows and all five prior exception arrays are unchanged. The same four audited windows remain. Three additions make 101 rows. The nine prior normal-week revisions remain identical; precisely six October temporary-profile boundaries are removed (15 → 9 revisions). Launch-era data, the resolved 2023 date, the September queue and historical coverage are preserved.
- ICE: the Christmas notice independently supplies Thursday 13:05 early closes for Coffee/Cocoa/Cotton/FCOJ, regular Sugar hours, the post-close queue beginning 30 minutes after matching ends and ending 15:30, Friday closure, and Monday late/regular opens and regular closes. The normal master supplies the unchanged closes.
- The five December 28 replacements match: Sugar Thursday 13:30–15:30 queue plus Monday 08:00–13:00 matching; Coffee/Cocoa Thursday 13:35–15:30 plus Monday 08:00–13:30; Cotton Thursday 13:35–15:30 plus Monday 08:00–14:20; FCOJ Thursday 13:35–15:30 plus Monday 08:00–14:00. Thursday is offset -4 from the Monday trade date.
- Cotton December 29 is independently derived from unchanged normal queues/current matching: Monday PCPO 14:50–18:00, Monday pre-open 19:30–21:00, Monday 21:00 through Tuesday 14:20 matching, all at offset -1. This suppresses the raw closed-Friday queue while retaining Monday's queue and overnight matching.

## Explicit regular Pre-Open scope check

The 2018 notice's phrase “Exchange business day prior to each trading day” governs PCPO. It does not announce a multi-day regular 20:00 Pre-Open crossing a closed holiday. The admitted current profiles contain regular pre-open wraps only on Monday–Thursday, with no Sunday queue. Their Thursday evening wraps feed Friday, which the Christmas notice closes; there is no existing normal-grid segment that feeds Monday from Sunday. The holiday notice explicitly restores Thursday afternoon PCPO and Monday matching without stating a Sunday or multi-day regular pre-open. Accordingly the December 28 replacements drop no sourced regular Pre-Open within the existing modeled scope; this review does not infer an additional one.

## Counts, rows and document provenance

Independent ICE table counts: Sugar 41; Coffee 43; Cocoa 43; FCOJ 35; Cotton 39; FANG 37; Dollar Index 27; venue 51. Net additions are FCOJ December 28, Cotton December 29, venue December 29; four existing December 28 scalar rows become replacements. All original rows remain present and FCOJ's exact eight 2027 withheld rows are unchanged. The venue's new date is withheld because its routed families disagree under the existing intersection rule.

The three new CME dates carry their exact source-window document IDs at T2. ICE replacements carry `IFUS-NOTICE-2026-CHRISTMAS` at T1, with the Tuesday derivation disclosed from the Christmas closure and unchanged normal queues. The source PDF's settlement/TAS windows are not treated as matching closes. Changed quotations, times, kinds, scope and source digests agree with the independently retrieved bytes. There are no charter or plan edits in the overall change set; source, holiday, test and prose classes were identified from the diff.

## Validation and mutations

- `cargo xtask verify-evidence` passed for `CME-SVC-2026-10-02`, `CME-SVC-2026-10-23`, `CME-SVC-2026-10-30` and `IFUS-NOTICE-2026-CHRISTMAS`; the best-effort literal quote matcher reports no match for compact event summaries, so those summaries were checked through the independent source parser and PDF text extraction above.
- CME targeted scope: **30 passed**.
- ICE targeted scope: **25 passed**.
- CME mutation: moved the October 24 queue opening from 15:15 to 15:16. The exact-queue test failed at its 15:15 order-entry assertion (expected true, got false).
- ICE mutation: moved Sugar's Thursday PCPO end from 15:30 to 15:31. The Christmas test failed at its end-exclusive 15:30 acceptance assertion.
- Both mutations were restored and their targeted tests passed again. `MUTATION-RESULTS.json` and the six logs retain exact results. Detached worktree clean after restoration.

No external posts or main-checkout edits were made. Full verification is coordinated by the lead reviewer on the verified successor.
