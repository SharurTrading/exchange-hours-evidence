# cme-2019-2021-fix — evidence index (fixer round 1)

Task: corrections to `holidays/cme-2019-2021.json` after the adversarial verdict
`holidays/cme-2019-2021.verify.json` (verdict FAIL on evidence discipline).
Fix work performed **2026-09-12 UTC** (`date -u` → 2026-09-12T07:49:48Z).
Charter: exchange-hours-rs AGENTS.md (LAW-HOLIDAY-SCOPE, LAW-PRIMARY-SOURCES, LAW-UTC-DATES,
LAW-SESSION-NOT-EXPIRY). All documents below are CME Group's own published material — **tier T1** —
read through the Internet Archive raw replay (`https://web.archive.org/web/<ts>id_/<url>`),
because cmegroup.com returns 403 to this machine.

Every quotation used in the corrected rows was re-read by this fixer from the saved bytes with an
independently invoked `xlrd` dump (`/tmp/cols.py`, raw cell values plus column index), not from the
previous round's `text/` dumps and not from the verifier's transcription.

## New artifacts retrieved in this round

| Local path | URL | Archive capture (UTC, memento-datetime) | `x-archive-orig-last-modified` | sha256 |
|---|---|---|---|---|
| `docs/2020-holiday-calendars.zip` | https://www.cmegroup.com/tools-information/holiday-calendar/files/2020-holiday-calendars.zip | **2026-07-30T11:18:34Z** (ts `20260730111834`) | Tue, 29 Dec 2020 21:32:10 GMT | 5263a4a5e9076bc0e69c7cd0e3fd9f82dc4d80b66f1b56f14070f08c1d762b59 |
| `docs/2021-holiday-calendars.zip` | https://www.cmegroup.com/tools-information/holiday-calendar/files/2021-holiday-calendars.zip | **2026-08-30T10:03:27Z** (ts `20260830100327`) | Mon, 03 Jan 2022 21:29:08 GMT | 0ee0860a3a0e035eb9d079419aca3cafcc4256d296fa916647987c396dda8c59 |
| `docs/2019-thanksgiving-day-holiday-schedule-arragements.xlsx` | https://www.cmegroup.com/tools-information/holiday-calendar/files/2019-thanksgiving-day-holiday-schedule-arragements.xlsx | 2024-02-20T03:37:34Z (ts `20240220033734`) | Thu, 26 Dec 2019 12:24:03 GMT | 6e65b0989065c7636b54aa63f150243fe628e6fb4ae22f9854347c797f389758 |

Raw response headers for each are in `headers/`; sha256 of everything in this directory is in `shasum.txt`.
Both re-fetched ZIPs are **byte-identical** to the copies saved in `../cme-2019-2021/docs/` — the bytes
were always right; only the recorded capture dates were wrong (D3).

## Enumeration re-run in this round

| File | Query | Result |
|---|---|---|
| `cdx/cdx-2019-zip.json` | exact URL, 2019 annual ZIP | one capture only: `20210126094837` — confirms the previously recorded 2019 date |
| `cdx/cdx-2020-zip.json` | exact URL, 2020 annual ZIP | **one capture only: `20260730111834`** |
| `cdx/cdx-2021-zip.json` | exact URL, 2021 annual ZIP | **one capture only: `20260830100327`** |
| `cdx/cdx-arragements.json` | exact URL, thanksgiving "arragements" xlsx | captures `20240220033734` and `20251227221707` (same digest), plus a 301 |
| `cdx/cdx-2020-gf-compact.json` | exact URL, `2020-good-friday-holiday-compact.xls` | **`[]` — the archive holds no capture of this URL at all** |
| `cdx/cdx-files-2019-2023.json` | prefix `…/holiday-calendar/files/`, 2019-2023, collapse=urlkey | 224 rows; no 2020 Good Friday `.xls` under any name (only `2020-good-friday-advisory.pdf`) |
| `cdx/cdx-2020-mlk-day-schedule.xls.json` | exact URL | one capture: `20260815194202` |
| `cdx/cdx-2020-martin-luther-king-holiday-schedule-compact.xls.json` | exact URL | one capture: `20250827082154` |

