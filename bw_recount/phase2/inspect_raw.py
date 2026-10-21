import sys, pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',60)
x = pd.ExcelFile(sys.argv[1]); print(x.sheet_names)
for s in x.sheet_names:
    df = x.parse(s, header=None, nrows=6); print('==', s, x.parse(s, header=None).shape); print(df.to_string()[:2500])
for f in sys.argv[2:]:
    d = pd.read_csv(f); print('==', f.split('/')[-1], d.shape); print(list(d.columns)); print(d.head(3).to_string()[:2500])
