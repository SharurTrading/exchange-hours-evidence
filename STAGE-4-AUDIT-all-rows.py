#!/usr/bin/env python3
"""Re-derive every shipped Saturday-session row from the operator bytes.

Second-pass audit, round 18. For each family branch it reads the row out of the
module source, resolves the row's cited document id through the evidence file's
`### Documents` table to a saved artifact, and checks that the artifact really
carries events against the row's trade date.

Deliberately does NOT read the module's block set: the point is to check the
row's date and citation against the bytes, independently of the code that
consumes them.
"""

import hashlib
import json
import os
import re
import subprocess
import sys

REPO = "/Users/agedvagabond/Developer/exchange-hours-rs"
# The window artifacts are spread across several era directories, not just the
# headline one: `probeB_*` under `cme-2025-2027-repair/live` and
# `cme-2025-2027-verify-r2/live` also hold them. Search the whole raw tree.
STORE = "/Users/agedvagabond/Developer/exchange-hours-research/holidays/raw"

# branch -> (family module, holiday module, evidence file, product)
TARGETS = [
    ("stage-4-energy", "globex_energy", "CL", "globex_energy.md"),
    ("stage-4-equity-index", "globex_equity_index", "ES", "globex_equity_index.md"),
    ("stage-4-rates-fx", "globex_interest_rates", "ZN", "globex_interest_rates.md"),
    ("stage-4-rates-fx", "globex_fx", "6E", "globex_fx.md"),
    ("stage-4-nikkei", "globex_nikkei_225_dollar", "NKD", "globex_nikkei_225_dollar.md"),
]


def show(branch, path):
    return subprocess.run(
        ["git", "-C", REPO, "show", f"origin/{branch}:{path}"],
        capture_output=True, text=True, check=True,
    ).stdout


def rows_for(branch, module, product):
    """(trade_date, document) for every replacement row the module ships."""
    text = show(branch, f"src/calendar/schedules/holidays/{module}.rs")
    found = []
    for match in re.finditer(
        r"\((\d{4}), (\d+), (\d+), ReplacementBlocks\(&[A-Z_]+\), (T1|T2), \"([^\"]+)\"\)",
        text,
    ):
        y, m, d, tier, doc = match.groups()
        digest = None
        found.append((f"{y}-{int(m):02d}-{int(d):02d}", doc, tier, digest))
    return found


def documents(branch, evidence):
    """document id -> set of artifact paths, from the evidence file's tables."""
    text = show(branch, f"docs/evidence/{evidence}")
    out = {}
    for line in text.splitlines():
        if not line.startswith("| `") or line.count("|") < 5:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        doc = cells[0].strip("`")
        url = cells[2] if len(cells) > 2 else ""
        digest = ""
        for cell in reversed(cells):
            m = re.fullmatch(r"`([0-9a-f]{64})`", cell)
            if m:
                digest = m.group(1)
                break
        out.setdefault(doc, []).append((url, digest))
    return out


# The two service product sets the store holds windows for, and the prefixes
# their artifacts use. A window exists in both; only one carries a given
# product, so the artifact must be chosen by the product being audited.
HEADLINE = "thbp"
SECOND = "extra"


def artifact_for(doc, start, product):
    """Find the saved artifact for `start` that carries `product`."""
    # `CME-SVC-B-...` ids name the second product set; the others the headline
    # set. The prefix is a hint, not the test — the product list decides.
    preferred = SECOND if "-B-" in doc else HEADLINE
    candidates = []
    for root, _, files in os.walk(STORE):
        for name in files:
            if name.endswith((".json.gz", ".raw")) or not name.endswith((".json", ".md")):
                continue
            # Any saved artifact whose name carries the window start. The store
            # names these windows several ways over its history (`thbp_`,
            # `extra_`, `probeB_`), so the name is not a filter beyond the date.
            if start not in name:
                continue
            candidates.append((os.path.join(root, name),
                               "json" if name.endswith(".json") else "reader"))
    # Prefer the hinted set, then any candidate that actually carries the product.
    candidates.sort(key=lambda c: 0 if os.path.basename(c[0]).startswith(preferred) else 1)
    for path, kind in candidates:
        if any(e[3] for e in events(path, kind, product)) or events(path, kind, product):
            return path, kind
    return None


def by_digest(digest):
    """(path, kind) for the saved artifact whose sha256 is `digest`."""
    for root, _, files in os.walk(STORE):
        for name in files:
            if name.endswith((".raw",)):
                continue
            path = os.path.join(root, name)
            try:
                with open(path, "rb") as handle:
                    h = hashlib.sha256(handle.read()).hexdigest()
            except OSError:
                continue
            if h == digest:
                return path, ("json" if name.endswith(".json") else "reader")
    return None


def events(path, kind, product):
    """(eventDate, time, marketEventType, tradeDate) tuples for `product`."""
    if kind == "json":
        with open(path) as handle:
            data = json.load(handle)
    else:
        raw = open(path, errors="replace").read()
        marker = "Markdown Content:"
        if marker in raw:
            data = json.loads(raw[raw.index(marker) + len(marker):].strip())
        else:
            # A reader-rendered page that carries the JSON body after its prose.
            start = raw.find('{"props"')
            if start < 0:
                return []
            data = json.loads(raw[start:].strip())
    out = []
    for prod in data.get("products", []):
        if prod.get("globex") != product:
            continue
        for schedule in prod.get("tradingHours", {}).get("schedules", []):
            for event in schedule.get("events", []):
                out.append((schedule["eventDate"], event.get("eventTime"),
                            event.get("marketEventType"), event.get("tradingDate")))
    return out


def main():
    failures = []
    checked = 0
    for branch, module, product, evidence in TARGETS:
        rows = rows_for(branch, module, product)
        docs = documents(branch, evidence)
        print(f"\n=== {branch} :: {module} ({product}) — {len(rows)} replacement rows")
        if not rows:
            failures.append(f"{branch}/{module}: no replacement rows found")
            continue
        for trade_date, doc, tier, digest in rows:
            checked += 1
            urls = docs.get(doc)
            digest = next((d for _, d in (urls or []) if d), "") or DIGESTS.get(doc, "")
            if urls is None:
                failures.append(f"{module} {trade_date}: document `{doc}` not in {evidence}")
                print(f"  {trade_date}  {doc:<24} !! not in the evidence file")
                continue
            start = re.search(r"(\d{4}-\d{2}-\d{2})$", doc).group(1)
            found = (by_digest(digest) if digest else None) or artifact_for(doc, start, product)
            if not found:
                failures.append(f"{module} {trade_date}: no saved artifact for `{doc}`")
                print(f"  {trade_date}  {doc:<24} !! no saved artifact")
                continue
            path, kind = found
            evs = [e for e in events(path, kind, product) if e[3] == trade_date]
            sat = sorted({e[0] for e in evs})
            kinds = sorted({e[1] + " " + (e[2] or "") for e in evs})
            ok = bool(evs)
            if not ok:
                failures.append(
                    f"{module} {trade_date}: {os.path.basename(path)} carries no "
                    f"{product} event against that trade date"
                )
            print(f"  {trade_date}  {doc:<24} {os.path.basename(path):<52} "
                  f"{'OK' if ok else '!!'}  events on {sat[:3]}  {kinds[:3]}")
    print(f"\nrows re-derived: {checked}; failures: {len(failures)}")
    for f in failures:
        print("  FAIL:", f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
