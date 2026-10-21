# ---------------- R0206 Continental Divide-Creston (WY) ----------------
N = "Continental Divide-Creston Natural Gas Development Project"
CDC_FEIS_ES = "https://eplanning.blm.gov/epl-front-office/projects/nepa/58344/72528/79528/CD-C_FEIS_Executive_Summary.pdf"
CDC_FEIS_CH4 = "https://eplanning.blm.gov/epl-front-office/projects/nepa/58344/71831/78860/CD-C_FEIS_Chapter_4_Environmental_Consequences.pdf"
CDC_PR = "https://www.blm.gov/press-release/blm-issues-decision-continental-divide-creston-natural-gas-development-project"
CDC_ST = "https://pgjonline.com/news/2021/july/williams-announces-upstream-operator-and-joint-venture-in-the-wamsutter-field"
CDC_STATUS = ("operating", "2021", CDC_ST)
R("R0206", N, "wells_approved", "wells", 4063, 8950, 8950, "expansion", *CDC_STATUS, CDC_FEIS_CH4,
  "Under Alternative F, 5,465 pads would be required for the drilling of 8,950 wells.", "high",
  "ROD (Sep 2016) selected Alt F (Agency Preferred): 8,950 infill wells on 5,465 pads; BLM press release says 'nearly 9,000 additional wells'. Low = Alt D (directional drilling, 4,063 wells). Infill of existing Wamsutter/Creston-Blue Gap fields (>4,700 existing wells). FEIS/ROD read via Wayback copy of ePlanning project 58344; ROD main text not retrieved (only attachments archived). STATUS: field operating; Williams/Crowheart JV (2021) reports 'over 3,500 operating wells' and 'more than 3,000 potential development locations' across 1.2 million net acres, implying most of the 8,950 ROD wells NOT drilled; count of wells drilled under ROD NOT FOUND (medium).")
R("R0206b", N, "development_years", "years", "", 15, "", "expansion", *CDC_STATUS, CDC_FEIS_ES,
  "the Operators would collectively drill the new wells at the average rate of approximately 600 wells per year over a period of 15 years.", "high",
  "Project life 30-40 yr (press release); well life 45-55 yr total field life per FEIS ES.")
R("R0206c", N, "gas_production_total", "Tcf", 5.5, 12.0, 12.0, "expansion", *CDC_STATUS, CDC_FEIS_CH4,
  "Estimated total production for the Proposed Action over the life of the field is 12.0 Tcf of gas and 167.3 million bbls of liquid condensates", "high",
  "EUR of new (Proposed Action/Alt F) wells. FEIS says production 'unchanged' at 12.0 Tcf under Alts B, C and F. Low = Alt D (5.5 Tcf). Adding existing wells gives 14.3 Tcf + 198.4 MMbbl. Condensate 167.3 MMbbl over life.")
R("R0206d", N, "gas_production_peak", "Bcf/yr", "", 735, "", "expansion", *CDC_STATUS, CDC_FEIS_CH4,
  "projected annual production peaking at more than 735 Bcf and 10.0 million bbls of liquid condensates", "high",
  "FEIS socioeconomics, Proposed Action (approx 2.0 Bcf/d). Ambiguous whether this includes existing wells (No Action peak from existing wells alone was 270 Bcf/yr in DEIS). DEIS (Nov 2012) said '670 MMcf' which is a typo for Bcf. Peak condensate 10.0 MMbbl/yr = ~27,400 bbl/d (computed).")
R("R0206e", N, "ghg_operations_annual", "tCO2e/yr", "", 5153235, "", "expansion", *CDC_STATUS, CDC_FEIS_CH4,
  "Table 4.5-3. CD-C Project alternative GHG emission summary (metric tpy) ... Total CO2e emissions ... Proposed Action 2022 5,153,235", "high",
  "Metric tonnes, peak year 2022, Proposed Action new sources only (GWP CH4=21 in DEIS). Total project area incl. existing wells 2022 = 8,625,612 t. No downstream combustion estimate found (NOT FOUND).")

# ---------------- R0393 Greater Natural Buttes (UT) ----------------
N = "Greater Natural Buttes Area Gas Development Project"
GNB_FR = "https://www.govinfo.gov/content/pkg/FR-2012-04-06/pdf/2012-8247.pdf"
GNB_CH4 = "http://www.blm.gov/style/medialib/blm/ut/vernal_fo/planning/greater_natural_buttes/gnb_feis_ii.Par.16945.File.dat/d_Chapter_4.pdf"
GNB_ROD = "http://www.blm.gov/style/medialib/blm/ut/vernal_fo/planning/greater_natural_buttes/record_of_decision.Par.86388.File.dat/Cover_ROD.pdf"
GNB_STATUS = ("operating", "2017", "https://www.sec.gov/Archives/edgar/data/773910/000077391016000073/apc201510k-10k.htm")
R("R0393", N, "wells_approved", "wells", "", 3675, "", "expansion", *GNB_STATUS, GNB_FR,
  "Under the Resource Protection Alternative (the Agency Preferred Alternative), up to 3,675 new gas wells would be drilled from 1,484 new well pads over a period of 10 years", "high",
  "ROD (May 2012, signed by Sec. Salazar) approved Resource Protection Alternative. Proposed Action was same 3,675 wells from 3,041 pads. Infill of existing Natural Buttes field (Kerr-McGee/Anadarko, now Occidental). Optimal Recovery Alt (not selected) had more wells. STATUS (Anadarko 10-Ks): drilled 341 wells in 2012 (ROD May 2012), 223 in 2013, 133 in 2014, 60 in 2015, then field run at reduced activity 2016-2017 (~2,850-2,930 operated wells). So roughly <=750 of 3,675 ROD wells drilled 2012-2015 (some 2012 wells pre-ROD); GNB gas sales 168 Bcf (2013), 154 (2014), 126 (2015) vs EIS peak ~274 Bcf/yr; $3.0 bn impairment 2015. Status after 2018 (Occidental) not checked.")
