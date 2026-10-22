# Phase 2 methods

Factor revisions after review (2026-10-21) are listed in `../SUMMARY.md` ('What changed'); `../factors.py` and `sizes_spec2.py` are authoritative. Mt brought forward now gives depletables 0 months, imputes unmatched projects at CGEP type means, and drops the litigated-uplift sensitivity.

```text
PHASE 2 METHODS (draft, 2026-10-21; to become phase2/METHODS2.md)
=================================================================

PIPELINE (run from bw_recount/)
1. phase2/extract_ceq2024.py
   - Run with python3.13 -I.
   - Input: CEQ EIS Timelines 2010-2024 workbook (Jan 13 2025; sheet "All FEISs", 1,903 rows):
     https://nepa.gov/sites/default/files/documents/CEQ_EIS_Timeline_Data_2024_1_13_2025.xlsx
   - Output: phase2/ceq_2024_eis.csv
2. phase2/reconcile.py
   - Matches the 1,269 rows of the 2018 workbook to the 2024 workbook, in this order:
     a. exact normalized title;
     b. same FEIS date + title similarity >= 0.6;
     c. similarity >= 0.85;
     d. two hand matches.
   - Output: phase2/reconcile_2018_to_2024.csv, with a re-dated flag.
3. phase2/new_universe.py
   - Hand classification of the 2024-workbook rows with no 2018 match: 253 keyword or energy-agency candidates plus a
     scan of the rest.
   - Output: phase2/universe_new.csv (155 EISs).
   - Same subsector scheme as Phase 1, plus OffshoreWind.
   - General RMP revisions are excluded, as in Phase 1. Specific oil and gas leasing RMPAs are included.
   - Nuclear licence renewals, HCP/ITP for existing wind farms, hydro relicensing and CRSO are coded as continuations.
   - dup_pooled marks a later EIS for a project already in the set (Jordan Cove 2019, SunZia 2023, Clinch River
     technology park, Plaquemines second listing). It is sized in its own era and zeroed in the pooled set.
4. phase2/sizes_spec2.py + phase2/build_projects2.py
   - Output: phase2/projects_sized2.csv.
   - Sizing inputs:
     - Subagent CSVs in phase2/sizing_out/ (P2F fossil, P2C clean). Same COMMON_RULES and confidence flags as
       Phase 1.
     - EIA Natural Gas Pipeline Projects (Aug 2026) and EIA US Liquefaction Capacity (Jun 2025): high confidence.
     - Individually cited URLs.
5. phase2/cgep_derive.py and phase2/cgep_join.py
   - Run with python3.13 -I on the decoded CGEP tables, which stay in the scratchpad.
   - Outputs:
     - phase2/cgep_type_medians.csv
     - phase2/cgep_archetype_totals.csv
     - phase2/cgep_join.csv: minimal table of ceq_id, CGEP project, technology, months_saved_total,
       months_saved_low, attribution. 115 of 144 replays join on ceq_title. The unjoined 29 are 25 geothermal
       exploration reviews (not EISs), Crimson Solar (missing from the CEQ workbook), and three scheduled 2026-28
       projects.
6. phase2/recount2.py
   - Reuses ../recount.py em() and factors.py unchanged.
   - Adds:
     - OffshoreWind CF_OW 0.40 / 0.40 / 0.45 (scorecard OW_CF; central at the less favorable end).
     - OVERLAP: LNG-feed or plant-feed laterals, zero.
     - PIPEOIL_EXPORT: crude-export ports. Global gross = bbl/d x 0.43 x U_PIPE; net = gross x NET_MIDSTREAM_OIL;
       US = 0.
     - A drop_fossil_continuation check for every fossil method.
   - One Monte Carlo (10,000 draws; shared factors once per draw) over all 2010-24 projects.
   - Aggregation by era (FEIS year): 2010-16, 2017-20, 2021-24, Phase 1 2010-18 set (unchanged), and 2010-24
     pooled (dup_pooled zeroed).
   - Outputs: results2_cells.csv, results2_mtyears.csv, results2_cgep_coverage.csv, projects2.csv.

KEY SIZING CHOICES (new items)
LNG:
- EIA baseload MTPA, with FERC totals for approved but unbuilt phases.
- Built = phases under construction or operating:
  - Driftwood 16.56 of 27.6
  - Rio Grande 16.2 of 27
  - Plaquemines 19.8
  - Calcasieu Pass 10
  - Port Arthur Phase 1 12
  - CP2 20 (FIDs 2025-26, medium)
  - Commonwealth 9.3 (FID May 2026, medium)
Pipelines:
- EIA additional capacity (Bcf/d). MIDSHIP is 1.44 (medium, secondary).
- Five LNG-feed laterals and two TVA plant-feed laterals are OVERLAP, i.e. counted at the terminal or plant.
Fields and leasing (cumulative production, annualized over H = 30 like Phase 1):
- Willow: 590 MMbbl (2020 FEIS; 2023 ROD 576).
- Nanushuk: 80 kb/d x 30 yr (medium).
- NPL: 7 Tcf.
- Moneta Divide: 18.16 Tcf + 254 MMbbl.
- Converse County: 1,370 MMbbl + 5.79 Tcf (conflicting low 94).
- Liberty: 120 MMbbl.
- ANWR Coastal Plain: midpoint of 1.5-10 Bbbl and 0-7 Tcf.
- NPR-A 2020: midpoint of 633-2,638 MMbbl.
- 2024-29 OCS Program: IMPUTED as 3/10 of the 2017-22 Program (BOEM pages unavailable).
- Osage: 2018 production x 30 yr (continuation).
- Enefit: 50 kb/d x 30 yr.
Coal (Mst):
- Alton 30.8
- Rosebud Area F 68.5
- San Juan deep lease 33 (mine closed 2022)
- Sugar Camp: IMPUTED at the universe median 55.7
Gas plants:
- TVA Cumberland 1,450 MW and Kingston 1,500 MW (EF 0.37 ASSUMED).
- NJ TRANSITGRID 104 MW (EF 0.45).
Offshore wind:
- COP-approved MW (Harvard EELP tracker; medium).
- Built = operating or under construction (Empire counted at 810 of 2,076).
Clean programmatics:
- Western Solar Plan PEIS: 697,830 acres RFD / 7 acres per MW (ASSUMED) x 50% realization (the Phase 1 rule for
  "potential" figures) = 49.8 GW; range 0-139.6 GW (5 acres/MW, full).
- NY Bight PEIS: 5,601 MW x 50%.
Nuclear:
- Clinch River ESP: 800 MWe envelope.
- Clinch River technology park: first BWRX-300, 300 MW (dup_pooled).
- Licence renewals: 0 central; operating MW credited only in credit_existing. Indian Point is credited 0 (closed).

CGEP TIMING (Mt-years)
- Mt-years = months / 12 x per-project Mt/yr, in every cell. Months come from the CGEP real-project replays
  (months_saved_total; months_saved_low as a sensitivity).
- Covered types: Pipeline, Transmission, Solar, Wind, OffshoreWind, Geothermal.
- Covered-type projects with no replay get the CGEP type median from all 144 replays:
  - pipeline 1.55
  - transmission 10.65
  - solar 0.70
  - wind 1.30
  - offshore 0.40
  - geothermal 0.00
- A matched-only variant is also reported.
- Uncovered types (LNG, coal, oil and gas fields and leasing, nuclear, hydro, gas plants, clean programmatics) are
  bracketed at 0, the pipeline median (1.55) and the transmission median (10.65, the largest type median; applying it
  to LNG or leasing is a deliberate stretch).
- Uncovered types receive the bracket months only, with no litigation uplift, because CGEP has no archetype for them.
- Litigated uplift: months + B&W litigation rate x (contested.total - smooth.total) for that type, from the CGEP
  number_ledger:
  - pipeline 21 - 4
  - transmission 96 - 2.5
  - solar 35 - 5.5
  - wind 20 - 4.5
  - offshore 24 - 7
  - geothermal 29 - 0
  - Offshore wind uses the B&W onshore-wind rate (0.38).
- The months are fixed (no uncertainty). The MC covers the emissions factors only.
- For depletable fossil resources the Mt-years are largely timing, not added cumulative extraction.

CAVEATS
- All Phase 1 caveats apply: exposure composition only, supply-chain overlap, and so on.
- Era assignment uses CEQ FEIS dates: Phase 1 EISs keep their 2018-workbook dates (universe.csv; the 21 re-dated items
  use their 2018 date), new EISs use 2024-workbook dates. One renewal (Turkey Point SLR) appears mis-dated to 2011 in the CEQ data; it
  has zero emissions.
- The 2024 workbook drops four new-reactor COLs and Greens Hollow, which Phase 1 kept. Using it alone for 2010-17
  would lower clean by 28 Mt/yr.
- Several statuses (SPOT, GulfLink, Texas LNG, solar status unknowns) rest on the absence of later notices.
- CGEP data: licence unknown. The methods appendix is marked "Draft for CGEP review, not for circulation". Only the
  minimal join table and two summary tables are stored here.

```
