import csv, glob, importlib.util, os, sys
S = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(S, '..', 'out', 'A1_boem_leasing.csv')
COLS = ["ceq_id","project_name","metric","unit","value_low","value_central","value_high","new_or_existing","status_2026","status_year","status_source_url","source_url","source_quote","confidence","notes"]
rows = []
for f in sorted(glob.glob(os.path.join(S, 'rows_*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    rows += m.rows
for r in rows:
    extra = set(r) - set(COLS)
    assert not extra, (r['ceq_id'], extra)
    assert len(r.get('source_quote','')) <= 200, (r['ceq_id'], len(r['source_quote']))
with open(OUT, 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, quoting=csv.QUOTE_NONNUMERIC)
    w.writeheader()
    for r in rows:
        w.writerow({c: r.get(c, "") for c in COLS})
print(len(rows), 'rows ->', OUT)
