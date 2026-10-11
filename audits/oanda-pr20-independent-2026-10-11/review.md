<!-- SPDX-License-Identifier: MIT-0 -->

# Independent archive-capture review — 2026-10-11 UTC

Verdict: pass evidence PR #20 at exact final pushed head
`edb1ae7d1bf1ff356cc98075787fdde834caab6e`. The reviewer did not write the
capture bundle. This capture/inventory verdict does not establish complete
runtime OANDA coverage or discharge exchange-hours-rs issue #332.

The original head `8ba1b1b11ac47b42a2276f88c08b52d4bda040b2` was rejected
for wrong usable-response counts and eight incorrect manifest classifications.
Seven supposedly unusable files were valid gzip bodies. The remaining false flag
was the uncompressed August 2022 UK holiday page, which explicitly states the
Summer Bank Holiday UK index/UK10Y closure and Sugar late opening. Those are
operator statements, even when they do not mention US books. The final head
corrects all flags, README/STATUS/PR counts and adds encoding metadata and exact
decoded derivatives without modifying any original response bytes.

The independently written `review-archive20.py` parses visible operator HTML,
detects gzip, compares each decoded derivative byte for byte with its raw body's
`gzip.decompress` output, verifies manifest byte lengths/digests and every
SHA256SUMS row, and recomputes CDX and saved-response counts. It reproduces 37
usable raw responses: 19 hours tables and 18 holiday calendars; seven exact gzip
derivatives; all 64 sidecar hashes; 27 distinct indexed hours digests starting
2021-03-03; and eight indexed hours replays still absent after retrieval. The
holiday index reproduces 18 rows spanning 2022–2026. All 37 original response
bytes are preserved. `archive20-final-verification.json` records these results.

Every source claim in the new README and STATUS section was read against the
visible operator text in the cited capture bundle:
`normal-weeks/oanda-uk-wayback-audit-2026-10-11/`.

- `hours-captures/20230605093523.html` prints FX 17:03–16:58 and XAU/USD
  18:03–16:58. `hours-captures/20240221005503.html` prints 17:05–16:59 and
  18:05–16:59. Neither observation states an unconditional effective day.
- The Australian/German seasonal footnote is generic and does not identify
  the Australian selector's DST jurisdiction.
- `holiday-captures/20250326184653.html` retains dated 2024 arrangements.
- `holiday-captures/20260217213704.html` states the ANZAC 2025 Australian day
  closure/night-session continuation missing from the current capture.
- `holiday-captures/20260608180629.html` repeats the incomplete Memorial
  index/bond reopening `18:0`.
- Both March 2025 and February 2026 captures state Carter's dated section
  under the Eastern-Time header: index close `9:30`, reopen `18:00`, beside
  bond/commodity `13:15` closes and `18:00`/`20:00` reopens. The local 24-hour
  notation and ordered same-day close/reopen support 09:30 ET as an explicit
  interpretation, distinct from what the raw source literally prints. The
  word “early” alone is not proof: the same operator calls Holy Thursday's
  17:00 close early despite the ordinary 16:59 grid.

No source/prose blocker remains in the capture PR. The new metadata/prose
passes whitespace checks; raw operator HTML retains its original formatting.
The evidence-only repository has no Rust workspace or runtime schedule change.
