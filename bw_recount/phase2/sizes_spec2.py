"""Phase 2 curated sizes for NEW energy EISs (CEQ 2010-2024 workbook, not in the 2018 workbook).
Same conventions as ../sizes_spec.py. 'ref' = 'P2F:<id>:<metric>' / 'P2C:<id>:<metric>' (phase2 sizing agent CSVs) or 'URL:...'.
"""
EIA_PIPE = 'URL:https://www.eia.gov/naturalgas/pipelines/EIA-NaturalGasPipelineProjectsAug2026.xlsx'
EIA_LNG = 'URL:https://www.eia.gov/naturalgas/U.S.liquefactioncapacity.xlsx'
S = {}
def e(i, **k): S[i] = k

# ---------------- LNG export (MTPA baseload; EIA US Liquefaction Capacity, Jun 2025 release) ----------------
e('C1351', m='LNG', v=10.0, hi=12.0, u='MTPA', b=10.0, st='operating', ne='new_build', ref=EIA_LNG, conf='high', note='Calcasieu Pass (CP15-550), 2022')
e('C1379', m='LNG', v=27.6, u='MTPA', b=16.56, st='under_construction', ne='new_build', ref=EIA_LNG, conf='high', note='Driftwood = Woodside Louisiana LNG: phase 1 16.56 MTPA under construction; 11.04 approved (FERC total 27.6)')
e('C1385', m='LNG', v=12.0, hi=13.5, u='MTPA', b=12.0, st='under_construction', ne='new_build', ref=EIA_LNG, conf='high', note='Port Arthur Phase 1 (CP17-20), 2027; Phase 2 is a later separate review (not counted)')
e('C1401', m='LNG', v=4.0, u='MTPA', b=0, st='predevelopment', ne='new_build', ref=EIA_LNG, conf='high', note='Texas LNG (Glenfarne); FID not confirmed (Argus May 2026 forward-looking only)')
e('C1408', m='LNG', v=1.0, u='MTPA', b=0, st='predevelopment', ne='new_build', ref='URL:https://aglaw.psu.edu/wp-content/uploads/2021/02/Jacksonville-Project-Final-Environmental-Impact-Statement-Apr.-2019.pdf', conf='medium', note='Eagle LNG Jacksonville: FEIS "total nominal capacity of 1.0 MTPA" (3 x 0.33; search-result text); not built')
e('C1410', m='LNG', v=10.85, u='MTPA', b=0, st='predevelopment', ne='expansion', ref=EIA_LNG, conf='high', note='Gulf LNG Liquefaction (CP15-521), undergoing FEED')
e('C1413', m='LNG', v=6.5, lo=6.0, u='MTPA', b=0, st='cancelled', ne='new_build', ref='URL:https://ogj.com/pipelines-transportation/lng/article/14199916/annova-lng-cancels-brownsville-tex-liquefaction-project', conf='medium', note='Annova LNG 6.5 MTPA (GEM lists 6.0); FERC approved Nov 2019; cancelled Mar 2021 (search-result text)')
e('C1415', m='LNG', v=27.0, u='MTPA', b=16.2, st='under_construction', ne='new_build', ref=EIA_LNG, conf='high', note='Rio Grande LNG: 5 x 5.4 MTPA approved; phase 1 (3 trains, 16.2) under construction; phase 2 10.8 approved')
e('C1428', m='LNG', v=19.8, hi=24.0, u='MTPA', b=19.8, st='operating', ne='new_build', ref=EIA_LNG, conf='high', note='Plaquemines LNG phases 1+2 (CP17-66/67), 2024-25; Gator Express feed pipeline embedded')
e('C1431', m='DUP', v=0, u='', b=0, st='operating', ne='duplicate', ref=EIA_LNG, p=dict(dup='C1428'), note='second listing of Plaquemines LNG')
e('C1537', m='LNG', v=20.0, u='MTPA', b=0, st='predevelopment', ne='new_build', ref=EIA_LNG, conf='high', note='Alaska LNG (CP17-178), proposed; no FID')
e('C1720', m='LNG', v=9.3, hi=9.5, u='MTPA', b=9.3, st='under_construction', ne='new_build', ref='URL:https://www.argusmedia.com/en/news-and-insights/latest-market-news/2827867-caturus-greenlights-commonwealth-lng-terminal-update', conf='medium',
  note='Commonwealth LNG: FID May 2026 (Argus, search-result text); 9.3-9.5 MTPA')
