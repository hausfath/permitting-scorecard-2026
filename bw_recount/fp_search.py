"""Duration-fingerprint subset search: which candidate sets reproduce B&W Table 1 mean permit duration?"""
import itertools, pandas as pd, sys
d = pd.read_csv('ceq_2018_eis.csv').set_index('ceq_id')
def search(name, n, mean, pool, show=20):
    lo, hi = (mean-0.005)*n, (mean+0.005)*n
    sols = [c for c in itertools.combinations(pool, n) if lo <= d.loc[list(c),'dur'].sum() <= hi]
    print(f'== {name} n={n} mean={mean}: {len(sols)} solutions from pool {len(pool)}')
    for c in sols[:show]:
        print('   ', [(i, round(d.loc[i,'dur'],2), d.loc[i,'title'][:40]) for i in c])
    return sols
nuc = ['R0263','R0288','R0553','R0701','R0956','R1053','R1107','R1110','R1145','N0016','N0021','N0022','R0352','R0353','R0354','R0355','R0356','R0357','R0358','R0359','R0360','R0361','R0362','R0363','R0364','R0365','R0366','R0367','R0368','N0072']
search('Nuclear',2,6.27,nuc)
search('GasPlant',2,1.67,['R0233','R0526','R0402','R0910','R0731','R0342','R1016'])
search('CoalPlant',2,2.00,['R0342','R1016','R0526','R0334','R0731','R0402'])
search('CarbonCapture',2,2.09,['R0539','R1111','R0342','R1016','R0526'])
search('Regasification',1,3.39,['R0009','R0772','R0773','R0255'])
search('Liquefaction',7,3.73,['R0141','R0216','R0255','R0340','R0380','R0515','R0540','R0593','R0773','R0772','R0009'])
search('BioPlant',2,3.70,['R0101','N0007','R0910','R0008','R0796','R0797','N0075','R0476'])
search('BioRefinery',1,1.71,['R0008','N0075','R0101'])
search('Geothermal',3,2.04,['R0149','R0897','R0371','R1122'])
search('PumpStorage',1,5.51,['R0260'])
search('Mine-Coal',4,6.99,['R0125','R0272','R1154','R0334','R0304','R0305','R0892','R1000','R0704','R0990','R0187','N0043','R0128','R0922'])
gas=['R0206','R0393','R0643','R1060','R1128','R0835','R0127','R0958','R0920','R0771','R0316','R0730','R0751','R1061','R1139','R0787','R0667','R0095','N0028']
search('Mine-Gas',6,6.95,gas)
search('Other-Energy',2,2.70,['R0476','R0910','R0451','R0402','R0731','R0771','R0601','N0076','R0383','R1013','R0876'],show=40)
