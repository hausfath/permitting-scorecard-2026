"""Validation gate: independent title-based classification of CEQ 2018 energy EISs vs B&W Table 1 counts.
Writes gate_counts.csv and bw_candidates.csv (every candidate, primary guess, ILP 'closest reconstruction' assignment)."""
import pandas as pd
from candidates import C, T, GROUP
d = pd.read_csv('ceq_2018_eis.csv').set_index('ceq_id')
ilp = pd.read_csv('bw_reconstructed_171.csv').set_index('ceq_id')['subsector']
cand = pd.DataFrame([dict(ceq_id=i, sheet=d.loc[i,'sheet'], primary_guess=p, alternates='|'.join(a),
        ilp_assignment=ilp.get(i,'NONE'), dur_noi_rod_or_feis=round(d.loc[i,'dur'],3), agency=d.loc[i,'agency'],
        state=d.loc[i,'state'], title=d.loc[i,'title']) for i,(p,a) in C.items()])
cand.to_csv('bw_candidates.csv', index=False)
rows=[]
for s,(n,m) in T.items():
    allc=(cand.primary_guess==s).sum(); rodc=((cand.primary_guess==s)&(cand.sheet=='ROD')).sum()
    rows.append(dict(group=GROUP[s], subsector=s, BW_count=n, title_based_all=allc, delta_all=allc-n,
                     title_based_ROD_sheet_only=rodc, delta_ROD_only=rodc-n,
                     pass_pm2=(abs(allc-n)<=2) if GROUP[s]!='Other' else 'n/a (other)'))
g=pd.DataFrame(rows)
tot=dict(group='ALL',subsector='TOTAL',BW_count=171,title_based_all=g.title_based_all.sum(),delta_all=g.title_based_all.sum()-171,
         title_based_ROD_sheet_only=g.title_based_ROD_sheet_only.sum(),delta_ROD_only=g.title_based_ROD_sheet_only.sum()-171,
         pass_pm2=abs(g.title_based_all.sum()-171)<=5)
g=pd.concat([g,pd.DataFrame([tot])]); g.to_csv('gate_counts.csv',index=False); print(g.to_string(index=False))
for grp in ['Clean','Fossil','Other']:
    print(grp, 'B&W', g[g.group==grp].BW_count.sum(), 'title-based', g[g.group==grp].title_based_all.sum())
