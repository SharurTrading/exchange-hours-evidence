"""Build the CDE 2021-2026 operator block from the saved notice bytes.

Every `verbatim` in the output is asserted to be a substring of the notice's
own pdftotext dump, so a quote that is not in the artifact cannot be emitted.
"""
import json, pathlib, re, sys

TXT = pathlib.Path("txt")

def text(ident):
    p = TXT / f"{ident}.txt"
    return p.read_text(errors="replace")

# (notice, event date, operator product group, status, exact printed cell, derived trade date, crate kind)
# `cell` must appear in the notice's own text.
OPS = [
    # ---- 2021 (FairX) ----
    ("21-03", "2021-07-05", "Equity Products and Energy Products", "closed",
     "Markets will be closed from 16:00 CT Friday, July 2nd", "2021-07-05", "closed"),
    ("21-04", "2021-09-06", "Equity Products and Energy Products", "closed",
     "Markets will be closed from 16:00 CT Friday, September 2nd", "2021-09-06", "closed"),
    ("21-06", "2021-11-25", "Equity Products", "closed", "Closed for holiday", "2021-11-25", "closed"),
    ("21-06", "2021-11-25", "Energy Products", "closed", "Closed for holiday", "2021-11-25", "closed"),
    ("21-06", "2021-11-26", "Equity Products", "early_close", "11/26 12:15 CT", "2021-11-26", "early_close"),
    ("21-06", "2021-11-26", "Energy Products", "early_close", "11/26 12:45 CT", "2021-11-26", "early_close"),
    ("21-07", "2021-12-24", "Equity Products", "closed", "Closed for holiday", "2021-12-24", "closed"),
    ("21-07", "2021-12-24", "Energy Products", "closed", "Closed for holiday", "2021-12-24", "closed"),
    # ---- 2022 ----
    ("22-01", "2022-01-17", "Equity Products", "closed", "Closed for holiday", "2022-01-17", "closed"),
    ("22-02", "2022-02-21", "Equity Products", "closed", "Closed for holiday", "2022-02-21", "closed"),
    ("22-04", "2022-04-15", "Equity Products", "closed", "Closed for holiday", "2022-04-15", "closed"),
    ("22-05", "2022-05-30", "Equity Products", "closed", "Closed for holiday", "2022-05-30", "closed"),
    ("22-06", "2022-06-20", "Equity Products", "closed", "Closed for holiday", "2022-06-20", "closed"),
    ("22-07", "2022-07-04", "Equity Products", "closed", "Closed for holiday", "2022-07-04", "closed"),
    ("22-08", "2022-09-05", "Equity Products", "closed", "Closed for holiday", "2022-09-05", "closed"),
    ("22-08", "2022-09-05", "Crypto Products", "closed", "Closed for holiday", "2022-09-05", "closed"),
    ("22-11", "2022-12-26", "Equity Products", "closed", "Closed for holiday", "2022-12-26", "closed"),
    ("23-01", "2023-01-02", "Equity Products", "closed", "Closed for holiday", "2023-01-02", "closed"),
    # ---- 2023 ----
    ("23-02", "2023-01-16", "Equity Products", "closed", "Closed for holiday", "2023-01-16", "closed"),
    ("23-03", "2023-02-20", "Equity Products", "closed", "Closed for holiday", "2023-02-20", "closed"),
    ("23-07", "2023-04-07", "Equity Products", "closed", "Closed for holiday", "2023-04-07", "closed"),
    ("23-09", "2023-05-29", "Equity Products", "closed", "Closed for holiday", "2023-05-29", "closed"),
    ("23-10", "2023-06-19", "Equity Products", "closed", "Closed for holiday", "2023-06-19", "closed"),
    ("23-10", "2023-06-19", "Crypto Products", "normal", "06/18 17:00 CT 06/19 16:00 CT", "2023-06-19", None),
    ("23-11", "2023-07-04", "Equity Products", "closed", "Closed for holiday", "2023-07-04", "closed"),
    ("23-13", "2023-09-04", "Equity Products", "closed", "Closed for holiday", "2023-09-04", "closed"),
    ("23-16", "2023-11-23", "Equity Products", "closed", "Closed for holiday", "2023-11-23", "closed"),
    ("23-16", "2023-11-24", "Equity Products", "early_close", "11/24 12:15 CT", "2023-11-24", "early_close"),
    ("23-16", "2023-11-24", "Energy Products", "early_close", "11/24 12:45 CT", "2023-11-24", "early_close"),
    ("23-16", "2023-11-24", "Crypto Products", "early_close", "11/24 12:45 CT", "2023-11-24", "early_close"),
    ("23-19", "2023-12-25", "Equity Products", "closed", "Closed for holiday", "2023-12-25", "closed"),
    ("23-20", "2024-01-01", "Equity Products", "closed", "Closed for holiday", "2024-01-01", "closed"),
    # ---- 2024 ----
    ("24-01", "2024-01-15", "Crypto Products", "closed", "Closed for", "2024-01-15", "closed"),
    ("24-02", "2024-02-19", "Crypto Products", "closed", "Closed for", "2024-02-19", "closed"),
    ("24-04", "2024-03-29", "Crypto Products", "closed", "Closed for holiday", "2024-03-29", "closed"),
    ("24-09", "2024-05-27", "Crypto Products", "closed", "Closed for", "2024-05-27", "closed"),
    ("24-12", "2024-06-19", "Energy Products", "closed", "Closed for", "2024-06-19", "closed"),
    ("24-12", "2024-06-19", "Crypto Products", "normal", "06/18 17:00 CT 06/19 16:00 CT", "2024-06-19", None),
    ("24-13", "2024-07-04", "Energy Products", "closed", "Closed for", "2024-07-04", "closed"),
    ("24-16", "2024-09-02", "Energy Products", "closed", "Closed for", "2024-09-02", "closed"),
    ("24-21", "2024-11-28", "Energy Products", "closed", "Closed for", "2024-11-28", "closed"),
    ("24-21", "2024-11-29", "Energy Products", "early_close", "11/29 13:45 CT", "2024-11-29", "early_close"),
    ("24-21", "2024-11-29", "Metal Products", "early_close", "11/29 13:45 CT", "2024-11-29", "early_close"),
    ("24-21", "2024-11-29", "Crypto Products", "early_close", "11/29 13:45 CT", "2024-11-29", "early_close"),
    ("24-23", "2024-12-24", "Energy Products", "early_close", "12/24 12:45 CT", "2024-12-24", "early_close"),
    ("24-23", "2024-12-24", "Metal Products", "early_close", "12/24 12:45 CT", "2024-12-24", "early_close"),
    ("24-23", "2024-12-24", "Crypto Products", "normal", "12/23 17:00 CT 12/24 16:00 CT", "2024-12-24", None),
    ("24-23", "2024-12-25", "Energy Products", "closed", "Closed for", "2024-12-25", "closed"),
    ("24-25", "2025-01-01", "Crypto Products", "closed", "Closed for holiday", "2025-01-01", "closed"),
    # ---- 2025 ----
    ("25-01", "2025-01-20", "Energy Products", "closed", "Closed for", "2025-01-20", "closed"),
    ("25-03", "2025-02-17", "Energy Products", "closed", "Closed for", "2025-02-17", "closed"),
    ("25-15", "2025-04-18", "Energy Products", "closed", "Closed for", "2025-04-18", "closed"),
    ("25-18", "2025-05-26", "Energy & Metal", "closed", "Closed for", "2025-05-26", "closed"),
    ("25-20", "2025-06-19", "Energy & Metal", "closed", "Closed for holiday", "2025-06-19", "closed"),
    ("25-20", "2025-06-19", "23x5 Crypto", "normal", "06/18 17:00 CT 06/19 16:00 CT", "2025-06-19", None),
    ("25-21", "2025-07-04", "Energy & Metal", "closed", "Closed for holiday", "2025-07-04", "closed"),
    ("25-29", "2025-09-01", "Energy & Metal", "closed", "Closed for holiday", "2025-09-01", "closed"),
    ("25-37", "2025-11-27", "Energy & Metal", "closed", "Closed for holiday", "2025-11-27", "closed"),
    ("25-37", "2025-11-28", "Energy & Metal", "early_close", "11/28 13:45 CT", "2025-11-28", "early_close"),
    ("25-37", "2025-11-28", "Equity", "early_close", "11/28 12:15 CT", "2025-11-28", "early_close"),
    ("25-37", "2025-11-28", "23x5 Crypto", "normal", "11/27 17:00 CT 11/28 16:00 CT", "2025-11-28", None),
    ("25-41", "2025-12-24", "Energy & Metal", "early_close", "12/24 12:45 CT", "2025-12-24", "early_close"),
    ("25-41", "2025-12-24", "Equity", "early_close", "12/24 12:15 CT", "2025-12-24", "early_close"),
    ("25-41", "2025-12-25", "Energy & Metal", "closed", "Closed for holiday", "2025-12-25", "closed"),
    ("25-42", "2026-01-01", "Energy & Metal", "closed", "Closed for holiday", "2026-01-01", "closed"),
    # ---- 2026 (already shipped; rebuilt here to prove the derivation reproduces it) ----
    ("26-01", "2026-01-19", "Energy, Metal & Equity", "closed", "Closed for holiday", "2026-01-19", "closed"),
    ("26-05", "2026-02-16", "Energy, Metal & Equity", "closed", "Closed for holiday", "2026-02-16", "closed"),
    ("26-12", "2026-04-03", "Energy, Metal & Equity", "closed", "Closed for holiday", "2026-04-03", "closed"),
    ("26-23", "2026-05-25", "Energy, Metal & Equity", "closed", "Closed for holiday", "2026-05-25", "closed"),
    ("26-27.1", "2026-06-19", "23x5 Products", "closed", "Closed for holiday", "2026-06-19", "closed"),
    ("26-29", "2026-07-03", "23x5 Products", "closed", "Closed for holiday", "2026-07-03", "closed"),
    ("26-36", "2026-09-07", "23x5 Products", "closed", "Closed for holiday", "2026-09-07", "closed"),
]

