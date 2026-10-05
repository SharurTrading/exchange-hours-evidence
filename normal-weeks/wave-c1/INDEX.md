# INDEX — wave-c1 (normal-week sourcing wave C1: CME families + Eurex fixed income, 2010 floor era)

Retrieval performed 2026-09-30 (UTC) from this machine. cmegroup.com returns an
anti-scraping block directly, so every CME artifact was read from the Internet
Archive with `id_` raw replay; the wayback timestamp is the *capture* time (UTC)
and dates the observation, not the state. Eurex artifacts are the operator's own
live `eurex.com/resource/blob/` URLs. Tier: T1 throughout (operator's own pages,
notices, and contract-specification amendments).

## Eurex Contract Specifications amendments (`eurex/`)

| file | document | URL | capture/retrieval (UTC) | sha256 |
|---|---|---|---|---|
| `btp-2009.pdf` | CS amendment "Euro-BTP Futures: Introduction", As of September 14, 2009 — Annex C fixed-income trading-hours table (FGBS/FGBM/FGBL/FGBX 07:30-08:00 / 08:00-22:00 / 22:00-22:30) | <https://www.eurex.com/resource/blob/328400/e12f28dfcc8ba1f7b94ea4da40b69c41/data/cs_history_14092009_en.pdf.pdf> | retrieved 2026-09-30T04:35Z | `c94ac7911b1e2b2835833f0c04d0989cdcd5e1a20f8f4cf9890d2b60c0a19f96` |
| `btpmid-2011.pdf` | CS amendment "Mid-Term Euro-BTP Futures: Introduction", As of 19.09.2011 — same Annex C table, FGBL/FGBM/FGBS/FGBX rows unchanged | <https://www.eurex.com/resource/blob/326452/9aa55ddb4fd3b0fb7fb15567a734ab5d/data/cs_history_19092011_en.pdf.pdf> | retrieved 2026-09-30T04:45Z | `eb52f6af0ccfbf36b145601d90d28e9c5d92b1ffdcf4d19e8fd3cdccd1b33162` |
| `oat-2013.pdf` | CS amendment "Mid-Term Euro-OAT-Futures: Introduction", As of 11.03.2013 — same Annex C table, FGBL/FGBM/FGBS/FGBX rows unchanged | <https://www.eurex.com/resource/blob/334064/488cfe99b1526c777b789ade2950e4e5/data/2013_03_11_cs_history_1_en.pdf.pdf> | retrieved 2026-09-30T05:00Z | `f927a78d8cc975ebe0207b32e64a7762bb53fd0c5c9fd9c37fe7b3b3e0a1560c` |
| `posttrading-2017.pdf` | CS amendment "Fixed Income Futures: Harmonisation of Post-Trading period on regular trading days", As of 28.08.2017 — FGBL/FGBM/FGBX Post-Trading Period Until 22:30 unchanged | <https://www.eurex.com/resource/blob/295608/36bcde7eecdd7167995bf1143432e5c9/data/2017_08_28_cs_2_history_en.pdf> | retrieved 2026-09-30T04:40Z | `a7a42a3936b182476cfbe4d0218ef518826171044236089bf34baef3a6b5cbac` |
| `exttime-2010.pdf` | CS amendment "Extension of trading time", cs_history_05072010 — read to confirm its Annex C rows are index-futures only (MSCI Russia, OMXH25, SLI, SMI), no fixed-income rows | <https://www.eurex.com/resource/blob/330302/b900fed6f0a95921bd1b24e768b14c76/data/cs_history_05072010_en.pdf.pdf> | retrieved 2026-09-30T04:42Z | `21941e2d858e452ca415c2b2d98c35f8f15f19667543180ddade8c0a1a8ca845` |
| `cs2009.pdf` | CS amendment history cs_history_26102009 (index subpart) — already cited by `docs/evidence/eurex.md`; read only to confirm it carries no fixed-income table | <https://www.eurex.com/resource/blob/296888/978b08fe3a240a0b4a8fb62a2647a197/data/cs_history_26102009_en.pdf.pdf> | retrieved 2026-09-30T04:33Z | `fea3a3c859112b482380a5e1ee017108978dbc9a3fadc7e953082225fc19d6bb` |
| `cs-index.html` | Eurex Contract Specifications index page listing the amendment archive (source of the per-amendment links above) | <https://www.eurex.com/ex-en/rules-regs/eurex-rules-regulations/03.-Contract-Specifications-4347288> | retrieved 2026-09-30T04:30Z | see `sha256s.txt` |