R("R0393b", N, "development_years", "years", "", 10, "", "expansion", *GNB_STATUS, GNB_FR,
  "up to 3,675 new gas wells would be drilled from 1,484 new well pads over a period of 10 years", "high",
  "Projected end of production 2059 (FEIS Table 2 summary).")
R("R0393c", N, "gas_production_peak", "MMcf/d", 278, 751, 1619, "expansion", *GNB_STATUS, GNB_CH4,
  "average daily gas production from within the GNBPA from this alternative is estimated to increase to a peak of approximately 751 MMcfd and 15,530 barrels condensate per day (BCPD)", "high",
  "Proposed Action value; FEIS says Resource Protection Alt has same wells and same recovery (6.07 Tcf). = ~274 Bcf/yr. Low = No Action (278 MMcfd), high = Optimal Recovery Alt (1,619 MMcfd). Field-wide (includes existing wells?) - text says 'average daily gas production from within the GNBPA', so likely includes existing production.")
R("R0393d", N, "oil_production_peak", "bbl/d", "", 15530, "", "expansion", *GNB_STATUS, GNB_CH4,
  "peak of approximately 751 MMcfd and 15,530 barrels condensate per day (BCPD)", "high", "Condensate.")
R("R0393e", N, "gas_production_total", "Tcf", 1.41, 6.07, 15.44, "expansion", *GNB_STATUS, GNB_CH4,
  "Recoverable gas and condensate resource over the life of the wells from implementation of the Proposed Action would be approximately 6,070 Bcf of gas and 86.5 million bbls condensate", "high",
  "Resource Protection (selected) = 6.07 Tcf / 86.5 MMbbl per FEIS summary table. Low = No Action, high = Optimal Recovery. Per-well EUR 0.96-1.28 Bcf gas and 3,000-20,000 bbl condensate (FEIS 4.8).")
R("R0393f", N, "eur_per_well", "Bcf", 0.96, "", 1.28, "expansion", *GNB_STATUS, GNB_CH4,
  "That profile assumes economic recovery ranging from 0.96 Bcf to 1.28 Bcf of gas and 3,000 to 20,000 barrels of oil condensates over the life of a well.", "high", "")
R("R0393g", N, "ghg_operations_annual", "tCO2e/yr", 1761016, 2754167, 5484666, "expansion", *GNB_STATUS, GNB_CH4,
  "Table 4.1-10 Detailed Summary of Annual GHG Emissions by Source for the Proposed Action ... Total (tonne CO2e) 2,231,452 24,102 53.5 506,135 16,580 2,754,167", "high",
  "Metric tonnes/yr, Proposed Action (Resource Protection Alt not separately modeled; same wells). Includes 1,183,596 t indirect (purchased electricity) emissions. Low = No Action, high = Optimal Recovery. No downstream combustion estimate (NOT FOUND).")

# ---------------- R0643 Monument Butte (UT) ----------------
N = "Monument Butte Area Oil and Gas Development Project (Newfield)"
MB_FR = "https://www.govinfo.gov/content/pkg/FR-2016-06-24/html/2016-15023.htm"
MB_FEIS = "https://files.library.northwestern.edu/transportation/online/unrestricted/EIS/2016/20160139/"
MB_PR = "https://www.blm.gov/press-release/Monument-Butte-oil-gas-project-decision-allows-energy-development-to-proceed-while-protecting-sensitive-resources"
MB_STATUS = ("operating", "2017", "https://www.sec.gov/Archives/edgar/data/912750/000091275018000004/nfx201710-k.htm")
R("R0643", N, "wells_approved", "wells", "", 5750, "", "expansion", *MB_STATUS, MB_FR,
  "Under the Resource Protection Alternative, up to 5,750 new wellbores would be drilled.", "high",
  "ROD Sep 30 2016 approved Alt D (Resource Protection). Same 5,750 as Proposed Action: 750 Green River oil wells (40-ac), 2,500 Green River oil infill wells (20-ac downhole), 2,500 deep gas wells. Existing field ~3,209 wells, 119,784 ac. STATUS: Newfield 2017 10-K: Uinta operations = Central Basin + Greater Monument Butte Unit waterflood; only 23 wells placed on production in Central Basin over 2016-2017, ~10% of 2018 capital to Uinta HBP drilling; Uinta net production ~17 MBOE/d (Q4 2017). Field operating but ROD build-out (esp. 2,500 deep gas wells) appears largely NOT executed; count of ROD wells drilled NOT FOUND. Later owner (Encana/Ovintiv after 2019 merger) not verified.")
R("R0643b", N, "development_years", "years", "", 16, "", "expansion", *MB_STATUS, MB_FR,
  "The MBPA contemplates the drilling of up to 5,750 new oil and gas wells over a 16-year period", "high", "")
R("R0643c", N, "oil_production_total", "MMbbl", "", 334.9, "", "expansion", *MB_STATUS, MB_FEIS,
  "Newfield estimates that its plan could yield over 334.9 million barrels of oil (MMBO), 540,669 million cubic feet (MMCF) of natural gas, and 10,085 million barrels (Mbbl) of natural gas liquids", "high",
  "FEIS Ch.1 (Preliminary pages thru Ch 3 pdf). Green River oil EUR; NGL '10,085 Mbbl' is ~10.1 MMbbl (EIS unit typo). No peak bbl/d found in FEIS (NOT FOUND).")
R("R0643d", N, "gas_production_total", "Tcf", "", 7.44, "", "expansion", *MB_STATUS, MB_FEIS,
  "540,669 million cubic feet (MMCF) of natural gas ... from the Green River formation, and 6.9 trillion cubic feet (Tcf) of natural gas from the deep gas development through 2035", "high",
  "Central = 0.54 Tcf Green River associated gas + 6.9 Tcf deep gas (sum computed). Secondary sources (NGI, WEG) quote only the 540 Bcf figure.")
