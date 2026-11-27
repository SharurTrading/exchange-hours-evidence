<!-- SPDX-License-Identifier: MIT-0 -->

# U.S. forward calendar retrieval on 2026-11-27 UTC

| Artifact | Operator URL | Retrieval |
|---|---|---|
| `nasdaq/trading-calendar-2027.pdf` | <https://www.nasdaq.com/docs/2027-trading-calendar> | Browser PDF download from the link on Nasdaq's public holiday page |
| `nasdaq/eta2026-69.html` | <https://www.nasdaqtrader.com/TraderNews.aspx?id=ETA2026-69> | Direct HTTPS operator response |
| `cme/2026-12-11_2026-12-15.json` | <https://www.cmegroup.com/services/trading-hours-by-product?id=8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2026-12-11&toEventDate=2026-12-15> | HTTP 200 at 06:28:22 UTC, original 3,848-byte response body |
| `cme/2028-05-25_2028-05-31.json` | <https://www.cmegroup.com/services/trading-hours-by-product?id=316,133,425,300,58,437,22,8478,5201,10191&pageNumber=1&pageSize=999&sortAsc=true&fromEventDate=2028-05-25&toEventDate=2028-05-31&isProtected> | HTTP 200 at 06:28:44 UTC, original 6,117-byte response body |

The Nasdaq PDF uses filled orange circles for exchange holidays and a
hollow orange circle for the 13:00 ET close on 2027-11-26. The day-session
and extended-session rows in ETA2026-69 give 13:00 and 17:00 ET for
2026-11-27.

The CME December response assigns the December 12 close, pre-open and reopen
at 02:00, 07:45 and 08:00 CT to the December 14 trade date for Bitcoin futures.
The May 2028 response returns all ten requested products with
`hasEvents: false` and empty event arrays. It does not establish a tradable
Memorial Day schedule. Only the HTTP response bodies are archived here.