e('C1778', m='LNG', v=20.0, hi=28.0, u='MTPA', b=20.0, st='under_construction', ne='new_build', ref='URL:https://www.worldoil.com/news/2025/7/28/venture-global-reaches-15-1-billion-investment-decision-for-cp2-lng/', conf='medium',
  note='CP2 LNG: FERC-approved 20 MTPA nameplate (28 peak); phase 1 FID Jul 2025, phase 2 FID 2026 (search-result text)')
e('C1498', m='LNG', v=7.8, u='MTPA', b=0, st='cancelled', ne='new_build', ref='A4:R0515:lng_capacity', conf='medium', p=dict(dup_pooled='R0515'), note='Jordan Cove 2019 FEIS (7.8 MTPA; same project as R0515, zeroed in pooled set)')

# ---------------- Gas pipelines (Bcf/d; EIA Natural Gas Pipeline Projects, Aug 2026) ----------------
P = [
 ('C1382', 0.400, 0, 'under_construction', 'dom', 'Northeast Supply Enhancement (revived; construction 2027)'),
 ('C1527', 0.550, 0, 'under_construction', 'dom', 'MVP Southgate (amended 550 MMcf/d), 2028'),
 ('C1657', 0.115, 0.115, 'operating', 'dom', 'East 300 Upgrade, 2023'),
 ('C1665', 0.125, 0, 'predevelopment', 'dom', 'Iroquois Enhancement by Compression (approved, 2028)'),
 ('C1680', 0.140, 0.140, 'operating', 'dom', 'Delta Lateral (to IPP Renewed gas plant), 2024'),
 ('C1684', 0.0507, 0.0507, 'operating', 'dom', 'Wisconsin Access, 2022'),
 ('C1710', 0.829, 0.829, 'operating', 'dom', 'Regional Energy Access, 2024'),
 ('C1715', 0.220, 0.220, 'operating', 'dom', 'Texas Gas Henderson County Expansion (power), 2024'),
 ('C1724', 0.400, 0.400, 'operating', 'dom', 'Spire STL (in service 2019; 2022 EIS on remand)'),
 ('C1735', 0.150, 0.150, 'operating', 'dom', 'GTN XPress, 2024'),
 ('C1739', 0.350, 0.350, 'operating', 'dom', 'Virginia Electrification Project, 2024'),
 ('C1742', 0.210, 0.210, 'operating', 'dom', 'Three Rivers Interconnection (power), 2024'),
 ('C1743', 0.350, 0.350, 'operating', 'dom', 'Ohio Valley Connector Expansion, 2024'),
 ('C1754', 0.423, 0.423, 'operating', 'dom', 'Southside Reliability Enhancement, 2024'),
 ('C1756', 0.0509, 0.0509, 'operating', 'dom', 'Northern Lights 2023, 2024'),
 ('C1763', 0.0206, 0.0206, 'operating', 'dom', 'Wahpeton Expansion, 2024'),
 ('C1787', 0.205, 0.205, 'operating', 'dom', 'Virginia Reliability Project 0.100 + Commonwealth Energy Connector 0.105, 2025'),
 ('C1412', 0.002, 0, 'predevelopment', 'dom', 'Crow Creek Pipeline (2 MMcf/d, approved)'),
 ('C1662', 0.495, 0.495, 'operating', 'mex', 'North Baja XPress (LNG/Mexico demand), 2023'),
]
for i, v, b, st, dest, note in P:
    e(i, m='PIPEGAS', v=v, u='Bcf/d', b=b, st=st, ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest=dest), note=note)
for i, v, b, note in [('C1656', 0.725, 0.725, 'East Lateral XPress -> Plaquemines LNG'), ('C1660', 2.2, 2.2, 'Evangeline Pass phases 1+2 -> Plaquemines LNG'),
                      ('C1664', 0.165, 0.165, 'Alberta Xpress -> LNG export'), ('C1721', 5.6, 0, 'Driftwood Lines 200/300 -> Driftwood LNG'), ('C1752', 1.26, 1.26, 'Venice Extension -> Plaquemines LNG')]:
    e(i, m='OVERLAP', v=v, u='Bcf/d', b=b, st='operating' if b else 'under_construction', ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest='lng'),
      note=note + ': feeds an LNG terminal in this universe; emissions counted at the terminal (0 here)')
