from pathlib import Path
from datetime import datetime, timedelta
import ast
import collections
import json
import re
import subprocess

REPO = Path('/workspace/exchange-hours-review-us-20261031')
OUT = Path(__file__).parent
BASE = '02a3c89'

def old(path):
    return subprocess.check_output(['git', 'show', f'{BASE}:{path}'], cwd=REPO, text=True)

def strip_comments(text):
    return re.sub(r'//[^\n]*', '', text)

def rows(text):
    text = strip_comments(text)
    out = {}
    for m in re.finditer(r'pub\(crate\) static (\w+):[^;]*?holidays!\s*\{(.*?)\n\};', text, re.S):
        body = m.group(2).split('rows:', 1)[1]
        body = body[body.index('[') + 1:body.rindex(']')]
        depth = 0
        start = 0
        entries = {}
        for i, c in enumerate(body):
            if c == '(':
                if depth == 0:
                    start = i
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    row = body[start:i+1]
                    d = re.match(r'\(\s*(\d+),\s*(\d+),\s*(\d+),', row)
                    assert d, row
                    date = '-'.join([d[1], d[2].zfill(2), d[3].zfill(2)])
                    entries[date] = re.sub(r'\s+', '', row)
        out[m.group(1)] = entries
    return out

def number(expr):
    node = ast.parse(expr.strip(), mode='eval').body
    def ev(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, int):
            return n.value
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -ev(n.operand)
        if isinstance(n, ast.BinOp) and isinstance(n.op, (ast.Add, ast.Sub, ast.Mult)):
            a, b = ev(n.left), ev(n.right)
            return a+b if isinstance(n.op, ast.Add) else a-b if isinstance(n.op, ast.Sub) else a*b
        raise ValueError(ast.dump(n))
    return ev(node)

def arrays(text):
    out = {}
    for m in re.finditer(r'static (\w+): \[ExceptionBlock; \d+\] = \[(.*?)\n\];', text, re.S):
        out[m.group(1)] = [[kind, number(off), number(start), number(end)]
                           for kind, off, start, end in re.findall(
            r'ExceptionBlock::(\w+)\(([^,]+),\s*([^,]+),\s*([^\)]+)\)', m.group(2))]
    return out

def cme():
    path = 'src/calendar/schedules/holidays/globex_cryptocurrency.rs'
    src = (REPO/path).read_text()
    prior, actual = rows(old(path))['TABLE'], rows(src)['TABLE']
    assert len(prior) == 98 and len(actual) == 101
    assert all(actual.get(d) == row for d, row in prior.items()), 'upstream holiday row changed'
    old_cov = re.search(r'coverage:\s*(\[[^;]+?\]),\s*rows:', old(path), re.S)[1]
    new_cov = re.search(r'coverage:\s*(\[[^;]+?\]),\s*rows:', src, re.S)[1]
    assert re.sub(r'\s+', '', old_cov) == re.sub(r'\s+', '', new_cov)
    parsed = arrays(src)
    derived = []
    for fname in ['cme_service_oct3.json', 'cme_service_oct24.json', 'cme_service_oct31.json']:
        data = json.loads((OUT/fname).read_text())
        product = data['products'][0]
        assert product['id'] == 8478 and product['prodGroup'] == 'BF'
        events = []
        for day in product['tradingHours']['schedules']:
            assert day['groupCode'] == 'BF'
            for event in day['events']:
                events.append((datetime.fromisoformat(day['eventDate']+'T'+event['eventTime']),
                               event['tradingDate'], event['marketEventType']))
        events.sort()
        monday = events[1][1]
        anchor = datetime.fromisoformat(monday)
        selected = [e for e in events if e[1] == monday]
        assert selected[0][2] == 'preopen' and selected[-1][2] == 'closed'
        blocks = []
        for left, right in zip(selected, selected[1:]):
            t, td, state = left
            end = right[0]
            if state == 'closed':
                continue
            kind = {'open': 'extended', 'preopen': 'order_entry'}[state]
            while t < end:
                midnight = datetime.combine(t.date()+timedelta(days=1), datetime.min.time())
                stop = min(end, midnight)
                off = (t.date()-anchor.date()).days
                start_ssm = t.hour*3600+t.minute*60+t.second
                end_ssm = 86400 if stop == midnight else stop.hour*3600+stop.minute*60+stop.second
                blocks.append([kind, off, start_ssm, end_ssm])
                t = stop
        assert len(blocks) == 7
        row = actual[monday]
        const = re.search(r'ReplacementBlocks\(&([^\)]+)\)', row)[1]
        assert parsed[const] == blocks, (fname, parsed[const], blocks)
        expected_doc = 'CME-SVC-'+events[0][0].date().isoformat()
        assert expected_doc in row and ',T2,' in row
        derived.append({'source': fname, 'trade_date': monday, 'document': expected_doc,
                        'blocks': blocks, 'matches_rust': True})
    normal = 'src/calendar/schedules/futures/us/cryptocurrency.rs'
    def revs(text):
        body = re.search(r'static REVISIONS:[^=]+= revisions!\[(.*?)\n\];', strip_comments(text), re.S)[1]
        return re.findall(r'\(\s*(\d+),\s*(\d+),\s*(\d+),\s*&([^,]+),\s*"([^"]+)"', body)
    prev, now = revs(old(normal)), revs((REPO/normal).read_text())
    assert len(prev) == 15 and len(now) == 9
    assert now == prev[:9], 'non-October revision changed'
    return {'rows_before': len(prior), 'rows_after': len(actual), 'all_upstream_rows_preserved': True,
            'coverage_unchanged': True, 'revisions_before': len(prev), 'revisions_after': len(now),
            'all_prior_nine_revisions_preserved': True, 'derivations': derived}

