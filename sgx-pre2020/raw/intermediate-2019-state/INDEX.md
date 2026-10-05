# Channel `intermediate-2019-state` — raw retrievals

Retrieved 2026-09-06. Remit: the intermediate **04:45 T+1 close** state, and anything
else SGX published in 2019. Only SGX-authored hosts (`sgx.com`, `api2.sgx.com`, the
archived `wps/wcm` portal) count as sources here.

## Headline

Two SGX-hosted channels carry the 04:45 grid, and **both are SGX's own**:

1. The **Derivatives Trading Calendar PDFs**, still **live** on `api2.sgx.com` at
   their original URLs (they are NOT in the Wayback Machine — see "Negatives").
2. The **`api2.sgx.com/content-api` `derivatives_products_list` GraphQL response**
   that backs the `www2.sgx.com/derivatives/products/*` pages. This is the per-contract
   product page data, and unlike the calendar it prints the **full session-state
   breakdown** (Pre-Opening / Non-Cancel / Opening / Pre-Closing / Non-Cancel).
   The Wayback Machine holds three usable captures of it: 2019-02-04, 2019-06-11
   (revisited identical 2019-06-21) and 2020-01-09.

The 04:45 state is **not one grid — it is two**, differing only in MSCI Singapore.

## Files

### Live retrievals from api2.sgx.com (not archived anywhere; capture = LIVE 2026-09-06)

| file | what it is |
| --- | --- |
| `live_2019-DT-Calendar_api2.pdf` / `.txt` | **SGX Derivatives Market Trading Calendar 2019.** `https://api2.sgx.com/sites/default/files/2019-01/2019%20DT%20Calendar.pdf`. Document says "All dates and information are accurate as of 15 January 2019." PDF CreationDate 2019-01-22, ModDate 2019-01-23; HTTP `last-modified: Wed, 23 Jan 2019 01:30:19 GMT`. sha256 `4ea3ba47…5877797` — byte-identical to the prior sweep's `../../artifacts/cal2019.pdf`, so that file's provenance is now nailed down. **T+1 close 4.45am throughout.** |
| `boundary_2018-Apr-Calendar_api2.pdf` / `.txt` | **SGX Derivatives Market Trading Calendar 2018 (Apr).** `https://api2.sgx.com/sites/default/files/2018-05/SGX%20Derivatives%20Trading%20Calendar%202018%20(Apr).pdf`. Document says "accurate as of 26 December 2017"; PDF CreationDate 2018-04-11; HTTP `last-modified: Mon, 21 May 2018 10:17:04 GMT`. Fetched as the **lower bound** on the 04:45 state. **Already 4.45am, with the identical five-family grid as the 2019 edition.** |

### Wayback replays of SGX's own content API (`id_` raw form)

| file | capture | what it shows |
| --- | --- | --- |
| `contentapi_derivatives_products_list_20190204200905.json` | 2019-02-04 20:09:05 | 42 products / 226 contracts. **04:45. SiMSCI 8:30–5:10 pm / 5:40 pm–4:45 am.** |
| `contentapi_derivatives_products_list_20190611051800.json` | 2019-06-11 05:18:00 | 46 products / 232 contracts. **04:45. SiMSCI 8:30–5:20 pm / 5:50 pm–4:45 am** — the SiMSCI grid has moved. |
| `contentapi_derivatives_products_list_20190621080419.json` | 2019-06-21 08:04:19 | Wayback revisit record. sha256 identical to the 2019-06-11 file (`5fbc896e…045e5fe`) — same bytes, so it extends the witness of that state by ten days without being new evidence. |
| `contentapi_derivatives_products_list_20200109051211.json` | 2020-01-09 05:12:11 | 47 products / 243 contracts. **05:15** — first SGX-hosted capture of the post-change close. Upper bound. |
| `contentapi_chinaa50_20190116144725.json` | 2019-01-16 14:47:25 | Single-product page payload for `/derivatives/products/chinaa50`. **A50 T+1 Opening 5.00 pm – 4.45 am.** Only per-product page capture in the era. |

### Wayback replays of the product pages themselves (SPA shells — no hours in the HTML)

`prod_chinaa50_20190116144452.html`, `prod_nikkei225_20190922123749.html`,
`prod_sgxsimsci_20190930120921.html`. Kept to document that the September 2019 page
captures exist but are **empty React shells** — their backing `content-api` calls were
not archived, which is why there is no SGX witness between 2019-06-21 and 2020-01-09.

### Derived, verbatim

