GHG = "https://www.boem.gov/ocs-oil-and-natural-gas (BOEM OCS Report 2016-065, Wolvovsky & Anderson Nov 2016; read via web.archive.org/web/20170629101116/https://www.boem.gov/ocs-oil-and-natural-gas/)"
PFP17 = "https://www.boem.gov/2017-2022-OCS-Oil-and-Gas-Leasing-PFP (read via web.archive.org/web/20191105223009/)"
FPEIS17 = "https://www.boem.gov/fpeis-volume1 (2017-2022 Final PEIS Vol 1, Nov 2016; read via web.archive.org/web/20170629100805/)"
B12 = "http://www.boem.gov/uploadedFiles/BOEM/Oil_and_Gas_Energy_Program/Leasing/Five_Year_Program/2012-2017_Five_Year_Program/"
PFP12 = B12 + "PFP%2012-17.pdf (2012-2017 Proposed Final Program, June 2012; via web.archive.org/web/20120915141004/)"
PEIS12_2 = B12 + "02_Alternatives.pdf (2012-2017 Final PEIS Ch.2, July 2012; via web.archive.org/web/20120916011349/)"
PEIS12_4 = B12 + "04_Environmental_Consequences.pdf (2012-2017 Final PEIS Ch.4; via web.archive.org/web/20120916011142/)"

N738 = "Outer Continental Shelf Oil and Gas Leasing Program: 2017-2022"
N824 = "OCS Oil and Gas Leasing Program 2012-2017 (Final PEIS)"
STATUS_NOTE = ("STATUS CONVENTION (all A1 rows): status_2026=operating means the leasing decision was implemented "
               "(sale held and leases issued; says nothing about whether leases are producing); cancelled = sale cancelled "
               "or held with zero bids; status_year = sale year. ")

