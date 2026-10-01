# Methods: permitting bill infographic and emissions assessment

Source text: *Bipartisan American Affordability and Jobs Act of 2026*, Senate draft (S.L.C. KAT26639), 417 pp., posted 2026-09-30 at
https://www.energy.senate.gov/wp-content/uploads/2026/09/Bipartisan-American-Affordability-and-Jobs-Act.pdf.
Every provision description was checked against the bill text. An independent adversarial legal-reading pass then reviewed the readings, and its corrections are incorporated (see "Legal-reading corrections" below).

## Rating scheme (infographic)

- **Lean** (CLEAN / BOTH / FOSSIL): which resources benefit *under the current policy environment*. The BOTH label is used for provisions that are facially neutral and whose beneficiary depends on which projects agencies are blocking or which projects face review and litigation (§§1106, 1110, 2201, 1401–1403).
- **Direction**: sign of the likely effect on US emissions relative to no bill. The emissions pips are colored by direction, independent of the "Helps" chip: blue = lowers (including "on net" and "for now"), red = raises, gray = either way.
- **Scale** (small / moderate / large / unknown): author judgment of the plausible US emissions effect over roughly 2030–2040. The rough meaning of each bin:
  - small: well under 10 MtCO₂/yr;
  - moderate: roughly 10–100 MtCO₂/yr;
  - large: potentially >100 MtCO₂/yr.
- **Test applied to each provision**: is federal permitting the binding constraint on deployment of the affected resource? These are ordinal judgments, not model output. The bill has not been modeled by anyone as of 2026-09-30.

| Provision | Lean | Scale | Rationale |
|---|---|---|---|
| Transmission (§§2101–2105, 2109) | Clean | Large | Transmission is the binding constraint (REPEAT 2022). The 'large' rating is generous after OBBBA cut the credits behind REPEAT's IRA-era numbers. Caveats: ERCOT is excluded. Backstop permits and plan-selected lines must "provide improved reliability" (new FPA 216(b)(4), §225(d)(3)), though the definition in §225(a)(4) is broad. The interregional mandate is procedural. FERC implementation risk. OBBBA reduces the marginal clean deployment unlocked. |
| NEPA deadlines/litigation (§§1106, 1110, 2201) | Both (lowers, on net) | Moderate | The provisions are facially neutral, but clean energy dominates the EIS pipeline. Bennon & Wilson (2023, ELR Table 1) cover 171 energy EIS projects from 2010–18. Of these, 97 are clean (solar 22, wind 13, transmission 42, hydro 14, geothermal 3, nuclear 2, pumped storage 1), 40 are fossil (pipeline 18, liquefaction 7, regasification 1, gas plant 2, coal plant 2, coal mine 4, gas mine 6), and 34 are other (programmatic 15, waste 8, bio 3, CCS 2, other mine 4, other energy 2). Clean is 57% of all energy EISs and fossil 23%, a ratio of 2.4:1. Among litigated projects, clean is 34 of about 58 (~59%) and fossil 17 (~29%), about 2:1. Per-project litigation rates are clean 35% and fossil 42%. An earlier version of the graphic reported ~70% and 2/3; those shares used the clean+fossil subset only and were corrected. IFP (2024) reports 62% clean vs 16% fossil among energy EISs. Counterpoints behind the BOTH label: (1) §2201's 150-day limit covers oil and gas lease sales (§2201(a)(1)(B)(i)); (2) §1110's no-vacatur remedy covers EA-level reviews, where BLM oil and gas work sits (5 EISs vs 381 EAs vs 77 CEs), and B&W's EIS-only sample can't see this tier; (3) vacatur stopped several fossil projects (Lease Sale 257, Willow, the Dakota Access easement, Sabal Trail). The author's colleagues argued for the lowers-emissions lean, citing land intensity, visibility to opposition, location of shale on private land, and renewables' greater potential for growth. |
| Offshore wind (§§2251–2252) | Clean | Small | Looser OCSLA 8(p)(4)(I) standard, preferred cable routes, and DOI as lead agency. Economics, not permits, are the main constraint after the IRA. |
| NHPA (§2301) | Clean | Small | Procedural; saves time and mitigation cost; §110(f) landmarks untouched. |
| Renewables/geothermal (§§2213–2214, 2221–2228) | Clean | Small | Federal land is a small share of wind and solar siting. §2108 was removed from this row because its behind-the-meter definition includes fossil backup generators. |
| Interconnection queues (§§2106, 2110, 2111) | Both (lowers, on net) | Moderate | §2106 requires consolidated 20-year generation-transmission planning with "resource and fuel-neutral planned interconnection locations", "upfront, fixed, zonal, per-megawatt" costs, single-decision-point cluster studies, nonrefundable financial security and withdrawal penalties. FERC has 18 months for the rule, and regions file within 2 years. §2110 covers AI and automation in queue processing; §2111 requires grid data within 15 days plus an automated-study specification. The provisions are fuel-neutral, but the queue is mostly clean. LBNL Queued Up 2026 (end of 2025) shows solar 773, storage 749, wind 220 and gas 253 GW of a 2,061 GW total, so solar+wind+storage = 84.5% and gas = 12.3% (computed in `anchors()`). The median wait was 61 months for projects built in 2025. Caveats: the gas queue grew 86% in 2025 while the others shrank; gas may have higher completion rates; withdrawal penalties mostly clear speculative solar and wind, which speeds up real projects of all types; FERC Order 2023 already required cluster studies, so part of this is codification. Added at Zeke's request; he agreed that it benefits both renewables and gas. |
| Permit certainty and deadlines (§§1401–1403) | Both | Moderate | §1401 protects issued permits of any type (including pipelines and LNG) and is clean-leaning today. §§1402(c)/1403 force decisions (not approvals) on stalled non-NEPA permits. The §§1402(c)/1403 deadlines reach only permits that need no EIS or EA. Anchor: 57.2 GW of wind, solar, hybrid and offshore capacity canceled or delayed beyond 2029. This is a plaintiffs' consultant estimate (Charles River Associates) cited by the court in Renew Northeast v. DOI (PI of Apr 21 2026), via Utility Dive. At an ASSUMED 25–35% capacity factor and 0.35–0.50 t/MWh, that is 44–88 MtCO₂/yr if built. It is not all attributable to the bill, since deadlines force decisions, not approvals, and §1402 claims wait 180–280 days. |
| Disparate-treatment damages (§1402) | Both | Unknown | Deters future pauses (e.g., LNG); the magnitude depends on future administrations. |
| Pipeline expansion (§§2102(b), 1202, 1204) | Fossil | Moderate | Pipeline capacity is binding in the Northeast. Gross anchor: 20 MtCO₂/yr per Bcf/d. The net effect depends on displacement and methane. The 401 and 404 changes also help power lines. |
| Onshore oil and gas (§§2211, 2229) | Fossil | Small | Production is limited by prices and geology (Columbia CGEP on EPRA 2024). Substitution: RFF (Prest, Sept 2024) estimates a 57% leakage rate for added federal oil. Its expanded-leasing scenario (not in this bill) gives +1.2 GtCO₂e globally over 2024–2050 (range 0.6–2.1), of which ~0.2 Gt is within the US. The anchor text was revised on the recommendation of the author's colleagues. |
| ~~NEPA scope (§1101)~~ | Removed | n/a | Removed from the graphic. The bill limits NEPA to effects "on the human environment of the United States". But *Seven County* (2025) already held that agencies need not analyze effects of separate upstream/downstream projects and gave them substantial deference on scope, and the 2023 Fiscal Responsibility Act amendments already excluded actions with effects entirely outside the US. The marginal change from this bill is therefore small. |

