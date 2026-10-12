# Independent Brent underlying-policy cross-review

Reviewed 2026-10-12 UTC. Scope: the other author’s 17 Brent proposals in `/tmp/oanda-underlying-brent-resolution.md` and `.json`, compared with public operator bytes under `/tmp/oanda-public-final-review/normal-weeks/oanda-underlying-policy-2026-10-12/`. Read-only; no runtime verification claim and no broker completeness approval.

**Verdict: no blocking data findings.** All 17 original gap dates match exactly:13 inherit-normal proposals and4 inherit-reopen proposals. Independently checked 32 executable blocks (64 boundary instants), all calendar weekdays, actual IANA London offsets and UTC conversions, Sunday-to-Monday dates, Friday omission of later block, and UserCustomized/no-operator-proof labels. All 7 source-manifest digests and all embedded row source digests match the retained bytes. PDF source text was freshly extracted independently; three calendar page 2 renders and OANDA commodity guide page 3 were visually read.

One nonblocking prose finding: the report describes the prior `oanda_brent.md` 19:00 ICE ordinary close defect as still present. Current `/tmp/oanda-source-completion/docs/evidence/oanda_brent.md` already says 01:00–23:00 London. Label this as a prior finding already corrected or remove it. This does not change a proposed row. Root and author notified.

## Exact reviewed artifacts

- `/tmp/oanda-underlying-brent-resolution.md` — SHA256 `e4c8235cff0d6641e72ad9750ec2b3b2e134e7821a0fa49ea0e2ed045f30eb23`
- `/tmp/oanda-underlying-brent-resolution.json` — SHA256 `4ba3838560a85b02ccce948492fd3591645f3ba327c0223ba697a49ce88b1c82`

## Source and policy checks

- Identity is ICE Futures Europe Brent Crude Futures, product 219, physical B/logical BRN. The operator product HTML prints those codes and ordinary London01:00–23:00 / New York20:00–18:00, Sunday London23:00. OANDA’s static guide page 3 names ICE EUROPE for Brent. Its old grid is not used to date or replace the current broker grid. CME energy, cash LSE holidays and oil-marker calculation windows are not donors.
- Annual TD key positively says regular trading hours. The listed UK closure exceptions name agricultural, gas, power, emissions and carbon products, excludingBrent. Thus underlying Brent ordinary trading on the 13 dates is supported, but OANDA silence is still not broker affirmation. January 9 Carter Circular 25/001 names SOFR/Swapnote contracts only; its settlement column and trading-ceases column are distinct.
- All 4 reopen proposals use the 2024 calendar’s prior holiday C/D trading-hours early close 18:30 London / 13:30 ET, then the underlying ordinary 20:00 ET restart (01:00 BST next date / 00:00Z). This is a specific selected policy, corroborated by other directlyprinted OANDA 20:00 ET reopens. It is not a dated OANDA proof for those 4 missing reopens.
- The selected 01:00 restart is explicitly one minute earlier than OANDA’s ordinary 01:01 London restart. That minute is the chosen exception; it would disappear under a different policy that mechanically intersects every donor block with the broker’s ordinary grid. Report/JSON consistently choose the exception and preserve broker 21:59 close, Monday–Thursday 22:05–22:59 later block and Friday no-later-block. Existing direct broker holiday rows take precedence.
- All 17 dates are outside US/UK DST mismatch windows. Summer offsets BST +01 / EDT −04; Carter January 9 and Thanksgiving eve November 26 are GMT +00 / EST −05. The first Monday block begins Sunday 23:01 London; all Friday blocks end 21:59 and stop. New York 20:00 on the prior civil holiday becomes London 01:00 next date, not 20:00 London or 20:01.
- The 2026 temporary DST PDF separately prints Brent 00:00–22:00 GMT / 20:00–18:00 EDT for October 25–30; 2010 Circular 10/070 provides compatible context. Neither keys a new cutover or affects any of the 17 dates. November 2024 calendar independently confirms B 20:00 UK / 15:00 ET, superseding January 2024 B 19:00. That amendment is a counterexample outside the 17 proposals, not a reason to change their C/D cells.

## Per-date independent source acceptance

