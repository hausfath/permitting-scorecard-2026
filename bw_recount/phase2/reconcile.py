"""Reconcile the CEQ 2018 workbook (1,269 EISs; our 237-EIS energy universe) with the CEQ 2010-2024 workbook.
Match: (1) exact normalized title; (2) same FEIS date + agency + title similarity >= 0.6; (3) title similarity >= 0.85.
Writes phase2/reconcile_2018_to_2024.csv (all 2018 rows) and prints universe recovery, re-dating, adds/drops."""
import re, difflib, pandas as pd
n = lambda s: re.sub(r'[^a-z0-9]', '', str(s).lower())
a = pd.read_csv('ceq_2018_eis.csv'); b = pd.read_csv('phase2/ceq_2024_eis.csv')
for df in (a, b):
    df['k'] = df.title.map(n); df['feis_d'] = pd.to_datetime(df.feis, errors='coerce').dt.date
    df['rod_d'] = pd.to_datetime(df.rod, errors='coerce').dt.date; df['noi_d'] = pd.to_datetime(df.noi, errors='coerce').dt.date
u = set(pd.read_csv('universe.csv').ceq_id)
used = set(); match = {}
bk = {}
for i, k in zip(b.id24, b.k): bk.setdefault(k, []).append(i)
B = b.set_index('id24')
for r in a.itertuples():
    c = [i for i in bk.get(r.k, []) if i not in used]
    if len(c) > 1:
        c2 = [i for i in c if B.loc[i, 'feis_d'] == r.feis_d]; c = c2 or c
    if c: match[r.ceq_id] = (c[0], 'exact_title'); used.add(c[0])
for r in a.itertuples():
    if r.ceq_id in match: continue
    cand = b[(b.feis_d == r.feis_d) & (~b.id24.isin(used))]
    best = max(((difflib.SequenceMatcher(None, r.k, x.k).ratio(), x.id24) for x in cand.itertuples()), default=(0, None))
    if best[0] >= 0.6: match[r.ceq_id] = (best[1], f'same_feis_date_sim{best[0]:.2f}'); used.add(best[1])
rest = b[~b.id24.isin(used)]
for r in a.itertuples():
    if r.ceq_id in match: continue
    best = max(((difflib.SequenceMatcher(None, r.k, x.k).ratio(), x.id24) for x in rest.itertuples() if x.id24 not in used), default=(0, None))
    if best[0] >= 0.85: match[r.ceq_id] = (best[1], f'fuzzy_sim{best[0]:.2f}'); used.add(best[1])
MANUAL = {'R0201': 'C0812', 'R1053': 'C1148'}   # hand-checked: same EIS, retitled/re-dated in the 2024 workbook
for k, v in MANUAL.items():
    if k not in match: match[k] = (v, 'manual_title_check'); used.add(v)
rows = []
for r in a.itertuples():
    m = match.get(r.ceq_id)
    x = B.loc[m[0]] if m else None
    rows.append(dict(ceq_id=r.ceq_id, in_universe=r.ceq_id in u, title=r.title[:120], match_id24=m[0] if m else '', match_type=m[1] if m else 'UNMATCHED',
        feis_2018=r.feis_d, feis_2024=x.feis_d if m else '', rod_2018=r.rod_d, rod_2024=x.rod_d if m else '', noi_2018=r.noi_d, noi_2024=x.noi_d if m else '',
        title_2024=x.title[:120] if m else ''))
R = pd.DataFrame(rows)
R['redated'] = (R.match_id24 != '') & ((R.feis_2018.astype(str) != R.feis_2024.astype(str)) | (R.rod_2018.astype(str) != R.rod_2024.astype(str)) | (R.noi_2018.astype(str) != R.noi_2024.astype(str)))
R.to_csv('phase2/reconcile_2018_to_2024.csv', index=False)
U = R[R.in_universe]
print('2018 rows', len(R), 'matched', (R.match_id24 != '').sum(), R.match_type.str.split('_sim').str[0].value_counts().to_dict())
print('universe', len(U), 'recovered', (U.match_id24 != '').sum())
print('UNIVERSE UNMATCHED:'); print(U[U.match_id24 == ''][['ceq_id', 'title', 'feis_2018']].to_string())
print('UNIVERSE fuzzy matches:'); print(U[U.match_type.str.startswith(('same', 'fuzzy'))][['ceq_id', 'match_type', 'title', 'title_2024']].to_string())
print('UNIVERSE re-dated:', U.redated.sum()); print(U[U.redated][['ceq_id', 'title', 'feis_2018', 'feis_2024', 'rod_2018', 'rod_2024', 'noi_2018', 'noi_2024']].to_string())
b['matched_2018'] = b.id24.isin(used)
b[['id24', 'matched_2018']].to_csv('phase2/ceq2024_matched_flag.csv', index=False)
x = b[~b.matched_2018]
print('2024 rows unmatched to 2018 wb:', len(x), 'of which FEIS<=2017:', (pd.to_datetime(x.feis) < '2018-01-01').sum())
