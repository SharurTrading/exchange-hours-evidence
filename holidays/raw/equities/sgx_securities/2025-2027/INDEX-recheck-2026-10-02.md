# SGX-ST — forward-horizon re-check, 2026-10-02 UTC

Third forward check (after the 2026-09-28 read and the 2026-09-29 re-check).
The `SGX-ST-SCHED` content-api endpoint was read again and answers changed
bytes (sha256 below differs from the shipped `45dbdc61…`), but the delta is
editorial elsewhere on the page (market-maker programme wording and a
board-lot FAQ that mentions a February 2027 implementation — not holidays).
The holiday sheet is content-identical: `SGX follows the Singapore holiday
calendar available on the Ministry of Manpower website.`, and the half-day
statement still reads `The Eve of Chinese New Year, Eve of Christmas and Eve
of New Year in 2025 & 2026 fall on business days. As such, there will be
half-day trading in 2025 & 2026.` with the same six 2025/2026 dates and no
2027 treatment. The 2027 arrangement remains unpublished; coverage stops at
2026-12-31.

| File | URL | Retrieved (UTC) | sha256 |
|---|---|---|---|
| `api2_content-api_stock-exchange_trading.live-20261002T235448Z.json` | <https://api2.sgx.com/content-api?queryId=dd24dd8e5b3ef52e535a662e01b58d76471f335e%3Apage&variables=%7B%22path%22%3A%22%2Fstock-exchange%2Ftrading%22%2C%22lang%22%3A%22EN%22%7D> | 2026-10-02 23:54 | `d40239628be36a0374d8ce9534233d1f5ec772168fb7dd64cbf12233423659be` |
