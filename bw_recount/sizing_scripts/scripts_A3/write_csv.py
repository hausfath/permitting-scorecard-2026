import csv,glob,runpy,os
d=os.path.dirname(os.path.abspath(__file__))
cols="ceq_id,project_name,metric,unit,value_low,value_central,value_high,new_or_existing,status_2026,status_year,status_source_url,source_url,source_quote,confidence,notes".split(",")
rows=[]
for f in sorted(glob.glob(os.path.join(d,"rows*.py"))):
    rows+=runpy.run_path(f)["rows"]
out="/private/tmp/claude-501/-Users-hausfath-Desktop-Climate-Science-The-Climate-Brink/42175875-4e02-4e65-ab8f-a48a292e262b/scratchpad/sizing/out/A3_coal_plants.csv"
with open(out,"w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=cols,quoting=csv.QUOTE_NONNUMERIC)
    w.writeheader()
    for r in rows:
        assert set(r)==set(cols),(r.get("ceq_id"),set(cols)^set(r))
        w.writerow(r)
print(len(rows),"rows")