def flat(s):
    return re.sub(r"\s+", " ", s)

failures = []
for notice, event, group, status, cell, trade_date, kind in OPS:
    if flat(cell) not in flat(text(notice)):
        failures.append((notice, cell))
if failures:
    print("VERBATIM NOT FOUND IN ARTIFACT:")
    for n, c in failures:
        print(f"   {n}: {c!r}")
    sys.exit(1)
print(f"all {len(OPS)} operator statements verified as substrings of their notice dumps")

# ---------------------------------------------------------------------------
# Derived venue rows: the 23x5 grid every CDE product group shares. A date on
# which any group closes is Closed; where none closes but any early-closes, the
# row takes the EARLIEST close (the intersection), so the venue never reports a
# window in which no product prints.
# ---------------------------------------------------------------------------
VENUE_ROWS = [
    ("2021-07-05", "closed", None, "CDE-MN-21-03"),
    ("2021-09-06", "closed", None, "CDE-MN-21-04"),
    ("2021-11-25", "closed", None, "CDE-MN-21-06"),
    ("2021-11-26", "early_close", 12 * 3600 + 15 * 60, "CDE-MN-21-06"),
    ("2021-12-24", "closed", None, "CDE-MN-21-07"),
    ("2022-01-17", "closed", None, "CDE-MN-22-01"),
    ("2022-02-21", "closed", None, "CDE-MN-22-02"),
    ("2022-04-15", "closed", None, "CDE-MN-22-04"),
    ("2022-05-30", "closed", None, "CDE-MN-22-05"),
    ("2022-06-20", "closed", None, "CDE-MN-22-06"),
    ("2022-07-04", "closed", None, "CDE-MN-22-07"),
    ("2022-09-05", "closed", None, "CDE-MN-22-08"),
    ("2022-11-24", "unsourced", None, "CDE-NOTICES-INDEX-2026-09-19"),
    ("2022-11-25", "unsourced", None, "CDE-NOTICES-INDEX-2026-09-19"),
    ("2022-12-26", "closed", None, "CDE-MN-22-11"),
    ("2023-01-02", "closed", None, "CDE-MN-23-01"),
    ("2023-01-16", "closed", None, "CDE-MN-23-02"),
    ("2023-02-20", "closed", None, "CDE-MN-23-03"),
    ("2023-04-07", "closed", None, "CDE-MN-23-07"),
    ("2023-05-29", "closed", None, "CDE-MN-23-09"),
    ("2023-06-19", "closed", None, "CDE-MN-23-10"),
    ("2023-07-04", "closed", None, "CDE-MN-23-11"),
    ("2023-09-04", "closed", None, "CDE-MN-23-13"),
    ("2023-11-23", "closed", None, "CDE-MN-23-16"),
    ("2023-11-24", "early_close", 12 * 3600 + 15 * 60, "CDE-MN-23-16"),
    ("2023-12-25", "closed", None, "CDE-MN-23-19"),
    ("2024-01-01", "closed", None, "CDE-MN-23-20"),
    ("2024-01-15", "closed", None, "CDE-MN-24-01"),
    ("2024-02-19", "closed", None, "CDE-MN-24-02"),
    ("2024-03-29", "closed", None, "CDE-MN-24-04"),
    ("2024-05-27", "closed", None, "CDE-MN-24-09"),
    ("2024-06-19", "closed", None, "CDE-MN-24-12"),
    ("2024-07-04", "closed", None, "CDE-MN-24-13"),
    ("2024-09-02", "closed", None, "CDE-MN-24-16"),
    ("2024-11-28", "closed", None, "CDE-MN-24-21"),
    ("2024-11-29", "early_close", 13 * 3600 + 45 * 60, "CDE-MN-24-21"),
    ("2024-12-24", "early_close", 12 * 3600 + 45 * 60, "CDE-MN-24-23"),
    ("2024-12-25", "closed", None, "CDE-MN-24-23"),
    ("2025-01-01", "closed", None, "CDE-MN-24-25"),
    ("2025-01-20", "closed", None, "CDE-MN-25-01"),
    ("2025-02-17", "closed", None, "CDE-MN-25-03"),
    ("2025-04-18", "closed", None, "CDE-MN-25-15"),
    ("2025-05-26", "closed", None, "CDE-MN-25-18"),
    ("2025-06-19", "closed", None, "CDE-MN-25-20"),
    ("2025-07-04", "closed", None, "CDE-MN-25-21"),
    ("2025-09-01", "closed", None, "CDE-MN-25-29"),
    ("2025-11-27", "closed", None, "CDE-MN-25-37"),
    ("2025-11-28", "early_close", 12 * 3600 + 15 * 60, "CDE-MN-25-37"),
    ("2025-12-24", "early_close", 12 * 3600 + 15 * 60, "CDE-MN-25-41"),
    ("2025-12-25", "closed", None, "CDE-MN-25-41"),
    ("2026-01-01", "closed", None, "CDE-MN-25-42"),
    ("2026-01-19", "closed", None, "CDE-MN-26-01"),
    ("2026-02-16", "closed", None, "CDE-MN-26-05"),
    ("2026-04-03", "closed", None, "CDE-MN-26-12"),
    ("2026-05-25", "closed", None, "CDE-MN-26-23"),
    ("2026-06-19", "closed", None, "CDE-MN-26-27.1"),
    ("2026-07-03", "closed", None, "CDE-MN-26-29"),
    ("2026-09-07", "closed", None, "CDE-MN-26-36"),
]

