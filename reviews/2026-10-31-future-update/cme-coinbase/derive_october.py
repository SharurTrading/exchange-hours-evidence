"""Derive complete Monday replacement blocks from captured CME event streams."""
from datetime import date, datetime, time, timedelta
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
CASES = [
    ('cme_service_oct3.json', '2026-10-05', 'SATURDAY_TO_0500_BLOCKS'),
    ('cme_service_oct24.json', '2026-10-26', 'SATURDAY_TO_1530_BLOCKS'),
    ('cme_service_oct31.json', '2026-11-02', 'SATURDAY_TO_0500_BLOCKS'),
]
results = []
for file, monday, table in CASES:
    payload = json.loads((ROOT / file).read_text())
    product, = payload['products']
    assert product['id'] == 8478 and product['prodGroup'] == 'BF'
    events = []
    for schedule in product['tradingHours']['schedules']:
        for event in schedule['events']:
            if event['tradingDate'] == monday:
                at = datetime.fromisoformat(schedule['eventDate'] + 'T' + event['eventTime'])
                events.append((at, event['marketEventType']))
    events.sort()
    assert [kind for _, kind in events] == ['preopen', 'open', 'closed', 'preopen', 'open', 'closed']
    assert events[0][0].date() == date.fromisoformat(monday) - timedelta(days=3)
    assert events[-1][0] == datetime.fromisoformat(monday + 'T16:00')
    blocks = []
    for (opening, kind), (close, _) in zip(events, events[1:]):
        if kind == 'closed':
            continue
        phase = {'preopen': 'order_entry', 'open': 'extended'}[kind]
        while opening < close:
            midnight = datetime.combine(opening.date() + timedelta(days=1), time())
            stop = min(close, midnight)
            offset = (opening.date() - date.fromisoformat(monday)).days
            start_seconds = (opening - datetime.combine(opening.date(), time())).seconds
            end_seconds = 86400 if stop == midnight else (stop - datetime.combine(stop.date(), time())).seconds
            blocks.append([phase, offset, start_seconds, end_seconds])
            opening = stop
    results.append({'trade_date': monday, 'source': file, 'rust_table': table, 'blocks': blocks})
(ROOT / 'derived_october_rows.json').write_text(json.dumps(results, indent=2) + '\n')
crate = Path('/workspace/exchange-hours-rs/src/calendar/schedules/holidays/globex_cryptocurrency.rs').read_text()
for row in results:
    body = re.search(r'static ' + row['rust_table'] + r': \[ExceptionBlock; 7\] = \[(.*?)\n\];', crate, re.S).group(1)
    actual = []
    for phase, offset, opening, close in re.findall(r'ExceptionBlock::(\w+)\((-?\d+), ([\d_ *+]+), ([\d_ *+]+)\)', body):
        actual.append([phase, int(offset), eval(opening, {'__builtins__': {}}), eval(close, {'__builtins__': {}})])
    assert actual == row['blocks'], (row, actual)
print(json.dumps({'rows': len(results), 'blocks_per_row': [len(row['blocks']) for row in results], 'matches': True}))
