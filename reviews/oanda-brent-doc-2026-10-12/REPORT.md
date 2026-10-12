Posted by an AI agent running as `gpt-6.1-sol` (`Codex`), using the maintainer's GitHub login.

# Independent PR #338 review

Reviewed UTC date: 2026-10-12.
Candidate: `ffe066acbbbbb68394545fc9e635aa934b1a96ad`.
Base: `85ed22bf4157c24a9388449ddc835e48bc8315ad`.
Scope: `CHANGELOG.md` and `docs/evidence/oanda_brent.md` only. No runtime table, public API, coverage interval, holiday classification or test changes.

## Source and scope findings

Fresh retrieval from `https://www.ice.com/products/219/Brent-Crude-Futures` independently reproduced SHA256 `8b9ca9b5ddfbfe482e33f6a5f5055a5e803988a5ca84a01d613e36106c711f0b`, identical to the cited store bytes. The Trading Hours table prints London 01:00–23:00 and New York 20:00–18:00. The Daily Settlement section separately describes a two-minute calculation period beginning at 19:28 London. The corrected prose follows LAW-SESSION-NOT-EXPIRY and LAW-PRIMARY-SOURCES.

The operator's separately captured October 2026 temporary-DST notice prints Brent 00:00–22:00 GMT for the US/UK transition mismatch. The paragraph therefore correctly qualifies the product-page clock instead of asserting a constant London close throughout the year. The ICE statements establish underlying-contract hours and do not certify OANDA's distinct blocks, a historical cutover or any currently withheld OANDA holiday arrangement (LAW-NO-FABRICATED-DATES, LAW-HOLIDAY-SCOPE).

The final canonical Documents header is recognized by the fixed parser. All seven shared OANDA rows are byte-identical to existing canonical rows in `oanda_fx.md` or `oanda_us_index_cfd.md`; adding them resolves native Brent citations locally without weakening a fence. The new observation/retrieval date is the actual UTC date, 2026-10-12 (LAW-EVIDENCE-FILES, LAW-UTC-DATES).

## Validation

PASS on the final exact head: `cargo fmt --all --check`, strict all-target Clippy, all-target nextest (1,352 passed, zero skipped), three doctests, warning-denied rustdoc, `cargo deny check`, and `cargo +1.95 check --all-targets`. The maintainer explicitly authorized `CARGO_PROFILE_TEST_OPT_LEVEL=1`; no production profile changed. The complete successful chain is saved in `quality-final-ffe066a.log`. Cargo-deny emitted only unmatched-license-allowance warnings and accepted advisories, bans, licenses and sources.

The shipped documentation fences passed, including native citation resolution and research-store digest checks. `cargo xtask verify-evidence ICE-BRENT-SPEC-2026-10-12` resolves the exact cited file. In an isolated exact-head checkout, changing only the first SHA256 nibble made that command exit 1 at `oanda_brent.md:163`; restoring the original file made the same command exit 0. Logs: `evidence-sha-mutation-ffe066a.log` and `evidence-sha-restored-ffe066a.log`. Runtime mutation is inapplicable to this documentation-only diff.

`git diff --check` passes and the reviewed checkout is clean. The GitHub PR head was independently checked as the exact candidate above. Earlier d3e/95d gates do not supply this final-head acceptance.

## Verdict

PASS. No actionable findings within the two-file change. The correction distinguishes the underlying trading hours from settlement and keeps OANDA runtime data and all native coverage refusals unchanged.
