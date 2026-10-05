# Nasdaq — forward-horizon re-check, 2026-10-02/03 UTC

Third forward check (after the 2026-09-27 and 2026-09-29 checks). Both
channels were read again:

- The `nasdaqtrader.com` calendar page answers its Incapsula JS challenge to
  the direct channel (HTTP 200 with a challenge stub — `d0203228…`), so it was
  rendered through the public reader: its bytes carry `2026` 21 times and zero
  2027 dates.
- The `nasdaq.com` holiday-schedule page was rendered through the public
  reader: `2026` 16 times, zero 2027 dates.

No 2027 holiday schedule is published; coverage stops at 2026-12-31.

| File | URL | Retrieved (UTC) | sha256 |
|---|---|---|---|
| `nasdaqtrader_calendar.live-20261003T000704Z.html` | <https://www.nasdaqtrader.com/trader.aspx?id=calendar> (direct channel; Incapsula challenge stub) | 2026-10-03 00:07 | `d02032286070b4dd9d8fbd985a7bdca8af8edf52b89ff177db3bfcb2c8a9c43d` |
| `nasdaqtrader_calendar.reader-20261003T000903Z.md` | <https://www.nasdaqtrader.com/trader.aspx?id=calendar> via the public reader | 2026-10-03 00:09 | `7547c43a7415999dbfe84ea58955b4578c7306cbbc010e3135f7e485af67c6d7` |
| `nasdaq_holiday_schedule.reader-20261003T000903Z.md` | <https://www.nasdaq.com/market-activity/stock-market-holiday-schedule> via the public reader | 2026-10-03 00:09 | `78aa390049b0562434ac838705407a7b70d05e97b2282cd104b1fa899058c92b` |
