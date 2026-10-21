"""Merge universe.csv + sizes_spec.py (+ source rows from the sizing subagent CSVs) into projects_sized.csv.
Usage: python3.13 -I build_projects.py <sizing_out_dir>
(-I because the agent CSVs are untrusted downloads-derived data; this script only parses them as CSV.)"""
import sys, os, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sizes_spec import S
OUT = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
u = pd.read_csv(os.path.join(here, 'universe.csv'))
agent = {}
for f in os.listdir(OUT):
    if f.endswith('.csv'):
        agent[f.split('_')[0]] = pd.read_csv(os.path.join(OUT, f), dtype=str)
def lookup(ref):
    if ref.startswith('URL:'):
        return dict(source_url=ref[4:], source_quote='', agent_conf='')
    a, rid, metric = ref.split(':')
    df = agent[a]
    r = df[(df.ceq_id == rid) & (df.metric == metric)]
    if r.empty:
        r = df[df.ceq_id == rid]
    if r.empty:
        raise KeyError(ref)
    r = r.iloc[0]
    url = r.get('source_url', '')
    if not isinstance(url, str) or not url.startswith('http'):
        same = df[df.ceq_id.str[:5] == rid[:5]]
        urls = [x for x in same.source_url if isinstance(x, str) and x.startswith('http')]
        url = urls[0] if urls else 'https://ceq.doe.gov/docs/nepa-practice/CEQ_EIS_Timelines.xlsx (size inferred from EIS title)'
    return dict(source_url=url, source_quote=str(r.get('source_quote', ''))[:240], agent_conf=r.get('confidence', ''))
rows = []
missing = []
for _, x in u.iterrows():
    i = x.ceq_id
    if i not in S:
        missing.append(i); continue
    s = S[i]
    src = lookup(s['ref'])
    conf = s.get('conf') or src['agent_conf'] or 'low'
    p = s.get('p', {})
    rows.append(dict(ceq_id=i, title=x.title, agency=x.agency, state=x.state, subsector=x.subsector, group=x.group, bw_subsector=x.bw_subsector,
        programmatic=x.programmatic, duplicate_of=p.get('dup', x.duplicate_of if isinstance(x.duplicate_of, str) else ''),
        method=s['m'], size_central=s['v'], size_low=s.get('lo', ''), size_high=s.get('hi', ''), size_unit=s.get('u', ''), built_size=s.get('b', 0),
        status_2026=s.get('st', ''), new_or_existing=s.get('ne', ''), size_confidence=conf, size_imputed=bool(s.get('imp', False)),
        params=';'.join(f'{k}={v}' for k, v in p.items()), source_url=src['source_url'], source_quote=src['source_quote'], note=s.get('note', '')))
d = pd.DataFrame(rows)
d.to_csv(os.path.join(here, 'projects_sized.csv'), index=False)
print('rows', len(d), 'missing spec for', len(missing), missing)
print(d.groupby(['group', 'method']).size().to_string())
