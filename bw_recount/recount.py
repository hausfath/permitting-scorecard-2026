"""Emissions-weighted recount of the CEQ 2010-18 energy EIS universe (B&W check included).
Reads projects_sized.csv (built by build_projects.py from universe.csv + sizes_spec.py), computes per-project
MtCO2/yr (clean = avoided, fossil = added) in four bases (US gross/net, global gross/net), aggregates exposure- and
litigation-weighted 2x2x2 cells, runs a Monte Carlo with shared factors drawn ONCE per draw, and writes:
  projects.csv, results_cells.csv, results_sensitivity.csv, results_concentration.csv, results_bw_check.csv
Usage: python3.13 recount.py [N_draws]
"""
import sys, os, json
import numpy as np, pandas as pd
from factors import *
HERE = os.path.dirname(os.path.abspath(__file__))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
RNG = np.random.default_rng(20261021)
P = pd.read_csv(os.path.join(HERE, 'projects_sized.csv'))
def params(s):
    out = {}
    if isinstance(s, str) and s:
        for kv in s.split(';'):
            k, v = kv.split('=', 1)
            try: out[k] = float(v)
            except ValueError: out[k] = v
    return out
P['p'] = P.params.apply(params)

def tri_ppf(q, a, c, b):
    a, c, b = float(a), float(c), float(b)
    if b <= a: return np.full_like(q, c, dtype=float)
    fc = (c - a) / (b - a)
    return np.where(q < fc, a + np.sqrt(q * (b - a) * (c - a)), b - np.sqrt((1 - q) * (b - a) * (b - c)))

def draw_shared(n, central=False, overrides=None):
    f = {}
    for k, (a, c, b) in SHARED.items():
        f[k] = np.full(n, c) if central else tri_ppf(RNG.random(n), a, c, b)
    for k, v in (overrides or {}).items():
        a, c, b = v if isinstance(v, tuple) else (v, v, v)
        f[k] = np.full(n, c) if central else tri_ppf(RNG.random(n), a, c, b)
    return f

def size_draw(r, n, central, use_built):
    if use_built:
        return np.full(n, float(r.built_size or 0))
    c = float(r.size_central)
    lo = r.size_low if pd.notna(r.size_low) and r.size_low != '' else None
    hi = r.size_high if pd.notna(r.size_high) and r.size_high != '' else None
    if lo is None and hi is None and r.size_imputed:
        lo, hi = 0.5 * c, 1.5 * c
    lo = float(lo) if lo is not None else c; hi = float(hi) if hi is not None else c
    if central or (lo == c and hi == c): return np.full(n, c)
    return tri_ppf(RNG.random(n), min(lo, c), c, max(hi, c))

def em(r, f, n, central=False, opt=None):
    """Return dict of arrays: usg, usn, glg, gln (MtCO2/yr, CO2e where noted).
    Programmatic EISs (clean RFD MW and fossil anticipated production) are scaled by the shared REAL_PROG factor."""
    out = _em(r, f, n, central, opt)
    if bool(r.programmatic) and 'REAL_PROG' in f:
        out = {k: v * f['REAL_PROG'] for k, v in out.items()}
    return out

