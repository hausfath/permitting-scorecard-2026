"""Phase 2: 2010-2024 era-split recount + CGEP-timing Mt-years.
Reads ../projects_sized.csv (Phase 1, 2010-17 FEISs from the 2018 workbook; unchanged) and phase2/projects_sized2.csv
(new EISs from the 2010-2024 workbook), computes per-project MtCO2/yr with ../recount.py's em() (plus Phase-2 methods),
ONE Monte Carlo over all projects (shared factors drawn once per draw), and aggregates by era:
  2010-16, 2017-20, 2021-24, 2010-18 (= Phase 1 set, unchanged), 2010-24 pooled (dup_pooled zeroed).
Then Mt-years brought forward = months_saved/12 x Mt/yr using the CGEP join (phase2/cgep_join.csv).
Usage (from bw_recount/): python3.13 phase2/recount2.py [N]
"""
import os, sys
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT); os.chdir(ROOT)
import recount as R1
from factors import SHARED, MT_PER_BCFD, T_CO2_PER_BBL, LIT_RATE
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
OVR = {'CF_OW': (0.40, 0.40, 0.45)}   # PLAN: scorecard OW_CF 0.40-0.45; central at the less favorable end
LIT = dict(LIT_RATE, OffshoreWind=LIT_RATE['Wind'])   # B&W has no offshore wind; use onshore wind rate (flagged)

p1 = pd.read_csv('projects_sized.csv'); u1 = pd.read_csv('universe.csv')[['ceq_id', 'feis']]
p1 = p1.merge(u1, on='ceq_id', how='left'); p1['feis_year'] = pd.to_datetime(p1.feis).dt.year; p1['phase'] = 1; p1['dup_pooled'] = ''
p2 = pd.read_csv('phase2/projects_sized2.csv'); p2['phase'] = 2
P = pd.concat([p1, p2], ignore_index=True)
P['p'] = P.params.apply(R1.params)
P['era'] = np.where(P.feis_year <= 2016, '2010-16', np.where(P.feis_year <= 2020, '2017-20', '2021-24'))

def em2(r, f, n, central=False, opt=None):
    m = r.method; z = np.zeros(n)
    if (opt or {}).get('drop_fossil_continuation') and r.group == 'Fossil' and r.new_or_existing == 'continuation':
        return dict(usg=z, usn=z, glg=z, gln=z)
    if m in ('OVERLAP',):
        return dict(usg=z, usn=z, glg=z, gln=z)
    if m == 'PIPEOIL_EXPORT':
        v = R1.size_draw(r, n, central, (opt or {}).get('built', False))
        g = v * 365 * T_CO2_PER_BBL / 1e6 * f['U_PIPE']
        return dict(usg=z, usn=z, glg=g, gln=g * f['NET_MIDSTREAM_OIL'])
    return R1.em(r, f, n, central, opt)

def run(n, central=False, opt=None, overrides=None):
    f = R1.draw_shared(n, central, {**OVR, **(overrides or {})})
    return {r.ceq_id: em2(r, f, n, central, opt) for r in P.itertuples()}

