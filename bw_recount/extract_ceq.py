"""Extract the CEQ Dec-2018 EIS Timelines workbook (FEIS with ROD: 1,161; No ROD: 108) to one small CSV.
Source: https://ceq.doe.gov/docs/nepa-practice/CEQ_EIS_Timelines.xlsx (via Wayback id_ snapshot 2021-12-01)."""
import sys, pandas as pd
src, out = sys.argv[1], sys.argv[2]
a = pd.read_excel(src, sheet_name='FEIS with ROD')
a.columns = ['title','agency','dept','state','noi','deis','feis','rod','y_noi_deis','y_deis_feis','y_feis_rod','y_noi_rod']
a['sheet'] = 'ROD'; a['ceq_id'] = ['R%04d' % i for i in range(1, len(a)+1)]
b = pd.read_excel(src, sheet_name='No ROD')
b.columns = ['title','agency','dept','state','noi','deis','feis','rod','y_noi_deis','y_deis_feis','y_noi_feis']
b['sheet'] = 'NoROD'; b['ceq_id'] = ['N%04d' % i for i in range(1, len(b)+1)]
d = pd.concat([a, b], ignore_index=True)
d['title'] = d['title'].astype(str).str.replace(r'\s+', ' ', regex=True).str.strip()
# duration B&W appear to use: NOI->ROD when ROD exists, else NOI->FEIS (right-censored)
d['dur'] = d['y_noi_rod'].where(d.sheet == 'ROD', d.get('y_noi_feis'))
cols = ['ceq_id','sheet','title','agency','dept','state','noi','deis','feis','rod','y_noi_rod','y_noi_feis','dur']
d[cols].to_csv(out, index=False)
print(d.sheet.value_counts().to_dict())