def _em(r, f, n, central=False, opt=None):
    opt = opt or {}
    m, p = r.method, r.p
    z = np.zeros(n)
    # depletables: annualize over the documented production life where the EIS gives one (p['life']), else H_YEARS;
    # opt['H'] forces one horizon for all (sensitivity)
    H = opt['H'] if 'H' in opt else p.get('life', H_YEARS)
    v = size_draw(r, n, central, opt.get('built', False))
    meth = opt.get('methane', False)
    def ch4_mt_per_bcf(): return 1e6 * T_CH4_PER_MCF * LEAK_RATE * GWP100_CH4 / 1e6   # Mt CO2e per Bcf produced (~0.0132)
    if m in ('DUP', 'NOSIZE', 'ZERO', 'COVERED', 'OTHER'):
        return dict(usg=z, usn=z, glg=z, gln=z)
    if m == 'GEN':
        if r.new_or_existing == 'continuation' and not opt.get('credit_existing'):
            return dict(usg=z, usn=z, glg=z, gln=z)
        x = v * f['CF_' + p['tech']] * 8760 * f['MER'] / 1e6
        return dict(usg=x, usn=x, glg=x, gln=x)
    if m == 'HYDRO':
        mw = v + (p.get('existing_mw', 0) if opt.get('credit_existing') else 0)
        x = mw * f['CF_HYDRO'] * 8760 * f['MER'] / 1e6
        return dict(usg=x, usn=x, glg=x, gln=x)
    if m == 'PROGCLEAN':
        x = v * f['CF_' + p['tech']] * 8760 * f['MER'] / 1e6
        return dict(usg=x, usn=x, glg=x, gln=x)
    if m == 'TX':
        pu = p['purpose']
        if pu == 'renew': x = v * f['TX_ENABLE_RENEW'] * f['TX_CF'] * 8760 * f['MER'] / 1e6
        elif pu == 'hydroimport': x = v * f['TX_CF_HYDROIMPORT'] * f['HYDROIMPORT_ADDL'] * 8760 * f['MER'] / 1e6
        elif pu in ('reliab', 'overlap'): x = v * f['TX_ENABLE_RELIAB'] * f['TX_CF'] * 8760 * f['MER'] / 1e6
        elif pu == 'gentie_ext': x = v * f['CF_' + p['tech']] * 8760 * f['MER'] / 1e6
        else: raise ValueError(pu)
        return dict(usg=x, usn=x, glg=x, gln=x)
    if m == 'PIPEGAS':
        g = v * MT_PER_BCFD * f['U_PIPE']
        if meth: g = g + v * 365 * f['U_PIPE'] * ch4_mt_per_bcf()
        net = v * MT_PER_BCFD * f['NET_PIPE']
        if p.get('dest') == 'mex':
            return dict(usg=z, usn=z, glg=g, gln=net)
        return dict(usg=g, usn=net, glg=g, gln=net)
    if m == 'REGAS':
        g = v * MT_PER_BCFD * f['U_PIPE']
        if p.get('displaces') == 'oil':
            net = g * (KG_PER_MMBTU_GAS - KG_PER_MMBTU_RESID) / KG_PER_MMBTU_GAS
        else:
            net = v * MT_PER_BCFD * f['NET_PIPE']
        return dict(usg=g, usn=net, glg=g, gln=net)
    if m == 'KXL':
        glg = tri_ppf(RNG.random(n), 147, 157.5, 168) if not central else np.full(n, 157.5)
        gln = np.full(n, 27.4) if central else tri_ppf(RNG.random(n), *SHARED['KXL_NET'])
        usg = 0.83 * 365 * T_CO2_PER_BBL * f['US_SHARE_OIL']
        return dict(usg=usg, usn=gln * f['USSHARE_OGNET'], glg=glg, gln=gln)
    if m == 'PIPEPROD':
        g = v * 365 * T_CO2_PER_BBL / 1e6 * f['U_PIPE']
        net = g * f['NET_MIDSTREAM_OIL']
        return dict(usg=g, usn=net, glg=g, gln=net)
    if m == 'LNG':
        t = v * f['U_LNG']                                  # Mt LNG/yr
        mj = t * 1e6 * GJ_PER_T_LNG * 1e3                   # MJ/yr
        feed_mcf = t * 1e6 * MCF_FEED_PER_T_LNG
        usg = mj * f['LIQ_GMJ'] / 1e12 + feed_mcf * f['UPSTREAM_KG_MCF'] / 1e9
        if meth: usg = usg + feed_mcf / 1e3 * ch4_mt_per_bcf()
        usn = t * BCFD_PER_MTPA * f['LNG_US_NET_PER_BCFD']
        glg = mj * f['LNG_ATTR_GMJ'] / 1e12
        gln = mj * f['LNG_CONSEQ_GMJ'] / 1e12
        return dict(usg=usg, usn=usn, glg=glg, gln=gln)
    if m == 'COALLEASE':
        if r.new_or_existing == 'continuation' and opt.get('drop_fossil_continuation'):
            return dict(usg=z, usn=z, glg=z, gln=z)
        cum = v * T_CO2_PER_ST[p['rank']]                   # Mt CO2 over life (v in million short tons)
        a = cum / H
        return dict(usg=a * f['US_SHARE_COAL'], usn=a * f['US_SHARE_COAL'] * f['NET_COAL'], glg=a, gln=a * f['NET_COAL'])
    if m == 'PLANT':
        cf = f[p['cfkey']]
        if 'eis_mt' in p:
            g = p['eis_mt'] * cf / p['eis_cf']
        else:
            g = v * cf * 8760 * p['ef'] * (1 - p.get('capture', 0)) / 1e6
        disp = v * cf * 8760 * f['MER'] / 1e6
        if r.new_or_existing == 'continuation' and opt.get('drop_fossil_continuation'):
            return dict(usg=z, usn=z, glg=z, gln=z)
        return dict(usg=g, usn=g - disp, glg=g, gln=g - disp)
    if m == 'PLANTDELTA':
        g = v; disp = v / p['ef'] * f['MER']
        if opt.get('drop_fossil_continuation'): return dict(usg=z, usn=z, glg=z, gln=z)
        return dict(usg=g, usn=g - disp, glg=g, gln=g - disp)
    if m == 'OG':
        # cumulative oil (MMbbl) and gas (Bcf), common quantile for both components; annualized over H
        q = np.full(n, 0.5) if central else RNG.random(n)
        def comp(c, lo, hi):
            if central or (lo == c and hi == c): return np.full(n, c)
            return tri_ppf(q, min(lo, c), c, max(hi, c))
        oil = comp(p.get('oil', 0.0), p.get('oil_lo', p.get('oil', 0.0)), p.get('oil_hi', p.get('oil', 0.0)))
        gas = comp(p.get('gas', 0.0), p.get('gas_lo', p.get('gas', 0.0)), p.get('gas_hi', p.get('gas', 0.0)))
        if opt.get('built') and float(r.built_size or 0) == 0:
            oil, gas = oil * 0, gas * 0
        oil_mt = oil * T_CO2_PER_BBL / H                     # MMbbl * t/bbl = Mt
        gas_mt = gas * (MT_PER_BCFD / 365) / H
        meth_mt = gas * ch4_mt_per_bcf() / H if meth else 0
        glg = oil_mt + gas_mt + meth_mt
        usg = oil_mt * f['US_SHARE_OIL'] + gas_mt * f['US_SHARE_GAS'] + meth_mt
        gln = oil_mt * f['NET_OIL'] + gas_mt * f['NET_OIL'] * f['DISP_GAS'] + meth_mt * f['NET_OIL']
        usn = oil_mt * f['NET_OIL'] * f['USSHARE_OGNET'] + gas_mt * f['NET_OIL'] * f['DISP_GAS'] * f['USSHARE_GASNET'] + meth_mt * f['NET_OIL']
        return dict(usg=usg, usn=usn, glg=glg, gln=gln)
    raise ValueError(m)

