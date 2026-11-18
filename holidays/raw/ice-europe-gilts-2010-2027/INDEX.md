# Evidence index — `ice-europe-gilts-2010-2027`

The directory's original contents (the archived IFEU Trading-Schedule editions
2021-2026 with their `pdftotext -layout` extractions, and the NYSE Liffe
notice-archive zips 2008-2014) were banked by the waves recorded in
`../ice-history-2026-10-13/INDEX.md` and
`normal-weeks/ice-gilts-2026-10-11/`; their digests live in that wave's
`INVENTORY.tsv` / `SHA256SUMS.txt`. This index covers only the later
incremental capture below.

## A. IFEU Christmas and New Year 2026 trading hours (2026-11-18 wave)

| # | File | Operator URL | Retrieved (UTC) | sha256 | What it witnesses |
|---|---|---|---|---|---|
| A1 | `20261118084411_IFEu_Christmas_New_Year_Trading_Hours_2026.pdf` | <https://www.ice.com/publicdocs/futures/IFEu_Christmas_New_Year_Trading_Hours_2026.pdf> | 2026-11-18 08:44:11 | `09adfc0b9977f96bfd8b3f7d31bc232932b1dc0b0584d7cd274de7b9066a16eb` | `IFEU Trading Hours: 2026 Christmas and New Year Holidays`, edition header "November 2026", 14 pages. The gilt-family rows: 24 and 31 December 2026 both print the gilt rows ("Long Gilt Futures and Options", "Short, Medium and Ultra Long Gilt Futures") with designated settlement periods 12:13-12:15 (GMT) and "Trading ceases 12:15 (GMT)"; 25 December "The Exchange will be closed."; 28 December the exchange is OPEN except a named list that includes "Short, Medium, Long and Ultra Long Gilt Futures and Long Gilt Options"; 29 December "OPEN for trading ... for all contracts"; 30 December prints no gilt row; 01 January 2027 "The Exchange will be CLOSED." |

`A1.txt` is the `pdftotext -layout` extraction of the PDF beside it; its mtime
is the extraction time, not a second retrieval. The PDF was fetched live from
the operator's site (HTTP 200, 290,836 bytes) — the same URL 404'd when probed
2026-10-11 UTC, so this edition postdates that check; the holiday-hours hub
page still linked the 2025 edition at retrieval time.

| # | File | Operator URL | Retrieved (UTC) | sha256 | What it witnesses |
|---|---|---|---|---|---|
| A2 | `holiday-hours-live-2026-11-18.html` | <https://www.ice.com/holiday-hours> | 2026-11-18 (minutes after A1) | `078ca72dce86a14897752dc5bb1fae4bb5bd372fa9401a7c7fc1c33742df4971` | The hub page's Christmas/New Year link still names `IFEu_Christmas_New_Year_Trading_Hours_2025.pdf` only (two occurrences; no 2026 link), so the 2026 edition was discovered by its predictable URL, not the hub. |

Consumed by `exchange-hours-rs` on 2026-11-18 UTC: document id
`IFEU-XMAS-2026` in `docs/evidence/ice_europe_gilts.md` — the two 2026 eves
upgraded from `Unsourced` to sourced 12:15 early closes, and the audited
window extended through 2027-01-01.