SETS = {
    '2010-16': lambda d: d.era == '2010-16',
    '2017-20': lambda d: d.era == '2017-20',
    '2021-24': lambda d: d.era == '2021-24',
    '2010-18 (Phase 1)': lambda d: d.phase == 1,
    '2010-24 pooled': lambda d: ~d.dup_pooled.fillna('').astype(bool),
}
KEY = {('US', 'net'): 'usn', ('US', 'gross'): 'usg', ('global', 'net'): 'gln', ('global', 'gross'): 'glg'}
def cells(E, n, weight=None, mult=None, label=''):
    out = []
    for sname, sel in SETS.items():
        d = P[sel(P) & P.group.isin(['Clean', 'Fossil'])]
        for tx in (True, False):
            dd = d if tx else d[d.subsector != 'Transmission']
            for (sc, ba), k in KEY.items():
                cl = np.zeros(n); fo = np.zeros(n)
                for r in dd.itertuples():
                    w = 1.0 if weight is None else weight(r)
                    x = w * (E[r.ceq_id][k] if mult is None else E[r.ceq_id][k] * mult(r))
                    if r.group == 'Clean': cl = cl + x
                    else: fo = fo + x
                net = fo - cl
                ratio = cl / np.where(fo == 0, np.nan, fo)
                out.append(dict(case=label, set=sname, transmission='in' if tx else 'out', scope=sc, basis=ba,
                    n_clean=int((dd.group == 'Clean').sum()), n_fossil=int((dd.group == 'Fossil').sum()),
                    clean_p50=np.median(cl), clean_p05=np.percentile(cl, 5), clean_p95=np.percentile(cl, 95),
                    fossil_p50=np.median(fo), fossil_p05=np.percentile(fo, 5), fossil_p95=np.percentile(fo, 95),
                    ratio_p50=np.nanmedian(ratio), ratio_p05=np.nanpercentile(ratio, 5), ratio_p95=np.nanpercentile(ratio, 95),
                    net_p50=np.median(net), net_p05=np.percentile(net, 5), net_p95=np.percentile(net, 95),
                    p_fossil_gt_clean=float(np.mean(fo > cl)), sign='RAISES' if np.median(net) > 0 else 'LOWERS'))
    return out

