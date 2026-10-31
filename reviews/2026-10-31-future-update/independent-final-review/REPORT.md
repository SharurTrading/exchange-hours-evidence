# Independent final review — 2026-10-31 UTC

Candidate: `72dff410dbab364ba9ab90c934af4abd7de8d7c4`.
Base: `02a3c89495c4f7f9b51fab833fd04d2bc815f456`.
Implementation PR: <https://github.com/SharurTrading/exchange-hours-rs/pull/375>.
Evidence dependency: <https://github.com/SharurTrading/exchange-hours-evidence/pull/40>.

Verdict: **PASS — no blocking data, prose or verification defects remain**.
The complete gate and restored mutation checks passed in the detached review
worktree. The initial documentation-fence defect is resolved on this exact head.

## Scope and isolation

The review worktree is `/workspace/exchange-hours-review-20261031`, detached at
the candidate commit. The main checkout is never mutated. Logs, fresh source
bytes, hashes, comparison JSON and mutation helpers live in this evidence
directory. `EXCHANGE_HOURS_RESEARCH` points to the evidence checkout; the shared
Cargo target directory is reused only as a compilation cache.

The diff contains 27 files: five data modules, eleven evidence files, six test
files, four schedule-documentation files and the CHANGELOG. No charter, plan,
dependency, identity, routing, wire-format or public API changes occur.
`file-classification.json` records every path.

## Independent NSE and Xetra source review

Fresh retrievals, made independently of the implementation captures, are
recorded in `fresh-retrieval.json`. The three newly cited primary PDFs reproduce
their Documents-table digests exactly:

| Document | SHA-256 |
|---|---|
| NSE/CMTR/76941, circular 149/2026 | `ce94ee1c54d98eccdf3c30fa0673ae2b6a49ea4ed4a72fb83d826f4359f71d58` |
| Xetra final trading session 2026 | `d3618ef9738a3cae92909d11d4eaf820ab7b71d1e723c1fa04a21062e9738115` |
| Xetra Trading Calendar 2027 | `5c62bf0a78afb8f6123638d6e7b9a30c864799e2c2210b73b13bcdb6e9a64cf2` |

The current Xetra trading-parameter sheet and FWB rules were independently
retrieved as corroboration for the inherited ordinary auction and order-entry
semantics. The parameter URL redirects to its current content hash; the manifest
retains both the requested and final URLs rather than treating a redirect as a
new cutover.

### NSE — 2026-11-08

The source is an unconditional capital-market special session on the named
Sunday, dated 2026-10-19. Its printed rows independently give block deals
13:50–14:05 IST; pre-open order entry from 14:05, with the last-two-minute
random close in the 14:10–14:15 limit-order period; matching 14:15–14:17;
buffer 14:17–14:20; continuous open 14:20; CAS continuous close 15:15;
non-CAS continuous close 15:30; CAS matching through 15:35; transition to
15:50; and post-close trading 15:50–16:00. Modification through 16:15 is not
an executable session.

The six code blocks follow from those rows and the existing venue auction
envelope convention: Extended 13:50–14:05, order-entry-only 14:05–14:13,
Extended 14:13–14:20, Regular 14:20–15:30, Extended 15:30–15:35 and
Extended 15:50–16:00. The 14:13 boundary is derived from 14:15 minus the
two-minute random-close window, not quoted as a separately printed matching
start. The evidence prose explicitly distinguishes the printed matching and
buffer rows from the inherited nominal envelope convention. Non-CAS trading
keeps the venue executable throughout CAS collection; the IPO/relisting and
illiquid subsegment windows create no outer-envelope edge. The Sunday itself
is the trade date; no wrap or local-date conversion is invented.

Only the 2026-11-08 holiday tuple changes compared with the base. Every prior
replacement array remains semantically identical. The newer-main 2026-01-15
election closure remains `Closed`, T2, `NSE-HOLMASTER-2026`. Independent tuple
parsing gives **232 rows = 217 Closed + 9 ReplacementBlocks + 6 Unsourced**.
The two audited windows and the 2018 bridged residual remain unchanged.

### Xetra — 2026-12-30

The one-page primary notice separates XETR from XFRA. The reviewed identity
models the documented XETR liquid DAX-share scope; XFRA and off-book reporting
deadlines are excluded. The notice supplies 07:00 pre-trading, 08:00 retail
early, 08:55 opening-auction call, 13:00 intraday call, 14:00 closing call,
closing-price determination no earlier than 14:05, DAX/MDAX/SDAX
Trade-at-Close ending 14:10, and post-trading ending 15:00 CET.

The unchanged ordinary conservative auction edges supply 09:00:30 and
13:02:30. The replacement therefore preserves order entry 07:00–08:00,
Extended 08:00–09:00:30, Regular 09:00:30–13:00, Extended
13:00–13:02:30, Regular 13:02:30–14:00, Extended 14:00–14:10 and
order entry 14:10–15:00. Retail late does not survive the final-session
timetable. A scalar early close cannot retain the shortened post-trading
phase or classify the new closing auction correctly.

This adds precisely one tuple, 2026-12-30. Independent parsing gives
**128 rows = 124 Closed + 3 scalar early closes + 1 ReplacementBlocks**, with
zero Unsourced rows and unchanged audited windows. The new 2027 PDF confirms
the five existing weekday closures. Its four asterisked dates state only that
hours may differ; no final intraday instant or unconditional early close is
fabricated from that footnote.

