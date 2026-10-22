# Bennon & Wilson emissions-weighted recount: summary (2026-10-21)

**Status: preliminary; internally reviewed** (two independent reviewers, `reviews/`). Fixes applied 2026-10-21.

## Revised results after external-style review (2026-10-21)

The statistics and energy-systems reviews are in `reviews/`. Their fixes changed the US-basis result from "fossil larger in 92% of draws" to roughly even. The full generated tables are in **`RESULTS_REVISED.md`**; numbers below come from that file.

**Main findings (transmission included, net basis, MtCO₂/yr):**
- **2010–17 (the Bennon & Wilson era, 2018 CEQ workbook).**
  - Global basis: fossil is larger, central 132 vs 246 (+114). The MC median is +76 [−10, +148]; fossil is about 1.5x clean (0.9–2.1x). This holds in every scenario except ICF's pipeline factor (−21) and the all-clean-favorable corner.
  - US basis: roughly even. Central +48, MC +8 [−74, +73]. The sign depends on how much coal new gas pipelines displaced: ICF −86, EIA (central) +48, Sabal Trail +105.
- **By era.**
  - 2017–20 leans heavily fossil: 8 vs 89 US, 8 vs 139 global.
  - 2021–24 leans clean: 80 vs 22 US, 80 vs 30 global. It stays clean in every scenario except the global all-fossil-favorable corner (+3).
  - Much of the 2021–24 clean side is permitted but unbuilt: the Western Solar Plan and offshore wind. Counting built or under-construction projects only, 2021–24 is about even (13 vs 16).
- **Pooled 2010–24.**
  - US central (+32) and MC median (−37) disagree in sign, because the factor triangles are skewed around best-supported centrals. The pooled US cell is not used publicly.
  - Global pooled: fossil larger, central +155, MC +98 [−23, +206].
- **Litigation-weighted** (Beta-drawn B&W rates), 2010–17: fossil larger on both bases. US +38 [−13, +86]; global +63 [+8, +116].
- **"Mt brought forward"** (CGEP timing join) is internal only and is not a valid clean-vs-fossil estimate (review M3).

