<!-- SPDX-License-Identifier: MIT-0 -->
# Evidence index — gate U8-cross-zone-design

Gate: U-8 of `docs/plans/2026-09-05-cme-trade-type-handoff.md` (design decision, not retrieval).
Capture host: this machine, 2026-09-06. `www.cmegroup.com` 403s this IP directly; every CME
artifact below came through the public text reader `https://r.jina.ai/<cme url>` in front of the
same cmegroup.com URL — the weaker-channel route already recorded in `docs/schedules/sources.md`
and already cited in shipped code (`spot_quoted.rs`).

**Capture date is not artifact date.** The trading-hours service returns a *forward-looking
published calendar*: a 2026-09-06 capture of the 2027-03-15 week states what CME publishes today
for that week, not a fact observed in March 2027. Treated here as evidence of the anchor zone,
never as a dated cutover.

| file | URL | capture (UTC) | artifact date | sha256 |
|---|---|---|---|---|
| `energy-tam-faq.jina.txt` | https://r.jina.ai/https://www.cmegroup.com/articles/2024/energy-trading-at-marker-frequently-asked-questions.html | 2026-09-06T05:20Z | `Published Time: 2024-06-05T00:00:00.000Z` (line 5 of the captured bytes); CME `/articles/2024/` path | 5b623062d5b2cf51736ebfda9c6c3e77b92e7e203276b221b493611858c9e12b |
| `svc-8407-oct.txt` | https://r.jina.ai/https://www.cmegroup.com/services/trading-hours-by-product?id=8407&fromEventDate=2026-10-26&toEventDate=2026-10-30&pageSize=100 | 2026-09-06T05:21Z | published calendar for 2026-10-26..30 | 3fc7f07db5c68db89fa11d7dcf47c5a1d4378a4a66e189fd1fc8a500925fcc44 |
| `svc-8407-dec.txt` | same service, id=8407, 2026-12-07..2026-12-11 | 2026-09-06T05:21Z | published calendar for 2026-12-07..11 | 0917c5f9a055dab1f61beda7c5712d69c2aed108748e110c94bb951b01160eaa |
| `svc-8407-2027mar.txt` | same service, id=8407, 2027-03-15..2027-03-19 | 2026-09-06T05:21Z | published calendar for 2027-03-15..19 | 1cce99cafc3181990a6f49aaf47f601b57b0c4fea750c3aee02b3f89e50cebf6 |
| `svc-7956-oct.txt` | same service, id=7956 (FTC, group C1), 2026-10-26..2026-10-30 | 2026-09-06T05:21Z | published calendar for 2026-10-26..30 | b86f4f02345e192df91fcc29be1051e82259d99f187b8ecce747a128d069edc0 |
| `svc-7956-dec.txt` | same service, id=7956, 2026-12-07..2026-12-11 | 2026-09-06T05:21Z | published calendar for 2026-12-07..11 | 4890b8ebde8f0f8b76b79c9a7e50ccd58cab6b0ea21794ff32ea61ed01aaa0fb |
| `drift-computation.py` / `drift-computation-2026-09-06.txt` | local, no network (IANA tz database via CPython `zoneinfo`) | 2026-09-06 | derived | see `shasum -a 256 *` |

## Second-hand artifacts relied on (already retrieved by the shape-queue run, not re-fetched)

- `../../../shape-queue/tam-taco-tmac-marker-and-close-variants.json` — evidence blocks [1]-[11];
  its [11] decodes the 2026-08-30 `TradingSessionList` week for groups 80:TM, 80:TS, 80:WM,
  78:GM, 78:TR in UTC.
- `../../../shape-queue/btic-basis-trade-at-index-close-inventor.json` — evidence block [11]
  decodes the same week for BTIC rows 6, 8, 14, 20, 23, 24, 27, 31, 34.
- `../../../shape-queue/HANDOFF-TABLE.md` and the repo's
  `docs/plans/2026-09-05-cme-trade-type-handoff.md` §2 row U-8 — the original DST probe.
- COMEX metals marker page (copper's explicit London/New-York DST carve-out) — quoted second-hand
  from the TAM challenge JSON's block [4]; the live re-fetch was rate-limited on 2026-09-06 and is
  recorded as not independently re-verified here.

## Added by the 2026-09-06 re-run of this gate (same gate id)

| file | URL | capture (UTC) | artifact date | note |
|---|---|---|---|---|
| `recheck-2026-09-06b.py` / `recheck-2026-09-06b.txt` | local, no network (IANA tz database via CPython `zoneinfo`) | 2026-09-06T06:1xZ | derived | Independent re-derivation, written without reference to `drift-computation.py`. Reproduces every Chicago clock pair, the 2026 weekday split (241/20 London, 170/91 Asia, 261 total), the two-state exactness 2010-2030, the misalignment-window table, and the four DST transition instants for 2026-2027. **Corrects** the calendar-day count to 21 or 28 (was 20 or 27) and the nearest-to-midnight boundary to Nikkei/TOPIX 00:30 CT (was `CLC` 01:00 CT). |

Also re-verified on this run: `shasum -a 256 -c SHA256SUMS.txt` passes for all seven stored
artifacts (the checksum file's own self-line cannot match by construction), and the first-hand
CME service bytes were re-read rather than quoted from the memo:
`svc-8407-oct.txt` 5x `closed@10:02`, `svc-8407-dec.txt` 5x `closed@09:02`,
`svc-8407-2027mar.txt` 5x `closed@10:02`, `svc-7956-oct.txt` 5x `closed@03:00`,
`svc-7956-dec.txt` 5x `closed@02:00`; `open@17:00` and the group pre-opens (`16:50` GM,
`16:45` C1) identical in every file.

In-repo lines cited by the memo were re-read at **`fdc5408`** (branch `main`, the current HEAD;
the earlier draft cited `31121b0`, a valid ancestor). All still hold verbatim:
`schedules/profile.rs:18-26`, `rule.rs:41-71`, `schedules/timeline.rs:147-167`,
`query/schedule.rs:26` and `:263-271`, `query/sessions.rs`, `query/identity.rs:18-35`,
`futures_profile.rs:365`, `futures_profile/profiles.rs:307-317`,
`ice_endex.rs:150`, `ice_abu_dhabi.rs:103`, `eurex_fixed_income.rs:36-41` and `:277-297`,
`europe.rs:120`, `b3.rs:201`, `bmv.rs:235`, `golden_grids.rs:99`, `verification.md:144-145`,
`tests/seasonal_calendars/international.rs:36-71`,
`tests/seasonal_calendars/transition_scans.rs:48`.
