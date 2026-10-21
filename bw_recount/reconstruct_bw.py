"""Reconstruct Bennon & Wilson (2023) 171 energy EISs from the CEQ 2018 workbook.
ILP: assign each candidate to one subsector (or NONE) so that every subsector count equals Table 1 exactly and the
summed NOI->ROD duration matches Table 1's mean x count within rounding (+/-0.005 yr x n); slack penalized heavily;
secondary objective = fewest departures from the title-based primary guess.
Then, per assigned project, test whether it is forced (no zero-slack-cost-equal solution without it)."""
import sys, numpy as np, pandas as pd
from scipy.optimize import milp, LinearConstraint, Bounds
from candidates import C, T, GROUP
d = pd.read_csv('ceq_2018_eis.csv').set_index('ceq_id')
SUBS = list(T)
def build(fix_out=None, slack_w=1000.0):
    var = []
    for i,(p,alts) in C.items():
        for s in dict.fromkeys((p,)+alts+('NONE',)):
            var.append((i,s))
    nx = len(var); ns = len(SUBS)
    nv = nx + 2*ns
    c = np.zeros(nv)
    for k,(i,s) in enumerate(var): c[k] = 0.0 if s == C[i][0] else 1.0
    c[nx:] = slack_w
    A=[]; lo=[]; hi=[]
    for i in C:
        row=np.zeros(nv); row[[k for k,(j,s) in enumerate(var) if j==i]]=1; A.append(row); lo.append(1); hi.append(1)
    for si,s in enumerate(SUBS):
        n,m = T[s]
        row=np.zeros(nv); idx=[k for k,(j,t) in enumerate(var) if t==s]; row[idx]=1; A.append(row); lo.append(n); hi.append(n)
        row=np.zeros(nv)
        for k in idx: row[k]=d.loc[var[k][0],'dur']
        row[nx+2*si]=1; row[nx+2*si+1]=-1
        A.append(row); lo.append((m-0.005)*n); hi.append((m+0.005)*n)
    ub=np.ones(nv); ub[nx:]=np.inf
    if fix_out:
        for k,v in enumerate(var):
            if v==fix_out: ub[k]=0
    integ=np.r_[np.ones(nx),np.zeros(2*ns)]
    r=milp(c,constraints=LinearConstraint(np.array(A),lo,hi),integrality=integ,bounds=Bounds(np.zeros(nv),ub),options={'time_limit':60})
    return r,var,nx
r,var,nx = build()
x = r.x
assign = {i:s for k,(i,s) in enumerate(var) if x[k]>0.5}
slack = {s:x[nx+2*si]-x[nx+2*si+1] for si,s in enumerate(SUBS)}
print('status',r.status,'obj',round(r.fun,3))
rows=[]
for s in SUBS:
    mem=[i for i,t in assign.items() if t==s]
    md=d.loc[mem,'dur'].mean() if mem else np.nan
    print(f'{s:20s} n={len(mem):3d}/{T[s][0]:3d} mean={md:.3f} target={T[s][1]:.2f} slack={slack[s]:+.3f}yr-sum')
    for i in mem: rows.append(dict(ceq_id=i,subsector=s,group=GROUP[s],primary_guess=C[i][0],dur=round(d.loc[i,'dur'],3),
                                    agency=d.loc[i,'agency'],state=d.loc[i,'state'],title=d.loc[i,'title']))
out=pd.DataFrame(rows)
changed=[(i,C[i][0],s) for i,s in assign.items() if s!=C[i][0]]
print('changes from primary:',len(changed)); [print('  ',c,d.loc[c[0],'title'][:70]) for c in changed]
if len(sys.argv)>1 and sys.argv[1]=='--forced':
    base=r.fun; forced=[]
    for i,s in assign.items():
        if s=='NONE': continue
        r2,_,_=build(fix_out=(i,s))
        forced.append(r2.fun-base)
    out['cost_if_removed']=[round(f,2) for f in forced]
out.to_csv('bw_reconstructed_171.csv',index=False)
