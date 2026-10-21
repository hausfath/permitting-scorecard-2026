import csv, sys
OUT = "/private/tmp/claude-501/-Users-hausfath-Desktop-Climate-Science-The-Climate-Brink/42175875-4e02-4e65-ab8f-a48a292e262b/scratchpad/sizing/out/A5_factors.csv"
COLS = ["factor", "value_low", "value_central", "value_high", "unit", "source_title", "source_url",
        "exact_quote", "page_or_section", "verified_fetched", "notes"]
R = []
def row(*a):
    assert len(a) == len(COLS), (len(a), a[0])
    R.append(dict(zip(COLS, a)))

RFF_IB = "https://www.rff.org/documents/4590/IB_24-09_-_updated.pdf"
RFF_IB_T = "Prest (2024) How Much Would Expanding Federal Oil and Gas Leasing Increase Global Carbon Emissions? RFF Issue Brief 24-09 (Sept 3 2024)"
PREST22 = "https://www.rff.org/documents/3229/WP_20-16__Dec_2021.pdf"
PREST22_T = "Prest (2022) Supply-Side Reforms to Oil and Gas Production on Federal Lands: Modeling the Implications for CO2 Emissions, Federal Revenues, and Leakage. JAERE 9(4):681-720 (RFF WP 20-16, Dec 2021 version = accepted text)"
PFGC = "https://www.rff.org/documents/4416/Prest_Fell_Gordon_Conway_2024_Updated_-_Combined.pdf"
PFGC_T = "Prest, Fell, Gordon & Conway (2024) Estimating the Emissions Reductions from Supply-side Fossil Fuel Interventions. Energy Economics 136:107720, doi:10.1016/j.eneco.2024.107720 (Crossref-verified; text quoted from RFF WP 23-11 updated 2024 PDF)"
GRS = "https://www.nber.org/system/files/working_papers/w22214/w22214.pdf"
GRS_T = "Gerarden, Reeder & Stock (2016) Federal Coal Program Reform, the Clean Power Plan, and the Interaction of Upstream and Downstream Climate Policies. NBER WP 22214 (2016); published AEJ: Economic Policy 12(1):167-199 (2020), doi:10.1257/pol.20160246 (Crossref-verified)"
DOE_S = "https://www.energy.gov/documents/energy-economic-and-environmental-assessment-us-lng-exportspdf"
DOE_S_T = "DOE (Dec 2024) Energy, Economic, and Environmental Assessment of U.S. LNG Exports: Summary Report (2024 LNG Export Study; Oct 2025 cover note added)"
DOE_B = "https://www.energy.gov/sites/default/files/2024-12/LNGUpdate_AppendixB_Dec2024.pdf"
DOE_B_T = "DOE (Dec 2024) 2024 LNG Export Study Appendix B: Domestic Energy, Economic, and Greenhouse Gas Assessment of U.S. LNG Exports (OnLocation/IEc, NEMS)"

# ---------------- 3. Leakage / substitution ----------------
row("Leakage rate, federal oil (and gas) supply (fraction of federal production offset by other supply)",
    0.36, 0.57, 0.79, "fraction", RFF_IB_T, RFF_IB,
    "Prest et al. (2024) conduct a meta-analysis of such elasticities, finding a central estimate for the leakage rate of 57 percent, which I use here ... each incremental barrel of federal oil production is assumed to result in 0.57 barrels of reduced oil production elsewhere and 0.43 barrels of pure increase in oil consumption, and similarly for gas. || Prest et al. (2024), who present a 95 percent range of leakage rates of approximately 36 to 79 percent.",
    "p.2 (Methods) and p.5 (Sensitivity, third)", "yes",
    "Same 57% applied to gas in the brief (no separate gas rate). Range is 95% interval from Prest et al. 2024 meta-analysis, which is oil-market based.")
row("Net-of-leakage fraction (1 - leakage), federal OIL",
    0.21, 0.43, 0.64, "fraction of gross combustion CO2", RFF_IB_T, RFF_IB,
    "0.43 barrels of pure increase in oil consumption ... each incremental barrel of federal oil that is produced results in (0.43 barrels) x (0.43 tCO2/barrel) = 0.185 tCO2 of additional global emissions.",
    "p.2", "yes",
    "Derived: 1-0.79=0.21, 1-0.57=0.43, 1-0.36=0.64. Prest (2022) JAERE gives 28-48% net (leakage 52-72%) with 72% base case; ROW-supply sensitivity widens leakage to 52-78% (net 22-48%). Global, not US-territorial: brief says >80% of induced consumption occurs outside US.")
row("Net-of-leakage fraction (1 - leakage), federal GAS",
    0.21, 0.43, 0.64, "fraction of gross life-cycle CO2e", RFF_IB_T, RFF_IB,
    "0.43 barrels of pure increase in oil consumption, and similarly for gas.",
    "p.2", "yes",
    "Brief applies oil-derived 57% to gas; Prest et al. 2024 (Energy Econ) footnote 23 says gas curtailment issues (gas-coal interaction) are 'beyond the scope of this paper', so the gas number is an extrapolation. Gas net emissions ALSO depend on what the gas displaces: see next row (0.034 vs 0.066 tCO2e/mcf).")
row("Federal gas emission factor, gross vs net-of-fuel-displacement",
    0.034, 0.066, 0.066, "tCO2e per mcf (GWP100, 2.3% leak)", RFF_IB_T, RFF_IB,
    "I use the same emissions factors as in Prest (2022) of 0.43 tons of carbon dioxide (tCO2) per barrel of oil and 0.066 tCO2e per thousand cubic feet (mcf) of gas, which corresponds to a 2.3 percent methane leak rate and a 100-year GWP. || the implied net gas emissions rate is 0.034 tCO2e per mcf. In this sensitivity analysis, this lower net emissions rate is used in place of the 0.066 tCO2e/mcf value used in the main analysis, lowering net gas-related emissions by about half.",
    "p.2; Appendix A p.9", "yes",
    "0.034 is from Prest (2022) using AEO2021 high/low oil-supply cases to infer what incremental gas displaces (mix of coal and clean power). Prest (2022) calls 0.034 'likely a conservative lower bound on the net gas emissions rate'. 0.066 = 117 lb CO2/mcf combustion + 28.55 lb CO2e methane. No-methane factor 0.053 tCO2/mcf.")
