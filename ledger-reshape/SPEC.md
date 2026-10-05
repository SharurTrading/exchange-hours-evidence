# Ledger reshape — design spec

Written 2026-09-12 (UTC). Design only; no file in
`/Users/agedvagabond/Developer/exchange-hours-rs` is edited by this document.

Governing laws: LAW-EVIDENCE-FILES, LAW-SERVICE-TIERS, LAW-WATCH,
LAW-PRIMARY-SOURCES, LAW-UTC-DATES, and the modeling convention *Carry the
earliest sourced state back to the floor*.

Measured baseline, read on 2026-09-12 from
`docs/schedules/verification.md`:

| Surface | Rows | Primary | Partial (executable) | Partial (order-entry) | Synthetic |
|---|---:|---:|---:|---:|---:|
| `Exchange` | 96 | 67 | 3 | 25 | 1 |
| `MarketHoursKey` | 36 | 6 | 19 | 10 | 1 |
| **Total** | **132** | 73 | 22 | 35 | 2 |

132 ledger rows, 76 distinct owner modules, 56 source-set anchors.

---

## 1. The new row shape

### 1.1 Header and separator (exact text)

```
| Identity | Owner | Source sets | Basis | Evidence tier | Service | Horizon | Reviewed on | Cadence | Basis note | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
```

Eleven columns. Both the `## Exchanges` table and the
``## `MarketHoursKey` profiles`` table use this identical header and separator.

### 1.2 Why this column order (fence-driven)

The requested order is adopted unchanged, and it is the right one for a
mechanical reason worth recording: cells `0..=3` keep the indices they have
today.

| Index | Column | Today | Fence that reads the index |
|---:|---|---|---|
| 0 | Identity | index 0 | `wire_name`, every ordering fence |
| 1 | Owner | index 1 | `every_exchange_owner_link_resolves`, `every_market_hours_key_owner_and_source_link_resolves` |
| 2 | Source sets | index 2 | `assert_source_links_resolve`, `cme_source_set_prose_counts_match_the_ledger` |
| 3 | Basis | index 3 | every `basis_count` closure in `mod.rs`; `databento.rs` `row_cells(ledger_row)[3]` |
| 4 | Evidence tier | new | new |
| 5 | Service | new | new |
| 6 | Horizon | new | new |
| 7 | Reviewed on | index 4 | `exchange_rows_have_complete_review_metadata`, `readme_and_review_dates_match_the_repository_cutoff` |
| 8 | Cadence | new | new |
| 9 | Basis note | index 5 (Notes) | nothing reads it by index today; `the_gap_kind_split_…` reads `"Gap: …"` out of it by whole-file substring |
| 10 | Evidence | new | new |

Only two existing index reads move (`Reviewed on` 4 → 7; the Notes cell 5 → 9),
and `databento.rs` and `trade_type_keys.rs` need no index edit at all. Do not
reorder these columns to "improve" the reading order; the cost is a
cross-file fence sweep for nothing.

### 1.3 Cell grammar

**`Identity`** — the canonical `snake_case` wire name in backticks, exactly as
today: ``| `globex_cryptocurrency` |``. One row per `Exchange::ALL` entry in
`Exchange::ALL` order, then one row per `MarketHoursKey::ALL` entry in
`MarketHoursKey::ALL` order. Unchanged.

**`Owner`** — **one or more** Markdown links to the production modules that
carry this identity's rule data *and* its timeline, `<br>`-separated, each
written `[<basename>](../../src/<path>)`. This is a change: the cell is
single-link today, and for 23 identities the timeline lives in a sibling the
cell does not name — `nasdaq`, `nasdaq_bx`, `nasdaq_psx`, `memx_eq` and
`miax_pearl_eq` keep their profiles in `equities/us/equities.rs` and their
`revisions!` blocks in `equities/us/history.rs`, and all 18 US options rows
keep theirs in `equities/us/options.rs` and `equities/us/options/history.rs`.
Both files must be named, timeline module last:

```
[equities.rs](../../src/calendar/schedules/equities/us/equities.rs)<br>[history.rs](../../src/calendar/schedules/equities/us/history.rs)
```

**`Source sets`** — unchanged: one or more `[ID](sources.md#anchor)` links,
`<br>`-separated. Fourteen rows carry two today (the `EU-FESE-SECONDARY`
companions); that stays legal.

**`Basis`** — exactly one of four literals, no markup, no trailing prose:

| Value | Meaning |
|---|---|
| `Primary` | current boundaries sourced at T1 or T2, no known modeled-history gap since January 2010 or since the sourced launch |
| `Partial / executable` | a named gap that touches a window in which a trade can print (`regular`/`extended`) |
| `Partial / order-entry` | a named gap confined to an `order_entry` or post-close window in which no trade can print |
| `Synthetic` | deterministic library policy, not a venue schedule (`unknown`, `always_open` only) |

The gap kind moves **out of the note and into the Basis cell**. The
`**Gap: executable** — …` / `**Gap: order-entry** — …` prefix that opens 57
notes today is deleted from the prose; nothing may restate it in the note.
`Secondary`, `Pragmatic` and `Known issue` are **retired**: no row uses them,
and the vocabulary becomes closed at four values. Keep a one-paragraph
"Retired basis labels" note in the ledger's `## Basis` prose so an old citation
still resolves, and say that a row that would need one of them is a defect to
fix, not a label to restore.

**`Evidence tier`** — `T1`, `T2`, `T3`, `T4`, or `—` for a `Synthetic` row.
Per LAW-PRIMARY-SOURCES this is the tier of the evidence behind the identity's
**current** schedule, not the worst tier anywhere in its history; a lower-tier
corroboration inside a carried interval is a residual risk in the evidence
file, not a downgrade here. A non-synthetic row must be `T1` or `T2` — a
current schedule at T3 or T4 is a defect, and the fence says so. Assign `T2`
only where the current grid rests on the operator's own machine channel
(a session-schedule feed, a reference-data API read as bytes and saved);
everything sourced from a rulebook, hours page, circular, notice, product
change log or specification PDF is `T1`.

