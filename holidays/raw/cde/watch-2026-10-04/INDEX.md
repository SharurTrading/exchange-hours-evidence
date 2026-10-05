# Coinbase Derivatives LAW-WATCH re-check — 2026-10-04 UTC (#155, post-2026-09-07 horizon)

Fourth forward re-check of the market-notices listing (after the 2026-09-19 wave,
the 2026-10-02 `../INDEX-recheck-2026-10-02.md` and the 2026-10-03
`../recheck-2026-10-03/` wave). Retrievals 00:29–00:37 UTC 2026-10-04; digests in
`SHA256SUMS.txt`.

**Outcome: NOT-YET.** No notice published past 26-37 (posted 09/24/2026); the
operator's holiday horizon is still trade date 2026-09-07.

- `cde_market_notices.reader-20261004T003100Z.md` — the live listing
  (`https://www.coinbase.com/derivatives/market-notices`) through the public reader
  (`r.jina.ai`, markdown mode), HTTP 200. The newest rows are unchanged from the 2026-10-03
  read: 26-33.3 (Market, posted 09/24/2026, effective 09/25/2026) and 26-37 (Market, posted
  09/24/2026, effective 10/24/2026, Q4 quarterly maintenance / FIA DR testing), then
  R2026-64..R2026-51 (Regulatory, 09/14-21/2026). The dates 09/28/2026, 10/01/2026 and
  10/05/2026 visible in the table are *effective* dates of those known regulatory notices,
  not new postings. No Market Notice 26-38 or later exists in the listing; the newest
  Holiday-category notice remains 26-36 (`2026 Labor Day`, posted 08/25/2026, effective
  09/07/2026). The five `Thanksgiving` strings in the table are the 2021-2025 Thanksgiving
  notices (posted late Oct to mid Nov of their years), so the 2026 Thanksgiving notice
  remains unpublished.
- `direct_market_notices-20261004T002900Z.html` — the direct channel still answers
  Cloudflare 403 (`Just a moment…`, 5805 bytes); recorded as the access state, not evidence.
- `cde_help_notices.reader-20261004T003500Z.md` and `…T003700Z.md` — the help-centre page
  (`https://help.coinbase.com/derivatives/general/market-notices`) through the reader passed
  the target's Cloudflare 403 through (255-byte stub, "Just a moment…"); the 00:37 retry is
  byte-identical. Both saved to keep the access record honest; the website listing above is
  the operative read and the help-centre page defers to it (evidence file, Sources).

Next check: 2026-10-11 (weekly), with the Thanksgiving notice expected around
2026-10-30 (the 2025 edition, 25-37, was posted 10/30/2025). Tracked as #155.
