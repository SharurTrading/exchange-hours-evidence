# INDEX — task cme-2022-2024, FIX round 1

All artifacts in this directory were retrieved on **2026-09-12 (UTC)** by the fixer for task `cme-2022-2024`,
in response to the verifier's FAIL verdict in `holidays/cme-2022-2024.verify.json`.

`cmegroup.com` answers 403 to this machine, so every operator document was read through the Wayback Machine's
verbatim `id_` raw replay of the operator's own bytes. `capture` is the Wayback capture timestamp (UTC). The
operator URL in the `source url` column is the exact archived original, cache-buster `_t` included — replay it
as `https://web.archive.org/web/<capture-timestamp>id_/<source url>`.

The channel is CME Group's own trading-hours service, `GET /services/trading-hours-by-product`, requested by
cmegroup.com's trading-hours widget for the ten representative products it shows
(`id=316,133,425,300,58,437,22,8478,5201,10191` = ZN, ES, CL, ZC, 6E, GC, LE, BTC, CSC, LBR). It is the
operator's own machine channel read as bytes and saved, i.e. **tier T2** under LAW-PRIMARY-SOURCES.

## 1. Recovered T2 windows — the six 2024 holidays round 0 declared unsourced (discrepancy D1)

Capture instant for all six: **2024-07-08T16:14:39Z** (`20240708161439`), the same crawl instant that produced
the already-accepted `api_2024-09-01.json` and `api_2024-11-27.json`. All six carry `"hasEvents": true`.

| file | sha256 | bytes | source url | capture (UTC) | what it is |
|---|---|---|---|---|---|
| `api_2024-01-14.json` | `a8fe0f3eed4c67939d3add5fa656173bc4119c3765174b084c0622a1934e0d22` | 8856 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2024-01-14&toEventDate=2024-01-16&isProtected&_t=1720455278663 | 2024-07-08T16:14:39Z | T2 window 14–16 Jan 2024. Sources the **2024-01-15 Dr. Martin Luther King, Jr. Day** rows. |
| `api_2024-02-18.json` | `af5ddb57cfa8bd6d377a0784fcdd33589e2055ede0a09b7fe4ae3e41d0d20f9a` | 8856 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2024-02-18&toEventDate=2024-02-20&isProtected&_t=1720455278669 | 2024-07-08T16:14:39Z | T2 window 18–20 Feb 2024. Sources the **2024-02-19 Presidents Day** rows. |
| `api_2024-03-28.json` | `9b41709219e36f56296843fe589e362a7513e9a98132a682a1b956f2e40c593b` | 5550 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2024-03-28&toEventDate=2024-03-30&isProtected&_t=1720455278672 | 2024-07-08T16:14:39Z | T2 window 28–30 Mar 2024. Sources the **2024-03-29 Good Friday** rows: all ten products have empty event arrays on 29 and 30 March, and 28 March ends at its final close with no evening reopen (CSC prints `13:55 closed`). |
| `api_2024-05-26.json` | `ccff9685aac5670c5eb4a7e2b86cf1d78a5c2c08325cd03673ab8c1e6f560138` | 8856 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2024-05-26&toEventDate=2024-05-28&isProtected&_t=1720455278675 | 2024-07-08T16:14:39Z | T2 window 26–28 May 2024. Sources the **2024-05-27 Memorial Day** rows. |
| `api_2024-06-18.json` | `57acecac3e1ad1a50dda8e3bcd6ca926b4d4c6c2ebc9d8324eb73332ed6a20ec` | 10517 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2024-06-18&toEventDate=2024-06-20&isProtected&_t=1720455278677 | 2024-07-08T16:14:39Z | T2 window 18–20 Jun 2024. Sources the **2024-06-19 Juneteenth** rows; 18 June prints each group's ordinary final close with the evening reopen carrying `tradingDate 2024-06-20`. |
| `api_2024-07-03.json` | `6ef0e2b055c349249f5cc7ea7c98132a31111a01ce7af028e13584c0f82d4d38` | 9083 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2024-07-03&toEventDate=2024-07-05&isProtected&_t=1720455278680 | 2024-07-08T16:14:39Z | T2 window 3–5 Jul 2024. Sources both the **2024-07-03 Independence Day eve** rows (ES prints `12:15 closed` for trade date 3 July while ZN/CL/GC/6E/BTC/CSC print their ordinary `16:00 closed`) and the **2024-07-04 Independence Day** rows. |