**`Service`** — `served` or `dormant`, lowercase, no markup. Derived from
LAW-SERVICE-TIERS against the census in
`exchange-hours-research/architecture-review/B-sharur-consumption.md` §2:

- **served keys (8)** — the keys SharurPlatform's family map
  (`crates/domain/src/globex_products.rs`) can produce: `globex_equity_index`,
  `globex_energy`, `globex_grains`, `globex_fx`, `globex_interest_rates`,
  `globex_livestock`, `globex_cryptocurrency`, `globex_nikkei_225_dollar`.
- **served exchanges (8)** — the venue namespaces the Rithmic adapter admits:
  `cbot` (CBOT), `coinbase_derivatives` (CDE), `cfe` (CFE), `cme` (CME),
  `comex` (COMEX), `eurex` (EUREX), `iceus` (NYBOT), `nymex` (NYMEX).
- **everything else (116) is `dormant`**, including both synthetic rows and
  including the `MarketHoursKey` rows named `eurex` and `sgx`: a venue
  namespace reaches an `Exchange`, never a key.

**`Horizon`** — the venue-local date below which this identity's rows are
carried rather than sourced, `YYYY-MM-DD`, or `—`. Three cases, in order:

1. The timeline's earliest revision row is a sourced launch closure — the
   baseline profile is the pre-launch `CLOSED` state and the first row is the
   operator-dated launch day → **`—`**. Nothing is carried.
2. The baseline grid is itself sourced at or through the January-2010 floor →
   **`2010-01-01`**. Nothing above the floor is carried; nothing below the
   floor is reviewed at all (AGENTS.md, *Below the January-2010 floor*).
3. The baseline grid is carried backwards from the earliest instant at which it
   is sourced, day `D` → **`D`**. This is the common case for an identity whose
   oldest admissible artifact post-dates the floor.

Read case 3's `D` off two things together: the earliest `revisions!` tuple in
the owner's timeline, and the sentence in the current note that says what the
baseline rests on. Where the note says the baseline is a *sourced intersection*
across an undated changeover, `D` is the date of the earliest artifact in that
intersection, not the changeover bracket's lower bound. A `Synthetic` row is
always `—`.

**`Reviewed on`** — the UTC date of the last full source-set review,
`YYYY-MM-DD` (LAW-UTC-DATES), or `—` for a `Synthetic` row. Values are carried
over from today's ledger unchanged; **the reshape advances no review date**, and
the repository cutoff stays `2026-08-22`.

**`Cadence`** — `monthly`, `quarterly` or `on demand`, lowercase. Mechanical
under LAW-WATCH:

- `dormant` → always `on demand`.
- `served` **and** (a revision row effective within the last year of the
  reviewed-on date **or** a 24/7 grid) → `monthly`.
- other `served` → `quarterly`.

Applied to the sixteen served identities as of 2026-09-12:

| Cadence | Identities |
|---|---|
| `monthly` | `cme`, `comex`, `nymex`, `coinbase_derivatives`, `globex_equity_index`, `globex_energy`, `globex_fx`, `globex_interest_rates`, `globex_cryptocurrency` |
| `quarterly` | `cbot`, `cfe`, `eurex`, `iceus`, `globex_grains`, `globex_livestock`, `globex_nikkei_225_dollar` |

(`cme_group.rs`, `energy_metals.rs`, `fx.rs` and `interest_rates.rs` all carry a
2026-08-22 revision row; `cryptocurrency.rs` carries 2026-09-19 *and* a 24/7
grid; `coinbase_derivatives.rs` carries 2026-09-11. `grains.rs` last moved
2015-07-05, `livestock.rs` 2020-05-31, `cme_nikkei.rs` 2015-09-20, `cfe.rs`
2021-12-06, `ice_us.rs` 2017-11-08, and `europe.rs` has no timeline at all.)

**`Basis note`** — at most **three sentences**, plain prose, **never** a `|`
character, no `<br>`, no Markdown table, no bold `Gap:` prefix, no
`**Systems in scope (…)**` clause. Sentence one says what the identity is and
what its current grid is. Sentence two says what the dated history rests on, or
what is undated. Sentence three, if present, says the one thing a reader must
know before relying on the row (a forward-dated row, an intersection, a
withheld window). Everything else — quotations, URLs, retrieval dates,
conflicts, interpretive steps, system-coverage enumerations, the
`Systems in scope` clauses, the discrepancy routings — moves verbatim to the
evidence file.

**`Evidence`** — exactly `[evidence](../evidence/<owner>.md)`, no other text in
the cell.

`<owner>` is the identity's wire name. Two wire names are carried by both an
`Exchange` row and a `MarketHoursKey` row — `eurex` and `sgx` — so the rule is
**mechanical, not a hand-kept exception list**: the file is `<wire>.md` for an
`Exchange` row, and for a `MarketHoursKey` row it is `<wire>.md` unless an
`Exchange` row carries the same wire name, in which case it is `<wire>_key.md`.
Today that yields exactly `docs/evidence/eurex_key.md` and
`docs/evidence/sgx_key.md`; no `Exchange` wire name ends in `_key`, so the
suffix can never collide. The fence derives the expected filename from the two
row sets, so a future collision is handled without an edit.

### 1.4 One file per identity, including shared modules

**Rule: one evidence file per ledger row, always — 132 rows, 132 files, a
bijection.** Twenty-one modules are shared by more than one row (`options.rs`
by 18, `nyse.rs` and `equities.rs` by 5 each, `euronext.rs` by 5,
`sgx_equity_index.rs` by 3, `metals_tas.rs` by 3, and so on), and a shared
module's narrative is written **once**.

