import csv
OUT = "/private/tmp/claude-501/-Users-hausfath-Desktop-Climate-Science-The-Climate-Brink/42175875-4e02-4e65-ab8f-a48a292e262b/scratchpad/sizing/out/A2_onshore_oilgas.csv"
COLS = ["ceq_id", "project_name", "metric", "unit", "value_low", "value_central", "value_high",
        "new_or_existing", "status_2026", "status_year", "status_source_url", "source_url",
        "source_quote", "confidence", "notes"]
rows = []

def R(ceq, name, metric, unit, low, cen, high, noe, st, sty, sturl, src, quote, conf, notes):
    rows.append(dict(zip(COLS, [ceq, name, metric, unit, low, cen, high, noe, st, sty, sturl, src, quote, conf, notes])))

exec(open(__file__.replace("build_A2.py", "rows_A2.py")).read())

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLS, quoting=csv.QUOTE_NONNUMERIC)
    w.writeheader()
    for r in rows:
        w.writerow(r)
print(len(rows), "rows;", len({r['ceq_id'][:5] for r in rows}), "ceq_ids")
