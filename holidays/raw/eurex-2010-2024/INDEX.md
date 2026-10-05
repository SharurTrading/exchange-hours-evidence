# Evidence index — task `eurex-2010-2024`

Primary-source retrieval for the `eurex` served identity's pre-2025 Trading Calendar
editions. The 2012–2024 editions were retrieved live from the operator's own Trading
Calendar archive on **2026-09-29 UTC**; the 2010 and 2011 editions survive only on the
predecessor `eurexchange.com` site and are Wayback `id_` replays of their era-original
captures (2010-02-16 and 2011-01-14). All timestamps are UTC (LAW-UTC-DATES). The
repository-facing record of these documents is `docs/evidence/eurex.md` § Documents.

Retrieval session note: `web.archive.org` was intermittently unreachable during the
2026-09-26 session (see `holidays/raw/eurex-2025-2027/INDEX.md`); the two Wayback
replays above were fetched in the 2026-09-29 session on retry.

Each file's sha256 was re-verified on **2026-10-03 UTC** against the table below and
against `docs/evidence/eurex.md` § Documents; all fifteen reproduce.

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `tradingcalendar_2010_en.wayback-20100216003515.pdf` | `https://web.archive.org/web/20100216003515id_/http://www.eurexchange.com/download/trading/tradingcalendar_2010_en.pdf` | 2026-09-29 (Wayback `id_` replay of capture `20100216003515`) | `9caaee91446b115fc1b069fec44653290cf1e57cefc26f86859fe5bee0e98f59` | 1587924 | **T1.** "Eurex Trading Hours 2010", p.2 "Overview of holidays by countries". All-derivatives closure lists; **no German-scope line**. |
| `tradingcalendar_2011_en.wayback-20110114201916.pdf` | `https://web.archive.org/web/20110114201916id_/http://www.eurexchange.com/download/trading/tradingcalendar_2011_en.pdf` | 2026-09-29 (Wayback `id_` replay of capture `20110114201916`) | `329fe76877537c873b433ab0b7fe2093b58fd72d0162444479d53a90ef704b2c` | 2218996 | **T1.** "Eurex trading hours 2011". All-derivatives closure lists; **no German-scope line**. |
| `tradingcalendar_2012_en.pdf` | `https://www.eurex.com/resource/blob/284994/e988f1cef4437150c0a74a5a8f285d64/data/tradingcalendar_2012_en.pdf` | 2026-09-29 | `3045def26f7af8ab5228b5714fb3d75043d14287c2ea8e476c43f3b0ac8d5739` | 1457389 | **T1.** All-derivatives lists; **no German-scope line**. |
| `tradingcalendar_2013_en.pdf` | `https://www.eurex.com/resource/blob/244836/3ad19654e330995e7d07e4da214ccecd/data/tradingcalendar_2013_en.pdf` | 2026-09-29 | `c22be70750ba8bac19e45e62bf638deb0c0efd0321a193b4bc633c3a6f21fd40` | 1349831 | **T1.** All-derivatives lists; **no German-scope line**. |
| `tradingcalendar_2014_en.pdf` | `https://www.eurex.com/resource/blob/249120/6fadad3fe12a3cc3fa392442532d4414/data/tradingcalendar_2014_en.pdf` | 2026-09-29 | `684fe66cb662a827ef9f6b44a41d566ec122b98fab5781b81af0ec28e22a1805` | 1208886 | **T1.** All-derivatives lists **plus** the dated German-scope line `Eurex is closed for trading and exercise in German equity and equity index derivatives as well as ETF and ETC derivatives, which are based on Xetra® listings: 3 October`. |
| `tradingcalendar_2015_en.pdf` | `https://www.eurex.com/resource/blob/243714/8c6cea18bbe820e719a578e3bd94976c/data/tradingcalendar_2015_en.pdf` | 2026-09-29 | `45b0dc151bca7bbe80f7f659b725afc3016ec8201f43a66880ba7b8782f61ef7` | 1257488 | **T1.** All-derivatives lists (Whit Monday 25 May trading-only); **no German-scope line**. |
| `tradingcalendar_2016_en.pdf` | `https://www.eurex.com/resource/blob/1260/f42d8f907b73ce30a66148cc287f2fe8/data/tradingcalendar_2016_en.pdf` | 2026-09-29 | `3ef1bb9885fe0d94f903269ff75dda52731752647ad93772e65e80aeaa4a32f7` | 1275733 | **T1.** German-scope line `…: 16 May, 3 October`. |
| `tradingcalendar_2017_en.pdf` | `https://www.eurex.com/resource/blob/241960/7dc968da8ed8d80fa004bd695ac9b648/data/tradingcalendar_2017_en.pdf` | 2026-09-29 | `86ce6888b3d98ad82da84eb25a36bc9e5d928f1eb0ee4fdc194c77e38cdfe2de` | 679969 | **T1.** German-scope line `…: 5 June, 3 October, 31 October`. |
| `tradingcalendar_2018_en.pdf` | `https://www.eurex.com/resource/blob/2806/32828d43772ac5ee3dd3d77a79743b47/data/tradingcalendar_2018_en.pdf` | 2026-09-29 | `e90fb8d6fbe90945678b8646f7f22ba30f6b2e7c3b42f2d6876b254888e8fa81` | 692008 | **T1.** German-scope line `…: 21 May, 3 October`. |
| `tradingcalendar_2019_en.pdf` | `https://www.eurex.com/resource/blob/1396378/2915487ad1e2f7d56508e1bd2f056995/data/tradingcalendar_2019_en.pdf` | 2026-09-29 | `f0a745897a1f3153a61a0ae8d3eda5245e79ef1376e8abcbb629fa81910504c9` | 683246 | **T1.** German-scope line with the futures carve-out: `Eurex is closed for trading and exercise in German equity derivatives and equity index options (trading in German equity index futures takes place!) as well as ETF and ETC derivatives, which are based on Xetra® listings: 10 June, 3 October`. |
| `tradingcalendar_2020_en.pdf` | `https://www.eurex.com/resource/blob/1690338/91db2a4864f0634f3ff1695ff0dddde5/data/tradingcalendar_2020_en.pdf` | 2026-09-29 | `5359f2632aa397a686615d2308fe145977ea42799c0819988d1c83ee8ca929be` | 206021 | **T1.** Same carve-out wording, `…: 1 June`. |
| `tradingcalendar_2021_en.pdf` | `https://www.eurex.com/resource/blob/2348622/f4f9a1b370f2e74462532319f2b15ddb/data/tradingcalendar_2021_en.pdf` | 2026-09-29 | `18a537935fbbf705a89485b428d525f3931467056d028a68a3d081e061b07cfd` | 153433 | **T1.** Same carve-out wording, `…: 24 May`. |
| `tradingcalendar_2022_en.pdf` | `https://www.eurex.com/resource/blob/2886140/a13cf78f8e10f826df3bf79278dd518a/data/tradingcalendar_2022_en.pdf` | 2026-09-29 | `395ab4adacb3a6596ba087f389365432cff1d63a7aadba5186a659aaf7f3b77f` | 156841 | **T1.** All-derivatives lists; **no German-scope line**. |
| `tradingcalendar_2023_en.pdf` | `https://www.eurex.com/resource/blob/3378814/910cf372738890f691bc1bfbccfd3aef/data/tradingcalendar_2023_en.pdf` | 2026-09-29 | `c1d936b4201a69d8dce24e12d97ad2d73f17f04f9e9f075511e1a74f8002892f` | 148077 | **T1.** All-derivatives lists; **no German-scope line**. |
| `tradingcalendar_2024_en.pdf` | `https://www.eurex.com/resource/blob/3816864/92a1dacec4476fdef2819750d932968a/data/tradingcalendar_2024_en.pdf` | 2026-09-29 | `9028606ab0b01bcf3d8dbae28ecd9b76984769f14eb2d6d0a6c136e2c227b7e2` | 168352 | **T1.** All-derivatives lists; **no German-scope line**. |

