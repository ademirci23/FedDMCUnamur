"""Builds results_summary.md: every complete run found under logs/, with its
final-round metrics. The summary is generated from the raw logs, never edited
by hand. The script sits in Results/ and looks for logs/ one level up, so it
can be run from anywhere:  python results/verify_numbers.py
"""
import re, glob, os
from datetime import datetime
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

FIELDS = {
    'DAR':  r'Server Defense accuracy: ([\d.]+)',
    'Prec': r'malicious Precision: ([\d.]+)',
    'Rec':  r'malicious Recall: ([\d.]+)',
    'ASR':  r'Global ASR: ([\d.]+)',
    'TACC': r'Global Model Test accuracy: ([\d.]+)',
}

# The precision/recall swap in the metrics code was fixed on 2026-06-19.
# Logs written before that carry the two values exchanged, so for those runs
# the values are swapped back here and the run is marked in the last column.
SWAP_FIX = datetime(2026, 6, 19, 3, 0)

# The local optimizer is hardcoded in main.py and never logged (one of the
# deviations the thesis documents). Runs before 2026-06-20 used the repository's
# Adam default. From 2026-06-20 on the code was switched to SGD, except the runs
# below, which were deliberately done under Adam for the comparison.
ADAM_AFTER_SWITCH = {
    '2026-06-20/00.41.08',   # Scaling, faithful variant, Adam side of the comparison
    '2026-06-20/00.42.42',   # Scaling, faithful variant, Adam side of the comparison
    '2026-06-20/01.22.06',   # LIT, faithful variant, Adam side of the comparison
    '2026-07-09/19.51.30',   # no-attack Adam run (the measured Adam ceiling)
    '2026-07-11/16.01.45',   # GS, HDBSCAN variant, Adam: non-IID redo of the early IID run
}

# Display names, in the order the thesis uses (not alphabetical).
ATTACKS = [
    ('no_attack',      'No attack (clean reference)'),
    ('GS_attack',      'Gaussian Noise attack'),
    ('LF_attack',      'Label Flipping attack'),
    ('LIT_attack',     'LIT backdoor attack'),
    ('Scaling_attack', 'Scaling backdoor attack'),
]
DEFENSES = [
    ('average',        'No defense (plain averaging)'),
    ('pca_agglomer_a', 'FedDMC, binary tree (faithful)'),
    ('pca_hdbscan_b',  'FedDMC, HDBSCAN variant'),
    ('multi_krum',     'Multi-Krum'),
    ('auror',          'Auror'),
    ('foolsgold',      'FoolsGold'),
    ('FLDetector',     'FLDetector (not implemented, runs plain averaging)'),
]
ATTACK_NAME = dict(ATTACKS)
DEFENSE_NAME = dict(DEFENSES)
ATTACK_POS = {k: i for i, (k, _) in enumerate(ATTACKS)}
DEFENSE_POS = {k: i for i, (k, _) in enumerate(DEFENSES)}
OPT_POS = {'SGD': 0, 'Adam': 1}
SPLIT_POS = {'non-IID': 0, 'IID': 1}


def run_start(folder):
    # folder looks like 2026-06-20/01.30.27
    date_part, time_part = folder.split('/')
    return datetime.strptime(date_part + ' ' + time_part, '%Y-%m-%d %H.%M.%S')


def fmt(v, pct=False):
    if v is None:
        return '-'
    return f'{v * 100:.2f}' if pct else f'{v:.2f}'


def spread(values, pct=False):
    # a single run shows its value, repeated runs show "low to high"
    values = [v for v in values if v is not None]
    if not values:
        return '-'
    lo, hi = min(values), max(values)
    if fmt(lo, pct) == fmt(hi, pct):
        return fmt(lo, pct)
    return f'{fmt(lo, pct)} to {fmt(hi, pct)}'


def md_table(headers, body):
    # pad every cell so the raw text stays aligned and readable without rendering
    all_rows = [headers] + body
    widths = [max(len(str(r[i])) for r in all_rows) for i in range(len(headers))]

    def line(cells):
        return '| ' + ' | '.join(str(c).ljust(widths[i]) for i, c in enumerate(cells)) + ' |'

    sep = '|' + '|'.join('-' * (w + 2) for w in widths) + '|'
    return [line(headers), sep] + [line(r) for r in body]


rows = defaultdict(list)
n_runs = 0
for readme in sorted(glob.glob(os.path.join(ROOT, 'logs', '*', '*', 'readme.md'))):
    fld = os.path.dirname(readme)
    cfg = open(readme, encoding='utf-8', errors='ignore').read()
    bz = re.search(r"byz_type': '(\w+)'", cfg)
    ag = re.search(r"agg_type': '(\w+)'", cfg)
    ii = re.search(r"'IID':\s*(\w+)", cfg)
    bz = bz.group(1) if bz else '?'
    ag = ag.group(1) if ag else '?'
    split = 'IID' if (ii and ii.group(1) == 'True') else 'non-IID'
    try:
        txt = open(os.path.join(fld, 'info.log'), encoding='utf-8').read()
    except OSError:
        continue
    last_round = re.findall(r'\[Round: (\d+)\]', txt)
    if not last_round or last_round[-1] != '199':
        continue  # incomplete or diagnostic run, not listed

    def last(rx):
        m = re.findall(rx, txt)
        return float(m[-1]) if m else None

    v = {k: last(rx) for k, rx in FIELDS.items()}
    run_id = fld.replace(os.sep, '/').split('logs/')[-1]
    started = run_start(run_id)
    swapped = started < SWAP_FIX
    prec, rec = v['Prec'], v['Rec']
    if swapped:
        prec, rec = rec, prec
    optimizer = 'Adam' if (started < datetime(2026, 6, 20) or run_id in ADAM_AFTER_SWITCH) else 'SGD'
    rows[(bz, ag)].append({
        'run': run_id, 'started': started, 'opt': optimizer, 'split': split,
        'tacc': v['TACC'], 'asr': v['ASR'], 'dar': v['DAR'],
        'prec': prec, 'rec': rec, 'swapped': swapped,
    })
    n_runs += 1