for i, v, note in [('C1774', 0.245, 'TGP Cumberland Project -> TVA Cumberland gas CC (C1736)'), ('C1901', 0.300, 'TGP Ridgeline -> TVA Kingston gas CC (C1810)')]:
    e(i, m='OVERLAP', v=v, u='Bcf/d', b=v, st='operating' if i == 'C1774' else 'under_construction', ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest='plant'),
      note=note + ': feeds a gas plant in this universe; emissions counted at the plant (0 here)')
e('C1690', m='NOSIZE', v=0, u='', b=0, st='operating', ne='expansion', ref='URL:', note='Hackberry gas storage: no added throughput (unquantified)')
e('C1700', m='NOSIZE', v=0, u='', b=0, st='operating', ne='expansion', ref='URL:', note='compressor relocation: no added throughput')
e('C1727', m='COVERED', v=0, u='', b=0, st='implemented', ne='programmatic', ref='URL:', note='Cook Inlet Sale 258: tiered to the 2017-22 Program (R0738)')


# ---------------- CLEAN (P2C agent rows; MW) ----------------
OW = [('C1616',800,800,'operating','Vineyard Wind 1 (up to 880)'), ('C1647',132,132,'operating','South Fork (Harvard EELP 130)'),
      ('C1768',1100,0,'cancelled','Ocean Wind 1, cancelled Oct 2023'), ('C1776',704,704,'under_construction','Revolution Wind, first power Mar 2026'),
      ('C1786',2076,810,'under_construction','Empire Wind 1+2 approved; Empire 1 (810) under construction, Empire 2 not proceeding'),
      ('C1788',2600,2600,'under_construction','CVOW, first power Mar 2026'), ('C1802',924,924,'under_construction','Sunrise Wind, completion 2027'),
      ('C1811',2600,0,'predevelopment','New England Wind 1+2 (remand sought)'), ('C1830',2800,0,'cancelled','Atlantic Shores South, no longer viable'),
      ('C1851',2200,0,'predevelopment','Maryland Offshore Wind (US Wind), permit under challenge'), ('C1886',2400,0,'predevelopment','SouthCoast Wind, voluntary remand Nov 2025')]
for i,v,b,st,note in OW:
    e(i, m='GEN', v=v, u='MW', b=b, st=st, ne='new_build', ref=f'P2C:{i}:nameplate_capacity', p=dict(tech='OW'), note=note)
SOL = [('C1485',300,300,'operating','PV','Desert Quartzite 300 MWac (+150 MW storage; ROD 450 incl. storage)'), ('C1502',300,300,'operating','PV','Eagle Shadow Mountain'),
       ('C1504',690,690,'operating','PV','Gemini'), ('C1514',464,464,'operating','PV','Edwards AFB solar EUL (low conf)'), ('C1578',250,125,'operating','PV','Yellow Pine (phase 1 125 built)'),
       ('C1631',300,0,'predevelopment','PV','Southern Bighorn (300-400)'), ('C1686',250,250,'operating','PV','Skeleton Creek solar'), ('C1694',200,0,'unknown','PV','TVA North Alabama'),
       ('C1718',149,0,'unknown','PV','Badger State'), ('C1738',200,0,'predevelopment','PV','TVA Moore County'), ('C1850',700,0,'predevelopment','PV','Libra'),
       ('C1881',400,0,'predevelopment','PV','Rough Hat Clark'), ('C1885',600,0,'predevelopment','PV','Jove')]
for i,v,b,st,tech,note in SOL:
    e(i, m='GEN', v=v, u='MW', b=b, st=st, ne='new_build', ref=f'P2C:{i}:nameplate_capacity', p=dict(tech=tech), note=note)