row("Leakage rate, federal oil & gas (Prest 2022 JAERE, leasing ban)",
    0.52, 0.72, 0.78, "fraction", PREST22_T, PREST22,
    "leakage rates are also substantial, ranging between 52 and 72 percent, depending on oil and gas demand elasticity assumptions. This means that, for example, the federal reductions of 292 MMTCO2 e from a leasing ban translate into only 80 to 139 MMTCO2 e worth of reductions in net global emissions. ... Leakage to US producers on state and private lands constitutes about 30 percent of the total leakage effect || the leakage rate varies in a range between 52 and 78 percent, compared to the 72 percent base case.",
    "Introduction p.~5; Section 4 results p.24-25", "yes",
    "72% is the base (low demand elasticity) case; 52% is the high-demand-elasticity case; 78% high ROW supply elasticity. Net-of-leakage 0.22-0.48. Text is the Dec 2021 accepted WP; check published JAERE pagination before quoting.")
row("Net life-cycle emissions reduction per barrel curtailed (supply-side intervention, oil)",
    0.40, 0.45, 0.50, "fraction of gross life-cycle emissions", PFGC_T, PFGC,
    "We find a rough band of central estimates for life-cycle emissions reductions from supply-side interventions in the range of 40-50 percent of the gross life-cycle emissions of each barrel curtailed, depending on the relative emissions intensity of the curtailed and substitute sources of supply. || almost identical means (56.9 percent versus 56.7 percent)",
    "Abstract; Section 4 (Fig. 4 discussion)", "yes",
    "Central 0.45 is midpoint of quoted band (my choice). Oil only; footnote 23: 'Modeling the curtailment of gas supply raises other issues that are beyond the scope of this paper, such as the interaction between gas and coal demand.'")
row("Net-of-substitution fraction, federal COAL (Powder River Basin; power-sector IPM, no CPP)",
    0.11, 0.50, 0.50, "fraction of gross combustion CO2 of foregone federal coal", GRS_T, GRS,
    "the 100% SCC adder on federal coal results in a 260 million metric ton (MMT) emissions reduction in 2030 relative to the no-CPP, no-adder case ... driving it from 318 million short tons in 2030 under the no-CPP, no-adder case to 11 million short tons in the no-CPP, 100% SCC adder case, a decline of 307 million short tons. This decline in PRB production is partially offset by a 42 million short ton increase in non-PRB coal production, or an offset of 14%. ... the main substitution is from federal coal to natural gas and, to a lesser extent, renewables.",
    "Section 5, p.26-27", "yes",
    "DERIVED central 0.50: 307 Mst x 17.6 MMBtu/st (paper's 8800 Btu/lb PRB) x 97.2 kg/MMBtu (paper's 214.3 lb/MMBtu) = 525 MMT gross; 260/525 = 0.495. Coal-to-coal leakage only 14% by tonnage; the rest of the gap is gas generation replacing coal. Electricity demand exogenous (no demand response) and no export-market leakage, so this is power-sector-only. Low 0.11 = binding mass-based-CPP case from Table 4 (next row); high left at 0.50 (no sourced higher value; demand response would push it up, export leakage down). NBER 2016 text; numbers may differ in AEJ 2020 version (not checked). Under a mass-based CPP the incremental reductions are much smaller (CPP binding) -- policy context dependent.")
row("Erickson & Lazarus (2018) federal leasing phase-out net global CO2 reduction",
    "", 280, "", "MtCO2/yr by 2030 (all federal fossil leases)", "Erickson & Lazarus (2018) Would constraining US fossil fuel production affect global CO2 emissions? A case study of US leasing policy. Climatic Change 150(1-2):29-42 (2018), doi:10.1007/s10584-018-2152-z [citation metadata verified via Crossref API; text not opened]",
    "https://doi.org/10.1007/s10584-018-2152-z",
    "[search snippet, not opened] 'such a policy would reduce U.S. emissions of carbon dioxide by 5 percent, or 280 million tons annually by 2030' (Salt Lake Tribune); SEI 2016 WP: 'could reduce global CO2 emissions by 100 million tonnes per year by 2030' with range 'as little as 4 Mt CO2' to '210 Mt CO2 in 2030'",
    "abstract (not opened)", "no",
    "UNVERIFIED: paywalled (Unpaywall is_oa=False); SEI site returns 403 to fetch tools. Coal-specific substitution fraction not retrieved. Citation metadata confirmed via api.crossref.org; numbers above are from search snippets only. Do not use values without opening the paper.")
row("Net-of-substitution fraction, federal COAL under binding downstream cap (GRS Table 4, mass-based CPP, 2040)",
    0.107, 0.11, 0.119, "fraction of gross combustion CO2 of foregone federal (PRB) coal", GRS_T, GRS,
    "Table 4 Comparison of Upstream Policies under Mass-based CPP, Prices and quantities in 2040: Emissions (MMT) 1,672 [no new upstream policy] 1,653 [20% SCC] 1,622 [100% SCC] 1,665 [50% cap] 1,631 [No new leases or renewals]; PRB prodn (MST) 266 171 20 232 42; Total coal prodn (MST) 763 730 661 756 678",
    "Section 5, Table 4, p.34", "yes",
    "DERIVED. No-new-leases: dCO2 = -41 MMT; dPRB = -224 Mst; dTotal coal = -85 Mst -> non-PRB coal +139 Mst (62% coal-to-coal offset). Gross = 224 x 17.6 MMBtu/st x 0.0972 t/MMBtu = 383 MMT; net 41/383 = 0.107. 100% SCC adder: 50/(246 x 1.711) = 0.119. Low net because the mass-based cap already binds (CPP no longer in force; illustrates that net effect depends on downstream policy). 2016 NBER text.")

