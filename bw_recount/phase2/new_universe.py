"""Phase 2: hand-classified NEW energy EISs from the CEQ 2010-2024 workbook (not in the 2018 workbook).
Writes phase2/universe_new.csv. Same subsector scheme as Phase 1 plus 'OffshoreWind'.
dup_pooled = id of an earlier EIS for the same project (sized in its own era, zeroed in the pooled 2010-24 set)."""
import pandas as pd
b = pd.read_csv('phase2/ceq_2024_eis.csv').set_index('id24')
N = {}
def a(sub, ids, note='', dup=None):
    for i in ids.split(): N[i] = (sub, note, dup)
# fossil
a('Liquefaction', 'C1351 C1379 C1385 C1401 C1408 C1410 C1413 C1415 C1428 C1537 C1720 C1778')
a('Liquefaction', 'C1431', 'DOE/second listing of Plaquemines LNG', dup='C1428')
a('Liquefaction', 'C1498', 'Jordan Cove 2019 FEIS (re-application)', dup='R0515')
a('Pipeline', 'C1319 C1382 C1527 C1657 C1665 C1680 C1683 C1684 C1710 C1715 C1724 C1735 C1739 C1742 C1743 C1754 C1756 C1763 C1774 C1787 C1901 C1374 C1412')
a('Pipeline', 'C1662', 'North Baja XPress: deliveries largely to Mexico')
a('Pipeline', 'C1656 C1660 C1664 C1721 C1752', 'LNG-feed pipeline for a terminal in this universe (overlap)')
a('Pipeline', 'C1708 C1844', 'deepwater crude-oil export terminal')
a('Pipeline', 'C1307', 'Enefit oil-shale utility corridor (oil, gas, water, power ROWs)')
a('Pipeline', 'C1690 C1700', 'gas storage / compression relocation: no added throughput (unsized)')
a('Mine-Coal', 'C1326 C1364 C1397 C1589')
a('Mine-Gas', 'C1316 C1528 C1570 C1574 C1333 C1353')
a('Leasing-Fossil', 'C1480 C1560 C1790 C1429 C1591')
a('Leasing-Fossil', 'C1727', 'Cook Inlet Sale 258: tiered to the 2017-22 Program (R0738) -> covered')
a('GasPlant', 'C1736 C1810', 'TVA coal retirement replaced by gas combined cycle')
a('GasPlant', 'C1547', 'NJ TRANSITGRID gas-fired microgrid')
# clean
a('OffshoreWind', 'C1616 C1647 C1768 C1776 C1786 C1788 C1802 C1811 C1830 C1851 C1886')
a('Solar', 'C1485 C1502 C1504 C1514 C1578 C1631 C1686 C1694 C1718 C1738 C1850 C1881 C1885')
a('Wind', 'C1107', 'Na Pua Makani (FEIS 2016; in 2024 workbook only)')
a('Wind', 'C1438 C1516 C1543 C1666 C1834')
a('Wind', 'C1458 C1487', 'HCP/ITP covering existing wind farms (continuation)')
a('Geothermal', 'C1276 C1298 C1512', 'geothermal leasing availability (programmatic)')
a('Hydro', 'C1330 C1422 C1383 C1519 C1566 C1716')
a('Hydro', 'C1568', 'Columbia River System Operations (operations of existing dams)')
a('PumpStorage', 'C1380 C1533 C1809')
a('Nuclear', 'C1405', 'Clinch River early site permit (SMRs)')
a('Nuclear', 'C1707', 'Clinch River Advanced Nuclear Reactor Technology Park (same site as C1405)', dup='C1405')
a('Nuclear', 'C0203 C0271 C1355 C1361 C1515 C1849 C1894', 'nuclear licence renewal (continuation)')
a('Transmission', 'C1291 C1318 C1387 C1478 C1491 C1837 C1867 C1879')
a('Transmission', 'C1749', 'SunZia 2023 FEIS (route change)', dup='R0998')
a('Programmatic-Clean', 'C1863 C1880')
# other bucket
a('Waste', 'C1293 C1536 C1573 C1378 C1645 C1705 C1741 C1772')
a('Other-Energy', 'C1679 C1697 C1781 C1709 C1878 C1746', 'nuclear research/fuel, Army CHP')
a('Programmatic-Other', 'C1451 C1855', 'TVA IRP; NRC license-renewal GEIS revision')
a('Programmatic-FossilOther', 'C1593 C1794', 'WY pipeline corridors; Pacific OCS decommissioning')
a('Mine-Other', 'C1377 C1602 C1866', 'uranium ISR amendment; lithium mines')
a('Other-Energy', 'C1347 C1476', 'utility HCPs (transmission operations)')
GRP = {**{k: 'Clean' for k in ['Solar','Wind','OffshoreWind','Transmission','Hydro','Geothermal','Nuclear','PumpStorage','Programmatic-Clean']},
       **{k: 'Fossil' for k in ['Pipeline','Liquefaction','Regasification','GasPlant','CoalPlant','Mine-Coal','Mine-Gas','Leasing-Fossil']},
       **{k: 'Other' for k in ['Waste','Other-Energy','Programmatic-Other','Programmatic-FossilOther','Mine-Other','BioPlant','BioRefinery','CarbonCapture']}}
rows = []
for i, (s, note, dup) in N.items():
    r = b.loc[i]
    fy = pd.to_datetime(r.feis).year
    era = '2010-16' if fy <= 2016 else ('2017-20' if fy <= 2020 else '2021-24')
    rows.append(dict(ceq_id=i, subsector=s, group=GRP[s], programmatic=s in ('Leasing-Fossil','Programmatic-Clean','Programmatic-FossilOther','Programmatic-Other'),
                     duplicate_of='', dup_pooled=dup or '', note=note, title=r.title, agency=r.agency, state=r.state,
                     noi=str(r.noi)[:10], feis=str(r.feis)[:10], rod=str(r.rod)[:10], feis_year=fy, era=era, sheet='2024wb'))
u = pd.DataFrame(rows).sort_values(['group','subsector','ceq_id'])
u.to_csv('phase2/universe_new.csv', index=False)
print(len(u)); print(u.groupby(['era','group']).size().unstack(fill_value=0)); print(u.groupby(['group','subsector']).size().to_string())
