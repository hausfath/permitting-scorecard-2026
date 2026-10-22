"""Shared emission / substitution factors for the B&W emissions-weighted recount.
Each SHARED factor: (low, central, high). The original PLAN set CENTRAL at the value less favorable to 'NEPA provisions
lower emissions on net'. After the 2026-10-21 reviews (reviews/), centrals were revised to the best-supported value,
because the published claim now runs the other way; direction-of-favor bounds are reported as scenarios instead.
Monte Carlo draws each shared factor ONCE per draw from triangular(low, central, high).
Sources, quotes and derivations: methods_draft.txt (Factors) and sizing_out/A5_factors.csv.
"""
# ---- fixed physical constants (EPA 40 CFR 98 Table C-1 / EIA) ----
MT_PER_BCFD = 1e6 * 53.06 * 1.036 * 365 / 1e9     # 20.06 MtCO2/yr per Bcf/d (scorecard convention: EPA 53.06 kg/MMBtu, EIA 1.036 MMBtu/Mcf)
T_CO2_PER_BBL = 0.43                                # EPA GHG equivalencies (5.80 MMBtu/bbl, 20.31 MMT C/QBtu)
T_CO2_PER_ST = {'subbituminous': 17.25 * 97.17 / 1000, 'bituminous': 24.93 * 93.28 / 1000, 'lignite': 14.21 * 97.72 / 1000}  # Table C-1
KG_PER_MMBTU_GAS, KG_PER_MMBTU_RESID = 53.06, 75.10  # Table C-1 natural gas, residual fuel oil No. 6
GJ_PER_T_LNG = 50.0                                  # ~LHV energy of LNG, matches DOE 2024 g/MJ basis (approx.)
BCFD_PER_MTPA = 0.1335                               # LNG product: 1 MTPA ~ 0.1335 Bcf/d (EIA conversion used in liquefaction workbook ~0.13)
MCF_FEED_PER_T_LNG = 48.7 * 1.10                     # feed gas incl ~10% liquefaction fuel/shrink
H_YEARS = 30                                         # horizon for annualizing cumulative production (generator-life convention)