rows = [
 # ---------------- R0738 2017-2022 Program ----------------
 dict(ceq_id="R0738", project_name=N738, metric="oil_production_total", unit="MMbbl",
      value_low=2189, value_central=3740, value_high=5928, new_or_existing="programmatic",
      status_2026="operating", status_year=2017, status_source_url="https://www.boem.gov/OCS-Lease-Sale-Statistics-GOM-Oil-and-Gas-Lease-Offerings/ (via web.archive.org)",
      source_url=GHG + "; also " + PFP17 + " Table 5-2",
      source_quote="Table 6-2 ... Proposed Final Program: Low Oil $40 2,189 MMbbl; Mid $100 3,740 MMbbl; High $160 5,928 MMbbl",
      confidence="high",
      notes=STATUS_NOTE + "Central=mid-price ($100/bbl, $5.34/mcf) for the Proposed Final Program / Preferred Alternative = 10 GOM sales + 1 Cook Inlet sale (Arctic excluded by ROD). "
            "PFP Table 5-2 per-area: GOM 2,105/3,531/5,593; Cook Inlet 84/209/335 MMbbl (2016-065 shows GOM low 2,106: rounding). Anticipated production over the 40-70 yr program life. "
            "Program rows are SUPERSETS of the sale-EIS rows (R0408, R0210, R0739 etc.); do not sum program and sale rows."),
 dict(ceq_id="R0738b", project_name=N738, metric="gas_production_total", unit="Bcf",
      value_low=5507, value_central=12104, value_high=22271, new_or_existing="programmatic",
      status_2026="operating", status_year=2017, status_source_url="https://www.boem.gov/OCS-Lease-Sale-Statistics-GOM-Oil-and-Gas-Lease-Offerings/ (via web.archive.org)",
      source_url=GHG + "; also " + PFP17 + " Table 5-2",
      source_quote="Table 6-2 ... Proposed Final Program Natural Gas: Low $2.14 5,507 bcf; Mid $5.34 12,104 bcf; High $8.54 22,271 bcf",
      confidence="high",
      notes="= 5.5 / 12.1 / 22.3 Tcf. GOM 5,470/12,011/22,122 + Cook Inlet 37/93/149 Bcf (PFP Table 5-2)."),
 dict(ceq_id="R0738c", project_name=N738 + " (Proposed Program incl. Beaufort+Chukchi, NOT adopted)", metric="oil_production_total", unit="MMbbl",
      value_low=2189, value_central=8680, value_high=13831, new_or_existing="programmatic",
      status_2026="withdrawn", status_year=2016, status_source_url="",
      source_url=PFP17 + " Table 5-2",
      source_quote="Table 5-2: Anticipated Production by Program Area ... TOTAL 2,189 8,680 13,831 [oil MMbbl]; 5,507 17,250 30,503 [gas Bcf]; BOE 3,169 11,749 19,259",
      confidence="high",
      notes="Includes Beaufort (2,295/3,673 MMbbl mid/high) and Chukchi (2,644/4,231) sales that the PFP/ROD dropped; Arctic low case = exploration only. Gas 5,507/17,250/30,503 Bcf. For reference only; use R0738/R0738b for the adopted program."),
 dict(ceq_id="R0738d", project_name=N738, metric="production_years", unit="years",
      value_low=40, value_central="", value_high=70, new_or_existing="programmatic",
      status_2026="operating", status_year=2017, status_source_url="",
      source_url=FPEIS17 + " Sec 3.2 (Tables 3.2-4, 3.2-5), Sec 3.7",
      source_quote="the E&D scenarios for the cumulative OCS activities ... for approximately 40 to 70 years after each initial regional sale; [Table 3.2-5 GOM] Years of activity < 50",
      confidence="high",
      notes="GOM: <50 years of activity, peak production ~20 years after first sale in 2017 (FPEIS p.3-43). Cook Inlet: <35 years of activity; production ~2030-2050. 2016-065: 'over the 40 to 70 year life of the 2017-2022 Program'. Lifecycle GHG peaks in 2030s-2040s (FPEIS p.4-8)."),
 dict(ceq_id="R0738e", project_name=N738, metric="oil_gas_production_peak_GOM", unit="MMBOE/yr",
      value_low="", value_central=345, value_high="", new_or_existing="programmatic",
      status_2026="operating", status_year=2017, status_source_url="",
      source_url=FPEIS17 + " Figures 3.2-6a (p.3-19) and 3.2-6b (p.3-20)",
      source_quote="Figures 3.2-6a/b Timing and Magnitude of ... Production in the Western / Central/Eastern Planning Area (Mid-Price Scenario, Year 0 = 2017) [curves only, no tabulated values]",
      confidence="medium",
      notes="VISUAL READ of plotted curves (+/-~10%): CPA/EPA mid-price peak ~300 MMBOE/yr at year ~19-20 (~2036-37); WPA peak ~45 MMBOE/yr at year ~15-20. Sum ~345 MMBOE/yr (~0.95 MMBOE/d). "
            "Integral check: ~(300+45)x30/2 = ~5,200 MMBOE vs PFP Table 5-2 mid GOM 5,668 MMBOE: consistent. Mid-price only; low/high not plotted. Split oil/gas by mid GOM ratio (3,531 MMbbl oil of 5,668 MMBOE = 62%) => ~215 MMbbl/yr oil (~0.59 MMbbl/d) at peak (derived)."),
 dict(ceq_id="R0738f", project_name=N738, metric="ghg_lifecycle_gross", unit="MtCO2e total",
      value_low=1285.4, value_central=2380.4, value_high=3958.3, new_or_existing="programmatic",
      status_2026="operating", status_year=2017, status_source_url="https://www.boem.gov/OCS-Lease-Sale-Statistics-GOM-Oil-and-Gas-Lease-Offerings/ (via web.archive.org)",
      source_url=GHG + " Table 8-1 (p.24)",
      source_quote="Table 8-1 ... in Thousands of Metric Tons of CO2e ... Total Proposed Final Program / Preferred Alternative 1,285,400 [low] 2,380,390 [mid] 3,958,300 [high]",
      confidence="high",
      notes="Full lifecycle (upstream OCS ops + midstream + end-use combustion), GWP per EPA 2015 (CH4=25). Over full 40-70 yr life. Proposed Program incl. Arctic: 1,285,540 / 4,834,450 / 7,886,680 kt. "
            "Sanity: 3,740 MMbbl x ~0.43 t/bbl + 12.1 Tcf x ~55 Mt/Tcf = ~2.3 Gt, matches mid."),
 dict(ceq_id="R0738g", project_name=N738, metric="ghg_net_vs_noaction", unit="MtCO2e total",
      value_low=-13.33, value_central=-13.92, value_high=-2.51, new_or_existing="programmatic",
      status_2026="operating", status_year=2017, status_source_url="https://www.boem.gov/OCS-Lease-Sale-Statistics-GOM-Oil-and-Gas-Lease-Offerings/ (via web.archive.org)",
      source_url=GHG + " Table 8-1 (p.24), Table 6-3 (MarketSim substitution)",
      source_quote="Cook Inlet 39,480/40,620; 97,620/150,570; 156,820/240,930. Gulf of Mexico 1,245,920/1,258,110; 2,282,770/2,243,740; 3,801,480/3,719,880 [Program/No Action, kt, low/mid/high]",
      confidence="medium",
      notes="DERIVED by me: (GOM+Cook Inlet Program) minus (GOM+Cook Inlet No Action) from BOEM area rows; sign = Program minus No Action, negative = Program LOWER than no-leasing. BOEM did not run a separate PFP No Action ('*' in Table 8-1: 'gross emissions estimates should be similar'). "
            "GOM alone is +12.2/+39.0/+81.6 Mt; Cook Inlet -1.1/-53.0/-84.1 Mt. BOEM-stated Proposed Program (with Arctic) net: -13.19/-122.98/-133.87 Mt (1,285,540-1,298,730; 4,834,450-4,957,430; 7,886,680-8,020,550). "
            "Net ~0 because MarketSim assumes ~61-63% of forgone OCS output replaced by imports (more GHG-intensive), ~26-28% onshore, only 7% reduced demand (Table 6-3). Net is ~0.5% of gross: highly assumption-driven."),
 dict(ceq_id="R0738h", project_name=N738, metric="ghg_lifecycle_annual_selected_years", unit="MtCO2e/yr",
      value_low=23.91, value_central="", value_high=56.87, new_or_existing="programmatic",
      status_2026="operating", status_year=2017, status_source_url="https://www.boem.gov/OCS-Lease-Sale-Statistics-GOM-Oil-and-Gas-Lease-Offerings/ (via web.archive.org)",
      source_url=GHG + " Table 8-3 (p.27) and FPEIS Figure 4.2-1 (p.4-9)",
      source_quote="Table 8-3 ... Proposed Final Program ... 2025: 23,910 [low] 56,870 [high]; 2050: 13,820 [low] 45,160 [high] (thousand t CO2e)",
      confidence="medium",
      notes="Values are BOEM's 2025 annual lifecycle emissions (low/high). 2050: 13.8/45.2 Mt/yr. PEAK not tabulated: FPEIS Fig 4.2-1 (visual read) low-price peak ~70 MtCO2e/yr ~2035-2038 (essentially all GOM); high-price GOM-only peak roughly 200-250 MtCO2e/yr mid-2030s (stacked plot incl. Arctic peaks ~350 Mt/yr; GOM share read is rough, low confidence). Mid-price annual not given."),

 # ---------------- R0824 2012-2017 Program ----------------
 dict(ceq_id="R0824", project_name=N824, metric="oil_production_total", unit="MMbbl",
      value_low=3600, value_central=5980, value_high=8130, new_or_existing="programmatic",
      status_2026="operating", status_year=2012, status_source_url="",
      source_url=PFP12 + " Table 11 (p.121); identical in " + PEIS12_2 + " Table 2.12.4-1",
      source_quote="Table 11: Production Estimates at Different Prices ... Oil (billion barrels) Low Mid High: Central GOM 2.24 3.77 4.34; Western GOM 0.56 0.86 0.97 [other areas in notes]",
      confidence="high",
      notes="Table 11 oil (BBO) low/mid/high: CGOM 2.24/3.77/4.34; WGOM 0.56/0.86/0.97; EGOM 0.00/0.05/0.07; Chukchi 0.50/1.00/2.15; Beaufort 0.20/0.20/0.40; Cook Inlet 0.10/0.10/0.20. Program total = MY SUM of BOEM area rows (BOEM gives no total row); 15 sales in 6 areas as approved. PEIS Sec 2.8 No Action: 'As much as 8.2 Bbbl of oil and 35 Tcf of natural gas would not be available' (matches high). Prices: low $60/$4.27, mid $110/$7.38, high $160/$11.39. "
            "AS IMPLEMENTED: Arctic sales (Beaufort 242, Chukchi 237) were cancelled (DOI, Oct 2015; date from memory, verify) and both EPA sales (225, 226) received no bids, so realized-program scope = GOM WPA+CPA 10 sales + Cook Inlet 244 (see R0824e). Superset of sale-EIS rows (R0413 etc.)."),
 dict(ceq_id="R0824b", project_name=N824, metric="gas_production_total", unit="Tcf",
      value_low=12.10, value_central=23.63, value_high=34.70, new_or_existing="programmatic",
      status_2026="operating", status_year=2012, status_source_url="",
      source_url=PFP12 + " Table 11 (p.121)",
      source_quote="Natural Gas (trillion cubic feet) Low Mid High: Central GOM 9.47 16.41 19.07; Western GOM 2.63 4.07 4.59; Chukchi 0.00 2.50 8.00 [others in notes]",
      confidence="high",
      notes="Table 11 gas (Tcf): CGOM 9.47/16.41/19.07; WGOM 2.63/4.07/4.59; EGOM 0.00/0.11/0.16; Chukchi 0.00/2.50/8.00; Beaufort 0.00/0.50/2.20; Cook Inlet 0.00/0.04/0.68. Sum of BOEM area rows (derived). PEIS GOM-only Table 4.4.1-1: 'Potentially available oil (Bbbl) 2.7-5.4; natural gas (tcf) 12-24' for 12 GOM sales."),
 dict(ceq_id="R0824c", project_name=N824, metric="production_years", unit="years",
      value_low=40, value_central="", value_high=50, new_or_existing="programmatic",
      status_2026="operating", status_year=2012, status_source_url="",
      source_url=PEIS12_4 + " Sec 4.4.1 (p.4-155) and intro",
      source_quote="Peak production associated with lease sales held under the new Program is expected to occur about 20 years after the Program's approval ... over the entire 40- to 50-year window of the Program",
      confidence="high",
      notes="GOM Table 4.4.1-1 'Years of activity 40-50'; 'Peak production is expected to occur after 2030.' No annual production profile found: oil_production_peak NOT FOUND. Annualize over ~40-50 yr with peak ~2032."),
 dict(ceq_id="R0824d", project_name=N824, metric="ghg_operations_upstream", unit="MtCO2e total",
      value_low=74.18, value_central="", value_high=147.89, new_or_existing="programmatic",
      status_2026="operating", status_year=2012, status_source_url="",
      source_url=PEIS12_4 + " Table 4.4.4-2 (p.4-200)",
      source_quote="TABLE 4.4.4-2 Projected Greenhouse Gas Emissions ... 2012-2017 Program (Tg CO2e) ... All GHGs 74.18-147.89 ... Emissions in the table represent 40-year totals",
      confidence="high",
      notes="UPSTREAM OCS OPERATIONS ONLY (no end-use combustion); CH4 GWP=21. The 2012 PEIS did not estimate lifecycle/downstream GHG or a net-vs-No-Action GHG figure. GOM share 71.18-120.5 Tg."),
 dict(ceq_id="R0824e", project_name=N824 + " (as implemented: GOM WPA/CPA 10 sales + Cook Inlet)", metric="ghg_lifecycle_gross", unit="MtCO2e total",
      value_low=2013.1, value_central="", value_high=3905.1, new_or_existing="programmatic",
      status_2026="operating", status_year=2012, status_source_url="",
      source_url=GHG + " Table 8-7 (p.32)",
      source_quote="Table 8-7 ... Current 2012-2017 Program ... Total: Original 2,013,120 [low] / 3,905,110 [high]; Adjusted 1,028,540 [low] / 2,016,240 [high] (thousand t CO2e)",
      confidence="high",
      notes="Retrospective lifecycle estimate made in Nov 2016, not in the 2012 PEIS. value_low/high = 'Original' case (pairs with R0824f production 2,896/5,510 MMbbl). 'Adjusted' case (GOM activity and production cut 50% 'to account for lower oil and gas prices and commensurately reduced leasing levels') = 1,028.5 / 2,016.2 MtCO2e. "
            "Scope excludes Arctic (no sales held) and EPA (no bids). No mid case and no No-Action comparison: ghg_net_vs_noaction NOT FOUND for R0824."),
 dict(ceq_id="R0824f", project_name=N824 + " (as implemented)", metric="oil_production_total", unit="MMbbl",
      value_low=2896, value_central="", value_high=5510, new_or_existing="programmatic",
      status_2026="operating", status_year=2012, status_source_url="",
      source_url=GHG + " Table 6-4 (p.19)",
      source_quote="Table 6-4 Production Estimates for the 2012-2017 Program ... Oil Low $60 2,796 MMbbl [GOM WPA/CPA, 10 sales] 100 MMbbl [Cook Inlet] 2,896 MMbbl; High $160 5,310 / 200 / 5,510 MMbbl",
      confidence="high",
      notes="Gas: low 12,105 Bcf, high 24,339 Bcf. 'Adjusted' cases halve GOM activity/production (=> ~1,498 / 2,855 MMbbl, derived). Section 6.2: 'The two lease sales held in the GOM Eastern Planning Area are not considered because no bids were received on the lease sales.'"),
]
