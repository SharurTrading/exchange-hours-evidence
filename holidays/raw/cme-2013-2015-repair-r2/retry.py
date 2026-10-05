#!/usr/bin/env python3
"""Resume fetch.py: retry captures still missing, with backoff."""
import json, os, subprocess, hashlib, time, random

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.dirname(HERE)
cands = json.load(open(os.path.join(HERE, 'retrieval.json')))
os.makedirs(os.path.join(HERE, 'pdf'), exist_ok=True)
todo = [c for c in cands if not c.get('bytes')]
print('remaining:', len(todo), flush=True)
for attempt in range(1, 7):
    still = []
    for i, c in enumerate(todo, 1):
        out = os.path.join(RAW, c['saved'])
        url = 'https://web.archive.org/web/%sid_/%s' % (c['timestamp'], c['original_url'])
        cp = subprocess.run(['curl', '-sS', '--max-time', '180', '--retry', '3',
                             '--retry-delay', '5', '--retry-all-errors', '-L', '-o', out,
                             '-w', '%{http_code}', url], capture_output=True, text=True)
        code = (cp.stdout or '').strip()
        if os.path.exists(out) and os.path.getsize(out) > 0:
            b = open(out, 'rb').read()
            c['sha256'] = hashlib.sha256(b).hexdigest(); c['bytes'] = len(b)
            c['note'] = 'http ' + code + ' (attempt %d)' % attempt
            print('%3d/%d OK  %-46s %-14s %s' % (i, len(todo), c['base'], c['timestamp'], c['bytes']), flush=True)
        else:
            c['note'] = 'http %s (attempt %d)' % (code, attempt)
            still.append(c)
            print('%3d/%d --  %-46s %-14s %s' % (i, len(todo), c['base'], c['timestamp'], c['note']), flush=True)
        time.sleep(2.0 + random.random())
    json.dump(cands, open(os.path.join(HERE, 'retrieval.json'), 'w'), indent=1)
    todo = still
    print('--- after attempt %d: %d still missing' % (attempt, len(todo)), flush=True)
    if not todo:
        break
    time.sleep(30 * attempt)
print('DONE missing=%d' % len(todo), flush=True)
