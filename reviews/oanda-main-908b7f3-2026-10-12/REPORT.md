# Final OANDA main release verification — 2026-10-12 UTC

Release PR328 merged at `908b7f33556e3bf363d92089ba49da87bb37cdd4`. This is a clean exact-main checkout, with whole tree `4e21549f3486d6ac23547df896b35a7a2a977fcf` identical to the independently reviewed release and integration trees. The independent final-main identity review is retained alongside this report. Prior source review partitions remain in evidence PR32; exact release-head full review is retained in PR33. No source or assertion was changed for final verification.

Fresh local final-main verification passed: formatting, strict Clippy, all1367 nextest tests with zero skips, three doctests, rustdoc warnings denied, cargo-deny, MSRV1.95, the current Euronext artifact replay and the complete evidence replay. The latter verifies3075 Documents rows across57 files and893 distinct digests. Local test-profile opt-level1 preserves all assertions; GitHub CI runs its configured profile separately.

Publish dry run, locked package validation and archive inspection passed. The archive identifies the exact main commit and contains486 files, including483 byte-identical tracked files. Cargo.toml normalization and removal of the unpublished xtask workspace package from Cargo.lock are the only tracked-file normalization; generated .cargo_vcs_info.json is expected. Every remaining67 lock package record is unchanged. Required evidence and maintenance documentation is present; raw captures, private code and repository-only tooling are excluded.

Consumer PR347 is merged with green CI and the operator's acceptance of its completed independent review. Its reviewed source passed4320 full-workspace tests,21 existing skips,16 doctests and all quality gates. Its190 pinned public production files match this main tree. The final registry pin remains consumer issue331 after actual publication; no version or checksum has been invented.

The selected scope is verified current operation and sufficiently specified published future arrangements. Historical gaps, including all26 listed arrangements and their timezones, remain in the single public issue332. Native UK OANDA holiday coverage stops at2026-10-30. Unsupported history and unpublished/insufficiently specified dates retain typed errors; this report makes no historical completeness claim. No tag, crates.io upload or GitHub release was created. Owner-authentication preflight reported no token in this environment; the publishing operator must authenticate before publication.

Final GitHub main CI outcome is recorded in STATUS.md and ci-main.json after completion.
