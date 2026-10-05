# Evidence index — task `eurex-2025-2027`

Primary-source retrieval for the `eurex` served identity (Eurex / Eurex Deutschland), whose
shipped holiday table covers only `2026-01-01 .. 2026-12-31` (`EUREX-HOLREG-2026`). This store
holds the **2025** coverage evidence and the **2027** published-future evidence.

Retrieval session: **2026-09-26, 07:13–07:16 UTC** (LAW-UTC-DATES). All timestamps below are UTC.
`curl` was used with a normal desktop browser User-Agent. No access control was evaded; no proxy
or credential trick was used. `web.archive.org` was intermittently unreachable from this machine
(`curl: (7) Failed to connect … port 443`) throughout the session and every archived artifact
below needed 2–5 retries; this is recorded because it bounds what was retrieved.

**No `.raw` copies are present, and none are needed.** Both fetch paths returned the operator's
bytes unmodified: `curl` on `eurex.com` writes the response body verbatim, and the Wayback
Machine's `id_` replay returns the raw archived WARC payload rather than a rewritten rendering.
This is confirmed rather than assumed — the live 2025 PDF and the Wayback `id_` replay of the
2025 PDF are **byte-identical** (both sha256 `d51053a3…`, both 161061 bytes). See §"Verification".

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `Eurex_Trading_Calendar_2025.pdf` | `https://www.eurex.com/resource/blob/4242284/1c8da6dc2702d508ee2a4740654ea77d/data/tradingcalendar_2025_en.pdf` | 2026-09-26T07:14:29Z | `d51053a39e786022db3fa2f12e00d9646145db10aa308ea1bd4446ed0cd16614` | 161061 | **T1. THE PRIMARY TARGET.** "Eurex trading calendar 2025", 2 pages, PDF 1.4. Page 2 column **"Overview of holidays by countries"** states the 2025 closure scope statements with day-level dates, and carries the German-scope note `… : tba.` Page 1 is the trading-hours table. |
| `Eurex_Trading_Calendar_2025.wayback-20250116023327.pdf` | `https://web.archive.org/web/20250116023327id_/https://www.eurex.com/resource/blob/4242284/1c8da6dc2702d508ee2a4740654ea77d/data/tradingcalendar_2025_en.pdf` | 2026-09-26T07:15:22Z | `d51053a39e786022db3fa2f12e00d9646145db10aa308ea1bd4446ed0cd16614` | 161061 | **T1 verbatim public mirror**, captured 2025-01-16. Byte-identical to the live copy — independent proof the live file is the document Eurex served in January 2025, not a later re-issue. |
| `Eurex_Trading_Calendar_2025.txt` | derived by `pdftotext -layout` from the PDF above | 2026-09-26T07:14:39Z | `68a7521755552c73b5c51ae173393122d1acd3ea60568b9b7e6d8fbec4b3240b` | 91328 | **Derived, not an operator artifact.** Layout-preserving text extraction, used to quote and cross-check the PDF. Do not cite as evidence; cite the PDF. |
| `eurex_holiday_regulations_2025.wayback-20250319022256.html` | `https://web.archive.org/web/20250319022256id_/https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations` | 2026-09-26T07:14:34Z | `a3ffe6ebe81a2063c409e6a40971991a3143a2c8440d38118a29d04acafe6b78` | 254007 | **T1.** The **2025** section of Eurex's Holiday regulations page (raw HTML). Contains the day-by-day 2025 table (**58 rows**) and the heading **"Non-trading days at Eurex 2025 - 2030"** with the 2025→2030 column table and its `*` footnote. This is the **earliest** of the three 2025 states. |
| `eurex_holiday_regulations_2025.wayback-20250623150653.html` | `https://web.archive.org/web/20250623150653id_/https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations` | 2026-09-26T07:15:50Z | `37f372ff0f18b78cb6d75e8b7826efdcc59167c0a92c0709a3cf3cd6ecab49f7` | 266752 | **T1.** Mid-2025 state of the same 2025 section (**54 rows**). Table content identical to the September capture. |
| `eurex_holiday_regulations_2025.wayback-20250913041407.html` | `https://web.archive.org/web/20250913041407id_/https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations` | 2026-09-26T07:15:50Z | `878e46c01a166f107607c19da8842e270f97915cfc1675b8928d2167ca804ea8` | 279331 | **T1. Controlling in-year 2025 state** (raw HTML, capture 2025-09-13). The 54-row day-by-day 2025 table transcribed verbatim in `eurex-2025-holidays.md` §3, plus the "Non-trading days at Eurex 2025 - 2030" table. |
| `eurex_holiday_regulations_2026.live-20260926.html` | `https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations` | 2026-09-26T07:13:32Z | `6eaa71115aa9efd4b2c9be2c22e6f7e67d4c175af372e2d78cf68a574c677faa` | 156497 | **T1.** The page as it stands today. Carries **only** a `<h2>2026</h2>` day-by-day section — **the 2025 section is gone from the live page**, which is why the three archived captures above are required — plus the heading **"Non-trading days at Eurex 2026 - 2030"**, whose 2027 column is the second independent statement of the 2027 holidays. |
| `eurex_trading_calendar_archive.live-20260926.html` | `https://www.eurex.com/ex-en/trade/trading-calendar/trading-calendar-archive` | 2026-09-26T07:13:30Z | `5011014c04f5f69602f7f292effb5ffcd07b83235fe91e656157eb725f50a28c` | 147139 | **T1.** The "Trading calendar archive" page. This is where the **live 2025 PDF URL was found**; it lists editions **2012–2026** and contains the string `2027` **zero** times — evidence that no Trading Calendar 2027 PDF exists. |
| `eurex_trading_calendar_hub.live-20260926.html` | `https://www.eurex.com/ex-en/trade/trading-calendar` | 2026-09-26T07:13:33Z | `f9b29f4f6b7e08a948041bb610980eee777a189b6cc02f4669d1b264143f802b` | 135242 | **T1.** The Trading calendar hub page. Offers **only** the 2026 PDF for download; no 2025 or 2027 edition is linked from the hub. |
| `eurex_indicative_trading_calendars.live-20260926.html` | `https://www.eurex.com/ex-en/trade/trading-calendar/indicative-trading-calendars` | 2026-09-26T07:15:54Z | `965c3e49a30854d3e3de187b2e6bc6e6321e7d770f248f6a4089ba875790bbd8` | 135846 | **T1.** Carries the operator's **express preliminary caveat** covering 2027–2036, quoted verbatim in `eurex-2025-holidays.md` §4.2. Decisive for the 2027 status question. |
| `eurex-2025-holidays.md` | (working note, this directory) | 2026-09-26T07:17:23Z | `839cfa499db8d71bb85877329c43f9d4261750e12f3a71cd9e24a8d1a81a47dd` | 19514 | The transcription: verbatim 2025 closure table, the operator's recurring-holiday grid, the Trading-Calendar scope statements, the `tba` German-scope note, the mid-2025 revision, and the 2027 status. |