# ---------------- 4. LNG exports ----------------
row("LNG exports: consequential global GHG intensity of additional US LNG (DOE 2024, core scenarios)",
    1.2, 6.3, 12.6, "g CO2e per MJ of additional US LNG exported (cumulative 2020-2050)", DOE_S_T, DOE_S,
    "Table ES-2 ... Defined Policies 20.3 [56.3] 113 [50%] 711 [0.05%] 0.08% 6.3; Commitments (High CCS) ... 3.1; Commitments (Mod CCS) ... 5.9; Net Zero (High CCS) ... 1.2 || global cumulative GHG emissions (2020-2050) are 324 MMT CO2e to 1,452 MMT CO2e higher ... equivalent to a range of 3.5 g CO2e/MJ to 12.6 CO2e/MJ for additional U.S. LNG exports.",
    "Summary Report p.S-6 to S-7, Table ES-2", "yes",
    "Low 1.2 = Net Zero High CCS core; central 6.3 = Defined Policies core (Existing/FID 23.7 -> Model Resolved 56.3 Bcf/d by 2050); high 12.6 = top of +20 Bcf/d High Exports sensitivities. Consequential = includes US upstream+liquefaction, shipping, ROW market effects; GHG incl. land sink. Oct 2025 cover note: DOE 'will not consider the environmental analysis' in export decisions (legal, not a scientific retraction).")
row("LNG exports: attributional (gross) life-cycle GHG intensity of US LNG used by DOE",
    "", 76, "", "g CO2e per MJ", DOE_S_T, DOE_S,
    "would cumulatively (2020-2050) contribute 8,588 MMT CO2e based on an attributional life cycle GHG profile of 76 g CO2e/MJ.",
    "Summary Report p.S-7", "yes",
    "Denominator for ratio row below.")
row("LNG exports: net global GHG as fraction of gross attributional life-cycle GHG",
    0.016, 0.083, 0.17, "fraction", DOE_S_T, DOE_S,
    "(derived from 1.2, 6.3, 12.6 g CO2e/MJ consequential vs 76 g CO2e/MJ attributional)",
    "Summary Report p.S-6 to S-7", "yes",
    "DERIVED. As fraction of US-gas COMBUSTION CO2 only (53.06 kg/MMBtu = 50.3 g/MJ HHV): 0.024 / 0.125 / 0.25. Model assumes global gas market in GCAM; MJ basis (HHV vs LHV) not checked in Appendix C.")
row("LNG exports: what additional US LNG displaces abroad (Defined Policies, cumulative 2020-2050, 113 EJ)",
    "", 0.37, "", "fraction of added US LNG displacing ROW gas production (also 0.25 renewables, 0.19 oil+coal)", DOE_S_T, DOE_S,
    "The largest share of this increase in exports, 37% of the total, displaces gas production in the rest of the world (ROW). Another 25% of the increase in U.S. LNG exports relative to existing and FID levels displaces renewables in the ROW, which puts upward pressure on global GHG emissions. At the same time, 19% of this increase displaces oil and coal, which puts downward pressure on global GHG emissions. Combined with an increase in primary energy demand (illustrated as net energy increase), the net effect ... is an increase in cumulative emissions of 708 MMTCO2e",
    "Summary Report Section IV.1, p.S-23 to S-24 (Fig. 4)", "yes",
    "Remaining ~19% is net energy increase (residual, inferred). Other core scenarios: 'More than half of the cumulative additional exports displace ROW sources of natural gas.'")
row("LNG exports: change in US domestic energy-related CO2 per unit added exports (NEMS, 2050)",
    "", 0.71, 1.41, "MtCO2/yr per Bcf/d of added exports (2050)", DOE_B_T, DOE_B,
    "The CO2 emission increase in Model Resolved compared to Existing/FID Exports scenarios is 23 MMT in Defined Policies with reference U.S. supply, 46 MMT in Defined Policies High US Supply, and 40 MMT in Defined Policies Low US Supply in 2050. || reflecting greater emissions associated with the production, transportation, and liquefaction of natural gas for export.",
    "Appendix B Section 9, p.B-38; Executive summary finding 4", "yes",
    "DERIVED: 23/32.6 = 0.71; 40/32.6 = 1.23; 46/32.6 = 1.41 (export difference 56.3-23.7 = 32.6 Bcf/d in all Defined Policies variants). Central = reference US supply (23 MMT, lowest of the three); high = High US Supply (46); Low US Supply gives 1.23. No lower case reported. As fraction of gross combustion CO2 of the exported gas (20.06 MtCO2/yr per Bcf/d at 1.036 MMBtu/Mcf x 53.06 kg): 0.035 / 0.061 / 0.070. Energy-related CO2 only; excludes upstream methane.")
row("LNG liquefaction GHG intensity (NETL average used by DOE)",
    "", 5.3, "", "g CO2e per MJ", DOE_S_T, DOE_S,
    "NETL estimates that the average liquefaction emissions for a project are 5.3 g CO2e/MJ. If an individual project has a liquefaction process with emissions of 2.9 g CO2e/MJ, the individual project consequential GHG intensity could be adjusted down by 2.4 g CO2e/MJ",
    "Summary Report Section VI.B, p.S-40", "yes",
    "Appendix C confirms basis: 'a GHG emissions intensity of 5.3 g CO2e/MJ of natural gas ready for export, reported on an IPCC AR6, 100-yr lower heating value (LHV) basis, and 5.6 g CO2e/MJ on an IPCC AR6, 20-yr' (App. C Section on Step 3). DERIVED: x ~49.5 MJ/kg LNG (LHV) = ~0.26 tCO2e/t LNG (mostly CO2 from compressor/turbine fuel). 2.9 g/MJ (~0.14 t/t) is DOE's illustrative low-emitting project. Appendix C URL: https://www.energy.gov/sites/default/files/2024-12/LNGUpdate_AppendixC_Dec2024.pdf")
row("US upstream GHG intensity of gas delivered to liquefaction terminal (NETL default)",
    5.6, 9.2, 14.6, "g CO2e per MJ exported, LHV, AR6 GWP100 (low = non-CH4 part only; high = DOE 1.4%-leak example)", DOE_S_T, DOE_S,
    "if an individual project's upstream emissions associated with natural gas delivered to the liquefaction terminal is different than the default value of 9.2 g CO2e/MJ.",
    "Summary Report Section VI.B, p.S-40", "yes",
    "Appendix C: 'the production through transmission (upstream) GHG intensity is 9.2 g CO2e/MJ exported on an IPCC AR6, 100-yr GWP, LHV basis and 15.7 g CO2e/MJ exported on an IPCC AR6, 20-yr GWP' and 'the project direct upstream emissions of 9.2 g CO2e/MJ (production through transmission) include 3.6 g CO2e/MJ associated with methane emissions. The methane emissions correspond to an upstream methane emission rate of 0.56%'. DERIVED: non-methane (approx CO2) upstream = 9.2-3.6 = 5.6 g/MJ LHV x ~0.985 GJ LHV/Mcf = ~5.5 kgCO2/Mcf (~10% of combustion CO2). FLAG: DOE/NETL methane rate 0.56% is ~4x below Alvarez 2.3% / Sherwin 2.43%; DOE's own example: at 1.4% leakage upstream rises to 14.6 g CO2e/MJ. Appendix C URL: https://www.energy.gov/sites/default/files/2024-12/LNGUpdate_AppendixC_Dec2024.pdf")