WIND = [('C1107',25,25,'operating','new_build','Na Pua Makani (FEIS 2016, 2024 workbook only)'), ('C1438',137,137,'operating','new_build','Skookumchuck'),
        ('C1516',252,0,'predevelopment','new_build','Campo (paused)'), ('C1543',100,0,'unknown','new_build','Borderlands'), ('C1666',504,0,'unknown','new_build','Rail Tie interconnection'),
        ('C1458',132.5,132.5,'operating','continuation','Hawaii four existing wind farms ITP PEIS'), ('C1487',4048.3,4048.3,'operating','continuation','MidAmerican Iowa HCP: 22 existing facilities')]
for i,v,b,st,ne,note in WIND:
    e(i, m='GEN', v=v, u='MW', b=b, st=st, ne=ne, ref=f'P2C:{i}:nameplate_capacity', p=dict(tech='WIND'), note=note)
e('C1834', m='GEN', v=723, lo=723, hi=1205, u='MW', b=0, st='cancelled', ne='new_build', ref='P2C:C1834:nameplate_capacity', conf='low', p=dict(tech='WIND'),
  note='Lava Ridge: Dec 2024 ROD up to 241 turbines = 723-1,205 MW (Wikipedia); central at low end; cancelled Aug 2025')
NUC_R = [('C0203',2060,'Indian Point 2&3 initial renewal (plants closed 2020-21; credit 0)', 0), ('C0271',1604,'Turkey Point 3&4 subsequent renewal (CEQ FEIS date 2011 looks mis-keyed)', 1604),
         ('C1355',974,'River Bend initial renewal',974), ('C1361',1152,'Waterford 3 initial renewal',1152), ('C1515',2617,'Peach Bottom subsequent renewal',2617),
         ('C1849',1875,'North Anna 1&2 subsequent renewal',1875), ('C1894',671,'Monticello subsequent renewal',671)]
for i,v,note,cred in NUC_R:
    e(i, m='GEN', v=cred, u='MW_existing', b=cred, st='operating' if cred else 'closed', ne='continuation', ref=f'P2C:{i}:nameplate_capacity', conf='low', p=dict(tech='NUC'),
      note=note + ': continuation, zero unless credit_existing')
e('C1405', m='GEN', v=800, u='MW', b=0, st='predevelopment', ne='new_build', ref='P2C:C1405:nameplate_capacity', p=dict(tech='NUC'), note='Clinch River ESP envelope max 800 MWe')
e('C1707', m='GEN', v=300, hi=1200, u='MW', b=300, st='under_construction', ne='new_build', ref='P2C:C1707:nameplate_capacity', p=dict(tech='NUC', dup_pooled='C1405'),
  note='Clinch River technology park: first BWRX-300 (construction permit Sep 2026); same site as C1405 -> zero in pooled set')
HY = [('C1330',5,0,'predevelopment','new_build','Lassen Lodge 5 MW new'), ('C1422',5,0,'predevelopment','new_build','Grant Lake 5 MW new'),
      ('C1716',-163,-163,'operating','continuation','Lower Klamath dam removal (-163 MW)'), ('C1383',0,0,'operating','relicensing','Yuba River relicense (MW NOT FOUND)'),
      ('C1519',0,0,'operating','relicensing','Bucks Creek relicense (MW NOT FOUND)'), ('C1566',0,0,'operating','relicensing','Don Pedro/La Grange relicense (MW NOT FOUND)'),
      ('C1568',0,0,'operating','continuation','Columbia River System Operations (existing federal dams)')]
for i,v,b,st,ne,note in HY:
    e(i, m='HYDRO', v=v, u='MW_incremental', b=b, st=st, ne=ne, ref=f'P2C:{i}:' + ('incremental_capacity' if i=='C1716' else 'nameplate_capacity'), p=dict(tech='HYDRO', existing_mw=0), note=note)
for i,v,note in [('C1380',393.3,'Swan Lake North closed-loop pumped storage'), ('C1533',240,'Mineville pumped storage'), ('C1809',0,'Goldendale pumped storage (MW NOT FOUND)')]:
    e(i, m='ZERO', v=v, u='MW', b=0, st='predevelopment', ne='new_build', ref=f'P2C:{i}:nameplate_capacity', p=dict(tech='PSH'), note=note + ': storage, 0 avoided')
for i in ['C1276','C1298','C1512']:
    e(i, m='NOSIZE', v=0, u='', b=0, st='implemented', ne='programmatic', ref=f'P2C:{i}:rfd_capacity', note='geothermal leasing availability; no MW scenario found (unquantified clean)')