R("R0643e", N, "ghg_operations_annual", "short_tons_CO2e/yr", "", 3038339, 3096936, "expansion", *MB_STATUS, MB_FEIS,
  "TABLE 4.2.1.4.1-1 MAXIMUM YEAR EMISSIONS UNDER ALTERNATIVE D ... GWP ... 3,038,339 ... tpy - tons per year", "high",
  "Maximum emissions year, Alt D (selected); high = Proposed Action 3,096,936. EIS units 'tpy' (not stated as metric; likely short tons -> ~2.76 Mt metric). Reported as 'GWP' (CO2e). No downstream estimate (WEG comments say FEIS did not analyze combustion).")

# ---------------- R1060 Gasco Uinta Basin Natural Gas Development Project (UT) ----------------
N = "Uinta Basin Natural Gas Development Project (Gasco)"
GA_ROD = "http://www.blm.gov/style/medialib/blm/ut/vernal_fo/planning/gasco_eis/gasco_rod.Par.41068.File.dat/Gasco%20ROD%2006152012.pdf"
GA_CH4 = "http://www.blm.gov/style/medialib/blm/ut/vernal_fo/planning/gasco_eis/gasco_folder_2.Par.68725.File.dat/08_Gasco%20Chapter%204.%20Environmental%20Consequences.pdf"
GA_STATUS = ("predevelopment", "2012", "https://www.sec.gov/Archives/edgar/data/1086319/000110465913017945/a12-29294_110k.htm")
R("R1060", N, "wells_approved", "wells", 1114, 1298, 1887, "expansion", *GA_STATUS, GA_ROD,
  "Under the Selected Alternative, Gasco could drill as many as 1,298 new gas production wells from up to 575 pads within the analyzed development area.", "high",
  "ROD June 15 2012, Alt F (Agency Preferred). Proposed Action (Alt A) = 1,491 wells on 1,491 pads over 15 yr. Low = Alts B/E (1,114), high = Alt C (1,887). Read via Wayback copy of BLM Vernal FO page. STATUS: Gasco FY2012 10-K: existing field had 133 gross producing wells; 'Due to low natural gas prices and permitting delays, we did not drill any natural gas wells in Utah' after the Wapiti deal through end-2012; company restructured Oct 2013 (Markham/Orogen took ~97.5% equity) and deregistered from SEC Dec 2013. Subsequent drilling NOT FOUND; treat ROD build-out as essentially unbuilt (existing ~133 wells producing).")
R("R1060b", N, "development_years", "years", "", 15, "", "expansion", *GA_STATUS, "https://www.govinfo.gov/content/pkg/FR-2012-03-16/pdf/2012-6324.pdf",
  "drilling 1,491 wells from the same number of well pads over a period of 15 years", "medium",
  "15 yr is Proposed Action drilling period per FEIS FR notice (seen via search summary); ROD gives total project life ~45 yr.")
R("R1060c", N, "gas_production_total", "Tcf", 1.17, 1.37, 1.99, "expansion", *GA_STATUS, GA_CH4,
  "Table 4-69. Natural Gas Produced by Alternative ... Number of wells ... 1,298 Gas produced (Tcf) ... 1.37 ... Assuming 1,052,985 Mcf per well.", "high",
  "ROD: 'The Selected Alternative provides for the production of an estimated 1.37 trillion cubic feet of natural gas'. No peak rate found (NOT FOUND).")
R("R1060d", N, "eur_per_well", "Bcf", "", 1.05, "", "expansion", *GA_STATUS, GA_CH4,
  "assuming 1,052,985 thousand cubic feet (Mcf) would be extracted per well over the life of the project", "high", "")
R("R1060e", N, "ghg_operations_annual", "short_tons_CO2e/yr", 389673, 557276, 660299, "expansion", *GA_STATUS, GA_CH4,
  "Table 4-15. Greenhouse Gases - Overall Operational Emissions (tons/year) ... Total in CO2e ... 557,276 (Agency Preferred)", "high",
  "Alt F (selected). 'tons' not stated metric; GWP CH4=21. Low=Alt B/E, high=Alt C.")

# ---------------- R1128 West Tavaputs Plateau (UT) ----------------
N = "West Tavaputs Plateau Natural Gas Full Field Development Plan (Bill Barrett)"
WTP_ROD = "http://www.oilandgasbmps.org/docs/UT37-WestTavaputsROD.pdf"
WTP_CH4 = "https://www.blm.gov/style/medialib/blm/ut/price_fo/oil_and_gas_2.Par.31304.File.dat/Chapter%204%20WTP%20FEIS%5B1%5D.pdf"
WTP_STATUS = ("operating", "2013", "https://www.sec.gov/Archives/edgar/data/1172139/000119312513070731/d445586d10k.htm")
R("R1128", N, "wells_approved", "wells", 558, 626, 807, "expansion", *WTP_STATUS, WTP_ROD,
  "BBC and other operators propose to develop approximately 626 natural gas wells from approximately 120 well pads (63 new well pads and 57 re-occupied well pads) on leased Federal lands over a 4 to 7 year period.", "high",
  "ROD July 2 2010 approved BBC's contracted development plan (626 wells). Proposed Action = 807 wells from 538 pads; low = 558 wells (alt. over 21-yr period). Expansion of existing Prickly Pear/Peter's Point units. STATUS (BBC FY2012 10-K): 298 gross producing wells end-2012; first ROD well spud Oct 27 2010; 86 new gross wells to sales in 2011, 16 drilled in 2012, no drilling planned 2013 (gas prices); 2012 production 95.3 MMcfe/d (34.9 Bcfe); assets sold to EnerVest Dec 2013. Roughly 120 of 626 ROD wells drilled (my sum, approximate).")
R("R1128b", N, "development_years", "years", 4, 7, 7, "expansion", *WTP_STATUS, WTP_ROD,
  "626 natural gas wells ... over a 4 to 7 year period", "high", "")
