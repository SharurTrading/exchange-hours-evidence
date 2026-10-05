# Evidence index — task `cfe-eurex-ice-cde-smfe-2026-2027`, **ROUND-1 FIX**

Artifacts retrieved by the FIXER in response to
`/Users/agedvagabond/Developer/exchange-hours-research/holidays/cfe-eurex-ice-cde-smfe-2026-2027.verify.json`
(discrepancies **A** and **B**; advisories **C**, **E**, **F** answered in CORRECTIONS below).

All retrieval times are UTC (`date -u`), per LAW-UTC-DATES. Retrieval session: **2026-09-12 07:41–07:48 UTC**.
The round-0 evidence directory `../cfe-eurex-ice-cde-smfe-2026-2027/` is unmodified; nothing in it was
deleted or rewritten. Round-0 result preserved at
`/Users/agedvagabond/Developer/exchange-hours-research/holidays/cfe-eurex-ice-cde-smfe-2026-2027.r0.json`.

| File | URL | Retrieved (UTC) | sha256 | What it is |
|---|---|---|---|---|
| `CDE_Market_Notice_26-01_MLK_Holiday.pdf` | https://images.ctfassets.net/k3n74unfin40/jJEoZRkAZ0JlPC3UcJ2CL/d71ac89c5cd10783b9a7e11f449d1424/Market_Notice_26-01_MLK_Holiday.pdf | 2026-09-12 07:41 | d4b206391f70a015002af78c04c46bdce0ed08f87005b5b8e383cc7c5cd01f38 | **T1. Discrepancy A.** Coinbase Derivatives **Market Notice 26-01**, Date `01/08/2026`, Subject "Coinbase Derivatives 2026 Martin Luther King Jr. Day Schedule". Hours-of-Operation grid in CT for trade dates Friday 1/16, Monday 1/19, Tuesday 1/20. This is the document round 0 declared did not exist. |
| `CDE_26-01.txt` | (`pdftotext -layout` of the above) | 2026-09-12 07:42 | 0b5d63198bdbf8151697dc5a11132dc92945d14575301c8fcc25ec9549db5485 | Text extraction; the verbatims in the JSON are read off this file and re-checked against the PDF. |
| `cde_market_notices_page_raw.html` | https://www.coinbase.com/derivatives/market-notices (via `https://r.jina.ai/…` with `x-respond-with: html`; direct coinbase.com returns 403 to this machine) | 2026-09-12 07:41 | 523705cd5fa828ba035ec789a637a5c5d71298d1db4ab39e554b05e2b2f15a87 | **Provenance for the notice hrefs (advisory F).** Client-rendered page bytes. Every Market-Notice PDF href lives here inside the embedded Contentful rich-text JSON as `/`-escaped `assets.ctfassets.net` / `images.ctfassets.net` URLs — including the 26-01 row: `…"uri":"https://images.ctfassets.net/k3n74unfin40/jJEoZRkAZ0JlPC3UcJ2CL/d71ac89c5cd10783b9a7e11f449d1424/Market_Notice_26-01_MLK_Holiday.pdf"},"content":[{"nodeType":"text","value":"2026 MLK"…`. |
| `ICE_Futures_US_Exchange_Notice_2026_Holiday_Calendar_20260609.pdf` | https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_Exchange_Notice_2026_Holiday_Calendar_20260609.pdf — retrieved by Wayback `id_` replay of capture **20260728113521**, then re-fetched **live** and confirmed byte-identical (see `fetchlog.txt`) | 2026-09-12 07:43 (archive) / 07:47 (live) | b9723d9afa1c20a0792b628de36c7d3726add58ea3d94972a1e7cefd3e50bf4e | **T1. Discrepancy B.** The Exchange-Notice copy of "ICE Futures U.S. — June 9, 2025 — 2026 Trading Holiday Calendar". Same printed date, same 18 holiday rows, **every status cell identical** to the Holiday-Hours-hub copy already held (`../cfe-eurex-ice-cde-smfe-2026-2027/IFUS_Trading_Hours_Holiday_Calendar.pdf`, sha256 `da975035…`), but with updated product-group headers: `Cocoa, Coffee "C"®, Coffee "C"® Metric, Cotton No 2®, FCOJ, Sugar No. 11 and No. 16 Contracts` and `Currency, Digital Asset, Stock, SOFR, MSCI Bond, and Mortgage Index Contracts`. PDF `CreationDate` 2026-02-18 15:46 UTC (the hub copy's is 2026-01-07 14:00 UTC). |
| `ICE_2026cal_20260609.txt` | (`pdftotext -layout` of the above) | 2026-09-12 07:43 | 4a886915c440f6557b43e11439786ec321f0d28b5341112351f3d8aa91b008ee | Text extraction. `diff` against the round-0 `IFUS.txt` yields **only**: the two group headers, `Holiday` vs `Holiday:` in table 1, `For more information:` vs `FOR MORE INFORMATION` in the footer, and whitespace. No open / closed / open¹ cell differs. |
| `ifus_notices_cdx_2025-2027.json` | https://web.archive.org/cdx/search/cdx?url=ice.com/publicdocs/futures_us/exchange_notices*&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&from=2025&to=2027&collapse=urlkey | 2026-09-12 07:42 | eeaae29bb32039f5e785291302e2618784703db963853aee22030da3cbbaff03 | **Negative evidence, tested.** 113 distinct archived IFUS exchange-notice URLs. Holiday-matching rows: 2016, 2017, 2021, 2022 Presidents Day, 2023 Memorial Day, 2025 Good Friday / Juneteenth / **MLK** / **Presidents Day**, and the 2026 calendar above. **No 2026 MLK notice and no 2026 Presidents Day notice exist in the archive** — the round-0 gap (`missing[5]`) is real, and the 2025 notices must not be read across years. |
| `cde_ctfassets_cdx_mlk.json` | https://web.archive.org/cdx/search/cdx?url=assets.ctfassets.net/k3n74unfin40*&…&filter=original:.*(MLK\|Market_Notice_26-01).* | 2026-09-12 07:47 | f7ba079a732f69151b201ed0c1841232e920902951150bb7b3a271597b17272d | **Negative evidence.** Exactly one row — the 2025 notice `Market_Notice_25-01__MLK.pdf`. The CDE notice corpus has essentially no archival backstop; 26-01 had to come from the operator's own listing (and did). |
| `fetchlog.txt` | (commands + responses) | 2026-09-12 07:47 | f167aa6b7a945667395ac3f3340f10e0047090ac5c4021667c1acf953272bbad | Reachability re-test (`https://web.archive.org/` → **HTTP 200 in 1.04 s**), the live-vs-archive byte comparison of the 2026 ICE calendar (`cmp: IDENTICAL`), and the CDE CDX query. |

## Retrieval notes

- **web.archive.org is reachable from this machine.** The round-0 claim of total unreachability is withdrawn.
  Observed behaviour: the *first* connection in a burst can fail with `curl: (7) Failed to connect … port 443`
  and the immediate retry succeeds (the 2026 ICE calendar replay failed on attempt 1, returned 200 on attempt 2).
  Retry before concluding a channel is down; never let an untested failure bound a gap.
- **CDE notice PDFs** are not linked in the reader's markdown render. Fetch the page through the reader with
  `-H "x-respond-with: html"` and grep the Contentful payload for `ctfassets` — the hrefs are `/`-escaped.
- ICE serves the 2026 holiday calendar at **two** paths with different bytes. Prefer the
  `publicdocs/futures_us/exchange_notices/…_20260609.pdf` copy: it is the later-generated one and its group
  headers agree with the 2027 calendar.

## CORRECTIONS to `../cfe-eurex-ice-cde-smfe-2026-2027/INDEX.md`

That file is left byte-intact; the following supersede it.

1. **Header claim — WITHDRAWN.** "web.archive.org was unreachable from this machine for the whole session …
   this bounds the gaps recorded below" is false. See `fetchlog.txt`. The gaps it bounded were re-tested by CDX
   enumeration in this round and survive on their own evidence.
2. **CDE row — CORRECTED.** "**No 2026 MLK notice is listed** (26-01/26-02/26-04 are absent from the table)" is
   false and is contradicted by that directory's own `cde_notices_page.md`: line 1257 ff. carry
   `26-01 | Market | 01/08/2026 | 2026 MLK | Holiday`; 26-02 ("Copper and Platinum Futures", 01/08/2026) is at
   line 1209 and 26-04 ("PAX Gold, Zcash & Five (5) Additional Perp Style Futures", 01/29/2026) at line 1017.
3. **Interpretive note 2 — CORRECTED (verifier advisory C).** "Only 2026-12-25 has 'None / None' and is a full
   closure" contradicts the JSON, which also records **2026-01-01** as `closed`. The JSON is right on its own
   trade-date reading: the 1 January row is `New Year's Day,2026-01-01,None,5:00 PM (Thu) to 8:30 AM (Fri)` and
   1 Jan 2026 is a Thursday, so the only session named *starts* on the holiday evening — no session runs into or
   ends on the holiday, hence no early-close instant, hence `closed`. The rule note 2 should state is: a holiday
   row is an **early close** when its Extended-Trading-Hours string ends at an instant *on* the holiday date
   (MLK, Presidents' Day, Good Friday, Memorial Day, Juneteenth, Independence Day Observed, Labor Day,
   Thanksgiving Day), and **closed** when it does not (2026-01-01, and 2026-12-25 which prints "None / None").
4. **Missing index row — ADDED (verifier advisory E).** `../cfe-eurex-ice-cde-smfe-2026-2027/cfe_notices_raw.html`,
   169 bytes, sha256 `7108fef32b066dcb8e074d4114e8614cfb6f1efeb9497c0b0268b7b4039f22bc`, retrieved 2026-09-12
   04:18 UTC from `https://www.cboe.com/us/futures/notices/`. Content: a Cloudflare **`307 Temporary Redirect`**
   stub, not the notices page. It sources nothing; the usable render is `cfe_notices.md`.
5. **Contentful provenance — now demonstrable (verifier advisory F).** The sentence "the PDF hrefs were recovered
   from the page's embedded Contentful JSON" was true of the retrieval method but unsupported by the saved bytes
   (`cde_notices_links.md` holds only `CDEI-*` disciplinary PDFs). `cde_market_notices_page_raw.html` in this
   directory is the artifact that actually carries those hrefs.
