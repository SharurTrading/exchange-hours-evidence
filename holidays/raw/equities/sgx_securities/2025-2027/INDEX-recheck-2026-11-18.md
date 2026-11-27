# SGX-ST — forward-horizon re-check, 2026-11-18 UTC

Fourth forward check (after the 2026-09-28 read, the 2026-09-29 re-check and
the 2026-10-02 re-check). Two questions this pass:

1. **Does the operator's own channel yet state a 2027 arrangement?** No. The
   `SGX-ST-SCHED` content-api endpoint was read again and answers changed
   bytes (sha256 below differs from the shipped `45dbdc61…` and from the
   2026-10-02 capture `d4023962…`), but the delta remains editorial elsewhere
   on the page; the only `2027` strings in the body are the board-lot FAQ's
   February-2027 implementation note. The holiday sheet is content-identical
   where it governs: `SGX follows the Singapore holiday calendar available on
   the Ministry of Manpower website.`, and the half-day statement still reads
   `The Eve of Chinese New Year, Eve of Christmas and Eve of New Year in
   2025 & 2026 fall on business days. As such, there will be half-day trading
   in 2025 & 2026.` with the same six 2025/2026 dates. No 2027 closure or
   half-day treatment is stated, so the window still ends at 2026-12-31 and
   no 2027 row keys — MOM's gazetted 2027 list alone has never keyed a row
   for this identity (the rows key from the operator's own bytes; MOM is the
   designated calendar the dates resolve against).
2. **Is the state side ready?** Yes — captured for when the operator speaks.
   The MOM page (server-rendered; page `datePublished` 2026-06-19) prints the
   2027 tab with the gazetted list: 1 January (Fri, New Year's Day);
   6–7 February (Sat–Sun, Chinese New Year, with MOM's own sentence
   "Monday, 8 February 2027, will be a public holiday if your rest day falls
   on 7 February 2027."); 10 March (Wed, Hari Raya Puasa); 26 March (Fri,
   Good Friday); 1 May (Sat, Labour Day); 17 May (Mon, Hari Raya Haji);
   20 May (Thu, Vesak Day); 9 August (Mon, National Day); 28 October (Thu,
   Deepavali); 25 December (Sat, Christmas Day) — ten rows, eleven dated
   days. Weekday closures under the validated derivation would be 1 January,
   8 February (MOM's substitution sentence), 10 March, 26 March, 17 May,
   20 May, 9 August, 28 October — eight dates — with the three Saturday
   holidays (Labour Day, Christmas Day, and CNY's 6–7 February weekend)
   closing no weekday; the half-day eve question stays the operator's to
   state. Recorded as a gap, not data: no runtime row moves.

| File | URL | Retrieved (UTC) | sha256 |
|---|---|---|---|
| `api2_content-api_stock-exchange_trading.live-20261118T090437Z.json` | <https://api2.sgx.com/content-api?queryId=dd24dd8e5b3ef52e535a662e01b58d76471f335e%3Apage&variables=%7B%22path%22%3A%22%2Fstock-exchange%2Ftrading%22%2C%22lang%22%3A%22EN%22%7D> | 2026-11-18 09:04:37 | `debd651570b4932ef6ac8bed871d535cb3b2fc8260f69668359fbcf8a32d77ac` |
| `live_mom_public_holidays-20261118.html` | <https://www.mom.gov.sg/employment-practices/public-holidays> | 2026-11-18 09:05:10 | `be7fa74808cd9c0034a44ab874f67ee3b48df0b1dd7cc7a8b9ef7d4ea4162cfe` |

Side probes this pass (observed, not retained as artifacts — both reproduce
the record's known negatives): the content-api query for a
`/stock-exchange/trading-hours-holidays` path answers `{"data":{"route":null}}`
(the same empty-route body the retired wps path served at its single 2022
capture), and the live `sgx.com/stock-exchange/trading-hours-and-holidays`
page renders as the same Angular SPA shell with an empty `#page-container`
and no server-side holiday content.

Closing condition (unchanged): SGX's own content-api bytes stating the 2027
treatment — a half-day sheet extended to 2027 (the eve question), or a 2027
securities trading-schedule naming the year's closures — at which point rows
key immediately from this store against the validated derivation. Re-checked
monthly per LAW-WATCH.
