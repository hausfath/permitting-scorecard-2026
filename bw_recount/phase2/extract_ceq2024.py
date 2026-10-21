"""Extract CEQ EIS Timelines 2010-2024 workbook (Jan 13 2025; 'All FEISs') to phase2/ceq_2024_eis.csv.
Source: https://nepa.gov/sites/default/files/documents/CEQ_EIS_Timeline_Data_2024_1_13_2025.xlsx
Usage: python3.13 -I extract_ceq2024.py XLSX OUTCSV"""
import sys, pandas as pd
d = pd.read_excel(sys.argv[1], sheet_name='All FEISs')
d.columns = ['title','agency','state','noi','deis','feis','rod','y_noi_deis','y_deis_feis','y_noi_feis','y_noi_rod']
d['title'] = d['title'].astype(str).str.replace(r'\s+', ' ', regex=True).str.strip()
d.insert(0, 'id24', ['C%04d' % i for i in range(1, len(d)+1)])
for c in ['noi','deis','feis','rod']:
    d[c+'_dt'] = pd.to_datetime(d[c], errors='coerce')
d.to_csv(sys.argv[2], index=False)
print(d.shape, d.feis_dt.min(), d.feis_dt.max(), 'no ROD:', d.rod_dt.isna().sum())
print(d.rod.astype(str).str[:12].value_counts().head(5))
print(d.feis_dt.dt.year.value_counts().sort_index().to_dict())