def ice():
    path = 'src/calendar/schedules/holidays/ice_us.rs'
    src = (REPO/path).read_text()
    prior, actual = rows(old(path)), rows(src)
    parsed = arrays(src)
    # Independent source transcription from the second-retrieved Christmas notice,
    # and current ICE master hours table (September2026). PCPO source states30min.
    matching_close = {'SUGAR': 13*3600, 'COFFEE': 13*3600+30*60,
                      'COCOA': 13*3600+30*60, 'ORANGE_JUICE': 14*3600,
                      'COTTON': 14*3600+20*60}
    derived = []
    for family, close in matching_close.items():
        christmas_close = close if family == 'SUGAR' else 13*3600+5*60
        queue_start = christmas_close+30*60
        blocks = [['order_entry', -4, queue_start, 15*3600+30*60],
                  ['regular', 0, 8*3600, close]]
        row = actual[family]['2026-12-28']
        const = re.search(r'ReplacementBlocks\(&([^\)]+)\)', row)[1]
        assert parsed[const] == blocks, (family, parsed[const], blocks)
        assert 'IFUS-NOTICE-2026-CHRISTMAS' in row and ',T1,' in row
        derived.append({'family': family, 'trade_date': '2026-12-28', 'blocks': blocks,
                        'matches_rust': True})
    cotton_next = [['order_entry', -1, (14*60+50)*60, 18*3600],
                   ['order_entry', -1, (19*60+30)*60, 21*3600],
                   ['regular', -1, 21*3600, (14*60+20)*60]]
    assert parsed['COTTON_AFTER_CHRISTMAS_REOPEN_BLOCKS'] == cotton_next
    assert 'COTTON_AFTER_CHRISTMAS_REOPEN_BLOCKS' in actual['COTTON']['2026-12-29']
    assert ',Unsourced,T1,' in actual['VENUE']['2026-12-29']
    old_unsourced = {d:row for d,row in prior['ORANGE_JUICE'].items() if ',Unsourced,' in row}
    new_unsourced = {d:row for d,row in actual['ORANGE_JUICE'].items() if ',Unsourced,' in row}
    assert len(old_unsourced) == 8 and new_unsourced == old_unsourced
    changes = {}
    for table in actual:
        changes[table] = {d: {'before': prior[table].get(d), 'after': row}
                          for d,row in actual[table].items() if prior[table].get(d) != row}
        assert set(prior[table]) <= set(actual[table]), ('removed row', table)
    assert sum(len(actual[k])-len(prior[k]) for k in actual) == 3
    assert len(actual['VENUE']) == 51
    return {'tables_before': {k:len(v) for k,v in prior.items()},
            'tables_after': {k:len(v) for k,v in actual.items()},
            'fcoj_eight_withheld_dates_preserved': list(new_unsourced),
            'derivations': derived, 'cotton_tuesday_blocks': cotton_next,
            'changed_rows': changes}

if __name__ == '__main__':
    result = {'head': subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),
              'base': BASE, 'cme': cme(), 'ice': ice()}
    (OUT/'INDEPENDENT-DERIVATION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'head': result['head'], 'cme_rows': result['cme']['rows_after'],
                      'cme_blocks': sum(len(x['blocks']) for x in result['cme']['derivations']),
                      'ice_counts': result['ice']['tables_after'], 'result': 'all comparisons match'},indent=2))
