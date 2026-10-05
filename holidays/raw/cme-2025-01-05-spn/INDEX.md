# `trading-hours-by-product` for 2025-01-05..2025-01-07 — Save Page Now attempt

Retrieved 2026-09-26T07:26:15Z, via Internet Archive **Save Page Now**
(`https://web.archive.org/save/<url>` → capture timestamp `20260926072615`), fetched
back with the `id_` raw replay.

Requested URL:

```
https://www.cmegroup.com/services/trading-hours-by-product
  ?id=316,133,425,300,58,437,22,8478,5201,10191
  &pageNumber=1&pageSize=999&sortAsc=true
  &fromEventDate=2025-01-05&toEventDate=2025-01-07
```

| file | sha256 | bytes | contents |
|---|---|---|---|
| `response.json.gz` | `989cc315a0ff22d2ddb7770a6711c07b32b13007891c22c3463eb6777fe32f17` | 757 | the archived response body, gzip, exactly as served |
| `response.json` | — (derived) | 3,877 | decompressed |

## Result: the response carries NO events

```json
{"props":{"sortAsc":"true","total":10,"pageNumber":1,"pageTotal":1,"pageSize":500,"hasEvents":false},
 "products":[{"foi":"Futures","globex":"ZN","prodGroup":"ZN","name":"10-Year T-Note Futures","id":316,...}, ...]}
```

All ten requested products return an empty `events` array for `2025-01-05`,
`2025-01-06` and `2025-01-07`, and the envelope's own flag reads
**`"hasEvents": false`**.

## Why this matters

This window is the one a primary-source report named as the cheapest way to close
issue #79: 2025-01-01 is a holiday, 01-02/03 are weekdays and 01-04 a Saturday, so
**2025-01-05 is the first ordinary Sunday leg inside the claimed interval**. A
response carrying that date's events would witness the Sunday queue in force at
the floor and move the seven scopes' knowledge bound from 2026-08-22 back to
2025-01-01 without ever dating the 2012 change.

**It does not work.** Either the operator's channel no longer retains a January-2025
window, or the archived fetch did not receive the events. A control attempt on a
recent window returned no capture at all, so the two explanations are not separated
here — and under LAW-BOUNDED-WORK neither was pursued further. No proxy, header
change or alternate endpoint was attempted.

**Consequence for #79:** the "retrieve an ordinary 2025 week" route cannot be
assumed to be a live-channel read. Anything obtained this way must be checked for a
non-empty `hasEvents` before it is treated as evidence — an empty envelope is
indistinguishable from a normal day by shape alone, and it is the retention limit
talking, not the operator.
