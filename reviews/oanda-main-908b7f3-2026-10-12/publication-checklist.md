# OANDA 1.1.0 publication candidate — 2026-10-12 UTC

Candidate: exchange-hours-rs main `908b7f33556e3bf363d92089ba49da87bb37cdd4`, version 1.1.0. This exact tree is `4e21549f3486d6ac23547df896b35a7a2a977fcf`, identical to the independently reviewed release and integration heads. PR328 is merged. Consumer PR347 is merged, with passing CI and the operator's acceptance of its completed independent review.

The selected release scope is current operation and sufficiently specified published future arrangements. Historical gaps remain disclosed in public issue332; no historical completeness claim is made. Native OANDA holiday publication ends2026-10-30. Unknown history and unpublished or insufficiently specified dates retain explicit errors. Consumer issue331 tracks replacing the provisional Git dependency with the actual published registry version after publication.

No v1.1.0 tag, crates.io package or GitHub release has been created. A read-only `cargo owner --list exchange-hours` preflight returned 'no token found'. The publishing operator must authenticate using cargo login or their owner credential; credentials must not be posted in chat or retained in research artifacts.

After exact-main quality CI and the clean-head local release checks pass, follow RELEASING.md on this exact commit: confirm owner/GitHub authentication, create and push annotated v1.1.0, run cargo publish --locked, create the GitHub release from the matching changelog, then verify crates.io and docs.rs. The final published consumer pin must use the actual registry checksum.