R("R1128c", N, "gas_production_peak", "MMcf/d", "", 250, "", "expansion", *WTP_STATUS, WTP_CH4,
  "it is estimated that BBC and other operators' Proposed Action would result in a potential recovery of up to 250 MMscf per day.", "high",
  "Proposed Action (807 wells) value; selected plan has 626 wells (no separate rate). FEIS says ultimate recovery 'unknown'. Per-well: shallow wells IP 2-4 MMscf/d, deep ~8 MMscf/d; condensate 1-2 bbl/d per well.")
R("R1128d", N, "ghg_operations_annual", "short_tons_CO2e/yr", "", 608748, "", "expansion", *WTP_STATUS, WTP_CH4,
  "Table 4.3-7 Comparison of WTP Proposed Action Greenhouse Gas Emissions ... WTP CO2 Emissions 553,539 ... WTP CH4 Emissions 2,629 (tons/year)", "high",
  "CO2e computed by me = 553,539 + 21 x 2,629 = 608,748 tons/yr (GWP 21). Proposed Action (807 wells), not the 626-well selected plan. 'tons' not stated as metric.")

# ---------------- R0835 White River FO Oil & Gas RMPA (CO) ----------------
N = "White River Field Office Oil and Gas Development RMP Amendment"
WR_ROD = "https://eplanning.blm.gov/public_projects/lup/65266/79043/91308/2015_Oil_and_Gas_Development_RMPA_ROD.pdf"
WR_CH4 = "https://files.library.northwestern.edu/transportation/online/unrestricted/EIS/2015/20150080/05_WRFO_OG_RMPA-FEIS_Ch4_EC_2015.pdf"
WR_ST = "https://www.blm.gov/sites/default/files/docs/2024-02/NW%20RAC%20Consolidated%20Manager%20Reports%20Feb%202024.pdf"
WR_STATUS = ("operating", "2024", WR_ST)
R("R0835", N, "rfd_wells", "wells", 4603, 15040, 21200, "programmatic", *WR_STATUS, WR_ROD,
  "Management of oil and gas development under the Approved RMPA combines elements of the four alternatives ... reflecting surface disturbance associated with development of 13,200 acres, while assuming development of 15,040 wells.", "high",
  "ROD Aug 20 2015 (Approved RMPA = Alt E). RFD over 20-yr period (2009-2028 per 2007 RFD); ~1,100 multi-well pads (972 in Mesaverde Play Area). Low = Alt A (no action, 4,603 wells), high = Alt D (21,200 wells). Land-use plan amendment; does not authorize individual wells. STATUS: BLM NW District manager report Feb 2024: ~3,400 active oil and gas wells in WRFO, 65 APDs processed + 30 pending, 2 active rigs in Piceance. Build-out far below RFD pace (~750 wells/yr implied); exact wells drilled 2015-2026 NOT FOUND.")
R("R0835b", N, "acres_available", "acres", "", 1700000, "", "programmatic", *WR_STATUS, WR_ROD,
  "Approximately 1.7 million acres of Federal oil and gas mineral estate is open to leasing and would be subject to lease stipulations", "high",
  "Out of 2.2 million acres federal mineral estate in WRFO.")
R("R0835c", N, "development_years", "years", "", 20, "", "programmatic", *WR_STATUS, WR_ROD,
  "the 2007 RFD Scenario ... projected the potential need for the construction of between 550 and 2,556 multiple well pads, averaging eight drilled wells per pad, over a 20-year period (2009 through 2028)", "high", "")
R("R0835d", N, "ghg_operations_annual", "tCO2e/yr", 2288465, 4195059, 5251537, "programmatic", *WR_STATUS, WR_CH4,
  "Table 4-31. 2028 Alternative E Planning Area GHG Emissions ... (mtpy) ... CO2e of Each GHG and Total CO2e 2,486,525 1,702,738 5,795 4,195,059", "high",
  "Metric t/yr in peak year 2028, Alt E (approved) oil & gas sources; low = Alt A, high = Alt C (Alt D also higher; not extracted). No downstream combustion estimate found.")
R("R0835e", N, "gas_production_peak", "Bcf/yr", "", 1162, "", "programmatic", *WR_STATUS, WR_CH4,
  "Unit-production CO2e emissions for Alternative E are estimated to be 3.61 mt of CO2e per MMscf", "low",
  "DERIVED by me, not stated in EIS: 4,195,059 t / 3.61 t per MMscf = ~1.16 million MMscf = ~1,162 Bcf/yr (~3.2 Bcf/d) implied 2028 gas production. No explicit production estimate found in FEIS Ch4/ES/App H (NOT FOUND). Treat as an upper-bound implied RFD production, far above actual WRFO output.")

# ---------------- R0787 Previously Issued O&G Leases in WRNF (BLM, CO) ----------------
N = "Previously Issued Oil and Gas Leases in the White River National Forest"
PIL_FR = "https://www.govinfo.gov/content/pkg/FR-2016-11-30/html/2016-28807.htm"
PIL_ES = "https://eplanning.blm.gov/epl-front-office/projects/nepa/65550/79303/91619/_Front_Matter_with_Executive_Summary.pdf"
PIL_ST = "https://www.aspenpublicradio.org/2018-09-10/judge-dismisses-thompson-divide-lawsuit-lease-cancellations-stand"
PIL_STATUS = ("operating", "2018", PIL_ST)
R("R0787", N, "leases_cancelled", "leases", "", 25, 65, "continuation", *PIL_STATUS, PIL_FR,
  "Under the BLM's Previously Issued Oil and Gas Lease ROD, 25 undeveloped leases are administratively cancelled in full, 12 undeveloped leases remain open with new stipulations applied under Alternative 4 (with lessee consent), 20 producing or committed leases are reaffirmed or modified", "high",
  "DECISION (ROD Nov 17 2016): of 65 leases (80,380 ac) analyzed: 25 cancelled (Thompson Divide area, none producing), 12 undeveloped kept with new stips, 20 producing/committed reaffirmed or modified, 4 expired Willow Creek Unit leases under appeal (Alt 2 if appeal succeeds), 1 expired lease (Alt 4 if reauthorized), no decision on 3 expired leases. High = Alt 5 (cancel all 65). STATUS: SG Interests suit over 18 of the cancelled leases settled 2018 ($1.5M), cancellations stand (Aspen Public Radio, medium). Producing leases continue; post-2016 drilling on retained leases NOT FOUND.")