- `grids_calendars.txt` — the two calendars' matching rows and footnotes, verbatim.
- `grids_20190204.txt`, `grids_20190611.txt`, `grids_20200109.txt` — the five families
  pulled from each API capture, verbatim (`extract.py` produces these).
- `extract.py` — the extractor. Handles both `title` (Feb 2019) and `name` (later) keys.

### CDX enumerations (evidence for the negatives)

`cdx_api2_2019.json` (empty), `cdx_api2_all.json`, `cdx_contentapi.txt`,
`cdx_sgxcom_2019.txt`, `cdx_products.txt`, `cdx_trading_page.txt`,
`cdx_www2_derivatives.json`, `cdx_oldportal*.txt`.

## Negatives established (not assumed — each has a CDX file behind it)

- **The 2019 Derivatives Trading Calendar is genuinely absent from the Wayback Machine.**
  `url=api2.sgx.com/sites/default/files/2019*&matchType=prefix` returns `[]`; the
  `2019-01` folder prefix returns ~200 rows and **no** `2019 DT Calendar.pdf`. The repo's
  belief that "no pre-2020 calendar survives" is **half right and materially wrong**: it
  is un-archived, but it is **still live at its original SGX URL** and was retrieved today.
- **No capture of any SGX hours surface between 2019-06-21 and 2020-01-09.** The
  `content-api` CDX has nothing product-related in that window; `www2.sgx.com/derivatives/trading`
  (the page the 2019 calendar's own footnote cites) has **no capture before 2020-08-03**.
  So the 04:45 → 05:15 changeover is not witnessed by any SGX artifact on either side within
  six months, and this channel cannot narrow it.
- No 2019 calendar under any other probed filename on api2 (`2019-02`, `2019-06`, `2019-11`,
  `2019-12`, `SGX Derivatives Trading Calendar 2019.pdf`, `_0.pdf` — all 404).

## Source anomalies — reported, not corrected

1. **The 2019 calendar prints "4.45pm" on three NTR (USD) rows** (MSCI Philippines,
   MSCI Malaysia, MSCI Thailand): "7.25am to 6.30pm / 7.00pm to **4.45pm**". The same three
   contracts print "Opening: 7:00 pm - 4:45 **am**" on SGX's own product API four months later
   (2019-06-11), and the 2018 calendar contains no "4.45pm" anywhere. It reads as a typo
   introduced in the 2019 edition, but it is quoted as printed. It does **not** touch the
   Singapore or Taiwan NTR rows.
2. **The 2018-07-11 portal page conflicts with SGX's own calendar over the same period.**
   That portal capture prints T+1 close **2.00 am** and Nikkei T open **7.45 am**; the
   2018 (Apr) calendar — authored 2018-04-11, served from 2018-05-21, three months *earlier* —
   prints **4.45 am** and **7.30 am**. Two SGX artifacts, overlapping in time, disagree. This
   channel records both and reconciles neither. (The portal page is the `portal-hours-page`
   channel's remit.)
3. The SiMSCI contract is named **"SGX MSCI Singapore Free Index Futures"** (code SGP)
   throughout 2018–2019 and is renamed **"SGX MSCI Singapore Index Futures"** by the 2020
   calendar. Same code, same product.

## Reading the CDX files

A **zero-byte `.txt`** or a **`[]` `.json`** is a *successful* query that matched nothing —
those are the negatives above, not failed fetches. Every fetch in this directory was
retried with backoff until it returned; Wayback 504'd repeatedly during the session and
one query (the exact-URL form for the 2019 calendar) never returned, but the `2019-01`
folder-prefix query did and answers the same question.

## The two 04:45 grids, side by side (five modelled families)

| | State A | State B |
| --- | --- | --- |
| witnessed | 2018 (Apr) cal · 2019 cal · 2019-02-04 API | 2019-06-11 API (= 2019-06-21) |
| Nikkei 225 F | 7.30am to 2.25pm / 2.55pm to 4.45am | same |
| FTSE China A50 F | 9.00am to 4.30pm / 5.00pm to 4.45am | same |
| MSCI Singapore Free F | 8.30am to 5.10pm / 5.40pm to 4.45am | **8:30 am - 5:20 pm / 5:50 pm - 4:45 am** |
| MSCI Taiwan F | 8.45am to 1.45pm / 2.15pm to 4.45am | same |
| MSCI Singapore Free NTR (USD) F | 7.25am to 6.30pm / 7.00pm to 4.45am | same |

State A → State B is a **SiMSCI-only** change. State B → the 2020 grid is a
**T+1-close-only** change (4.45am → 5.15am), uniform across all six families.
Neither changeover day is stated by any artifact in this channel, and none is inferred.
