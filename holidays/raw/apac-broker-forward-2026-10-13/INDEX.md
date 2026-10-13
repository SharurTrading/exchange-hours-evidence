# Evidence index — task `apac-broker-forward-2026-10-13`

APAC / broker-book / crypto / CFE forward-publication watch. Retrieval session
**2026-10-13 23:27–23:39 UTC** (`date -u`, LAW-UTC-DATES). A monthly LAW-WATCH
re-pull of each operator's live holiday/adjusted-hours channels, diffed against
the banked captures already held in this store; **no new publication was found
for any operator** — every diff below is a clean negative. This directory adds
the fresh live bytes that make each negative auditable and changes nothing in
the earlier capture sets.

Baseline captures diffed against (all already in this store, untouched):

- HKEX: `equities/hkex/forward-2028/hkex_holiday_schedule.live-20261002T235917Z.html`
  (live page, 2026-10-02 recheck) and the `HKEX-TC-2026-2027` digest recorded in
  the crate's `docs/evidence/hkex.md` (2026-09-28 retrieval).
- ASX: `equities/asx/2025-2027/live_asx_cash_market_trading_calendar.html`
  (2026-09-28) and `asx24-2010-2027/live_asx24_trading_calendar.html` (2026-10-11).
- SGX: `equities/sgx_securities/2025-2027/api2_content-api_stock-exchange_trading.json`
  and `live_mom_public_holidays.html` (both 2026-09-28).
- OANDA UK: `oanda-uk-holiday-hours-2026-10-10/oanda-uk-holiday-trading-hours.html`
  and `normal-weeks/oanda-uk-hours-2026-10-10/oanda-uk-hours-of-operation.html`.
- CDE: `cde-2026-2027/` (2026-09-26 sweep; listing rows then stopped at 26-37 listed-only).
- CFE: `cfe-eurex-ice-cde-smfe-2026-2027/cboe_us_futures_holidays_2026.csv` etc. (2026-09-12).

## Documents

