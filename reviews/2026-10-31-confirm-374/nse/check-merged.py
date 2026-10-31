"""Confirm the six merged Muhurat blocks against the freshly extracted PDF."""

import ast
import datetime
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
CRATE = pathlib.Path('/workspace/exchange-hours-rs')
pdf = ROOT / 'CMTR76941.pdf'
text = (ROOT / 'CMTR76941.layout.txt').read_text()
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == (
    'ce94ee1c54d98eccdf3c30fa0673ae2b6a49ea4ed4a72fb83d826f4359f71d58'
)
assert 'Sunday, November 08, 2026' in text
assert 'Department: CAPITAL MARKET SEGMENT' in text
assert 'System driven random closure' in text and 'in the last 2 minutes' in text
times = re.findall(r'\b\d{2}:\d{2}\b', text)
# Source-order indexes below were checked against the labelled PDF table.
# This list validates that extraction did not reorder or omit its time cells.
assert times == [
    '14:05', '14:10', '14:10', '14:15', '14:15', '14:17', '14:17',
    '14:20', '14:20', '15:15', '15:15', '15:20', '15:20', '15:25',
    '15:25', '15:30', '15:30', '15:35', '15:35', '15:50', '15:50',
    '16:00', '15:30', '13:50', '14:05', '14:05', '14:50', '15:05',
    '15:30', '14:25', '15:10', '14:20', '16:15',
]

def seconds(value):
    h, m = map(int, value.split(':'))
    return h * 3600 + m * 60

preopen_start = seconds(times[0])
preopen_random_earliest = seconds(times[3]) - 2 * 60
continuous_open = seconds(times[8])
non_cas_close = seconds(times[22])
expected = [
    ['extended', 0, seconds(times[23]), seconds(times[24])],
    ['order_entry', 0, preopen_start, preopen_random_earliest],
    ['extended', 0, preopen_random_earliest, continuous_open],
    ['regular', 0, continuous_open, non_cas_close],
    ['extended', 0, non_cas_close, seconds(times[17])],
    ['extended', 0, seconds(times[20]), seconds(times[21])],
]
module = CRATE / 'src/calendar/schedules/holidays/nse_india.rs'
source = module.read_text()
body = re.search(
    r'static MUHURAT_2026_BLOCKS: \[ExceptionBlock; 6\] = \[(.*?)\n\];',
    source, re.S,
).group(1)

def integer(expression):
    node = ast.parse(expression.strip().replace('_', ''), mode='eval').body
    def walk(n):
        if isinstance(n, ast.Constant) and type(n.value) is int:
            return n.value
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
            return walk(n.left) + walk(n.right)
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult):
            return walk(n.left) * walk(n.right)
        raise ValueError(ast.dump(n))
    return walk(node)

actual = []
for kind, args in re.findall(r'ExceptionBlock::(\w+)\(([^)]+)\)', body):
    actual.append([kind, *map(integer, args.split(','))])
assert actual == expected, (actual, expected)
assert '(2026, 11, 8, ReplacementBlocks(&MUHURAT_2026_BLOCKS), T1, "NSE-CIRC-2026-149")' in source
assert datetime.date(2026, 11, 8).weekday() == 6
result = {
    'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'merged_crate_head': subprocess.check_output(
        ['git', '-C', str(CRATE), 'rev-parse', 'HEAD'], text=True,
    ).strip(),
    'source_pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'merged_module_sha256': hashlib.sha256(module.read_bytes()).hexdigest(),
    'source_times_in_printed_order': times,
    'block_fields': ['kind', 'day_offset', 'open_seconds_IST', 'close_seconds_IST'],
    'derived_blocks': expected,
    'merged_blocks': actual,
    'phase_derivation': {
        'fixed_preopen_order_entry_end': '14:15 minus the printed last-two-minute random closure = 14:13',
        'preopen_envelope': '14:13 through continuous open 14:20; printed matching 14:15-14:17 and buffer 14:17-14:20 retained',
        'regular_union': 'continuous starts 14:20; CAS leaves at 15:15, non-CAS remains continuous to 15:30',
        'cas_tail': 'matching continues from non-CAS close 15:30 to CAS matching end 15:35',
        'closed_transition': '15:35-15:50, then post-close 15:50-16:00',
        'trade_date': '2026-11-08 Sunday, day offsets zero',
    },
    'result': 'PASS: all six merged blocks and Sunday replacement row match',
}
(ROOT / 'merged-check.json').write_text(json.dumps(result, indent=2) + '\n')
print(result['result'])
