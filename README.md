<!-- SPDX-License-Identifier: MIT-0 -->

# exchange-hours-evidence

The public, versioned research store behind the
[`exchange-hours`](https://github.com/SharurTrading/exchange-hours-rs) crate's
evidence chain (LAW-EVIDENCE-FILES in that repository's `AGENTS.md`). Every
session time, every dated change and every holiday the crate encodes cites a
document id; this repository holds the **bytes** those ids resolve to, so any
contributor can re-verify a claim instead of trusting a reviewer's local
store.

The layout is the working store's layout, at the repo root: per-task
directories (`holidays/raw/...`, `cme-globex/...`, `normal-weeks/...`,
`STATUS.md` and the rest). Every citation path in the crate's
`docs/evidence/*.md` files, and every path in a task's `INDEX.md`, resolves
here unchanged. `STATUS.md` is the decision log: it records not just what
entered the record but why each verdict was reached.

## Directory map

- `STATUS.md` — the decision log: verdicts, closures, rejections, and why.
- `holidays/raw/` — the raw holiday-calendar captures, one directory per
  retrieval task. The CME families dominate the top level (`cme-…` eras with
  their `-fix`, `-repair`, `-verify` passes, `cbot-…`, `cde…`, `cfe…`,
  `cme-globex`, `cme-nikkei-…`, plus `eurex…`, `iceus…`,
  `coinbase-derivatives-…`, `hkex`, `nyse-nasdaq`, `six`, `xetra`,
  `review-224-closure-negatives` and the rest). **The cash-equity venues live
  one level down, in `holidays/raw/equities/<venue>/`** — `asx`, `b3`,
  `borsa_istanbul`, `euronext_paris`, `hkex`, `lse`, `nse_india`, `nyse`,
  `nzx`, `sgx_securities`, `six`, `sse`, `tadawul`, `tse`, `tsx`, `xetra` —
  with `INDEX.md` and `SHA256SUMS.txt` beside them. A capture missing from a
  task directory is probably under `equities/`.
- `holidays/` — the per-era working blocks the encoders read
  (`cme-2013-2015.json` and friends, with their `.verify.json` twins).
- `normal-weeks/` — normal-week capture waves.
- `cme-globex/` — Globex session-schedule evidence: rulebooks, product
  specifications, trading-hours pages.
- `raw/` — the earliest bare saves, keyed by capture date, from before the
  per-task `INDEX.md` convention.
- `ecbtc/`, `sgx-pre2020/` — per-venue research task directories (evidence
  state, decisions, source hunts).
- `holiday-tables/`, `ledger-reshape/`, `staged/` — wave and ledger working
  notes (assembly results, decisions, specs).
- `architecture-review/`, `catalog-artifacts/` — the 2026-09-12 architectural
  review and the consumer catalog tables it produced.
- `scratch-archive-2026-09-13/` — the archived pre-migration scratch, kept
  because its captures are still cited.
- `STAGE-*.md`/`STAGE-*.txt`, `gate-probe-*.tsv`, `DEV-PLAN-to-release.md`,
  `gate-1.0-acceptance.md`, `evidence-requests-2026-10.md` — the 1.0.0 gate
  stage's working files and probes.

## The audit chain

A claim in the crate verifies in five steps:

1. the evidence file (`docs/evidence/<owner>.md` in the crate) states the
   claim and cites a **document id** beside the row;
2. the file's `### Documents` table carries that id's **row**: the replay or
   service URL, the capture-or-retrieval instant (UTC), the tier (T1–T4, per
   LAW-PRIMARY-SOURCES) and the artifact's **sha256**;
3. the artifact's **path** is in this repository (or in the maintainer's
   working store, of which this repo is the byte-identical public mirror);
4. the file's **sha256** recomputes to the row's digest;
5. the **quote** the evidence file records appears verbatim in the bytes.

## Verifying

From a checkout of [`exchange-hours-rs`](https://github.com/SharurTrading/exchange-hours-rs)
whose sibling directory holds this repository (or with
`EXCHANGE_HOURS_RESEARCH` pointing at this checkout):

```sh
cargo xtask verify-evidence '<document-id>'   # one artifact: citation line, digest check, quote context
cargo xtask verify-evidence --all             # every Documents row in every evidence file
```

The tool resolves the id across all `### Documents` tables, recomputes the
sha256 from the bytes here, and exits non-zero on any mismatch. This
repository's digest fence also runs in the crate's CI
(`.github/workflows/evidence-audit.yml`) on every pull request that touches
`docs/evidence/` — the audit is enforced, not customary.

A full clone is ~230 MiB packed. Without it:
`git clone --filter=blob:none` plus `git sparse-checkout set <venue-dir>`
fetches one venue's evidence on demand; the git history is the version
record, so a citation can be checked at the date it was written, too.

## Ingest policy

- **The initial bulk import predates the branch-protection ruleset and was
  grandfathered**: it landed as a direct push before the ruleset was active,
  and was byte-verified afterwards against the store's digests (`rsync -rcn`
  checksums, and the per-task `INDEX.md`/`SHA256SUMS.txt` sidecars) — clean.
  It is the only direct push to `main` this repository will ever carry.
- **All future ingest is branch + pull request.** The PR diff — new capture
  files plus their `INDEX.md`/`SHA256SUMS.txt` entries — is the reviewable
  audit log of what entered the record, and `main` is protected so direct
  pushes are not accepted.
- **Captures are immutable after recording.** A stored artifact is never
  edited, renamed or re-normalized; its sha256 is its identity.
- **Corrections are new artifacts.** A re-retrieval that supersedes an
  earlier capture is added under its own digest beside a note; the earlier
  artifact stays. Silent mutation is detectable from the digests and
  prevented by the PR gate.

## Sync

The maintainer's local working store (at `../exchange-hours-research` beside
the crate checkout) stays the capture workspace; this repository is its
public, versioned mirror. The sync lands through a pull request:

```sh
rsync -a /path/to/exchange-hours-research/ /path/to/exchange-hours-evidence/
git -C /path/to/exchange-hours-evidence checkout -b watch-<date>
git -C /path/to/exchange-hours-evidence add -A
git -C /path/to/exchange-hours-evidence commit -m "<what the watch retrieved>"
git -C /path/to/exchange-hours-evidence push -u origin watch-<date>
# open the PR into main; the INDEX/SHA256SUMS diff is the reviewable log
```

The weekly watch cadence's additions (LAW-WATCH in the crate's `AGENTS.md`)
land here the same way.

## License and republishing posture

The repository's own prose, notes and decision log are
[MIT-0](LICENSE). The stored artifacts are operator documents — holiday
calendars, rulebooks, notices, feed captures — all of which are already
public, retrieved from the operators or from verbatim public mirrors
(Wayback) as LAW-PRIMARY-SOURCES requires; this repository republishes them
for verifiability, and each remains its operator's document.

## Branch protection

`main` is protected by an org ruleset: pushes require a pull request (the
initial bulk import above is the grandfathered exception), history stays
linear, force pushes and deletions are refused. Approving reviews are not
required — the maintainer may merge their own ingest PRs.
