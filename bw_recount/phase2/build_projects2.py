"""Merge phase2/universe_new.csv + phase2/sizes_spec2.py (+ source rows from sizing CSVs) into phase2/projects_sized2.csv.
Usage (from bw_recount/): python3.13 -I phase2/build_projects2.py <sizing_dir_with_P2F/P2C_csvs> <phase1_sizing_out_dir>"""
import sys, os, pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(ROOT, 'phase2'))
from sizes_spec2 import S
u = pd.read_csv(os.path.join(ROOT, 'phase2', 'universe_new.csv'))
agent = {}
for dd in sys.argv[1:]:
    for f in os.listdir(dd):
        if f.endswith('.csv'): agent[f.split('_')[0]] = pd.read_csv(os.path.join(dd, f), dtype=str)
def lookup(ref):
    if ref.startswith('URL:'): return dict(source_url=ref[4:], source_quote='', agent_conf='')
    a, rid, metric = ref.split(':'); df = agent[a]
    r = df[(df.ceq_id == rid) & (df.metric == metric)]
    if r.empty: r = df[df.ceq_id.str[:5] == rid[:5]]
    if r.empty: raise KeyError(ref)
    r = r.iloc[0]; url = r.get('source_url', '')
    if not isinstance(url, str) or not url.startswith('http'):
        urls = [x for x in df[df.ceq_id.str[:5] == rid[:5]].source_url if isinstance(x, str) and x.startswith('http')]
        url = urls[0] if urls else ''
    return dict(source_url=url, source_quote=str(r.get('source_quote', ''))[:240], agent_conf=r.get('confidence', ''))
rows, missing = [], []
for _, x in u.iterrows():
    i = x.ceq_id
    if i not in S: missing.append(i); continue
    s = S[i]; src = lookup(s['ref']); p = s.get('p', {})
    rows.append(dict(ceq_id=i, title=x.title, agency=x.agency, state=x.state, subsector=x.subsector, group=x.group, bw_subsector='(post-2018)',
        programmatic=x.programmatic, duplicate_of=p.get('dup', ''), dup_pooled=p.get('dup_pooled', x.dup_pooled if isinstance(x.dup_pooled, str) else ''),
        method=s['m'], size_central=s['v'], size_low=s.get('lo', ''), size_high=s.get('hi', ''), size_unit=s.get('u', ''), built_size=s.get('b', 0),
        status_2026=s.get('st', ''), new_or_existing=s.get('ne', ''), size_confidence=s.get('conf') or src['agent_conf'] or 'low', size_imputed=bool(s.get('imp', False)),
        params=';'.join(f'{k}={v}' for k, v in p.items() if k not in ('dup_pooled',)), source_url=src['source_url'], source_quote=src['source_quote'], note=s.get('note', ''),
        feis=x.feis, feis_year=x.feis_year, era=x.era))
d = pd.DataFrame(rows); d.to_csv(os.path.join(ROOT, 'phase2', 'projects_sized2.csv'), index=False)
print('rows', len(d), 'missing', len(missing), missing)