# ---------------- 5. Gas pipelines ----------------
FERC = "https://ferc.gov/sites/default/files/2020-05/02-05-18-FEIS.pdf"
FERC_T = "FERC (Feb 5 2018) Southeast Market Pipelines Project Final Supplemental EIS (Sabal Trail et al.), Docket CP14-554-002 et al."
EIA_P = "https://www.eia.gov/outlooks/aeo/IIF_pipeline/"
EIA_P_T = "EIA (Mar 30 2022) AEO2022 Issues in Focus: Exploration of the No Interstate Natural Gas Pipeline Builds case"
ICF = "https://www.api.org/-/media/Files/Energy-Economics/API-Studies/2026/ICF-API%20Permit%20Reform%20Study%20Report.pdf"
ICF_T = "ICF for American Petroleum Institute (May 2026) Permit Reform Study Report (2026-2035, Reference vs API Policy Case)"
row("Pipeline: net/gross downstream CO2e, Sabal Trail (SMP) 1.1 Bcf/d, FERC final SEIS",
    0.36, 0.58, 1.0, "fraction (net PTE / gross PTE; low = net / full burn)", FERC_T, FERC,
    "Total Downstream CO2 Emissions 14.5; Duke Energy Citrus County coal retirement change -3.87; FPL Martin County change due to switch from oil/natural gas to only natural gas -2.27; Net Increase in Downstream Permitted Emissions 8.36 || GHG Volume (million metric tons per year) Net PTE 8.36, Gross PTE 14.5, Full Burn 23.0 ... These projections account for the offset from coal retirement and oil to natural gas conversion. || Because the No Action Alternative could result in lesser, equal, or greater GHG emissions than the SMP Project, we cannot use the quantified downstream GHG emissions from the SMP Project to meaningfully compare the two.",
    "Final SEIS pp.4-6 (Tables 1-2) and p.~11 (alternatives)", "yes",
    "DERIVED ratios: 8.36/14.5 = 0.58; 8.36/23.0 = 0.36; high 1.0 = no displacement (FERC's own 'equal or greater' caveat). Offsets are only project-specific permitted retirements, not a market model. CH4 GWP=25 (AR4). Raw 20 MB PDF deleted after extraction.")
row("Pipeline: net change in total US energy CO2 per unit change in gas-combustion CO2 (EIA NEMS no-new-interstate-pipelines case, 2050)",
    "", 0.43, "", "fraction (dTotal CO2 / dGas-combustion CO2)", EIA_P_T, EIA_P,
    "In the No Interstate Pipeline Builds case, the amount of CO2 emitted from natural gas combustion in 2050 is 1,748 million metric tons (MMmt), about 80 MMmt (4.4%) lower compared with the Reference case. ... However, total CO2 emissions from all fuel sources are only 34 MMmt (0.7%) lower in the No Interstate Pipeline Builds case than in the Reference case in 2050. The relatively small difference in CO2 emissions from all fuel sources partly results from higher levels of coal-fired power generation, which is more carbon intensive than the natural gas-fired generation it displaces.",
    "Energy-related CO2 emissions section", "yes",
    "DERIVED 34/80 = 0.43: i.e., building the pipelines (7.4 Bcf/d interregional capacity by 2050) raises US CO2 by ~43% of the gross combustion CO2 of the added gas. Also: 'coal-fired generation is 46 BkWh higher ... in 2050' and 'fewer coal and nuclear power plants retire in this case'. Renewables +103 BkWh and nuclear +36 BkWh also fill in. AEO2022 (pre-IRA) policy baseline; excludes upstream methane. LNG exports -0.2 Tcf in the no-build case (foreign effect not counted).")
row("Pipeline+permitting package: power-sector CO2 change with ~22 Bcf/d extra pipeline capacity (ICF for API)",
    "", -33, "", "MtCO2/yr (avg 2026-2035, power sector only)", ICF_T, ICF,
    "Comprehensive permitting reform enables a stronger buildout of gas pipelines (assumed ~ 22 Bcf/d additional to the Reference Case) || In the API Policy Case, coal generation is being displaced by natural gas and additional renewables, leading to lower carbon emissions than the API Reference Case. In the Reference Case, CO2 emissions average around 1,373 million metric tons per year and under the Policy Case this is reduced to around 1,340 million metric tons per year, a decline of 2.4%. Cumulatively, over the 10-year period between 2026 and 2035, CO2 emissions declined under the Policy Case by 367 million metric tons || [Table, avg 2026-2035, Bcf/d] Residential & Commercial +0.1; Industrial +0.6; Power +1.1; Pipeline Fuel and L&P +0.2; LNG Export Feedgas +1.4; Total Demand +3.4",
    "Executive Summary pp.5-7; gas balance p.15; power CO2 p.45", "yes",
    "Industry-commissioned; scenarios 'chosen by API'. Policy case bundles pipelines WITH transmission/renewables permitting, so pipeline effect is not isolable. DERIVED: power-sector gas +1.1 Bcf/d = ~22 Mt/yr gross combustion vs -33 Mt/yr power CO2 -> net/gross ~ -1.5 (power only). Adding unreported non-power domestic gas (+0.9 Bcf/d = ~+18 Mt/yr) gives economy-wide ~ -15 Mt/yr on ~40 Mt/yr gross domestic combustion -> net/gross ~ -0.4. CO2 reported for power sector only; no upstream methane.")