## CME trading-hours pages (`cme-hours-pages/`)

| file | page | capture (UTC) | sha256 | what it shows |
|---|---|---|---|---|
| `equities-20090406.html` | cmegroup.com/trading_hours/equities-hours.html | 2009-04-06T22:34:56Z | `1b5a9fb31a6b1207cc915041f42d22e3b9c1eabf100d18ef7ab0597b652014fc` | pre-floor equity grid: E-mini rows "15:30-16:30 and 17:00-15:15" (weekday) / "17:00-15:15" (Sunday); full-size SP rows "17:00-8:15"; no Pre-Open rows on the page |
| `equities-20100402.html` | same page | 2010-04-02T12:24:30Z | `6991513178bb5446323041d57de4177cb3921f3f9f165738ee68953e2701a06d` | same grid at the floor era; no Pre-Open rows |
| `equities-20110901.html` | same page | 2011-09-01T18:18:47Z | `3446a665366795d1ff40fc74de7f237727ede78812018e891c9067cc1a682860` | same grid; no Pre-Open rows yet |
| `equities-20120503.html` | same page | 2012-05-03T10:43:28Z | `1927c18749e0e508178eaf0f0fb52c94d6b7b25436c6ed6529b1206b38fdf673` | the already-cited capture: Pre-Open Electronic Trading (Sunday) 16:15, (Weekday) 16:45 |
| `fx-20090502.html` | cmegroup.com/trading_hours/fx-hours.html | 2009-05-02T19:42:22Z | `50adab84126c8f99da5569faecb178771a9f6b0301bf62ce26032a112dab9ecd` | pre-floor FX grid: "17:00-16:00 next day" per product; no Pre-Open rows |
| `fx-20110918.html` | same page | 2011-09-18T05:57:01Z | `c125c6998dd95b2cd7a52651b5c2057dbc2bc1058e56e778b38417a98d03dfe0` | same grid; no Pre-Open rows yet |
| `metals-20110902.html` | cmegroup.com/trading_hours/metals-hours.html | 2011-09-02T04:38:56Z | `94a6a1a6bc404e85aa20f8e383a9ff585c17c9f72bbdad09fb230a737432bde5` | metals grid; no Pre-Open rows yet |
| `metals-20120501.html` | same page | 2012-05-01T18:24:31Z | `feb67d4b9b8194c3ef65cc4f1a0ba903223b3e3347c635a7d44c10c791ed4d66` | the earliest metals capture with Pre-Open rows: Sunday "17:15 ET (16:15 CT)", weekday "17:45 ET (16:45 CT)", session "18:00-17:15 ET (17:00-16:15 CT)" |
| `energy-20100502.html` | cmegroup.com/trading_hours/energy-hours.html | 2010-05-02T09:01:21Z | `887ec4baf97dce7a6fbbccd16ee597d39357a6ea39d47a495192dc72f8b72aeb` | energy grid at the floor era; no Pre-Open rows |

## CME Globex notices (`cme-notices/`)

Weekly CME Globex notices read in full, retrieved as Internet Archive raw replays
of `http://www.cmegroup.com/tools-information/lookups/advisories/electronic-trading/<name>.html`.
Per-file sha256 in `sha256s.txt`. The load-bearing ones:

