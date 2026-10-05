# sgx_securities 2020-2024 retry (2026-09-30 UTC)

The Wave-D re-check of the `wps/portal/sgxweb/home/trading/securities/
trading_hours_calendar` capture gap. Findings:

1. The wps page's own 2020-2024 captures remain SPA shells: the 2021-12-24,
   2022-05-25 and 2024-03-02 replays (`wps_shell_capture-*.html`) are the
   React runtime (`runtime.*.js` + `index.<hash>.chunk.js`) with no holiday
   content in their bytes.
2. The SPA's own content-api query for the wps path was captured exactly once
   (`wayback_content-api_wps-trading-hours-calendar_capture-20220913T171707Z.json`,
   2022-09-13 17:17:07 UTC) and its complete body is
   `{"data":{"route":null}}` — the API served no content for the retired wps
   path. 23 bytes; not a witness.
3. The current site's own content-api query
   (`queryId=...:page&variables={"path":"/stock-exchange/trading","lang":"EN"}`)
   first appears in the Wayback index at capture 2026-07-25 — nothing for
   2020-2024.
4. The `sgx_en/home/trading/securities/trading_hours_and_calendar/`
   announcement family holds only the 2011-08-01 all-day-trading notice
   (first capture 2022-02-03), which names no holiday table.

CDX queries (all 2026-09-30 UTC): `matchType=domain` over `api2.sgx.com`
(1 499 distinct urlkeys, `content-api` page queries for the new-site paths and
`we_chat_qr_validator`/`alerts`/`all_menus` shapes only); `filter=original:
.*trading_hours_calendar.*` over `api2.sgx.com/content-api*` (1 row, the
2022-09-13 capture above); domain-wide `filter=urlkey:.*(holiday|calendar).*`
2020-2025 (no unexamined operator calendar page family).