row("Pipeline: SUGGESTED net-CO2 / gross-combustion-CO2 bracket for new US pipeline gas (synthesis)",
    -0.4, 0.4, 1.0, "fraction of gross combustion CO2 (US domestic, CO2 only)", "Synthesis of FERC 2018 SEIS, EIA AEO2022 IIF, ICF/API 2026, Prest 2022 (0.034/0.066 = 0.52 net-of-displacement for federal gas)", EIA_P,
    "(see source rows above)", "n/a", "no",
    "ANALYST JUDGMENT, not a published number. Central ~0.4 anchored on EIA NEMS (0.43) and close to FERC net/full-burn (0.36) and Prest's displaced-mix ratio 0.034/0.066 = 0.52. Low -0.4 = ICF/API economy-wide derived (confounded, industry-funded). High 1.0 = no displacement (gas meets new load or displaces clean). Net effect is strongly time- and baseline-dependent (coal fleet shrinking makes future coal displacement smaller). Add upstream methane separately.")

# ---------------- 1. Combustion CO2 ----------------
EIAC = "https://www.eia.gov/environment/emissions/co2_vol_mass.php"
EIAC_T = "EIA Carbon Dioxide Emissions Coefficients (release Sept 18 2024; based on EPA GHG Inventory 1990-2022)"
CFR = "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-98/subpart-C"
CFR_T = "40 CFR Part 98 Subpart C, Table C-1 (EPA GHGRP default CO2 emission factors and high heat values), eCFR as of 2026-10-01"
EPAEQ = "https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references"
EPAEQ_T = "EPA Greenhouse Gas Equivalencies Calculator - Calculations and References (last updated Aug 4 2026)"
row("Natural gas combustion CO2 (EIA current coefficient)", 52.91, 52.91, 53.06, "kg CO2/MMBtu (HHV)", EIAC_T, EIAC,
    "Natural Gas | 120.85 thousand cubic feet | 54.81 thousand cubic feet | 116.65 | 52.91 || Coefficients are based on data from 2022. EIA uses these coefficients for estimating 2023, and more recent, energy-related CO2 emissions.",
    "Table: Carbon Dioxide Emissions Coefficients by Fuel", "yes",
    "FLAG: the caller's 53.06 is the EPA GHGRP Table C-1 default (next row), not EIA's current 52.91 (0.3% lower). Either is defensible; name the convention. Per Mcf: 54.81 kg (EIA).")
row("Natural gas combustion CO2 (EPA GHGRP default) and default HHV", 53.06, 53.06, 53.06, "kg CO2/MMBtu; HHV 1.026 MMBtu/Mcf", CFR_T, CFR,
    "Natural gas mmBtu/scf kg CO2/mmBtu (Weighted U.S. Average) 1.026 x 10^-3 53.06",
    "Table C-1 to Subpart C of Part 98", "yes",
    "Default GHGRP HHV is 1.026 MMBtu/Mcf; EIA's coefficient table implies 54.81/52.91 = 1.036 MMBtu/Mcf (DERIVED). 53.06 x 1.036 = 54.97 kg/Mcf; 53.06 x 1.026 = 54.44 kg/Mcf. Gross per Bcf/d-yr: 20.06 MtCO2 (53.06, 1.036).")
row("Natural gas heat content (implied by EIA coefficients)", 1.026, 1.036, 1.036, "MMBtu per Mcf", EIAC_T, EIAC,
    "Natural Gas | 120.85 thousand cubic feet | 54.81 thousand cubic feet | 116.65 | 52.91",
    "Table: Carbon Dioxide Emissions Coefficients by Fuel", "yes",
    "DERIVED 54.81/52.91 = 1.036. Low = GHGRP default 1.026. EIA MER Table A4 not fetched.")
row("Crude oil combustion CO2 per barrel", 0.43, 0.43, 0.43, "tCO2/bbl", EPAEQ_T, EPAEQ,
    "The average heat content of crude oil is 5.80 mmbtu per barrel (EPA 2024). The average carbon coefficient of crude oil is 20.31 MMT C/QBtu (EPA 2024). The fraction oxidized is assumed to be 100 percent (IPCC 2006). ... 5.80 mmbtu/barrel x 20.31 kg C/mmbtu x 44 kg CO2/12 kg C x 1 metric ton/1,000 kg = 0.43 metric tons CO2/barrel",
    "Barrels of oil consumed", "yes",
    "Cross-check 40 CFR 98 Table C-1: 'Crude Oil 0.138 [mmBtu/gal] 74.54 [kg CO2/mmBtu]' -> 5.80 MMBtu/bbl x 74.54 = 0.432 t/bbl. Combustion only (no refining/upstream); treats all crude as combusted (non-energy uses ignored).")
for rank, hhv, ef, eia_t, eia_ef in [("Bituminous", 24.93, 93.28, "2,324.56", 93.24),
                                     ("Subbituminous (e.g., PRB)", 17.25, 97.17, "1,675.49", 97.13),
                                     ("Lignite", 14.21, 97.72, "1,396.37", 98.27)]:
    row(f"Coal combustion CO2 - {rank}", min(ef, eia_ef), ef, max(ef, eia_ef), "kg CO2/MMBtu", CFR_T, CFR,
        f"Table C-1: {rank.split(' ')[0]} {hhv} [mmBtu/short ton] {ef} [kg CO2/mmBtu] || EIA coefficients: {rank.split(' ')[0]} | {eia_t} short ton [kg] | {eia_ef} [kg/MMBtu]",
        "Table C-1 to Subpart C of Part 98; EIA coefficients table 'Coals by type'", "yes",
        f"Range spans GHGRP vs EIA values. Per short ton: {round(hhv*ef/1000,3)} tCO2 (GHGRP) vs {eia_t.replace(',','')} kg (EIA).")
    row(f"Coal heat content - {rank}", "", hhv, "", "MMBtu per short ton (HHV)", CFR_T, CFR,
        f"{rank.split(' ')[0]} {hhv} {ef}", "Table C-1 to Subpart C of Part 98", "yes",
        "GHGRP default; EIA coefficient table implies the same value (kg/st divided by kg/MMBtu). Actual PRB 8,400-8,800 Btu/lb = 16.8-17.6 MMBtu/st (Gerarden et al. use 8,800 Btu/lb); not separately verified from EIA coal data." if "Sub" in rank else "GHGRP default; EIA coefficient table implies the same value (kg/st divided by kg/MMBtu).")