CELLS = [(tx, sc, ba) for tx in (True, False) for sc in ('us', 'gl') for ba in ('net', 'gross')]
KEY = {('us', 'gross'): 'usg', ('us', 'net'): 'usn', ('gl', 'gross'): 'glg', ('gl', 'net'): 'gln'}

def run(n, central=False, opt=None, overrides=None, subset=None, weight=None):
    """Returns per-project dict of arrays and the project frame used."""
    f = draw_shared(n, central, overrides)
    df = P if subset is None else P[subset(P)]
    E = {r.ceq_id: em(r, f, n, central, opt) for r in df.itertuples()}
    return df, E

def aggregate(df, E, weight=None, n=1):
    out = {}
    for tx, sc, ba in CELLS:
        k = KEY[(sc, ba)]
        cl = np.zeros(n); fo = np.zeros(n)
        for r in df.itertuples():
            if r.group not in ('Clean', 'Fossil'): continue
            if not tx and r.subsector == 'Transmission': continue
            w = 1.0 if weight is None else weight(r)
            if r.group == 'Clean': cl = cl + w * E[r.ceq_id][k]
            else: fo = fo + w * E[r.ceq_id][k]
        out[(tx, sc, ba)] = (cl, fo)
    return out

def summarize(agg, label):
    rows = []
    for (tx, sc, ba), (cl, fo) in agg.items():
        net = fo - cl
        ratio = np.where(fo > 0, cl / np.where(fo == 0, np.nan, fo), np.inf)
        rows.append(dict(case=label, transmission='in' if tx else 'out', scope='US' if sc == 'us' else 'global', basis=ba,
            clean_avoided_p50=np.median(cl), clean_p05=np.percentile(cl, 5), clean_p95=np.percentile(cl, 95),
            fossil_added_p50=np.median(fo), fossil_p05=np.percentile(fo, 5), fossil_p95=np.percentile(fo, 95),
            ratio_clean_to_fossil_p50=np.nanmedian(ratio), ratio_p05=np.nanpercentile(ratio, 5), ratio_p95=np.nanpercentile(ratio, 95),
            net_fossil_minus_clean_p50=np.median(net), net_p05=np.percentile(net, 5), net_p95=np.percentile(net, 95),
            share_draws_fossil_gt_clean=float(np.mean(fo > cl)), sign='LOWERS' if np.median(net) < 0 else 'RAISES'))
    return rows

def det(df, E):
    return {k: {i: float(np.asarray(v)[0]) for i, v in d.items()} for k, d in [(i, E[i]) for i in E]}

