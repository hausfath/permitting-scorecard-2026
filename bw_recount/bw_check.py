"""B&W check (PLAN revision): B&W Table 1 counts x pool-mean emissions per subsector, plus min/max over
fingerprint-feasible subsets (count = Table 1 count AND mean NOI->ROD duration within rounding of Table 1).
Where no fingerprint-feasible subset exists (Nuclear, Mine-Coal, BioPlant, Hydro), min/max over any subset of the
Table 1 size. Energy-Programmatic (B&W 'Other') is split: fossil leasing members add to fossil, clean programmatic to clean.
Writes results_bw_check.csv. Uses central per-project emissions from projects.csv."""
import os, numpy as np, pandas as pd
from scipy.optimize import milp, LinearConstraint, Bounds
from candidates import C, T, GROUP
HERE = os.path.dirname(os.path.abspath(__file__))
d = pd.read_csv(os.path.join(HERE, 'ceq_2018_eis.csv')).set_index('ceq_id')
pr = pd.read_csv(os.path.join(HERE, 'projects.csv')).set_index('ceq_id')
days = (d['dur'] * 365).round()
def emis(i, k):
    if i in pr.index and pr.loc[i, 'group'] in ('Clean', 'Fossil'):
        sign = 1 if pr.loc[i, 'group'] == GROUP_OF.get(i, pr.loc[i, 'group']) else 1
        return float(pr.loc[i, f'em_{k}_central'])
    return 0.0
GROUP_OF = {}
def opt(pool, n, s, k, sense, use_fp, wvec):
    """min (sense=+1) or max (sense=-1) of sum w_i x_i s.t. sum x = n and (optionally) duration sum in tolerance."""
    m = T[s][1]
    c = sense * np.array(wvec)
    A = [np.ones(len(pool))]; lo = [n]; hi = [n]
    if use_fp:
        A.append(np.array([days[i] for i in pool])); lo.append((m - 0.005) * n * 365); hi.append((m + 0.005) * n * 365)
    r = milp(c, constraints=LinearConstraint(np.array(A), lo, hi), integrality=np.ones(len(pool)), bounds=Bounds(0, 1))
    if r.status != 0: return None, None
    sel = [pool[j] for j in range(len(pool)) if r.x[j] > 0.5]
    return float(np.dot(wvec, r.x)), sel
EXPL = {
 'Wind': 'R0023 R0174 R0633 R0725 R0912 R1121 R0235 R0336 R0422 R0499 R0390 R0480 R0949 R1138 R0262 R0267 R0712 R1071'.split(),
 'Transmission': [i for i,(p,a) in C.items() if p=='Transmission'] + 'R0423 R0601 R0402 R0480 R1121'.split(),
 'Hydro': 'R0079 R0115 R0604 R0660 R1001 R1002 R1032 R1119 N0049 N0051 N0063 N0067 N0069 N0078 R0569 R0533 R0179 R0626 R0497 R0442 R0588 R0072 R0230'.split()}
UMAP = {'Leasing-Fossil':'Energy-Programmatic','Programmatic-Clean':'Energy-Programmatic','Programmatic-FossilOther':'Energy-Programmatic','Programmatic-Other':'Energy-Programmatic'}
pr['bw_like'] = [UMAP.get(x, x) for x in pr.subsector]
rows = []
LEASE_IDS = set(pr.index[pr.subsector == 'Leasing-Fossil']); CLEANPROG = set(pr.index[pr.subsector == 'Programmatic-Clean'])
for k in ['usn', 'gln', 'usg', 'glg']:
    for s, (n, m) in T.items():
        pool = EXPL.get(s) or [i for i, (p, a) in C.items() if p == s or s in a]
        grp = GROUP[s]
        upool = list(pr.index[pr.bw_like == s])
        if s == 'Energy-Programmatic':
            # signed contribution: fossil leasing +, clean programmatic - (net fossil-minus-clean)
            w = [emis(i, k) if i in LEASE_IDS else (-emis(i, k) if i in CLEANPROG else 0.0) for i in pool]
        else:
            w = [emis(i, k) for i in pool]
        fp_ok = opt(pool, n, s, k, 1, True, w)[0] is not None
        mn, smin = opt(pool, n, s, k, 1, fp_ok, w)
        mx, smax = opt(pool, n, s, k, -1, fp_ok, w)
        mx = -mx if mx is not None else None
        mx = abs(mx) if mx is not None else None
        # recompute signed max properly
        if smax is not None:
            mx = float(sum(w[pool.index(i)] for i in smax))
        rows.append(dict(metric=k, subsector=s, group=grp, bw_count=n, pool_n=len(pool), fingerprint_constrained=fp_ok,
                         universe_pool_n=len(upool), count_x_poolmean=n * float(np.mean([ (emis(i,k) if i not in CLEANPROG else -emis(i,k)) if s=='Energy-Programmatic' else emis(i,k) for i in upool])) if upool else 0.0, min_feasible=mn, max_feasible=mx,
                         argmin=' '.join(smin or []), argmax=' '.join(smax or [])))
R = pd.DataFrame(rows)
R.to_csv(os.path.join(HERE, 'results_bw_check.csv'), index=False)
for k in ['usn', 'gln']:
    x = R[R.metric == k]
    cl = x[x.group == 'Clean']; fo = x[x.group == 'Fossil']; ep = x[x.subsector == 'Energy-Programmatic']
    print(f'== {k}: clean count*mean {cl.count_x_poolmean.sum():.1f} [min {cl.min_feasible.sum():.1f}, max {cl.max_feasible.sum():.1f}]; '
          f'fossil {fo.count_x_poolmean.sum():.1f} [min {fo.min_feasible.sum():.1f}, max {fo.max_feasible.sum():.1f}]; '
          f'EP net(fossil-clean) {ep.count_x_poolmean.sum():.1f} [{ep.min_feasible.sum():.1f}, {ep.max_feasible.sum():.1f}]')
    print(x[['subsector', 'bw_count', 'universe_pool_n', 'pool_n', 'fingerprint_constrained', 'count_x_poolmean', 'min_feasible', 'max_feasible']].round(1).to_string(index=False))
