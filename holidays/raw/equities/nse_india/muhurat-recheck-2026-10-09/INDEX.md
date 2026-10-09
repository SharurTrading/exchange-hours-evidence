# nse_india — Muhurat re-check, 2026-10-09 UTC

A bounded third pass over the seven still-`Unsourced` Muhurat dates
(2011-10-26, 2012-11-13, 2013-11-03, 2014-10-23, 2017-10-19, 2019-10-27 and
the 2026-11-08 banner date). It closed negative on every angle and re-dated
the 2026 watch item. Two findings about the 2026-10-06 pass accompany it:

1. The 2026-10-06 sweep files `cdx_nseindia_cmtr.txt` and
   `cdx_nseindia_cmtr_lc.txt` (under `muhurat-recovery-2026-10-06/`) are an
   Internet Archive "Temporarily Offline" page and a "504 Gateway Time-out"
   page, not CDX rows — the apex-host (`nseindia.com`, no `www`) prefix sweep
   never completed in that pass. This pass completed it (files below); the CDX
   API canonicalises the `www.` and apex hosts onto one key set, so the
   completed sweep covers the same URL space the successful `www`/`www1`
   sweeps of 2026-10-06 already read.
2. The Wayback availability API answered `429 Too Many Requests` to every
   exact-URL probe this pass (seven `19187` path/host variants, including the
   `nseindia.com/content/cmtr/19187.pdf` family); the CDX queries below are
   the pass's evidence, and the prefix query `…/content/circulars/cmtr19`
   subsumes the exact URL `…/content/circulars/cmtr19187.pdf`.

## Angles and results

- **2011 (`NSE/CMTR/19187`).** `cdx_apex_cmtr19.txt` — the completed apex-host
  prefix sweep over download numbers 19xxx — holds nine rows and no 19187:
  only cmtr19013 (2011-10-27 capture), CMTR19075 (2011-12-16 replay),
  CMTR19431 (2011-12-16 replay), CMTR19539 (the 2012 list), CMTR19860.zip,
  CMTR19982, and three 2003-era `.wri` files. Negative, now on a completed
  sweep.
- **2012/2013/2014 windows.** `cdx_apex_cmtr2.txt` (147 rows, numbers 2xxxx)
  filtered to the Diwali issuance windows (20561+; 24200-24700; 27000-27500)
  shows only the rows the 2026-10-06 pass already knew: CMTR20561
  (2012-05-22), the CMTR24103-24137 September-2013 zip run, CMTR24121,
  CMTR24369/24377 (2014-04), and CMTR26919/26956/26986 (2014-07). No capture
  in any Muhurat window. Negative.
- **2017 window.** `cdx_apex_cmtr33.txt` — CMTR33424 (recovered 2026-10-06),
  CMTR33442, CMTR33746 (2017-07-04) and no PDF above it. Negative.
- **2019 window.** `cdx_apex_cmtr42.txt` — CMTR42010 and CMTR42070 (the
  September-2019 bulk capture) and nothing between it and CMTR42877. Negative.
- **`/content/cmtr/` path family.** `cdx_apex_content_cmtr_dir.txt` — zero
  rows; the directory family (e.g. `content/cmtr/19187.pdf`) has no captures
  at all. Negative.
- **2026 (`2026-11-08`).** The circular had not issued as of the retrieval:
  the operator's own live circulars channel
  (`https://www.nseindia.com/api/circulars?index=CM&fromDate=22-09-2026&toDate=09-10-2026`,
  answered HTTP 200 with a browser user-agent and cookie warm-up after the
  HTML pages still answered 403; saved as
  `nse_circulars_cm.live-20261009T213953Z.json`) lists 414 CM circulars from
  2026-09-22 through 2026-10-09 and not one names Muhurat or Diwali. The
  2025 edition issued 2025-09-22, 29 days before Diwali; this retrieval sits
  30 days before Diwali 2026-11-08, so the issuance window was opening as the
  query ran. Still the publication-season watch, not a gap; closing condition
  unchanged (the operator's circular).

## Files

- `cdx_apex_cmtr19.txt` — Wayback CDX, `url=nseindia.com/content/circulars/cmtr19`,
  `matchType=prefix`, `collapse=urlkey`, retrieved 2026-10-09 UTC.
- `cdx_apex_cmtr2.txt` — same query with prefix `cmtr2`.
- `cdx_apex_cmtr33.txt` — same query with prefix `cmtr33`.
- `cdx_apex_cmtr42.txt` — same query with prefix `cmtr42`.
- `cdx_apex_content_cmtr_dir.txt` — same query with prefix
  `nseindia.com/content/cmtr/` (zero rows).
- `nse_circulars_cm.live-20261009T213953Z.json` — the live circulars API
  response quoted above, exactly as served (sha256 in `SHA256SUMS.txt`).

Every row date above is 2026-10-09 UTC (LAW-UTC-DATES).