SHARED = {
    # clean generation
    'MER':            (0.35, 0.40, 0.50),     # tCO2/MWh displaced (scorecard 0.35-0.50; central toward low end)
    'CF_PV':          (0.214, 0.244, 0.283),  # EIA EPM 6.07.B 2025 fleet 0.244; ATB 2024 low/central range
    'CF_CSP':         (0.205, 0.236, 0.25),   # EIA solar thermal 2021-25
    'CF_WIND':        (0.30, 0.342, 0.40),    # EIA 2025 fleet 0.342; ATB/2022 market 0.37
    'CF_GEO':         (0.60, 0.659, 0.75),    # EIA 2021-25 0.646-0.698
    'CF_NUC':         (0.88, 0.91, 0.93),     # EIA 0.908-0.93
    'CF_HYDRO':       (0.30, 0.353, 0.40),    # EIA 0.346-0.363
    # transmission
    'TX_ENABLE_RENEW': (0.25, 0.50, 1.40),    # GW clean enabled per GW rated transfer (ASSUMED low central; ACP 1.4 high)
    'TX_ENABLE_RELIAB': (0.00, 0.00, 0.30),   # reliability/load-serving and overlap lines
    'TX_CF':          (0.25, 0.30, 0.35),     # blended wind/solar CF of enabled capacity (scorecard ws_cf)
    'TX_CF_HYDROIMPORT': (0.50, 0.70, 0.85),  # line utilization of Canadian-hydro import lines (ASSUMED)
    'HYDROIMPORT_ADDL': (0.25, 0.50, 1.00),   # share of imported hydro that is incremental (not diverted from other markets) (ASSUMED)
    # fossil utilization
    'U_PIPE':         (0.60, 0.80, 0.95),     # ASSUMED
    'U_LNG':          (0.75, 0.90, 1.00),     # ASSUMED
    'CF_GASPLANT':    (0.40, 0.60, 0.75),     # ASSUMED (NGCC)
    'CF_COALPLANT':   (0.50, 0.65, 0.80),     # ASSUMED
    # substitution / net factors
    # net US CO2 per unit of FULL-BURN capacity CO2 (capacity x 20.06 Mt per Bcf/d), i.e. utilization folded in:
    #   EIA AEO2022 no-new-interstate-pipelines case: total CO2 -34 Mt with ~7.4 Bcf/d less capacity -> 34/(7.4*20.06) = 0.23
    #     (CENTRAL since 2026-10-21 review: the only systemic market estimate; 2050 snapshot, so plausibly high for 2017-30 lines)
    #   FERC Sabal Trail final SEIS: net 8.36 / full burn 23.0 = 0.36 (HIGH; full burn minus two named offsets, not a market estimate)
    #   ICF for API 2026: power-sector CO2 -33 Mt/yr with ~22 Bcf/d more capacity -> -33/(22*20.06) = -0.075 (LOW; power sector only)
    #   (former high of 0.90, no displacement, had no study behind it and was dropped)
    'NET_PIPE':       (-0.075, 0.23, 0.36),
    'NET_OIL':        (0.21, 0.43, 0.64),     # 1 - leakage, Prest (RFF IB 24-09, 2024) 57% [36-79%]
    'DISP_GAS':       (0.52, 1.00, 1.00),     # gas net-of-fuel-displacement factor: Prest 0.034/0.066 = 0.52 low; central no credit (Prest central uses 0.066)
    'USSHARE_OGNET':  (0.10, 0.17, 0.30),     # US territorial share of global net from added federal oil & gas (RFF IB 24-09 Table 1)
    'USSHARE_GASNET': (0.17, 0.80, 0.95),     # gas-weighted: induced gas use mostly North American (ASSUMED; low = Prest combined 17%)
    'US_SHARE_OIL':   (0.70, 0.85, 1.00),     # share of gross oil combustion occurring in US (ASSUMED)
    'US_SHARE_GAS':   (0.85, 0.95, 1.00),     # (ASSUMED)
    'NET_COAL':       (0.10, 0.25, 0.50),     # GRS (NBER w22214) 0.50 is a basin-wide price shock = upper bound for a single PRB tract (adjacent reserves substitute first); central 0.25 reviewer judgment (2026-10-21); 0.11 binding cap
    'US_SHARE_COAL':  (0.90, 0.97, 1.00),     # (ASSUMED; PRB coal almost all domestic)
    'NET_MIDSTREAM_OIL': (0.0, 0.10, 0.30),   # products pipeline serving an existing market (ASSUMED)
    'NET_EXPORT_PORT': (0.0, 0.0, 0.03),      # crude export ports: no production created; only netback channel ~1% of throughput (review 2026-10-21)
    # programmatic realization: ONE shared factor applied to every programmatic EIS, clean (RFD MW) and fossil (anticipated
    # production) alike. ASSUMED symmetric; BLM had permitted ~29 GW of all clean types by Jul 2024, and BOEM anticipated
    # production overstates outcomes (Arctic / Cook Inlet sales yielded little). Replaces the clean-only 50% haircut.
    'REAL_PROG':      (0.25, 0.50, 1.00),
    # LNG (DOE 2024 LNG Export Study)
    'LNG_CONSEQ_GMJ': (1.2, 6.3, 12.6),       # consequential global GHG, g CO2e/MJ exported (Table ES-2)
    'LNG_ATTR_GMJ':   (76.0, 76.0, 76.0),     # attributional life-cycle, g CO2e/MJ
    'LNG_US_NET_PER_BCFD': (0.71, 1.23, 1.41),# US domestic energy CO2 change, Mt/yr per Bcf/d exported (NEMS; ref / low-supply / high-supply)
    'LIQ_GMJ':        (2.9, 5.3, 6.5),        # liquefaction g CO2e/MJ (NETL avg 5.3; DOE low-emitting example 2.9)
    'UPSTREAM_KG_MCF': (3.5, 5.5, 8.0),       # US upstream non-methane CO2, kg/Mcf (DOE App. C derived 5.5)
    'KXL_NET':        (1.3, 27.4, 27.4),      # MtCO2e/yr incremental lifecycle vs reference crudes (State FSEIS via CRS) -- per-project factor
}
# methane sensitivity (not in central)
LEAK_RATE = 0.023            # Alvarez et al. 2018 (2.3% of gross US production)
GWP100_CH4 = 29.8            # IPCC AR6 WG1 Table 7.15, fossil methane
T_CH4_PER_MCF = 0.0192       # ~19.2 kg CH4 per Mcf of methane at standard conditions

LIT_RATE = {  # B&W Table 1 litigation rates applied to the universe
    'Solar': .64, 'Wind': .38, 'Transmission': .31, 'Hydro': 0.0, 'Geothermal': .33, 'Nuclear': 0.0, 'PumpStorage': 1.0,
    'Pipeline': .56, 'Liquefaction': .29, 'Regasification': 0.0, 'GasPlant': 0.0, 'CoalPlant': 0.0, 'Mine-Coal': .50, 'Mine-Gas': .50,
    'Leasing-Fossil': .20, 'Programmatic-Clean': .20, 'Programmatic-FossilOther': .20, 'Programmatic-Other': .20,
    'Waste': .25, 'BioPlant': .50, 'BioRefinery': 0.0, 'CarbonCapture': 0.0, 'Mine-Other': .25, 'Other-Energy': 0.0}

# B&W Table 1 counts (n) used to draw litigation rates from Jeffreys Beta(k+0.5, n-k+0.5), shared per draw (review 2026-10-21).
LIT_N = {'Solar': 22, 'Wind': 13, 'Transmission': 42, 'Hydro': 14, 'Geothermal': 3, 'Nuclear': 2, 'PumpStorage': 1,
    'Pipeline': 18, 'Liquefaction': 7, 'Regasification': 1, 'GasPlant': 2, 'CoalPlant': 2, 'Mine-Coal': 4, 'Mine-Gas': 6,
    'Leasing-Fossil': 15, 'Programmatic-Clean': 15, 'Programmatic-FossilOther': 15, 'Programmatic-Other': 15,
    'Waste': 8, 'BioPlant': 2, 'BioRefinery': 1, 'CarbonCapture': 2, 'Mine-Other': 4, 'Other-Energy': 2}
