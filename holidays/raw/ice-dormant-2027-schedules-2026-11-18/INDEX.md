# Evidence index — `ice-dormant-2027-schedules-2026-11-18`

Retrieval session: **2026-11-18 09:02 UTC** (`date -u`). All times UTC
(LAW-UTC-DATES). Purpose: the operator published year-2027 schedules touching
two **dormant** ICE identities; the crate's dormant-tier obligation is capture
plus a dated evidence-file note, with **no runtime-table change** — neither
identity's built-in data is touched by this wave.

| # | File | Operator URL | Retrieved (UTC) | sha256 | What it witnesses |
|---|---|---|---|---|---|
| A1 | `20261118090229_ICE_Endex_Trading_Schedule.pdf` | <https://www.ice.com/publicdocs/ICE_Endex_Trading_Schedule.pdf> | 2026-11-18 09:02:29 | `503c3eee7b26e7c90892fb391e8ad9b1cbea1e7e59879644bed506c7b89cd644` | "ICE ENDEX TRADING SCHEDULE — 1. Energy Derivatives, EUA's and GO Futures": Year-2026 and **Year-2027** holiday tables (2027 opens "Friday 01 January 2027 — New Year's Day — Closed"; also Good Friday 26 March, Easter Monday 29 March, and the US-holiday `C` rows). PDF internal title `ICE_Endex_Trading_Schedule V1.01 2627.docx`, created 2026-10-08 (AEDT) — the October-2026 V1.01 2026/2027 edition. |
| A2 | `20261118090229_Trading_Schedule.pdf` | <https://www.ice.com/publicdocs/Trading_Schedule.pdf> | 2026-11-18 09:02:29 | `518da0a932f71d81bd1f04b09ecd6598731531f90d587382dbcf3e3b23e0ac1e` | "IFEU Trading Schedule: Oil, Utilities and Agricultural", edition header "November 2026" (PDF created 2026-11-12), carrying the 2026 daily pages and a "**2027 Trading Schedule**" section with a `Year: 2027` table (2027-01-01 New Year's Day Closed, MLK Day 18 January `A`, Singapore Markers TAPS note, ...). This URL is the live oil/utilities/agri edition — the same channel the gilts evidence cites as the exchange-wide 2019/2020-era document class, now editioned per complex. |

The `*.txt` files are `pdftotext -layout` extractions beside their PDFs; their
mtime is the extraction time, not a second retrieval.

Consumed by `exchange-hours-rs` on 2026-11-18 UTC as dormant-tier evidence
notes only: `docs/evidence/ice_endex.md` and
`docs/evidence/ice_europe_commodities.md`. No schedule, holiday or ledger row
changes for either identity; the 2027 tables sit here until a consumer reaches
those identities (LAW-SERVICE-TIERS dormant obligations).
