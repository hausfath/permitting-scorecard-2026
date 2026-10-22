# Energy-systems review (Opus, read-only), 2026-10-21

**Status:** addressed 2026-10-21. The numbers quoted here are from the first-pass run; see `../SUMMARY.md` 'Revised results' and `../RESULTS_REVISED.md`.

Summary of the reviewer's report. All variants are central deterministic values for the primary cell (transmission in, US/net) unless stated.

**Sources.**
- Fetched and read by the reviewer: EIA AEO2022 IIF pipeline page; BLM Western Solar Plan FAQ (Aug 2024); GRS w22214 (paragraph around Table 4).
- Search snippets only, unverified: SO 3438; the July 2025 DOI memo; SPOT and GulfLink licence dates; PRB 2023–24 mine tonnage.

## Critical
**C1. The NET_PIPE central of 0.36 is weakly supported.**
- Phase 1 US/net breaks even at NET_PIPE ≈ 0.003, so the US sign amounts to "did new pipelines add any US CO₂ at all".
- The 0.36 comes from Sabal Trail: full burn minus two named offsets. FERC itself "cannot use" a No Action comparison, so this is not a market estimate.
- EIA's no-builds case gives 0.23 for 2050. Marcellus takeaway lines operating 2017–2030 probably displaced more coal, so their true factor is plausibly below 0.23.
- **Fix:** central 0.23, triangle (−0.075, 0.23, 0.36), and state the breakeven.

**C2. ANWR is annualized over 30 years, but the FEIS uses 70.**
- **Fix:** 70 years. Global/net falls from 38.2 to 16.4; consider using the low case as central.

**C3. The crude export ports (SPOT, GulfLink) have an unsourced 10% net factor.**
- The netback channel is about 1% of throughput, and the ports overlap with the production EISs.
- **Fix:** 0 central, range 0–0.03.
- Combined with C2, 2021–24 global/net becomes 79.7 clean vs 25.7 fossil.

## Major
**M1. DRECP is mis-sized.** The BLM LUPA governs the 8,100 MW figure; 20,000 MW is the regional planning assumption. The halving rule was also skipped.
- **Fix:** about 7,600 MW. Clean falls from 16.7 to about 6.5 Mt.

**M2. The Western Solar Plan figure is a goal-derived need, not a forecast.**
- NREL's ~700,000 acres is what "would likely be needed to meet our nation's clean energy goals".
- BLM had permitted about 29 GW of all clean types by July 2024.
- Without the WSP, 2021–24 US/net is 37.1 vs 33.6.

**M3. Programmatic halving is asymmetric.**
- BOEM's anticipated production is also an overestimate; the Arctic and Cook Inlet sales yielded almost nothing.
- The OCS programmes annualize to 265 MMbbl/yr and 2.8 Bcf/d, about 40% of GoM oil.
- Check PFP Table 6-2 for the production period.
- **Fix:** apply a symmetric, empirically calibrated realization factor to both sides.

**M4. Coal.**
- Wright Area central counts North Hilight, which was never sold. Using sold tonnage (1,346 Mst): 49.1 → 36.5 Mt.
- NET_COAL 0.50 comes from a basin-wide price shock. For a single lease tract it is an upper bound; reviewer's judgment is a central of about 0.25 (range 0.1–0.5).
- The emission factor and the treatment of continuations as exposure are fine.

**M5. Fossil supply-chain overlap is not corrected.**
- Ruby and Apex (12.8) carry Rockies federal-field gas (28.5).
- MIDSHIP (10.4, dest=dom) is Cheniere's LNG feed line, which is inconsistent with the zeroed LNG laterals and overlaps the NEMS LNG figure that already includes induced production.
- **Fix:** zero or partially net complementary links.

**M6. Mt-years.**
- Coherent for flow assets; for depletables it measures timing only.
- **Fix:** set leasing, coal and field rows to 0 and drop the 10.65-month bracket for them.

## Minor
- The PLAN rule is applied unevenly in both directions. MER 0.40 vs Cambium ~0.20 favors clean (+231); excluding methane favors clean (+13).
- SunZia is effectively a gen-tie for ~3.5 GW of wind, so it is understated (1.6 vs ~4.2 Mt).
- Converse County is inflated by H = 30.
- Rio Grande built_size may be stale (unverified).
- Spot-checks passed:
  - pipeline Bcf/d for Rover, MXP, MVP, Atlantic Sunrise, Leach, NEXUS, Ruby, ACP, REAE;
  - reactor MW;
  - offshore wind COP MW.

## Combined effect on Phase 1 US/net
| Change | Clean vs fossil (net) |
|---|---|
| NET_PIPE 0.23 + Wright sold + NET_COAL 0.25 | 143 vs 207 (+63) |
| + DRECP fix | about +73 |
| with NET_PIPE 0.15 instead | about +38 |

Global/net stays at about +167 or higher.

## Verdict
- **Global/net 2010–18:** "fossil larger by emissions" holds.
- **US/net:** holds only if new pipelines added any net US CO₂.
- **Anchor fixes:** attribute 2.4:1 to B&W (this universe is 121:78, about 1.55:1) and name the basis.
- **2021–24** leans clean once ANWR and the ports are fixed, but that rests on the WSP and offshore wind that is permitted but unbuilt.
- **Rating:** "Either way, size unknown" is well supported.