# Recompute the intersection from the flagged operator statements and require
# it to reproduce the table above.
STAMP = re.compile(r"(\d{2})/(\d{2})\s+(\d{2}):(\d{2})\s+CT")
derived = {}
by_date = {}
for notice, event, group, status, cell, trade_date, kind in OPS:
    if kind is None:
        continue
    by_date.setdefault(trade_date, []).append((notice, status, flat(cell)))
for trade_date, entries in sorted(by_date.items()):
    if any(s == "closed" for _, s, _ in entries):
        derived[trade_date] = ("closed", None)
    else:
        instants = []
        for _, s, c in entries:
            if s == "early_close":
                hits = STAMP.findall(c)
                # the cell is "MM/DD HH:MM CT"; take the last stamp on the line
                hh, mm = int(hits[-1][2]), int(hits[-1][3])
                instants.append(hh * 3600 + mm * 60)
        derived[trade_date] = ("early_close", min(instants)) if instants else ("normal", None)
# the two unreadable 2022 Thanksgiving dates
derived["2022-11-24"] = ("unsourced", None)
derived["2022-11-25"] = ("unsourced", None)

expected = {d: (k, i) for d, k, i, _ in VENUE_ROWS}
assert derived == expected, (
    "derivation mismatch:\n  only derived: "
    + str({k: v for k, v in derived.items() if expected.get(k) != v})
    + "\n  only expected: "
    + str({k: v for k, v in expected.items() if derived.get(k) != v})
)
print(f"venue derivation recomputed from the operator statements: {len(derived)} rows, all match")