## Anchors (computed in `infographic.py::anchors()`)

- **Wind/solar at risk (shown on graphic).** See the permit-certainty row above.

- **Offshore wind at stake.**
  - Nameplate capacities: CVOW 2.6, Sunrise 0.924, Vineyard 1 0.806, Revolution 0.704, Empire 1 0.81 GW, for 5.84 GW total. These come from news coverage, not primary filings. Utility Dive's "7 GW" figure for the five projects doesn't reconcile with this sum.
  - Capacity factor **ASSUMED** at 40–45%, giving 20.5–23.0 TWh/yr.
  - Displacement rate **ASSUMED** at 0.35–0.50 tCO₂/MWh, bracketing older AVERT regional rates (Northeast 0.46, Mid-Atlantic 0.73; Synapse compilation). The result is 7.2–11.5 MtCO₂/yr.
  - Sensitivity: using the Mid-Atlantic 0.73 rate for CVOW's 2.6 GW would raise the upper end. Cambium LRMERs would be the better update.
- **Pipeline.** Uses EIA's 53.06 kg CO₂/MMBtu and 1.036 MMBtu/Mcf, giving 54.97 kg/Mcf. At 1 Bcf/d that is 20.1 MtCO₂/yr of gross combustion emissions. It excludes upstream methane and ignores displacement.
- **REPEAT (2022)**: ">80% of the potential emissions reductions delivered by IRA in 2030 are lost if transmission expansion is constrained to 1%/year" (~800 Mt/yr); https://zenodo.org/records/7106176.

## Legal-reading corrections incorporated
- §2229: the 5→10-year change applies only to EPAct §390(b)(4), pipeline placement in an approved corridor. It does not change the developed-field windows.
- §2211: exemptions (a)(2)/(a)(3) have no federal-share threshold.
- §1202: "direct point source discharge" is undefined. Stream-crossing fills remain discharges, so the change narrows the state 401 veto rather than ending it.
- LNG: there is no NGA §3 deadline. But new NEPA §3(18)(B)(xiii) combined with §1402(c)'s 1-year clock could create an indirect deadline for DOE export decisions.
- §1401 exception (B) and the presidential-permit gap were added to the caveats.

## Known limitations
- No integrated energy-system modeling. The scale bins are subjective.
- The 2024 EPRA estimates (Third Way et al.) are not transferable to this text.
- The effect of Sept 16, 2026 as the §1401 cutoff date is not understood; I found no source explaining the choice of date.
