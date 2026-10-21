"""Extract EIA Natural Gas Pipeline Projects (Aug 2026) rows matching universe pipelines -> eia_pipeline_matches.csv
Usage: python3.13 -I eia_pipe_lookup.py XLSX OUTCSV"""
import sys, re, pandas as pd
frames=[]
for s in ['Natural Gas Pipeline Projects','Historical Projects (1996-2024)']:
    df = pd.read_excel(sys.argv[1], sheet_name=s, header=1); df['sheet']=s; frames.append(df)
d = pd.concat(frames, ignore_index=True)
d.columns=[str(c).strip() for c in d.columns]
pats = {'R0017':'Algonquin Incremental','R0050':'Apex','R0063':'Atlantic Coast|Supply Header','R0066':'Atlantic Sunrise',
 'R0202':'Constitution|Wright Interconnect','R0550':'Leach X|Rayne X','R0651':'Mountain Valley|Equitrans Expansion','R0652':'Mountaineer|Gulf X',
 'R0683':'New Jersey.?New York','R0693':'NEXUS|Nexus|Texas Eastern Appalachian|TEAL','R0753':'PennEast','R0880':'Rockaway|Northeast Connector',
 'R0887':'Rover|Panhandle Backhaul|Trunkline Backhaul','R0890':'Ruby','R0931':'Sierrita','R0961':'Sabal|Hillabee|Florida Southeast|Southeast Market',
 'N0004':'Alaska Stand|ASAP','R0515':'Pacific Connector','R0141':'Cameron','R0216':'Corpus','R0340':'Freeport','R0380':'Golden Pass','R0540':'Lake Charles','R0593':'Magnolia'}
out=[]
for k,p in pats.items():
    m = d[d['Project Name'].astype(str).str.contains(p, regex=True, na=False)]
    for _,r in m.iterrows():
        out.append(dict(ceq_id=k, sheet=r['sheet'], project=r['Project Name'], operator=r.get('Pipeline Operator Name'), status=r.get('Status'),
            in_service=r.get('Year In Service Date'), miles=r.get('Miles'), add_cap_mmcfd=r.get('Additional Capacity (MMcf/d)'), project_type=r.get('Project Type'),
            docket=r.get('Docket Number'), demand=r.get('Demand Served')))
o=pd.DataFrame(out); o.to_csv(sys.argv[2], index=False)
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',45)
print(o.drop(columns=['sheet','operator']).to_string())
