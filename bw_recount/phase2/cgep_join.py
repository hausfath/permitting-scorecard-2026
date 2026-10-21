"""Join CGEP real-project replays (Columbia CGEP, 'Project timeline savings under BAAJA', Oct 21 2026, used with permission;
decoded page copy; per-project months saved republished with the author's permission) to our 2010-24 universe on ceq_title.
Usage: python3.13 -I phase2/cgep_join.py <real_project_replays.csv>
Writes phase2/cgep_join.csv (minimal: ceq_id, cgep project, technology, months_saved_total, months_saved_low)."""
import sys, re, difflib, pandas as pd
n = lambda s: re.sub(r'[^a-z0-9]', '', str(s).lower())
c = pd.read_csv(sys.argv[1])
u1 = pd.read_csv('universe.csv')[['ceq_id', 'title', 'subsector', 'group']]
u2 = pd.read_csv('phase2/universe_new.csv')[['ceq_id', 'title', 'subsector', 'group']]
U = pd.concat([u1, u2], ignore_index=True); U['k'] = U.title.map(n)
d18 = pd.read_csv('ceq_2018_eis.csv')[['ceq_id', 'title']]; d18['k'] = d18.title.map(n)
d24 = pd.read_csv('phase2/ceq_2024_eis.csv')[['id24', 'title']]; d24['k'] = d24.title.map(n)
rec = pd.read_csv('phase2/reconcile_2018_to_2024.csv')[['ceq_id', 'match_id24']]
id24_to_18 = dict(zip(rec.match_id24, rec.ceq_id))
uk = dict(zip(U.k, U.ceq_id)); uset = set(U.ceq_id)
rows = []
for r in c.itertuples():
    k = n(r.ceq_title); cid = uk.get(k); how = 'exact'
    if cid is None and isinstance(r.ceq_title, str):
        # title as in 2024 workbook -> map to 2018 id if reconciled
        m = d24[d24.k == k]
        if len(m):
            i24 = m.id24.iloc[0]; cid = id24_to_18.get(i24, i24); how = 'via_2024_wb'
    if cid is None and isinstance(r.ceq_title, str):
        best = max(((difflib.SequenceMatcher(None, k, x).ratio(), i) for x, i in uk.items()), default=(0, None))
        if best[0] >= 0.8: cid, how = best[1], f'fuzzy{best[0]:.2f}'
    rows.append(dict(ceq_id=cid if cid in uset else '', cgep_project=r.project, technology=r.technology, months_saved_total=r.months_saved_total,
                     months_saved_low=r.months_saved_low, cgep_status=r.status, match=how if cid in uset else ('not_in_universe:' + str(cid) if cid else 'unmatched')))
J = pd.DataFrame(rows)
J['attribution'] = 'Columbia CGEP, Project timeline savings under BAAJA (Oct 21, 2026; https://www.energypolicy.columbia.edu/how-the-senate-permitting-reform-bill-could-impact-energy-project-timelines/; used with permission), real-project replays'
J[J.ceq_id.astype(bool)][['ceq_id', 'cgep_project', 'technology', 'months_saved_total', 'months_saved_low', 'attribution']].to_csv('phase2/cgep_join.csv', index=False)
print(J.match.str.split(':').str[0].str.replace(r'fuzzy.*', 'fuzzy', regex=True).value_counts().to_dict())
print(J[~J.ceq_id.astype(bool)][['cgep_project', 'technology', 'match']].to_string())