# ---------------- 2. Capacity factors ----------------
EPM = "https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b"
EPM_T = "EIA Electric Power Monthly Table 6.07.B Capacity Factors for Utility Scale Generators Primarily Using Non-Fossil Fuels (accessed 2026-10-21; data through Jul 2026)"
cf = {  # tech: (2021,2022,2023,2024,2025)
 "Solar PV (utility-scale)": (24.4,24.4,23.2,23.2,24.4),
 "Solar thermal": (20.5,23.1,22.1,25.0,23.6),
 "Wind": (34.4,35.9,33.2,34.3,34.2),
 "Geothermal": (69.8,69.0,69.4,64.6,65.9),
 "Nuclear": (92.8,92.7,93.0,90.8,91.0),
 "Conventional hydroelectric": (36.0,36.3,35.0,34.6,35.3),
}
for tech,v in cf.items():
    row(f"Fleet capacity factor, {tech} (US, 2021-2025)", round(min(v)/100,3), round(v[4]/100,3), round(max(v)/100,3), "fraction (net gen / time-adjusted summer capacity)", EPM_T, EPM,
        f"Annual Data rows 2021|2022|2023|2024|2025 for {tech.split(' (')[0]}: " + " | ".join(f"{x}%" for x in v) + " || Values for 2024 and prior years are final. Values for 2025 and 2026 are preliminary.",
        "Table 6.07.B annual rows", "yes",
        "Central = 2025 (preliminary); low/high = min/max of 2021-2025. Solar PV CF on AC (summer capacity) basis; fast capacity growth biases fleet PV CF slightly low because time-adjusted capacity handles in-year additions. 'Hydroelectric' column = conventional hydro (pumped storage is separate)." if "PV" in tech else
        "Central = 2025 (preliminary); low/high = min/max of 2021-2025.")
ATBPV = "https://atb.nlr.gov/electricity/2024/utility-scale_pv"
ATBW = "https://atb.nlr.gov/electricity/2024/land-based_wind"
row("New utility-scale PV capacity factor, NREL/NLR ATB 2024 (resource classes 1-10, AC, 1-axis tracking, ILR 1.34)", 0.214, 0.283, 0.340, "fraction (AC)",
    "NREL (now NLR) 2024 Annual Technology Baseline: Utility-Scale PV", ATBPV,
    "Resource Class | GHI Bin (kWh/m2/day) | Mean Alternating Current(AC) Capacity Factor ... 1 | >5.75 | 34.0% ... 5 | 4.75-5 | 28.3% ... 10 | <3.75 | 21.4% || These AC capacity factors are for a one-axis tracking system with a DC-to-AC ratio of 1.34",
    "Resource Categorization table; Capacity Factor section", "yes",
    "Central = Class 5 (mid-range bin; ATB page does not name a single representative PV class on the text fetched - my choice). Values are first-year 2021 CF by class; ATB says lifetime-average CF includes 0.7%/yr degradation. Site moved from atb.nrel.gov (DNS fails) to atb.nlr.gov.")
row("New land-based wind net capacity factor, NREL/NLR ATB 2024 (2030 Moderate, Wind Speed Classes 4-10)", 0.276, 0.475, 0.475, "fraction",
    "NREL (now NLR) 2024 Annual Technology Baseline: Land-Based Wind", ATBW,
    "NCF (%) | 37 [2022 market average] | 47.5 (Wind Speed Class 4) | 36.3 (Wind Speed Class 8) | 35.1 (Wind Speed Class 9) | 27.6 (Wind Speed Class 10) || NCF values reported for Moderate Scenario ... Wind Speed Class 4 is indicative of a moderate-quality wind regime and is intended to be a representative wind resource for most wind projects installed in the United States.",
    "Performance Details by Representative Wind Turbine Technology (2030)", "yes",
    "Central = Class 4 (ATB's stated representative class) 2030 Moderate. 2022 market average turbine (Wiser & Bolinger) = 37%, close to EIA fleet ~34%. ATB Class 4 looks optimistic vs realized fleet; consider 0.37-0.42 for near-term builds (judgment).")

# ---------------- 6. Upstream methane & GWPs ----------------
row("US oil & gas supply-chain methane loss rate (Alvarez et al. 2018, 2015 national)", "", 0.023, "", "fraction of gross US gas production",
    "Alvarez et al. (2018) Assessment of methane emissions from the U.S. oil and gas supply chain. Science 361:186-188, doi:10.1126/science.aar7204 (PMC6223263)",
    "https://europepmc.org/article/PMC/PMC6223263",
    "When scaled up nationally, our facility-based estimate of 2015 supply chain emissions is 13 +/- 2 teragrams per year, equivalent to 2.3% of gross U.S. gas production. This value is ~60% higher than the U.S. Environmental Protection Agency inventory estimate",
    "Abstract (Europe PMC record)", "yes",
    "Only abstract fetched (via Europe PMC API). 13 +/- 2 Tg implies roughly 2.0-2.7% (DERIVED by scaling, not stated). This is the value behind Prest's 0.066 tCO2e/mcf.")
row("US oil & gas methane loss rate, six-region aerial average (Sherwin et al. 2024)", 0.0227, 0.0243, 0.0259, "fraction of covered gas production (95% CI)",
    "Sherwin et al. (2024) US oil and gas system emissions from nearly one million aerial site measurements. Nature 627:328-334, doi:10.1038/s41586-024-07117-5; Author Correction Nature 654:E16 (2026), doi:10.1038/s41586-026-10605-5",
    "https://www.nature.com/articles/s41586-024-07117-5",
    "Total estimated emissions range from 0.71% (95% confidence interval (CI) 0.61%, 0.81%) of covered natural gas production in a high-productivity, gas-rich region to 9.77% (95% CI 9.19%, 10.45%) in a rapidly expanding, oil-focused region. The six-region weighted average is 2.43% (95% CI 2.27%, 2.59%), or roughly three times the national government inventory estimate || [Correction] several errors were present and have been corrected in the HTML and PDF versions ... The main results, conclusions, and our interpretations of the data remain unchanged.",
    "Abstract (current corrected HTML); Author Correction", "yes",
    "FLAG: an Author Correction (2026) fixed unit-conversion and double-counting errors; the current (corrected) abstract reads 2.43%. The pre-correction (Mar 2024) headline value was not retrieved (Wayback rate-limited); citations predating the correction may carry a different figure - check before reusing any secondary-source number. Covers 6 regions = 29% of US gas production, not a national estimate; regional range 0.71-9.77%.")
