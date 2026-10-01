"""
Infographic: main provisions of the Bipartisan American Affordability and Jobs
Act of 2026 (Senate draft, Sept 30 2026) and their likely emissions direction.

This is a qualitative table, not a data chart. "Helps" and "scale" are author
judgments documented in METHODS.md; the only numbers shown are anchors that are
computed in anchors() below or quoted from a cited source.

Color: diverging blue (clean-leaning) / red (fossil-leaning) with a neutral
gray midpoint ("both"). Poles validated with the dataviz validator (CVD dE 23.8,
normal 31.6, both >= 3:1 on surface). Every chip carries a text label, so lean
is never encoded by color alone.

Designed standalone (no reference to an accompanying post). Body text is sized
at roughly 2% of image width so it stays legible when opened on a phone.

Outputs (1800 px wide): permitting_infographic.png (for the post, with the
"Not in this bill" box) and permitting_infographic_social.png (without it).
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

SURFACE = "#fcfcfb"
INK, INK2, INK3 = "#1a1a19", "#4f4c48", "#6f6c67"
RULE = "#e4e2dd"
LEAN = {  # color, chip label
    "clean":  ("#2a78d6", "CLEAN"),
    "both":   ("#6f6d68", "BOTH"),
    "fossil": ("#d03b3b", "FOSSIL"),
}
ARROW = {"down": "↓", "up": "↑", "depends": "↕"}
# Emissions pips colored by direction (not by who benefits): lowers = blue,
# raises = red, either way = gray. Text labels carry the meaning too.
EM_COL = {"down": LEAN["clean"][0], "up": LEAN["fossil"][0], "depends": LEAN["both"][0]}
SCALE = {3: "large", 2: "moderate", 1: "small", 0: "unknown"}

MER = (0.35, 0.50)   # ASSUMED marginal emission rate displaced, tCO2/MWh


def anchors():
    """Numbers shown on the graphic (or in the post), computed here."""
    # Wind/solar capacity canceled or at material risk from federal actions:
    # 57.2 GW, Charles River Associates report cited in Renew Northeast v. DOI
    # (D. Mass., PI of Apr 21 2026), per Utility Dive. Includes some offshore.
    ws_gw = 57.2
    ws_cf = (0.25, 0.35)       # ASSUMED blended solar/wind capacity factor
    ws_twh = [ws_gw * c * 8.76 for c in ws_cf]
    ws_mt = (ws_twh[0] * MER[0], ws_twh[1] * MER[1])
    # Five offshore wind projects paused Dec 22 2025 (nameplate GW); used in post.
    ow = {"CVOW": 2.6, "Sunrise": 0.924, "Vineyard 1": 0.806,
          "Revolution": 0.704, "Empire 1": 0.81}
    ow_gw = sum(ow.values())
    ow_twh = [ow_gw * c * 8.76 for c in (0.40, 0.45)]   # ASSUMED CF
    ow_mt = (ow_twh[0] * MER[0], ow_twh[1] * MER[1])
    # Gas pipeline: 1 Bcf/d fully utilized, EIA 53.06 kg CO2/MMBtu, 1.036 MMBtu/Mcf
    mt_per_bcfd = 1e6 * 53.06 * 1.036 * 365 / 1e9
    # Interconnection queue, end of 2025 (LBNL Queued Up 2026 edition), GW active.
    q = {"solar": 773, "storage": 749, "wind": 220, "gas": 253}
    q_total = 2061                     # LBNL total active capacity (generation + storage)
    q_clean_share = (q["solar"] + q["storage"] + q["wind"]) / q_total
    q_gas_share = q["gas"] / q_total
    q_median_months = 61               # median request-to-operation, projects built in 2025
    return {"q_total": q_total, "q_clean_share": q_clean_share, "q_gas_share": q_gas_share,
            "q_months": q_median_months, "ws_gw": ws_gw, "ws_mt": ws_mt, "ow_gw": ow_gw, "ow_mt": ow_mt,
            "pipe_mt": mt_per_bcfd}




A = anchors()
CO2 = "CO$_2$"
LO, HI = A["ws_mt"]

GROUPS = [
    ("Mostly helps clean energy", [
        dict(name="Transmission", sec="§§2101–2105, 2109",
             what="FERC backstop siting without a DOE corridor; interregional planning",
             lean="clean", dir="down", dlab="Lowers", scale=3,
             anchor="If transmission grew only ~1%/yr, >80% of the IRA’s potential "
                    "2030 cuts would be lost (REPEAT, 2022)"),
        dict(name="Interconnection queues", sec="§§2106, 2110, 2111",
             what="Planned zones with fixed connection costs; faster, automated studies",
             lean="clean", dir="down", dlab="Lowers", scale=2,
             anchor=f"~{A['q_clean_share']*100:.0f}% of the {A['q_total']:,} GW waiting to connect is "
                    f"solar, wind and storage; median wait {A['q_months']} months (LBNL)"),
        dict(name="Renewables and geothermal", sec="§§2213–2214, 2221–2228",
             what="Faster decisions on public land; annual geothermal lease sales",
             lean="clean", dir="down", dlab="Lowers", scale=1, anchor=None),
        dict(name="Historic-preservation reviews", sec="§2301",
             what="Visual impacts on historic sites mostly no longer count as ‘adverse’",
             lean="clean", dir="down", dlab="Lowers", scale=1, anchor=None),
        dict(name="Offshore wind leasing", sec="§§2251–2252",
             what="Looser ‘interference with other uses’ test; preferred cable routes",
             lean="clean", dir="down", dlab="Lowers", scale=1, anchor=None),
    ]),
    ("Cuts both ways", [
        dict(name="NEPA deadlines and lawsuit limits", sec="§§1106, 1110, 2201",
             what="Tighter review deadlines; 150 days to sue; courts can’t cancel permits",
             lean="both", dir="down", dlab="Lowers, on net", scale=2,
             anchor="Clean projects outnumbered fossil 2.4:1 in 2010–18 energy EISs "
                    "and 2:1 in lawsuits (Bennon & Wilson)"),
        dict(name="Permit certainty and deadlines", sec="§§1401, 1402(c), 1403",
             what="Protects issued permits; forces decisions on stalled non-NEPA permits",
             lean="both", dir="down", dlab="Lowers, for now", scale=2,
             anchor=f"{A['ws_gw']:.0f} GW of wind, solar and hybrid canceled or delayed by "
                    f"federal actions (plaintiffs’ est.): {LO:.0f}–{HI:.0f} Mt{CO2}/yr if built"),
        dict(name="Damages for permit discrimination", sec="§1402",
             what="Large damages if agencies intentionally delay or deny a project type",
             lean="both", dir="depends", dlab="Either way", scale=0, anchor=None),
    ]),
    ("Mostly helps fossil fuels", [
        dict(name="Gas pipeline expansion", sec="§§2102(b), 1202, 1204",
             what="Looping and compression in existing corridors skip NEPA; state water-\n"
                  "quality vetoes narrowed, federal wetland permits eased (helps power lines too)",
             lean="fossil", dir="up", dlab="Likely raises", scale=2,
             anchor=f"Each 1 Bcf/d of added capacity ≈ {A['pipe_mt']:.0f} Mt{CO2}/yr "
                    "if fully used (gross)"),
        dict(name="Onshore oil and gas drilling", sec="§§2211, 2229",
             what="No federal permit for many private-land wells; broader NEPA exemptions",
             lean="fossil", dir="up", dlab="Raises", scale=1,
             anchor="Output is set mostly by prices; ~57% of added federal oil displaces "
                    "production elsewhere (RFF)"),
    ]),
]

# ---------------------------------------------------------------- layout
plt.rcParams["font.family"] = ["Arial", "DejaVu Sans"]  # DejaVu supplies arrows
W = 12
LINE = 0.3                      # height of one extra description line
ROW_BASE, ANCHOR_ADD, GROUP_H = 1.06, 0.36, 0.66


def row_h(r):
    return ROW_BASE + LINE * r["what"].count("\n") + (ANCHOR_ADD if r["anchor"] else 0)


BOX_H = 1.72   # "Not in this bill" box incl. gap above

def render(show_box, out):
    H = 3.65 + len(GROUPS) * GROUP_H + sum(row_h(r) for _, rs in GROUPS for r in rs) + 3.45 - (0 if show_box else BOX_H)

    fig = plt.figure(figsize=(W, H), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    renderer = fig.canvas.get_renderer()

    L, R = 0.5, W - 0.5
    X_LEAN, X_EM = 8.55, 9.55


    def pips(x, yc, n, color, r=0.1, gap=0.3):
        for i in range(3):
            ax.add_patch(Circle((x + i * gap, yc), r,
                                facecolor=color if i < n else SURFACE,
                                edgecolor=color, lw=1.8))


    def text_right_edge(t):
        bb = t.get_window_extent(renderer=renderer)
        return ax.transData.inverted().transform((bb.x1, bb.y0))[0]


    y = H - 0.5
    ax.text(L, y, "What’s in the Senate permitting deal", fontsize=30,
            fontweight="bold", color=INK, va="top")
    y -= 0.68
    ax.text(L, y, "…and what it could mean for US emissions", fontsize=21,
            color=INK2, va="top")
    y -= 0.58
    ax.text(L, y, "Bipartisan American Affordability and Jobs Act of 2026 "
            "(Senate draft, Sept. 30, 2026)", fontsize=14, color=INK3, va="top")

    # scale key
    y -= 0.78
    t = ax.text(L, y, "Emissions scale (author judgment):", fontsize=14, color=INK2,
                va="center", fontweight="bold")
    kx = text_right_edge(t) + 0.3
    for n, lab in [(1, "small <10"), (2, "moderate 10–100"),
                   (3, f"large >100 Mt{CO2}/yr")]:
        pips(kx, y, n, INK, r=0.075, gap=0.22)
        t = ax.text(kx + 0.7, y, lab, fontsize=14, color=INK2, va="center")
        kx = text_right_edge(t) + 0.35

    # column headers
    y -= 0.62
    for x, lab, ha in [(L, "PROVISION", "left"), (X_LEAN, "HELPS", "center"),
                       (X_EM, "EMISSIONS", "left")]:
        ax.text(x, y, lab, fontsize=12.5, color=INK3, fontweight="bold",
                va="center", ha=ha)
    y -= 0.24
    ax.plot([L, R], [y, y], color=INK3, lw=1.3)

    for gname, rows in GROUPS:
        y -= GROUP_H
        ax.text(L, y + 0.24, gname.upper(), fontsize=14, fontweight="bold",
                color=INK2, va="center")
        for r in rows:
            h = row_h(r)
            top = y - 0.04
            col, chip = LEAN[r["lean"]]
            t = ax.text(L, top, r["name"], fontsize=20, fontweight="bold",
                        color=INK, va="top")
            ax.text(text_right_edge(t) + 0.15, top - 0.06, r["sec"], fontsize=13,
                    color=INK3, va="top")
            ax.text(L, top - 0.44, r["what"], fontsize=16, color=INK2,
                    va="top", linespacing=1.3)
            if r["anchor"]:
                ya = top - 0.84 - LINE * r["what"].count("\n")
                ax.text(L, ya, "→ " + r["anchor"], fontsize=14,
                        color=INK, va="top", fontstyle="italic")
            yc = top - 0.22
            ax.add_patch(FancyBboxPatch((X_LEAN - 0.5, yc - 0.19), 1.0, 0.38,
                                        boxstyle="round,pad=0,rounding_size=0.09",
                                        facecolor=col, edgecolor="none"))
            ax.text(X_LEAN, yc, chip, fontsize=14, fontweight="bold",
                    color="white", ha="center", va="center")
            ax.text(X_EM, yc, f"{ARROW[r['dir']]} {r['dlab']}", fontsize=16,
                    color=INK, va="center", fontweight="bold")
            if r["scale"]:
                pips(X_EM + 0.12, yc - 0.46, r["scale"], EM_COL[r["dir"]])
                ax.text(X_EM + 0.98, yc - 0.46, SCALE[r["scale"]], fontsize=15,
                        color=INK2, va="center")
            else:
                ax.text(X_EM, yc - 0.46, "size unknown", fontsize=15,
                        color=INK2, va="center", fontstyle="italic")
            y -= h
            ax.plot([L, R], [y + 0.06, y + 0.06], color=RULE, lw=1.1)

    # not-in-bill box (omitted in the social version)
    if show_box:
        y -= 0.3
        bh = 1.42
        ax.add_patch(FancyBboxPatch((L, y - bh), R - L, bh,
                                    boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor="#f0efec", edgecolor="none"))
        ax.text(L + 0.25, y - 0.22, "Not in this bill (unlike the 2024 Manchin–Barrasso bill):",
                fontsize=16, fontweight="bold", color=INK, va="top")
        ax.text(L + 0.25, y - 0.64,
                "mandatory oil and gas lease sales, coal leasing, or an LNG-specific export deadline\n"
                "(general permit clocks could still reach DOE). The July 2025 budget law already "
                "mandated\noil, gas and coal leasing; DOE lifted the LNG export pause in Jan. 2025.",
                fontsize=15, color=INK2, va="top", linespacing=1.3)

    # footer
    foot = [
        "Also: faster Endangered Species Act consultations and limits on challenges "
        "(§§1302–1305), which cut both ways.",
        "‘Helps’ reflects who faces federal obstacles and most NEPA reviews today; "
        "neutral provisions can protect either side later.",
        "Numbers are context anchors, not estimates of the bill’s effect. Wind/solar "
        f"anchor assumes 25–35% capacity factor, {MER[0]:.2f}–{MER[1]:.2f} t{CO2}/MWh displaced.",
        "NEPA: federal environmental-review law · EIS: its most detailed review · "
        "FERC: federal grid regulator · Bcf/d: billion cubic feet/day",
    ]
    ax.text(L, 1.72, "\n".join(foot), fontsize=11.5, color=INK3, va="top",
            linespacing=1.5)
    ax.text(L, 0.62, "Sources: bill text; REPEAT (2022); Bennon & Wilson (2023); RFF (2024); LBNL (2026); "
            "CRA via Renew Northeast v. DOI; EIA; author calculations.",
            fontsize=11.5, color=INK3, va="top")
    ax.text(R, 0.3, "Zeke Hausfather · The Climate Brink", fontsize=12.5,
            color=INK3, va="top", ha="right")

    fig.savefig(out, dpi=150, facecolor=SURFACE)
    plt.close(fig)
    print("saved", out, f"{W*150:.0f}x{H*150:.0f}px")


if __name__ == "__main__":
    render(show_box=True, out="permitting_infographic.png")          # for the post
    render(show_box=False, out="permitting_infographic_social.png")  # for social media
    print("anchors:", {k: (tuple(round(x, 1) for x in v) if isinstance(v, tuple) else round(v, 3))
                       for k, v in A.items()})

