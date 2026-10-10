# INDEX — `cfe-ic17-022` (the 2017 CFE Independence Day circular, recovered 2026-10-10 UTC)

Retrieval session: **2026-10-10 00:55–01:20 UTC** (`date -u`). All times UTC (LAW-UTC-DATES).

The crate's 2017-07-03 `Unsourced` marker closes: **CFE Information Circular IC17-022, "Modified
Trading Hours for Independence Day Holiday", dated June 16, 2017**, whose first schedule paragraph
reads, in session language, *"Modified Trading Schedule for Monday, July 3, 2017: Trading in all CFE
products will close at 12:15 p.m. on Monday, July 3, 2017."* It also states the July 4 and July 5
arrangements (extended `3:30 p.m. (Monday) to 10:30 a.m.` / regular `None` on the holiday; regular
`8:30 a.m. to 3:15 p.m.` opening `5:00 p.m. (Tuesday)` on July 5), corroborating the two rows
already keyed to the holiday-calendar page.

## How it was found and from where

1. `cfecirculars.com` — the channel the wave was sent to hunt — is dead: the domain does not
   resolve (NXDOMAIN), the Wayback CDX holds **zero** captures under every match type
   (`cdx-cfecirculars.com-empty.json`), and the Common Crawl index answers "No Captures found" for
   the 2017 collections queried (`cc-cfecirculars.com-2017-34-empty.json` is the CC-MAIN-2017-34
   response).
2. The operator's own circulars index on `cfe.cboe.com` **is** archived: the capture of
   `http://cfe.cboe.com/about-cfe/cfe-information-circulars` at `2017-08-20T09:31:45Z`
   (`cfe-information-circulars-index-2017-08-20.html`) lists, among others, *"June 16, 2017:
   CFEIC17-022 Modified Trading Hours for Independence Day Holiday"* linking
   `/publish/CFEinfocirc/CFEIC17-022.pdf`. That index page is the operator's own T1 statement that
   the circular existed, with its title and date.
3. The Wayback Machine has no capture of the PDF. Common Crawl **CC-MAIN-2017-34** crawled it on
   **2017-08-18T16:16:38Z** — index row: status 200, length 96563, WARC
   `crawl-data/CC-MAIN-2017-34/segments/1502886104704.64/warc/CC-MAIN-20170818160227-20170818180227-00487.warc.gz`,
   offset 75537381 (`cc-index-cfeinfocirc-CC-MAIN-2017-34.json` holds the full collection response).
   The record was fetched from `data.commoncrawl.org` by range request and decompressed;
   `cc-CC-MAIN-2017-34-record-20170818161638.warc` is the decompressed WARC record (108182 bytes)
   whose headers carry `WARC-Target-URI: http://cfe.cboe.com/publish/CFEinfocirc/CFEIC17-022.pdf`,
   `WARC-Date: 2017-08-18T16:16:38Z`, payload digest `sha1:UH2YZK6YULPT4VKAK6SFSS2BTQUEMN3T`, and
   the origin server's `Last-Modified: Fri, 16 Jun 2017 18:29:48 GMT` — the operator's own host
   answering with the file two days after its stated date.

## Artifacts

| file | sha256 | bytes | source url | capture (UTC) | what it is |
|---|---|---|---|---|---|
| `CFEIC17-022.pdf` | `5f85272f911637d2b5bd175854cb4caa40d0e9cc48ba903202a25b3172e3d618` | 107229 | http://cfe.cboe.com/publish/CFEinfocirc/CFEIC17-022.pdf (via Common Crawl CC-MAIN-2017-34, crawl 2017-08-18T16:16:38Z) | 2017-08-18T16:16:38Z (origin `Last-Modified` 2017-06-16T18:29:48Z) | **The circular.** T1. Six pages: the 12:15 p.m. CT July 3 close for all CFE products; VXT TAS end 12:13 (trade-type restriction, keys nothing, LAW-SESSION-NOT-EXPIRY); block-trade/ECRP reporting deadlines (not session boundaries); the Tuesday July 4 holiday chart (Extended 3:30 p.m. Mon – 10:30 a.m., Regular None); the July 5 column (Regular 8:30 a.m. – 3:15 p.m. after a 5:00 p.m. Tuesday open); and the full submission-window chart. |
| `CFEIC17-022.txt` | `bdf2b199e9dde796d316b17fb40e35ee9f01c34def2fd9b8fcd099bff80af378` | 9345 | derived | — | `pdftotext -layout` of the PDF beside it. |
| `cc-CC-MAIN-2017-34-record-20170818161638.warc` | `de1fdceee9d59b1b74583999b87090ac478e11eff81792624986e459b70f0742` | 108182 | data.commoncrawl.org range fetch, offset 75537381 | crawl 2017-08-18T16:16:38Z | The decompressed WARC response record — the provenance chain from the crawl to the PDF bytes. |
| `cc-index-cfeinfocirc-CC-MAIN-2017-34.json` | `c099cef63530b72360906dd51a3e907b9a48bc73a4dbe5b0fd222602fd46a597` | 13158 | index.commoncrawl.org CC-MAIN-2017-34 query `cfe.cboe.com/publish/CFEinfocirc/*` | live fetch 2026-10-10 01:05 | The collection index rows (29 URLs): the 022 row above, plus 029–032 crawled the same day. |
| `cfe-information-circulars-index-2017-08-20.html` | `1d73bb1f5711f6864c6d9755ba71466bad11fcd26bd3bc5784b5163cc19cb3fe` | 93886 | https://web.archive.org/web/20170820093145id_/http://cfe.cboe.com/about-cfe/cfe-information-circulars | Wayback capture 2017-08-20T09:31:45Z, replayed 2026-10-10 00:58 | The operator's circulars index naming CFEIC17-022 with its June 16, 2017 date and title, and IC17-054/055 (Christmas, New Year) for the same year. |
| `cdx-cfecirculars.com-empty.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 3 | CDX `cfecirculars.com matchType=domain` | live fetch 2026-10-10 00:56 | Empty result set — the domain the wave was sent to has no captures. |
| `cc-cfecirculars.com-2017-34-empty.json` | `64054e32f6705fb905dd4bc21018671a4f60848b95a8667e42975be413042481` | 55 | index.commoncrawl.org CC-MAIN-2017-34 query `cfecirculars.com/*` | live fetch 2026-10-10 00:57 | "No Captures found" (2017-13/34/43/51 all answered the same). |