`source-review-counts.json` and the reviewed snapshots retain the independent
tuple comparisons and exact module hashes. These data files are unchanged
between the initial source-review head `5dff8b6` and the final candidate.

## CME and ICE independent source review

The separately authored source review is
`../independent-final-us-review/REPORT.md`, with its own fresh retrievals,
independent parser, raw event derivation and meaningful mutations. It found no
blocking defects. This review inspected that report, the complete implementation
diff, the changed records and the independently recomputed whole-change
inventory; it does not present the other reviewer's retrieval as its own.

The CME source parser matches all 21 blocks for the three Monday trade dates
spanning the October Saturday maintenance extensions, preserving every one of
the base's 98 holiday rows and all four windows. Three exceptions make 101
rows. Exactly six October temporary-profile boundaries are removed, leaving
the nine earlier normal-week revisions and ordinary detached behavior intact.
The ICE source review verifies all six replacement arrangements, the exact
post-close queues, Cotton's following wrapped day and the eight pre-existing
FCOJ 2027 withheld dates. Shared counts independently agree: Sugar 41, Coffee
43, Cocoa 43, FCOJ 35, Cotton 39, FANG 37, Dollar Index 27 and venue 51.
The broad venue adds one withheld date because exact-family arrangements
disagree; it is not substituted for those families. `whole-change-counts.json`
records this reviewer's inventory.

## Prose, provenance and policy checks

New and changed phase times, dates, kinds, counts, document IDs, windows,
conditional-date notes and CHANGELOG statements agree with the reviewed data
and source interpretations. The PR description was checked through GitHub's
read-only metadata tool and reports the candidate hash accurately. Source
publication dates remain distinct from retrieval dates. New repository records
use 2026-10-31 UTC, and exchange event dates remain venue-local.

Forward reconfirmations are concretely tracked by issue #374: NSE by
2026-11-07, ICE by 2026-12-23 and Xetra by 2026-12-29. The issue was read
independently and contains all three sets of deadlines and source links. No
conditional US overnight or MRX launch is activated. Existing OANDA and other
publication boundaries remain unchanged. Evidence PR #40 is an explicit merge
dependency for the default-branch digest audit.

## Verification and findings

The initial candidate `5dff8b6` failed the pinned MRX checklist-marker test:
`docs/schedules/updating.md` had renamed a heading asserted by
`tests/schedule_documentation/fences.rs`. This was reported before completion.
Candidate `72dff410` preserves that exact marker and places the Q1 2027 target
in its body. `repaired-fence.log` records the formerly failing test passing;
`quality-initial.log` preserves the original failure. No source/data edit was
required by the repair.

The full quality chain completed successfully on the final candidate:

- `cargo fmt --all --check`: passed.
- `cargo clippy --all-targets -- -D warnings`: passed.
- `cargo nextest run --all-targets --failure-output immediate-final --status-level fail`:
  **1407 passed, zero skipped**, 34 binaries; 625.186 seconds, including the
  exhaustive coverage-control test. The two nextest output flags affect logging
  only, not test selection or execution.
- `cargo test --doc`: **3 passed**.
- `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps`: passed.
- `cargo deny check`: passed; advisories, bans, licenses and sources all report
  OK. Unused pre-existing license-allowance warnings are non-failing.
- `cargo +1.95 check --all-targets`: passed on the final candidate.
- `npx markdownlint-cli2@0.23.3`: passed, **175 files, zero issues**.
- `cargo xtask verify-evidence`: all seven document IDs passed:
  `NSE-CIRC-2026-149`, `DB-FINAL-SESSION-2026`, `DB-TC-PDF-2027`,
  `CME-SVC-2026-10-02`, `CME-SVC-2026-10-23`, `CME-SVC-2026-10-30`, and
  `IFUS-NOTICE-2026-CHRISTMAS`. The best-effort literal matcher cannot match
  compact summaries directly to PDF/JSON bytes; the raw PDF extraction and
  independent event parser establish those phase claims instead.
- The parent task additionally ran `cargo xtask verify-evidence --all` on the
  exact final candidate: **3248 Documents rows across 63 evidence files,
  1002 distinct digests**, all resolved to bytes held in the evidence store.
  This reviewer inspected the successful result in `evidence-all.log`.

Two meaningful mutations were then executed in this detached worktree:

1. NSE pre-open order-entry close moved from 14:13 to 14:12 IST. Its public
   phase-boundary test failed at 14:12:59 (expected order entry, got closed).
2. Xetra post-trading close moved from 15:00 to 14:59 CET. Its public
   phase-boundary test failed at 14:59:59 (expected order entry, got closed).

Both mutant runs exited 100 because the named public test asserted the wrong
observable state; neither failure was a compile error. Each original file was
restored byte-for-byte in a `finally` block, then its targeted test passed.
`mutation-results.json` retains original hashes and exit statuses. The US
source review independently detected and restored a CME queue-boundary mutation
and an ICE post-close-queue mutation as described in its report.

The review worktree is clean at
`72dff410dbab364ba9ab90c934af4abd7de8d7c4` after restoration. No external
review was posted by this reviewer; the parent task owns the consolidated PR
review and evidence dependency publication.

The final whole-store `cargo xtask verify-evidence --all` check also passed:
**3,248 Documents rows across 63 evidence files and 1,002 distinct digests**
resolve to captured bytes. `evidence-all.log` records the exact result.
