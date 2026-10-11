#!/usr/bin/env python3
"""Review helper: immutable-head row counts and normalized holiday comparison."""
import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

class Events(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag = None
        self.buf = []
        self.events = []
    def handle_starttag(self, tag, attrs):
        if tag in ['h2', 'h3', 'h4', 'li']:
            self.tag = tag
            self.buf = []
    def handle_data(self, data):
        if self.tag:
            self.buf.append(data)
    def handle_endtag(self, tag):
        if tag == self.tag:
            self.events.append((tag, ' '.join(''.join(self.buf).split())))
            self.tag = None

def holiday_events(path):
    parser = Events()
    parser.feed(path.read_text())
    start = next(i for i, row in enumerate(parser.events) if row[1] == '2026')
    tail = parser.events[start:]
    end = next(i for i, row in enumerate(tail) if row[1] == 'Apply for an account today')
    return tail[:end]

p = argparse.ArgumentParser()
p.add_argument('library', type=Path)
p.add_argument('evidence', type=Path)
p.add_argument('head')
a = p.parse_args()
def at_head(path):
    return subprocess.check_output(['git', '-C', str(a.library), 'show', f'{a.head}:{path}'], text=True)
ledger = []
for line in at_head('docs/schedules/verification.md').splitlines():
    if line.startswith('| `'):
        cells = [x.strip() for x in line.split('|')[1:-1]]
        if len(cells) == 12 and cells[5] in ['served', 'dormant']:
            ledger.append(cells)
names = ['oanda_us_index_cfd', 'oanda_us_bond_cfd', 'oanda_us_commodity_cfd', 'oanda_metals', 'oanda_brent']
counts = {}
for name in names:
    text = at_head(f'src/calendar/schedules/holidays/{name}.rs')
    tuples = re.findall(r'^\s*\((202[56]), (\d+), (\d+), (.+), T1, "[^"]+"\),', text, re.M)
    counts[name] = len(tuples)
result = {'head': a.head, 'ledger_total': len(ledger), 'basis': dict(Counter(x[3] for x in ledger)), 'service': dict(Counter(x[5] for x in ledger)), 'holiday_rows': sum(x[7] != '—' for x in ledger), 'changed_oanda_table_counts': counts, 'changed_rows_total': sum(counts.values())}
cited = a.evidence / 'holidays/raw/oanda-uk-holiday-hours-2026-10-10/oanda-uk-holiday-trading-hours.html'
fresh = a.evidence / 'audits/oanda-pr334-independent-2026-10-11/current-holidays.html'
assert holiday_events(cited) == holiday_events(fresh)
result['holiday_events_compared'] = len(holiday_events(fresh))
result['cited_holiday_digest'] = hashlib.sha256(cited.read_bytes()).hexdigest()
result['fresh_holiday_digest'] = hashlib.sha256(fresh.read_bytes()).hexdigest()
print(json.dumps(result, indent=2))
