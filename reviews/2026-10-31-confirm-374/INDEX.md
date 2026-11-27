<!-- SPDX-License-Identifier: MIT-0 -->

# Special-session confirmations — 2026-10-31 UTC

This wave completes the publication checks requested by
[exchange-hours-rs issue #374](https://github.com/SharurTrading/exchange-hours-rs/issues/374)
against the schedules merged in PR #375, commit
`d3f6b21db8f4f7523f0c79b786c16c6852c4678c`.

| Scope | Session dates | Original confirm-by date | Fresh primary PDF retrieval, UTC | SHA-256 |
|---|---|---|---|---|
| NSE capital-market Muhurat | 2026-11-08 | 2026-11-07 | 2026-10-31 23:19:09.653909 | `ce94ee1c54d98eccdf3c30fa0673ae2b6a49ea4ed4a72fb83d826f4359f71d58` |
| ICE Futures U.S. exact families | 2026-12-24, 2026-12-28; dependent Cotton 2026-12-29 | 2026-12-23 | 2026-10-31 23:19:44.587592 | `a7658155b57c51085cd3b36abc9ff6b91f3ca353cda88365a06459ebb40f0801` |
| Xetra DAX-share scope | 2026-12-30 | 2026-12-29 | 2026-10-31 23:19:02.444473 | `d3618ef9738a3cae92909d11d4eaf820ab7b71d1e723c1fa04a21062e9738115` |

All three primary PDFs reproduce the merged citations byte for byte. The
checked current operator notice channels contain no superseding timetable for
these sessions. Each report states its bounded channel search and the exact
retrieval times; this is confirmation of the available publications before
their effective days. The runtime schedules and publication horizons are
unchanged.

- [NSE report](nse/REPORT.md): fresh circular, dated circular API response,
  later CMTR and relevant administrative notices, phase derivation and checks.
- [ICE report](ice/REPORT.md): Christmas notice, ordinary-hours and PCPO
  publications, current notices response, family scope and queue comparisons.
- [Xetra report](xetra/REPORT.md): final-session PDF, current calendar,
  circulars 049/2026 and 050/2026, bounded listing/RSS/topic search and phases.
- [Independent source review](independent-source-review/REPORT.md): separate
  primary retrievals and review of the confirmation records.
- [Independent verification](independent-verification/REPORT.md): exact-head
  repository checks and unchanged runtime/test-tree comparison.

Each source subtree retains its URL/UTC/SHA-256 retrieval manifest and
`SHA256SUMS.txt`. Original captures and their historical retrieval metadata
remain preserved in the earlier wave. The crate's source registry and each
affected evidence file record completion of the corresponding #374 check.
