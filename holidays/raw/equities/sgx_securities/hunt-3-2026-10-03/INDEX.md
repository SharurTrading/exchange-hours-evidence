# sgx_securities hunt 3 — 2026-10-03 UTC — completed negative

Third retrieval pass on #213 (the 2011-08-01..2013-12-31 and
2020-01-02..2024-12-31 holiday capture gaps). Every angle named in the hunt
brief was swept with fresh surfaces; none surfaced an operator artifact
printing either span's closures. Retrieval instant for all fetches:
2026-10-03 08:56-09:45 UTC. Digests in `SHA256SUMS.txt`.

## Angles swept this pass

1. **Operator annual reports (the "investor information" premise).** The
   IR microsite `investorrelations.sgx.com` hosts the operator's own annual
   reports as `common/download/download.cfm` redirects onto Broadridge's
   `files.shareholder.com/downloads/ABEA-69RPAC/...` — a URL surface no
   earlier pass had enumerated. Complete archived PDFs exist for the FY2010,
   FY2011, FY2013, FY2014 and FY2016 reports (200-status captures listed in
   `cdx_files_shareholder_sgx.txt`). Retrieved whole and text-searched:
   `SGX_Annual_Report_2011.pdf` (capture 20170329023013, 69 796 words),
   `Singapore_Exchange_Annual_Report_2013.pdf` (capture 20130903162013,
   65 124 words) and, for the genre baseline, `SGX_AR07_CorporateSection.pdf`
   (capture 20081003120828, 50 pages). **All three contain zero occurrences
   of "holiday"** — SGX annual reports do not print public-holiday calendars,
   so the channel cannot key 2012/2013 or 2020-2024 rows no matter how many
   editions are archived. Negative on the premise, tested at three documents.
   The 2013-era `annuals.cfm` listing (`sgx-ir-annuals-20130818104810.html`)
   is saved as the provenance of the FY2012 fileid.
2. **Domain-wide CDX, now complete rather than sampled.** A full
   `holiday|calendar` urlkey filter across every sgx.com subdomain returns
   exactly **6 urlkeys for 2010-2014** (the securities and derivatives
   trading-hours pages in both portal eras plus CSS/dojo assets) and
   **43 for 2019-2025** (the same pages, their content-api queries, IR
   calendar-events pages, and unrelated assets) — no other operator calendar
   page, annual trading-schedule notice, or holiday announcement exists in
   the Wayback index for either gap era, at any URL name
   (`cdx_sgx_domain_holidaycal_2010-2014.txt`,
   `cdx_sgx_domain_holidaycal_2019-2025.txt`). This upgrades the earlier
   3 000-urlkey sample sweep to a complete negative.
3. **The WCM content tree of the sgxweb era.**
   `wps/wcm/connect/sgx_en/home/trading/securities/trading_hours_and_calendar*`
   holds exactly four captures — two 2022 SPA shells (captures
   `20220203161334` and `20220203161324`, both 200-status) and two 301
   redirects (`20220203161215` on 2022 and `20241213221530` on 2024-12-13) —
   all of the 2011-08-01 all-day-trading news item (fetched:
   `sgx-wcm-nonstop-...html`, itself a browser-upgrade/SPA shell with no
   holiday content). The domain-wide `wcm/connect ... holiday|public` filter
   (`cdx_sgx_wcm_holiday_public_all.txt`) holds 35 status-coded rows (a 36th
   row is truncated mid-URL by the crawler's save): the three known May-2009
   `2008+publicholidays` / `2009+public+holidays` / `World+Holidays` sheets,
   a 2017 REIT-index `Holiday Schedule` PDF (`SGX+APAC+ex+Japan+Dividend+
   Leaders+REIT+Index...`, capture 20170715132158 — an index publication, not
   a securities trading-schedule page, and 2017 lies inside the audited
   2014-2019 window in any case), and ~31 public-consultation/regulation/news
   rows matching the filter's `public` half. The securities WCM tree is
   capture-empty for both gaps.
4. **The wps SPA's own data channel, named by its bytes.** The SPA chunk
   captured at `wps/portal/sgxweb/home/trading/securities/
   index.81c0aad9d9cfe2d8e9a1.chunk.js` (capture 20211224084214, fetched)
   is the site bundle and names `api2.sgx.com` as its only data/asset host —
   the host whose 1 499 urlkeys the 2026-09-30 pass enumerated with no
   calendar shape. The 2020-2024 holiday data moved through a channel whose
   only archived response is the known `{"data":{"route":null}}`.
5. **Common Crawl record completed.** CC-MAIN-2022-05 exact-page query for
   the wps securities calendar (degraded on 2026-10-02): **"No Captures"**
   (`cc_CC-MAIN-2022-05_wps_exact.json`). Domain filters
   `sgx.com + holiday|calendar|trading_hours` for CC-MAIN-2021-43,
   CC-MAIN-2023-50 and CC-MAIN-2024-30: **zero captures** (the 2021-43 query
   502'd once and completed on retry). CC-MAIN-2012-26 does not exist under
   that name. The CC record for both gap eras is now complete-negative.
6. **`sgx.com.sg`** (never swept before): the `holiday|calendar` filtered
   query is empty (`cdx_sgxcomsg_holidaycal.txt` — the filtered dump is the
   saved record); the session-log enumeration of the legacy domain (804
   urlkeys, 2000-2006 era plus redirect shells) was not archived as a dump.
   Corrected 2026-10-03 UTC (PR #270 review): the 804 count is a session
   observation, not derivable from a saved artifact.

## Review corrections, 2026-10-03 UTC

The PR #270 second-retrieval review found the committed evidence sentence for
item 3 misstating these dumps ("all 2022 SPA shells"; the filter "surfaces
only the known May-2009 sheets"); item 3 above is restated to the dumps
themselves. `SHA256SUMS.txt` was reformatted the same day to the standard
two-space separator (all 22 digests re-verified OK) and its self-referential
line — the empty-string digest — dropped.

## Net

The 2020-2024 span is negative on every machine-reachable channel: Wayback
(complete domain filter), Common Crawl (2020/2021/2022/2023/2024 crawls),
the content API (enumerated + route:null), the WCM tree, the IR/Broadridge
annual-report channel, and web search. The 2011-08-01..2013-12-31 span is
likewise negative except the **human-side item**: the archive.today snapshot
`archive.li/20120910023452/...trading_hours_calendar` (existence proven
2026-10-02, captcha-blocked from this network) remains the one lead — skip
per the hunt charter, it is the maintainer's.

Closing conditions unchanged (issue #213; evidence file
`docs/evidence/sgx_securities.md`).
