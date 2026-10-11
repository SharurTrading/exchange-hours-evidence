#!/usr/bin/env python3
"""Reproduce source digests, Carter context and independent zone conversions."""
from datetime import datetime
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo
import json
import sys

class OperatorText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
    def handle_data(self, text):
        if not self.skip:
            self.text.append(text)

store = Path(sys.argv[1])
head = sys.argv[2]
root = store / 'normal-weeks/oanda-uk-wayback-audit-2026-10-11/holiday-captures'
rows = []
for stamp in ('20250326184653', '20260217213704'):
    raw = (root / (stamp + '.html')).read_bytes()
    parser = OperatorText()
    parser.feed(raw.decode())
    text = ' '.join(' '.join(parser.text).split())
    quote = 'US index close early at 9:30 and reopen at 18:00'
    assert quote in text
    index = text.index(quote)
    rows.append({'capture': stamp, 'sha256': sha256(raw).hexdigest(),
                 'carter_context': text[index-85:index+310],
                 'eastern_time_present': 'Eastern Time' in text})

def utc(text, zone):
    return datetime.fromisoformat(text).replace(tzinfo=ZoneInfo(zone)).astimezone(ZoneInfo('UTC')).isoformat()

pdf = store / 'normal-weeks/oanda-uk-hours-2026-10-10/oanda-uk-hours-of-operation.pdf'
result = {'head': head, 'carter_captures': rows,
          'carter_utc': {'close': utc('2025-01-09T09:30:00', 'America/New_York'),
                         'following_trade_date_open': utc('2025-01-09T18:00:00', 'America/New_York'),
                         'following_trade_date_close': utc('2025-01-10T16:59:00', 'America/New_York')},
          'current_pdf_sha256': sha256(pdf.read_bytes()).hexdigest(),
          'named_zone_samples': {
              'sydney_summer_marked_close': utc('2026-10-13T07:59:00', 'Australia/Sydney'),
              'sydney_winter_marked_close': utc('2027-06-01T06:59:00', 'Australia/Sydney'),
              'frankfurt_summer_marked_open': utc('2026-03-30T02:16:00', 'Europe/Berlin'),
              'frankfurt_winter_marked_open': utc('2026-03-09T01:16:00', 'Europe/Berlin')}}
print(json.dumps(result, indent=2))
