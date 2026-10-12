# Independent review — current OANDA Asia books

Review date: 2026-10-12 UTC. Reviewer: GPT-6 (Codex), independent of the writer.
Exact candidate: `8f2a9830260e4f9c30c4ee322a9baa1a685650f9`.
Base: `acd44a`; final review checkout `/tmp/oanda-independent-asia-final-edge`.
Verdict: PASS for the independent Asia source/behavior partition at this exact
head. The individual branch is superseded by combined release PR #344; its
duplicate full chain was deliberately cancelled and is not claimed as a pass.
No merge or publication was performed by this reviewer.

## Scope and evidence

The two new `MarketHoursKey` values are `oanda_china50_cfd` and
`oanda_singapore30_cfd`. I independently retrieved the UK operator normal-hours
and holiday pages, read the supplied PDF text, compared the captured operator
HTML, and verified the canonical archived 2024-02-21 witness. The frozen public
research checkout is `/tmp/oanda-current-evidence-frozen` at `1c28ebbbf0ba46da75bb85d16ea215aa63e4b37a`.

The China A50 grid is 09:01–16:29 and 17:01–04:44; Singapore 30 is
08:31–17:19 and 17:51–05:14. Both are Monday–Friday opening days in
Asia/Singapore (UTC+08:00), with Friday nights wrapping into Saturday.
No SGX futures queue, expiry, settlement or maintenance boundary is copied.
No separately published regular phase or timed order-entry phase is asserted.
Both executable blocks are extended. The engine's maintenance classification
is separate from operator wording: the 32-minute inter-trade-date gap is
Maintenance by crate policy; the same-trade-date morning gap is Closed.

The current operator holiday list names CN50/SG30 explicitly when those books
change (January 1, 2026 is an example outside the new audit). Its published
October 10–30 changes name CHINAH/HK33 and Swedish share CFDs, not these two
books. Each table therefore has zero exception rows in the bounded
2026-10-10..2026-10-30 holiday trade-date window. No normal holiday classification
is claimed beyond that window or below it. Normal-hour corroboration from
2024-02-21 does not turn that capture into a broker cutover or extend the
holiday audit. Below the first holiday window, sourced normal-session queries
may answer beside the one-flank bridge while holiday classification refuses.
Earlier normal-week history remains carried, with #332 recording its closing
condition. The permanent 2010 support floor is unchanged.

Fresh retrieval digests: normal hours
`4686a54f0836f6cb42a32267a3201b7bfa48d789da8b5e5817b4773bc9fc91bd`;
holiday page `38c6dfc9e1b28f8eb0fce00cc5f30d22841917ecdd290431d160ff21e24f185a`.
The saved 2024 witness digest is
`aab9b3032c1d53e6155009fce6a5156983c2d21a2f0bd768f1860f465b8b6a63`.
Original PDF/HTML and current saved-page hashes are recorded in
`source-hashes.json`; independent count and clock calculations are in
`final-counts.json`. The final digest fence passes: 3066 Documents rows,
52 files, 891 distinct digests, every digest present in the frozen store.

## Behavior and public registration

Public boundary fixtures and separate source-derived probes check opens,
end-exclusive closes, regular/extended/queue distinctions, day/night bounds,
Friday/Saturday wrapping, closing civil trade dates, next Monday opening,
intraday/Daily/Weekly/Monthly candle adapters, wire serde/parse identities,
historical bridge/refusal behavior and future publication refusal.

The last Friday night is deliberately a partial publication boundary. Before
Singapore midnight starting October 31, `is_open` admits the sourced October
30 opening-day block and `session_bounds` returns its full Saturday close.
The same instant's closing trade-date classification and Daily candle query
refuse the uncovered October 31 date. At local midnight and afterwards,
instant queries refuse too, even before that returned close. After the close
and on November 2 all tested instant queries refuse. Monthly candles needing
October 31 refuse. This conservative boundary is disclosed and tested; it is
not complete October 31 operation or a new invented holiday window.

