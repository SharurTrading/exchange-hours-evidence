# Independent source review of issue #374 confirmation

Verdict: **PASS — no blocking or advisory defects found at the final reviewed head.**

Reviewed crate head: `6078da48c15a2dc602961a7ea0759ef0cfcaa17c`.
Base: `d3f6b21db8f4f7523f0c79b786c16c6852c4678c` (merged PR #375).
Detached review worktree: `/workspace/exchange-hours-review-confirm374-us`.
Review date: 2026-10-31 UTC. The reviewer did not author the confirmation changes.

## Scope and method

The exact diff contains 11 Markdown files: ten evidence files (NSE, Xetra and eight ICE identities), plus the source-monitoring registry. There are no runtime, test, Cargo, ledger, coverage, README, CHANGELOG, plan or charter changes. All ten changed evidence files retain their original Documents sections byte for byte. The Xetra 2027 watch remains issue #200; the completed forward confirmations remain attributed to #374.

The source review uses independent HTTP retrievals and the raw retained bytes, not the authors' reports as source truth. `INVENTORY.json` records the three independent primary-PDF retrievals, exact URLs, HTTP status, UTC retrieval instants, sizes and SHA-256s. All three are HTTP 200 and match both the prior citations and fresh author captures:

| Primary artifact | Independent retrieval UTC | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| NSE CMTR76941 | 2026-10-31T23:19:53.936922Z | 161272 | `ce94ee1c54d98eccdf3c30fa0673ae2b6a49ea4ed4a72fb83d826f4359f71d58` |
| Xetra final session 2026 | 2026-10-31T23:19:53.937392Z | 158845 | `d3618ef9738a3cae92909d11d4eaf820ab7b71d1e723c1fa04a21062e9738115` |
| ICE Christmas 2026 | 2026-10-31T23:19:53.937858Z | 132381 | `a7658155b57c51085cd3b36abc9ff6b91f3ca353cda88365a06459ebb40f0801` |

`AUTHOR-CAPTURE-VERIFICATION.json` records successful independent size and SHA-256 reproduction for all 23 author manifest entries across the NSE, Xetra and ICE confirmation folders, including the supplementary notices. Raw HTML can vary in dynamic page content across retrievals; each author's stored HTML reproduces its declared digest, and the independently retrieved visible circular content agrees.

## Recomputed source and prose claims

`FINAL-COMPARISON.json` records a Python regular-expression parser of the final-head block arrays, checked against expectations derived independently from the source PDFs and the already sourced normal profiles: seven arrays, 24 block entries, all matching. The source registry's three confirmation sentences link to the appropriate evidence and retain the original effective sessions and deadlines.

- **NSE:** the original circular unconditionally specifies the live 2026-11-08 capital-market session. The six-block venue union retains block deals 13:50–14:05, order entry 14:05–14:13, executable pre-open 14:13–14:20, regular trading 14:20–15:30, CAS matching tail 15:30–15:35 and post-close 15:50–16:00 (Asia/Kolkata). The earliest random closure is 14:13, derived from the last two minutes before 14:15. Non-CAS continuous trading supplies regular status through 15:30 even while CAS securities run auction phases. The 15:35–15:50 gap remains closed; administrative modification until 16:15 creates no additional trading. The confirmation changes none of these values or historical gaps.
- **Xetra:** the XETR section of the final-session PDF supplies the 2026-12-30 date, 07:00 pre-trading, 08:00 retail start, 08:55 opening call, 13:00 intraday call, 14:00 closing call, uncross no earlier than 14:05, DAX/MDAX/SDAX Trade-at-Close end 14:10 and post-trading end 15:00 (CET). The seven-block merged envelope matches. The new prose correctly attributes 09:00:30 and 13:02:30 conservative uncross instants to the existing normal-profile basis rather than pretending they are literals in this PDF.
- **ICE:** the Christmas PDF supplies December 24 Coffee/Cocoa/Cotton/FCOJ 13:05 matching close, regular Sugar hours, the shortened queue 30 minutes after matching close through 15:30, December 25 closure, and Monday December 28 late opens/regular closes. The fresh master-hours and original PCPO support PDFs match this reviewer's independent captures from PR #375 byte for byte. The five Monday replacement families retain Thursday queues at offset -4: Sugar 13:30–15:30, others 13:35–15:30; Monday matching starts 08:00, with existing respective closes 13:00, 13:30, 13:30, 14:20 and 14:00. Cotton's dependent December 29 replacement retains Monday 14:50–18:00 PCPO, 19:30–21:00 pre-open and 21:00–Tuesday 14:20 matching. FANG+ and USDX 13:15 Christmas-eve closes, Friday closure, regular Monday, and the broad venue's withheld December 24/28/29 answers are accurately described. No family schedule is substituted for the unresolved broad venue envelope.

## Independent bounded amendment checks

Independent raw responses and request metadata are in `CHANNELS.json`, `ADDITIONAL-CHANNELS.json` and their named byte copies; `CHANNEL-RELEVANT-RECORDS.json` preserves the relevant returned listings.

- **NSE:** the live API query for October 19–31 returns 275 records and exactly six distinct later CMTR documents (77217, 77210, 77196, 77188, 77182 and 77047). Their retained full PDF/archive content does not amend the cash-session timetable. ISC77098 explicitly references CMTR76941 and November 8; CMPT77037 and CMPL77195 address clearing/reporting administration. The duplicate listing of the original CMTR76941 is not counted as a second distinct notice.
- **ICE:** the independent listing response matches the author response SHA-256 exactly. Its ten latest entries span October 2–29, with the original Christmas notice dated October 22 and no later Christmas amendment among the entries returned. The result is deliberately scoped to those latest entries; it is not a claim to have read all 129 catalogue results.
- **Xetra:** independent current circulars, both October 30 circulars 049/2026 and 050/2026, the current calendar, RSS and query responses corroborate the prose. The current first page has ten entries, RSS ten entries, and the exact final-session query five results. Both newest circulars repeat December 30 and refer readers to the official calendar announcement. The calendar still links the same PDF. No superseding timetable appears in these checked channels. Raw RSS reproduces the author digest exactly. The human-readable October 30 circular dates are preserved without rewriting the RSS's different timestamp fields.

The new wording says what was confirmed as of the stated October 31 retrievals. It does not claim the future session has executed or exclude later notices. LAW-WATCH requires confirmation before the effective day and supplies no minimum proximity to that day; these fresh checks precede the November 7, December 23 and December 29 confirm-by deadlines. All repository dates used for the confirmation are UTC.

## Verification and limits

- Exact-head `git diff --check` passes, and the detached worktree is clean.
- The diff is confined to the 11 declared Markdown files; runtime and test bytes are identical to the merged base.
- This is a source/prose review. The separate final-head gate agent owns the complete quality, MSRV and Markdown verification and its recorded results.
- No new mutation was needed because no shipped row changed. The unchanged CME/ICE runtime review and meaningful mutations are retained in `reviews/2026-10-31-future-update/independent-final-us-review/REPORT.md` and its logs; the original PR #375 independent reviews cover the unchanged NSE/Xetra rows. This confirmation review independently rechecked the six/seven block counts and relevant ICE arrays against fresh primary bytes.
- No crate edits, external posts, commits or pushes were made by this reviewer. The parent owns evidence STATUS and the attributed PR review publication.
