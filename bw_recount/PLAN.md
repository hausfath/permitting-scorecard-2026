# Emissions-weighted recount of Bennon & Wilson (2023) energy EISs

**Question.** The scorecard's NEPA row ("Lowers, on net", §§1106, 1110, 2201) rests on project counts: clean projects outnumber fossil 2.4:1 among 2010–18 energy EISs and 2:1 among litigated ones. Does the clean lean survive when each project is weighted by its emissions (avoided for clean, added for fossil)?

**Scope note.** This tests the *composition* of projects exposed to EIS-level NEPA review and litigation. It does not estimate the bill's effect, which would also need the marginal change in delay or cancellation risk. The implicit assumption is that this change is the same per project across types, which is the same assumption the count-based ratio makes.

## Data
- **Bennon & Wilson (2023)**: [53 ELR 10836](https://www.elr.info/sites/default/files/files-general/53.10836.pdf).
  - Built from CEQ's database of 1,161 EISs (final EIS 2010 to mid-2018), narrowed to 171 energy and 184 transport projects.
  - Project-level litigation coding is **not published**. Table 1 gives counts and litigation rates by subsector.
- **CEQ, Environmental Impact Statement Timelines (2010–2017)**: the December 2018 report and its Excel workbook (nepa.gov / ceq.doe.gov). The June 2020 update (1,276 EISs, 2010–2018) is a fallback.

## Validation targets (B&W Table 1, energy subsectors: count, litigation rate)

| Group | Subsector | Count | Litigation rate |
|---|---|---|---|
| Clean | Solar | 22 | 64% |
| Clean | Wind | 13 | 38% |
| Clean | Transmission | 42 | 31% |
| Clean | Hydro | 14 | 0% |
| Clean | Geothermal | 3 | 33% |
| Clean | Nuclear | 2 | 0% |
| Clean | PumpStorage | 1 | 100% |
| Fossil | Pipeline | 18 | 56% |
| Fossil | Liquefaction | 7 | 29% |
| Fossil | Regasification | 1 | 0% |
| Fossil | GasPlant | 2 | 0% |
| Fossil | CoalPlant | 2 | 0% |
| Fossil | Mine-Coal | 4 | 50% |
| Fossil | Mine-Gas | 6 | 50% |
| Other | Energy-Programmatic | 15 | 20% |
| Other | Waste | 8 | 25% |
| Other | BioPlant | 2 | 50% |
| Other | BioRefinery | 1 | 0% |
| Other | CarbonCapture | 2 | 0% |
| Other | Mine-Other | 4 | 25% |
| Other | Other-Energy | 2 | 0% |

Totals: clean 97, fossil 40, other 34, all 171.

## Steps

0. **Validation gate. Stop and report if it fails.**
   - Rebuild the 171-project energy list from the CEQ workbook and assign B&W subsectors.
   - Pass if the total is within ±5 of 171 and every clean and fossil subsector count is within ±2.
   - Report the reproduced counts next to Table 1 and list every ambiguous assignment.
   - **Name all 15 Energy-Programmatic EISs and all 6 Mine-Gas EISs.**
     - Lease-sale programs (e.g., OCS five-year program, Gulf multisale) or field-development EISs are fossil in a sensitivity, because §2201's 150-day limit covers lease sales.
     - Programmatic clean EISs (e.g., the 2012 Solar PEIS) are clean in the same sensitivity.
   - Write the gate result to `SUMMARY.md` before starting step 1.
1. **Physical size per project, in order of leverage.** Write `projects.csv` after each tier:
   1. the 40 fossil projects;
   2. solar, wind, nuclear and geothermal;
   3. hydro triage (new vs relicensing only);
   4. transmission, loosely (rated MW, or kV × miles).

   For each project:
   - Generation: MW. Pipelines: Bcf/d. LNG: MTPA. Mines: Mt/yr. Gas-field development: production or well count.
   - Use the EIS, ROD, FERC or BLM dockets, or EIA.
   - Record a source URL and a confidence flag for every value.
   - Classify **new build vs relicensing or expansion of existing** facilities. FERC hydro relicensing has no incremental avoided emissions.
2. **Emissions per project** at full operation, MtCO₂/yr, with low/central/high factors:
   - **Clean generation:** MW × capacity factor (EIA or ATB by technology) × displaced 0.35–0.50 tCO₂/MWh. These are the scorecard's MER values (`infographic.py`).
   - **Transmission:** kept as its own bucket. Enabled clean capacity per GW of transfer has a low central value (less favorable to clean), with ACP's 1.4 as the high end. Many lines are reliability or load-serving lines rather than renewable-enabling, so classify each one where possible.
   - **Pipelines:** Bcf/d × 20.1 MtCO₂ per Bcf/d (EIA factors) × utilization. Report gross, and net of what the gas displaces (coal versus other gas). Upstream methane is a sensitivity (state the GWP and leak rate).
   - **LNG:** US-territorial (liquefaction plus upstream) vs global (plus downstream combustion), each gross and net of substitution abroad.
   - **Coal mines, gas-field development, gas and coal plants:** combustion emissions, gross and net of substitution. RFF Prest (2024) gives about 57% displacement for added federal oil; use literature values for coal and gas and cite them.
   - **Other** (programmatic, waste, bio, CCS, other mines): tabulated but excluded from the clean/fossil net; one sensitivity includes the classifiable ones.
3. **Aggregate.**
   - **(a) Exposure-weighted.** All projects: clean avoided vs fossil added, Mt/yr and ratio.
   - **(b) Litigation-weighted.** Subsector litigation rate × subsector emissions (expected value). If time permits, identify which specific fossil and clean-generation projects were litigated and compare with the subsector-rate estimate.
   - **Variants:** a 2×2×2 grid of transmission in/out × US-territorial/global × gross/net.
   - Extract B&W's completion status (built, under construction, predevelopment, cancelled) by sector, if the paper gives it. It bears on the assumption of the same marginal effect per project.
4. **Uncertainty.** Monte Carlo over the factor ranges. Shared factors (MER, utilization, substitution rates, capacity factor by technology) are drawn **once per draw**, not per project. Report the clean:fossil ratio and the net Mt with intervals, and the share of draws where fossil exceeds clean.
5. **Headline rule.**
   - The primary cell is **transmission included, US-territorial, net**. That is the scorecard row's actual scope; its 97 clean count includes the 42 transmission EISs.
   - The global/net cell gets equal billing.
   - The transmission-excluded cells answer a separate question, how much of the row is unique rather than overlapping the Transmission row, and are reported as that.
   - The "harder to confirm" rule applies to factor choices *within* a cell (utilization, substitution, capacity factor, transmission-enablement), not to scope: where a factor is defensible either way, the central value is the one less favorable to "lowers on net".
   - State explicitly whether any variant flips the sign.

## Deliverables (in `bw_recount/`)
- `projects.csv`: one row per project with subsector, size, source URL, confidence, and emissions low/central/high.
- `recount.py`: reads `projects.csv`, writes results and the Monte Carlo summary.
- `METHODS.md`: factors, sources, variants, caveats.
- `SUMMARY.md`: validation check, headline, sensitivity table.
- Raw downloads go to the scratchpad and are deleted after extraction.

## Revision 2026-10-21, after the failed validation gate

Zeke chose the **full CEQ universe as the primary set, with B&W as a check**.

**Primary set**
- All energy EISs in the CEQ Dec 2018 workbook, from both the "FEIS with ROD" and "No ROD" sheets. The title-based candidates number 229.
- Review the classifications by hand. Examples: Downeast LNG counts as Liquefaction, per the fingerprint. Programmatic wind or solar PEISs are clean programmatics.

**Programmatic EISs**
- These are in scope, because §2201's 150-day limit covers lease sales.
- Leasing and lease-sale EISs count as fossil; clean programmatics (DRECP, Solar PEIS and similar) count as clean.
- Size the leasing EISs from the agency's own production and GHG estimates, e.g. BOEM's program and lease-sale EISs and its MarketSim net-of-substitution figures.
- **Do not double count** a five-year program together with the lease sales it covers. Pick one level and document the choice.
- A sensitivity excludes all programmatic EISs (projects only).

**Litigation weighting**
- Apply B&W Table 1 subsector litigation rates to the universe.

**B&W check**
- Take B&W counts × pool-mean size by subsector.
- Report the min and max over fingerprint-feasible subsets (`fingerprint_inclusion.csv`).

**Extra sensitivities and outputs**
- Built-only: weight only projects that were built or are under construction, using current status where findable.
- Concentration: the share of each side's total from its top 10 projects.

**Output format**
- The subagent harness blocks .md files.
- Write `summary_draft.txt` and `methods_draft.txt`; they will be converted to SUMMARY.md and METHODS.md.

## Phase 2 (2026-10-21): extend to 2019–2024 and combine with Columbia CGEP timelines

Zeke approved both steps. Outputs go in `bw_recount/phase2/`.

**A. Extension**
- **Source:** CEQ EIS Timelines 2010–2024 workbook (Jan 13 2025), 1,903 FEISs in sheet "All FEISs". Local copy: scratchpad `ceq2025/ceq2024.xlsx`, from `https://nepa.gov/sites/default/files/documents/CEQ_EIS_Timeline_Data_2024_1_13_2025.xlsx`.
- **Reconcile with the 2018 workbook first:**
  - Show that the 2010–mid-2018 energy universe (237 EISs) is recovered from the 2024 workbook.
  - List any projects added, dropped or re-dated.
  - The 2024 workbook includes FEISs without a ROD.
- **Classify and size** every new energy EIS (FEIS after the 2018 workbook's coverage, through 2024). Use the same subsector scheme, sizing rules, factors (`factors.py`), confidence flags and imputation rules.
  - Offshore wind COP EISs: MW, capacity factor 0.40–0.45 (scorecard OW_CF), MER as before.
  - Watch for nuclear licence renewals and subsequent renewals. These are continuations, like hydro relicensing: zero by default, and credited only under the "credit existing" sensitivity.
- **Optional, if time permits:** 2025–Oct 2026 FEISs from EPA e-NEPA (`cdxapps.epa.gov/cdx-enepa-II`; 500-record cap per query, so query by date range). Report separately if done.
- **Report by era:** 2010–16, 2017–20, 2021–24 (and 2025–26 if done), plus 2010–18 (unchanged) and 2010–24 pooled. Use the same 2x2x2 cells and Monte Carlo, with shared factors drawn once per draw.

**B. Combined timing estimate (Mt-years accelerated)**
- **Source:** CGEP real-project replays. Decoded copy: scratchpad `cgep/emb/real_project_replays.csv`, 144 projects in six technologies. Join on `ceq_title` to our projects.
- **Estimate:** months_saved_total / 12 × each project's emissions (Mt/yr, every cell) = Mt-years brought forward. Clean projects bring displacement forward (avoided cumulative CO₂); fossil projects bring emissions forward. Note that for depletable fossil resources this is largely timing, not necessarily added cumulative extraction.
- **Coverage:** CGEP covers pipelines (the only fossil type), transmission, solar, wind, offshore wind and geothermal. Report the share of exposure emissions on each side that CGEP covers.
- **Uncovered types** (LNG, coal leases, oil and gas leasing and fields, nuclear, hydro, clean programmatics): bracket with 0 months, CGEP's pipeline median, and the max over CGEP types.
- **Sensitivities:**
  - `months_saved_low` in place of `months_saved_total`.
  - Litigated-case uplift: expected months = replay months + B&W litigation rate × (CGEP archetype "delays and challenges" total − "deadlines met" total) for that type. The archetype totals are in CGEP's `number_ledger` (wf.<type>.smooth.total / contested.total) in scratchpad `cgep/emb/baaja_timelines_all_data.csv`.
- **Headline:** clean vs fossil Mt-years, ratio, MC interval, P(fossil > clean), for covered types only and with uncovered brackets.

**Rules**
- Same rules as before: python3.13 (`-I` for raw data), source URL and confidence for every value, imputation flagged.
- Write `.txt` drafts (`summary2_draft.txt`, `methods2_draft.txt`), since the harness blocks `.md`.
- Do not modify existing published results files. New outputs go in `phase2/`.
- CGEP data licence is unknown. Keep raw CGEP tables in the scratchpad. In `phase2/`, store only a minimal join table (our ceq_id, CGEP project name, technology, months_saved_total, months_saved_low) with attribution.
- Delete raw downloads when done, and stop any helper agents before finishing.
