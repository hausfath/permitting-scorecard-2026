"""
Build a shareable, reproducible version of the permitting infographic:
  - permitting_provisions.csv  (one row per provision; paste into a sheet/Datawrapper)
  - share/index.html           (web page with the table, copyable CSV, notes, sources)

Row content is imported from infographic.py (GROUPS, anchors), so the graphic,
the CSV and the page never drift apart. Run after editing infographic.py.
"""

import csv
import html
import io
import re

import infographic as ig

SCALE_MEANING = {3: "large (>100 MtCO2/yr)", 2: "moderate (10-100 MtCO2/yr)",
                 1: "small (<10 MtCO2/yr)", 0: "unknown"}
ANCHOR_SOURCE = {
    "Transmission": ("Princeton REPEAT (2022)", "https://zenodo.org/records/7106176"),
    "NEPA deadlines and lawsuit limits": (
        "Bennon & Wilson (2023), Table 1; author's recount",
        "https://www.elr.info/sites/default/files/files-general/53.10836.pdf"),
    "Permit certainty and deadlines": (
        "Charles River Associates estimate cited in Renew Northeast v. DOI (via Utility Dive); author calculation",
        "https://www.utilitydive.com/news/court-trump-wind-solar-permitting/818152/"),
    "Gas pipeline expansion": ("EIA emission factors; author calculation",
                               "https://www.eia.gov/environment/emissions/co2_vol_mass.php"),
    "Onshore oil and gas drilling": (
        "Resources for the Future (Prest, 2024)",
        "https://www.rff.org/publications/issue-briefs/federal-permitting-reform-expand-oil-and-gas-leasing-carbon-emissions/"),
}
NOTES = [
    "Scale ratings are the author's qualitative judgments of how much each provision could change US "
    "emissions; the bill has not been modeled. Numbers are context anchors, not estimates of the bill's effect.",
    "'Helps' reflects who faces federal obstacles and most NEPA reviews today; neutral provisions can "
    "protect either side under future administrations.",
    "Wind/solar anchor assumes a 25-35% capacity factor and 0.35-0.50 tCO2/MWh displaced.",
    "Also in the bill: faster Endangered Species Act consultations and limits on challenges "
    "(secs. 1302-1305), which cut both ways.",
    "Not in this bill (unlike the 2024 Manchin-Barrasso bill): mandatory oil and gas lease sales, coal "
    "leasing, or an LNG-specific export deadline (general permit clocks could still reach DOE). The July "
    "2025 budget law already mandated oil, gas and coal leasing; DOE lifted the LNG export pause in Jan. 2025.",
]
SOURCES = [
    ("Bill text (Senate draft, Sept. 30, 2026)",
     "https://www.energy.senate.gov/wp-content/uploads/2026/09/Bipartisan-American-Affordability-and-Jobs-Act.pdf"),
    ("Princeton REPEAT, transmission and the IRA (2022)", "https://zenodo.org/records/7106176"),
    ("Bennon & Wilson, NEPA litigation over large energy and transport projects (ELR, 2023)",
     "https://www.elr.info/sites/default/files/files-general/53.10836.pdf"),
    ("Resources for the Future, federal leasing and global emissions (2024)",
     "https://www.rff.org/publications/issue-briefs/federal-permitting-reform-expand-oil-and-gas-leasing-carbon-emissions/"),
    ("Utility Dive on Renew Northeast v. DOI (Apr. 2026)",
     "https://www.utilitydive.com/news/court-trump-wind-solar-permitting/818152/"),
]
CREDIT = "Zeke Hausfather, The Climate Brink"


def plain(s):
    """Strip matplotlib mathtext and line breaks for text output."""
    s = s.replace("CO$_2$", "CO₂").replace("\n", " ")
    s = re.sub(r"-\s+", "-", s) if "water-\n" in s else s
    return s.replace("water- quality", "water-quality").strip()


def rows():
    out = []
    for group, rs in ig.GROUPS:
        for r in rs:
            src, url = ANCHOR_SOURCE.get(r["name"], ("", ""))
            out.append({
                "group": group,
                "provision": r["name"],
                "bill_sections": r["sec"],
                "what_it_does": plain(r["what"]),
                "helps": ig.LEAN[r["lean"]][1].title(),
                "emissions_direction": r["dlab"],
                "emissions_scale": SCALE_MEANING[r["scale"]],
                "context_anchor": plain(r["anchor"]) if r["anchor"] else "",
                "anchor_source": src,
                "anchor_source_url": url,
            })
    return out