| file | notice | capture (UTC) | what it states |
|---|---|---|---|
| `20090608.html` | Globex notice of June 8, 2009 (repeated in `20090615`, `20090622`) | 2019-08-22T13:30:24Z | "Commodity Trading Hours Extended — Effective Wednesday, July 1, the ETH for CBOT grains, oilseeds and ethanol contracts ... will be expanded from 6 a.m. Central time to 7:15 a.m. CT. With this change, these futures, options and spreads will be available for electronic trading on CME Globex from 6 p.m. to 7:15 a.m. Sunday through Friday. There is no change to the regular trading hours (RTH), 9:30 a.m. to 1:15 p.m. weekdays." |
| `20090831.html` | Globex notice of August 31, 2009 (repeated in `20090907`, `20090914`) | 2019-07-22T18:07:03Z | Equity Futures Enhancements effective Sunday, October 4, 2009: "Customers may re-enter GTC and GTD orders during the pre-open, 4:15 to 5:00 p.m. CT, Sunday, October 4." — the operator's name for the normal Sunday Pre-Open window of the CME Equity futures complex, printed before the support floor |
| `20090126.html` / `20090127.html` / `20090130.html` | Globex notices of late January 2009 (DME migration) | see `sha256s.txt` | "Trading hours for DME products on CME Globex will match the NYMEX Crude Oil products: Sunday - Friday, 5:00 p.m. - 4:15 p.m. CT." — the pre-floor NYMEX energy grid |
| `20100315.html` | Globex notice of March 15, 2010 (already cited by `cbot.md`/`globex_grains.md`) | 2010-03-29T15:42:09Z | "Current Pre-Open for CBOT, KCBT and MGEX Grain Futures — Sundays: 4:15 p.m. - 6 p.m.; Mondays through Fridays: 7:15 a.m. - 9:30 a.m.; Mondays through Fridays: 2:30 p.m. - 4 p.m." |
| `20101018.html` | Globex notice of October 18, 2010 | see `sha256s.txt` | "Pre-Open Schedule Change — Effective Monday, November 15, the Monday through Thursday afternoon pre-open for CME, CBOT, KCBT and MGEX products on CME Globex will begin 5 minutes earlier, at 4:45 p.m. Central time. With this change, the afternoon pre-open times will match the current schedule for NYMEX, COMEX and DME products" — the 2010-11-15 revision's own publication (the repo cites its repeat at `20101025.html`), stating both the outgoing 16:50 value and that NYMEX/COMEX/DME already opened their weekday queue at 16:45 |
| `20101025.html`, `20101227.html`, `20110110.html` | Globex notices of October 2010 - January 2011 (COMEX/NYMEX/DME futures enhancements) | see `sha256s.txt` | launch-weekend notices whose extended pre-open (from 15:00 CT) contrasts with "TAS products will pre-open at their normal time, 16:15 CT" — floor-era corroboration of the 16:15 Sunday queue value for the COMEX/NYMEX complex (names the TAS products; the crate's family scope excludes TAS, so this is corroboration, not the row's basis) |
| `20080109.html` | Globex notice of January 9, 2008 (CBOT commodity migration) | see `sha256s.txt` | the 2008-era commodity grid with queues (16:50 pre-open / 18:00 open / 06:00 halt / 09:30 SBS / 13:15 close / 14:30-16:30 afternoon pre-open) — history for the pre-expansion era, superseded by the dated 2009-07-01 expansion |

The full 2008-2011 weekly notice series was retrieved from the archive: 244
files on disk (130 for 2008-2009, 114 for 2010-2011; four carry suffixed or
non-sequence names — `20080219a`, `20081110_SA`, `200908017`,
`20110808_standalone`). 242 of the 244 are readable and each was text-scanned
for pre-open schedule statements. Two captures failed as zero-byte files and
were not read: `20090119.html` and `20100726.html`.

## Search record for the Sunday Pre-Open, FX and energy/metals (bounded, 2026-09-30 UTC)

The hunt that would have moved `globex_fx` and the energy/metals horizons to the
floor, and where it closed:

- The per-class trading-hours pages carried **no Pre-Open rows before 2012**:
  equities 2009-04-06, 2010-04-02, 2011-09-01 (rows appear by the 2012-05-03
  capture); fx 2009-05-02, 2011-09-18 (rows by 2012-05-03); metals 2011-09-02
  (rows by 2012-05-01). So the pages cannot state the queue below 2012.
- The archived weekly Globex notices of 2008-2011 (244 on disk, 242 readable;
  the two failures above unread) name a floor-era Sunday Pre-Open value only
  four ways: the equity complex's own window (20090831/0907/0914, quoted
  above), the interest-rate products' own schedule table (20090326/20090330,
  "CME and CBOT Interest Rate Products Schedule — Effective April 5" 2009:
  Sundays Pre-Open 16:15, Monday-Friday Pre-Open 16:50 — it corroborates the
  already-sourced `globex_interest_rates` floor grid and moves nothing here),
  the COMEX/NYMEX launch notices' "TAS products ... normal time, 16:15 CT"
  (TAS is outside the served family scopes), and Random Length Lumber's dated
  2010-06-21 "Sunday evening pre-open: 16:15 CT" (lumber is not a served root).
  No notice states the FX or energy/metals complex's normal Sunday Pre-Open
  before the 2012 captures.
- Closing conditions (unchanged from #79's own record): an operator statement of
  the FX or energy/metals complex's Sunday Pre-Open in session language dated
  before 2012.
