<!-- SPDX-License-Identifier: MIT-0 -->

# PR 1 result — "Fences before the families" (issue #58)

**Branch:** `trade-type-fences` (from `origin/main` @ `687e562`)
**Commit:** `413dbbe` — "Fence the ledger, the handoff and the CME counts before #58's keys"
**PR:** https://github.com/SharurTrading/exchange-hours-rs/pull/78 — **open, not merged**
**Completed:** 2026-09-12 UTC

## Issues opened (all before the docs that cite them)

| # | Title | Covers |
|---|---|---|
| [#73](https://github.com/SharurTrading/exchange-hours-rs/issues/73) | Blocked: the three cryptocurrency BTIC keys (U-15 undated cutover, U-8 N1, FAQ-vs-feed stop conflict) | `globex_cryptocurrency_btic_new_york`, `_london`, `_apac` |
| [#74](https://github.com/SharurTrading/exchange-hours-rs/issues/74) | Blocked: globex_europe_index_btic (DVT/E3T) and globex_ftse_china_50_btic (FTC) — no gate covered them | both keys; E3G route change; FTC's wrong flat-CT page; the zone anchor |
| [#75](https://github.com/SharurTrading/exchange-hours-rs/issues/75) | Blocked: globex_equity_index_btic_plus_taco_plus (ES1/ES2/EQ1) — two conflicting launch days | U-19; Rule 524 not a channel for it |
| [#76](https://github.com/SharurTrading/exchange-hours-rs/issues/76) | CME's unexplained Saturday (05:00, 17:00) CT feed block spans TACO, Nikkei BTIC and crypto BTIC | the cross-family pattern, one issue |
| [#77](https://github.com/SharurTrading/exchange-hours-rs/issues/77) | session_profile and hours_for_market_hours_key docs are already false for seasonal keys | U-8 memo §3.5 items 1–2, plus §3.6's golden blind spot |

Pre-existing and cited rather than re-opened: **#71** (decision D-3), **#72**
(decision D-4). Both were found with `gh issue list --search "Decision D-"`.

## Fences added

All in `tests/schedule_documentation/`, six new test functions, each with a doc
comment naming the artifact it guards and what a red means.

New file `tests/schedule_documentation/trade_type_keys.rs`:

1. **F1** `ledger_covers_every_market_hours_key_variant` — ties
   `EXPECTED_MARKET_HOURS_KEY_NAMES` to `MarketHoursKey::ALL`. The suite did not
   import `MarketHoursKey` at all before this.
2. **F2** `handoff_keys_are_registered_or_rejected` — every `globex_*` name the
   handoff proposes must be a shipped key, a name in `unsupported-families.md`,
   or a scheduled key in the new plan doc. Doc comment states the residual risk
   and that the correct response to a red is to author or reject the key,
   **never to edit the handoff**.
3. **F2b** `rejected_handoff_roots_are_named_in_the_register` — reads the roots
   out of the three rejected handoff rows and requires the register to name each.
4. **F3** `cme_source_set_prose_counts_match_the_ledger` — derives the
   `US-CME-GROUP` Status paragraph's "All fourteen …" and "Thirteen of the
   fourteen are Partial".
5. **F4** `every_executable_gap_row_is_named_in_the_prose` — every
   `Gap: executable` row must be named in the README's and the ledger's
   enumerations, by wire name or by a declared collective phrase whose
   written-out count must match.
6. **F5** `golden_header_identity_counts_match_the_ledger` — derives
   `tests/golden_grids.rs`'s "all 96 exchanges and all 31 keys at once".

In `tests/schedule_documentation/mod.rs`:

7. **F6** capacity fix — both local number-word lists replaced by the module's
   `number_words`. The 25-entry list would have panicked on PR 2; the 20-entry
   list silently produced "Six key rows are **Primary** and 24 are **Partial**".
   The README sentence is now spelled out.

## Plan items skipped or changed, and why

- **F5's first half (README:178 variant arithmetic) — SKIPPED, premise false.**
  The plan says README:178 is unfenced and README:40 is the fenced one. It is
  the reverse: `readme_and_audit_quantify_assurance_from_the_ledger` already
  asserts `"{n} variants—{m} operator-derived product-family keys"` (that *is*
  README:178) and `assert_key_basis_prose_matches_the_ledger` already covers
  README:40. Only the golden header was genuinely unfenced. Stated in the PR.
- **F2 required a third register — DEVIATION, stated in the PR.** The plan's
  literal wording (registered key OR named in `unsupported-families.md`) would
  have been red on the 32 names PRs 2–13 author: the handoff proposes 38 names
  the crate does not ship, of which only 6 are blocked. Filing the 32 under
  "unsupported" would misstate them, so the fence accepts a third register — the
  live plan doc's PR table, which names every one of the 32 with its PR number.
  A name in none of the three is still red.
- **F2's root mirror was scoped.** "Every root the handoff marks `**UNMAPPED**`"
  would sweep in the FX, equity-index, yield, route-drift and join-defect rows,
  which lean on existing keys and are research items, not rejections. The fence
  anchors on the three rejected rows (`TNT`, `TAS`, `AWT`) — handwritten, because
  deciding a row is a rejection is a judgement — and reads the roots from the
  handoff, so a root added to one of those rows goes red.
- **F4 needed a collective-phrase table.** Neither enumeration lists the ICE or
  SGX keys individually and the README writes "CME Nikkei 225 Dollar" rather
  than the wire name, so a bare "wire name must appear" rule was not implementable
  against the current prose. `EXECUTABLE_COLLECTIVE_NAMES` maps a prefix to its
  phrase, dies if a prefix stops matching, and checks any written-out count.
- **Coverage plan item 5** updated (it said "No new keys are authored from it
  yet" with no pointer to a sequence); **item 6** left alone — its status line is
  still true.

## Mutation checks — all red, all green on restore

| # | Mutation | Test |
|---|---|---|
| M1 | dropped `globex_event_contracts_btc` from `EXPECTED_MARKET_HOURS_KEY_NAMES`, left the ledger row | `ledger_covers_every_market_hours_key_variant` |
| M2 | appended a `globex_mutation_check_key` span to the handoff | `handoff_keys_are_registered_or_rejected` |
| M2b | dropped `ZTT` from the Treasury TAS rejection | `rejected_handoff_roots_are_named_in_the_register` |
| M3 | `sources.md` "All fourteen" → "All fifteen" | `cme_source_set_prose_counts_match_the_ledger` |
| M4 | deleted `small_exchange` from the README's executable enumeration | `every_executable_gap_row_is_named_in_the_prose` |
| M5 | golden header "all 31 keys" → "all 32 keys" | `golden_header_identity_counts_match_the_ledger` |
| M6 | README "twenty-four" → "24" (the pre-fix spelling) | `readme_and_audit_quantify_assurance_from_the_ledger` |

One caution recorded for the next session: restoring a mutation with
`git checkout -- <file>` also reverts that file's *intended* edits. Use a `cp`
backup per file instead; it happened once here and was caught by the test count.

## Gates, on the final tree

`cargo fmt --all --check` 0 · `cargo clippy --all-targets -- -D warnings` 0 ·
`cargo nextest run --all-targets` 0 (**544 run, 544 passed**) ·
`cargo test --doc` 0 · `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` 0 ·
`cargo deny check` 0 · `cargo +1.95 check --all-targets` 0.

**Test count: 538 → 544.** No golden regeneration; this PR adds no key and
`tests/golden/normal_week_grids.txt` is untouched.

## Files touched

- new `tests/schedule_documentation/trade_type_keys.rs`
- new `docs/plans/2026-09-12-cme-trade-type-keys.md` (221 lines)
- `tests/schedule_documentation/mod.rs` (module registration + F6)
- `docs/schedules/unsupported-families.md` (three-part structure, 3 rejections, 6 blocked)
- `README.md` (spelled Partial key count)
- `CHANGELOG.md` (three bullets under `[Unreleased]` / **Changed**)
- `docs/plans/2026-09-05-cme-globex-family-coverage.md` (item 5 status)

## Next

PR 2 (metals TAS, 5 keys) is ready and needs no decision. **D-8 is one
retrieval and should run before PR 4 lands** — it either unblocks the crypto
BTIC keys tracked in #73 or forces PR 4's crypto TAS era-2 date to be
re-examined.

---

## Review round — 2026-09-12 UTC

**Commit:** `5bb2896` — "PR 1: review fixes" (second commit on `trade-type-fences`, pushed).
**PR body updated** with a `## Review` section via `gh pr edit --body-file`.

Eight confirmed findings, all applied. No new issues were opened: the one
LAW-FOLLOW-UPS-ARE-ISSUES breach was a *missing citation*, not a missing issue
— #73 already existed and already made D-8's retrieval its first closing
condition.

### Code

1. **`handoff_keys_are_registered_or_rejected` was answering from prose.**
   `UNSUPPORTED_FAMILIES.contains(&quoted)` is an unanchored substring test
   over the whole register, so *any* backticked mention answered a name —
   including `unsupported-families.md:147`, "They must **not** ride
   `globex_bloomberg_commodity_index`". Dropping that name from the plan's PR
   table left the fence green. Replaced with a new helper:

   ```rust
   fn names_in_unsupported_register(quoted: &str) -> bool {
       UNSUPPORTED_FAMILIES.lines().any(|line| {
           if line.starts_with("###") {
               return line.contains(quoted);
           }
           line.starts_with("| ") && row_cells(line).first() == Some(&quoted)
       })
   }
   ```

   Only a first-cell table entry (the ambiguous and blocked tables) or a
   rejection-section heading counts — the register's own stated three parts.
   The six blocked names and `sgx_equity_index` are first-cell rows and keep
   matching; `globex_bloomberg_commodity_index`, `globex_energy` and
   `globex_interest_rates` (prose-only mentions) stop matching.

2. **That fence's doc comment overclaimed — corrected, and PR1-result.md's
   "Doc comment states the residual risk" above is superseded.** The old
   comment said a name could otherwise "be quietly dropped between two PRs and
   nothing says so". It cannot say that: 31 of the 38 unshipped names are
   answered by the work list alone, presence there is textual, and the plan is
   a dated record no PR prunes. The comment now states the guarantee it does
   give — no surveyed name becomes *unanswerable* — and names the deliberate
   drop it catches (PR 12, gated on #72). The stronger guarantee would need a
   fourth term the plan does not supply (a per-key shipped/outstanding marker a
   landing PR flips); that was not added.

### Documentation

| File | Fix |
|---|---|
| plan, PR 4 row + D-8 paragraph | cite [#73] at both points D-8 is named (LAW-FOLLOW-UPS-ARE-ISSUES citation clause) |
| plan, sequence note | "PRs 9, 10 and 13 must cite #76" → "PRs 10 and 13". #76 is scoped to those two; the U16-U17 census finds (05:00, 17:00) CT only on ESQ/3T, NQQ/NT, RTQ/RE, NIT/N6, NKT/ND — PR 9's EST (7968) and ES1 (8689) Saturday rows are empty |
| plan, line 20 + line 11 | "eight gate result files / nine verifier files" → **nine / ten**; opening sentence's "Eight research gates and their nine adversarial verdicts" → **nine / ten** so the two statements agree. Checkable: nine non-verify gate `*.json` matching the nine table rows, ten `*.verify*.json` (the tenth is U-8's preserved pass-1) |
| `CHANGELOG.md`:313 | "Five documentation fences" → "Six" |
| `CHANGELOG.md` commodity-index BTIC | "a filing whose only BTIC window for them is the ClearPort one" → "the one filing that tabulates a BTIC window for them, whose AW row prints a 17:00 CT Globex start". The AW row's Current cell is the Globex 17:00–13:30 CT value, not ClearPort's 17:00–16:00; the contradiction is 17:00 vs a measured 08:15 open |
| `unsupported-families.md` Treasury TAS | both SER-8863 and Globex Notice 2021-10-18 state trade date 2021-11-15 **conditionally**; say so, refer to [#71], and quote the Notice's own "pending completion of all regulatory review periods" where only SER-8863's was disclosed. Verdict unchanged |

**Left alone deliberately:** the module doc comment's "Five artifacts"
(`trade_type_keys.rs`:5) — it counts the five artifacts #55 and #60 each
restated by hand (README, sources.md, unsupported-families.md,
verification.md, golden_grids.rs), not the fences. The first commit's message
still says "Five fences"; rewriting history for that alone was not worth it,
and the CHANGELOG and PR body now say six.

### Mutation checks (fence touched: F2)

| Mutation | Before the fix | After |
|---|---|---|
| drop `globex_bloomberg_commodity_index` from the plan's PR table | **green** (prose answered it) | **red** |
| drop `globex_dairy` from the plan's PR table | red | red |
| drop a blocked key from the plan only | green | green (register table row answers it) |
| drop that blocked key from the plan *and* the register | red | red |

Used `cp` backups per file, per the caution recorded above — no
`git checkout --`.

### Gates, on the final tree

`cargo fmt --all --check` 0 · `cargo clippy --all-targets -- -D warnings` 0 ·
`cargo nextest run --all-targets` 0 (**544 run, 544 passed**) ·
`cargo test --doc` 0 (3 passed) ·
`RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` 0 · `cargo deny check` 0 ·
`cargo +1.95 check --all-targets` 0.

Test count unchanged at 544 — the review added no test, it corrected one.

[#71]: https://github.com/SharurTrading/exchange-hours-rs/issues/71
[#73]: https://github.com/SharurTrading/exchange-hours-rs/issues/73
