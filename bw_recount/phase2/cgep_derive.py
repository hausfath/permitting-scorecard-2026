"""Derive two small tables from the CGEP decoded data (raw kept in scratchpad; licence unknown):
phase2/cgep_type_medians.csv (median months saved by technology, all 144 replays) and
phase2/cgep_archetype_totals.csv (number_ledger wf.<type>.smooth.total / contested.total).
Usage: python3.13 -I phase2/cgep_derive.py <emb_dir>"""
import sys, pandas as pd
c = pd.read_csv(sys.argv[1] + '/real_project_replays.csv')
m = c.groupby('technology').agg(n=('project', 'size'), months_saved_total=('months_saved_total', 'median'), months_saved_low=('months_saved_low', 'median'),
                                mean_total=('months_saved_total', 'mean'))
m['source'] = 'Columbia CGEP, Project timeline savings under BAAJA (Oct 21, 2026; https://www.energypolicy.columbia.edu/how-the-senate-permitting-reform-bill-could-impact-energy-project-timelines/; used with permission), real-project replays'
m.to_csv('phase2/cgep_type_medians.csv'); print(m)
d = pd.read_csv(sys.argv[1] + '/baaja_timelines_all_data.csv', low_memory=False)
n = d[(d.table == 'number_ledger') & d.id.astype(str).str.match(r'^wf\.[a-z]+\.(smooth|contested)\.total$')]
rows = {}
for r in n.itertuples():
    _, t, sc, _ = r.id.split('.')
    rows.setdefault(t, {})[sc + '_total'] = float(r.value)
a = pd.DataFrame(rows).T; a.index.name = 'technology'
a['source'] = 'Columbia CGEP (https://www.energypolicy.columbia.edu/how-the-senate-permitting-reform-bill-could-impact-energy-project-timelines/; used with permission) number_ledger wf.<type>.smooth.total / contested.total (Deadlines met / Delays and challenges, months sooner to in service)'
a.to_csv('phase2/cgep_archetype_totals.csv'); print(a)
