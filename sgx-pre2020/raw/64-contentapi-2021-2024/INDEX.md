# Issue #64 — SGX content API 2021-2024: do the five equity-index keys' routines change between the
# 2020-01-09 payload and the 2025 circular?

Retrieved 2026-09-06 by the #64 evidence pass. Every artifact below is SGX-authored and SGX-served
(api2.sgx.com content API, or the server-rendered www.sgx.com product pages that embed the same
CMS `tradingHours.processed` strings). Nothing here is a member mirror or a third party.

ANSWER IN ONE LINE. Across every `derivatives_products_list` capture the archive holds for
2021-2024 — 22 captures, at least one in every half-year — the `tradingHours.processed` strings for
SGX Nikkei 225 Index Futures, SGX FTSE China A50 Index Futures, SGX MSCI Singapore Index Futures,
SGX FTSE Taiwan Index Futures and SGX MSCI Singapore Free NTR (USD) Index Futures are **unchanged
from the 2020-01-09 payload, to the minute**. The only difference anywhere in the span is an HTML
re-serialisation at capture 20240605055619 (`<br />` -> `<br><br>`, U+00A0 -> `&nbsp;`,
`<p dir="ltr">` added); no time moves. So the crate's carry-forward of the 2020 routines through
2021-2024 is now directly witnessed, not assumed.

## A. CDX enumeration (this pass, not reused)

- `cdx_contentapi_all_2021_2025.txt` — `url=api2.sgx.com/content-api*&from=20201201&to=20260101`,
  `collapse=digest`, fields timestamp,statuscode,original,digest.
- `cdx_contentapi_all_2021_2025_nocollapse.txt` — same range, no collapse, fields
  timestamp,statuscode,original,digest,length. 1012 rows. Distinct persisted-query names in the
  range: page(190), we_chat_qr_validator(165), all_menus(141), alerts(139), taxonomy_terms(62),
  market_statistics_reports_list(56), advertisement_list(56), **derivatives_products_list(29)**, ...
- `cdx_www_products_gapwindow.txt` — `www.sgx.com/derivatives/products*`, 2024-11-01..2025-04-06.
- `cdx_www_ssf.txt` — `www.sgx.com/derivatives/products*`, 2023-09-01..2024-03-01.
- `targets.json` — the 29 `derivatives_products_list` rows, sorted.

SGX rotated the queryId hash repeatedly; the enumeration is by URL prefix, never by hash. The
`limit:10000` variant stops at 20200602051032; every capture from 20200715061901 on is the paged
`limit:100&offset:0` variant, and `count` in the payload (52-72) is below 100 throughout, so a
single page is the whole catalogue — no offset paging was needed.

**There is no `derivatives_products_list` capture between 20241007031911 and 20250407083045.**
The only content-api captures inside that window are three `:page` requests for
`/derivatives/products/sgxsimsci` (20241105093248, 20241105093428, 20240919134720) and all three
carry a stale queryId, so all three return, verbatim:
`{"errors":[{"message":"The persisted query loader must return query string or instance of GraphQL\\Language\\AST\\DocumentNode but got: null.","extensions":{"category":"request"}}]}`
(saved as raw_page_*.bin). Section D closes that window from a different SGX channel instead.

## B. `derivatives_products_list` captures retrieved (all 29; 22 fall in 2021-2024)

Files: `raw_<ts>.bin` (as served, gzip where the origin gzipped it), `dec_<ts>.json` (decoded),
`extracted_tradinghours.json` (the five keys, per capture), `diffs.txt` (first-seen + every change),
`allcontract_diffs.txt` (normalised consecutive diff over EVERY contract in the payload).

