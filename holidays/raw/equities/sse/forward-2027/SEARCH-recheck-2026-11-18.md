# SSE — forward-horizon re-check, 2026-11-18 UTC

Fourth forward check (after the 2026-09-28 retrieval, the 2026-09-29 web
search and the 2026-10-03 re-check). Web search for the notice title
`关于2027年部分节假日休市安排的通知` — both unrestricted and restricted to
`sse.com.cn` — returned nothing: the exact-title query has no hits at all
yet, and no operator page mentions a 2027 closure arrangement. The SSE
announcement list channel (`www.sse.com.cn/disclosure/announcement/general/`)
was read live through 2026-11-18 (latest entries are fund notices of
2026-11-16/18) and carries no holiday-arrangement notice; the announcement
query API errored as on the prior checks; `english.sse.com.cn` news releases
carry no 2027 holiday content and the English trading-calendar page refused
again (HTTP 403, the recorded behaviour).

What did appear is the national layer: the State Council General Office's
2027 arrangement (国办发明电〔2026〕10号, published 2026-11-05 on gov.cn,
with the English release of 2026-11-06). It was retrieved and saved under
`../state-council-2027/` with its digests. It states the civil 放假 windows
and the 调休 working weekends in national-holiday language, not the
exchange's 休市 sessions, and the table's rows key only from the operator's
own annual notice — so it keys no row (LAW-PRIMARY-SOURCES) and the audited
window stays 2011-01-01..2026-12-31.

The exchange publishes the next year's arrangement each late December (the
2026 notice was published 2025-12-22), so nothing is expected before then.
Coverage stops at 2026-12-31; the closing condition is the operator's own
2027 notice.