def write_csv(data, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        w.writeheader(); w.writerows(data)
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(data[0].keys()))
    w.writeheader(); w.writerows(data)
    return buf.getvalue()


def chip(helps):
    return f'<span class="chip chip-{helps.lower()}">{helps.upper()}</span>'


def em_cell(r):
    d = r["emissions_direction"]
    cls = "down" if d.startswith("Lowers") else ("up" if ("aise" in d) else "both")
    arrow = {"down": "↓", "up": "↑", "both": "↕"}[cls]
    n = {"large": 3, "moderate": 2, "small": 1}.get(r["emissions_scale"].split(" ")[0], 0)
    dots = "".join(f'<span class="dot{" on" if i < n else ""}"></span>' for i in range(3)) if n else ""
    scale = r["emissions_scale"].split(" (")[0]
    return (f'<div class="em em-{cls}"><strong>{arrow} {html.escape(d)}</strong>'
            f'<span class="scale">{dots}<span>{html.escape(scale)}</span></span></div>')


def build_html(data, csv_text):
    body_rows = []
    group = None
    for r in data:
        if r["group"] != group:
            group = r["group"]
            body_rows.append(f'<tr class="grp"><th colspan="4" scope="colgroup">{html.escape(group)}</th></tr>')
        anchor = ""
        if r["context_anchor"]:
            src = (f' <a href="{r["anchor_source_url"]}" target="_blank" rel="noopener">'
                   f'source</a>') if r["anchor_source_url"] else ""
            anchor = f'<p class="anchor">→ {html.escape(r["context_anchor"])}{src}</p>'
        body_rows.append(
            "<tr>"
            f'<td class="prov"><strong>{html.escape(r["provision"])}</strong>'
            f'<span class="sec">{html.escape(r["bill_sections"])}</span></td>'
            f'<td class="what"><p>{html.escape(r["what_it_does"])}</p>{anchor}</td>'
            f'<td class="helps">{chip(r["helps"])}</td>'
            f'<td>{em_cell(r)}</td>'
            "</tr>")
    notes = "".join(f"<li>{html.escape(n)}</li>" for n in NOTES)
    sources = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{html.escape(t)}</a></li>'
                      for t, u in SOURCES)
    from PIL import Image
    img_w, img_h = Image.open("permitting_infographic_social.png").size
    return TEMPLATE.format(img_w=img_w, img_h=img_h, rows="\n".join(body_rows), notes=notes, sources=sources,
                           csv=html.escape(csv_text), credit=html.escape(CREDIT))


