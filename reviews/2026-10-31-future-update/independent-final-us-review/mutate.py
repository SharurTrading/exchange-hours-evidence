from pathlib import Path
import json
import subprocess

REPO = Path('/workspace/exchange-hours-review-us-20261031')
OUT = Path(__file__).parent
cases = [
    {
        'name': 'cme',
        'file': 'src/calendar/schedules/holidays/globex_cryptocurrency.rs',
        'old': 'ExceptionBlock::order_entry(-2, 15 * 3_600 + 15 * 60, 15 * 3_600 + 30 * 60)',
        'new': 'ExceptionBlock::order_entry(-2, 15 * 3_600 + 16 * 60, 15 * 3_600 + 30 * 60)',
        'test': 'october_maintenance_rows_preserve_the_weekend_and_exact_queues',
        'scope': 'holidays_globex_cryptocurrency::',
    },
    {
        'name': 'ice',
        'file': 'src/calendar/schedules/holidays/ice_us.rs',
        'old': 'ExceptionBlock::order_entry(-4, 13 * 3_600 + 30 * 60, 15 * 3_600 + 30 * 60)',
        'new': 'ExceptionBlock::order_entry(-4, 13 * 3_600 + 30 * 60, 15 * 3_600 + 31 * 60)',
        'test': 'the_2026_christmas_notice_shortens_queues_and_states_the_monday_reopen',
        'scope': 'holidays_ice_us::',
    },
]

def run(name, test):
    result = subprocess.run(['cargo', 'test', '--test', 'futures_family_boundaries', test],
                            cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (OUT/(name+'.log')).write_text(result.stdout)
    print(name, 'exit', result.returncode, flush=True)
    return result.returncode

records = []
for case in cases:
    baseline = run(case['name']+'-baseline', case['scope'])
    assert baseline == 0, 'baseline failed'
    path = REPO/case['file']
    original = path.read_text()
    assert original.count(case['old']) == 1
    try:
        path.write_text(original.replace(case['old'], case['new']))
        mutated = run(case['name']+'-mutated', case['test'])
        assert mutated != 0, 'mutation was not detected'
    finally:
        path.write_text(original)
    restored = run(case['name']+'-restored', case['test'])
    assert restored == 0
    records.append({**case, 'baseline_exit': baseline, 'mutated_exit': mutated,
                    'restored_exit': restored})

(OUT/'MUTATION-RESULTS.json').write_text(json.dumps(records,indent=2)+'\n')
status = subprocess.check_output(['git','status','--short'],cwd=REPO,text=True)
assert not status, status
print('Both mutations detected; worktree clean.', flush=True)
