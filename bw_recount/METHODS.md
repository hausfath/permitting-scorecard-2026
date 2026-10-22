# Recount methods (2026-10-21)

Converted from the subagent's methods draft. **Factor values in the text block below are the first-pass values.** For the factors revised after review, see `SUMMARY.md` ('What changed') and `factors.py`, which is authoritative: NET_PIPE, NET_COAL, NET_EXPORT_PORT, REAL_PROG, per-project production lives, and Beta litigation rates. Factors live in `factors.py`; per-project sizes and sources live in `sizes_spec.py` and `sizing_out/`.

```text
B&W EMISSIONS-WEIGHTED RECOUNT: METHODS (draft, 2026-10-21; to become METHODS.md)
=====================================================================================

PIPELINE (all scripts in bw_recount/; run in this order)
1. extract_ceq.py
   - Input: CEQ Dec 2018 EIS Timelines workbook (Wayback id_ copy of
     https://ceq.doe.gov/docs/nepa-practice/CEQ_EIS_Timelines.xlsx).
   - Output: ceq_2018_eis.csv (1,161 ROD rows + 108 No-ROD rows).
   - Duration field: NOI->ROD years, or NOI->FEIS when there is no ROD.
2. Gate scripts
   - candidates.py: title-based candidate pools.
   - reconstruct_bw.py: ILP closest reconstruction.
   - fp_search.py, fp_enumerate.py, fp_programmatic.py: duration fingerprint.
   - gate_counts.py: gate table.
3. universe.py
   - Output: universe.csv, the hand-reviewed primary set.
   - 237 EISs = 229 title-based + Four Corners, Groton, Point Thomson-as-fossil, Fort Bliss, Schofield, Maricopa Sun,
     the CCSM eagle-take EIS, NECPL and Moab MLP (the last two were missed by candidates.py).
   - Programmatic EISs are split into four groups:
     - Leasing-Fossil (fossil).
     - Programmatic-Clean (clean).
     - Programmatic-FossilOther (G&G, incidental take, regulations; Other).
     - Programmatic-Other (Other).
4. sizes_spec.py
   - One hand-curated size per EIS, with method code, status, new/existing flag, imputation flag, and a ref to the
     source row.
5. build_projects.py (run with python3.13 -I)
   - Joins the spec to the sizing CSVs (scratchpad sizing/out/A*.csv) for source URL, quote and confidence.
   - Output: projects_sized.csv.
6. recount.py
   - Per-project emissions, 2x2x2 cells, Monte Carlo (10,000 draws), sensitivities.
   - Outputs: projects.csv, results_cells.csv, results_concentration.csv, results_imputed_share.csv.
7. bw_check.py
   - B&W counts x pool means, and fingerprint-feasible min/max via ILP.
   - Output: results_bw_check.csv.

SIZING SOURCES
Sizes were gathered by eight sizing subagents. Their CSVs, with quotes and URLs, are in the scratchpad.
- Overridden with EIA databases (high confidence):
  - Pipeline capacities: EIA Natural Gas Pipeline Projects, Aug 2026.
  - LNG baseload MTPA: EIA US Liquefaction Capacity, Jun 2025.
- Other primary sources:
  - Coal leases: BLM ROD and Federal Register sale notices (high).
  - BOEM Program production: PFP Table 6-2; 2016 retrospective Table 6-4 (high).
  - Onshore fields: BLM FEIS/ROD (high).
- Clean projects: mostly medium (DOI/BLM releases, Wikipedia, trade press). Nuclear COLs are medium/low.
  Small transmission lines are rated from the kV in the title (imputed).
- Confidence flags: high = EIS/ROD/docket/agency or EIA data; medium = reputable secondary; low = inferred or
  search-snippet only.
- Imputations (flagged size_imputed=True; default range 0.5-1.5x unless stated):
  - PSEG ESP: 2,234 MW, AP1000 pair.
  - RDEP: 1,665 MW.
  - kV-based line ratings: AEP loadability 500 kV 900 MW, 345 kV 400 MW; 230 kV SIL 132 MW, 115 kV 33 MW;
    161/138 kV by V^2 scaling (unverified).
  - Gas EUR of 1.0 Bcf per well for WRFO, West Tavaputs, Bull Mountain and the WRNF leasing EISs (range of GNB 0.96-1.28 and Gasco
    1.05 Bcf/well).
  - Dixie NF oil: per-well rate from the Uinta NF FSEIS.

EMISSION METHODS (MtCO2/yr; CO2e where methane or lifecycle values are used)
Clean generation:
- MW x CF(tech) x 8760 x MER.
- Same value in all four bases. Clean "gross" = "net", since MER is already a displaced rate.
- Hydro relicensing: 0 (PLAN). Only incremental MW counts.
- Pumped storage: 0.
- Existing wind farms getting HCP/ITP permits (Fowler Ridge, Beech Ridge): 0 in central.
Transmission:
- Renewable-enabling: rating x ENABLE x TX_CF x 8760 x MER.
- Canadian hydro import lines (CHPE, GNTL, Northern Pass, NECPL): rating x utilization x additionality share x 8760 x
  MER.
- Reliability/load-serving lines and "overlap" lines: ENABLE_RELIAB (0 central). Overlap means lines that mainly
  deliver generation already in this universe, e.g. West of Devers and Eldorado-Ivanpah.
- Gen-ties to external projects (ESJ wind 155 MW, Echanis 104 MW): project MW x CF_WIND x MER.
Clean programmatics:
- RFD MW x CF_PV x MER.
- "Potential" or "if fully built out" figures are halved (ASSUMED 50% realization) because they are upper bounds. This
  applies to the Solar PEIS ("as much as 23,700 MW", DOI release, fetched), West Chocolate (3,330 MW) and RDEP.
- DRECP's 20,000 MW planning assumption is used minus Palen PV (500 MW, already in the universe).
- Fossil RFDs and BOEM anticipated production are not halved, because they are expected-value projections, not
  ceilings. The projects-only sensitivity shows the sign does not depend on this.
Gas pipelines:
- Gross = capacity x 20.06 x U.
- Net = capacity x 20.06 x NET_PIPE, where NET_PIPE is net US CO2 per unit of full-burn capacity CO2.
- Sierrita (Mexico export) counts globally only.
- The Jordan Cove feed pipeline is embedded in the LNG terminal.
Keystone XL:
- Global gross 147-168 and global net 1.3-27.4 MtCO2e/yr, from the State Department FSEIS via CRS R43415 (fetched).
- US gross = 0.83 Mb/d x 0.43 x US_SHARE_OIL.
- US net = global net x USSHARE_OGNET.
UNEV products pipeline:
- Gross = bbl/d x 0.43 x U.
- Net = gross x NET_MIDSTREAM_OIL (ASSUMED 0.10, range 0-0.3).
LNG export:
- t = MTPA x U_LNG; energy = t x 50 GJ/t.
- US gross = liquefaction (LIQ_GMJ x energy) + US upstream CO2 (UPSTREAM_KG_MCF x feed Mcf).
- US net = t x 0.1335 Bcf/d per MTPA x LNG_US_NET_PER_BCFD (DOE 2024, NEMS).
- Global gross = 76 g CO2e/MJ x energy (DOE attributional).
- Global net = LNG_CONSEQ_GMJ x energy (DOE 2024 consequential, Table ES-2).
Regasification/import:
- Gross = send-out x 20.06 x U.
- Aguirre net = gross x (53.06 - 75.10)/53.06, i.e. displaced No. 6 fuel oil (eCFR Table C-1, fetched). This is
  negative.
- Port Ambrose and Downeast (FEIS analysed import): net = send-out x 20.06 x NET_PIPE.
Coal leases:
- Cumulative = Mst x tCO2/st by rank (Table C-1: subbituminous 1.676, bituminous 2.326, lignite 1.389).
- Annual = cumulative / 30.
- US net and global net = annual x NET_COAL.
- Wright Area central = the four ROD-approved tracts (1,813 Mst). Low = sold (1,346). High = all six as applied
  (2,435). Built = sold.
Fossil plants:
- Gross = EIS annual CO2 scaled by CF, or MW x CF x EF x (1 - capture).
- Net = gross - MW x CF x MER (the generation it displaces).
- Groton: the EIS incremental 0.132 Mt/yr.
Oil and gas fields and leasing (cumulative oil MMbbl, gas Bcf; /30):
- Global gross = oil x 0.43 + gas x 0.05496 Mt/Bcf.
- Global net = oil x NET_OIL + gas x NET_OIL x DISP_GAS.
- US net = oil x NET_OIL x USSHARE_OGNET + gas x NET_OIL x DISP_GAS x USSHARE_GASNET.
- Program level vs sale level: each OCS lease-sale EIS is tiered to a Program in the universe, so production is
  counted once, at Program level. Sale 216/222 implements the 2007-12 Program, which is not in the universe, so it is
  counted at sale level. Sale-level sums reproduce the Program totals within about 1%.
Other bucket:
- Waste, bio, CCS, uranium, other energy, and fossil-related programmatics with no production decision.
- Tabulated, not netted.

SHARED FACTORS (triangular low / central / high; drawn ONCE per Monte Carlo draw)
Where a value is defensible either way, the central is the one less favorable to "lowers on net".
Clean generation:
- MER, 0.35 / 0.40 / 0.50 t/MWh. Scorecard range (infographic.py MER), with the central toward the low end.
- Context for MER:
  - Cambium 2024 mid-case LRMER: 2030 median 0.20 [0.04-0.46]; 2035 0.10.
  - AVERT 2023 short-run: about 0.6.
  - Cambium assumes IRA credits and the 2024 CAA 111 rules persist, so it is likely biased low now. It is run as a
    sensitivity (0.10-0.30).
- Capacity factors, EIA EPM Table 6.07.B (2025 prelim; 2021-25 range) and NREL ATB 2024:
  - PV 0.214 / 0.244 / 0.283
  - CSP 0.205 / 0.236 / 0.25
  - Wind 0.30 / 0.342 / 0.40
  - Geothermal 0.60 / 0.659 / 0.75
  - Nuclear 0.88 / 0.91 / 0.93
  - Hydro 0.30 / 0.353 / 0.40
Transmission:
- ENABLE_RENEW 0.25 / 0.50 / 1.40. ASSUMED low central; 1.4 is ACP's Oct 2026 fact-sheet assumption (no stated
  method). No published lower ratio was found.
- TX_CF 0.25 / 0.30 / 0.35 (scorecard ws_cf).
- Hydro-import utilization 0.5 / 0.7 / 0.85 and additionality 0.25 / 0.5 / 1.0 (ASSUMED).
Fossil utilization (ASSUMED):
- U_PIPE 0.6 / 0.8 / 0.95
- U_LNG 0.75 / 0.9 / 1.0
- CF gas plant 0.4 / 0.6 / 0.75
- CF coal plant 0.5 / 0.65 / 0.8
NET_PIPE: -0.075 / 0.36 / 0.90 (per unit full-burn capacity CO2)
- Central 0.36: FERC Sabal Trail final SEIS, net 8.36 / full burn 23.0 Mt/yr. Offsets counted there are only the
  permitted Crystal River coal retirement and the Martin oil switch.
- Sensitivity 0.23: EIA AEO2022 No Interstate Pipeline Builds case: total CO2 -34 Mt in 2050 with 7.4 Bcf/d less
  interregional capacity; 34 / (7.4 x 20.06). Fetched and quoted.
- Low -0.075: ICF for API 2026, power-sector -33 Mt/yr with about 22 Bcf/d more capacity. Industry-funded, bundled
  with other permitting changes, power sector only.
- High 0.90: no displacement at high utilization.
Oil and gas leakage and shares:
- NET_OIL 0.21 / 0.43 / 0.64: 1 - leakage, Prest RFF IB 24-09 (2024), 57% [36-79%], fetched. Prest 2022 JAERE
  (leakage 72% base) is run as a sensitivity.
- DISP_GAS 0.52 / 1.0 / 1.0: Prest's displaced-mix gas factor 0.034 / 0.066. Central gives no credit, as Prest's
  central does.
- USSHARE_OGNET 0.10 / 0.17 / 0.30: RFF IB 24-09 Table 1. US consumption share of the global increase, about
  0.2 of 1.2 Gt.
- USSHARE_GASNET 0.17 / 0.80 / 0.95: ASSUMED. Induced gas use is mostly North American; Prest does not separate gas.
- US_SHARE_OIL 0.7 / 0.85 / 1.0, US_SHARE_GAS 0.85 / 0.95 / 1.0, US_SHARE_COAL 0.9 / 0.97 / 1.0 (ASSUMED).
NET_COAL: 0.11 / 0.50 / 0.50
- Gerarden, Reeder & Stock, NBER w22214. 0.50 is the no-binding-cap power-sector case; 0.11 is under a binding
  downstream cap.
- This is a US power-sector model, so it is treated as US-territorial.
- Not checked against the AEJ:EP 2020 published version.
LNG (DOE 2024 LNG Export Study, fetched):
- Consequential global intensity 1.2 / 6.3 / 12.6 g CO2e/MJ; attributional 76.
- US domestic CO2 0.71 / 1.23 / 1.41 Mt/yr per Bcf/d exported (NEMS reference / low-supply / high-supply; central is
  the less favorable variant).
- Liquefaction 2.9 / 5.3 / 6.5 g/MJ.
- Upstream non-methane CO2 3.5 / 5.5 / 8.0 kg/Mcf.
- The DOE study uses a 0.56% methane rate, about 4x below Alvarez/Sherwin.
Methane sensitivity:
- 2.3% of throughput (Alvarez 2018; Sherwin 2024 corrected 2.43%), GWP100 29.8 (AR6 fossil CH4).
- Applied to pipelines, LNG feed and field gas. Counted US-territorial; the net for fields scales by NET_OIL.
Combustion constants:
- 53.06 kg/MMBtu x 1.036 MMBtu/Mcf = 20.06 Mt per Bcf/d (scorecard convention; EIA's current coefficient 52.91 is
  0.3% lower).
- 0.43 tCO2/bbl (EPA equivalencies).
Horizon: 30 yr for depletables (generator-life convention); 20 yr as a sensitivity.

AGGREGATION
- (a) Exposure-weighted sums.
- (b) Litigation-weighted: each project x its B&W Table 1 subsector rate.
  - Leasing and programmatic EISs take the Energy-Programmatic rate, 20%.
  - Nuclear's 0% comes from n = 2 in B&W and is applied to 12 COLs.
- Cells: transmission in/out x US/global x gross/net.
- Monte Carlo:
  - 10,000 draws, seed 20261021.
  - Shared factors are drawn once per draw.
  - Per-project size ranges (lo/hi) and the KXL factors are drawn per project.
  - Oil and gas components of one EIS share a quantile.
- Central deterministic = all factors at central. The MC median differs because the triangulars are skewed.
- Concentration: top-10 share per side.
- Imputed and low-confidence shares are computed on central emissions.

CAVEATS
- Exposure composition only; this is not the bill's effect (PLAN scope note).
- Supply-chain overlap: pipelines, gas fields, LNG terminals and leasing can carry the same molecules. Counting per
  EIS is what the PLAN asks for, so fossil "exposure" sums are not additive physical emissions.
- Most exposed clean capacity was never built: nuclear COLs, CSP. Most exposed fossil capacity was built: pipelines,
  Wright Area leases. See the built-only sensitivity.
- The clean side is 57% nuclear COLs. Litigation weighting zeroes them (B&W 0% on n = 2).
- H = 30 understates nuclear's 60-80 yr cumulative relative to depletable leases. This is less favorable to clean, by
  design.
- Kemper is counted at its EIS IGCC-with-capture emissions, although it runs as NGCC.
- Programmatic asymmetry: clean potentials are halved, fossil RFDs are not (see methods above).
- Unquantified fossil: NPR-A IAP (Willow lies in these lands), the oil shale PEIS, Moab MLP, Shadura, and the USACE TX
  regional coal REIS. Leaving them out biases toward clean.
- Unquantified clean: the Upper Great Plains Wind PEIS, the Hawaii PEIS and Humboldt-Toiyabe geothermal leasing.
- Status data for several clean projects are "unknown". They are treated as not built in the built-only case.
- The B&W check uses central per-project emissions. Its min/max are ILP extremes, not a probability interval.
- Erickson & Lazarus (2018) is UNVERIFIED (paywalled). Not used numerically.

```