TEMPLATE = """<title>Senate Permitting Deal Scorecard</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,600;0,700;1,400&display=swap">
<style>
/* Layout: one reading column (~72ch) with a full-width scorecard table; notes and data below. */
:root {{
  --bg: #fbfbf9; --panel: #f0efeb; --ink: #1a1a19; --ink2: #4f4c48; --ink3: #6f6c67;
  --rule: #e2e0da; --clean: #2a78d6; --fossil: #d03b3b; --both: #6f6d68; --on-chip: #ffffff;
  --sans: "IBM Plex Sans", "Helvetica Neue", Arial, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #171716; --panel: #232321; --ink: #f3f2ee; --ink2: #c9c6be; --ink3: #9d9a92;
  --rule: #35342f; --clean: #4b93e8; --fossil: #e26464; --both: #8d8a83; --on-chip: #0f0f0e; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #171716; --panel: #232321; --ink: #f3f2ee; --ink2: #c9c6be; --ink3: #9d9a92;
  --rule: #35342f; --clean: #4b93e8; --fossil: #e26464; --both: #8d8a83; --on-chip: #0f0f0e; color-scheme: dark }}
body {{ background: var(--bg); color: var(--ink); font: 16px/1.5 var(--sans); }}
.wrap {{ max-width: 1040px; margin: 0 auto; padding-inline: 20px; padding-block: 40px 56px; display: grid; gap: 28px; }}
header {{ display: grid; gap: 8px; }}
h1 {{ font-size: clamp(1.7rem, 4vw, 2.4rem); line-height: 1.15; margin: 0; text-wrap: balance; }}
.dek {{ font-size: 1.15rem; color: var(--ink2); margin: 0; max-width: 68ch; }}
.meta {{ font-size: .9rem; color: var(--ink3); margin: 0; }}
.key {{ display: flex; flex-wrap: wrap; gap: 10px 22px; align-items: center; font-size: .92rem; color: var(--ink2); }}
.key b {{ color: var(--ink); }}
.tablebox {{ overflow-x: auto; border-top: 2px solid var(--ink3); }}
table {{ width: 100%; min-width: 760px; border-collapse: collapse; }}
thead th {{ text-align: left; font-size: .75rem; letter-spacing: .08em; text-transform: uppercase; color: var(--ink3); padding: 10px 12px 8px; }}
tr.grp th {{ text-align: left; font-size: .8rem; letter-spacing: .08em; text-transform: uppercase; color: var(--ink2); padding: 22px 12px 6px; }}
td {{ vertical-align: top; padding: 12px; border-bottom: 1px solid var(--rule); }}
td.prov {{ width: 26%; }}
td.prov strong {{ display: block; font-size: 1.05rem; line-height: 1.3; }}
.sec {{ font-family: var(--mono); font-size: .8rem; color: var(--ink3); }}
td.what p {{ margin: 0; color: var(--ink2); }}
p.anchor {{ margin-top: 6px !important; color: var(--ink) !important; font-style: italic; font-size: .93rem; }}
p.anchor a {{ font-style: normal; color: var(--ink3); }}
td.helps {{ width: 90px; }}
.chip {{ display: inline-block; padding: 3px 10px; border-radius: 6px; color: var(--on-chip); font-weight: 700; font-size: .78rem; letter-spacing: .04em; }}
.chip-clean {{ background: var(--clean); }} .chip-fossil {{ background: var(--fossil); }} .chip-both {{ background: var(--both); }}
.em {{ display: grid; gap: 4px; min-width: 170px; }}
.scale {{ display: flex; align-items: center; gap: 5px; color: var(--ink2); font-size: .92rem; }}
.scale > span:last-child {{ margin-left: 6px; }}
.dot {{ width: 12px; height: 12px; border-radius: 50%; border: 2px solid currentColor; box-sizing: border-box; }}
.dot.on {{ background: currentColor; }}
.em-down .scale .dot {{ color: var(--clean); }} .em-up .scale .dot {{ color: var(--fossil); }} .em-both .scale .dot {{ color: var(--both); }}
section h2 {{ font-size: 1.15rem; margin: 0 0 8px; }}
section ul {{ margin: 0; padding-left: 1.2em; display: grid; gap: 6px; color: var(--ink2); max-width: 80ch; }}
a {{ color: var(--clean); }}
a:focus-visible, button:focus-visible, textarea:focus-visible {{ outline: 3px solid var(--clean); outline-offset: 2px; }}
.data {{ background: var(--panel); border-radius: 10px; padding: 18px; display: grid; gap: 10px; }}
.data p {{ margin: 0; color: var(--ink2); }}
.data .row {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }}
button, .btn {{ display: inline-block; text-decoration: none; font: 600 .95rem var(--sans); padding: 8px 14px; border-radius: 8px; border: 1px solid var(--ink3); background: var(--bg); color: var(--ink); cursor: pointer; }}
#status {{ font-size: .9rem; color: var(--ink3); }}
textarea {{ width: 100%; box-sizing: border-box; min-height: 180px; font: .8rem/1.45 var(--mono); color: var(--ink); background: var(--bg); border: 1px solid var(--rule); border-radius: 8px; padding: 10px; resize: vertical; }}
footer {{ font-size: .9rem; color: var(--ink3); }}
.fig img {{ display: block; width: 100%; max-width: 640px; height: auto; border: 1px solid var(--rule); border-radius: 8px; }}
</style>

<div class="wrap">
  <header>
    <h1>What's in the Senate permitting deal, and what it could mean for US emissions</h1>
    <p class="dek">A provision-by-provision scorecard of the Bipartisan American Affordability and Jobs Act of 2026: who each part helps today, and the likely direction and rough scale of its effect on US emissions.</p>
    <p class="meta">Senate draft of Sept. 30, 2026 · Analysis by {credit}</p>
  </header>

  <div class="key" aria-label="Emissions scale key">
    <b>Emissions scale (author judgment):</b>
    <span>small &lt;10</span><span>moderate 10–100</span><span>large &gt;100 MtCO₂/yr</span>
    <span>Dots are blue if a provision lowers emissions, red if it raises them, gray if either way.</span>
  </div>

  <div class="tablebox">
    <table>
      <thead><tr><th scope="col">Provision</th><th scope="col">What it does</th><th scope="col">Helps</th><th scope="col">Emissions</th></tr></thead>
      <tbody>
{rows}
      </tbody>
    </table>
  </div>

  <section>
    <h2>Notes</h2>
    <ul>{notes}</ul>
  </section>

  <section class="data" aria-labelledby="data-h">
    <h2 id="data-h">Reuse the data</h2>
    <p>The same table as CSV, one row per provision. Paste it into a spreadsheet or Datawrapper. Please credit {credit}.</p>
    <div class="row"><button id="copy" type="button">Copy CSV</button><span id="status" role="status"></span></div>
    <textarea id="csv" readonly aria-label="CSV data">{csv}</textarea>
  </section>

  <section class="fig">
    <h2>The graphic</h2>
    <img src="permitting_infographic_social.png" width="{img_w}" height="{img_h}" loading="lazy" alt="Scorecard graphic of the Senate permitting deal: provisions grouped as mostly helping clean energy, cutting both ways, or mostly helping fossil fuels, each with its likely emissions direction and scale, matching the table above.">
  </section>

  <section>
    <h2>Sources</h2>
    <ul>{sources}</ul>
  </section>

  <footer>Ratings are qualitative and reflect the Senate draft as released; they may change with the manager's amendment.</footer>
</div>

<script>
(function () {{
  var btn = document.getElementById('copy'), ta = document.getElementById('csv'), st = document.getElementById('status');
  btn.addEventListener('click', function () {{
    function fallback() {{ ta.focus(); ta.select(); st.textContent = 'Selected. Press Ctrl+C or Cmd+C to copy.'; }}
    try {{
      navigator.clipboard.writeText(ta.value).then(function () {{ st.textContent = 'Copied to clipboard.'; }}, fallback);
    }} catch (e) {{ fallback(); }}
  }});
}})();
</script>
"""