| Document | URL | Retrieved (UTC) | sha256 | Bytes | What it is |
|---|---|---|---|---|---|
| `hkex_tc_live_20261013.html` | https://www.hkex.com.hk/Services/Trading/Derivatives/Overview/Trading-Calendar-and-Holiday-Schedule?sc_lang=en | 2026-10-13 23:27:47 | `5f35901bd5ecf4a52d5b9622c4cf732be0f8822d70b2ecf0a899002d05cf008c` | 384,985 | **T1.** HKEX live Trading Calendar and Holiday Schedule page. Footer still `Updated 31 Jul 2026`; all 27 table rows naming 2026/2027 content-identical to the 2026-10-02 capture; the page names 2027 seventeen times and 2028 zero times. |
| `asx_tc_live_20261013.html` | https://www.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours/trading-calendar | 2026-10-13 23:29:29 | `aceeab4a2abefea3ac0d89f0dc1d11b0bf369f6008dbb2da0fd7875706a00bd6` | 148,042 | **T1.** ASX live cash-market trading calendar. The 2026 and 2027 sheets (`CLOSED`/`CLOSE EARLY` rows, footnotes 14:10 early close) match the crate's shipped `ASX-CAL-LIVE` rows and the 2026-09-28 capture. |
| `asx24_tc_live_20261013.html` | https://www.asx.com.au/markets/market-resources/asx-24-trading-calendar | 2026-10-13 23:30:27 | `91cd7a7a1217d29f11c21bcb36810ecbbce8b4caa5ee58558624e11f3fcb0376` | 155,024 | **T1.** ASX live ASX 24 trading calendar. 32/32 dated rows (2026 + 2027 tables) content-identical to `asx24-2010-2027/live_asx24_trading_calendar.html` (2026-10-11); ONO footnote dates identical (23 Jan, 5 Jun, 8 Jun 2026; 11 Jun, 14 Jun 2027); no 2028 mention. |
| `sgx_content_api_20261013.json` | https://api2.sgx.com/content-api?queryId=dd24dd8e5b3ef52e535a662e01b58d76471f335e%3Apage&variables=%7B%22path%22%3A%22%2Fstock-exchange%2Ftrading%22%2C%22lang%22%3A%22EN%22%7D | 2026-10-13 23:31:55 | `d40239628be36a0374d8ce9534233d1f5ec772168fb7dd64cbf12233423659be` | 141,120 | **T2.** SGX content-API feed behind `/stock-exchange/trading` (same queryId as `SGX-ST-SCHED`). Holiday content unchanged: the MOM designation sentence, the half-day grid, and the eve statement still scope themselves to `2025 &amp; 2026`; no 2027 holiday or half-day statement. Only non-schedule delta vs the 2026-09-28 capture: a Market Maker and Active Trader Programmes (MMAT) blurb module. |
| `mom_holidays_20261013.html` | https://www.mom.gov.sg/employment-practices/public-holidays | 2026-10-13 23:32:41 | `4a35858ca345100db03d6f7b3acd70aea2b42d1fca8b73efefd819ccc221b15f` | 88,639 | **T1.** MOM public-holidays page (the calendar SGX designates). Year tabs 2025/2026/2027 all content-identical to the 2026-09-28 capture: no 2026 errata, 2027 still gazetted and unchanged, no 2028 tab. |
| `oanda_holiday-trading-hours_20261013.html` | https://www.oanda.com/uk-en/trading/holiday-trading-hours/ | 2026-10-13 23:33:23 | `91f26449809e3d4c1ec566b8cca97096c004f5ec4c6f13306098b5c0e4cd798e` | 239,918 | **T1.** OANDA UK holiday trading hours page. 104/104 dated section headers content-identical to the 2026-10-10 capture; the newest dated section is still `Friday, 30 Oct 2026 – All Saint Day (SE)`. No November/December 2026 arrangement, no 2027 section. |
| `oanda_hours-of-operation_20261013.html` | https://www.oanda.com/uk-en/trading/hours-of-operation/ | 2026-10-13 23:33:24 | `a9b643a94f046d6e36917d4e5ef488520c51ca69199563465120a5f0981b3145` | 470,997 | **T1.** OANDA UK hours-of-operation page. All 25 time-grid tokens (`17:05 - 16:59` family grids) identical to the 2026-10-10 capture — normal week unchanged. |
| `cde_direct_20261013.html` | https://www.coinbase.com/derivatives/market-notices | 2026-10-13 23:35:40 | `165ce478889b8ce2111518d8abb09f8fa7ed33f5aa1c0e62c83702c0301aa7f4` | 5,794 | **Refusal evidence.** Direct fetch returns HTTP 403 (Cloudflare), same block the 2026-09-26 session recorded; kept so the block stays auditable. |
| `cde_notices_reader_20261013.md` | https://r.jina.ai/https://www.coinbase.com/derivatives/market-notices | 2026-10-13 23:35:47 | `4733f9aae657307f45cf45cad34f139dc161961274b703595a9224d31635f439` | 45,806 | **T1 listing (reader render).** CDE market-notices listing, newest first. Newest schedule-relevant rows: `26-33.3` (published 09/24/2026, effective 09/25/2026, gateway-deploy amendment, Maintenance) and `26-37` (published 09/24/2026, effective 10/24/2026, Q4 quarterly maintenance window) — both already recorded listed-only on 2026-09-26. Nothing numbered above 26-37; the only later row is `R2026-56` (10/07/2026, Rule Filing, MMP supplemental — not a schedule document). **No Thanksgiving 2026, Christmas 2026 or 2027 holiday notice exists yet.** |
| `cdx_cde_recent.json` | https://web.archive.org/cdx/search/cdx?url=assets.ctfassets.net%2Fk3n74unfin40%2F*&filter=original:.*otice.*&from=20260919&to=20261015&output=json&limit=300 | 2026-10-13 23:37:34 | `a7e4413bbd96195d5c52d6b509b5af89f441715a9e08e516e0c1c65f06ec2919` | 3,161 | **Negative-hunt record.** Wayback CDX for the CDE assets bucket, 2026-09-19..2026-10-15: every capture is a crawl of an already-known notice PDF (26-33, 26-33.1, 26-33.2, 26-30, 26-32, 26-25, 26-22, 26-20, 26-13); no new notice PDF exists. |
| `cboe_futures_holidays_csv_20261013.csv` | https://www.cboe.com/us/futures/holidays/csv/ | 2026-10-13 23:38:09 | `b92bd6ea475ff8817e20e243c045b639e29c6331d42520932aaa7c65b9d650c0` | 1,165 | **T1.** Cboe's CSV export of the CFE holiday schedule, regenerated `# Generated: 2026:10:13 16:26:54`. All 13 data rows byte-identical (diff excluding the Generated header) to the 2026-09-12 capture; still 2026 only — no 2027 rows, no errata. |
| `cboe_hours_us_futures_20261013.html` | https://www.cboe.com/about/hours/us-futures | 2026-10-13 23:38:10 | `3239381c783f9547c7a34a5b93987238bd26738135b36903378eac7b571946d1` | 503,603 | **T1.** Cboe Hours & Holidays → U.S. Futures. Only the 2026 Futures Holiday Schedule section exists; the page's only `2027` strings are nav links to `cboe.com/rmc-2027` (a conference), not a holiday table. |
| `cfe_circulars_20261013.md` | https://r.jina.ai/https://www.cboe.com/us/futures/regulation/circulars | 2026-10-13 23:38:42 | `530bbc05058b0f814d0295e9e53ab168e310b348c9da921b69938fd397278bc4` | 99,370 | **T1 index.** CFE regulatory circular listing. The latest holiday-related circular remains CFERG26-004 (2026-03-31, 2026 holiday calendar); no 2027 holiday circular listed. |

`INDEX.md` (this file) is the register. Per-operator findings and the exact
diff method: `apac-forward-findings.md` beside it.

## Access notes

- `www.coinbase.com` returns 403 to direct `curl` from this host (Cloudflare),
  reproduced in `cde_direct_20261013.html`; the `r.jina.ai` reader render
  succeeded in markdown mode (the `x-respond-with: html` variant that was
  refused on 2026-09-26 was not retried).
- All other operator channels fetched directly (plain `curl` with a browser
  User-Agent); `web.archive.org` was reachable this session (the CDX query
  succeeded).

## Result (one line each)

1. **HKEX** — no change: live edition still `Updated 31 Jul 2026`; 2026/2027 tables unchanged; no 2028 edition.
2. **ASX / ASX 24** — no change: cash sheet matches the shipped rows; ASX 24 tables and ONO dates identical to 2026-10-11; no 2028.
3. **SGX** — no change: T2 feed holiday content unchanged, eve/half-day statement still scoped `2025 & 2026`; MOM tabs unchanged; the 2027 gap (SGX has not stated 2027 half-day treatment) stays open.
4. **OANDA UK** — no post-2026-10-30 publication: holiday page identical to 2026-10-10, newest section `Friday, 30 Oct 2026`; hours grids unchanged.
5. **CDE (coinbase_derivatives)** — no new notices above 26-37; no Thanksgiving/Christmas 2026 or 2027 holiday notice yet (2025 pattern expects the Thanksgiving notice in autumn).
6. **CFE** — CSV regenerated 2026-10-13 with identical 2026-only rows; no 2027 publication in the CSV, hours page or circulars.