**What changed (all from the reviews):**
- NET_PIPE: central 0.23 (EIA systemic), range −0.075 (ICF) to 0.36 (Sabal Trail). The unsupported 0.90 high was dropped.
- NET_COAL: (0.10, 0.25, 0.50).
- Wright Area: sold tonnage (1,345.7 Mst).
- Crude export ports: NET_EXPORT_PORT (0, 0, 0.03).
- Depletables: annualized over each EIS's documented production life where given (ANWR 70, NPR-A 70, Moneta 65, NPL 40, OCS 2012–17 45, 2017–22 and 2024–29 55), else 30 years.
- Programmatic EISs on both sides: one shared realization factor, REAL_PROG (0.25, 0.50, 1.00). This replaces the clean-only 50% haircut; clean RFDs are now entered at full potential. Field-development project EISs (Moneta, Converse, Creston) are not programmatic and keep their full RFD; this residual asymmetry is noted.
- DRECP: 7,600 MW (the LUPA's ~8,100 less Palen), not 19,500.
- SunZia: treated as a gen-tie for ~3.5 GW of wind.
- MIDSHIP: zeroed as an LNG feed line.
- Litigation rates: drawn from Jeffreys Beta.
- A scenario table replaces probability headlines.
- Phase 1 relabeled 2010–17. Its FEIS years run 2010–2017; B&W's sample is 2010–mid-2018.

Everything below this section is the **superseded first-pass write-up**, kept for the record. Its numbers are historical.

---


Reproduce: `python3.13 -I build_projects.py sizing_out && python3.13 recount.py` (results verified to reproduce byte-identically after raw downloads were deleted).

## Scope
**Read first: what this does and does not show.**
- It shows the 2.4:1 count ratio says nothing reliable about emissions. Weighted by emissions, the 2010–18 EIS-exposed mix leans fossil under every weighting tried.
- It does **not** show that the 2030–40 NEPA-exposed mix leans fossil. The 2010–mid-2018 sample captures three things specific to that era:
  - the Powder River Basin coal-lease cycle (Wright Area);
  - the nuclear-renaissance COLs;
  - the Appalachian gas takeaway buildout.
- It contains no offshore wind construction-and-operations plans (those EISs are all 2021 or later) and few of the large interregional transmission lines now proposed. EA-level reviews (most BLM oil and gas permits) are also outside it.
- **Pipeline factor.** The US/net sign rests on the per-Bcf/d pipeline displacement factor:
  - The central 0.36 comes from Sabal Trail, where the gas displaced Florida coal and oil. That is a stretch for Marcellus takeaway lines serving markets that already had gas.
  - With EIA's systemic 0.23, fossil is still larger (net +58, P = 0.99), but the margin is a third as wide.
  - Global/net holds under every factor tried. US/net holds under every pipeline factor except ICF's and is thin under EIA's.

This tests the composition of energy projects exposed to EIS-level NEPA review (final EIS 2010 to mid-2018). It does
not estimate the bill's effect. That would also need the change in delay or cancellation risk per project, which is
implicitly assumed equal across project types (the same assumption the count ratio makes). All values are MtCO2/yr at
full operation. Cumulative production decisions (leases, fields) are annualized over 30 years.

## 1. VALIDATION GATE (step 0): FAILED as written, so the primary set was revised (PLAN revision 2026-10-21)
- The CEQ Dec 2018 workbook (Wayback copy) has exactly 1,161 FEIS-with-ROD rows, which matches B&W. B&W also use 28
  of the 108 "No ROD" rows (fn. 147).
- An independent title-based classification gives 229 energy EISs against B&W's 171. Clean 112 vs 97, fossil 52 vs
  40. The main miss is Nuclear: 12 new-reactor COL/ESP EISs vs B&W's 2. Solar, Pipeline, Mine-Coal and Mine-Gas are
  also off by more than 2.
- The duration fingerprint (Table 1 mean NOI->ROD) identifies eight small subsectors uniquely. It cannot pin down the
  large ones, and Nuclear, Mine-Coal, BioPlant and Hydro have no feasible match.
- Latent bug found later: the title pass missed two EISs, R0681 New England Clean Power Link and R0628 Moab Master
  Leasing Plan. Gate counts move by +1 Transmission and +1 Energy-Programmatic. The gate conclusion is unchanged.
- Per Zeke's decision, the primary set is now the hand-reviewed universe of 237 EISs: 121 clean, 78 fossil, 38 other,
  with 7 duplicate EISs zeroed. B&W's composition is run as a check (section 6).

## 2. HEADLINE: primary cell = transmission included, US-territorial, net
- Central factors (deterministic): clean avoided 143 vs fossil added 300 MtCO2/yr.
  Clean:fossil ratio 0.48. Net +157 Mt/yr (fossil exceeds clean).
- Monte Carlo (10,000 draws; shared factors drawn once per draw): clean 151 vs fossil 280.
  Ratio median 0.54 [5-95%: 0.34-1.13]. Net +129 [-17, +289]. Fossil exceeds clean in 92% of draws.
  The MC median sits below the deterministic central because several triangulars are skewed: the central was set at
  the less-favorable end, per the PLAN rule.

## 3. GLOBAL / NET (equal billing)
- Central: clean 143 vs fossil 405. Ratio 0.35. Net +262.
- MC: clean 151 vs fossil 386. Ratio 0.39 [0.27-0.66]. Net +233 [+78, +400]. Fossil exceeds clean in 100% of draws.

## 4. SIGN TABLE: 2x2x2, exposure-weighted (central; MC share of draws with fossil > clean)

```
   Transmission  Scope   Basis  Clean  Fossil   Net   Sign     P(fossil>clean)
   in            US      net      143     300  +157   RAISES   0.92
   in            US      gross    143     923  +779   RAISES   1.00
   in            global  net      143     405  +262   RAISES   1.00
   in            global  gross    143    1304  +1160  RAISES   1.00
   out           US      net      127     300  +173   RAISES   0.96
   out           US      gross    127     923  +796   RAISES   1.00
   out           global  net      127     405  +278   RAISES   1.00
   out           global  gross    127    1304  +1177  RAISES   1.00
```

- Litigation-weighted (B&W Table 1 subsector rates applied to the universe): all 8 cells RAISE.
  The primary cell is clean 21 vs fossil 135 (MC), with P = 1.00.
- The transmission-out cells answer a separate question: how much of the row is unique rather than overlapping the
  Transmission row. Transmission is 16 of the 143 clean Mt.
- Only one variant flips any cell: the ICF/API pipeline value (-0.075 per unit full-burn capacity).
  - It flips both US/net cells: primary net -77, P = 0.00.
  - Even under it, the global/net cell stays fossil-larger in 77% of draws (net +26).
  - No other sensitivity flips a sign.

## 5. WHAT DRIVES EACH SIDE (central, US net)

Clean (143 Mt/yr):
- Nuclear: 82 Mt/yr, 57%, from 12 COL/ESP EISs. Only Vogtle 3&4 were built; V.C. Summer was abandoned, and the rest
  are not built or were withdrawn.
- Clean programmatics: 30 Mt/yr, 21%. DRECP 16.7; Solar PEIS 10.1 (after a 50% haircut on its "as much as 23,700 MW"
  full build-out).
- Transmission: 16 Mt/yr.
- Solar projects 7.7 and wind 7.0, about 15 Mt/yr together.
- Top 10: DRECP, Comanche Peak 3&4 (10.8), Solar PEIS, STP 3&4 (8.6), then seven AP1000 pairs at 7.1 each (Vogtle,
  Summer, Levy, Turkey Point, Lee, and the PSEG ESP imputed). These ten are 62% of clean.

Fossil (300 Mt/yr):
- Gas pipelines: 157 Mt/yr, 52%. About 21 Bcf/d of capacity, sized from EIA's pipeline database; most of it built.
- Coal leases: 60 Mt/yr. Wright Area alone is 49 Mt/yr, 16% (four ROD-approved PRB tracts, 1,813 Mst).
- Leasing programs: 42 Mt/yr.
- LNG: 19 Mt/yr.
- Gas fields: 18 Mt/yr.
- Top 10: Wright Area 49, Rover 23.5, Mountaineer XPress 19.5, the 2012-17 OCS Program 15.9, MVP 14.4, Atlantic
  Sunrise 12.3, the 2017-22 OCS Program 11.5, Leach XPress 11.1, Ruby 10.8, ACP 10.8. These ten are 60% of fossil.
- Global net top 10 adds the OCS programs (40, 33), Keystone XL (27.4) and the White River FO RMPA (11.9).
- Concentration: the top 10 carry about 60% of each side in every basis (results_concentration.csv).

## 6. B&W CHECK: B&W Table 1 counts x universe pool-mean, with min/max over fingerprint-feasible subsets (US net)
- Clean: 42 [30-60]. Fossil: 200 [117-256]. Energy-Programmatic, net fossil-minus-clean: +5 [-30, +42].
- Global net: clean 42 [30-60], fossil 239 [137-302], Energy-Programmatic +26 [-30, +99].
- So on B&W's own 2.4:1 count composition, emissions still lean fossil by roughly 3-6x. This holds independently of
  the 10 extra nuclear COLs.
- Finding: the Solar fingerprint forces the Solar PEIS into every feasible 22-subset, and Upper Great Plains Wind PEIS
  is in 96% of Wind matches. B&W's "solar" and "wind" counts therefore very likely include programmatic EISs with no
  project MW.

## 7. SENSITIVITIES (primary cell, MC median; clean vs fossil, net, P(fossil>clean))

```
   Case                                                    Clean  Fossil  Net    P
   Projects only (no programmatic either side)              122     251   +128   0.93
   Built / under construction only (programmatics excl.)     32     190   +158   1.00
     (Exposed clean capacity mostly was not built; exposed fossil capacity mostly was.)
   Cambium-like MER 0.10-0.30 t/MWh                          73     284   +212   1.00
   Horizon 20 yr for depletables                            151     325   +172   0.97
   Upstream methane (2.3%, GWP100 29.8)                     151     294   +142   0.95
   Pipeline net = EIA no-new-pipelines (0.23)               151     210    +58   0.99
   Pipeline net = ICF/API (-0.075)                          151      75    -77   0.00   SIGN FLIPS (US cells only)
   Pipeline net = no displacement (0.90)                    151     507   +355   1.00
   Oil/gas leakage = Prest 2022 (net 0.28)                  151     271   +119   0.91
   Transmission enablement = ACP 1.4                        167     280   +113   0.89
   Drop fossil continuations (coal leases incl. Wright,     151     234    +82   0.81
     Four Corners, Groton)  [corrected; see note below]
   Credit existing clean (hydro relicensing, wind HCPs)     156     281   +123   0.91
```

## Lease-Sale / Programmatic
- What is in the leasing set: 24 Leasing-Fossil EISs, sized at the five-year-Program level (2012-17 and 2017-22 OCS
  Programs). The 11 lease-sale EISs tiered to them are "covered" to avoid double counting. Also counted are Sale
  216/222 (from the 2007-12 Program), the White River FO RMPA RFD, and small USFS leasing EISs.
- NPR-A, oil shale and Moab are unquantified.
- Contribution: leasing adds 42 Mt/yr US net (14% of fossil) and 99 Mt/yr global net (25%).
- Sizing at the sale level instead reproduces the Program totals within about 1% (2012-17 multisale midpoint 4,175
  MMbbl / 18.3 Tcf vs Program 4,203 MMbbl / 18.2 Tcf). The Program-vs-sale choice therefore does not matter; the
  meaningful test is the projects-only sensitivity.
- Mine-Gas (9 EISs): Continental Divide-Creston 7.7, Monument Butte 5.1, Greater Natural Buttes 3.9, Gasco Uinta 0.9,
  West Tavaputs 0.4, Point Thomson 0.1, Bull Mountain 0.1 (EUR imputed) and South Unit 0.0 Mt/yr US net. Shadura is
  not sized (pending at close).

## 8. DATA QUALITY
- Imputed sizes:
  - Clean: 6.6% of emissions (PSEG ESP, RDEP, kV-rated small lines).
  - Fossil: 3.5% (EUR-imputed WRFO / West Tavaputs / WRNF / Bull Mountain, Dixie).
- Low-confidence sources: 41% of clean emissions (DRECP and several nuclear COLs: snippet-level) vs 3% of fossil.
  Fossil's biggest items come from EIA databases, BOEM PEIS tables and the Wright Area FR notices, all high confidence.
- Unquantified fossil (NPR-A, where Willow sits; the oil shale PEIS; Moab) biases the result toward clean.

## 9. NOT DONE / OPEN
- Step 3(b): the project-level litigation match.
- ROD-level checks of the largest solar and wind capacities.
- Shadura sizing.
- Erickson & Lazarus (2018) is unverified (paywalled).
- Status checks: Grapevine Canyon, Salt Wells, Mohave, Aiya, Amargosa.

## 10. Added in review: cancelled or stalled projects only (central, US net)
The bill's effect works through projects that review and litigation would otherwise stop or delay, not through projects built anyway. Restricting to projects cancelled, withdrawn, in predevelopment, or without a ROD, computed from `projects.csv`:

| Subset | Clean | Fossil |
|---|---|---|
| All cancelled or stalled | 83.6 | 46.4 |
| Excluding nuclear | 8.6 | 46.4 |

- The clean total is almost entirely nuclear COLs (Comanche Peak, STP, Levy, Lee, Summer, Turkey Point, PSEG, Bell Bend, Calvert Cliffs, North Anna). Those were abandoned for cost and market reasons, not NEPA.
- The largest stalled fossil items are Atlantic Coast (10.8) and PennEast (8.0). Both were cancelled after litigation or permit denials, so these are cases where permitting actually bound. That includes state permitting: PennEast turned partly on New Jersey, and state 401 issues fall under the scorecard's pipeline row.
- The more relevant metric is delay-years × Mt/yr: MVP, for example, was about 6 years × 14 Mt. It has not been computed.

So even on the subset most relevant to the counterfactual, emissions lean fossil once nuclear is set aside.

## 11. Bug fixed in review (2026-10-21)
- `recount.py`'s "drop fossil continuations" sensitivity skipped the COALLEASE branch, so it dropped only Four Corners and Groton and kept the coal-lease continuations: Wright Area 49, Buckskin Hay Creek 4.5, Greens Hollow 2.1, East Lynn 1.0, COC-1362 0.4 Mt/yr.
- Fixed. Primary cell under the corrected sensitivity: fossil 234 vs clean 151, net +82 [5–95%: −60, +237], P(fossil > clean) = 0.81 (previously reported +124, P = 0.91).
- No other result changed. The headline did not use this flag.