documents = {
    "CDE-NOTICES-INDEX-2026-09-19":
        "Coinbase Derivatives Market Notices listing, coinbase.com/derivatives/market-notices, "
        "read 2026-09-19 (client-rendered bytes via r.jina.ai, x-respond-with: html). Establishes "
        "which notices the operator published; notice 22-10 is listed but its PDF is unreachable.",
    "CDE-NOTICES-PAGE-2022-12-15":
        "Wayback capture 20221215074037 of coinbase.com/derivatives/market-notices, the archived "
        "listing that carries the 2021-2022 notice PDF hrefs.",
}
for notice, _e, _g, _s, _c, _d, _k in OPS:
    documents.setdefault(f"CDE-MN-{notice}", f"Coinbase Derivatives Market Notice {notice}")
# Retrieved and read, but keying no row; recorded so the evidence prose that
# cites them resolves to bytes.
documents["CDE-MN-24-26"] = (
    "Coinbase Derivatives Market Notice 24-26, an UNPLANNED technical early close on 2024-12-24. "
    "Keys no row; see missing[2]."
)
documents["CDE-MN-24-27"] = (
    "Coinbase Derivatives Market Notice 24-27, which states the 2025-01-09 National Day of "
    "Mourning session 'will observe a normal trading day'. Keys no row; see missing[3]."
)
documents["CDE-MN-26-27"] = (
    "Coinbase Derivatives Market Notice 26-27, superseded by 26-27.1 (which moved Gold and Silver "
    "into the 24x7 tier on trade date 2026-06-15). Kept for lineage."
)

