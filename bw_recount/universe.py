"""Primary set (PLAN revision 2026-10-21): all title-based CEQ energy EISs (both sheets), hand-reviewed.
Writes universe.csv: one row per EIS with reviewed subsector, analysis group, B&W-style subsector, duplicate flags."""
import pandas as pd
from candidates import C, GROUP
d = pd.read_csv('ceq_2018_eis.csv').set_index('ceq_id')
rows = {i: dict(ceq_id=i, bw_subsector=p, subsector=p, note='') for i,(p,a) in C.items() if p != 'NONE'}
def setsub(i, s, note):
    rows.setdefault(i, dict(ceq_id=i, bw_subsector='NONE', subsector=s, note=''))
    rows[i]['subsector'] = s; rows[i]['note'] = note
# --- hand review (each change documented)
setsub('R0515','Liquefaction','LNG export terminal + Pacific Connector feed pipeline; sized as LNG (pipeline embedded). B&W likely Pipeline.')
setsub('R0255','Liquefaction','Downeast LNG: in every B&W Liquefaction fingerprint match (PLAN revision).')
setsub('R0334','CoalPlant','Four Corners Power Plant + Navajo Mine continuation (lease renewal); not in B&W set by title review.')
setsub('R0402','GasPlant','Groton Generation Station: removal of operating limits at existing gas plant.')
setsub('R0771','Mine-Gas','Point Thomson gas-condensate field development (B&W fingerprint puts it in Other-Energy).')
setsub('R0267','Wind','ECO Substation / Tule Wind / ESJ gen-tie: generation (Tule Wind) dominates.')
setsub('R0476','Other-Energy','Fort Bliss energy/water/waste initiatives (B&W Other-Energy by fingerprint).')
setsub('R0910','Other-Energy','Schofield Generating Station (multi-fuel/biofuel-capable Army plant).')
setsub('N0062','Solar','Maricopa Sun Solar Complex HCP.')
setsub('R0681','Transmission','New England Clean Power Link (HVDC, Quebec hydro import). MISSED by candidates.py title pass (latent bug, found 2026-10-21).')
setsub('R0628','Leasing-Fossil','Moab Master Leasing Plan (BLM O&G leasing plan). MISSED by candidates.py title pass (latent bug).')
setsub('R0262','Wind','Eagle take permits for Chokecherry-Sierra Madre; duplicate of R0174.')
# programmatic split
LEASE = 'R0628 R0210 R0407 R0408 R0409 R0410 R0411 R0412 R0413 R0414 R0415 R0416 R0738 R0739 R0824 R0316 R0730 R0751 R1061 R1139 R0787 R0835 R0667 R0790'.split()
FOSPROG_OTHER = 'R0804 N0039 N0028 R0095 R0867 R0668'.split()   # G&G, incidental take, regulations: fossil-related, no production decision
CLEANPROG = 'R0827 R0240 R0861 R1122 R1071 N0076'.split()
for i in LEASE: setsub(i,'Leasing-Fossil','Fossil leasing / lease-sale / leasing-availability EIS (PLAN revision: fossil).')
for i in FOSPROG_OTHER: setsub(i,'Programmatic-FossilOther','Fossil-related programmatic with no leasing/production decision (G&G, incidental take, regulations).')
for i in CLEANPROG: setsub(i,'Programmatic-Clean','Clean programmatic (PLAN revision: clean).')
for i in 'R1013 N0075 R0796 R0797 R0828'.split(): setsub(i,'Programmatic-Other','Mixed/bio/uranium programmatic: Other.')
DUP = {'R0262':'R0174','R0110':'R0631','R0286':'R0287','R1040':'R1041','R0889':'R0890','R0305':'R0304','R0575':'R0576'}
GRP = {**GROUP, 'Leasing-Fossil':'Fossil','Programmatic-Clean':'Clean','Programmatic-FossilOther':'Other','Programmatic-Other':'Other'}
u = pd.DataFrame(rows.values())
u['group'] = u.subsector.map(GRP)
u['programmatic'] = u.subsector.str.startswith(('Leasing','Programmatic'))
u['duplicate_of'] = u.ceq_id.map(DUP).fillna('')
for c in ['title','agency','state','noi','feis','rod','sheet']: u[c] = u.ceq_id.map(d[c])
u = u.sort_values(['group','subsector','ceq_id'])
u.to_csv('universe.csv', index=False)
print(len(u)); print(u.groupby(['group','subsector']).size().to_string())
print(u.group.value_counts().to_dict())
