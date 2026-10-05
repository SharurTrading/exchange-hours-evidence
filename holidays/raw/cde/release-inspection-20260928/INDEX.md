# INDEX — Stage 7 release-month re-inspection, Coinbase Derivatives (coinbase_derivatives)

Retrieval session: **2026-09-27 19:56–19:58 UTC** (`date -u`). The market-notices listing is
client-rendered; read through `https://r.jina.ai/`. Prior holdings: `holidays/raw/cde-2021-2025/`,
`cde-2026-2027/`, `coinbase-derivatives-2022-2024/`, and the 2026-2027 wave's CDE notices
(newest held: MN 26-36, 2026 Labor Day, published 2026-08-25; horizon 2026-09-07).

## Verdict: NO NEW holiday publication — the horizon stands at 2026-09-07

- The listing (`cde_notices_page.md`) shows **no Holiday-category notice after 26-36**. The next CDE
  holiday (Thanksgiving, Nov 26) had no notice as of retrieval; historically CDE posts those ~2 weeks
  ahead (Labor Day: Aug 25 for Sep 7; New Year 2026: Nov 25, 2025).
- One NEW Market notice, **26-37 — "CDE Q4 Quarterly Maintenance Window & FIA DR Testing - Details"**
  (listed 2026-09-24, effective 2026-10-24; Maintenance category — the same FIA industry DR exercise
  CME's notice 20260921 names). Recorded, not retrievable this pass: the reader render no longer
  exposes the Contentful asset URLs and a direct fetch of the page returns a 5.7 KB client shell
  (`cde_notices_raw.html`), so the PDF bytes were not recovered within the one-pass timebox. If the
  release PR needs it, recover the asset id from the page's Contentful JSON (the 2026-09-12 method).
  It is a maintenance-window arrangement, not a holiday grid change; it cannot extend the holiday
  horizon by itself.
- The #112 items are untouched by this pass: 22-10 stays a proven channel death; 24-12 stays
  draft-only (no final revision listed as of today).

## Artifacts

| file | url | retrieved (UTC) | sha256 |
|---|---|---|---|
| `cde_notices_page.md` | https://www.coinbase.com/derivatives/market-notices (reader) | 2026-09-27 ~19:57 | see SHA256SUMS.txt |
| `cde_notices_raw.html` | same URL, direct fetch — client-rendered shell kept as evidence of the direct channel's refusal | 2026-09-27 ~19:58 | see SHA256SUMS.txt |