if __name__ == '__main__':
    lit = lambda r: LIT_RATE[r.subsector]
    # litigation rates drawn per subsector from Jeffreys Beta(k+0.5, n-k+0.5) on B&W Table 1 counts, shared per draw
    LIT_DRAW = {}
    for sub, rate in LIT_RATE.items():
        nn = LIT_N.get(sub, 15); kk = round(rate * nn)
        LIT_DRAW[sub] = RNG.beta(kk + 0.5, nn - kk + 0.5, N)
    lit_mc = lambda r: LIT_DRAW[r.subsector]
    prog = lambda d: ~d.programmatic.astype(bool)
    allrows = []
    # ---------- base: central deterministic + MC
    dfc, Ec = run(1, central=True)
    df, E = run(N)
    allrows += summarize(aggregate(df, E, n=N), 'base_exposure')
    allrows += summarize(aggregate(df, E, weight=lit, n=N), 'base_litigation_fixed_rates')
    allrows += summarize(aggregate(df, E, weight=lit_mc, n=N), 'base_litigation_beta_rates')
    # ---------- per-project table
    pr = P.copy()
    for k in ['usg', 'usn', 'glg', 'gln']:
        pr[f'em_{k}_central'] = [float(Ec[i][k][0]) for i in pr.ceq_id]
        pr[f'em_{k}_p05'] = [float(np.percentile(E[i][k], 5)) for i in pr.ceq_id]
        pr[f'em_{k}_p95'] = [float(np.percentile(E[i][k], 95)) for i in pr.ceq_id]
    pr['litigation_rate_bw'] = pr.subsector.map(LIT_RATE)
    pr.drop(columns=['p']).to_csv(os.path.join(HERE, 'projects.csv'), index=False)
    # central deterministic cells
    allrows += summarize(aggregate(dfc, Ec, n=1), 'base_central_deterministic')
    # ---------- sensitivities (MC)
    SENS = {
        'projects_only': dict(subset=prog),
        'built_only': dict(subset=prog, opt=dict(built=True)),
        'MER_cambium_0.10-0.30': dict(overrides={'MER': (0.10, 0.20, 0.30)}),
        'horizon_20yr': dict(opt=dict(H=20)),
        'methane_2.3pct_GWP100': dict(opt=dict(methane=True)),
        'pipe_net_ICF_-0.075': dict(overrides={'NET_PIPE': -0.075}),
        'pipe_net_SabalTrail_0.36': dict(overrides={'NET_PIPE': 0.36}),
        'no_programmatic_haircut_REAL_PROG_1': dict(overrides={'REAL_PROG': 1.0}),
        'horizon_30yr_all_depletables': dict(opt=dict(H=30)),
        'leakage_Prest2022_net0.28': dict(overrides={'NET_OIL': (0.22, 0.28, 0.48)}),
        'tx_enable_ACP_1.4': dict(overrides={'TX_ENABLE_RENEW': 1.4}),
        'drop_fossil_continuations': dict(opt=dict(drop_fossil_continuation=True)),
        'credit_existing_clean': dict(opt=dict(credit_existing=True)),
    }
    for name, kw in SENS.items():
        d2, E2 = run(N, opt=kw.get('opt'), overrides=kw.get('overrides'), subset=kw.get('subset'))
        allrows += summarize(aggregate(d2, E2, n=N), name)
    R = pd.DataFrame(allrows)
    R.to_csv(os.path.join(HERE, 'results_cells.csv'), index=False)
    # ---------- concentration: top-10 share per side (central, primary cell + global net)
    conc = []
    for sc, ba in [('us', 'net'), ('gl', 'net'), ('us', 'gross'), ('gl', 'gross')]:
        k = KEY[(sc, ba)]
        for g in ['Clean', 'Fossil']:
            s = pr[pr.group == g][['ceq_id', 'title', 'subsector', f'em_{k}_central']].sort_values(f'em_{k}_central', ascending=False)
            tot = s[f'em_{k}_central'].sum()
            top = s.head(10)
            conc.append(dict(scope=sc, basis=ba, group=g, total=tot, top10_sum=top[f'em_{k}_central'].sum(),
                             top10_share=top[f'em_{k}_central'].sum() / tot if tot else np.nan,
                             top10=' | '.join(f'{r.ceq_id} {r.title[:40]} ({r[f"em_{k}_central"]:.1f})' for _, r in top.iterrows())))
    pd.DataFrame(conc).to_csv(os.path.join(HERE, 'results_concentration.csv'), index=False)
    # ---------- imputed share
    imp = []
    for k in ['usn', 'gln']:
        for g in ['Clean', 'Fossil']:
            s = pr[pr.group == g]
            tot = s[f'em_{k}_central'].clip(lower=0).sum()
            imp.append(dict(metric=k, group=g, imputed_share=s[s.size_imputed.astype(bool)][f'em_{k}_central'].clip(lower=0).sum() / tot if tot else np.nan,
                            low_conf_share=s[s.size_confidence == 'low'][f'em_{k}_central'].clip(lower=0).sum() / tot if tot else np.nan))
    pd.DataFrame(imp).to_csv(os.path.join(HERE, 'results_imputed_share.csv'), index=False)
    print(R[(R.transmission == 'in') & (R.basis == 'net')][['case', 'scope', 'clean_avoided_p50', 'fossil_added_p50', 'ratio_clean_to_fossil_p50', 'net_p05', 'net_fossil_minus_clean_p50', 'net_p95', 'share_draws_fossil_gt_clean']].round(2).to_string())
