# Senate permitting deal scorecard

A provision-by-provision scorecard of the **Bipartisan American Affordability and Jobs Act of 2026** (Senate draft released September 30, 2026). For each provision it shows who it helps today (clean energy, fossil fuels, or both) and the likely direction and rough scale of its effect on US emissions.

**View it:** https://hausfath.github.io/permitting-scorecard-2026/

By Zeke Hausfather, [The Climate Brink](https://www.theclimatebrink.com/).

## What's here

| File | What it is |
|---|---|
| `index.html` | The web page (served by GitHub Pages) |
| `permitting_provisions.csv` | The scorecard as data, one row per provision |
| `permitting_infographic_social.png` | The graphic for social media |
| `permitting_infographic.png` | The same graphic with a "Not in this bill" box |
| `METHODS.md` | How each provision was rated, with the numbers and reasoning behind every anchor |
| `infographic.py` | Holds all row content and computed anchors, and draws both PNGs |
| `build_share.py` | Builds the CSV and web page from the same row content |

## How it's built

All provision text, ratings and context numbers live in one place, the `GROUPS` list in `infographic.py`. The numbers shown as anchors (the wind and solar emissions range, and CO₂ per Bcf/d of pipeline capacity) are computed in `anchors()` rather than typed in by hand.

```bash
pip install matplotlib        # Arial is used if installed; DejaVu Sans supplies the arrow glyphs
python infographic.py         # writes permitting_infographic.png and permitting_infographic_social.png
python build_share.py         # writes permitting_provisions.csv and index.html
```

To change a rating or a description, edit `GROUPS` in `infographic.py`, then run both scripts. The graphic, CSV and page will stay in sync.

## Important caveats

- **The ratings are the author's qualitative judgments.** No one has modeled this bill. The scale key (small <10, moderate 10–100, large >100 MtCO₂/yr) sets rough orders of magnitude, not estimates.
- **The numbers are context anchors, not estimates of the bill's effect.** Assumptions (capacity factors, displaced emission rates) are stated in `METHODS.md`.
- **"Helps" reflects who faces federal obstacles and most NEPA reviews today.** Several provisions are neutral on their face and could protect either side under a future administration.
- **The scorecard reflects the Sept. 30, 2026 Senate draft.** It may change with the manager's amendment.

## Sources

- Bill text: [Senate Energy and Natural Resources Committee](https://www.energy.senate.gov/wp-content/uploads/2026/09/Bipartisan-American-Affordability-and-Jobs-Act.pdf)
- [Princeton REPEAT (2022)](https://zenodo.org/records/7106176), transmission and the IRA
- [Bennon & Wilson (2023)](https://www.elr.info/sites/default/files/files-general/53.10836.pdf), NEPA litigation over large energy and transport projects (Table 1 recounted by the author)
- [LBNL, Queued Up: 2026 edition](https://emp.lbl.gov/publications/queued-2026-edition-characteristics), interconnection queues
- [Resources for the Future (Prest, 2024)](https://www.rff.org/publications/issue-briefs/federal-permitting-reform-expand-oil-and-gas-leasing-carbon-emissions/), federal leasing and global emissions
- [Utility Dive (April 2026)](https://www.utilitydive.com/news/court-trump-wind-solar-permitting/818152/), on the Charles River Associates estimate cited in *Renew Northeast v. DOI*
- EIA CO₂ emission factors for natural gas

## License

- **Code** (`*.py`): MIT License; see `LICENSE`.
- **Content** (the graphics, CSV, page text and METHODS): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit "Zeke Hausfather, The Climate Brink".
- **Data sources:** the bill text is a US government work in the public domain. Cited studies and articles remain under their publishers' terms; only short factual figures are reproduced here.