TX2 = [('C1478',3200,'renew',3200,'operating','P2C:C1478c:transmission_rating',False,'Ten West Link 500 kV (AZ solar to CA)'),
       ('C1491',400,'renew',400,'operating','P2C:C1491:voltage',True,'Cardinal-Hickory Creek 345 kV (MISO MVP); rating imputed from kV'),
       ('C1837',900,'renew',900,'under_construction','P2C:C1837:voltage',True,'Greenlink West 525 kV; rating imputed from kV (500 kV class)'),
       ('C1867',1500,'renew',0,'predevelopment','P2C:C1867c:transmission_rating',False,'Cross-Tie 500 kV UT-NV (snippet, low)'),
       ('C1387',400,'reliab',0,'under_construction','P2C:C1387:voltage',True,'NPPD R-Project 345 kV (reliability + wind access); imputed'),
       ('C1291',33,'reliab',33,'operating','P2C:C1291:voltage',True,'Estes-Flatiron 115 kV rebuild'),
       ('C1318',33,'reliab',0,'unknown','P2C:C1318:voltage',True,'Bordertown-California 120 kV'),
       ('C1879',33,'reliab',0,'predevelopment','P2C:C1879:voltage',True,'McClellanville 115 kV')]
for i,v,purp,b,st,ref,imp,note in TX2:
    e(i, m='TX', v=v, u='MW_rating', b=b, st=st, ne='new_build', ref=ref, imp=imp, p=dict(purpose=purp), note=note)
e('C1749', m='TX', v=3021, u='MW_rating', b=3021, st='operating', ne='new_build', ref='P2C:C1749c:transmission_rating', p=dict(purpose='renew', dup_pooled='R0998'), note='SunZia 2023 FEIS (route change); same line as R0998 -> zero in pooled set')
e('C1863', m='PROGCLEAN', v=99690, lo=77537, hi=139566, u='MW_rfd', b=0, st='implemented', ne='programmatic', ref='P2C:C1863:rfd_capacity', imp=True, p=dict(tech='PV'),
  note='2024 Western Solar Plan PEIS: RFD ~697,830 acres by 2045 (DOE Solar Futures). MW IMPUTED at 7 acres/MW (5-9) = 99.7 GW (77.5-139.6) full potential; realization via shared REAL_PROG. BLM FAQ: acreage is what clean energy goals would need, not a forecast')
e('C1880', m='PROGCLEAN', v=5601, hi=7000, u='MW_rfd', b=0, st='implemented', ne='programmatic', ref='P2C:C1880:rfd_capacity', p=dict(tech='OW'),
  note='NY Bight PEIS: 5,601 MW across six leases (up to 7 GW); realization via REAL_PROG; COP EISs would follow separately')


# ---------------- FOSSIL fields, leasing, coal (P2F agent rows; cumulative oil MMbbl / gas Bcf, annualized over H) ----------------
e('C1574', m='OG', v=1, u='cumulative', b=1, st='under_construction', ne='new_build', ref='P2F:C1574:oil_production_total', p=dict(oil=590, oil_lo=576, oil_hi=628.9),
  note='Willow MDP 2020 FEIS: 590 MMbbl/30 yr (2023 ROD approved 3 pads = 576; 5-pad Alt B 628.9); peak 160-180 kb/d; gas reinjected; under construction (FID Dec 2023)')
e('C1333', m='OG', v=1, u='cumulative', b=0, st='cancelled', ne='new_build', ref='P2F:C1333b:oil_production_total', p=dict(oil=120, oil_lo=74, oil_hi=120),
  note='Liberty (Hilcorp) ~120 MMbbl (BOEM model 74-86); approval vacated, cancelled')
e('C1353', m='OG', v=1, u='cumulative', b=1, st='operating', ne='new_build', ref='P2F:C1353:oil_production_peak', conf='medium', p=dict(oil=876, oil_lo=876, oil_hi=1314),
  note='Nanushuk/Pikka: 80,000 bbl/d phase-1 design (120,000 high) x 30 yr = 876 MMbbl (1,314 high); FEIS not retrieved')