## 2. Negative and boundary controls — what the T2 channel really does

Round 0 asserted that the service "returns `hasEvents:false` with empty event arrays for dates already past".
That is false, and the files below establish the true behaviour: the service serves a **rolling window of recent
history**, which at the 2024-07-08 crawl reached back roughly seven months. Every 2024 U.S. holiday is therefore
recoverable from that crawl; the January–April 2023 holidays are not.

| file | sha256 | bytes | source url | capture (UTC) | what it is |
|---|---|---|---|---|---|
| `neg_api_2023-01-15.json` | `507fd196a7654ddd916218b2aa24a146eeaca4e1f7cb7daded4e7a9c689cda82` | 3898 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2023-01-15&toEventDate=2023-01-17&isProtected&_t=1720455278636 | 2024-07-08T16:14:38Z | `"hasEvents": false`, all ten products' event arrays empty. Confirms the **2023-01-16 MLK** gap is genuine in this channel. |
| `neg_api_2023-02-19.json` | `d063238a83e8cb84d4484a86b26cb1d976f1ccfdb91972eecc08dcc0cec49412` | 3898 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2023-02-19&toEventDate=2023-02-21&isProtected&_t=1720455278640 | 2024-07-08T16:14:38Z | `"hasEvents": false`, all arrays empty. Confirms the **2023-02-20 Presidents Day** gap. |
| `neg_api_2023-04-06.json` | `0543d5f6d2efd4aa6f4132ce9f5425b9ba9f64de08eccd677b78d6b43c6e9d4f` | 3898 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2023-04-06&toEventDate=2023-04-08&isProtected&_t=1720455278642 | 2024-07-08T16:14:38Z | `"hasEvents": false`, all arrays empty. Confirms the **2023-04-07 Good Friday** gap. |
| `probe_2023-05-28.json` | `7d8a5f8b6ef7370c7e1aedceccee3d9a0bcc10c5d91df4c0159b9aa80faa4d94` | 3898 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2023-05-28&toEventDate=2023-05-30&isProtected&_t=1720455278644 | 2024-07-08T16:14:38Z | Lower boundary probe: `"hasEvents": false`. The 2024-07-08 crawl does **not** reach May 2023. |
| `probe_2023-12-24.json` | `8d379b7764c3b3cf084f86ef393bc78fb80fbd2e9c2cd6a7f00cd280838582b6` | 7732 | https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2023-12-24&toEventDate=2023-12-26&isProtected&_t=1720455278659 | 2024-07-08T16:14:39Z | Upper boundary probe: `"hasEvents": true`, fully populated. The same crawl **does** reach December 2023, which is what rules out "empty because past". Not used to source any row (2023-12-25 is already T1 from `christmas-day-2023.pdf`). |

| file | sha256 | bytes | what it is |
|---|---|---|---|
| `urls.txt` | `4f1fea2623d2624a5404c29b0928e78eb316b072a68f7e647e4827c8f0abef86` | 1530 | The fetch list actually used for section 1: `outname|wayback-timestamp|archived original url`, one line per file. Kept so a reader can re-issue the six replays verbatim. |

## 3. No new bytes were needed for discrepancy D2

D2 (four verbatims quoting a `TRADE DATE` label out of a cell that is empty) was settled by re-reading artifacts
already saved in `raw/cme-2022-2024/`, not by retrieval. The re-read was done with
`pdftotext -bbox-layout <file>.pdf` and the column x-origins read off the header row:

