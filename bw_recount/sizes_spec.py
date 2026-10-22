"""Curated per-project size specification for the emissions-weighted recount (hand-reviewed 2026-10-21).
One entry per universe EIS. Values were chosen from the sizing subagent CSVs (sizing_out/A*.csv; the
'ref' field points to the row used, and build_projects.py copies its source URL / quote / confidence), from EIA
databases (high confidence), or set here with an explicit source. Fields:
  m    : method code (see recount.py)
  v    : central size; lo/hi: optional range; u: unit
  b    : built size (operating or under construction) for the built-only sensitivity (0 = not built)
  st   : status_2026; ne: new_build | expansion | continuation | relicensing | programmatic | duplicate
  ref  : 'A#:<row id>:<metric>' or 'URL:<url>'; conf: overrides confidence; imp: True if imputed
  p    : extra parameters (tech, purpose, rank, ...)
"""
EIA_PIPE = 'URL:https://www.eia.gov/naturalgas/pipelines/EIA-NaturalGasPipelineProjectsAug2026.xlsx'
EIA_LNG = 'URL:https://www.eia.gov/naturalgas/U.S.liquefactioncapacity.xlsx'
S = {}
def e(i, **k): S[i] = k

# ---------------- PIPELINES (Bcf/d; EIA Natural Gas Pipeline Projects, Aug 2026 = high confidence) ----------------
e('R0017', m='PIPEGAS', v=0.342, u='Bcf/d', b=0.342, st='operating', ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='AIM, CP14-96, in service 2016')
e('R0050', m='PIPEGAS', v=0.266, u='Bcf/d', b=0.266, st='operating', ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Kern River Apex Expansion CP10-14, 2011')
e('R0063', m='PIPEGAS', v=1.5, u='Bcf/d', b=0, st='cancelled', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Atlantic Coast Pipeline CP15-554 (+Supply Header CP15-555, same gas); cancelled 2020')
e('R0066', m='PIPEGAS', v=1.7, u='Bcf/d', b=1.7, st='operating', ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Atlantic Sunrise phases IA/IB/II = 0.40+0.45+0.85 Bcf/d, 2017-18')
e('R0202', m='PIPEGAS', v=0.65, u='Bcf/d', b=0, st='cancelled', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Constitution CP13-499 cancelled 2020 (revival pre-applied, not counted)')
e('R0550', m='PIPEGAS', v=1.53, u='Bcf/d', b=1.53, st='operating', ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Leach XPress 1.53 Bcf/d; Rayne XPress (1.1, reversal of same system) not added')
e('R0651', m='PIPEGAS', v=2.0, lo=2.0, hi=2.6, u='Bcf/d', b=2.0, st='operating', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='MVP 2.0 Bcf/d (2024); Equitrans Expansion 0.6 feeds MVP (high only)')
e('R0652', m='PIPEGAS', v=2.7, u='Bcf/d', b=2.7, st='operating', ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Mountaineer XPress 1.84+0.86 Bcf/d (2019); Gulf XPress 0.875 reversal downstream, not added')
e('R0683', m='PIPEGAS', v=0.8, u='Bcf/d', b=0.8, st='operating', ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='NJ-NY Project CP11-56, 2013')
e('R0693', m='PIPEGAS', v=1.5, u='Bcf/d', b=1.5, st='operating', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='NEXUS 1.5 Bcf/d (2018); TEAL laterals feed NEXUS, not added')
e('R0753', m='PIPEGAS', v=1.107, u='Bcf/d', b=0, st='cancelled', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='PennEast cancelled 2021')
e('R0880', m='PIPEGAS', v=0.647, u='Bcf/d', b=0.647, st='operating', ne='expansion', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Transco Rockaway Delivery Lateral 0.647 (2015); NE Connector 0.10 supports it, not added')
e('R0887', m='PIPEGAS', v=3.25, u='Bcf/d', b=3.25, st='operating', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Rover phases 1+2 = 1.70+1.55 (2017-18); Panhandle/Trunkline backhauls carry the same gas, not added')
e('R0889', m='DUP', v=0, u='', b=0, st='operating', ne='duplicate', ref='A4:R0889:duplicate', p=dict(dup='R0890'), note='BLM Ruby EIS duplicates FERC R0890')
e('R0890', m='PIPEGAS', v=1.5, u='Bcf/d', b=1.5, st='operating', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Ruby CP09-54, 2011')
e('R0931', m='PIPEGAS', v=0.201, u='Bcf/d', b=0.201, st='operating', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='mex'), note='Sierrita 2014: export to Mexico (combustion outside US)')
e('R0961', m='PIPEGAS', v=1.0, lo=0.83, hi=1.1, u='Bcf/d', b=1.0, st='operating', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='Sabal Trail ph I+II 0.83+0.17 Bcf/d; FERC SEIS analysed 1.1')
e('N0004', m='PIPEGAS', v=0.5, u='Bcf/d', b=0, st='predevelopment', ne='new_build', ref=EIA_PIPE, conf='high', p=dict(dest='dom'), note='ASAP on hold (EIA)')
e('N0050', m='KXL', v=830000, u='bbl/d', b=0, st='cancelled', ne='new_build', ref='URL:https://www.everycrsreport.com/files/20141230_R43415_727b4665c03a07b956fbba9bd8597fa51e4a1f75.pdf', conf='medium',
  note='State Dept FSEIS (2014) via CRS R43415: gross lifecycle 147-168 MtCO2e/yr; incremental vs reference crudes 1.3-27.4 MtCO2e/yr. Cancelled 2021.')
e('R1063', m='PIPEPROD', v=62000, hi=120000, u='bbl/d', b=62000, st='operating', ne='new_build', ref='A4:R1063:pipeline_capacity', note='UNEV refined-products line SLC to Las Vegas (2012); displaces other supply to the same market')

# ---------------- LNG (MTPA baseload; EIA US Liquefaction Capacity, Jun 2025 release) ----------------
e('R0141', m='LNG', v=13.5, hi=14.97, u='MTPA', b=13.5, st='operating', ne='expansion', ref=EIA_LNG, conf='high', note='Cameron T1-3 (CP13-25), 2019-20; brownfield at import terminal')
e('R0216', m='LNG', v=13.57, hi=18.2, u='MTPA', b=13.57, st='operating', ne='new_build', ref=EIA_LNG, conf='high', note='Corpus Christi T1-3 (CP12-507), 2018-20')
e('R0340', m='LNG', v=15.0, hi=18.06, u='MTPA', b=15.0, st='operating', ne='expansion', ref=EIA_LNG, conf='high', note='Freeport T1-3 (CP12-509), 2019-20')
e('R0380', m='LNG', v=15.6, hi=18.1, u='MTPA', b=15.6, st='under_construction', ne='expansion', ref=EIA_LNG, conf='high', note='Golden Pass T1-3; T1 start 2026')
e('R0540', m='LNG', v=16.45, u='MTPA', b=0, st='cancelled', ne='expansion', ref=EIA_LNG, conf='high', note='Lake Charles (CP14-120); development suspended Dec 2025 (A4)')
e('R0593', m='LNG', v=8.0, hi=8.8, u='MTPA', b=0, st='predevelopment', ne='new_build', ref='A4:R0593:lng_capacity', note='Magnolia; no construction')
e('R0773', m='LNG', v=13.2, u='MTPA', b=0, st='predevelopment', ne='new_build', ref=EIA_LNG, conf='high', note='Delfin FLNG (FERC CP15-490 / MARAD); first-vessel FID reported Jun 2026, not yet construction (A4)')
e('R0515', m='LNG', v=6.8, hi=7.8, u='MTPA', b=0, st='cancelled', ne='new_build', ref='A4:R0515:lng_capacity', note='Jordan Cove + Pacific Connector (1.2 Bcf/d feed line embedded, not counted separately). Cancelled 2021')
e('R0255', m='REGAS', v=0.5, hi=0.625, u='Bcf/d', b=0, st='cancelled', ne='new_build', ref='A4:R0255:regas_sendout', p=dict(displaces='gas'),
  note='Downeast LNG: FEIS analysed an IMPORT terminal (0.5 Bcf/d avg send-out); labeled Liquefaction per PLAN/fingerprint but sized as import. Terminated 2016')
e('R0009', m='REGAS', v=0.5, u='Bcf/d', b=0, st='cancelled', ne='new_build', ref='A4:R0009:regas_sendout', p=dict(displaces='oil'), note='Aguirre GasPort: switch Aguirre plant from fuel oil to gas; authorization vacated 2019')
e('R0772', m='REGAS', v=0.4, u='Bcf/d', b=0, st='cancelled', ne='new_build', ref='A4:R0772:regas_sendout', p=dict(displaces='gas'), note='Port Ambrose; vetoed by NY governor 2015')

# ---------------- COAL MINES (cumulative million short tons; annual-equivalent over horizon H) ----------------
e('R1154', m='COALLEASE', v=1345.7, lo=1345.7, hi=1813.3, u='Mst_total', b=1345.7, st='operating', ne='continuation', ref='A3:R1154:coal_reserves_leased', p=dict(rank='subbituminous'),
  note='Wright Area: ROD-approved tracts N Hilight 467.6 + S Hilight 222.7 + N Porcupine 721.2 + S Porcupine 401.8; sold = 1,345.7 (N Hilight never sold); all six as applied 2,435.4. Extends Black Thunder & North Antelope Rochelle')
e('R0125', m='COALLEASE', v=167.0, u='Mst_total', b=0, st='withdrawn', ne='continuation', ref='A3:R0125:coal_reserves_leased', p=dict(rank='subbituminous'), note='Buckskin Hay Creek II: ROD 2013, sole bid rejected, never leased')
e('R0272', m='COALLEASE', v=26.0, u='Mst_total', b=0, st='unknown', ne='continuation', ref='A3:R0272:coal_reserves_leased', p=dict(rank='bituminous'), note='East Lynn Lake (WV); sale outcome not found')
e('N0043', m='COALLEASE', v=55.7, u='Mst_total', b=0, st='unknown', ne='continuation', ref='A3:N0043:coal_reserves_leased', p=dict(rank='bituminous'), note='Greens Hollow (SUFCO, UT); 2017 sale outcome not verified')
e('R0304', m='COALLEASE', v=10.0, u='Mst_total', b=10.0, st='operating', ne='continuation', ref='A3:R0304:coal_reserves_leased', conf='medium', p=dict(rank='bituminous'), note='West Elk lease modifications (~10 Mt, 2019 OSMRE ROD)')
e('R0305', m='DUP', v=0, u='', b=0, st='operating', ne='duplicate', ref='A3:R0305:coal_reserves_leased', p=dict(dup='R0304'), note='duplicate of R0304')
e('R0892', m='COALLEASE', v=130.0, u='Mst_total', b=0, st='unknown', ne='expansion', ref='A3:R0892:coal_reserves_leased', p=dict(rank='lignite'), note='Rusk permit area, South Hallsville No.1 (private lignite, USACE 404); Pirkey plant status unverified')
e('R1000', m='NOSIZE', v=0, u='', b=0, st='unknown', ne='programmatic', ref='A3:R1000:programmatic_no_size', note='USACE Fort Worth regional programmatic EIS for surface coal/lignite mining permits: no tonnage')

# ---------------- FOSSIL PLANTS ----------------
e('R0334', m='PLANT', v=1540, u='MW_net', b=1540, st='operating', ne='continuation', ref='A3:R0334:nameplate_capacity', p=dict(eis_mt=11.4, eis_cf=0.92, fuel='coal', cfkey='CF_COALPLANT'),
  note='Four Corners units 4&5 + Navajo Mine (one EIS): EIS 11.4 Mt/yr at 92% CF (metric per heat-input check); lease/ROW extension to 2041')
e('R0233', m='PLANT', v=300, u='MW', b=300, st='operating', ne='new_build', ref='A3:R0233:nameplate_capacity', p=dict(ef=0.40, fuel='gas', cfkey='CF_GASPLANT'), note='Deer Creek NGCC 2012; EF 0.40 t/MWh ASSUMED (NGCC with duct firing)')
e('R0526', m='PLANT', v=582, u='MW', b=582, st='operating', ne='new_build', ref='A3:R0526:nameplate_capacity', p=dict(eis_mt=1.8, eis_mt_hi=2.6, eis_cf=0.85, fuel='gas', cfkey='CF_GASPLANT'),
  note='Kemper IGCC (EIS 1.8-2.6 Mt/yr with capture); gasifier abandoned 2017, CTs run as NGCC (built flag = yes, emissions at EIS rate scaled by CF)')
e('R0402', m='PLANTDELTA', v=0.1318, u='MtCO2/yr_incremental', b=0.1318, st='operating', ne='continuation', ref='A3:R0402b:co2_annual_eis', p=dict(ef=0.55),
  note='Groton: removal of 50-MW average output limit; EIS incremental 131,776 tCO2e/yr (0.318 vs 0.186)')
e('R0342', m='PLANT', v=168, u='MW', b=0, st='cancelled', ne='expansion', ref='A3:R0342:nameplate_capacity', p=dict(ef=1.0, capture=0.9, fuel='coal', cfkey='CF_COALPLANT'), note='FutureGen 2.0 oxy-combustion, 90% capture; cancelled 2015')
e('R1016', m='PLANT', v=213, lo=130, u='MW_net', b=0, st='cancelled', ne='new_build', ref='A3:R1016c:net_capacity_to_grid', p=dict(eis_mt=0.3, eis_cf=0.85, fuel='coal', cfkey='CF_COALPLANT'), note='Texas Clean Energy Project IGCC with ~90% capture for EOR; cancelled 2016')

# ---------------- SOLAR (MW AC approved; built) ----------------
for i,v,b,st,tech,ref,note in [
 ('N0062',700,20,'operating','PV','A6:N0062:nameplate_capacity','Maricopa Sun HCP: 700 MW complex analysed; ~20 MW built (low conf)'),
 ('N0096',550,550,'operating','PV','A6:N0096:nameplate_capacity','Topaz (DOE loan guarantee EIS)'),
 ('R0011',100,0,'unknown','PV','A6:R0011:nameplate_capacity','Aiya Solar (Moapa)'),
 ('R0024',500,0,'unknown','CSP','A6:R0024:nameplate_capacity','Amargosa Farm Road (CSP)'),
 ('R0136',663.5,0,'cancelled','CSP','A6:R0136:nameplate_capacity','Calico: ROD 663.5 MW'),
 ('R0168',45,0,'cancelled','PV','A6:R0168:nameplate_capacity','Chevron Lucerne Valley'),
 ('R0239',150,150,'operating','PV','A6:R0239:nameplate_capacity','Desert Harvest (built ~214, capped at approved 150)'),
 ('R0314',550,550,'operating','PV','A6:R0314:nameplate_capacity','Desert Sunlight'),
 ('R0370',250,250,'operating','CSP','A6:R0370:nameplate_capacity','Genesis trough'),
 ('R0475',709,0,'cancelled','CSP','A6:R0475:nameplate_capacity','Imperial Valley (SES Solar Two) dish; PV successor on private land not credited'),
 ('R0501',400,392,'operating','CSP','A6:R0501:nameplate_capacity','Ivanpah'),
 ('R0517',350,250,'operating','PV','A6:R0517:nameplate_capacity','K Road Moapa'),
 ('R0607',750,250,'operating','PV','A6:R0607:nameplate_capacity','McCoy'),
 ('R0631',485,235,'operating','PV','A6:R0631:nameplate_capacity','Modified Blythe (PV); original Blythe 1,000 MW CSP (R0110) treated as duplicate'),
 ('R0726',20,0,'withdrawn','PV','A6:R0726:nameplate_capacity','Ocotillo Sol'),
 ('R0746',500,457,'operating','PV','A6:R0746:nameplate_capacity','Palen (EDF PV successor, 2022)'),
 ('R0750',399,135,'operating','PV','A6:R0750:nameplate_capacity','Panoche Valley'),
 ('R0846',100,0,'cancelled','CSP','A6:R0846:nameplate_capacity','Quartzsite'),
 ('R0860',200,0,'predevelopment','PV','A6:R0860:nameplate_capacity','RES Americas Moapa'),
 ('R0870',150,0,'cancelled','CSP','A6:R0870:nameplate_capacity','Rice Solar'),
 ('R0933',400,250,'operating','PV','A6:R0933:nameplate_capacity','Silver State South'),
 ('R0944',287,0,'cancelled','PV','A6:R0944:nameplate_capacity','Soda Mountain'),
 ('R0946',375,0,'predevelopment','PV','A6:R0946:nameplate_capacity','Sonoran (title typo 3,756 MW; FR says 375)'),
 ('R0983',300,300,'operating','PV','A6:R0983:nameplate_capacity','Stateline'),
 ('R1036',110,110,'operating','CSP','A6:R1036:nameplate_capacity','Crescent Dunes'),
]:
    e(i, m='GEN', v=v, u='MW', b=b, st=st, ne='new_build', ref=ref, p=dict(tech=tech), note=note)
e('R0110', m='DUP', v=0, u='', b=0, st='cancelled', ne='duplicate', ref='A6:R0110:nameplate_capacity', p=dict(dup='R0631'), note='Blythe CSP 1,000 MW never built; site re-permitted as Modified Blythe (R0631)')

# ---------------- WIND ----------------
for i,v,b,st,ne,ref,note in [
 ('R0023',153,153,'operating','new_build','A6:R0023:nameplate_capacity','Alta East'),
 ('R0174',3000,3000,'under_construction','new_build','A6:R0174:nameplate_capacity','Chokecherry & Sierra Madre, completion ~2029'),
 ('R0235',30,30,'operating','new_build','A6:R0235:nameplate_capacity','Deerfield (VT)'),
 ('R0267',186,131,'operating','new_build','A6:R0267:nameplate_capacity','Tule Wind (ECO Substation EIS)'),
 ('R0390',500,0,'unknown','new_build','A6:R0390:nameplate_capacity','Grapevine Canyon'),
 ('R0422',250,0,'cancelled','new_build','A6:R0422:nameplate_capacity','Buckeye (HCP; never built)'),
 ('R0480',400,400,'operating','new_build','A6:R0480:nameplate_capacity','Grande Prairie interconnection'),
 ('R0633',500,0,'predevelopment','new_build','A6:R0633:nameplate_capacity','Mohave County'),
 ('R0725',315,265,'operating','new_build','A6:R0725:nameplate_capacity','Ocotillo Express (ROD 315)'),
 ('R0912',200,0,'cancelled','new_build','A6:R0912:nameplate_capacity','Searchlight'),
 ('R0949',151.5,151.5,'operating','new_build','A6:R0949:nameplate_capacity','PrairieWinds / Crow Lake'),
 ('R1121',104,0,'unknown','new_build','A6:R1121:nameplate_capacity','West Butte'),
 ('R1138',75,0,'cancelled','new_build','A6:R1138:nameplate_capacity','Whistling Ridge'),
 ('R0336',600,600,'operating','continuation','A6:R0336:nameplate_capacity','Fowler Ridge HCP for existing farm'),
 ('R0499',186,186,'operating','continuation','A6:R0499:nameplate_capacity','Beech Ridge HCP, mostly existing (low conf)'),
]:
    e(i, m='GEN', v=v, u='MW', b=b, st=st, ne=ne, ref=ref, p=dict(tech='WIND'), note=note)
e('R0262', m='DUP', v=0, u='', b=0, st='under_construction', ne='duplicate', ref='A6:R0262:nameplate_capacity', p=dict(dup='R0174'), note='eagle take permit EIS for CCSM phase I')

# ---------------- GEOTHERMAL / NUCLEAR / STORAGE ----------------
e('R0149', m='GEN', v=33, u='MW', b=30, st='operating', ne='expansion', ref='A6:R0149:nameplate_capacity', p=dict(tech='GEO'), note='Casa Diablo IV')
e('R0897', m='GEN', v=160, u='MW', b=0, st='unknown', ne='new_build', ref='A6:R0897:nameplate_capacity', p=dict(tech='GEO'), note='Salt Wells (three projects)')
e('R0371', m='NOSIZE', v=0, u='', b=0, st='implemented', ne='programmatic', ref='A6:R0371:nameplate_capacity', note='Humboldt-Toiyabe geothermal leasing availability: no MW scenario found (clean programmatic, unquantified)')
for i,v,b,st,ref,note in [
 ('R1110',2234,2234,'operating','A6:R1110:nameplate_capacity','Vogtle 3&4 (2023-24)'),
 ('R1107',2234,0,'cancelled','A6:R1107:nameplate_capacity','V.C. Summer 2&3 abandoned 2017'),
 ('R1145',2234,0,'cancelled','A6:R1145:nameplate_capacity','W.S. Lee (COLs held, project cancelled)'),
 ('R1053',2234,0,'predevelopment','A6:R1053:nameplate_capacity','Turkey Point 6&7 (COL issued)'),
 ('R0956',2700,0,'cancelled','A6:R0956:nameplate_capacity','STP 3&4 (COL terminated 2018)'),
 ('R0701',1538,0,'predevelopment','A6:R0701:nameplate_capacity','North Anna 3 (COL issued)'),
 ('R0553',2234,0,'cancelled','A6:R0553:nameplate_capacity','Levy 1&2 (COL terminated 2018)'),
 ('R0288',1520,0,'predevelopment','A6:R0288:nameplate_capacity','Fermi 3 (COL issued)'),
 ('N0022',1600,0,'withdrawn','A6:N0022:nameplate_capacity','Bell Bend withdrawn 2016'),
 ('N0016',1600,0,'withdrawn','A6:N0016:nameplate_capacity','Calvert Cliffs 3 withdrawn 2015'),
 ('N0021',3400,0,'predevelopment','A6:N0021:nameplate_capacity','Comanche Peak 3&4 (suspended)'),
]:
    e(i, m='GEN', v=v, u='MW', b=b, st=st, ne='expansion', ref=ref, p=dict(tech='NUC'), note=note)
e('R0263', m='GEN', v=2234, lo=0, u='MW', b=0, st='predevelopment', ne='expansion', ref='A6:R0263:nameplate_capacity', imp=True, conf='low', p=dict(tech='NUC'),
  note='PSEG early site permit: no design/MW in sources; IMPUTED at the subsector-typical AP1000 pair (2,234 MW), low=0')
e('R0260', m='ZERO', v=1300, u='MW', b=0, st='predevelopment', ne='new_build', ref='A6:R0260:nameplate_capacity', p=dict(tech='PSH'), note='Eagle Mountain pumped storage: storage, no direct avoided emissions (0)')

# ---------------- HYDRO (incremental MW for new/added capacity; existing MW kept for symmetric sensitivity) ----------------
for i,inc,ex,b,st,ne,ref,note in [
 ('R0079',10,0,0,'cancelled','new_build','A7:R0079:nameplate_capacity','Bear River Narrows; FERC preferred license denial; not built'),
 ('R1002',19.8,0,0,'predevelopment','new_build','A7:R1002:nameplate_capacity','Sweetheart Lake; licensed 2016, no construction confirmed'),
 ('N0063',14,368,0,'operating','relicensing','A7:N0063b:incremental_capacity','McCloud-Pit relicense; +14 MW proposed (not built)'),
 ('N0078',11.4,266.1,0,'operating','relicensing','A7:N0078b:incremental_capacity','Drum-Spaulding/Yuba-Bear; +11.4 MW proposed'),
 ('R1032',1.3,82.3,0,'operating','relicensing','A7:R1032b:incremental_capacity','Toledo Bend +1.3 MW min-flow unit'),
 ('N0051',-4.6,0,-4.6,'unknown','continuation','A7:N0051b:incremental_capacity','Kilarc-Cow Creek license surrender (removal)'),
 ('N0067',0,112.5,0,'operating','relicensing','A7:N0067:nameplate_capacity','Merced relicense'),
 ('N0069',0,223.7,0,'operating','relicensing','A7:N0069:nameplate_capacity','Middle Fork American relicense (MW low conf)'),
 ('R0115',0,1003.3,0,'operating','relicensing','A7:R0115:nameplate_capacity','Boundary relicense'),
 ('R0604',0,182.5,0,'operating','relicensing','A7:R0604:nameplate_capacity','Martin Dam relicense'),
 ('R0660',0,19.62,0,'operating','relicensing','A7:R0660:nameplate_capacity','York Haven relicense'),
 ('R1001',0,25,0,'operating','relicensing','A7:R1001:nameplate_capacity','Swan Falls relicense'),
 ('R1119',0,774.3,0,'operating','relicensing','A7:R1119:nameplate_capacity','Wells relicense'),
 ('N0049',0,0,0,'operating','continuation','A7:N0049b:incremental_capacity','Kerr drought management plan (operations only)'),
]:
    e(i, m='HYDRO', v=inc, u='MW_incremental', b=b, st=st, ne=ne, ref=ref, p=dict(tech='HYDRO', existing_mw=ex), note=note)

# ---------------- TRANSMISSION (rated MW; purpose) ----------------
# kV-imputed ratings: AEP 'Transmission Facts' loadability (~1.0 SIL) 500 kV 900, 345 kV 400 MW; 230/115 kV SIL 132/33 (ND memo);
# 161/138 kV by V^2 scaling (A5, unverified). Imputed values flagged imp=True.
KV_RATING = {500: 900, 345: 400, 230: 132, 220: 120, 161: 65, 138: 48, 115: 33, 69: 12, 60: 9, 34.5: 3}
TX = [
 ('R1041',3000,'renew',3000,'under_construction','A7:R1041c:transmission_rating',False,'TransWest Express (BLM; USFS R1040 duplicate)'),
 ('R0287',1500,'renew',1500,'operating','A7:R0287c:transmission_rating',False,'Energy Gateway South (BLM; USFS R0286 duplicate)'),
 ('R0162',1250,'hydroimport',1250,'operating','A7:R0162c:transmission_rating',False,'Champlain Hudson Power Express (2026)'),
 ('R0768',4000,'renew',0,'cancelled','A7:R0768c:transmission_rating',False,'Plains & Eastern Clean Line (cancelled 2018)'),
 ('R0392',750,'hydroimport',750,'operating','A7:R0392c:transmission_rating',False,'Great Northern (Manitoba hydro, 2020)'),
 ('R0717',1090,'hydroimport',0,'cancelled','A7:R0717c:transmission_rating',False,'Northern Pass (cancelled 2019)'),
 ('R0681',1000,'hydroimport',0,'cancelled','URL:https://www.interconnection.fyi/project/isone-501',False,'New England Clean Power Link 1,000 MW import-only HVDC; withdrawn from ISO-NE queue (medium, secondary)'),
 ('R0111',1000,'reliab',1000,'under_construction','A7:R0111c:transmission_rating',False,'Boardman to Hemingway'),
 ('R1009',4500,'renew',4500,'operating','A7:R1009c:transmission_rating',False,'Tehachapi Renewable Transmission Project (2016)'),
 ('R0075',1000,'renew',1000,'operating','A7:R0075c:transmission_rating',False,'Barren Ridge (LADWP)'),
 ('R0966',1000,'renew',0,'predevelopment','A7:R0966c:transmission_rating',False,'Southline'),
 ('R0158',800,'renew',800,'operating','A7:R0158c:transmission_rating',False,'Central Ferry-Lower Monumental (wind)'),
 ('R0091',900,'renew',900,'operating','A7:R0091:voltage',True,'Big Eddy-Knight 500 kV (Columbia Gorge wind); rating imputed from kV'),
 ('R0349',900,'renew',900,'under_construction','A7:R0349:voltage',True,'Gateway West 500 kV; segments D.1/D.2 built ~2020; rating imputed from kV'),
 ('R0731',600,'reliab',600,'operating','A7:R0731c:transmission_rating',False,'ON Line (DOE LPO 600 MW); classed reliability/load-serving (less favorable to clean)'),
 ('R1125',4800,'overlap',4800,'operating','A7:R1125c:transmission_rating',False,'West of Devers upgrade: delivers Riverside East solar largely in this universe -> overlap (0 central)'),
 ('R0963',120,'overlap',120,'operating','A7:R0963:voltage',True,'Eldorado-Ivanpah 220 kV: serves Ivanpah/Stateline/Silver State (in universe) -> overlap'),
 ('R0052',900,'reliab',900,'operating','A7:R0052:voltage',True,'Susquehanna-Roseland 500 kV'),
 ('R0054',900,'reliab',900,'operating','A7:R0054:voltage',True,'APS Sun Valley-Morgan 500 kV'),
 ('R0634',900,'reliab',900,'operating','A7:R0634:voltage',True,'Mona-Oquirrh 500 kV'),
 ('N0046',900,'reliab',0,'cancelled','A7:N0046:voltage',True,'BPA I-5 Corridor 500 kV (cancelled 2017)'),
 ('R0047',400,'reliab',400,'operating','A7:R0047:voltage',True,'Antelope Valley-Neset 345 kV (Bakken load)'),
 ('R0426',400,'reliab',400,'operating','A7:R0426:voltage',True,'Hampton-Rochester-La Crosse 345 kV (CapX2020)'),
 ('R0932',400,'reliab',0,'unknown','A7:R0932:voltage',True,'Sigurd-Red Butte 345 kV'),
 ('R0085',132,'reliab',132,'operating','A7:R0085:voltage',True,'Bemidji-Grand Rapids 230 kV'),
 ('R0905',132,'reliab',0,'cancelled','A7:R0905:voltage',True,'San Luis 230 kV'),
 ('R0176',132,'reliab',0,'unknown','A7:R0176:voltage',True,'Tallahassee SW 230 kV'),
 ('R1008',132,'reliab',0,'unknown','A7:R1008:voltage',True,'Teckla-Osage-Rapid City 230 kV'),
 ('R1101',132,'reliab',0,'unknown','A7:R1101:voltage',True,'Vantage-Pomona Heights 230 kV'),
 ('R0503',65,'reliab',0,'unknown','A7:R0503:voltage',True,'Jack Rabbit-Big Sky 161 kV'),
 ('R1046',48,'reliab',0,'unknown','A7:R1046:voltage',True,'Tropic-Hatch 138 kV'),
 ('R0014',33,'reliab',0,'unknown','A7:R0014:voltage',True,'Albany-Eugene 115 kV rebuild'),
 ('R0452',33,'reliab',0,'unknown','A7:R0452:voltage',True,'Hooper Springs 115 kV'),
 ('R0139',9,'reliab',0,'unknown','A7:R0139:voltage',True,'CalPeco 60 kV upgrade'),
 ('R0531',3,'reliab',0,'unknown','A7:R0531:voltage',True,'Kirkwood Meadows 34.5 kV'),
 ('R0383',12,'reliab',0,'unknown','A7:R0383:voltage',True,'Granby/Windy Gap rebuild (kV not found; 69 kV assumed)'),
 ('R0520',12,'reliab',0,'unknown','A7:R0520:voltage',True,'Kake-Petersburg intertie (kV not found; 69 kV assumed)'),
 ('R0606',12,'reliab',0,'unknown','A7:R0606:voltage',True,'USFS power line replacements (kV not found; 69 kV assumed)'),
]
for i,v,purp,b,st,ref,imp,note in TX:
    e(i, m='TX', v=v, u='MW_rating', b=b, st=st, ne='new_build', ref=ref, imp=imp, p=dict(purpose=purp), note=note)
e('R0285', m='TX', v=155.1, u='MW_enabled', b=155.1, st='operating', ne='new_build', ref='URL:https://nadb.org/news/first-us-mexico-cross-border-wind-farm-inaugurated-in-tecate-baja-california', conf='medium', p=dict(purpose='gentie_ext', tech='WIND'),
  note='Energia Sierra Juarez gen-tie: enables ESJ wind (Mexico) phase 1, 155.1 MW, COD June 2015, PPA to SDG&E (NADB; search-result text, page not opened). Phase 2 (108 MW) status unknown; DOE permit caps transfer at 400 MW')
e('R0998', m='TX', v=3500, u='MW_enabled', b=3500, st='operating', ne='new_build', ref='A7:R0998c:transmission_rating', conf='medium', p=dict(purpose='gentie_ext', tech='WIND'),
  note='SunZia (3,000 MW rating) treated as gen-tie for the ~3.5 GW SunZia Wind project it was built for (review 2026-10-21; was renew x TX_ENABLE_RENEW)')
e('R0712', m='TX', v=104, u='MW_enabled', b=0, st='unknown', ne='new_build', ref='A7:R0712:voltage', conf='low', p=dict(purpose='gentie_ext', tech='WIND'), note='North Steens 230 kV gen-tie for Echanis wind (104 MW, private land); build status unknown')
e('R0286', m='DUP', v=0, u='', b=0, st='operating', ne='duplicate', ref='A7:R0286:voltage', p=dict(dup='R0287'), note='USFS EGS duplicate')
e('R1040', m='DUP', v=0, u='', b=0, st='under_construction', ne='duplicate', ref='A7:R1040:voltage', p=dict(dup='R1041'), note='USFS TWE duplicate')

# ---------------- CLEAN PROGRAMMATIC (RFD MW) ----------------
e('R0827', m='PROGCLEAN', v=23700, u='MW_rfd', b=0, st='implemented', ne='programmatic', ref='URL:https://www.doi.gov/news/pressreleases/Obama-Administration-Approves-Roadmap-for-Utility-Scale-Solar-Energy-Development-on-Public-Lands', conf='medium', p=dict(tech='PV'),
  note='Solar PEIS: DOI "if fully built out ... as much as 23,700 megawatts" (fetched) = upper bound; full potential; realization via shared REAL_PROG (review 2026-10-21)')
e('R0240', m='PROGCLEAN', v=7600, lo=7600, hi=19500, u='MW_rfd', b=0, st='implemented', ne='programmatic', ref='A6:R0240:rfd_capacity', p=dict(tech='PV'),
  note='DRECP LUPA: DFAs could supply ~8,100 MW (the BLM plan); 20,000 MW is the regional planning assumption (high). Minus Palen PV 500 MW (in universe) = 7,600 central; realization via REAL_PROG. Corrected 2026-10-21 per review; snippet-level (low)')
e('R1122', m='PROGCLEAN', v=3330, u='MW_rfd', b=0, st='implemented', ne='programmatic', ref='A6:R1122:rfd_capacity', p=dict(tech='PV'), note='West Chocolate Mtns REEA potential 3,330 MW solar (+150 geothermal ignored) = potential; realization via shared REAL_PROG')
e('R0861', m='PROGCLEAN', v=3330, u='MW_rfd', b=0, st='implemented', ne='programmatic', ref='A6:R0861:rfd_capacity', imp=True, conf='low', p=dict(tech='PV'),
  note='Restoration Design Energy Project RFD NOT FOUND; IMPUTED at the smallest documented clean-programmatic potential (3,330 MW); realization via REAL_PROG')
e('R1071', m='NOSIZE', v=0, u='', b=0, st='implemented', ne='programmatic', ref='A6:R1071:rfd_capacity', note='Upper Great Plains Wind PEIS: procedural framework, no MW scenario (unquantified)')
e('N0076', m='NOSIZE', v=0, u='', b=0, st='no ROD', ne='programmatic', ref='A6:N0076:rfd_capacity', note='Hawaii Clean Energy PEIS: no MW scenario, no ROD (unquantified)')

# ---------------- OFFSHORE LEASING (BOEM; program level carries emissions, sale EISs = COVERED) ----------------
e('R0824', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='A1:R0824f:oil_production_total',
  p=dict(oil=4203, oil_lo=1498, oil_hi=5510, gas=18222, gas_lo=6053, gas_hi=24339, life=45),
  note='2012-2017 Program as implemented (10 GOM WPA/CPA sales + Cook Inlet; EPA sales got no bids; Arctic sales cancelled): BOEM 2016 Table 6-4 low/high 2,896/5,510 MMbbl, 12,105/24,339 Bcf; central = midpoint; low = BOEM "adjusted" (GOM halved) low')
e('R0738', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='A1:R0738:oil_production_total',
  p=dict(oil=3740, oil_lo=2189, oil_hi=5928, gas=12104, gas_lo=5507, gas_hi=22271, life=55),
  note='2017-2022 Program PFP (GOM + Cook Inlet) Table 6-2, mid/low/high price; BOEM lifecycle 2,380 Mt (1,285-3,958); BOEM MarketSim net vs No Action ~ -14 Mt (not used: pre-2020 MarketSim, see methods)')
e('R0416', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='A1:R0416:oil_production_total',
  p=dict(oil=1212.5, oil_lo=801, oil_hi=1624, gas=4946, gas_lo=3332, gas_hi=6560),
  note='CPA Sale 216/222 (2012) implements the 2007-2012 Program (not in universe), so counted at sale level; 442 tracts leased')
for i in ['R0210','R0407','R0408','R0409','R0410','R0411','R0412','R0413','R0414','R0415','R0739']:
    e(i, m='COVERED', v=0, u='', b=0, st='implemented', ne='programmatic', ref=f'A1:{i}:oil_production_total' if i not in ('R0210',) else 'A1:R0210:oil_production_total',
      note='Lease-sale EIS tiered to a five-year Program in the universe (R0824 or R0738): production counted at Program level to avoid double counting')
e('R0667', m='NOSIZE', v=0, u='', b=0, st='implemented', ne='programmatic', ref='A1:R0667:area_available_for_leasing',
  note='NPR-A IAP (2013): 11.8 M acres available; ROD gives no production estimate; FEIS RFD not retrieved. UNQUANTIFIED fossil (biases toward clean; Willow lies in these lands)')
e('R0790', m='NOSIZE', v=0, u='', b=0, st='implemented', ne='programmatic', ref='A1:R0790:oil_production_rate_per_hypothetical_facility',
  note='Oil shale/tar sands allocation PEIS (2013): no RFD total; no commercial production. UNQUANTIFIED')
e('R0628', m='NOSIZE', v=0, u='', b=0, st='implemented', ne='programmatic', ref='URL:',
  note='Moab Master Leasing Plan (2016): not sized (missed by the first title pass; it mainly restricted leasing). UNQUANTIFIED')

# ---------------- ONSHORE FIELDS & LEASING (cumulative oil MMbbl, gas Bcf) ----------------
EUR_NOTE = 'gas IMPUTED as RFD wells x 1.0 Bcf/well (subsector-typical: GNB 0.96-1.28, Gasco 1.05 Bcf/well from those EISs)'
e('R0206', m='OG', v=1, u='cumulative', b=1, st='operating', ne='expansion', ref='A2:R0206c:gas_production_total', p=dict(gas=12000, gas_lo=5500, gas_hi=12000, oil=167.3),
  note='Continental Divide-Creston: 8,950 infill wells (ROD 2016); new-well EUR 12.0 Tcf, condensate 167.3 MMbbl')
e('R0393', m='OG', v=1, u='cumulative', b=1, st='operating', ne='expansion', ref='A2:R0393e:gas_production_total', p=dict(gas=6070, gas_hi=15440, oil=86.5),
  note='Greater Natural Buttes: 3,675 wells; 6.07 Tcf, 86.5 MMbbl (FEIS)')
e('R0643', m='OG', v=1, u='cumulative', b=1, st='operating', ne='expansion', ref='A2:R0643d:gas_production_total', p=dict(gas=7440, oil=345.0),
  note='Monument Butte: 5,750 wells; oil 334.9 + NGL 10.1 MMbbl; gas 0.54 + 6.9 Tcf')
e('R1060', m='OG', v=1, u='cumulative', b=0, st='predevelopment', ne='expansion', ref='A2:R1060c:gas_production_total', p=dict(gas=1370, gas_lo=1170, gas_hi=1990),
  note='Uinta Basin (Gasco) 1,298 wells; ROD: 1.37 Tcf; little development')
e('R1128', m='OG', v=1, u='cumulative', b=1, st='operating', ne='expansion', ref='A2:R1128:wells_approved', imp=True, p=dict(gas=626, gas_lo=313, gas_hi=801),
  note='West Tavaputs 626 wells; FEIS: ultimate recovery unknown; ' + EUR_NOTE)
e('R0835', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='A2:R0835:rfd_wells', imp=True, p=dict(gas=15040, gas_lo=4603, gas_hi=19250),
  note='White River FO RMPA RFD 15,040 wells/20 yr (Alt E); ' + EUR_NOTE + '; low = No Action wells')
e('R0787', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='A2:R0787c:rfd_wells', imp=True, p=dict(gas=376, gas_lo=188, gas_hi=444),
  note='WRNF previously issued leases: 37 retained, 25 cancelled; RFD 375.6 wells on retained leases; ' + EUR_NOTE)
e('R1139', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='A2:R1139b:rfd_wells', imp=True, p=dict(gas=487, gas_lo=258, gas_hi=1014),
  note='White River NF leasing availability: RFD 487 wells (258-1,014); ' + EUR_NOTE)
e('R0751', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='A2:R0751c:oil_production_total', p=dict(oil=412, oil_lo=0, oil_hi=412),
  note='Pawnee NG: NSO leasing; 590 MMbbl with leasing vs 178 from existing leases -> incremental 412 MMbbl (gas unit garbled in FEIS; omitted)')
e('R0316', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='A2:R0316c:oil_production_avg', p=dict(oil=16.4),
  note='Fishlake NF: full RFD avg 3,000 bbl/d x 15 yr = 16.4 MMbbl (frontier, little leasing interest)')


e('R0958', m='OG', v=1, u='cumulative', b=0, st='unknown', ne='expansion', ref='A2:R0958c:eur_per_well', conf='low', p=dict(oil=8.9, oil_lo=5.0, oil_hi=21.7),
  note='South Unit (Ashley NF) 356 wells x ~25 Mbbl historic EUR (5-61 Mbbl) = ~8.9 MMbbl (agent rough product, low)')
e('R0730', m='OG', v=1, u='cumulative', b=0, st='implemented', ne='programmatic', ref='A2:R0730:rfd_wells', imp=True, p=dict(oil=5.4, oil_lo=0, oil_hi=10.9),
  note='Dixie NF leasing RFD 80 wells (20 production); IMPUTED oil = 20 wells x 18,165 bbl/well/yr (Uinta NF FSEIS per-well assumption) x 15 yr')
e('R1061', m='NOSIZE', v=0, u='', b=0, st='implemented', ne='programmatic', ref='A2:R1061b:rfd_wells', note='Uinta NF leasing: RFD is 12 exploratory wells; no production scenario (negligible, unquantified)')


e('R0771', m='OG', v=1, u='cumulative', b=1, st='operating', ne='new_build', ref='A2:R0771:oil_production_peak', p=dict(oil=109.5, oil_lo=109.5, oil_hi=766.5),
  note='Point Thomson gas-condensate cycling (Corps ROD 2012; producing since 2016): 10,000 bbl/d condensate x 30 yr = 109.5 MMbbl; high = 70,000 bbl/d export-pipeline design; gas reinjected (no sales)')
e('R0127', m='OG', v=1, u='cumulative', b=0, st='unknown', ne='expansion', ref='A2:R0127:wells_approved', imp=True, p=dict(gas=146, gas_lo=55, gas_hi=187),
  note='Bull Mountain Unit MDP: framework for 146 gas wells (ROD 2017 approved one APD); no EUR in FEIS; ' + EUR_NOTE)

# ---------------- PENDING onshore items (A2 not yet returned) -> provisional NOSIZE, replaced below if sized ----------------
for i in ['R0127','R0958','R0920','R0771','R0730','R1061']:
    if i not in S:
        e(i, m='NOSIZE', v=0, u='', b=0, st='unknown', ne='expansion', ref='URL:', note='NOT SIZED: pending at close (sizing subagent did not return a value)')
# ---------------- OTHER bucket (tabulated, excluded from clean/fossil net) ----------------
import os as _os, pandas as _pd
_u = _pd.read_csv(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'universe.csv'))
for _i, _s in zip(_u.ceq_id, _u.subsector):
    if _i not in S and _u.loc[_u.ceq_id == _i, 'group'].iloc[0] == 'Other':
        e(_i, m='OTHER', v=0, u='', b=0, st='', ne='', ref='URL:', note='Other bucket: excluded from clean/fossil net; see A8_other.csv for characterization')