| Date | Checked source interpretation | Blocks / UTC |
|---|---|---|
| 2024-04-01 | 2024 p2 Easter Monday TD; p4 TD regular; named closures exclude Brent | 2 blocks, all boundaries verified |
| 2024-05-28 | May 27 D / p5 Brent 18:30 trading close; next ordinary restart 20 ET | 2 blocks, all boundaries verified |
| 2024-06-20 | June 19 C / p5 Brent 18:30 trading close; next ordinary restart 20 ET | 2 blocks, all boundaries verified |
| 2024-07-03 | July 4 C, not July 3; ordinary preceding Wednesday | 2 blocks, all boundaries verified |
| 2024-07-05 | July 4 C / p5 Brent 18:30 trading close; following Friday restart 20 ET | 1 blocks, all boundaries verified |
| 2024-08-26 | 2024 p2 UK holiday TD; p4 regular; named closures exclude Brent | 2 blocks, all boundaries verified |
| 2024-09-03 | September 2 C / p5 Brent 18:30 trading close; next ordinary restart 20 ET | 2 blocks, all boundaries verified |
| 2025-01-09 | 2025 ordinary day; Circular 25/001 limited SOFR/Swapnote amendment | 2 blocks, all boundaries verified |
| 2025-04-17 | 2025 p2 TD; added marker windows are not trading closes | 2 blocks, all boundaries verified |
| 2025-04-21 | 2025 p2 Easter Monday TD; p4 regular; named closures exclude Brent | 2 blocks, all boundaries verified |
| 2025-07-03 | July 4 C, not July 3; ordinary preceding Thursday | 2 blocks, all boundaries verified |
| 2025-08-25 | 2025 p2 UK holiday TD; p4 regular; named closures exclude Brent | 2 blocks, all boundaries verified |
| 2025-11-26 | 2025 p3 Thanksgiving November 27 C / November 28 B; preceding Wednesday ordinary | 2 blocks, all boundaries verified |
| 2026-04-06 | 2026 p2 Easter Monday TD; p6 regular; named closures exclude Brent | 2 blocks, all boundaries verified |
| 2026-05-01 | 2026 p2 April 30 TD marker adjustment; May 1 ordinary Friday | 1 blocks, all boundaries verified |
| 2026-05-04 | 2026 p2 May Day TD; p6 regular; named closures exclude Brent | 2 blocks, all boundaries verified |
| 2026-08-31 | 2026 p2 Summer Bank TD; p6 regular; named closures exclude Brent | 2 blocks, all boundaries verified |

## Primary byte inventory

| Operator source | SHA256 |
|---|---|
| [ICE-2024.pdf](https://web.archive.org/web/20240130192820id_/https://www.theice.com/publicdocs/Trading_Schedule.pdf) | `690bb94d096b980cf72322c58c0a298cf75b50a1777f2ad9d8ecb4d4425b5980` |
| [ICE-2025.pdf](https://web.archive.org/web/20250523135606id_/https://www.theice.com/publicdocs/Trading_Schedule.pdf) | `bd107d0525a758d4715a6f39fd58d6eb24b39baafc555973945ad6bbf6607ea0` |
| [Trading_Schedule-2026.pdf](https://www.theice.com/publicdocs/Trading_Schedule.pdf) | `0f46a2b316933b4fcf25be81411273e7bf7119bbcf22dcee0d40ce456b86b9a0` |
| [25001.pdf](https://www.ice.com/publicdocs/circulars/25001.pdf) | `97b2647bf995e6402e5f79f17b7c4cb2390c65ff53b880fe9544c1bb07ca30a9` |
| [Brent-product.html](https://www.ice.com/products/219/Brent-) | `8f0d899a5a32d257469bcef25cfaf03c9782706bf25fe2c2afc11fd7d178927f` |
| [ICE-DST-2026.pdf](https://www.ice.com/publicdocs/futures/Trading_Schedule_Temporary_Trading_Hours_for_DST.pdf) | `c9ffb649c802465a7f5ceedef403140c36a3575966cd619e3d4a1526fe6d9579` |
| [10070.pdf](https://www.ice.com/publicdocs/circulars/10070.pdf) | `31049852805e6a17cbbe62f15c2e0733979507562331e8daa550fc4c4e372e18` |
| [November 2024 ICE edition](https://web.archive.org/web/20241118133442id_/https://www.theice.com/publicdocs/Trading_Schedule.pdf) | `2b08e9220d2258caa5eccbe09c651ab6d8f851f3768d9b4e1d10227419253935` |
| OANDA static Hours_of_Operation 252 | `778ea39e0f71005015a111963061cd86f8d7fce7b589af0279316992239244ba` |
| OANDA current UK hours | `991afbcc0a92ad2996e68e23dc96099ef1dbda57f871c3144edcb2d2ddaa1d6b` |

Machine check details and exact reviewed hashes: `/tmp/oanda-brent-cross-review/check-results.json`; independent validator: `/tmp/oanda-brent-cross-review/check.py`. All 17 recommendations remain inherited User policy proposals. Direct OANDA T1/T2 completeness remains unchanged.