## Disposition of the new document (D7)

`2019-thanksgiving-day-holiday-schedule-arragements.xlsx` — single sheet, "Execution List", headed
`NYMEX | Thanksgiving`, columns `Contract Title | Commodity Code | Rulebook Chapter | PRA Afffected |
2019-11-28 | 2019-11-29`, 33 BALMO / price-reporting-agency contract rows tick-marked against both dates
(e.g. "Mont Belvieu LDH Propane (OPIS) BALMO Futures | 8O | 296 | OPIS | ü | ü").
**It states no session instants and no open/close language.** It is a pricing-agency / expiry execution
list, so under LAW-SESSION-NOT-EXPIRY it keys no row. Recorded here only to close the enumeration gap.

## Corrections made to `../cme-2019-2021/INDEX.md` (same research store, not the rs repo)

- **D2** — `docs/2020-good-friday-holiday-compact.xls` is relabelled as a **failed retrieval**: it is
  4,749 bytes of HTML ("The Wayback Machine has not archived that URL"), sha256
  `2c10f98451635b204f24db82793e079dd4c806568333ff04137f154f6e8db1a2`, not a CME workbook. The file is
  left on disk unchanged so that `shasum.txt` still verifies 86/86, and the INDEX sentence claiming the
  `docs/` copies are byte-identical to the ZIP members is now qualified to exclude it. The genuine 2020
  Good Friday compact sheet is the ZIP member `zip2020/2020-good-friday-holiday-compact.xls`
  (sha256 `aa0936e9278904f40bc23abba57c2c379207af49d0cb6971f07289010fe1745e`), which is what every
  2020 Good Friday row cites. My own CDX (`cdx/cdx-2020-gf-compact.json`, and the 224-row prefix crawl)
  confirms no capture of that URL exists, so the retrieval could not have succeeded.
- **D3** — the 2020 and 2021 ZIP capture cells now read `2026-07-30T11:18:34Z` and `2026-08-30T10:03:27Z`
  with the operator's `Last-Modified` beside them, replacing "nearest-2021 replay" / "nearest-2022 replay".
- **D9** — the supplementary table's sha256 for `docs/2019-new-years-full-JAN2019.xls` is corrected from
  `2684…` (which is the *compact* sheet) to `6eafe7ee71c676299bd612eb3760d23d449c2111be8cee463d24308959e4d170`,
  re-hashed by this fixer.
- **D8** — an addendum in that INDEX now hashes and tabulates the files that were relied on but never
  manifested (the four archived `holiday-calendar.html` pages, the six CDX result files, `t1.xls`,
  `list.txt`, `dumpxls.py`, `fetch.sh`), and records the two missing `list.txt` capture times
  (`2020-mlk-day-schedule.xls` → 2026-08-15T19:42:02Z; `2020-martin-luther-king-holiday-schedule-compact.xls`
  → 2025-08-27T08:21:54Z). `t1.xls` is identified as a byte-identical duplicate of
  `docs/2021-presidents-compact.xls` (`7a8d5ce35c639998abf64723de2cc2d649dc015b1aa6cfc3bc326ab5cdfd0c4f`).

## Rows corrected in `../../cme-2019-2021.json` (previous round preserved as `cme-2019-2021.r0.json`)

See that file's `coverage` field for the full account. D1 (fabricated cross-year quotation), D4
(TOPIX row described as Nikkei, twice), D5 (11 instants re-quoted as printed), D6 (2021-12-23 derived
instants), D10 (16 family rows added: 6 on 2020-01-02, 10 Nikkei rows). Every one was re-read from the
`.xls` bytes already under `../cme-2019-2021/` (whose 86/86 hashes I did not disturb).
