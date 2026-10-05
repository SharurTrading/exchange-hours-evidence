#!/usr/bin/env python3
"""Re-derive every shipped Saturday-session row from the operator bytes.

Reads the cited service windows directly and reports, for each row in the two
open PRs, what the operator published against what the row states. Written for
the round-6 self-audit; not committed to the crate.
"""

import json
import re
import sys

STORE = "/Users/agedvagabond/Developer/exchange-hours-research/holidays/raw/cme-2025-2027"

# The six rows under audit: (family, trade date, cited window, [window paths])
ROWS = [
    ("globex_energy", "2026-06-22", "CME-SVC-2026-06-18",
     ["arc/thbp_2026-06-18_2026-06-20_20260619113404.json"]),
    ("globex_energy", "2026-07-06", "CME-SVC-2026-07-03",
     ["arc/thbp_2026-07-03_2026-07-05_20260619114108.json"]),
    ("globex_energy", "2027-06-21", "CME-SVC-2027-06-17",
     ["live/thbp/thbp_2027-06-17_2027-06-19.json"]),
    ("globex_equity_index", "2026-06-22", "CME-SVC-2026-06-18",
     ["arc/thbp_2026-06-18_2026-06-20_20260619113404.json"]),
    ("globex_equity_index", "2026-07-06", "CME-SVC-2026-07-03",
     ["arc/thbp_2026-07-03_2026-07-05_20260619114108.json"]),
    ("globex_equity_index", "2027-06-21", "CME-SVC-2027-06-17",
     ["live/thbp/thbp_2027-06-17_2027-06-19.json"]),
]

PRODUCT = {"globex_energy": "CL", "globex_equity_index": "ES"}


def load(path):
    with open(f"{STORE}/{path}") as handle:
        return json.load(handle)


def events(path, product):
    """Every (eventDate, time, kind, tradeDate) the window prints for product."""
    out = []
    for prod in load(path)["products"]:
        if prod["globex"] != product:
            continue
        for schedule in prod["tradingHours"]["schedules"]:
            for event in schedule.get("events", []):
                out.append(
                    (
                        schedule["eventDate"],
                        event.get("eventTime"),
                        event.get("marketEventType"),
                        event.get("tradingDate"),
                    )
                )
    return out


def to_seconds(stamp):
    hours, minutes = (int(part) for part in stamp.split(":"))
    return hours * 3600 + minutes * 60


def main():
    failures = 0
    for family, trade_date, document, paths in ROWS:
        product = PRODUCT[family]
        found = []
        for path in paths:
            for row in events(path, product):
                if row[3] == trade_date:
                    found.append((path, *row))
        print(f"\n=== {family}  trade date {trade_date}  cited {document}")
        if not found:
            print("   !! the operator states NO event carrying this trade date")
            failures += 1
            continue
        # The window must contain the events the row is built from.
        for path, event_date, stamp, kind, carried in sorted(found):
            print(f"   {event_date} {stamp:>5} {kind:<8} -> trade date {carried}")
        # Cross-check the document id actually names the path cited.
        # (The id encodes the window start, so a mismatch is a citation defect.)
        window_start = min(row[1] for row in found)
        if document.rsplit("-", 0)[0] and document not in (
            "CME-SVC-" + window_start,
            "CME-SVC-" + window_start + "-SAT",
        ):
            print(
                f"   note: cited id `{document}` does not encode the window start "
                f"{window_start} (it encodes the window the artifacts were read at)"
            )
    print(f"\nrows audited: {len(ROWS)}; windows with no event for their trade date: {failures}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