R("R0787b", N, "leases_retained", "leases", "", 37, "", "continuation", *PIL_STATUS, PIL_FR,
  "12 undeveloped leases remain open with new stipulations ... 20 producing or committed leases are reaffirmed or modified ... four expired leases currently under appeal ... one expired lease subject to appeal", "high",
  "Computed: 12 + 20 + 4 + 1 = 37 leases retained or conditionally retained (my sum).")
R("R0787c", N, "rfd_wells", "wells", "", 375.6, 416.4, "continuation", *PIL_STATUS, PIL_ES,
  "Table ES-2 Number of Projected Wells by Alternative ... Totals (80,380 acres) Vertical/Directional Wells ... 358.4 ... Horizontal wells ... 17.2 (Preferred Alternative)", "high",
  "Preferred Alt (basis of ROD) = 358.4 vertical/directional + 17.2 horizontal = 375.6 wells on 53.7 pads (my sum); Alt 1/2 = 416.4. FEIS says 444 wells unconstrained in 65 leases. 20-yr RFDS (USFS 2010). ROD modified Preferred Alt slightly (7 more leases cancelled in full), so ROD-level wells likely slightly lower.")
R("R0787d", N, "ghg_operations_annual", "tCO2e/yr", 908770, "", 1160586, "continuation", *PIL_STATUS, PIL_ES,
  "The range of annual contribution to global greenhouse gas emissions is estimated to be between 908,770 metric tons of carbon dioxide equivalent and 1,160,586 metric tons ... for the maximum oil and gas production year in 2021.", "medium",
  "Range across development levels; scope (upstream only vs incl. end-use) not confirmed for this number. FEIS Ch4 also gives CRVFO-wide (outside Roan) federal O&G GHG incl. end-use CO2 of 5.4-7.9 Mt CO2e/yr (2021) - field-office-wide, not lease-specific.")

# ---------------- R1139 White River NF Oil and Gas Leasing (USFS, CO) ----------------
N = "White River National Forest Oil and Gas Leasing"
WN_B = "https://files.library.northwestern.edu/transportation/online/unrestricted/EIS/2014/20140361/"
WN_DROD = WN_B + "WRNF%20Oil%20and%20Gas%20DRAFT_ROD_12_14.pdf"
WN_FEIS = WN_B + "Final%20EIS%20(entire%20document).pdf"
WN_STATUS = ("unknown", "", "")
R("R1139", N, "acres_available", "acres", "", 194123, "", "programmatic", *WN_STATUS, WN_DROD,
  "194,123 acres will be Administratively Available for Leasing", "high",
  "From DRAFT ROD (Dec 2014) in the FEIS package; final ROD signed Dec 2015 (per BLM FR notice) - final ROD text not retrieved, press coverage gives 194,100 ac. Decision = combination of Alts B and C; 800,555 ac legally closed; 1,281,726 ac closed by management direction. Press (Herald Times) reports ~176,000 ac closed that had been open.")
R("R1139b", N, "rfd_wells", "wells", 258, 487, 1014, "programmatic", *WN_STATUS, WN_FEIS,
  "Table 34 ... Total Number of Wells 678 (A) 258 (B1) 442 (B2) 355 (C1) 487 (C2) ... (based on 20 year development timeline)", "high",
  "20-yr RFDS. Decision combined Alts B and C, so central set to Alt C Scenario 2 (487) as upper end of selected range; low = Alt B Scen 1 (258); high = unconstrained baseline RFDS (up to 1,014). No Action (A) = 678. STATUS: actual wells drilled on WRNF leases 2015-2026 NOT FOUND; most projected activity is on Rifle/Sopris RDs (Piceance margin) with existing producing leases; 2024 Thompson Divide mineral withdrawal (not verified here) further limits new leasing.")
R("R1139c", N, "ghg_operations_annual", "short_tons_CO2e/yr", 81070, 151439, 210106, "programmatic", *WN_STATUS, WN_FEIS,
  "Table 34. Greenhouse Gas (GHG) Emission Estimates ... TOTAL GHG Emissions (CO2e) 210,106 81,070 137,552 110,879 151,439", "high",
  "tons/yr (units not stated metric); central = Alt C2 (487 wells); low = B1; high = Alt A. Simple CO2 + 20% non-CO2 allowance method. No downstream.")

# ---------------- R0751 Pawnee National Grassland O&G Leasing (USFS, CO) ----------------
N = "Pawnee National Grassland Oil and Gas Leasing Analysis"
PW_B = "https://files.library.northwestern.edu/transportation/online/unrestricted/EIS/2014/20140350/"
PW_DROD = PW_B + "FEIS%20Draft%20ROD.pdf"
PW_FEIS = PW_B + "FEIS%20Pawnee%20Oil%20and%20Gas.pdf"
PW_ST = "https://wsmtlaw.com/news/at-last-a-federal-oil-and-gas-lease-sale-in-the-pawnee-national-grasslands"
PW_STATUS = ("operating", "2015", PW_ST)
R("R0751", N, "acres_available", "acres", "", 100000, "", "programmatic", *PW_STATUS, PW_DROD,
  "This decision will continue to make nearly all federal unleased lands on the PNG available for oil and gas leasing-approximately 100,000 acres.", "high",
  "Selected NSO Alternative (ROD signed Feb 9 2015; draft ROD text read). All available lands carry No Surface Occupancy: federal minerals reachable only by horizontal wells from adjacent non-federal/private/already-leased lands. 2,980 ac unavailable. STATUS: BLM offered 42 parcels / 25,215 PNG mineral acres (all NSO) at May 14 2015 sale (law-firm summary, medium); outcome of sale and wells drilled NOT FOUND. Surrounding DJ Basin (Weld County) development is active.")
