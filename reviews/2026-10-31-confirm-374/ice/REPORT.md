<!-- SPDX-License-Identifier: MIT-0 -->

# ICE forward-publication confirmation for issue #374

Completed 2026-10-31 23:21:52 UTC. Checked crate head
`d3f6b21db8f4f7523f0c79b786c16c6852c4678c` (merged PR #375).
No runtime discrepancy was found and no runtime file was changed.

## Fresh operator artifacts

`MANIFEST.json` records original request/final URLs, methods, exact UTC start
and completion instants, HTTP status, Content-Type, Last-Modified, byte counts
and SHA-256 for each successful retrieval. All four requests returned HTTP 200.

- Christmas notice: https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_2026_Christmas_Holiday_20261022.pdf
  Retrieved `2026-10-31T23:19:44.587592+00:00`; 132381 bytes; SHA-256
  `a7658155b57c51085cd3b36abc9ff6b91f3ca353cda88365a06459ebb40f0801`. Byte-identical to the retained 23 October and earlier
  31 October captures. The publication remains dated 22 October 2026 and is
  unconditional in session language, without a readiness/approval condition.
- Current regular-hours master: September 2026 edition,
  `ICE_Futures_US_Regular_Trading_Hours.pdf`; SHA-256
  `381c04fcb4d5b4093f72463246652ac8e24c3ca7b89283dfe86f736497c13ed2`.
- PCPO notice dated 20 September 2018,
  `ICE_Futures_US_PCPO_Session_20180920.pdf`; SHA-256
  `42a4e0ec45f59fae316924a8421bbdd779a3ee6e8b47aea08ad5944caa27b21d`.
- Current 2026 notices listing: POST `https://www.ice.com/api/sitesearchservice/v1/search/websitenotices?searchCollections=futures_us_exchange_notice&year=2026`,
  retrieved `2026-10-31T23:19:44.472388+00:00`; SHA-256
  `8b8e279bb921eafa7c7777b2f0d3f54d204682a98ea3321f148c4da1f08a74fd`.

Every PDF was independently converted with `pdftotext -layout`; the retained
`.txt` files show the complete session cells and the PCPO footnote. No expiry,
TAS-end or settlement-window cell was read as a matching boundary.

## Scope and clock comparison

All clock values below are America/New_York local time. The source itself
states New York time. Exception offsets are civil-day offsets relative to the
record's trade date, not UTC offsets.

| Modelled family | 24 December matching close | 24 December PCPO | 28 December matching |
|---|---|---|---|
| Sugar No.11 | 13:00, regular | 13:30–15:30 | 08:00–13:00 |
| Coffee C | 13:05 | 13:35–15:30 | 08:00–13:30 |
| Cocoa | 13:05 | 13:35–15:30 | 08:00–13:30 |
| Cotton No.2 | 13:05 | 13:35–15:30 | 08:00–14:20 |
| FCOJ | 13:05 | 13:35–15:30 | 08:00–14:00, regular open |
| NYSE FANG+ | 13:15 | no softs PCPO scope | regular matching |
| US Dollar Index | 13:15 | no softs PCPO scope | regular matching |

All seven families remain closed for trade date 25 December. The notice's
softs footnote names Sugar 11, Coffee C/Metric, Cocoa, Cotton No.2 and FCOJ,
plus unmodelled Canola. Sugar 16's separate regular-open clause does not
change the Sugar 11 key. Canola, the newly listed livestock contracts, Daily
Gold/Silver and other non-routed groups are outside these exact keys. FANG+
continues the existing disclosed interpretation of the notice's NYSE Stock
Indexes group; the regular-hours master separately names NYSE FANG+ and
corroborates its normal 20:00–18:00 grid. USDX is explicitly named in the
notice. No new product scope was admitted.

The shortened Thursday queues feed Monday 28 December and are represented at
offset -4 on that trade date. The 2018 PCPO notice states thirty minutes after
the contract's close through 18:00 on the prior Exchange business day; the
Christmas footnote expressly shortens the 24 December endpoint to 15:30.
It thus corroborates the preserved Thursday queue, with Friday 25 December
closed. Cotton's special Monday 08:00 matching is explicit in the Christmas
notice and is not inferred from the ordinary week, which has no Sunday leg.

Cotton's dependent 29 December replacement is a model consequence, not a claim
that the Christmas notice prints 29 December: it restates the unchanged Monday
28 December 14:50–18:00 PCPO and 19:30–21:00 Pre-Open, then Monday 21:00 through
Tuesday 14:20 matching. Those boundaries match the fresh ordinary-hours master
and PCPO table. It removes the raw Christmas-Friday queue that would otherwise
be assigned to Tuesday by the ordinary no-Sunday grid. The broad venue retains
its 24/28/29 December disagreement markers.

`verify_merged_data.py` independently compares the manually read/derived clock
matrix with the merged Rust block constants and dates. `MERGED_DATA_CHECK.json`
records 18 successful checks, the source SHA-256 and the exact crate head.
`cargo test --test futures_family_boundaries holidays_ice_us` passed all 25 ICE
tests, including the full queue/reopen boundary regression and the next-day
Cotton queue assignment. This reuses the existing tests; no test was added.

## Supersession check and limits

The current public ICE 2026 notices service reports 129 total notices and
returns the latest ten, in descending publication order, covering 2–29 October.
The 22 October Christmas notice links to the exact verified PDF. The three later
entries are margin updates dated 29 and 27 October and the livestock-options
listing dated 26 October. No newer Christmas-hours amendment or replacement was
identified in this checked publication window. The current PDF itself is
unchanged. The older 119 records were not paginated because the returned window
already reaches before the Christmas notice; this is not an exhaustive audit
of unrelated ICE publications or every operator channel.

The confirmation is bounded to those live artifacts as retrieved on 31 October
at 23:19:44 UTC and satisfies the before 23 December publication check tracked
in #374. It does not witness December production trading, guarantee that ICE
will not issue a later amendment, change the publication horizon, or supply
unpublished 2027 exception instants. Source URLs and original retrieval history
in the crate's Documents tables are preserved rather than overwritten.