block = {
    "task": "cde-2021-2026",
    "coverage":
        "Retrieved 2026-09-19 02:02-02:4x UTC (LAW-UTC-DATES). Bytes + INDEX.md under "
        "../exchange-hours-research/holidays/raw/cde-2021-2025/. Covers every CDE holiday "
        "notice from the venue's first trade date (2021-06-28) through 2026-09-07, the end of "
        "the window already shipped. 53 of 54 listed holiday notices retrieved live at T1; "
        "notice 22-10 (Thanksgiving 2022) is listed by the operator but its PDF is unreachable.",
    "holidays": [],
    "missing": [
        "Notice 22-10 (2022 Thanksgiving) is listed by the operator (id 22-10, category Holiday, "
        "posted 12/12/2022, subject 'Market Notice - Thanksgiving Holiday Schedule 2022') but its "
        "link is a dead info.fairx.com page: the host fails TLS and the Wayback Machine holds no "
        "capture of it. Trade dates 2022-11-24 and 2022-11-25 are therefore Unsourced rather than "
        "claimed closed. Closed by: any surviving copy of notice 22-10, or a later notice that "
        "restates the outgoing 2022 schedule. Tracked as issue #112.",
        "Trade date 2021-12-31 (Friday) carries no notice. The operator's own listing is complete "
        "for 2021 (21-01..21-07, no id gaps) and it published a notice for every other observed "
        "holiday, so the date is carried as audited normal. New Year's Day 2022 fell on a Saturday "
        "and the 23x5 grid has no Saturday session. Residual risk: an unpublished closure would be "
        "under-reported here.",
        "Notice 24-26 records an UNPLANNED early close: 'On December 24, 2024, Coinbase Derivatives "
        "Crypto Futures markets closed early at 14:30 CT due to a technical issue.' It is a venue "
        "incident rather than a published holiday schedule, which is the operative reason it keys "
        "no row; trade date 2024-12-24 takes its row from notice 24-23, the published Christmas "
        "schedule, whose earliest grid close is 12:45 CT anyway.",
        "Notice 24-27 states that trade date 2025-01-09 (a National Day of Mourning) 'will observe "
        "a normal trading day'. It is an audited-normal date and ships no row.",
        "Notice 21-04 (Labor Day 2021) prints 'closed from 16:00 CT Friday, September 2nd', but "
        "2021-09-02 was a Thursday and the Friday before Labor Day was 2021-09-03. The subject "
        "('Labor Day Observed Monday, September 6th, 2021'), the Monday-17:00 reopening sentence "
        "and the identical construction in notice 21-03 all place the closure on the Monday, so "
        "2021-09-06 is the affected trade date. Read literally the start instant would also close "
        "trade date 2021-09-03; that date is carried as audited normal and is the one residual "
        "source ambiguity in the window.",
        "Notice 24-12 (Juneteenth 2024) is headed 'Market Notice | IN DRAFT' in the operator's own "
        "published PDF, the only notice in the corpus that is. It is listed by the operator at T1 "
        "with a posted date and its grid is unambiguous, and a wrongly-shipped closure errs toward "
        "closed, so trade date 2024-06-19 ships Closed. Residual risk: a later final revision is "
        "not held. Closed by: a non-draft copy of 24-12. Tracked as issue #112.",
    ],
    "crate_rows": [
        {"trade_date": d, "kind": k, "close_ssm": i, "document": doc}
        for d, k, i, doc in VENUE_ROWS
    ],
    "documents": documents,
}
# The canonical location the evidence file cites and both tools read.
OUT = pathlib.Path(__file__).resolve().parents[2] / "cde-2021-2026.json"
OUT.write_text(json.dumps(block, ensure_ascii=False, indent=1))
print(f"wrote {OUT.name}: {len(VENUE_ROWS)} crate rows, "
      f"{sum(1 for r in VENUE_ROWS if r[1]=='closed')} closed, "
      f"{sum(1 for r in VENUE_ROWS if r[1]=='early_close')} early close, "
      f"{sum(1 for r in VENUE_ROWS if r[1]=='unsourced')} unsourced")
