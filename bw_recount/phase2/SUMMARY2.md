# Phase 2 summary: 2019–24 extension and CGEP timing join (2026-10-21)

**Status: preliminary.** Not yet externally reviewed. Converted from the subagent draft.

**Credit:** per-project months saved (`cgep_join.csv`), type medians and archetype totals are from Columbia CGEP, [How the Senate Permitting Reform Bill Could Impact Energy Project Timelines](https://www.energypolicy.columbia.edu/how-the-senate-permitting-reform-bill-could-impact-energy-project-timelines/) (Jack Andreasen Cavanaugh, Oct 21, 2026). They are republished here with the author's permission. CGEP's full tables are not redistributed; get them from the CGEP page.

```text
NOTE BEFORE COMMITTING phase2/: CGEP's methods appendix is marked "Draft for CGEP review, not for circulation".
phase2/ holds a minimal join table and two derived summaries from it; check with CGEP before pushing to the public repo.

PHASE 2 SUMMARY (draft, 2026-10-21; to become phase2/SUMMARY2.md)
Extension to 2019-2024 (CEQ 2010-2024 workbook) and CGEP-timing Mt-years
=====================================================================

All values are MtCO2/yr at full operation (clean = avoided, fossil = added), or Mt-years for the timing estimate.
- "Central" = all factors at central values.
- "MC" = 10,000 draws, median [5-95%]; shared factors drawn once per draw.
- Primary cell = transmission in, US-territorial, net.
- Exposure composition only; this is not the bill's effect. Same caveats as Phase 1.

1. RECONCILIATION: 2018 workbook -> 2010-2024 workbook (Jan 13 2025, 1,903 FEISs)
- Coverage: the 2018 workbook covers FEIS 2010-2017. The 2024 workbook lists 1,264 FEISs for those years, against
  1,269 in the 2018 workbook.
- Recovered: 231 of the 237 Phase 1 universe EISs.
  - 229 by title (one fuzzy).
  - 2 by hand: the spent-fuel generic EIS (R0201) and Turkey Point 6&7 COLs (R1053), both retitled or re-dated.
- Re-dated: 21 universe EISs have a different NOI, FEIS or ROD date.
  - Mostly FEIS dates shifting by days to weeks.
  - Six No-ROD EISs now carry a ROD (e.g., I-5 Corridor 2017, G&G GoM 2020, Middle Fork American 2019).
- Dropped from the 2024 workbook: 6 EISs.
  - Four new-reactor COLs: Levy 1&2, Calvert Cliffs 3, Comanche Peak 3&4, Bell Bend.
  - Greens Hollow coal lease.
  - The duplicate West Elk lease-modification EIS (R0305).
  - The dropped COLs carry 28.2 of Phase 1's 143 Mt/yr clean (US net). Greens Hollow carries 2.1 Mt fossil.
  - Phase 1 keeps them; the 2010-18 set is unchanged.
- Added for 2010-17 in the 2024 workbook only:
  - Na Pua Makani wind ITP (FEIS 2016, 25 MW). Included in the 2010-16 era.
  - Two nuclear licence renewals: Indian Point; Turkey Point 3&4 subsequent renewal, whose CEQ FEIS date of 2011
    looks mis-keyed. Both are continuations, so zero emissions.
  - The rest are non-energy.

2. NEW ENERGY EISs (FEIS 2018-2024, plus the three 2010-17 additions)
- Totals: 155 new EISs, hand-classified: 65 clean, 67 fossil, 23 other.
- By FEIS year (clean / fossil):

  Year   Clean  Fossil
  2018       7       9
  2019      13      15
  2020      10       9
  2021       4       6
  2022       6      15
  2023       6      10
  2024      16       3

- Fossil (67):
  - 34 pipelines (7 are LNG- or plant-feed laterals, counted at the terminal or plant), including 2 crude-export
    deepwater ports and the Enefit corridor.
  - 14 LNG EISs (12 terminals + 2 duplicates).
  - 6 field developments, 6 leasing programs, 4 coal mines, 3 gas plants.
- Clean (65):
  - 11 offshore wind COPs, 13 solar, 8 wind, 9 transmission.
  - 9 nuclear: 1 ESP, 1 technology park, 7 licence renewals.
  - 7 hydro, 3 pumped storage, 3 geothermal leasing, 2 clean programmatics.
- Biggest new clean (US = global net):
  - 2024 Western Solar Plan PEIS: 42.6. IMPUTED from about 697,830 acres RFD at 7 acres/MW, x 50% realization.
  - NY Bight PEIS: 3.9.
  - Atlantic Shores South: 3.9 (cancelled).
  - New England Wind: 3.6.
  - CVOW: 3.6.
  - SouthCoast: 3.4.
  - Maryland OW: 3.1.
  - Empire: 2.9.
  - Clinch River ESP: 2.6.
  - Ten West Link: 1.7.
- Biggest new fossil (US net / global net):
  - ANWR Coastal Plain leasing: 8.2 / 38.2 (leases cancelled 2023).
  - SPOT crude-export port: 0 / 25.1.
  - Moneta Divide: 11.7 / 15.9.
  - Converse County: 5.1 / 13.0.
  - Texas GulfLink: 0 / 12.6.
  - MIDSHIP pipeline: 10.4 / 10.4.
  - NPR-A IAP 2020: 1.7 / 10.1.
  - 2024-29 OCS Program: 3.5 / 9.8 (imputed).
  - Driftwood LNG: 4.1 / 7.8.
  - Rio Grande LNG: 4.0 / 7.7.

3. ERA RESULTS (central; MC median [5-95%], P(fossil > clean))

Primary cell (transmission in, US, net):
  Era             Clean  Fossil  Net    Ratio  MC net             P
  2010-16           142     235    +93   0.60  +59 [-32, +158]    0.84
  2017-20             8     144   +136   0.06  +133 [+58, +216]   1.00
  2021-24            80      34    -46   2.37  -63 [-119, -16]    0.01   LOWERS
  2010-18 Phase 1   143     300   +157   0.48  +129 [-17, +289]   0.92   (unchanged)
  2010-24 pooled    227     411   +184   0.55  +130 [-62, +341]   0.85

Global/net:
  Era             Clean  Fossil  Net    MC net             P
  2010-16           142     340   +198  +163 [+61, +274]   1.00
  2017-20             8     227   +219  +220 [+134, +314]  1.00
  2021-24            80      85     +5   +1 [-67, +66]      0.51
  2010-24 pooled    227     650   +423  +387 [+166, +623]  1.00

Sign table, central:
- Every era and cell RAISES except 2021-24 US/net, both transmission in (-46) and out (-43).
- All gross cells and all global/net cells raise. 2021-24 global/net is roughly a tie (+5, P = 0.51).

What 2021-24 rests on:
- Without programmatics it narrows: projects-only US/net is 38 clean vs 32 fossil (net -6, P = 0.3).
- Global/net projects-only flips to fossil-larger (+52, P = 1.0).
- Built/under construction only: 13 clean vs 30 fossil (net +17, P = 0.9).
- Cambium MER: -8.5 (P = 0.4).
- So the 2021-24 clean lean depends on the Western Solar Plan PEIS and on permitted-but-unbuilt offshore wind.

Pooled 2010-24 sensitivities (primary cell, MC):
  Case                        Clean  Fossil  Net    P
  Projects only                 163     341   +177   0.9
  Built only                     46     247   +200   1.0
  Pipe net EIA 0.23             254     295    +41   0.8
  Pipe net ICF -0.075           253     124   -130   0.0   flips (global/net still +118, P = 0.9)
  Drop fossil continuations     253     338    +82   0.7
  Credit existing               293     388    +92   0.8
  Cambium MER                   122     392   +268   1.0

Litigation-weighted (B&W rates; offshore wind uses the onshore-wind 38%):
- Pooled US/net: 49 clean vs 182 fossil (P = 0.99).
- 2021-24: -8.6 (P = 0.2).

4. COMBINED TIMING: Mt-years brought forward (pooled 2010-24, transmission in, net)
Mt-years = CGEP months saved / 12 x emissions. Clean projects bring avoided CO2 forward; fossil projects bring
emissions forward. For depletable fossil resources this is largely timing, not added cumulative extraction.

Covered types only (pipeline, transmission, solar, wind, offshore, geothermal; unmatched projects at CGEP type
median):
- US/net: central clean 29.9 vs fossil 29.5 Mt-yr. Ratio 1.02.
  MC: clean 41 vs fossil 32, ratio 1.31 [0.58-5.96], net -10 [-44, +22], P(fossil > clean) = 0.30.
- Global/net: central 29.9 vs 38.7 (ratio 0.77). MC P = 0.49.
- Matched projects only (115 CGEP replays): central 28.4 vs 28.2 (US/net).
- Transmission carries 23 of the 30 clean Mt-years, because CGEP's transmission median is 10.65 months against
  0.4-1.55 for the other types. Without transmission, clean is 6.6 vs fossil 29.5.

Brackets for uncovered types (LNG, coal, oil and gas leasing and fields, nuclear, hydro, clean programmatics), US/net
central:
  Months assumed for uncovered types     Clean  Fossil
  0                                      29.9    29.5
  CGEP pipeline median (1.55 mo)         50.7    56.6
  Transmission median (10.65 mo, max)  172.6   215.7
- Global/net at 1.55 mo: 50.7 vs 87.9.
- Global/net at 10.65 mo: 172.6 vs 376.5.

Sensitivities (uncovered types get bracket months only, no uplift):
- months_saved_low: 22.2 vs 24.6 (US/net central).
- Litigated-case uplift (expected months = replay + B&W rate x (Delays and challenges - Deadlines met archetype
  total)):
  - Uncovered = 0: 113.7 vs 189.1 US/net (ratio 0.60). MC net +54 [-116, +237], P = 0.69.
  - Global/net: 113.7 vs 252.5.

Headline: on the deadlines-met replays the timing effect is a wash for covered types, and the clean side's share
depends on transmission. Once litigated cases are weighted in, or uncovered fossil types get any months, fossil
Mt-years exceed clean.

5. CGEP COVERAGE (share of pooled 2010-24 exposure emissions, central)
  Side     Basis       Covered types   Matched CGEP project
  Clean    US/net           29%              26%
  Fossil   US/net           48%              46%
  Fossil   global/net       41%              30%

6. DATA QUALITY
- Imputed sizes:
  - Pooled clean: 23% of emissions, mostly the Western Solar Plan PEIS acres-to-MW conversion.
  - New-EIS clean: 50%.
  - Pooled fossil: 4%.
- Low-confidence sources: 27% of pooled clean, 3% of fossil.

7. PHYSICALLY ODD / UNRESOLVED
- Western Solar Plan PEIS: 42.6 Mt/yr from an acreage RFD drawn from DOE's Solar Futures decarbonization scenario.
  The acres-to-MW factor (7) is ASSUMED. This single programmatic drives the 2021-24 sign.
- SPOT and GulfLink crude-export ports: 25 + 13 Mt/yr global net, from an ASSUMED 10% midstream net factor on
  2 + 1 Mb/d. Export capacity does not create production. Neither is built.
- Moneta Divide (18 Tcf over 65 yr) is annualized over 30 yr, like all depletables. Its annual rate is overstated
  relative to the EIS schedule; cumulative is consistent.
- Converse County oil conflict: BLM 1,370 MMbbl vs a county page's 94 MMbbl. Central 1,370, low 94.
- Kingston coal retirement reversed (Feb 2026): its gas CC adds on top of coal for now. Our method nets gas against
  marginal MER, not against coal.
- CEQ omissions: Crimson Solar (FEIS 2021, in CGEP) is not in the 2024 workbook. The Willow 2023 SEIS is not listed
  separately.
- Not sized: Sugar Camp coal (imputed), Riley Ridge CO2 pipeline, three geothermal leasing EISs, relicensed hydro MW
  (only affects credit-existing).
- Not done: the optional 2025-26 e-NEPA extension.
- CGEP materials are marked "Draft for CGEP review, not for circulation" (methods appendix header). phase2/ holds
  only the minimal join table and two derived summaries (type medians, archetype totals), with attribution. Check
  with CGEP before these go into the public repo.

```

## Review notes (main session, 2026-10-21)
- **2021–24 is roughly balanced, not clean-leaning.**
  - 42.6 of its 79.7 clean Mt (US net) come from one imputed programmatic line: the 2024 Western Solar Plan RFD, 697,830 acres from a DOE scenario at an assumed 7 acres/MW, halved.
  - Projects only, the split is 38 vs 32. Built only, it is 13 vs 30.
- **2021–24 global/net (79.7 vs 85.1) leans on two unbuilt crude export ports.** SPOT (25.1) and Texas GulfLink (12.6) are counted at an assumed 10% net factor. Zeroed, fossil falls to 47.5 vs clean 79.7 (central, not MC).
- **ANWR status is stale.** The Coastal Plain row is tagged "cancelled". Per CRS IF12006, Interior rescinded the Biden ROD in Oct 2025 and lifted the suspension on AIDEA's leases, and a court vacated the 2023 cancellations in Mar 2025. No result changes, because programmatic EISs are excluded from built-only, but the label should be corrected.
- **Mt-years has two readings:**
  - With transmission: 29.9 clean vs 29.5 fossil.
  - Without transmission, which is the NEPA row's unique contribution: 6.6 vs 29.5.
  - CGEP covers 29% of clean and 48% of fossil exposure, so the brackets for uncovered types matter more than the covered tie.
- **CEQ data quality.** The 2024 workbook silently drops six EISs that were in its own 2018 edition, including four reactor COLs (~20% of 2010–17 clean exposure) and the Greens Hollow coal lease.