e('C1316', m='OG', v=1, u='cumulative', b=0, st='unknown', ne='new_build', ref='P2F:C1316b:gas_production_total', p=dict(gas=7000, oil=78.75, oil_lo=17.5, oil_hi=140, life=40),
  note='Normally Pressured Lance: 3,500 wells, 7 Tcf over 40 yr (BLM release); oil 17.5-140 MMbbl (midpoint); IBLA vacated approval Jan 2026')
e('C1528', m='OG', v=1, u='cumulative', b=0, st='predevelopment', ne='new_build', ref='P2F:C1528b:gas_production_total', p=dict(gas=18160, oil=254, life=65),
  note='Moneta Divide: 4,250 wells, 18.16 Tcf + 254 MMbbl over 65 yr (annualized over its documented 65 yr since 2026-10-21); no large drilling program found')
e('C1570', m='OG', v=1, u='cumulative', b=1, st='operating', ne='new_build', ref='P2F:C1570b:oil_production_total', conf='medium', p=dict(oil=1370, oil_lo=94, oil_hi=1370, gas=5790),
  note='Converse County: 5,000 wells; BLM figure 1,370 MMbbl + 5.79 Tcf (a county page quotes 94 MMbbl: CONFLICT, low=94); ROD vacated Feb 2026, drilling continues under individual reviews')
e('C1480', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='P2F:C1480:oil_production_total', p=dict(oil=5750, oil_lo=1500, oil_hi=10000, gas=3500, gas_lo=0, gas_hi=7000, life=70),
  note='Coastal Plain (ANWR) leasing program: hypothetical 1.5-10 Bbbl over ~70 yr (midpoint central), gas 0-7 Tcf; 2021 leases cancelled 2023, cancellations vacated Mar 2025, Interior rescinded the 2024 ROD and lifted AIDEA suspension Oct 2025 (CRS IF12006); annualized over the FEIS 70 yr')
e('C1560', m='OG', v=1, u='cumulative', b=0, st='withdrawn', ne='programmatic', ref='P2F:C1560b:oil_production_total', p=dict(oil=1635.8, oil_lo=633.2, oil_hi=2638.4, life=70),
  note='NPR-A IAP 2020 (Alt E) RFD 633-2,638 MMbbl over 70 yr excl. Willow (midpoint central); superseded 2022')
e('C1790', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='P2F:C1790:lease_sales', imp=True, p=dict(oil=1122, oil_lo=657, oil_hi=1778, gas=3631, gas_lo=1652, gas_hi=6681, life=55),
  note='2024-29 OCS Program (3 GOM sales): BOEM production NOT FOUND; IMPUTED as 3/10 of the 2017-22 Program (10 GOM sales) low/mid/high')
e('C1429', m='NOSIZE', v=0, u='', b=0, st='unknown', ne='programmatic', ref='P2F:C1429:wells_approved', note='BLM Central Coast O&G RMPA: RFD 37 wells (negligible; unquantified)')
e('C1591', m='OG', v=1, u='cumulative', b=1, st='operating', ne='continuation', ref='P2F:C1591c:oil_production_peak', conf='medium', p=dict(oil=107.3, gas=136),
  note='Osage County O&G (BIA): mature field, RFD 4,761 wells 2018-37; 2018 county production 3.575 MMbbl + 4.53 Bcf/yr x 30 yr (EIS downstream 3.7-3.85 Mt/yr); continuation')
e('C1326', m='COALLEASE', v=30.8, hi=44.9, u='Mst_total', b=0, st='unknown', ne='expansion', ref='P2F:C1326:coal_reserves_leased', p=dict(rank='bituminous'), note='Alton Coal Tract LBA (preferred K1 30.8 Mst); sale/mining status unknown')
e('C1364', m='COALLEASE', v=68.5, hi=70.8, u='Mst_total', b=68.5, st='operating', ne='expansion', ref='P2F:C1364:coal_reserves_leased', p=dict(rank='subbituminous'), note='Rosebud Mine Area F (feeds Colstrip); extends mine ~8-19 yr')
e('C1397', m='COALLEASE', v=33, hi=53, u='Mst_total', b=0, st='cancelled', ne='continuation', ref='P2F:C1397b:coal_production_rate', p=dict(rank='subbituminous'),
  note='San Juan Mine deep lease extension: ROD ~3 Mst/yr through 2033 (=33 Mst; 53 Mst lease); San Juan GS retired 2022, mine closed')


