# lse — CDX retry sweep, 2026-09-29 UTC (issue #218)

Domain-wide and prefix Wayback CDX sweeps re-run after the CDX service
recovered (the 2026-09-29 morning session had recorded "service unavailable"
caveats). Every file is the verbatim CDX JSON response saved at retrieval.

| File | Query | Result |
|---|---|---|
| `cdx_lse_trade_busdays.json` | exact URL `londonstockexchange.com/trade/trading-access/business-days`, all captures | 26 captures; earliest 2020-07-31, latest 2026-03-15. No capture inside 2020-01-01..2020-05-25. |
| `cdx_lse_trade_business.json` | prefix `londonstockexchange.com/trade/` 2019-2020, urlkey `.*business.*`, collapsed | 4 rows; only the business-days page and a 2019 education-page 301. |
| `cdx_lse_ps_busdays_all.json` | prefix `londonstockexchange.com/products-and-services/trading-services/business-days`, all captures | 78 rows. The `.htm` form's last 200 is 2014-02-09; 404s 2015-07-08..2017-12-16; 301s 2018-07-07..2020-06-09. No 2015-2019 200. |
| `cdx_lse_ate_business.json` | prefix `about-the-exchange` 2014-2019, urlkey `.*business.*` | last 200 2014-01-15; 404 2014-02-26. |
| `cdx_lse_products-and-services_business.json` | prefix `products-and-services` 2014-2020, urlkey `.*business.*`, 200s only | 4 rows, all 2014 except a 2019 XLS. |
| `cdx_lse_traders-and-brokers_business.json` | prefix `traders-and-brokers` 2014-2020, same filter | 1 row (2015 education page). |
| `cdx_lse_news_business.json` | prefix `news` 2014-2020, same filter | RNS articles only, all SPA-era 2020. |
| `cdx_lse_docs.json` | domain `docs.londonstockexchange.com` 2014-2020, collapsed | 954 url keys; no holiday/business-days document (images and 2020+ assets only). |
| `cdx_lseg_domain.json` | domain `lseg.com` 2014-2021, collapsed, limit 5000 | 5000 url keys; no exchange business-days page (Academy course calendars and `www2.lseg.com` analytics beacons only). |
| `cdx_lse_api.json` + `cdx_lse_api_pages.json` | domain `api.londonstockexchange.com` / prefix `api/v1/pages` | business-days API captures are exactly the four known (2024-02-07, 2024-03-08, 2025-12-18, 2026-06-17); nothing inside the 2025-01-02..2025-12-17 gap. |
| `cdx_lse_business.json`, `cdx_lse_holiday_gap.json` | domain `londonstockexchange.com` with regex filters | **CDX 504 Gateway Time-out on every attempt (5x business filter, 3x holiday filter)** — recorded as the incomplete part of the sweep; the per-directory prefix sweeps above are the substitute. |

Negative result: no operator artifact for 2015-01-02..2019-12-31 or
2020-01-01..2020-08-30 (nor for the five 2025 dates). Issue #218 updated.