def attack_key(bz):
    return (ATTACK_POS.get(bz, len(ATTACKS)), bz)


def defense_key(ag):
    return (DEFENSE_POS.get(ag, len(DEFENSES)), ag)


attacks_present = sorted({bz for (bz, _) in rows}, key=attack_key)

out = []
out.append('# Results Summary (generated)')
out.append('')
out.append('One line per complete run (a run that reached round 199) found under `logs/`,')
out.append('with its final-round metrics. This file is generated from the raw logs by')
out.append('`verify_numbers.py` and is never edited by hand. To update it after new runs:')
out.append('')
out.append('    python results/verify_numbers.py')
out.append('')
out.append('How to read the columns:')
out.append('')
out.append('- **TACC (%)**: final test accuracy of the global model.')
out.append('- **ASR (%)**: backdoor success rate. Only the two backdoor attacks (LIT and')
out.append('  Scaling) have one.')
out.append('- **DAR**: detection accuracy, the fraction of the 100 clients classified')
out.append('  correctly. A defense that flags nobody scores 0.72 (the 72 honest clients).')
out.append('- **Precision / Recall** of the malicious flagging. Logs written before the')
out.append('  metrics fix of 2026-06-19 stored the two values swapped: those runs are')
out.append('  marked "yes" in the last column and the values shown are already corrected.')
out.append('- **Optimizer**: hardcoded in `main.py` and never logged (a documented')
out.append('  deviation). The column follows the switch timeline: Adam until 2026-06-19,')
out.append('  SGD from 2026-06-20, except the deliberate Adam comparison runs listed in')
out.append('  the script.')
out.append('- **Split**: seven early runs (2026-04-12 and 04-13) were launched with the')
out.append('  IID split by mistake, before the setup was fixed to the non-IID split')
out.append('  (Dirichlet, beta 5) the thesis uses. They stay in the list, marked IID.')
out.append('')
out.append('Runs stopped before round 199 (quick diagnostic runs) are not listed.')
out.append('')
out.append('## At a glance')
out.append('')
out.append('One row per attack, defense, optimizer, and data split. Cells show the single')
out.append('value of a lone run or the low-to-high spread of repeated runs.')
out.append('')

glance = []
for bz in attacks_present:
    first_of_attack = True
    defenses_present = sorted({ag for (b, ag) in rows if b == bz}, key=defense_key)
    for ag in defenses_present:
        group = rows[(bz, ag)]
        first_of_defense = True
        combos = sorted({(r['opt'], r['split']) for r in group},
                        key=lambda c: (OPT_POS.get(c[0], 9), SPLIT_POS.get(c[1], 9)))
        for opt, split in combos:
            sub = [r for r in group if r['opt'] == opt and r['split'] == split]
            glance.append([
                ATTACK_NAME.get(bz, bz) if first_of_attack else '',
                DEFENSE_NAME.get(ag, ag) if first_of_defense else '',
                opt, split,
                len(sub),
                spread([r['tacc'] for r in sub], pct=True),
                spread([r['asr'] for r in sub], pct=True),
                spread([r['dar'] for r in sub]),
            ])
            first_of_attack = False
            first_of_defense = False
out.extend(md_table(
    ['Attack', 'Defense', 'Optimizer', 'Split', 'Runs', 'TACC (%)', 'ASR (%)', 'DAR'], glance))
out.append('')

out.append('## All runs, attack by attack')
out.append('')
for bz in attacks_present:
    out.append(f'### {ATTACK_NAME.get(bz, bz)}')
    out.append('')
    body = []
    defenses_present = sorted({ag for (b, ag) in rows if b == bz}, key=defense_key)
    for ag in defenses_present:
        first = True
        for r in sorted(rows[(bz, ag)], key=lambda r: r['started']):
            body.append([
                DEFENSE_NAME.get(ag, ag) if first else '',
                r['run'], r['opt'], r['split'],
                fmt(r['tacc'], pct=True), fmt(r['asr'], pct=True), fmt(r['dar']),
                fmt(r['prec']), fmt(r['rec']),
                'yes' if r['swapped'] else '-',
            ])
            first = False
    out.extend(md_table(
        ['Defense', 'Run', 'Optimizer', 'Split', 'TACC (%)', 'ASR (%)', 'DAR',
         'Precision', 'Recall', 'Pre-fix log'], body))
    out.append('')

with open(os.path.join(HERE, 'results_summary.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')

print(f'wrote {os.path.join(HERE, "results_summary.md")} ({n_runs} complete runs)')
