"""Per-subsector fingerprint enumeration: number of subsets of the title-based candidate pool with B&W's count whose
mean NOI->ROD duration rounds to Table 1's value, and each candidate's inclusion share across those subsets.
Exact DP over (count, integer-day sum)."""
import pandas as pd, numpy as np
from collections import defaultdict
from candidates import C, T
d = pd.read_csv('ceq_2018_eis.csv').set_index('ceq_id')
days = (d['dur']*365).round().astype(int)
def count_subsets(items, n, lo, hi):
    H = int(np.floor(hi)); f = np.zeros((n+1, H+1)); f[0,0] = 1.0
    for i in items:
        w = int(days[i])
        if w > H: continue
        f[1:, w:] += f[:-1, :H+1-w].copy()
    return f[n, int(np.ceil(lo)):H+1].sum()
def analyse(s, pool, label=''):
    n, m = T[s]; lo, hi = (m-0.005)*n*365, (m+0.005)*n*365
    def total(items):
        return count_subsets(items, n, lo, hi)
    tot = total(pool)
    inc = {i: (tot - total([j for j in pool if j!=i]))/tot if tot else np.nan for i in pool} if tot and len(pool)<=60 else {}
    return dict(subsector=s, pool=label or 'title-based', pool_n=len(pool), need=n, matching_subsets=tot), inc
rows=[]; incl=[]
for s in T:
    pool = [i for i,(p,a) in C.items() if p==s or s in a]
    r, inc = analyse(s, pool); rows.append(r)
    for i,v in inc.items(): incl.append(dict(subsector=s, pool=r['pool'], ceq_id=i, inclusion_share=round(v,3), dur=round(d.loc[i,'dur'],2), title=d.loc[i,'title'][:90]))
    pool2 = [i for i,(p,a) in C.items() if p==s]   # primary-only pool
    if set(pool2)!=set(pool) and pool2:
        r2, inc2 = analyse(s, pool2, 'primary-only'); rows.append(r2)
        for i,v in inc2.items(): incl.append(dict(subsector=s, pool='primary-only', ceq_id=i, inclusion_share=round(v,3), dur=round(d.loc[i,'dur'],2), title=d.loc[i,'title'][:90]))
out = pd.DataFrame(rows); print(out.to_string(index=False))
pd.DataFrame(incl).to_csv('fingerprint_inclusion.csv', index=False)
out.to_csv('fingerprint_summary.csv', index=False)

# ---- explicit, physically plausible pools for the subsectors that matter most for weighting
EXPL = {
 'Wind': 'R0023 R0174 R0633 R0725 R0912 R1121 R0235 R0336 R0422 R0499 R0390 R0480 R0949 R1138 R0262 R0267 R0712 R1071',
 'Transmission': ' '.join(i for i,(p,a) in C.items() if p=='Transmission') + ' R0423 R0601 R0402 R0480 R1121',
 'Hydro': 'R0079 R0115 R0604 R0660 R1001 R1002 R1032 R1119 N0049 N0051 N0063 N0067 N0069 N0078 R0569 R0533 R0179 R0626 R0497 R0442 R0588 R0072 R0230',
}
rows2=[]; incl2=[]
for s,ids in EXPL.items():
    pool=ids.split(); r,inc=analyse(s,pool,'explicit'); rows2.append(r)
    for i,v in inc.items(): incl2.append(dict(subsector=s,pool='explicit',ceq_id=i,inclusion_share=round(v,3),dur=round(d.loc[i,'dur'],2),title=d.loc[i,'title'][:90]))
print(pd.DataFrame(rows2).to_string(index=False))
pd.concat([pd.read_csv('fingerprint_inclusion.csv'),pd.DataFrame(incl2)]).to_csv('fingerprint_inclusion.csv',index=False)
pd.concat([out,pd.DataFrame(rows2)]).to_csv('fingerprint_summary.csv',index=False)