if __name__ == '__main__':
    Ec = run(1, central=True); E = run(N)
    rows = cells(Ec, 1, label='central') + cells(E, N, label='mc') + cells(E, N, weight=lambda r: LIT.get(r.subsector, 0.0), label='mc_litigation')
    for name, kw in {'projects_only_mc': None, 'built_only_mc': dict(built=True), 'credit_existing_mc': dict(credit_existing=True),
                     'pipe_net_EIA_0.23_mc': 'pipeEIA', 'drop_fossil_continuations_mc': dict(drop_fossil_continuation=True), 'pipe_net_ICF_-0.075_mc': 'pipeICF', 'MER_cambium_mc': 'mer'}.items():
        if name == 'projects_only_mc':
            E2 = E; keep = P.programmatic.astype(bool)
            rows += cells({i: (v if not keep[P.ceq_id == i].iloc[0] else {k: v[k] * 0 for k in v}) for i, v in E.items()}, N, label=name)
        elif kw == 'pipeEIA': rows += cells(run(N, overrides={'NET_PIPE': 0.23}), N, label=name)
        elif kw == 'pipeICF': rows += cells(run(N, overrides={'NET_PIPE': -0.075}), N, label=name)
        elif kw == 'mer': rows += cells(run(N, overrides={'MER': (0.10, 0.20, 0.30)}), N, label=name)
        else:
            E2 = run(N, opt=kw)
            if name == 'built_only_mc':
                keep = P.programmatic.astype(bool)
                E2 = {i: (v if not keep[P.ceq_id == i].iloc[0] else {k: v[k] * 0 for k in v}) for i, v in E2.items()}
            rows += cells(E2, N, label=name)
    C = pd.DataFrame(rows); C.to_csv('phase2/results2_cells.csv', index=False)
    # per-project table (phase 2 additions only; phase 1 already in ../projects.csv)
    pr = P[P.phase == 2].drop(columns=['p']).copy()
    for k in ['usg', 'usn', 'glg', 'gln']:
        pr[f'em_{k}_central'] = [float(Ec[i][k][0]) for i in pr.ceq_id]
        pr[f'em_{k}_p05'] = [float(np.percentile(E[i][k], 5)) for i in pr.ceq_id]
        pr[f'em_{k}_p95'] = [float(np.percentile(E[i][k], 95)) for i in pr.ceq_id]
    pr['litigation_rate_bw'] = pr.subsector.map(LIT)
    pr.to_csv('phase2/projects2.csv', index=False)

    # ---------------- Mt-years brought forward (CGEP timing) ----------------
    J = pd.read_csv('phase2/cgep_join.csv'); J = J[J.ceq_id.astype(str).str.len() > 0]
    TYPE = {'Pipeline': 'pipeline', 'Transmission': 'transmission', 'Solar': 'solar', 'Wind': 'wind', 'OffshoreWind': 'offshore', 'Geothermal': 'geothermal'}
    med = J.groupby('technology').months_saved_total.median().to_dict(); med_low = J.groupby('technology').months_saved_low.median().to_dict()
    raw = pd.read_csv('phase2/cgep_type_medians.csv').set_index('technology') if os.path.exists('phase2/cgep_type_medians.csv') else None
    ARCH = pd.read_csv('phase2/cgep_archetype_totals.csv').set_index('technology')
    mt = dict(zip(J.ceq_id, J.months_saved_total)); ml = dict(zip(J.ceq_id, J.months_saved_low))
    TECHMED = raw.months_saved_total.to_dict() if raw is not None else med
    TECHMED_LOW = raw.months_saved_low.to_dict() if raw is not None else med_low
    pipe_med = TECHMED['pipeline']; max_med = max(TECHMED.values())
    def months(r, col='total', uncovered=0.0, impute_unmatched=True, uplift=False):
        t = TYPE.get(r.subsector)
        if t is None:
            mo = uncovered
            if uplift and uncovered > 0:
                pass
            return mo
        d = mt if col == 'total' else ml
        if r.ceq_id in d: mo = d[r.ceq_id]
        elif impute_unmatched: mo = (TECHMED if col == 'total' else TECHMED_LOW)[t]
        else: mo = 0.0
        if uplift:
            mo = mo + LIT.get(r.subsector, 0) * (ARCH.loc[t, 'contested_total'] - ARCH.loc[t, 'smooth_total'])
        return mo
    out = []
    for label, kw in {
        'covered_matched_only': dict(impute_unmatched=False),
        'covered_types (unmatched at type median)': dict(),
        'uncovered=0': dict(uncovered=0.0),
        f'uncovered=pipeline median ({pipe_med:.1f} mo)': dict(uncovered=pipe_med),
        f'uncovered=max CGEP type median ({max_med:.1f} mo)': dict(uncovered=max_med),
        'months_saved_low (uncovered=0)': dict(col='low'),
        'litigated uplift (uncovered=0)': dict(uplift=True),
        f'litigated uplift (uncovered=pipeline median)': dict(uplift=True, uncovered=pipe_med),
    }.items():
        covered_only = label.startswith('covered')
        mult = lambda r, kw=kw: (months(r, **kw) / 12.0) if (not covered_only or r.subsector in TYPE) else 0.0
        for row in cells(E, N, mult=mult, label='mtyears: ' + label):
            out.append(row)
        for row in cells(Ec, 1, mult=mult, label='mtyears_central: ' + label):
            out.append(row)
    M = pd.DataFrame(out); M.to_csv('phase2/results2_mtyears.csv', index=False)
    # coverage shares (central, pooled)
    cov = []
    d = P[SETS['2010-24 pooled'](P) & P.group.isin(['Clean', 'Fossil'])]
    for k in ['usn', 'gln']:
        for g in ['Clean', 'Fossil']:
            s = d[d.group == g]
            tot = sum(max(Ec[i][k][0], 0) for i in s.ceq_id)
            typ = sum(max(Ec[i][k][0], 0) for i in s.ceq_id if s.set_index('ceq_id').loc[i, 'subsector'] in TYPE)
            mat = sum(max(Ec[i][k][0], 0) for i in s.ceq_id if i in mt)
            cov.append(dict(metric=k, group=g, total=tot, share_covered_type=typ / tot if tot else np.nan, share_matched_project=mat / tot if tot else np.nan))
    pd.DataFrame(cov).to_csv('phase2/results2_cgep_coverage.csv', index=False)
    print(pd.DataFrame(cov).round(3).to_string())