* `christmas-day-2023.pdf` — `MONDAY, 25 DECEMBER 2023` column head at x=196.8, its time events at x=209.6;
  `TUESDAY, 26 DECEMBER 2023` at x=470.7 / 483.5. The Monday column carries text at the INTEREST RATE (y=398.4),
  EQUITIES (476.8), ENERGY (556.5), FX (777.5), METALS (858.2), CRYPTOCURRENCIES (1022.4) and DAIRY (1100.6)
  rows, and **nothing at all** at GRAINS (row label y=680.6), LIVESTOCK (954.1) or LUMBER (1179.9).
* `new-years-day-2024.pdf` — `MONDAY, 1 JANUARY 2024` at x=226.4 / 239.2, `TUESDAY, 2 JANUARY 2024` at
  x=471.4 / 484.1. Monday entries at INTEREST RATE (y=390.4), EQUITIES (468.8), ENERGY (548.5), FX (769.5),
  METALS (850.2), CRYPTOCURRENCIES (1014.4), DAIRY (1092.6); **nothing** at GRAINS (672.6), LIVESTOCK (946.1)
  or LUMBER (1171.9).
* `thanksgiving-day-2023.pdf` — columns at x=171/183.7 (Wed 22 Nov), x=392.7/405.5 (Thu 23 Nov),
  x=584.2/597.0 (Fri 24 Nov). The CRYPTOCURRENCIES Thursday cell **does** carry `TRADE DATE: FRI 24 NOV`
  (y=1032.6, x=392.7), which the round-0 verbatim omitted; unlike the INTEREST RATE / EQUITIES / ENERGY / FX /
  METALS cells it prints `16:00 (PREOPEN)` with no trailing `HALT`.

## 4. Addendum — `raw/cme-2022-2024/INDEX.md` completeness (discrepancy D4)

The round-0 INDEX omitted twelve files and left two rows without a URL or description. Those files stay where
they are; this section supplies the missing sha256, byte length and description so every saved artifact in that
directory has an INDEX row somewhere.

### 4a. The two rows the round-0 INDEX left as `(unlisted)`

Both are Wayback CDX index responses fetched live on 2026-09-12; the query that reproduces each row set is given
so a reader can re-issue it.

| file | sha256 | bytes | reproducing query | what it is |
|---|---|---|---|---|
| `cdx_47e9ad.json` | `2dee06594369a62381e72beec878dc0af20ab305738fec34249e32d4c3c67463` | 5104 | `https://web.archive.org/cdx/search/cdx?url=https://www.cmegroup.com/trading-hours/files/*&output=json&fl=timestamp,original,statuscode,mimetype,length` | 42 CDX rows over `cmegroup.com/trading-hours/files/` — the holiday one-pager tree. Contains the 200s for the six 2023 one-pagers (`memorial-day-2023`, `juneteenth-2023`, `4th-of-july-2023`, `labor-day-2023`, `thanksgiving-day-2023`, `christmas-day-2023`) plus `new-years-day-2024.pdf`, and the 404s for `mlk-day-2023/2024/2025`, `martin-luther-king-day-2023`, `martin-luther-king-jr-day-2023/2024/2025`, `presidents-day-2024/2025`, `good-friday-2023/2024/2025`, `memorial-day-2024/2025`, `juneteenth-2024/2025`, `4th-of-july-2024/2025`, `independence-day-2024/2025`, `labor-day-2024`, `thanksgiving-day-2024/2025`, `christmas-day-2024/2025`, `new-years-day-2025`. This is the file behind the claim that CME published no 2024 one-pagers after New Year's Day. |
| `cdx_f98105.json` | `961d763aeed79a75b34c5893e7eac057d06cbd9aa87ac6e153a96a246a95a55f` | 1423 | `https://web.archive.org/cdx/search/cdx?url=https://www.cmegroup.com/content/dam/cmegroup/trading-hours/files/day-of-mourning-january-9-2024.pdf&output=json&fl=timestamp,original,statuscode,mimetype,length` | 8 CDX rows, all for `content/dam/cmegroup/trading-hours/files/day-of-mourning-january-9-2024.pdf` (captures 2025-01-14 … 2025-06-05). CME's filename says 2024 but every capture is 2025; the document is the National Day of Mourning schedule for **9 January 2025**, which is outside this task's 2022–2024 scope. Recorded here so the file is accounted for, and flagged for whoever holds `cme-2025-2027`. |

