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

A full clone is ~306 MB packed. Without it:
`git clone --filter=blob:none` plus `git sparse-checkout set <venue-dir>`
fetches one venue's evidence on demand; the git history is the version
record, so a citation can be checked at the date it was written, too.

## Ingest policy

- **Captures are immutable after recording.** A stored artifact is never
  edited, renamed or re-normalized; its sha256 is its identity. The PR diff
  of a capture (and of any `INDEX.md` / `SHA256SUMS.txt` beside it) is the
  reviewable audit log of what entered the record.
- **Corrections are new artifacts.** A re-retrieval that supersedes an
  earlier capture is added under its own digest beside a note; the earlier
  artifact stays. Silent mutation is detectable from the digests and
  prevented by the PR gate.
- **Additions come through pull requests** into `main`. Direct pushes are
  not accepted; `main` is protected.

## Sync

The maintainer's local working store (at `../exchange-hours-research` beside
the crate checkout) stays the capture workspace; this repository is its
public, versioned mirror. The sync is mechanical:

```sh
rsync -a /path/to/exchange-hours-research/ /path/to/exchange-hours-evidence/
git -C /path/to/exchange-hours-evidence add -A
git -C /path/to/exchange-hours-evidence commit -m "<what the watch retrieved>"
git -C /path/to/exchange-hours-evidence push
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

`main` is PR-gated. Recommended settings (applied when org permissions
allow): require pull requests (approving reviews not required — the
maintainer may self-merge), no force pushes, no deletions, linear history.