R("R0751b", N, "rfd_wells", "wells", 0, 265, 354, "programmatic", *PW_STATUS, PW_FEIS,
  "Approximately 265 new and exploratory wells would be drilled. Of those wells, 234 producing wells would remain in the long term.", "high",
  "BLM 2012/2013 RFD (2013-2033, 20 yr). Under NSO alt no wells/pads on unleased PNG surface (low=0), but horizontal wells from adjacent lands still extract the resource; No Leasing alt = 292 wells on adjacent lands. High = 354 wells accessing federal minerals in CARMMS air scenario.")
R("R0751c", N, "oil_production_total", "MMbbl", 178, 590, 590, "programmatic", *PW_STATUS, PW_FEIS,
  "100% recovery of oil and gas resources (590 million barrels of oil and 1180 MCF of gas will be produced from existing and unleased lands)", "medium",
  "FEIS summary table: NSO alt = 100% recovery (590 MMbbl oil + '1180 MCF' gas - unit evidently garbled, likely Bcf); No Leasing = 178 MMbbl from existing leases only. Incremental from unleased lands ~412 MMbbl (my subtraction). Numbers look high relative to 265 wells (~2.2 MMbbl/well) - treat as resource-in-place-style estimate; flag.")
R("R0751d", N, "ghg_operations_annual", "tCO2e/yr", "", 231269, 253293, "programmatic", *PW_STATUS, PW_FEIS,
  "Table 57 Maximum Annual Potential Greenhouse Gas Emissions from Pawnee NG Development Under the 2021 High Development Scenario (tons) ... 254,859 231,269 (metric tons)", "high",
  "Metric t/yr, 354-well high scenario, GWP 21; high = GWP 25 (253,293 t). FEIS states it excludes processing and end-use emissions.")

# ---------------- R0316 Fishlake NF Oil and Gas Leasing (USFS, UT) ----------------
N = "Fishlake National Forest Oil and Gas Leasing Analysis"
FL_B = "https://files.library.northwestern.edu/transportation/online/unrestricted/EIS/2013/20130265/"
FL_ROD = FL_B + "ROD%20Fishlake%20Oil%20and%20Gas%20Leasing.pdf"
FL_FEIS = FL_B + "Fishlake%20Oil%20and%20Gas%20ROD%20and%20EIS.pdf"
FL_ST = "https://www.blm.gov/press-release/november-2015-lease-sale-rescheduled-february-2016"
FL_STATUS = ("predevelopment", "2016", FL_ST)
R("R0316", N, "acres_available", "acres", "", 1707810, "", "programmatic", *FL_STATUS, FL_ROD,
  "Our decision will make approximately 1,707,810 acres of National Forest System land administratively available for oil and gas leasing ... Standard Lease Term 62,468 | CSU 209,120 | TL 82,359 | NSO 1,353,863", "high",
  "ROD (Alt C; signed Aug 20 2013) read by OCR of scanned ROD. Includes 253,299 ac of Dixie NF Teasdale unit. 1.35 M ac (79%) NSO. STATUS: frontier area with one 302-ac existing lease at time of EIS; BLM offered 4 Fishlake NF parcels (1,653 ac) in the Nov 2015 sale rescheduled to Feb 2016 (BLM press release); no Fishlake NF production found (NOT FOUND).")
R("R0316b", N, "rfd_wells", "wells", "", 73, "", "programmatic", *FL_STATUS, FL_FEIS,
  "Table 1.12-1: Predicted Number and Type of Wells ... Total fields/wells 43 wells 2 fields 30 wells 73 wells", "high",
  "15-yr RFDS: 43 exploration wells + 2 oil fields with 30 production wells (Sevier Frontal Zone play + other plays). Same RFD assumed under all action alternatives.")
R("R0316c", N, "oil_production_avg", "bbl/yr", "", 1095000, "", "programmatic", *FL_STATUS, FL_FEIS,
  "Average Production (barrels) 1,095,000 ... Based on lower-bound estimate of 6,000 barrels per day for the Sevier Frontal Zone field and 30 wells in production (6000/30=200 barrels per day per well x 15 wells in operation on average x 365 days)", "high",
  "= 3,000 bbl/d average (computed). Socioeconomic revenue table under full RFDS.")
R("R0316d", N, "ghg_operations_annual", "tCO2e/yr", "", 65709, "", "programmatic", *FL_STATUS, FL_FEIS,
  "Table 3.12-7 Estimated Emissions (Metric Tons of Carbon Dioxide Equivalent) ... Exploration 7,495 Production 58,214 ... Product End Use (off-site) 268,312 TOTAL 365,336", "medium",
  "Operations = exploration 7,495 + production 58,214 = 65,709 t (my sum). Time basis not stated in table (presumably annual at full RFD). See R0316e for downstream.")
R("R0316e", N, "ghg_downstream_annual", "tCO2e/yr", "", 299627, 365336, "programmatic", *FL_STATUS, FL_FEIS,
  "Transportation of Crude 2,161 Refining 28,286 Transportation of Refined 868 Product End Use (off-site) 268,312 TOTAL 365,336", "medium",
  "Downstream = 2,161 + 28,286 + 868 + 268,312 = 299,627 t (my sum); end use alone 268,312; high = table TOTAL incl. operations.")