AR6 = "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/"
AR6_T = "Forster et al. (2021) IPCC AR6 WG1 Chapter 7: The Earth's Energy Budget, Climate Feedbacks and Climate Sensitivity, Table 7.15"
row("GWP100 fossil methane (AR6)", 18.8, 29.8, 40.8, "kg CO2e per kg CH4", AR6_T, AR6,
    "CH4-fossil | 11.8 +/- 1.8 | 5.7 +/- 1.4 x10-4 | 82.5 +/- 25.8 | 29.8 +/- 11 | 10.0 +/- 3.8 | 13.2 +/- 6.1 | 7.5 +/- 2.9",
    "Table 7.15 (columns: lifetime, RE, GWP-20, GWP-100, GWP-500, GTP-50, GTP-100)", "yes",
    "Low/high = central +/- stated uncertainty (Table 7.15 uncertainties are 5-95% per chapter SM; not re-checked). Non-fossil CH4 GWP100 = 27.0 +/- 11. FERC 2018 SEIS used AR4 GWP 25.")
row("GWP20 fossil methane (AR6)", 56.7, 82.5, 108.3, "kg CO2e per kg CH4", AR6_T, AR6,
    "CH4-fossil | 11.8 +/- 1.8 | 5.7 +/- 1.4 x10-4 | 82.5 +/- 25.8 | 29.8 +/- 11",
    "Table 7.15", "yes", "Non-fossil CH4 GWP20 = 79.7 +/- 25.8.")

# ---------------- 7. Transmission enablement ----------------
ACP = "https://cleanpower.org/wp-content/uploads/gateway/2026/10/ACP-Clean-Energy-and-Environmental-Case-for-BAAJA.pdf"
ACP_T = "American Clean Power (Oct 2026, updated 10/09/26) The Clean Energy and Environmental Case for the Bipartisan American Affordability and Jobs Act (fact sheet)"
row("Clean capacity enabled per GW of new transmission transfer capacity (ACP assumption)", "", 1.4, "", "GW clean per GW transfer capacity", ACP_T, ACP,
    "ACP estimates that 1 GW of new transmission transfer capacity typically enables about 1.4 GW of clean energy development; identified transmission investments could enable roughly 200 GW of clean energy, with more as the grid expands.",
    "p.3, item 4 'Transmission Planning and Siting'", "yes",
    "Advocacy fact sheet; no method or citation given for 1.4. Same sheet: '350+ GW of projects could avoid roughly 290 million metric tons of CO2 annually' -> implied ~0.83 MtCO2/yr per GW (DERIVED). No lower published GW-per-GW-transfer ratio found in two searches (MISO LRTP Tranche 1: '53 GW' / '56 GW' of renewables enabled by $10.3-10.4B of lines, but no transfer-capacity denominator; snippets only, UNVERIFIED). GAP: treat 1.4 as an upper-end advocacy assumption.")
row("ACP fact sheet: annual CO2 avoided by 350+ GW enabled clean projects", "", 290, "", "MtCO2/yr", ACP_T, ACP,
    "Together, these 350+ GW of projects could avoid roughly 290 million metric tons of CO2 annually - about 6% of current U.S. carbon emissions. || C2ES and Greenline Insights find that transmission and interconnection reforms could reduce annual CO2 emissions by 71 million metric tons and enable nearly 100 GW of additional clean power by 2035 across regions representing 54% of U.S. electricity demand.",
    "p.4", "yes",
    "Implied ACP 0.83 Mt/GW-yr vs C2ES/Greenline 71/100 = 0.71 Mt/GW-yr (DERIVED; C2ES not opened, quoted via ACP = secondary).")
AEP = "https://WeCanFigureThisOut.org/ENERGY/Web_notes/Electricity/Generic_Power_Plant_and_Grid_Supporting_Files/American%20Electric%20Power%20Corp%20-%20Transmission%20Facts.pdf"
AEP_T = "American Electric Power, 'Transmission Facts' (c. 2008-2009; third-party mirror) citing Dunlop, Gutman & Marchenko (1979) IEEE Trans. PAS-98(2)"
for kv, lo, c, hi, q in [("765 kV single circuit", 2200, 2300, 2400, "765 kV Single Circuit 2200 - 2400 MW 550 Miles"),
                         ("500 kV single circuit", 900, 900, 900, "500 kV Single Circuit 900 MW 140 Miles"),
                         ("345 kV double circuit", 800, 800, 800, "345 kV Double Circuit 800 MW 110 Miles"),
                         ("345 kV single circuit", 400, 400, 400, "345 kV Single Circuit 400 MW 50 Miles")]:
    row(f"Line loadability ~1.0 SIL at 300 miles, {kv}", lo, c, hi, "MW per circuit (SIL-based, long line)", AEP_T, AEP,
        "Voltage Class | Loadability (@300 Miles) | 'Reach' (@1500 MW): " + q + " || a 765 kV line can reliably transmit 2200-2400 MW (i.e., 1.0 SIL) for distances up to 300 miles, whereas the similarly situated 500 kV and 345 kV lines with bundled conductors can deliver only about 900 MW and 400 MW, respectively. For short distances, these relationships can differ to some extent reflecting thermal capacities established primarily by the number/size of line conductors and station equipment ratings.",
        "Q11, p.3", "yes",
        "Mirror copy (not aep.com); document dates to ~2008 (cites AEP 2008 Fact Book). Short lines (<~50-100 mi) can carry 2-3x SIL up to thermal limits (St. Clair curve; not separately verified here).")
ND = "https://www.ndlegis.gov/sites/default/files/resource/committee-memorandum/surge-impedance-loading.pdf"
ND_T = "North Dakota Legislative Council staff (April 2000) Surge Impedance Loading memorandum, Electric Industry Competition Committee"
for kv, mw in [("230 kV", 132), ("115 kV", 33), ("69 kV", 12)]:
    row(f"Surge impedance loading, {kv}", "", mw, "", "MW per circuit (SIL)", ND_T, ND,
        f"[OCR text, table: Voltage | MW] 345 kV 298 | 230 kV 132 | 115 kV 33 | 69 kV 12",
        "single-page memo table", "yes",
        "Low-quality OCR scan from 2000; values match textbook SIL magnitudes (SIL ~ V^2/Zc with Zc ~ 300-400 ohm). Note it gives 345 kV = 298 MW vs AEP's 400 MW for bundled conductors. Thermal ratings are typically 2-4x SIL for short lines.")
