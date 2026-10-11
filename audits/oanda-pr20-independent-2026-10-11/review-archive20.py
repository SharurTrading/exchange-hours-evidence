from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import gzip, hashlib, json, subprocess, sys

class OperatorHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.cells = []
        self.cell = None
        self.skip = 0

    def handle_starttag(self, tag, attributes):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag in ('td', 'th'):
            self.cell = []

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
        if tag in ('td', 'th') and self.cell is not None:
            self.cells.append(' '.join(' '.join(self.cell).split()))
            self.cell = None

    def handle_data(self, data):
        if not self.skip:
            self.text.append(data)
            if self.cell is not None:
                self.cell.append(data)

root = Path(sys.argv[1]) / 'normal-weeks/oanda-uk-wayback-audit-2026-10-11'
head = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip()
manifest = json.loads((root / 'manifest.json').read_text())
counts = Counter()
compressed = []
for item in manifest['captures']:
    raw = (root / item['path']).read_bytes()
    assert len(raw) == item['bytes']
    assert hashlib.sha256(raw).hexdigest() == item['sha256']
    if raw[:2] == b'\x1f\x8b':
        decoded = gzip.decompress(raw)
        assert item['raw_response_encoding'] == 'gzip'
        assert (root / item['decoded_path']).read_bytes() == decoded
        assert hashlib.sha256(decoded).hexdigest() == item['decoded_sha256']
        compressed.append(item['path'])
    else:
        decoded = raw
        assert item['raw_response_encoding'] == 'utf-8-html'
    parser = OperatorHTML()
    parser.feed(decoded.decode('utf-8'))
    text = ' '.join(' '.join(parser.text).split()).lower()
    kind = item['path'].split('/')[0]
    if kind == 'hours-captures':
        usable = 'Australia 200' in parser.cells and len(parser.cells) > 40
    else:
        usable = 'holiday trading hours' in text and 'eastern time' in text and 'closed' in text
    assert usable == item['usable_operator_schedule'], item['path']
    counts[(kind, usable)] += 1
hash_rows = (root / 'SHA256SUMS.txt').read_text().splitlines()
for row in hash_rows:
    digest, name = row.split('  ', 1)
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
hours_index = json.loads((root / 'uk-hours-cdx-result').read_text())[1:]
holiday_index = json.loads((root / 'uk-holidays-before2025-cdx-result').read_text())[1:] + json.loads((root / 'uk-holidays-2025-2026-cdx-result').read_text())[1:]
saved_hours = {Path(item['path']).stem for item in manifest['captures'] if item['path'].startswith('hours-captures/')}
missing = [item[0] for item in hours_index if item[0] not in saved_hours]
result = {'head': head, 'source_counts': {str(key): value for key, value in counts.items()},
          'raw_responses': len(manifest['captures']), 'sidecar_hashes': len(hash_rows),
          'exact_gzip_derivatives': compressed, 'hours_index_rows': len(hours_index),
          'holiday_index_rows': len(holiday_index), 'missing_hours_responses': missing}
print(json.dumps(result, indent=2))