## German-scope line, edition by edition (full-text scan, 2026-10-03 UTC)

Extracted with `pdftotext` (`-layout` and `-raw`, cross-checked) from the PDFs above;
the scanned strings are the closure notes of the p.2 "Overview of holidays by
countries" panel, not the trading-hours footnote ("German Equity Options/LEPOs/Weekly
Options: 08:51–17:31"), which is not a closure statement.

| Edition | German-scope closure line | Dates |
|---|---|---|
| 2010 | none | — |
| 2011 | none | — |
| 2012 | none | — |
| 2013 | none | — |
| 2014 | `Eurex is closed for trading and exercise in German equity and equity index derivatives as well as ETF and ETC derivatives, which are based on Xetra® listings: 3 October` | 2014-10-03 |
| 2015 | none | — |
| 2016 | `… German equity and equity index derivatives … Xetra® listings: 16 May, 3 October` | 2016-05-16, 2016-10-03 |
| 2017 | `… German equity and equity index derivatives … Xetra® listings: 5 June, 3 October, 31 October` | 2017-06-05, 2017-10-03, 2017-10-31 |
| 2018 | `… German equity and equity index derivatives … Xetra® listings: 21 May, 3 October` | 2018-05-21, 2018-10-03 |
| 2019 | `Eurex is closed for trading and exercise in German equity derivatives and equity index options (trading in German equity index futures takes place!) as well as ETF and ETC derivatives, which are based on Xetra® listings: 10 June, 3 October` | futures trade — no closure in the benchmark-index-futures scope |
| 2020 | same carve-out wording, `… Xetra® listings: 1 June` | futures trade |
| 2021 | same carve-out wording, `… Xetra® listings: 24 May` | futures trade |
| 2022 | none | — |
| 2023 | none | — |
| 2024 | none | — |