# ---------------- R1061 Uinta NF Oil and Gas Leasing (USFS, UT) ----------------
N = "Uinta National Forest Oil and Gas Leasing Implementation"
BOXF = "https://usfs-public.app.box.com/v/PinyonPublic/folder/"
UN_ROD = BOXF + "158565156077 (Uinta ROD_Final_02182011.pdf)"
UN_FSEIS = BOXF + "158567443680 (FSEIS.pdf)"
UN_STATUS = ("predevelopment", "", "")
R("R1061", N, "acres_available", "acres", 207280, 736070, "", "programmatic", *UN_STATUS, UN_ROD,
  "My decision will make approximately 736, 070 acres of the area analyzed (see Table 1) administratively available for oil and gas leasing.", "high",
  "ROD signed Feb 18 2011 (FS Pinyon Public Box archive, project 3021). 511,480 ac of these are in IRAs and leasable only with NSO/NGD stipulation; 9,880 ac recommended wilderness unavailable. Low = Alt 1 no action (207,280 ac available). STATUS: area historically all dry holes (13 wells 1945-1995, all P&A per FSEIS); no subsequent Uinta NF production found (NOT FOUND).")
R("R1061b", N, "rfd_wells", "wells", 5, 12, 12, "programmatic", *UN_STATUS, UN_ROD,
  "The FEIS predicts that a total of 12 wells could be developed over 15 years.", "high",
  "12 exploratory wells over 15 yr across 9 RFDS areas; range 5-12 by alternative. FSEIS socioeconomics assumes average 18,165 bbl/well/yr if productive (not a field-level production estimate).")

# ---------------- R0730 Dixie NF Oil and Gas Leasing (USFS, UT) ----------------
N = "Oil and Gas Leasing on Lands Administered by the Dixie National Forest"
DX_RFDS = "http://www.fs.fed.us/r4/dixie/projects/oil_gas/RFDS/RFDS_doc.pdf"
DX_APP = BOXF + "158554794594 (Administrative Review Response - Mueller, Kevin.pdf)"
DX_STATUS = ("predevelopment", "", "")
R("R0730", N, "rfd_wells", "wells", "", 80, "", "programmatic", *DX_STATUS, DX_RFDS,
  "It is estimated here that 60 exploration wells will be drilled during the next 15 years possibly resulting in the discovery of one new oil field with 20 production wells.", "medium",
  "From the RFDS report (archived 2009 project page, pre-FEIS); appeal response confirms 'All of the alternatives, with the exception of Alternative A, forecast the same reasonably foreseeable development scenario'. 60 exploration + 20 production = 80 wells over 15 yr (my sum). Study area ~1,627,837 ac (2006 NOI). ROD (signed by Forest Supervisor Robert MacWhorter; affirmed on appeal) acres available NOT FOUND - ROD/FEIS text not retrieved. Teasdale unit later folded into Fishlake decision (R0316). STATUS: no Dixie NF oil production found (NOT FOUND).")

# ---------------- R0958 South Unit O&G Development (Ashley NF, UT) ----------------
N = "South Unit Oil and Gas Development Project (Berry Petroleum), Ashley NF"
SU_ROD = BOXF + "158553124626 (Record of Decision - February 21, 2012.pdf)"
SU_FEIS = BOXF + "158553259670 (South Unit Oil and Gas Development - FEIS Vo 1.pdf)"
SU_NOTE = BOXF + "395873224242 (20260701NoteToFileHeritageDesignCriteria.pdf)"
SU_STATUS = ("unknown", "2026", SU_NOTE)
R("R0958", N, "wells_approved", "wells", "", 356, 400, "expansion", *SU_STATUS, SU_ROD,
  "A maximum of 356 new wells will be drilled. The Operator's original MDP estimated that up to 400 wells would be needed ... 44 new wells have been approved in separate NEPA decisions.", "high",
  "ROD Feb 21 2012: up to 356 wells on up to 162 new pads (directional), 57 mi new road; 25,900-ac project area (Green River/Wasatch oil). Proposed MDP = 400 wells. STATUS: Ashley NF June 2026 note to file modifies heritage design criteria for the still-active project, but gives no count of wells drilled (NOT FOUND).")
R("R0958b", N, "development_years", "years", 5, 20, 20, "expansion", *SU_STATUS, SU_ROD,
  "Drilling is expected to occur over a 5- to 20-year period following this decision, with approximately 20-40 wells drilled per year.", "high",
  "Up to 55 yr including production.")
R("R0958c", N, "eur_per_well", "Mbbl", 14, "", 61, "expansion", *SU_STATUS, SU_FEIS,
  "Table 3-84. Average EUR and Most Frequent Interval ... 1998 25 ... 2001 61 ... 2006 14 (Mstb)", "high",
  "Historic average oil EUR per well by completion year (operator data), range 5-82 Mstb, quarter of wells 20-30 Mstb. Implies ~356 x 25 Mstb ~ 9 MMbbl total (my rough product, low confidence). No field-level production estimate found.")
R("R0958d", N, "ghg_operations_annual", "tCO2e/yr", "", 106000, "", "expansion", *SU_STATUS, SU_FEIS,
  "Table 3-18. Modeled GHG Emissions. CO2 Equivalent (metric tons/year) Proposed Action 1.06E+05 ... Year of maximum emissions", "high",
  "Proposed Action (400 wells), maximum year; no downstream.")

# ---------------- R0127 Bull Mountain Unit MDP (BLM, CO) ----------------
N = "Bull Mountain Unit Master Development Plan (SG Interests)"
BM_FR = "https://www.govinfo.gov/content/pkg/FR-2017-10-04/html/2017-20948.htm"
BM_FEIS = "https://files.library.northwestern.edu/transportation/online/unrestricted/EIS/2016/20160151/Bull_Mtn_Final_EIS_July_2016_Vol_I_reduced.pdf"
BM_PR = "https://blm.gov/press-release/blm-issues-decision-bull-mountain-unit-master-development-plan"
BM_STATUS = ("unknown", "", BM_PR)
R("R0127", N, "wells_approved", "wells", 55, 146, 146, "expansion", *BM_STATUS, BM_FR,
  "The Selected Alternative approves a plan for the exploration and development of up to 146 natural gas wells, four water disposal wells, and associated infrastructure on Federal and private mineral leases", "high",
  "ROD (Oct 2017) selected Alt D (BLM Preferred); MDP framework for 146 gas wells (CBM + shale) + 4 water disposal wells; approves only ONE federal APD (12-89-7-1), further APDs need site-specific review (BLM press release). Low = Alt A no action (55 wells on private minerals). 19,670-ac unit near Paonia; existing 9-12 producing wells. STATUS: post-2017 drilling NOT FOUND.")