The one copy lives in the **anchor identity's** file: the first of the sharing
identities in ledger order (`Exchange::ALL` before `MarketHoursKey::ALL`). For
`sgx_equity_index.rs` the anchor is `sgx_equity_index_japan`; for
`sgx_equity_index_more.rs` it is `sgx_equity_index_taiwan`; for `cme_group.rs`
it is `cme`; for `europe.rs` it is `eurex` (the exchange); for
`futures/international/sgx.rs` it is `sgx` (the exchange).

Every non-anchor sharer's file is still complete for its own row: it carries
its own `## Ledger basis`, its own `## Revision rows` (its own timeline's days
only), its own `## Sources` and `## Gaps and residual risks`, and in place of a
`## Module narrative` section it carries a one-line cross-reference block:

```
> Shared module. The narrative for
> [`sgx_equity_index.rs`](../../src/calendar/schedules/futures/international/sgx_equity_index.rs)
> lives in [`sgx_equity_index_japan`](sgx_equity_index_japan.md#module-narrative-moved-from-srccalendarschedulesfuturesinternationalsgx_equity_indexrs-on-2026-09-12-utc).
> Sibling identities: [`sgx_equity_index_china`](sgx_equity_index_china.md),
> [`sgx_equity_index_singapore`](sgx_equity_index_singapore.md).
```

This is a deliberate choice against duplicating the shared narrative into each
sharer's file. Eighteen copies of the US options narrative would drift the
first time one of them is corrected, and no fence can detect prose drift
between copies. One authoritative copy plus a link cannot drift.

---

## 2. Two worked rows, rewritten from today's ledger

### 2.1 A served key — `globex_cryptocurrency`

Today (one cell, ten sentences, `Reviewed on` at index 4):

> `| `globex_cryptocurrency` | [cryptocurrency.rs](…) | [US-CME-GROUP](sources.md#us-cme-group) | Partial | 2026-09-06 | **Gap: order-entry** — the trading session is sourced; what is undated is a queue or post-close phase in which no trade can print. CME non-spot-quoted cryptocurrency futures. The exact current 24/7 phases, 2026-05-29 transition, multi-day bounds, weekly close, and following-open-business-day convention are retained, as are the three one-day Saturday maintenance extensions CME's Globex notices state for this family's channels 326/327 — 2026-08-01 to 09:00 CT (notice 20260727), 2026-08-29 to 06:00 and 2026-09-19 to 08:00 CT (notice 20260824, restated by 20260831) — each without a replacement Pre-Open and each reverting to the 02:00–04:00 standard window; the September row is forward-dated on the operator's statement, and the two later rows were added on 2026-09-06 (#61). The 2017–2026 matching grid is exact, but primary evidence does not date the five-day era's Sunday/weekday Pre-Open onset, so dated history omits those queues. The 2026-08-31 review confirmed this at the source: … Later member-product listings remain catalog data. |`

Reshaped:

```
| `globex_cryptocurrency` | [cryptocurrency.rs](../../src/calendar/schedules/futures/us/cryptocurrency.rs) | [US-CME-GROUP](sources.md#us-cme-group) | Partial / order-entry | T1 | served | — | 2026-09-06 | monthly | CME non-spot-quoted cryptocurrency futures, on the 24/7 Globex grid CME filing 26-114 introduced for trade date 2026-05-30. The 2017-12-17 launch grid, the 2026-05-29 transition day and the three one-day Saturday extensions are exact, and the 2026-09-19 row is forward-dated on CME Globex notice 20260824. Primary evidence does not date the five-day era's Sunday and weekday Pre-Open onset, so dated history omits those queues. | [evidence](../evidence/globex_cryptocurrency.md) |
```

How each new cell was derived:

- **Basis** — the old note's `**Gap: order-entry**` prefix, moved into the cell
  and the prefix deleted from the prose.
- **Evidence tier** — `T1`. The citations are CME's own SER notice, its own
  rule filing 26-114, and its own Globex advisories; none is a machine channel,
  so not `T2`.
- **Service** — `served`: `GlobexCryptocurrency` carries 21 roots in
  SharurPlatform's family map, the largest of the eight.