Counts at this exact Asia head: 143 ledger rows = 97 Exchange variants and
46 keys, including two synthetic values; 74 Primary, 36 Partial/order-entry,
31 Partial/executable, two Synthetic. Service split here is 36 served and
107 dormant; activation is a separate independently reviewed change.
54 rows have holiday tables. Independent normal-week arithmetic gives
345300 seconds for China A50 and 363300 for Singapore 30, matching the
registered golden values. Registration lists, routing, ledger rows, source
IDs, evidence digests and counter prose were reviewed together.

## Findings resolved

The first head's claim that these grids were witnessed only from October 10,
2026 was false: the stored February 21, 2024 operator page prints both grids.
The writer corrected chronology, canonical source metadata and bridge
fixtures. A later probe exposed imprecise publication-edge prose; the writer
added explicit midnight/closing-date refusal wording and a public regression.
Neither correction invented a historical effective date or widened the
holiday table. The superseded 6a45 and 89f802 full runs reached 1354 passing
checks and were explicitly interrupted during the long holiday walk after
this final head replaced them; they are not claimed as full passes.

## Exact-head checks

Rust toolchain: rustc 1.97.1 (8bab26f4f 2026-07-14),
cargo 1.97.1 (c980f4866 2026-06-30); MSRV gate uses 1.95.
Individual unmodified chain: `final-edge-verification.log` (deliberately
cancelled after supersession). Fmt and strict all-target Clippy passed;
1355 tests passed with zero skips. The only remaining exhaustive holiday walk
was interrupted at 1326.761 seconds, yielding exit 130. The following doctest,
rustdoc, deny and MSRV commands in that individual chain did not run. The
summary's one SIGINT result is the requested cancellation, not a calendar
failure; this log is not a full verification PASS.
Digest proof: `final-edge-evidence-fence.log` (passed).
Affected clean fixtures and independent probes: `final-restored-and-probes.log`
(passed: four writer tests plus one independent probe fixture).

Meaningful mutation at the exact final head: change China day opening from
09:01 to 09:02. The public boundary fixture fails at the sourced 09:01 open
(`Ok(false)` versus `Ok(true)`); `final-mutation-red.log` preserves that failure.
Restore is exact. The mutation target
`/tmp/oanda-independent-asia-final-mutation-target` is separate from the
clean proof target `/tmp/oanda-independent-asia-final-restored-target` and
unmodified full-chain target `/tmp/oanda-independent-asia-final-edge/target`.
No contaminated mutation output is used as a clean proof (#336 mitigation).
The review and probe worktrees are clean after the temporary probes are saved
as `independent-source-probes.rs` and removed from the checkout.

## Superseding combined verification

Only combined PR #344 is intended to merge. Its exact head is
`071def42ededf8c4b7c375db3a20900c973beaf2`. I verified that
`oanda_asia.rs` and `tests/oanda_asia_current.rs` are byte-identical between
the reviewed Asia head and that combined head. The two evidence files retain
the reviewed source and publication-boundary prose; their changed service
paragraphs belong to my separate activation change, independently reviewed
by root. This report does not self-approve those activation edits.

The separate nonauthor combined reviewer independently accepted the Asian
source/data and integration partition, ran a fresh source parser, meaningful
Asia close mutation/restoration, and completed the exact combined full chain:
1367 tests passed, zero skips, three doctests, fmt, strict all-target Clippy,
warning-denying rustdoc, cargo-deny and Rust 1.95 all-target check. I inspected
that review and its full log at
`/tmp/oanda-combined-integration-review-results/REPORT.md` and
`/tmp/oanda-combined-integration-review-results/quality-071def4.log`.
Its evidence fence covers 3075 Documents rows, 57 files and 893 digests;
publish dry-run and archive verification also passed. These are the other
reviewer's proofs, not a retroactive full PASS for my cancelled Asia run.

Public combined verdict:
https://github.com/SharurTrading/exchange-hours-rs/pull/344#issuecomment-6116332460
The scope partition was separately reviewed at
https://github.com/SharurTrading/exchange-hours-rs/pull/344#issuecomment-6116325995
Historical issue #332 remains open. Supersession closes the duplicate
individual-chain work; exact-head PR #344 CI and normal merge gates remain
the integration owner's responsibility.