e('C1589', m='COALLEASE', v=55.7, lo=10, hi=167, u='Mst_total', b=0, st='unknown', ne='expansion', ref='P2F:C1589:coal_reserves_leased', imp=True, conf='low', p=dict(rank='bituminous'),
  note='Sugar Camp Mine No.1 (TVA coal rights, IL): tonnage NOT FOUND; IMPUTED at the median coal-lease size in this universe (55.7 Mst; range 10-167)')
e('C1708', m='PIPEOIL_EXPORT', v=2000000, u='bbl/d', b=0, st='predevelopment', ne='new_build', ref='P2F:C1708:throughput', note='SPOT deepwater crude export port (2 Mb/d); no construction found')
e('C1844', m='PIPEOIL_EXPORT', v=1000000, u='bbl/d', b=0, st='predevelopment', ne='new_build', ref='P2F:C1844:throughput', note='Texas GulfLink deepwater crude export port (1 Mb/d); ROD delayed')
e('C1307', m='OG', v=1, u='cumulative', b=0, st='predevelopment', ne='new_build', ref='P2F:C1307:oil_production_peak', p=dict(oil=547.5),
  note='Enefit utility corridor enabling the private-land South oil-shale project, 50,000 bbl/d (x 30 yr = 547.5 MMbbl); not built')
e('C1374', m='NOSIZE', v=0, u='', b=0, st='unknown', ne='new_build', ref='P2F:C1374:pipeline_length', note='Riley Ridge to Natrona: CO2 pipeline for EOR (244 mi); throughput NOT FOUND (unquantified fossil-enabling)')
e('C1736', m='PLANT', v=1450, u='MW', b=1450, st='under_construction', ne='new_build', ref='P2F:C1736:nameplate_capacity', p=dict(ef=0.37, fuel='gas', cfkey='CF_GASPLANT'),
  note='TVA Cumberland: 1,450 MW gas CC replacing one 1,235 MW coal unit (EF 0.37 t/MWh ASSUMED); net vs MER like other plants')
e('C1810', m='PLANT', v=1500, u='MW', b=1500, st='under_construction', ne='new_build', ref='P2F:C1810:nameplate_capacity', p=dict(ef=0.37, fuel='gas', cfkey='CF_GASPLANT'),
  note='TVA Kingston: >=1,500 MW gas; coal retirement reversed Feb 2026 (gas adds on top of coal for now)')
e('C1547', m='PLANT', v=104, u='MW', b=0, st='unknown', ne='new_build', ref='P2F:C1547:nameplate_capacity', p=dict(ef=0.45, fuel='gas', cfkey='CF_GASPLANT'), note='NJ TRANSITGRID gas-fired microgrid (104 MW from NOI; EF 0.45 ASSUMED)')


e('C1319', m='OVERLAP', v=1.44, lo=1.4, u='Bcf/d', b=1.44, st='operating', ne='new_build', ref='URL:https://naturalgasworld.com/us-ferc-approves-oklahoma-pipe-project-63610', conf='medium', p=dict(dest='dom'),
  note='Midcontinent Supply Header (MIDSHIP), Anadarko to Gulf Coast, ~1.4-1.44 Bcf/d, in service 2020 (search-result text). Zeroed 2026-10-21: Cheniere LNG feed line, overlaps the LNG terminals US net (NEMS includes induced production), consistent with zeroed LNG laterals')
e('C1683', m='NOSIZE', v=0, u='', b=0, st='operating', ne='expansion', ref='URL:https://ferc.gov/news-events/news/ferc-staff-issues-final-environmental-impact-statement-clear-creek-expansion', note='Clear Creek gas storage expansion (4 to 20 Bcf storage): no added throughput (unquantified)')

# ---------------- OTHER bucket (tabulated, excluded from clean/fossil net) ----------------
import os as _os, pandas as _pd
_u = _pd.read_csv(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'universe_new.csv'))
for _i, _g in zip(_u.ceq_id, _u.group):
    if _i not in S and _g == 'Other':
        e(_i, m='OTHER', v=0, u='', b=0, st='', ne='', ref='URL:', note='Other bucket: excluded from clean/fossil net')