SITE_URL = "https://hausfath.github.io/permitting-scorecard-2026/"
DATA_ARTIFACT = """  <section class="data" aria-labelledby="data-h">
    <h2 id="data-h">Reuse the data</h2>
    <p>The same table as CSV, one row per provision. Paste it into a spreadsheet or Datawrapper. Please credit {credit}.</p>
    <div class="row"><button id="copy" type="button">Copy CSV</button><span id="status" role="status"></span></div>
    <textarea id="csv" readonly aria-label="CSV data">{csv}</textarea>
  </section>"""
DATA_SITE = """  <section class="data" aria-labelledby="data-h">
    <h2 id="data-h">Data</h2>
    <p>The same table as a CSV file, one row per provision. Please credit {credit}.</p>
    <div class="row"><a class="btn" href="permitting_provisions.csv" download>Download CSV</a></div>
  </section>"""


def build_site(data, csv_text):
    """Standalone page for GitHub Pages: full document, CSV download link, no script."""
    page = build_html(data, csv_text)
    art = DATA_ARTIFACT.format(credit=html.escape(CREDIT), csv=html.escape(csv_text))
    assert art in page, "data block not found"
    page = page.replace(art, DATA_SITE.format(credit=html.escape(CREDIT)))
    page = page[:page.index("<script>")].rstrip() + "\n"
    title_end = page.index("</title>") + len("</title>")
    title = page[:title_end]
    rest = page[title_end:]
    desc = ("Provision-by-provision scorecard of the 2026 Senate permitting deal: who each part helps "
            "and its likely effect on US emissions. By " + CREDIT + ".")
    head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{title}
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="What's in the Senate permitting deal">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE_URL}">
<meta property="og:image" content="{SITE_URL}permitting_infographic_social.png">
<meta name="twitter:card" content="summary_large_image">
"""
    style_end = rest.index("</style>") + len("</style>")
    head_rest, body = rest[:style_end], rest[style_end:]
    head_rest = head_rest.replace("body {{", "body {{").replace(
        "body { background: var(--bg);", "body { margin: 0; background: var(--bg);")
    return head + head_rest + "\n</head>\n<body>" + body + "</body>\n</html>\n"


if __name__ == "__main__":
    import os
    data = rows()
    csv_text = write_csv(data, "permitting_provisions.csv")
    os.makedirs("share", exist_ok=True)
    import shutil
    shutil.copy("permitting_infographic_social.png", "share/permitting_infographic_social.png")
    with open("share/index.html", "w", encoding="utf-8") as f:
        f.write(build_html(data, csv_text))
    with open("index.html", "w", encoding="utf-8") as f:   # GitHub Pages site root
        f.write(build_site(data, csv_text))
    print(f"wrote permitting_provisions.csv ({len(data)} rows), share/index.html, index.html")
    for d in data:
        print(" -", d["provision"], "|", d["helps"], "|", d["emissions_direction"], "|", d["context_anchor"][:70])
