# Statistics review (Opus, read-only), 2026-10-21

**Status:** addressed 2026-10-21. The numbers quoted here are from the first-pass run; see `../SUMMARY.md` 'Revised results' and `../RESULTS_REVISED.md`.

Summary of the reviewer's report. Scratch scripts were in the session scratchpad (`review_stats/`).

**Arithmetic.** Reproduced:
- Phase 1 primary cell: 143.14 vs 299.92.
- Global/net: 143.14 vs 404.98.
- 2021–24 cell: 79.71 vs 33.62 / 85.15.
- Mt-years: 29.9 / 29.5 and 113.7 / 189.1.
- Five high-leverage rows end to end: Wright Area, Rover, Comanche Peak, Solar PEIS, Moneta Divide.

## Critical
**C1.** The US/net sign comes down to one factor.
- With non-pipeline fossil at 142.86 vs clean at 143.14, US/net ≈ −0.3 + 436 × NET_PIPE.
- MC correlation between net and NET_PIPE is 0.97. P = 0.92 simply restates the triangular prior placed on NET_PIPE (peak at Sabal Trail 0.36; upper bound 0.90 assumed).
- Per-project size draws barely matter (net SD 92 vs 91 with sizes fixed).
- **Fix:** report a discrete scenario table by pipeline study, and publish no probability for US/net.

## Major
**M1.** The "less favorable to clean" central rule now favors the published claim.
- Clean-favorable centrals (MER 0.45, NET_PIPE 0.23, NET_COAL 0.3, USSHARE_GASNET 0.5): US/net +38, global/net +161.
- All factors at their clean-favorable bounds: US/net −83, global/net −19. This corner is unlikely; a copula barely moves P.
- **Fix:** headline the scenario table.

**M2.** Structural uncertainty is missing from every interval.
- Unmodeled choices: the 2024-dropped COLs (−28 Mt), Wright Area as a continuation, nuclear COLs abandoned for cost (82 Mt), programmatic realization (WSP 0–120 Mt), and supply-chain double counting.
- The 50% programmatic haircut is drawn per project. It should be one shared factor, and DRECP should be included in it (currently not halved).

**M3.** Mt-years is not fit for a clean-vs-fossil comparison.
- CGEP's replays end at the federal decision, so post-approval suits fall outside them (MVP 0.1 and ACP 0.1 months).
- The uplift is not a valid expected value:
  - It applies the B&W P(any suit) to a vacatur "high-end case".
  - The archetypes run to in-service, and most of the transmission figure is state siting.
  - The archetypes also include agency delay.
- Units should be "Mt brought forward". Impute type means, not medians: the tie becomes 32.0 vs 29.9.
- The metric ignores cancellations.

**M4.** The era contrast is overstated.
- Within-era project bootstrap for 2021–24:
  - net −43.5 [−127, +14] with WSP;
  - −0.9 [−24, +22] without WSP.
- Fossil share, 2021–24 vs 2010–20: −0.41 [−0.59, −0.09], or −0.22 without WSP. 2017–20 does most of the work.
- Era is confounded with administration.
- **Fix:** report the bootstrap and leave-one-out results, and use no trend language.

**M5.** Litigation weights are fixed and rest on tiny n.
- Nuclear 0% comes from n = 2 (Jeffreys 90% interval 0–0.57).
- With nuclear at 0.31: 44 vs 141. With rates pooled by side: ~50 vs 129. The sign holds.
- **Fix:** draw the rates from Beta distributions; code litigation at the project level (step 3b).

## Minor
- **Central vs MC median gap.** Coherent, not a bug. Headline the MC median.
- **Overlap.** Solar PEIS, DRECP and WSP overlap; pipelines overlap gas fields and LNG. **Fix:** run a max-not-sum sensitivity.
- **Global/net.** Fossil gets Prest leakage while clean gets no rebound, so global/net is conservative toward clean.
- **Built-only and stalled-only.** These select on the outcome, so treat them as descriptive only.
- **Annualization.** Add a cumulative-over-asset-life sensitivity. Moneta is annualized at 2.2× its EIS rate.
- **Label.** Phase 1 FEIS run 2010–2017; the "2010–18" label is wrong.

## Verdict
- The anchor holds as a description of 2010–18 EIS exposure.
  - Robust on global/net: 100% of draws, and 77% even under ICF.
  - Robust on B&W composition: 42 vs 200.
- It is not supported as a probability for US/net.
- The 2.4:1 figure is B&W's count; the recount universe is 121:78.
- Suggested wording: "...fossil projects were larger by emissions under most assumptions (about 2–3x on a global net basis...). The US-only comparison depends on how much coal new gas pipelines displaced."
- "Either way, size unknown" remains right. Keep Mt-years out of public comparisons until M3 is fixed.
