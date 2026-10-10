# INDEX — `iceus-notices-service-2026-10-09` (the ICE notices listing service sweep)

Retrieval session: **2026-10-09 23:48–23:56 UTC** (`date -u`). All times UTC (LAW-UTC-DATES).

The ICE Futures U.S. notices page (`https://www.ice.com/futures-us/notices`) renders client-side
from the operator's own listing service. The backing endpoint, read out of the page's JS bundle
(`static.ice.com/cms/41.10.18/chunks/...`, `buildUrl` of the `cms-component-report` config and
`Sn = r => "/api/sitesearchservice/v1" + r`), is:

    POST https://www.ice.com/api/sitesearchservice/v1/search/websitenotices?searchCollections=futures_us_exchange_notice&year=<YYYY>&max=<n>&offset=0&pageNumber=1

with header `Accept: application/json`; plain curl with a browser UA answers. This is the operator's
own machine channel (T2), and it reaches the whole back catalogue the page's default view never
showed: 188 exchange notices for 2025, 244 for 2024, 122 for 2026 (as of the capture). The prior
waves' closing condition for #168 — "page 2+ of the paginated report" — is this endpoint, and it
names every notice the Wayback CDX prefix enumeration could not.

## A. Primary documents (T1, retrieved live from the operator)

| # | File | URL | Retrieved (UTC) | sha256 | Bytes | Contents |
|---|---|---|---|---|---|---|
| A1 | `ICE_Futures_US_2025_IndDayHoliday_20250508.pdf` | https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_2025_IndDayHoliday_20250508.pdf | 2026-10-09 23:49:05 | `74b89e65fd51405d0df0fc4809785e470f8ed2823c18bd119fe6fd21d637cbe2` | 131308 | **2025 Independence Day Trading Schedule**, dated MAY 8, 2025. Thu July 3: softs/FCOJ/Canola/Gold-Silver/energy Regular; U.S. Dollar Index Regular; MSCI Index and “NYSE FANG+TM Index and ICE Stock, Mortgage and SOFR Index Contracts” **Early Close - 1:15 pm** (TAS ends 1:00 pm). Fri July 4: softs group **Closed**; U.S. Dollar Index **Early Close – 1:00 pm**; MSCI and FANG+ bullet **Early Close – 1:00 pm**. Mon July 7: **Late Open for Cotton: 8:00 am**, regular open/close for everything else. |
| A2 | `ICE_Futures_US_2025_Christmas_Holiday_20251031.pdf` | https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_2025_Christmas_Holiday_20251031.pdf | 2026-10-09 23:49:10 | `b5e92b1abf47947bef85e290f2efc16c9fcd9288ce40830d293c71aca1007809` | 160135 | **2025 Christmas Holiday Trading Schedule**, dated October 31, 2025. Wed Dec 24: **Early Close at 1:05 pm** for Cotton, Coffee “C”, Cocoa and FCOJ (TAS Cotton/FCOJ ends 1:00 pm), **Regular Close for Sugar 11 and 16**; “MSCI Stock Index, NYSE FANG+TM Index, and ICE Stock Index Contracts” **Early Close at 1:15 pm**; U.S. Dollar Index **Early Close at 1:45 pm**; Post-Close Pre-Open order entry starts 30 min after each close and ends 3:30 pm. Thu Dec 25: **Closed**. Fri Dec 26: **Late Open 7:30 am** for Coffee “C”, Cocoa, Cotton No. 2 and Sugar 11; regular open for FCOJ and Sugar 16; regular close for all; MSCI/FANG+ and Dollar Index bullets **Regular Hours**. |
| A3 | `ICE_Futures_US_2026_MLKDay_Holiday_20251203.pdf` | https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_2026_MLKDay_Holiday_20251203.pdf | 2026-10-09 23:49:15 | `1cab5d8d23084cce002098769fa472aa8795bd410fc30a2e43850ec319030780` | 126216 | **2026 Martin Luther King Day Holiday Trading Schedule**, dated December 3, 2025. Mon Jan 19: softs group **Closed**; MSCI Stock Index **Early Close – 1:00 pm**; “NYSE Stock Index, MSCI Bond Index, and ICE Mortgage, Bond Index and SOFR Index Contracts” **Early Close – 1:00 pm**; **U.S. Dollar Index “Regular Hours, TAS trading will not be held”** (TAS suspension, not a session boundary). The `iceus` 2026 evidence previously recorded “no 2026 MLK Exchange Notice exists” — this notice falsifies that. |
| A4 | `ICE_Futures_US_2026_Presidents_Day_Holiday_20251223.pdf` | https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_2026_Presidents_Day_Holiday_20251223.pdf | 2026-10-09 23:49:20 | `961d3a35f54f13477ab927610e75e445cc9acefa2c3dd2d7b5340f0a9080e76b` | 124860 | **2026 Presidents Day Holiday Trading Schedule** (and Louis Riel), dated December 23, 2025. Mon Feb 16: softs + Canola **Closed**; MSCI Stock Index **Early Close – 1:00 pm**; “NYSE Stock Index, MSCI Bond Index, and ICE Mortgage, Bond Index, SOFR Index and FTSE Stock Index Contracts” **Early Close – 1:00 pm**; U.S. Dollar Index “Regular Hours, TAS trading will not be held”. Falsifies the earlier “no 2026 Presidents Day Exchange Notice exists” record. |

The `.txt` beside each PDF is `pdftotext -layout` extraction (extraction time 2026-10-09 ~23:50 UTC,
not a second retrieval).

Also re-retrieved byte-for-byte and **not** duplicated here: `ICE_Futures_US_Juneteenth_2026_Notice_20260320.pdf`
(live, 2026-10-09 23:49 UTC) hashes `6f07e49c36c70ef0c81cf028c3c7f539339b03092c81b22cf9c583f9f0c6b9e2`,
byte-identical to the copy the store already holds at
`holidays/raw/cfe-eurex-ice-cde-smfe-2026-2027/` — it is last-trade-day / final-settlement content only
(LAW-SESSION-NOT-EXPIRY, keys nothing), and the byte match validates the live retrieval channel.

## B. The T2 listing captures

| # | File | URL / provenance | Captured (UTC) | sha256 | Bytes | Contents |
|---|---|---|---|---|---|---|
| B1 | `listing_2024.json` | POST `.../search/websitenotices?searchCollections=futures_us_exchange_notice&year=2024&max=200&offset=0&pageNumber=1` | 2026-10-09 23:48:52 | `d4015c17398e3f604c82eb210abd3e3f708b5ce7b7251defb0e2f316617b763c` | 64881 | `totalCount` 244, first 200 results. |
| B2 | `listing_2025.json` | same, `year=2025` | 2026-10-09 23:48:44 | `979200252af5011b6b58a231633706a9a96e53924bda65dac1215ee4336df013` | 62001 | `totalCount` 188, complete. Names A1 (pubDate May 8 2025) and A2 (pubDate Oct 31 2025) with their live URLs. |
| B3 | `listing_2026.json` | same, `year=2026` | 2026-10-09 23:48:57 | `f537c8f77863e5ccfacfea9dec62218eeb72f2801a1fdbaa84bb4b3534276280` | 39126 | `totalCount` 122, complete. Latest notice Oct 5 2026; **no 2026 Christmas/Boxing Day notice has issued** as of the capture, so the 2026-12-28 `open1` marker stays open. |

The `cdx/` subdirectory is empty — no archive artifacts were needed this time; the operator's own
service answered.
