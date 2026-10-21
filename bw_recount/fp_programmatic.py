"""Energy-Programmatic composition implied by the duration fingerprint: across all 15-subsets of the candidate pool
whose mean NOI->ROD duration rounds to 3.23 yr, distribution of (# fossil lease-sale/leasing EISs, # clean programmatic)."""
import numpy as np, pandas as pd
from candidates import C, T
d = pd.read_csv('ceq_2018_eis.csv').set_index('ceq_id'); days=(d.dur*365).round().astype(int)
pool=[i for i,(p,a) in C.items() if p=='Energy-Programmatic']
LEASE=set('R0210 R0407 R0408 R0409 R0410 R0411 R0412 R0413 R0414 R0415 R0416 R0738 R0739 R0824 R0316 R0730 R0751 R1061 R1139 R0787 R0835 R0667 R0790'.split())
CLEAN=set('R0827 R0240 R0861 R1122 R1071 N0076'.split())
n,m=T['Energy-Programmatic']; lo,hi=(m-0.005)*n*365,(m+0.005)*n*365; H=int(hi)
f=np.zeros((n+1,n+1,len(CLEAN)+1,H+1)); f[0,0,0,0]=1
for i in pool:
    w=days[i]; a=int(i in LEASE); b=int(i in CLEAN)
    g=f.copy()
    g[1:, a:, b:, w:] += f[:-1, :n+1-a, :len(CLEAN)+1-b, :H+1-w]
    f=g
tab=f[n,:,:,int(np.ceil(lo)):].sum(axis=2)
tot=tab.sum(); print('pool',len(pool),'matching subsets',tot)
pa=tab.sum(axis=1)/tot; pb=tab.sum(axis=0)/tot
print('P(# lease/leasing EISs = k):',{k:round(v,3) for k,v in enumerate(pa) if v>0.001})
print('P(# clean programmatic = k):',{k:round(v,3) for k,v in enumerate(pb) if v>0.001})
print('E[lease]=%.2f E[clean]=%.2f'%((pa*np.arange(len(pa))).sum(),(pb*np.arange(len(pb))).sum()))
print('lease pool',len(LEASE&set(pool)),'clean pool',len(CLEAN&set(pool)),'other pool',len(set(pool)-LEASE-CLEAN))