Exact archived URL form: `https://web.archive.org/web/<ts>id_/https://api2.sgx.com/content-api?queryId=<hash>%3Aderivatives_products_list&variables=%7B%22limit%22%3A100%2C%22offset%22%3A0%2C%22lang%22%3A%22EN%22%7D`

    capture (UTC)     half-year  queryId hash                              count  note
    20201206215049    2020H2     24dae0b548df549663707f60a9b482ca34de96ef   62    baseline for this pass
    20210105215220    2021H1     24dae0b548df549663707f60a9b482ca34de96ef   56
    20210216135503    2021H1     1f2389dc1e9410bcb4d9adeb9a49843a74e92a8b   55
    20210505065146    2021H1     f548e2fbd421be8b407f9b2571ee3286b44f6493   52
    20210604230405    2021H1     f548e2fbd421be8b407f9b2571ee3286b44f6493   53
    20210916185853    2021H2     a0d3e40edf4601ad5ce0536a38621dc9ea636cd5   59
    20211121024828    2021H2     75eea23663d1a2cc5a56189c42c01ee0d0ff4dd0   60
    20211123031015    2021H2     75eea23663d1a2cc5a56189c42c01ee0d0ff4dd0   60
    20220331155214    2022H1     5dea8654ce3118c9dc2f58c3ecd8e706e7c6e5b9   61
    20220523115319    2022H1     cc841af8e1646c1b80452df00e5762068394ea00   61
    20221102023108    2022H2     69607708850964950ff4f02e84746e155b288abb   63
    20230205123204    2023H1     47dc2eeb56ebcf6333871f4acfd1dbe9cb2b5ab6   64
    20230409014043    2023H1     47dc2eeb56ebcf6333871f4acfd1dbe9cb2b5ab6   66    lang=ZH_HANS
    20230526055103    2023H1     aab9c339d8d413395111f34d48814a323b676b4c   66
    20230829130145    2023H2     aab9c339d8d413395111f34d48814a323b676b4c   71
    20240207134658    2024H1     19f962b634490d0f2d1288cb2a5327efd6ec1c47   71
    20240215021646    2024H1     19f962b634490d0f2d1288cb2a5327efd6ec1c47   71    CDX "-" revisit, same digest
    20240316061416    2024H1     82414bb12f50e42129f1027029c3effa6707a740    -    stale hash; error body only
    20240426072245    2024H1     19f962b634490d0f2d1288cb2a5327efd6ec1c47   71
    20240605055619    2024H1     403f997d9996aad58079745c4782cc21eb7f89b7   71    HTML re-serialisation
    20240629110526    2024H1     403f997d9996aad58079745c4782cc21eb7f89b7   71
    20240721045147    2024H2     403f997d9996aad58079745c4782cc21eb7f89b7   72
    20240721045256    2024H2     403f997d9996aad58079745c4782cc21eb7f89b7   72
    20241007031911    2024H2     f6241666a335933a0ac9df97e14bfa23771b887c   72    last before the gap
    20250407083045    2025H1     9b5f40321735d88857c12bd08459b5aba7fe2d1e   71    first after the gap
    20250531092552    2025H1     54d7880bed915819b82da8c0cf77d10e299ea9cc   72
    20250822020227    2025H2     54d7880bed915819b82da8c0cf77d10e299ea9cc   72
    20250901094028    2025H2     54d7880bed915819b82da8c0cf77d10e299ea9cc   72
    20250902152826    2025H2     54d7880bed915819b82da8c0cf77d10e299ea9cc   72

`20240316061416` body, verbatim:
`{"errors":[{"message":"The persisted query loader must return query string or instance of GraphQL\\Language\\AST\\DocumentNode but got: null.","category":"request"}]}`

## C. The state held through 2021-2024, VERBATIM (first-seen at 20201206215049, unchanged to
##    20241007031911 apart from the markup re-serialisation at 20240605055619)

SGX Nikkei 225 Index Futures [NK]
    <p>T Session:<br />\nPre -Opening : 7.15 am - 7.28 am<br />\nNon -Cancel : 7.28 am - 7.30 am<br />\nOpening : 7.30 am - 2.25 pm<br />\nPre-Closing : 2.25 pm - 2.29 pm<br />\nNon-Cancel : 2. 29 pm - 2.30 pm</p>\n<p> </p>\n<p>T+1 Session:<br />\nPre -Opening : 2.45 pm - 2.53 pm<br />\nNon -Cancel : 2.53 pm - 2.55 pm<br />\nOpening : 2.55 pm - 5.15 am<br />\nPre - Closing : NA<br />\nNon - Cancel : NA</p>\n