## Verification performed (not assumed)

1. **Live vs archived 2025 PDF.** `cmp` reports the two PDFs byte-identical; both sha256
   `d51053a39e786022db3fa2f12e00d9646145db10aa308ea1bd4446ed0cd16614`. Independent capture dates
   (2025-01-16 vs 2026-09-26) argue the file is unchanged since publication.
2. **PDF authenticity.** The page-2 running header reads `Eurex trading calendar 2025`. The
   embedded PDF metadata reads `/Title: Trading Calendar 2024` with
   `/CreationDate: 20241223121730+01'00'` — a **template carry-over in the operator's own
   metadata**, not a mis-filed 2024 document. The creation instant (2024-12-23) precedes the
   2025 year it describes, which is what a genuine forward-published edition looks like. Do not
   mistake the metadata for evidence that this is the 2024 calendar.
3. **Transcription fidelity.** Every row of `eurex-2025-holidays.md` §3 was machine-diffed against
   the `<table>` in `eurex_holiday_regulations_2025.wayback-20250913041407.html`: **54 source rows,
   54 transcribed rows, 0 mismatches** on date, verbatim text and closure marker (37 closures,
   17 cash-payment-only notes).
4. **Cross-artifact agreement.** The PDF's `all derivatives: 1 January, 18 April, 21 April, 1 May,
   25 December, 26 December` and `24 December, 31 December`, and its seven per-country clause
   date lists, each match the corresponding day-by-day rows of the page. No disagreement found.
5. **The 2027 URL trap was tested.** `…/blob/4873184/0ca7669a…/data/tradingcalendar_2027_en.pdf`
   returns **HTTP 200** — but so does `…/data/zzz-does-not-exist.pdf`, and both return the **2026**
   PDF (sha256 `b0796b42…`). Eurex's blob route is a catch-all keyed on the blob id+hash, not the
   trailing filename. The 200 is therefore **not** evidence a 2027 edition exists.
6. **Caveat-language scan.** Full-text scans of the live 2026 page and all three 2025 captures find
   **zero** occurrences of `preliminar`, `indicativ` and `subject to change`, and the only footnote
   anywhere on them is the `*` asterisk note. The single `Xetra` string on the holiday-regulations
   pages is a footer navigation link.

## Known limitation

`web.archive.org` refused connections for most of this session and every archived byte required
repeated retries. Only one capture of the 2025 PDF and three captures of the 2025
holiday-regulations page were obtained; the CDX index was reachable, so the *set* of captures is
known to be complete even where a given capture could not be fetched. Specifically,
`20250623150653` and `20250913041407` succeeded on retry, and the CDX listing shows no further
2025 capture of the holiday-regulations page beyond those three.