- **Horizon** — `—`, by case 1. `REVISIONS` in `cryptocurrency.rs` opens at
  `(2017, 12, 17, &FIVE_DAY, "CME SER-8051R")` over a `CLOSED` baseline, and the
  launch is operator-dated ("Effective Sunday 17 December 2017 for trade date
  Monday 18 December 2017"). Nothing is carried, so no date is owed.
- **Cadence** — `monthly`, on both triggers: a 2026-09-19 revision row inside
  the last year, and a 24/7 grid.
- **Basis note** — three sentences. The Saturday-extension enumeration (dates,
  notice numbers, CT reopen times, channels 326/327, the missing replacement
  Pre-Open), the 2026-08-31 capture analysis, the #61 provenance and the
  member-product-listing sentence all move to
  `docs/evidence/globex_cryptocurrency.md`; sentence two keeps only the claim
  and points at the file.

### 2.2 A dormant exchange — `tse`

Today:

> `| `tse` | [tse.rs](…) | [APAC-JPX](sources.md#apac-jpx) | Primary | 2026-08-24 | TSE venue union across arrowhead and ToSTNeT is 08:00–18:00 today. Primary pre-scope evidence establishes the 08:00 tail at the January-2010 floor (Working Paper No.3) and through the post-2011 era (the November 2020 Investigation Report states order acceptance began as normal at 08:00); the 2011 phase change and exact 2024-11-05 ToSTNeT close extension are date-aware. |`

Reshaped:

```
| `tse` | [tse.rs](../../src/calendar/schedules/equities/apac/tse.rs) | [APAC-JPX](sources.md#apac-jpx) | Primary | T1 | dormant | 2010-01-01 | 2026-08-24 | on demand | The TSE venue union across arrowhead and ToSTNeT is 08:00–18:00 today, with the 08:00–08:20 lead classified order-entry because nothing can print in it. JPX's own Working Paper No.3 fixes the 08:00 acceptance edge at the January-2010 floor and its November 2020 Investigation Report carries it through the post-2011 era. The 2011-11-21 arrowhead extension and the 2024-11-05 ToSTNeT close extension are both date-aware. | [evidence](../evidence/tse.md) |
```

- **Evidence tier** — `T1`: JPX's own trading-hours pages, its own transition
  table, its own working paper and its own investigation report.
- **Service** — `dormant`: no SharurPlatform adapter admits a TSE namespace and
  no root maps to it.
- **Horizon** — `2010-01-01`, by case 2. `REVISIONS` in `tse.rs` is
  `[2011-11-21, 2024-11-05]` over a `TSE_PROFILE` baseline, and the module
  comment records that JPX Working Paper No.3 analyses the operator's own FLEX
  order-book data **from 2010-01-04** and that the 2010 shareholder report puts
  the 17:30 ToSTNeT extension in November 2009, before the floor. The baseline
  is therefore sourced through the floor, not carried down to it — so the
  horizon is the floor itself, not `—` (nothing launched) and not `2011-11-21`
  (the baseline below that row is sourced, not carried).
- **Cadence** — `on demand`, mechanically from `dormant`.
- **Basis note** — three sentences; the Working Paper and Investigation Report
  quotations, URLs and the arrowhead/ToSTNeT eligibility caveat move to
  `docs/evidence/tse.md`, which also receives the module's four comment blocks
  as `## Module narrative`.

---

## 3. `docs/evidence/<owner>.md` — the template

One file per ledger row. Headings are **exact**; the fences split on them.

````markdown
<!-- SPDX-License-Identifier: MIT-0 -->

# `globex_cryptocurrency` — evidence

- **Kind:** `MarketHoursKey`
- **Owner module:** [`cryptocurrency.rs`](../../src/calendar/schedules/futures/us/cryptocurrency.rs)
- **Source sets:** [`US-CME-GROUP`](../schedules/sources.md#us-cme-group)
- **Ledger row:** [verification.md](../schedules/verification.md)

## Ledger basis (moved from docs/schedules/verification.md on 2026-09-12 UTC)

<the former Notes cell, verbatim, including its `**Gap: order-entry** — …`
prefix and its `**Systems in scope (…)**` clause where it had one. Verbatim
means verbatim: this section is the audit trail for the distillation, so it is
copied without rewrapping words, not summarised. Where the cell used `<br>`
for a line break, expand it to a real newline; change nothing else.>

## Revision rows

One line per `revisions!` tuple in this identity's timeline, in timeline order:

- 2017-12-17 — T1 — CME SER-8051R — five-day launch grid, 17:00–16:00 CT.
- 2026-05-29 — T1 — CME filing 26-114 — one-day bridge into the 24/7 grid.
- 2026-05-30 — T1 — CME filing 26-114 — permanent 24/7 normal week.
- 2026-08-01 — T1 — CME Globex notice 20260727 — Saturday reopen 09:00 CT.
- 2026-08-02 — T1 — CME Globex notice 20260727 — revert to the standard window.
- 2026-08-29 — T1 — CME Globex notice 20260824 — Saturday reopen 06:00 CT.
- 2026-08-30 — T1 — CME Globex notice 20260824 — revert to the standard window.
- 2026-09-19 — T1 — CME Globex notice 20260824 — Saturday reopen 08:00 CT.
- 2026-09-20 — T1 — CME Globex notice 20260824 — revert to the standard window.

## Sources

- <https://www.cmegroup.com/notices/ser/2017/12/SER-8051R.html> — CME SER-8051R, bitcoin futures launch — retrieved 2026-08-31.
- <https://www.cmegroup.com/content/dam/cmegroup/market-regulation/rule-filings/2026/5/26-114.pdf> — CME rule filing 26-114, 24/7 cryptocurrency trading — retrieved 2026-05-25.
- …one bullet per URL the module cites, plus any URL the moved narrative cites.

## Gaps and residual risks

- **order-entry** — the five-day era's Sunday and weekday Pre-Open onset is
  undated; the 2017-12-14, 2017-12-22 and 2018-01-04 contract-specification
  captures publish the matching grid only. Closing condition: a CME artifact
  that states the Pre-Open in session language on a day-level effective date.
  Served identity, so tracked as an issue (LAW-FOLLOW-UPS-ARE-ISSUES).

## Module narrative (moved from src/calendar/schedules/futures/us/cryptocurrency.rs on 2026-09-12 UTC)

<the module's prose comment blocks, verbatim, with the `// ` markers stripped
and the URLs kept. Present only for a module whose narrative is moved in this
change; absent otherwise. A non-anchor sharer of a shared module carries the
cross-reference block from §1.4 here instead.>
````

Notes on the template:

- **Revision-row line grammar** is fixed so it parses:
  `- YYYY-MM-DD — T<n> — <document id> — <label>`, separator `" — "` (space,
  em dash, space), `splitn(4, " — ")`, so the label may itself contain em
  dashes. The document id is the `revisions!` citation literal verbatim.
- The tier on a revision line is that row's own evidence tier, which may differ
  from the identity's current-schedule tier in the ledger.
- An identity with **no** timeline (`europe.rs`, `bme.rs`, and the other single
  static profiles) writes exactly
  `None. <module> holds a single static profile with no dated revision row.`
  under `## Revision rows`. The fence accepts that sentence and nothing else in
  place of bullets.
- The two synthetic rows get files too (`unknown.md`, `always_open.md`), so the
  bijection in §4 holds; theirs say the profile is library policy, carry no
  revision rows, and list no sources.

---

## 4. Fence changes, file by file

### 4.1 `tests/schedule_documentation/mod.rs` — edits

| Item | Change |
|---|---|
| `const VALID_BASES: [&str; 6]` | → `const VALID_BASES: [&str; 4] = ["Primary", "Partial / executable", "Partial / order-entry", "Synthetic"]` |
| *(new)* `VALID_EVIDENCE_TIERS` | `["T1", "T2", "T3", "T4"]` |
| *(new)* `VALID_SERVICE_TIERS` | `["served", "dormant"]` |
| *(new)* `VALID_CADENCES` | `["monthly", "quarterly", "on demand"]` |
| *(new)* `const LEDGER_CELLS: usize = 11;` | replaces every literal `6` in a `cells.len()` assertion |
| `fn owner_target(owner: &str) -> &str` | → `fn owner_targets(owner: &str) -> Vec<&str>`: split the cell on `<br>`, take each link's destination, assert at least one. Callers assert every target resolves. |
| `fn repository_cutoff` | unchanged |
| `fn exchange_rows` / `market_hours_key_rows` / `row_cells` / `wire_name` | unchanged (the new header row does not start with ``| ` ``) |
| `validated_source_link_count` / `assert_source_links_resolve` | unchanged |
| *(new)* `fn basis_of(row) -> &str` | `row_cells(row)[3]` |
| *(new)* `fn is_partial(row) -> bool` | `basis_of(row).starts_with("Partial")` |
| *(new)* `fn evidence_target(row) -> &str` | parses cell 10, asserts the exact `[evidence](../evidence/<name>.md)` form, returns `<name>.md` |

| Test | Change |
|---|---|
| `verification_ledger_has_every_exchange_once_and_in_order` | unchanged |
| `verification_ledger_has_every_market_hours_key_once_and_in_order` | unchanged |
| `market_hours_key_selection_contract_is_explicit` | unchanged |
| `exchange_rows_have_complete_review_metadata` | `cells.len()` `6` → `LEDGER_CELLS`; `reviewed` `cells[4]` → `cells[7]`; add: `cells[4]` in `VALID_EVIDENCE_TIERS` (or `—` iff `Synthetic`), `cells[5]` in `VALID_SERVICE_TIERS`, `cells[6]` is `—` or an ISO date, `cells[8]` in `VALID_CADENCES`, `cells[9]` contains no `\|` and at most three sentence terminators, `cells[10]` parses as an evidence link. `unknown` arm: also assert `dormant`, `on demand`, `—` horizon, `—` tier. Non-synthetic arm: assert tier is `T1` or `T2`. |
| `market_hours_key_rows_have_complete_review_metadata` | identical edits, `always_open` arm |
| `every_market_hours_key_owner_and_source_link_resolves` | `cells.len()` → `LEDGER_CELLS`; `owner_target` → `owner_targets`, loop and assert each resolves |
| `every_exchange_owner_link_resolves` | `owner_target` → `owner_targets`, loop |
| `readme_and_review_dates_match_the_repository_cutoff` | `cells.len()` → `LEDGER_CELLS`; `cells[4]` → `cells[7]` (two sites) |
| `readme_test_inventory_counts_match_the_ledger` | unchanged |
| `readme_and_audit_quantify_assurance_from_the_ledger` | `basis_count(rows, "Partial")` → `rows.iter().filter(|r| is_partial(r)).count()`; delete `secondary`, `pragmatic`, `known_issues` and the `history_gap_rows` sum that used them (`history_gap_rows` becomes `partial`); rewrite the two distribution-table format strings to four basis columns |
| `assert_key_basis_prose_matches_the_ledger` | `key_partial` counts both Partial labels |
| `the_gap_kind_split_is_quoted_consistently_everywhere` | **stop reading `VERIFICATION.matches("Gap: …")`.** Count from the Basis cell over exchange+key rows: `order_entry = rows.filter(basis == "Partial / order-entry").count()`, `executable = rows.filter(basis == "Partial / executable").count()`. Every asserted claim string is unchanged, so README, ledger-summary and audit prose keep their current wording and current numbers (35/22/57). |
| `assurance_prose_restates_exchange_counts_from_the_ledger` | `basis_count(.., "Partial")` → `is_partial`; claim strings unchanged |
| `every_ledger_source_link_has_a_registry_anchor` | unchanged |
| `conditional_future_revisions_remain_unencoded_pending_confirmation` | unchanged |
| `date_exception_contract_distinguishes_boundaries_coverage_and_finality` | unchanged |
| `number_words` | unchanged |
| *(new module)* | `mod evidence_files;` beside the existing three |

`mod.rs` also gains `const EVIDENCE_DIR` and a helper that lists
`docs/evidence/*.md`; the counts above (35 / 22 / 57 / 67 / 28 / 6 / 29 / 95 /
96 / 35 / 36) are **unchanged by the reshape**, so no README or audit number
moves — only the strings that name the retired basis labels.

### 4.2 `tests/schedule_documentation/databento.rs`

`row_cells(ledger_row)[3]` keeps its index. Two edits:

- `docs/schedules/databento-venues.md`'s fifth column currently holds `Primary`
  or `Partial`; it must now hold the four-value Basis literal, because the test
  asserts `row[4] == row_cells(ledger_row)[3]`. Rewrite that column (50 rows)
  and the file's `Primary` / `Partial` explanatory paragraph.
- `assert!(matches!(row[4], "Primary" | "Partial"))` →
  `assert!(row[4] == "Primary" || row[4].starts_with("Partial / "))`.

### 4.3 `tests/schedule_documentation/trade_type_keys.rs`

- `cme_source_set_prose_counts_match_the_ledger` — index 2 and 3 unchanged;
  `row_cells(row)[3] == "Partial"` → `is_partial(row)`.
- `every_executable_gap_row_is_named_in_the_prose` — replace the
  `line.contains("Gap: executable")` filter with
  `row_cells(line)[3] == "Partial / executable"`. Everything else
  (`EXECUTABLE_COLLECTIVE_NAMES`, `span_between`, `assert_collective_counts`)
  is unchanged, and the enumerated prose in README and the ledger is unchanged.
- `ledger_covers_every_market_hours_key_variant` — unchanged.
- `golden_header_identity_counts_match_the_ledger` — unchanged.

### 4.4 `tests/schedule_documentation/source_registry.rs`

Unchanged. `every_source_set_is_referenced_by_a_ledger_row` matches on the
whole row string, not a cell index.

### 4.5 New file — `tests/schedule_documentation/evidence_files.rs`

**How a revision row is attributed to an evidence file.** Two candidate designs
were considered:

- *Rejected:* parse the owner-link module and map module → identities through
  the owner cell. It breaks twice. (a) 23 identities keep their `revisions!`
  blocks in a sibling the owner cell does not name (`equities/us/history.rs`,
  `equities/us/options/history.rs`), so their days would be invisible. (b) Ten
  modules hold **one** timeline shared by several ledger rows (`cme_group.rs`
  → `cme` + `globex_equity_index`; `energy_metals.rs` → `comex` + `nymex` +
  `globex_energy`; `grains.rs` → `cbot` + `globex_grains`; `cfe.rs`,
  `ice_us.rs`, `sgx.rs`, `europe.rs`) while five hold **several** timelines for
  several rows (`nyse.rs`, `cboe.rs`, `trfs.rs`, `metals_tas.rs`,
  `sgx_equity_index.rs`). The union-of-files weakening that makes (b) pass also
  makes it useless: a day could land in one sharer's file and pass.
  Static-name matching (`NASDAQ_REVISIONS` ↔ `nasdaq`) resolves (b) for the
  per-identity modules and fails flat for the shared-grid ones
  (`CME_REVISIONS` names no key; `ENERGY_METALS_REVISIONS` names no row).
- **Adopted:** the module **declares** its evidence files beside each timeline.
  LAW-EVIDENCE-FILES already requires the module to carry "a link to the
  evidence file", so this adds an obligation the law already states rather than
  a new artifact. Immediately above every `revisions!` block, in the block's own
  comment run, one line:

  ```rust
  // Evidence: docs/evidence/cme.md, docs/evidence/globex_equity_index.md
  static CME_REVISIONS: &[Revision] = revisions![
  ```

  Attribution is then exact, survives the `history.rs` siblings, survives a
  shared grid serving several rows, and survives a rename of the static.

Tests:

1. `every_revisions_block_declares_its_evidence_files` — walk every `.rs` under
   `src/`; for each `revisions![` occurrence, scan upward over the contiguous
   `//`/`static`/attribute lines to the preceding blank line and require exactly
   one `// Evidence:` line; require each named path to exist under
   `docs/evidence/` and to be linked by a ledger row's cell 10.
2. `every_revision_row_day_appears_in_its_evidence_file` — the fence
   LAW-EVIDENCE-FILES names. Parse the block's tuples by brace-matching
   `revisions![ … ]`, stripping whitespace, then regex
   `\((\d{4}),(\d{1,2}),(\d{1,2}),` — this survives rustfmt's per-field
   wrapping, which splits most tuples across five lines. Format each as
   `YYYY-MM-DD` and assert it appears as the first field of a bullet in the
   `## Revision rows` section of **every** file the block declares.
3. `every_evidence_revision_line_exists_in_source` — the converse. Every bullet
   under `## Revision rows` must parse as
   `- YYYY-MM-DD — T<n> — <id> — <label>`, its day must be a day of some block
   that declares this file, and its `<id>` must be the citation literal of a
   tuple on that day. Catches a hand-written line for a row that was deleted.
4. `every_ledger_row_links_an_existing_evidence_file` — for all 132 rows, cell
   10 parses, names the file §1.3's `_key` rule derives, and that file exists.
5. `every_evidence_file_is_linked_by_exactly_one_row` — the converse: the set
   of `docs/evidence/*.md` equals the set of linked filenames, one row each.
   Bijection, so an orphan file and a missing file both fail.
6. `every_evidence_file_has_the_required_sections` — exact headings present in
   order: `# `, `## Ledger basis (moved from docs/schedules/verification.md on `,
   `## Revision rows`, `## Sources`, `## Gaps and residual risks`; SPDX header
   on line 1. `## Module narrative (moved from ` optional.
7. `every_evidence_file_names_its_ledger_row` — the file's `Kind:` line agrees
   with which table the linking row is in, so an `Exchange` narrative cannot be
   filed under a key.
8. `modules_carry_no_narrative` — the migration-completion fence. A module is
   clean when no comment run outside the `//!` header exceeds
   `MAX_COMMENT_RUN = 6` lines. A `const NARRATIVE_DEBT: &[&str]` lists the
   module paths not yet migrated; a listed module is skipped, an unlisted one is
   asserted. Each migration group's PR removes its own modules from the list and
   the reshape is done when the list is empty. A module *not* in the list that
   grows a long comment run fails — which is exactly LAW-EVIDENCE-FILES's "a new
   module never carries one".

### 4.6 Documents that change alongside the fences

- `docs/schedules/verification.md` — new header, 132 rewritten rows, the
  `## Basis` prose rewritten to four values plus a retired-labels paragraph, the
  "The row shape changes in a coming reshape" paragraph deleted (it ships), the
  "Exact historical notices … remain beside the owner code until
  LAW-EVIDENCE-FILES moves that narrative" sentences replaced by a pointer to
  `docs/evidence/`. The `## System-coverage audit (Phase 1)` section stays in
  the ledger — it is a method and a discrepancy register, not a row narrative —
  but every per-row `**Systems in scope (2026-09-02):**` clause moves into the
  row's evidence file.
- `docs/schedules/updating.md` — the basis list (four values), the paragraph
  that says the service tier, evidence tier, horizon and cadence "live in the
  row's basis prose" until the reshape (they now have columns), and the two
  "until LAW-EVIDENCE-FILES moves that narrative" sentences.
- `docs/schedules/sources.md` — the intro sentence "remain beside the profile in
  the linked owner code until LAW-EVIDENCE-FILES moves that narrative to
  `docs/evidence/<owner>.md` in a later change" → points at the evidence files.
- `docs/schedules/databento-venues.md` — the Basis column (§4.2).
- `docs/schedules/audit-2026-08-22.md` — the two distribution-table rows become
  `| Public rows | Primary | Partial / executable | Partial / order-entry | Synthetic |`,
  `| 96 `Exchange` identifiers | 67 | 3 | 25 | 1 |`,
  `| 36 `MarketHoursKey` values | 6 | 19 | 10 | 1 |`. The spelled-out
  Primary/Partial sentences the fences read keep their current wording.
- `README.md` — delete "No row relies on Secondary, Pragmatic, or Known issue
  evidence." and replace it with the four-value vocabulary; add the
  served/dormant sentence if a new fence derives it. Every fenced count is
  unchanged.
- `AGENTS.md` — step 9 of *Adding or revising an identity* gains the evidence
  file and the eleven-column row.
- `CHANGELOG.md` under `[Unreleased]`.

---

## 5. Migration groups

Groups are **disjoint by identity, by owner module, and by evidence-file
anchor**, so two agents never touch the same `.rs`, the same evidence file, or
the same shared narrative. That is why the served exchanges travel with the
served keys they share a module with (`cme`/`globex_equity_index` in
`cme_group.rs`), and why the four dormant keys that share a module with a
served identity (`cfe_vix`, `ice_us`, `eurex`, `sgx`) are not in the dormant-key
group.

Every group's PR: rewrite its rows in `docs/schedules/verification.md`, create
its evidence files, move its module narratives, add the `// Evidence:` lines,
and remove its modules from `NARRATIVE_DEBT`. The shared fence edits of §4.1–4.5
land **first**, in a separate preparatory PR, with all 132 rows rewritten
mechanically (columns added, gap prefix moved) and `NARRATIVE_DEBT` listing all
76 modules; the seven groups then drain the debt in parallel.

**7 groups · 132 identities · 76 owner modules.**

### Group A — served CME families and their venues (12)

Modules: `cme_group.rs`, `energy_metals.rs`, `grains.rs`, `fx.rs`,
`interest_rates.rs`, `livestock.rs`, `cryptocurrency.rs`, `cme_nikkei.rs`.
All eight module narratives named in the task brief are here.

`cme`, `cbot`, `comex`, `nymex`, `globex_equity_index`, `globex_energy`,
`globex_grains`, `globex_fx`, `globex_interest_rates`, `globex_livestock`,
`globex_cryptocurrency`, `globex_nikkei_225_dollar`.

Anchors: `cme` (for `cme_group.rs`, shared with `globex_equity_index`), `cbot`
(`grains.rs`), `comex` (`energy_metals.rs`, shared with `nymex` and
`globex_energy`). `globex_fx`, `globex_interest_rates`, `globex_livestock`,
`globex_cryptocurrency`, `globex_nikkei_225_dollar` each own their module.

### Group B — the other served venues (8)

Modules: `cfe.rs`, `coinbase_derivatives.rs`, `ice_us.rs`, `europe.rs`.

`cfe`, `coinbase_derivatives`, `eurex`, `eex`, `iceus`, `cfe_vix`, `eurex`
(key → `eurex_key.md`), `ice_us`.

Anchors: `cfe` (shared with `cfe_vix`), `eurex` (exchange; `europe.rs` shared
with `eex` and the `eurex` key), `iceus` (shared with `ice_us`).
`coinbase_derivatives` owns its module. `europe.rs` has no `revisions!` block,
so its three files use the "no dated revision row" sentence.

### Group C — dormant keys (24)

Modules: `mini_grains.rs`, `ice_sugar.rs`, `ice_coffee.rs`, `ice_cocoa.rs`,
`ice_cotton.rs`, `ice_fcoj.rs`, `ice_usdx.rs`, `eurex_fixed_income.rs`,
`sgx_equity_index.rs`, `sgx_equity_index_more.rs`, `rough_rice.rs`,
`weather.rs`, `spot_quoted.rs`, `event_contracts.rs`,
`bitcoin_event_contracts.rs`, `metals_tas.rs`, `pgm_tas.rs`,
`futures_profile/profiles.rs`.

`globex_mini_grains`, `ice_us_sugar`, `ice_us_coffee`, `ice_us_cocoa`,
`ice_us_cotton`, `ice_us_orange_juice`, `ice_us_dollar_index`,
`eurex_fixed_income`, `sgx_equity_index_japan`, `sgx_equity_index_china`,
`sgx_equity_index_singapore`, `sgx_equity_index_taiwan`,
`sgx_equity_index_ntr_usd`, `globex_rough_rice`, `globex_weather`,
`globex_spot_quoted`, `globex_event_contracts`, `globex_event_contracts_btc`,
`globex_gold_tas`, `globex_silver_tas`, `globex_copper_tas`,
`globex_platinum_tas`, `globex_palladium_tas`, `always_open`.

Anchors: `sgx_equity_index_japan` (`sgx_equity_index.rs`),
`sgx_equity_index_taiwan` (`sgx_equity_index_more.rs`), `globex_gold_tas`
(`metals_tas.rs`), `globex_platinum_tas` (`pgm_tas.rs`). This group holds 19 of
the ledger's 22 `Partial / executable` rows, so it is the heaviest on evidence
prose even though it is not the largest by count.

### Group D — US cash equities, ATSs, TRFs, and the synthetic fallback (23)

Modules: `futures_profile.rs`, `equities/us/equities.rs`,
`equities/us/history.rs`, `equities/us/cboe.rs`, `equities/us/nyse.rs`,
`equities/us/ats.rs`, `equities/us/independent.rs`, `equities/us/trfs.rs`.
This group owns both halves of the `equities.rs` / `history.rs` split, so it is
the group that introduces the two-link Owner cell.

`unknown`, `nasdaq`, `nasdaq_bx`, `nasdaq_psx`, `cboe_bzx`, `cboe_byx`,
`cboe_edga`, `cboe_edgx`, `nyse`, `nyse_arca`, `nyse_american`,
`nyse_national`, `nyse_texas`, `memx_eq`, `miax_pearl_eq`, `iex`, `ltse`,
`24x`, `txse`, `blue_ocean_ats`, `finra_trf_carteret`, `finra_trf_chicago`,
`finra_trf_nyse`.

Anchors: `nasdaq` (`equities.rs` + `history.rs`, shared with `nasdaq_bx`,
`nasdaq_psx`, `memx_eq`, `miax_pearl_eq`), `cboe_bzx` (`cboe.rs`), `nyse`
(`nyse.rs`), `iex` (`ats.rs`), `ltse` (`independent.rs`),
`finra_trf_carteret` (`trfs.rs`). This group also carries the per-row
`**Systems in scope (2026-09-02):**` clauses for the completed US cash-equity
tranche.

### Group E — US equity options (18)

Modules: `equities/us/options.rs`, `equities/us/options/history.rs`.
One module pair, one anchor, 18 files.

`cboe_options_c1`, `cboe_c2_options`, `cboe_bzx_options`, `cboe_edgx_options`,
`nyse_arca_options`, `nyse_american_options`, `nasdaq_phlx`, `nasdaq_ise`,
`nasdaq_nom`, `nasdaq_mrx`, `nasdaq_gemx`, `nasdaq_bx_options`,
`miax_options`, `miax_emerald_options`, `miax_pearl_options`,
`miax_sapphire_options`, `box_options`, `memx_options`.

Anchor: `cboe_options_c1`; the other 17 files carry the §1.4 cross-reference
block.

### Group F — APAC equities and the non-CME futures venues (27)

Modules: `small_exchange.rs`, `ice_europe.rs`, `ice_endex.rs`,
`ice_abu_dhabi.rs`, `ice_canada.rs`, `futures/international/sgx.rs`, `asx.rs`,
`tmx_australia.rs`, `nzx.rs`, `tse.rs`, `nse.rs`, `bse.rs`, `hkex.rs`,
`equities/apac/sgx.rs`, `bursa.rs`, `set.rs`, `idx.rs`, `pse.rs`, `hose.rs`,
`sse.rs`, `szse.rs`, `krx.rs`, `twse.rs`, `binance.rs`.

`small_exchange`, `iceeu`, `ice_europe_commodities`, `ice_europe_financials`,
`ice_endex`, `ice_abu_dhabi`, `ice_canada`, `sgx`, `sgx` (key →
`sgx_key.md`), `asx`, `tmx_australia`, `nzx`, `tse`, `nse_india`, `bse_india`,
`hkex`, `sgx_securities`, `bursa_malaysia`, `set_thailand`, `idx`, `pse`,
`hose`, `sse`, `szse`, `krx`, `twse`, `binance_futures`.

Anchors: `iceeu` (`ice_europe.rs`, shared with the two ICE Europe segment
rows), `sgx` (exchange; `futures/international/sgx.rs` shared with the `sgx`
key). Note the two distinct `sgx.rs` files: `sgx_securities` is owned by
`equities/apac/sgx.rs` and is its own anchor. `small_exchange` is one of the
three `Partial / executable` exchange rows.

### Group G — Europe, EMEA and Americas equities (20)

Modules: `lse.rs`, `xetra.rs`, `six.rs`, `euronext.rs`, `euronext/dublin.rs`,
`bme.rs`, `nasdaq_nordics.rs`, `vienna.rs`, `bist.rs`, `tsx.rs`, `jse.rs`,
`tadawul.rs`, `b3.rs`, `bmv.rs`.

`lse`, `xetra`, `six`, `euronext_paris`, `euronext_amsterdam`,
`euronext_brussels`, `euronext_lisbon`, `euronext_dublin`, `euronext_milan`,
`bme`, `nasdaq_stockholm`, `nasdaq_helsinki`, `nasdaq_copenhagen`, `vienna`,
`borsa_istanbul`, `tsx`, `jse`, `tadawul`, `b3`, `bmv`.

Anchors: `euronext_paris` (`euronext.rs`, shared with Amsterdam, Brussels,
Lisbon and Milan — Dublin has its own module and is its own anchor),
`nasdaq_stockholm` (`nasdaq_nordics.rs`). Eight of these rows carry the
`EU-FESE-SECONDARY` second source-set link.

### Totals

| Group | Identities | Exchanges | Keys |
|---|---:|---:|---:|
| A — served CME families | 12 | 4 | 8 |
| B — other served venues | 8 | 5 | 3 |
| C — dormant keys | 24 | 0 | 24 |
| D — US cash equities | 23 | 23 | 0 |
| E — US equity options | 18 | 18 | 0 |
| F — APAC + non-CME futures | 27 | 26 | 1 |
| G — Europe/EMEA/Americas | 20 | 20 | 0 |
| **Total** | **132** | **96** | **36** |

Matches the 132 ledger rows exactly (96 `Exchange` + 36 `MarketHoursKey`).