SGX FTSE China A50 Index Futures [CN]
    <p>T Session:<br />\nPre - Opening: 8.45 am - 8.58 am<br />\nNon - Cancel: 8.58 am - 9.00 am<br />\nOpening: 9.00 am - 4.30 pm<br />\nPre - Closing: 4.30 pm - 4.34 pm<br />\nNon - Cancel: 4.34 pm - 4.35 pm</p>\n<p> </p>\n<p>T + 1 Session:<br />\nPre - Opening: 4.50 pm - 4.58 pm<br />\nNon - Cancel: 4.58 pm - 5.00 pm<br />\nOpening: 5.00 pm - 5.15 am<br />\nPre - Closing: NA<br />\nNon - Cancel: NA</p>\n

SGX MSCI Singapore Index Futures [SGP]   (the crate's "MSCI Singapore (Free)" family)
    <p>T Session:<br />\nPre - Opening: 8:15 am - 8:28 am<br />\nNon - Cancel: 8:28 am - 8:30 am<br />\nOpening: 8:30 am - 5:20 pm<br />\nPre - Closing: 5:20 pm - 5:24 pm<br />\nNon - Cancel: 5:24 pm - 5:25 pm</p>\n<p> </p>\n<p>T+1 Session:<br />\nPre - Opening: 5:40 pm - 5:48 pm<br />\nNon - Cancel: 5:48 pm - 5:50 pm<br />\nOpening: 5:50 pm - 5:15 am</p>\n

SGX FTSE Taiwan Index Futures [TWN]
    <p>T Session:<br />\nPre - Opening: 8.30 am - 8.43 am<br />\nNon - Cancel: 8.43 am - 8.45 am<br />\nOpening: 8.45 am - 1.45 pm<br />\nPre - Closing: 1.45 pm - 1.49 pm<br />\nNon - Cancel: 1.49 pm - 1.50 pm</p>\n<p> </p>\n<p>T+1 Session:<br />\nPre - Opening: 2.05 pm - 2.13 pm<br />\nNon - Cancel: 2.13 pm - 2.15 pm<br />\nOpening: 2.15 pm - 5.15 am</p>\n

SGX MSCI Singapore Free NTR (USD) Index Futures [NSG]
    <p>T-session:<br />\nPre - Opening: 7.10 am - 7.23 am<br />\nNon - Cancel: 7.23 am - 7.25 am<br />\nOpening: 7.25 am - 6.30 pm<br />\nPre - Closing: 6.30 pm - 6.34 pm<br />\nNon - Cancel: 6.34 pm - 6.35 pm</p>\n<p> </p>\n<p>T + 1 Session: <br />\nPre - Opening: 6.50 pm - 6.58 pm <br />\nNon - Cancel: 6.58 pm - 7.00 pm <br />\nOpening: 7.00 pm - 5.15 am <br />\nPre - Closing: NA <br />\nNon - Cancel: NA</p>\n

SGX MSCI Singapore NTR (USD) Index Futures [NSP]  (the sibling NTR row, same grid, different wording)
    <p>T Session:<br />\nPre -Opening : 7.10 am - 7.23 am<br />\nNon -Cancel : 7.23 am - 7.25 am<br />\nOpening : 7.25 am - 6.30 pm<br />\nPre-Closing : 6.30 pm - 6.34 pm<br />\nNon-Cancel : 6.34 pm - 6.35 pm</p>\n<p> </p>\n<p>T+1 Session:<br />\nPre -Opening : 6.50 pm - 6.58 pm<br />\nNon -Cancel :6.58 pm - 7.00 pm<br />\nOpening : 7.00 pm - 5.15 am<br />\nPre - Closing : NA<br />\nNon - Cancel : NA </p>\n

### Every capture in which anything differed (from `diffs.txt`)

1. **20230409014043** — `SGX MSCI Singapore NTR (USD) Index Futures` absent. This is the ZH_HANS
   capture: its `derivativesCategories` read `{"id":"187","name":"外汇"}`, `{"id":"188","name":"股票指数"}`,
   so the Chinese CMS tree simply has no NSP node. The four other keys carry byte-identical English
   strings. **Not a schedule change.** NSP is present again at 20230526055103.
2. **20240605055619** — markup only, all six rows. Example, Nikkei:
   PREV `<p>T Session:<br />\nPre -Opening : 7.15 am - 7.28 am<br />...`
   NOW  `<p dir="ltr">T Session:<br><br>\nPre -Opening : 7.15 am - 7.28 am<br><br>...`
   Every time token is identical. `allcontract_diffs.txt` normalises tags away and reports
   `(no normalized tradingHours change on any contract)` for 20240426072245 -> 20240605055619.
3. **20241007031911 -> 20250407083045** — the real move, spanning both circulars (section D).

## D. The 2024-11-04 Japan change (DT/AM 50 of 2024) — CONFIRMED, from SGX's own server

The content API is blind between 2024-10-07 and 2025-04-07, so the confirmation comes from the
server-rendered `www.sgx.com` product pages, which embed the same CMS `tradingHours.processed`
value in the page's JSON island. Each page carries an Akamai edge stamp `"ak.t":"<epoch>"` that
matches its Wayback capture instant to within 4 seconds, so the capture instant is corroborated by
the origin itself (checked for all 20 pages; see the list at the end of this file).

Files `raw_html_<ts>.html`; extraction in `extracted_ssr_tradinghours.json` via `extract_html.py`.
Archived URL form: `https://web.archive.org/web/<ts>id_/https://www.sgx.com/derivatives/products/<slug>[?cc=<code>]`

**BEFORE — 20241007180652** (ak.t 2024-10-07 18:06:52 UTC = 2024-10-08 02:06:52 SGT),
`https://web.archive.org/web/20241007180652id_/https://www.sgx.com/derivatives/products/nikkei225futuresoptions?cc=NK`

    SGX Nikkei 225 Index Futures
      T Session: ... Opening : 7.30 am - 2.25 pm ... Pre-Closing : 2.25 pm - 2.29 pm ... Non-Cancel : 2. 29 pm - 2.30 pm
      T+1 Session: Pre -Opening : 2.45 pm - 2.53 pm ... Non -Cancel : 2.53 pm - 2.55 pm ... Opening : 2.55 pm - 5.15 am
    SGX Nikkei 225 Index Options
      T Session: Order Cancellation : 7.15 am -7.30 am / Opening : 7.30 am - 2.30 pm
      T+1 Session: Order Cancellation : 2.45 pm - 2.55 pm / Opening : 2.55 pm - 5.15 am
    (SGX USD Nikkei 225 and SGX Mini Nikkei 225 identical to NK.)

**AFTER — 20241114152443** (ak.t 2024-11-14 15:24:43 UTC = 2024-11-14 23:24:43 SGT),
`https://web.archive.org/web/20241114152443id_/https://www.sgx.com/derivatives/products/nikkei225futuresoptions?cc=NU`

    SGX Nikkei 225 Index Futures, verbatim:
      <p dir="ltr">T Session:<br>Pre-Opening : 7.15 am - 7.28 am<br>Non-Cancel : 7.28 am - 7.30 am<br>Opening : 7.30 am - 2.55 pm<br>Pre-Closing : 2.55 pm - 2.59 pm<br>Non-Cancel : 2.59 pm - 3.00 pm</p>\n<p dir="ltr">&nbsp;</p>\n<p dir="ltr">T+1 Session:<br>Pre-Opening : 3.15 pm - 3.23 pm<br>Non-Cancel : 3.23 pm - 3.25 pm<br>Opening : 3.25 pm - 5.15 am<br>Pre-Closing : NA<br>Non-Cancel : NA</p>\n
    SGX Nikkei 225 Index Options, verbatim:
      <p>T Session:<br><br>Opening : 7.30 am - 3.00 pm</p>\n<p>&nbsp;</p>\n<p>T+1 Session:<br><br>Opening : 3.25 pm - 5.15 am</p>\n
    (SGX USD Nikkei 225 and SGX Mini Nikkei 225 carry the same revised strings.)

That is **exactly** DT/AM 50 of 2024's "Revised" column, routine by routine, including the separate
NKO row (T Opening 7.30 am -> 3.00 pm; T+1 3.25 pm). The change is bracketed by SGX-served pages
to 2024-10-08 SGT .. 2024-11-14 SGT, and the circular's stated Monday 4 November 2024 sits inside.
Corroborated again at **20250125201017** (ak.t 2025-01-25 20:10:17 UTC), identical strings.

**Non-Japan keys did NOT move at 2024-11-04**, as DT/AM 50 says (it names no China, Singapore,
Taiwan or NTR contract):

    Singapore  20241103233055 (ak.t 2024-11-03 23:30:54 UTC = 2024-11-04 07:30:54 SGT, i.e. the
               effective Monday itself) and 20241209080330 (2024-12-09 16:03:28 SGT)
               .../derivatives/products/sgxsimsci?cc=NSG  — SGP, CSGP, NSG and NSP strings are
               character-identical across the pair and identical to the 2020 payload.
    Taiwan     20240826132006, 20241117055357, 20241209075537  .../products/twnfc?cc=TWN
               — TWN and CTWN identical across all three.
    China      20240826131725 and 20250124141331  .../products/chinaa50?cc=CN — identical.

**AFTER DT/AM 15 — 20250407182010** (ak.t 2025-04-07 18:20:10 UTC = 2025-04-08 02:20:10 SGT),
`https://web.archive.org/web/20250407182010id_/https://www.sgx.com/derivatives/products/nikkei225futuresoptions?cc=NK`

    <p dir="ltr">T Session:<br>Pre-Opening : 7.15 am - 7.28 am<br>Non-Cancel : 7.28 am - 7.30 am<br>Opening : 7.30 am - 2.55 pm<br>Pre-Closing : 2.55 pm - 2.59 pm<br>Non-Cancel : 2.59 pm - 3.00 pm</p>\n<p dir="ltr">&nbsp;</p>\n<p dir="ltr">T+1 Session:<br>Pre-Opening : 3.05 pm - 3.08 pm<br>Non-Cancel : 3.08 pm - 3.10 pm<br>Opening : 3.10 pm - 5.15 am<br>Pre-Closing : NA<br>Non-Cancel : NA</p>\n

T is untouched (DT/AM 15: "no change to the T session trading hours") and still carries DT/AM 50's
revised values; only T+1 moves. The 20250407083045 content-api payload agrees for all five keys:
A50 T+1 4.40-4.43 / 4.43-4.45 / 4.45 pm; SGP 5:30-5:33 / 5:33-5:35 / 5:35 pm; TWN 1.55-1.58 /
1.58-2.00 / 2.00 pm; NSG 6.40-6.43 / 6.43-6.45 / 6.45 pm.

DATA-QUALITY NOTE, not a schedule fact: in the 20250407083045 payload the **NSP** row's T+1 reads
`Pre -Opening : 6.40 pm - 6.43 pm ... Non -Cancel :6.43 pm - 6.45 pm ... Opening : 7.00 pm - 5.15 am`
— SGX moved the routine but left the old 7.00 pm open in that one string. Its sibling NSG says
6.45 pm. Treat NSP's 7.00 pm as an SGX typo, not a divergence.

## E. The 2023-11-27 US SSF T+1 change — it touches NO equity-index routine

Bracketing captures 20230829130145 -> 20240207134658 (`allcontract_diffs.txt`, block at line 883):
the only session changes in the whole 71-contract payload are the US single-stock futures gaining
a T+1 session, and two India rows disappearing. Verbatim:

    Grab Futures [ZGRA]
      A (20230829130145): T Session only: Pre-opening 8:15 am - 8:28 am Non-Cancel: 8:28 am - 8:30 am Opening: 8:30 am - 8:20 pm Pre-Closing: 8:20 pm -8:24 pm Non-Cancel: 8:24 pm - 8:25 pm
      B (20240207134658): T Session: Pre-opening 8:15 am - 8:28 am Non-Cancel: 8:28 am - 8:30 am Opening: 8:30 am - 8:20 pm Pre-Closing: 8:20 pm -8:24 pm Non-Cancel: 8:24 pm - 8:25 pm  T+1 Session: Pre-Opening: 8:40 pm - 8:48 pm Non-Cancel: 8:48 pm - 8:50 pm Opening: 8:50 pm - 5:15 am
    TSMC ADR Futures [ZTSM] and SEA ADR Futures [ZSEA]: same new T+1 block.
    ("TSMC Futures"/"SEA Futures" are renamed to "... ADR Futures" in the same edit.)
    SGX Nifty 50 Index Futures [IN], SGX Nifty 50 Index Options [CIN], SGX Nifty Bank Index
    Futures [INB]: tradingHours -> null (the Nifty suite's retirement, unrelated).

**None of NK, CN, SGP, TWN, NSG or NSP appears in that diff block.** The CMS was demonstrably live
and edited in that window, so the negative is a real negative, not a stale payload.

Tightened with SGX-served pages on either side of 2023-11-27 (all four families, identical strings
to the 2020 payload):

    Nikkei     20231003195656 (ak.t 2023-10-03 19:56:54 UTC) -> 20231203010708 (2023-12-03 01:07:06 UTC)
               .../products/nikkei225futuresoptions[?cc=CNK]  — NK still 7.30 am - 2.25 pm /
               2.45-2.53 / 2.53-2.55 / 2.55 pm - 5.15 am after the date. NKO unchanged.
    China A50  20231003213014 -> 20231203005356  .../products/chinaa50[?cc=CN] — identical.
    Singapore  20231003051530 -> 20231206120158  .../products/sgxsimsci?cc=SGP — SGP and NSG identical.
    Taiwan     20230930071559 -> 20240209051137  .../products/twnfc?cc=TWN — identical.

## F. Akamai origin stamps vs Wayback capture instants (all SSR pages)

    capture ts        cdx (UTC)              ak.t (UTC)             delta
    20230930071559    2023-09-30 07:15:59    2023-09-30 07:15:57    -2s
    20231003051530    2023-10-03 05:15:30    2023-10-03 05:15:27    -3s
    20231003195656    2023-10-03 19:56:56    2023-10-03 19:56:54    -2s
    20231003213014    2023-10-03 21:30:14    2023-10-03 21:30:13    -1s
    20231203005356    2023-12-03 00:53:56    2023-12-03 00:53:54    -2s
    20231203010708    2023-12-03 01:07:08    2023-12-03 01:07:06    -2s
    20231206120158    2023-12-06 12:01:58    2023-12-06 12:01:54    -4s
    20240209051137    2024-02-09 05:11:37    2024-02-09 05:11:37     0s
    20240826131725    2024-08-26 13:17:25    2024-08-26 13:17:25     0s
    20240826132006    2024-08-26 13:20:06    2024-08-26 13:20:06     0s
    20240826132436    2024-08-26 13:24:36    2024-08-26 13:24:36     0s
    20241007180652    2024-10-07 18:06:52    2024-10-07 18:06:52     0s
    20241103233055    2024-11-03 23:30:55    2024-11-03 23:30:54    -1s
    20241114152443    2024-11-14 15:24:43    2024-11-14 15:24:43     0s
    20241117055357    2024-11-17 05:53:57    2024-11-17 05:53:57     0s
    20241209075537    2024-12-09 07:55:37    2024-12-09 07:55:34    -3s
    20241209080330    2024-12-09 08:03:30    2024-12-09 08:03:28    -2s
    20250124141331    2025-01-24 14:13:31    2025-01-24 14:13:30    -1s
    20250125201017    2025-01-25 20:10:17    2025-01-25 20:10:17     0s
    20250407182010    2025-04-07 18:20:10    2025-04-07 18:20:10     0s

## G. Scripts

`fetch.py` (retrieval with backoff), `decode.py` (gzip -> json), `extract.py` (five keys + change
log -> `diffs.txt`), `extract_html.py` (SSR pages -> `extracted_ssr_tradinghours.json`).
The all-contract diff in `allcontract_diffs.txt` was produced by the inline script recorded in the
session; it strips tags and collapses whitespace before comparing, so it reports only real time
changes.

## H. What this does and does not license

- It **does** license deleting the "(#64)" carry-forward caveat's uncertainty for 2021-2024: the
  routines are now witnessed, per half-year, in SGX's own payloads, unchanged.
- It **does** give SGX-served corroboration of DT/AM 50 of 2024 — until now only a Fubon mirror —
  including its NKO row, bracketed 2024-10-08 SGT .. 2024-11-14 SGT.
- It **does not** state a day. No artifact here says "with effect from"; the day still comes from
  DT/AM 50 itself. Under LAW-NO-FABRICATED-DATES the row's date remains the circular's.
- It **does** answer the US SSF question: the 2023-11-27 change is visible in SGX's payload and
  touches only ZGRA / ZSEA / ZTSM. No equity-index routine moves.