R("R0127b", N, "development_years", "years", 3, 6, 6, "expansion", *BM_STATUS, BM_FEIS,
  "Drilling rate 27 wells per year ... Drilling duration 3 years (Alt A) ... 6 years (action alts)", "high",
  "Well life 40 yr, project analysis horizon 50 yr.")
R("R0127c", N, "gas_production_existing", "Bcf/yr", "", 0.93, "", "expansion", *BM_STATUS, BM_FEIS,
  "Table 2-5 Bull Mountain Unit Annual Production Rates ... 2014 9 ... 923,948 (MCF) ... 2015 (through July) 928,815", "high",
  "Existing-unit baseline (9 producing wells, ~0.93 Bcf in 2014), NOT a project forecast. No full-field production or EUR estimate found in FEIS Vol I (NOT FOUND).")
R("R0127d", N, "ghg_operations_annual", "tCO2e/yr", "", 44389, "", "expansion", *BM_STATUS, BM_FEIS,
  "Table 4-13 Alternative B Year 5 GHG Emissions (metric tons per year) ... CO2e 7,107 37,282 44,389", "high",
  "Alt B year 5 (construction + production); FEIS says Alt D (selected) GHG 'comparable to the emissions estimated for Alternative B'. No downstream.")

# ---------------- R0771 Point Thomson (USACE, AK) ----------------
N = "Point Thomson Project (ExxonMobil; Corps Section 404/10 permit)"
PT_V1 = "https://www.arlis.org/docs/vol1/AlaskaGas/Report3/Report_PtThom_FEIS/v1.pdf"
PT_V2 = "https://www.arlis.org/docs/vol1/AlaskaGas/Report3/Report_PtThom_FEIS/v2.pdf"
PT_ST = "https://alaskapublic.org/news/2021-10-22/exxon-transfers-point-thomson-operations-to-hilcorp"
PT_STATUS = ("operating", "2016", PT_ST)
R("R0771", N, "oil_production_peak", "bbl/d", "", 10000, 70000, "new_build", *PT_STATUS, PT_V1,
  "Initial production of liquid hydrocarbons is expected to be approximately 10,000 bpd [barrels per day].", "high",
  "Gas-condensate cycling project (Thomson Sand): condensate to TAPS via export pipeline sized for 70,000 bpd design flow (high = pipeline design, for possible later expansion). Corps ROD Oct 2012. Field est. 8 Tcf gas reserves (FEIS Ch3) - gas reinjected, not sold. STATUS: first production April 2016 (ExxonMobil). Petroleum News (via search snippet, page not opened) reported Jan 2020-Jul 2021 average 8,300 bbl/d (peak month 9,600); a Jan 2026 Alaska DNR presentation (search snippet only, Cloudflare-blocked) lists 'Producing ~ 4,140 bbl oil per day', operator Hilcorp (operatorship transferred from ExxonMobil, approved Dec 2021; ExxonMobil retains ~60% ownership). Current-rate figures = low confidence.")
R("R0771b", N, "gas_cycling_rate", "MMscf/d", "", 200, 450, "new_build", *PT_STATUS, PT_V1,
  "This pipeline would operate at 200 mmscfd, and would ... [convey] dry gas to the reinjection well", "high",
  "Gas produced, stripped of liquids and reinjected (no gas sales). High = 450 MMscfd variant considered in FEIS alternatives development. Minimum 5 wells from 3 pads (Central, East, West).")
R("R0771c", N, "ghg_operations_annual", "tCO2/yr", 238000, 302000, "", "new_build", *PT_STATUS, PT_V2,
  "Table 5.4-9: Annual Million Metric Tons of CO2 ... Action Alternatives - Total 0.302 ... Stationary Sources 0.238", "high",
  "Metric t CO2 (not CO2e) per year, operations phase, all action alternatives. FEIS explicitly excludes end-use combustion: 'the indirect impacts of use of the product from Point Thomson are not included in this EIS'.")

# ---------------- R0920 Shadura Natural Gas Development (FWS, Kenai NWR, AK) ----------------
N = "Shadura Natural Gas Development Project, Kenai NWR (NordAq / CIRI)"
SH_FEIS = "https://files.library.northwestern.edu/transportation/online/unrestricted/EIS/2013/20130132/FWS_R7_ShaduraNatGas_FEIS.pdf"
SH_ST = "https://peninsulaclarion.com/news/state-reduces-fine-for-nordaq-wells"
SH_STATUS = ("cancelled", "2018", SH_ST)
R("R0920", N, "wells_approved", "wells", 1, 6, 6, "new_build", *SH_STATUS, SH_FEIS,
  "Should well testing be successful, six wells and associated production facilities would be operated over a 30-year period.", "high",
  "FWS ROD June 28 2013 (access road/pad on CIRI subsurface estate in refuge). Two-stage plan: Stage 1 one test well on minimal pad; full build 6 wells (low=1). Facility design volume 50 MMcf/d per NordAq 2011 website as reported by Petroleum News 2012 (search snippet; company said actual output could be much lower) - not in FEIS text I grepped. STATUS: never developed. Peninsula Clarion: NordAq ended its CIRI lease June 2015; Shadura No.1 exploration well (2011) plugged and abandoned March 19 2018. Medium.")
R("R0920b", N, "ghg_operations_annual", "short_tons_CO2e/yr", "", 29397, "", "new_build", *SH_STATUS, SH_FEIS,
  "Table 4-4 Operational Emissions-Alternative 2 ... CO2equivalent 29,396.7 ... Duration Initial 1st Year", "high",
  "'tons' (unit basis not stated as metric); first operating year. Construction 2,390 + 2,232 t. No production volume estimate found in FEIS (NOT FOUND).")