row("Surge impedance loading, 138 kV and 161 kV (scaled)", 45, 48, 65, "MW per circuit (SIL)", ND_T, ND,
    "(DERIVED from 115 kV = 33 MW scaled by (V/115)^2: 138 kV -> 47.5 MW; 161 kV -> 64.7 MW)",
    "derived", "no",
    "NOT a published value; V^2 scaling from the ND 115 kV SIL. Low/central = 138 kV range, high = 161 kV. Replace with a textbook/utility table (e.g., Glover-Sarma-Overbye typical SIL table) if needed.")

# ---------------- 8. Marginal emission rates ----------------
CAMB = "https://data.nlr.gov/system/files/289/1744314776-Cambium24_Workbook.xlsx"
CAMB_T = "NREL Cambium 2024 Workbook (released March 2025), sheet 'Data - Annual', CO2 from Direct Combustion LRMER (kg per MWh of end-use demand), 18 GEA regions; docs NREL/TP-6A40-93005"
CAMBD = "https://docs.nlr.gov/docs/fy25osti/93005.pdf"
for yr, lo, med, mean, hi, note in [
    (2030, 0.041, 0.203, 0.218, 0.462, "Across all 8 scenarios, 2030 regional MEDIANS span 0.153-0.226 t/MWh; regional extremes 0.031-0.469."),
    (2035, 0.019, 0.100, 0.100, 0.195, "Across all 8 scenarios, 2035 regional medians span 0.080-0.141 t/MWh; regional extremes 0.018-0.265.")]:
    row(f"Cambium 2024 LRMER, CO2 combustion, Mid-case, {yr} (18 regions, unweighted)", lo, med, hi, "tCO2/MWh end-use (central = median of regions)", CAMB_T, CAMB,
        "[workbook block header] 'CO2 from Direct Combustion (kg per MWh of end-use demand)' || [Description tab] 'The long-run marginal emission rate is an estimate of the rate of emissions that would be either induced or avoided by a change in electric demand, taking into account how the change could influence both the operation as well as the structure of the grid' ... 'estimates produced with Cambium data should not be used as a basis for impact claims.' || [Docs p.12] 'All scenarios include representations of state, regional, and federal policies as of August 2024. These include representations of IRA's main electric sector provisions, updated CAA section 111 regulations based on the rules finalized in May 2024' ... 'in all scenarios IRA's tax credits for qualifying generation are represented as not phasing out.'",
        "Workbook 'Data - Annual' cols for Mid-case; Description and Guidance tab; docs Section 2 p.12", "yes",
        f"DERIVED summary stats from the workbook (computed here; mean={mean}). Unweighted across regions (no load weights in workbook). {note} Adding precombustion CO2 adds ~0.02 (2030) / ~0.012 (2035) t/MWh median. FLAG: assumes IRA credits never phase out and May-2024 CAA 111 rules, both since rolled back, so these LRMERs are likely biased LOW for current policy. End-use basis includes ~3-5% distribution losses (busbar slightly lower). Designed for load changes; workbook warns scalar LRMER is less accurate for wind/solar. Workbook (26.5 MB) deleted after extraction; regional extract at raw_A5/cambium24_lrmer_co2_regional_extract.csv.")
AV = "https://www.epa.gov/system/files/documents/2024-04/avert_emission_rates_04-11-24_0.xlsx"
AV_T = "EPA AVERT v4.3 Avoided Emission Rates 2017-2023 (posted April 11 2024), sheet '2023'"
row("AVERT 2023 avoided CO2 rate, onshore wind (national fossil-gen-weighted; regional range)", 0.429, 0.593, 0.765, "tCO2/MWh", AV_T, AV,
    "Avoided CO2 Rate | Onshore Wind 1308.3 | Offshore Wind 1227.9 | Utility PV 1347.1 | Distributed PV 1449.4 ... Portfolio EE 1454.7 [lb/MWh] || National rates presented here reflect a weighted average of the avoided emission rates of AVERT's 14 regions. Averages are weighted by the fraction of 2023 fossil generation in each region. || Regional onshore wind: California 946.5 ... Rocky Mountains 1685.9",
    "2023 sheet, National Weighted Averages and Regional Emission Rates", "yes",
    "lb->t x 0.000453592. Short-run marginal (existing fleet, displaced fossil only, 2023), so an UPPER bracket for long-lived projects. Regional min = California 946.5, max = Rocky Mountains 1685.9 lb/MWh.")
row("AVERT 2023 avoided CO2 rate, utility-scale PV (national; regional range)", 0.431, 0.611, 0.763, "tCO2/MWh", AV_T, AV,
    "Avoided CO2 Rate | ... Utility PV 1347.1 [lb/MWh] || Regional Utility PV: California 949.4 ... Rocky Mountains 1681.6",
    "2023 sheet", "yes",
    "Same caveats as wind row. AVERT page lists 2023 as latest data year (page last updated Mar 3 2026).")
row("SYNTHESIS: bracket check for assumed 0.35-0.50 tCO2/MWh displaced-generation rate", 0.10, 0.35, 0.61, "tCO2/MWh", "Cambium 2024 LRMER (2030s) vs AVERT 2023 SRMER", CAMB,
    "(see rows above)", "n/a", "no",
    "ANALYST NOTE: the assumed 0.35-0.50 sits ABOVE Cambium 2024 Mid-case LRMER medians (0.20 in 2030, 0.10 in 2035) and BELOW AVERT 2023 short-run national rates (0.59-0.61). Cambium's low values reflect IRA-era policy assumptions that no longer hold, so the truth for post-2025 policy is probably between. 0.35-0.50 is defensible as a 2025-2035 blend but is not 'conservative' relative to Cambium; run 0.20 as a sensitivity.")

if __name__ == "__main__":
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in R:
            w.writerow(r)
    print(len(R), "rows ->", OUT)
