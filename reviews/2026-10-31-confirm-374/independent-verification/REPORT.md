# Independent verification — issue #374

**PASS** for crate commit `6078da48c15a2dc602961a7ea0759ef0cfcaa17c`.

Base: `d3f6b21db8f4f7523f0c79b786c16c6852c4678c`. Detached worktree: `/workspace/exchange-hours-review-374`.

The diff contains exactly eleven Markdown files: ten evidence records and the schedule source registry. Git object equality confirms that the complete `src` and `tests` trees, Cargo manifest and lockfile, pinned toolchain, and workflow tree are unchanged. No runtime data, test, dependency, or workflow changes were introduced.

The exact head was verified from 2026-10-31T23:26:11.456223+00:00 through 2026-10-31T23:37:08.154259+00:00; total wall time 656.698 seconds. The worktree was clean and still at that head after the final gate.

## Required gates

| Gate | Result | Seconds | Log |
|---|---|---|---|
| fmt | PASS | 0.722 | [fmt.log](fmt.log) |
| clippy | PASS | 0.099 | [clippy.log](clippy.log) |
| nextest | PASS | 618.322 | [nextest.log](nextest.log) |
| doctests | PASS | 0.789 | [doctests.log](doctests.log) |
| strict-docs | PASS | 3.772 | [strict-docs.log](strict-docs.log) |
| deny | PASS | 2.127 | [deny.log](deny.log) |
| markdownlint | PASS | 4.679 | [markdownlint.log](markdownlint.log) |
| msrv | PASS | 10.847 | [msrv.log](msrv.log) |
| verify-evidence | PASS | 15.321 | [verify-evidence.log](verify-evidence.log) |

- Nextest: **1,407 passed, zero skipped**. The exhaustive holiday-table coverage test took 586.372 seconds; it completed successfully.
- Doctests: **3 passed**, none ignored or filtered out.
- Markdownlint: pinned **0.23.3**, **175 files**, zero issues.
- Evidence byte verification: **3,248 Documents rows**, **63 evidence files**, **1,002 distinct digests**; all reproduced from the evidence store.
- MSRV: `cargo +1.95 check --all-targets` passed.

## Reproduction and scope

All commands, exit codes, UTC timestamps, durations and log SHA-256 digests are recorded in [summary.json](summary.json). The diff and exact changed-file list are retained as [review.diff](review.diff) and [changed-files.txt](changed-files.txt).

The review uses its own target directory, `/workspace/exchange-hours-review-374/target`; it was created fresh for this detached worktree. The superseded first documentation head used the same worktree cache before being stopped at the parent’s request. No crate or xtask executable from another workspace was reused, so embedded manifest paths resolve the reviewed checkout. The superseded run is archived separately and is not a verification result for this head.

No mutation or additional tests were introduced because this follow-up changes confirmation prose only and all runtime/test objects equal the base. Independent source/prose reproduction is recorded separately in [the source review](../independent-source-review/REPORT.md). This report records the mechanical verification gates.

## Tool versions

- rustc: `rustc 1.99.1 (58cf8f9c3 2026-10-13)`.
- cargo: `cargo 1.99.1 (5f94df478 2026-08-27)`.
- msrv_rustc: `rustc 1.95.0 (59807616e 2026-04-14)`.
- nextest: `cargo-nextest 0.9.150 (d225b1daf 2026-10-26)`.
- deny: `cargo-deny 0.20.2`.
- node: `v24.19.0`.