### 4b. Helper scripts and derived copies (not operator artifacts)

Nothing in the result is sourced from these; they are the working tools and gunzipped copies kept for
reproducibility.

| file | sha256 | bytes | what it is |
|---|---|---|---|
| `fetch.sh` | `cf5b4b3177611fa470fda35cb527887f0f8a5738659c4cb64fa5962e76e5a444` | 1004 | Helper: `fetch.sh <outname> <url>` — live fetch into `raw/cme-2022-2024/`. |
| `wb.sh` | `735f4b4d7c7ee955c217d99a28537d05fb7f9199301d1c969f554c1f56e33ef8` | 566 | Helper: `wb.sh <outfile> <timestamp> <url>` — Wayback `id_` replay fetch. |
| `dumpapi.py` | `16b5fa752ffc7716dc119486a136115766b9303de45766195b70dc0bcfa7a568` | 699 | Helper: prints a trading-hours-service JSON as `product / eventDate / events`. |
| `dumpxls.py` | `bfc8cd2fda254c187c7f2ec52c25a234004d47f0f3000123f5c383886763f894` | 505 | Helper: dumps every sheet of a `.xls` cell by cell via `xlrd`. |
| `dumpxls2.py` | `348e3f2ff8bb3e81552f0f6b1bb881a48edd2535f905622b357368822613b627` | 754 | Helper: same, with Excel serial times decoded to `HH:MM`. |
| `pdfcols.py` | `7204786921be03274a97d81c4dbc782da1aba896216f902cb75d8d59da1a045b` | 1541 | Helper: column-aware extraction of the 2023/2024 one-pagers by product-group row label. |
| `x22.py` | `12e3475ebd4e90b64eede50a5c335a508110953f53435d422c32573eb4040236` | 1496 | Helper: extracts the named 2022-sheet product-group rows. |
| `page_20230116.plain.html` | `2917984167c50c026062068a5301e524565e32541ec5ed0b8b79bb3acbc18a9a` | 138297 | Derived copy of `page_20230116.html` (identical sha256 — the response was not gzipped). |
| `page_20231203.plain.html` | `194f85a1676f6e6fba7b3c9681ffdead8803b3ddbdf368d043d2939a8546c7b3` | 214962 | Derived copy of `page_20231203.html` (identical sha256). |
| `page_20240115.plain.html` | `00a0314cfb181e362e4fd2d4912eed692cae91e5a2fbc020a440ed15abb28032` | 184335 | **Gunzipped** copy of `page_20240115.html` (28437 bytes gzip). Same operator bytes, decompressed for reading. |
| `th_20240526.plain.html` | `14d476443bc14a4c1a3f4c2969f2008363fb4017e7a5b51c96f1722872ad2403` | 240978 | Derived copy of `th_20240526.html` (identical sha256). |
| `trading-hours.plain.js` | `d5a9e0bfd0cf54f81adaf86a36ece1d4a1a87a61acf4878d2c9650089ac000c8` | 58233 | **Gunzipped** copy of `trading-hours.js` (12233 bytes gzip); this is where the `/services/trading-hours-by-product` endpoint and its `id=` list are read from. |

## 5. Round-0 channel-table correction

`raw/cme-2022-2024/INDEX.md` states, in its channel notes, that "The service returns `hasEvents:false` with empty
event arrays for dates already past, so only Wayback captures taken before a holiday carry data." **That sentence
is wrong** and is superseded by section 2 above: the service serves a rolling history window, and the 2024-07-08
crawl carries full events for every 2024 window and for 2023-12-24. The round-0 INDEX is left unedited as the
round-0 record; this file is the correction.
