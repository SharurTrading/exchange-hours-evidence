#!/usr/bin/env python3
"""Retrieve every earlier distinct-digest capture of a cited 2013-2015 PDF URL.

Input : ../cme-2013-2015/cdx_holiday_calendar.json (round-0 CDX)
        ../cme-2013-2015/names.txt, ../cme-2013-2015-fix/todo.tsv (already-held)
Output: pdf/<base>__<ts>.pdf  +  cdx_candidates.json  +  retrieval.json
"""
import json, os, subprocess, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.dirname(HERE)
BLOCK = os.path.join(os.path.dirname(RAW), 'cme-2013-2015.json')

def load(path):
    d = json.load(open(path)); hdr = d[0]
    return [dict(zip(hdr, r)) for r in d[1:]]

blk = json.load(open(BLOCK))
cited_pdf = {v['file'] for v in blk['documents'].values()
             if isinstance(v, dict) and v.get('file', '').endswith('.pdf')}
cdx = load(os.path.join(RAW, 'cme-2013-2015', 'cdx_holiday_calendar.json'))
held = set()
for line in open(os.path.join(RAW, 'cme-2013-2015', 'names.txt')):
    line = line.strip()
    if line and '__' in line:
        held.add(tuple(line.rsplit('__', 1)))
for line in open(os.path.join(RAW, 'cme-2013-2015-fix', 'todo.tsv')):
    p = line.rstrip('\n').split('\t')
    if len(p) >= 2:
        held.add((p[1].rsplit('/', 1)[-1], p[0]))
for f in os.listdir(os.path.join(RAW, 'cme-2013-2015-verify-r2', 'new')):
    b, ts = f[:-4].rsplit('__', 1)
    held.add((b, ts))

cands = []
seen = set()
for r in cdx:
    if r['statuscode'] != '200' or not r['original'].lower().endswith('.pdf'):
        continue
    base = r['original'].rsplit('/', 1)[-1]
    if base not in cited_pdf:
        continue
    key = (base, r['timestamp'])
    if key in held or key in seen:
        continue
    seen.add(key)
    cands.append({'base': base, 'timestamp': r['timestamp'],
                  'original_url': r['original'], 'cdx_digest': r['digest'],
                  'cdx_length': r['length']})
cands.sort(key=lambda c: (c['base'], c['timestamp']))
json.dump(cands, open(os.path.join(HERE, 'cdx_candidates.json'), 'w'), indent=1)
print('candidates:', len(cands), flush=True)

os.makedirs(os.path.join(HERE, 'pdf'), exist_ok=True)
man = []
for i, c in enumerate(cands, 1):
    out = os.path.join(HERE, 'pdf', '%s__%s.pdf' % (c['base'], c['timestamp']))
    c['saved'] = os.path.relpath(out, RAW)
    if os.path.exists(out) and os.path.getsize(out) > 0:
        c['note'] = 'already saved'
    else:
        url = 'https://web.archive.org/web/%sid_/%s' % (c['timestamp'], c['original_url'])
        cp = subprocess.run(['curl', '-sS', '--max-time', '120', '-L', '-o', out,
                             '-w', '%{http_code} %{size_download}', url],
                            capture_output=True, text=True)
        c['note'] = 'http ' + (cp.stdout or '').strip()
        if cp.returncode != 0:
            c['note'] += ' curlrc=%d %s' % (cp.returncode, (cp.stderr or '').strip()[:120])
    if os.path.exists(out):
        b = open(out, 'rb').read()
        c['sha256'] = hashlib.sha256(b).hexdigest()
        c['bytes'] = len(b)
    else:
        c['sha256'] = None; c['bytes'] = 0
    print('%3d/%d %-46s %-14s %s %s' % (i, len(cands), c['base'], c['timestamp'],
                                        c.get('bytes'), c['note']), flush=True)
    man.append(c)
json.dump(man, open(os.path.join(HERE, 'retrieval.json'), 'w'), indent=1)
ok = sum(1 for c in man if c.get('bytes'))
print('DONE retrieved %d/%d with bytes' % (ok, len(man)), flush=True)
