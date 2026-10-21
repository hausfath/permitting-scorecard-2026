T2 = "https://www.boem.gov/OCS-Lease-Sale-Statistics-GOM-Oil-and-Gas-Lease-Offerings/ (BOEM GOM Table 2 Lease Offerings; read via web.archive.org 2024 capture, last row = Sale 256)"
LD = "https://www.data.boem.gov/Leasing/Files/1221.pdf (BOEM Lease Data report, Gulf region, dated 02-Oct-2026)"
LDAK = "https://www.data.boem.gov/Leasing/Files/1221ak.pdf (BOEM Lease Data report, Alaska OCS Region, dated 01-Oct-2026)"
NEPA = "http://www.boem.gov/nepaprocess/ (GOM NEPA document index, via web.archive.org 2017)"
def W(u): return u + " (read via web.archive.org)"

MS12 = W("http://www.boem.gov/Environmental-Stewardship/Environmental-Assessment/NEPA/BOEM-2012-019_v1.aspx")
MS17 = W("https://www.boem.gov/BOEM-EIS-2017-009-v1/")
MS17v2 = W("https://www.boem.gov/BOEM-EIS-2017-009-v2/")

WPA_Q = "the proposed WPA lease sale is 0.116-0.200 billion barrels of oil (BBO) and 0.538-0.938 trillion cubic feet (Tcf) of gas"
CPA_Q = "a proposed CPA lease sale is 0.460-0.894 billion barrels of oil (BBO) and 1.939-3.903 trillion cubic feet (Tcf) of gas"

# Table 2 outcomes: sale: (date, area, tracts_offered, tracts_bid, tracts_leased, high_bids_$M, leased_bonus_$M)
T2D = {
 '222': ('6/20/2012','CGOM',7434,454,442,1704.5,1681.6),
 '229': ('11/28/2012','WGOM',3873,116,116,133.8,133.8),
 '227': ('3/20/2013','CGOM',7299,320,307,1214.7,1199.1),
 '233': ('8/28/2013','WGOM',4036,56,54,123.7,121.5),
 '231': ('3/19/2014','CGOM',7511,326,320,850.8,845.9),
 '225': ('3/19/2014','EGOM',134,0,0,0.0,0.0),
 '238': ('8/20/2014','WGOM',4026,81,80,110.0,109.1),
 '235': ('3/18/2015','CGOM',7788,169,161,538.8,533.1),
 '246': ('8/19/2015','WGOM',4083,33,33,22.7,22.7),
 '241': ('3/23/2016','CGOM',8349,128,116,156.4,139.7),
 '226': ('3/23/2016','EGOM',162,0,0,0.0,0.0),
 '248': ('8/24/2016','WGOM',4399,24,24,18.1,18.1),
 '247': ('3/22/2017','CGOM',9118,163,148,274.8,263.4),
 '249': ('8/16/2017','GOM',14220,90,81,121.1,110.9),
 '250': ('3/20/2018','GOM',14474,148,139,124.8,115.3),
 '251': ('8/15/2018','GOM',14622,144,141,178.1,175.5),
 '252': ('3/20/2019','GOM',14699,227,211,244.3,231.8),
 '253': ('8/21/2019 [Table 2 typo 8/2/12019]','GOM',14600,151,147,159.4,155.0),
 '254': ('3/18/2020','GOM',14641,71,63,93.1,86.2),
 '256': ('11/18/2020','GOM',14909,93,86,120.9,111.6),
}
# Lease-data status counts (Oct 2026) by sale no. (records incl. rejected high bids)
LDS = {
 '222': "453 records: PROD 3, UNIT 9, RELINQ 321, EXPIR 101, TERMIN 7, REJECT 12",
 '229': "116: RELINQ 107, TERMIN 5, EXPIR 4 (none producing)",
 '227': "320: PROD 8, UNIT 3, RELINQ 210, EXPIR 78, TERMIN 8, REJECT 13",
 '233': "53: UNIT 1, RELINQ 45, EXPIR 5, REJECT 2",
 '231': "325: PROD 1, UNIT 5, SOP 1, RELINQ 243, EXPIR 65, TERMIN 4, REJECT 6",
 '238': "81: RELINQ 75, EXPIR 5, REJECT 1 (none producing)",
 '235': "169: PROD 1, UNIT 1, OPERNS 1, RELINQ 114, EXPIR 44, REJECT 8",
 '246': "33: RELINQ 24, EXPIR 9 (none producing)",
 '241': "128: PROD 5, UNIT 2, OPERNS 1, PRIMRY 2, RELINQ 65, EXPIR 38, TERMIN 3, NO-EXE 4, REJECT 7",
 '248': "24: RELINQ 13, EXPIR 11 (none producing)",
 '247': "163: PROD 1, UNIT 9, PRIMRY 28, RELINQ 71, EXPIR 32, TERMIN 7, REJECT 10, other 5",
 '249': "90: PROD 2, UNIT 1, PRIMRY 30, RELINQ 34, EXPIR 14, REJECT 7",
 '250': "148: PROD 4, UNIT 2, PRIMRY 22, RELINQ 77, EXPIR 33, TERMIN 1, REJECT 9",
 '251': "144: UNIT 2, PRIMRY 15, RELINQ 92, EXPIR 32, REJECT 3",
 '252': "227: UNIT 6, PRIMRY 71, RELINQ 103, EXPIR 30, TERMIN 1, REJECT 15",
 '253': "151: PROD 1, UNIT 1, OPERNS 1, PRIMRY 54, RELINQ 77, EXPIR 13, REJECT 4",
 '254': "71: PROD 2, PRIMRY 15, RELINQ 39, EXPIR 7, REJECT 8",
 '256': "93: PROD 3, UNIT 2, PRIMRY 50, RELINQ 24, EXPIR 6, TERMIN 1, REJECT 7",
 '257': "308: PROD 1, PRIMRY 135, RELINQ 170, REJECT 1 (lease effective dates 10/01/2022)",
 '259': "313: PROD 1, UNIT 1, PRIMRY 193, RELINQ 100, REJECT 14 (effective mid-2023)",
 '261': "311: PRIMRY 245, RELINQ 54, REJECT 12 (effective early 2024)",
}

def outcome_txt(s):
    d = T2D[s]
    return f"Sale {s} ({d[1]}, {d[0]}): {d[2]:,} tracts offered, {d[3]} bid, {d[4]} leased, ${d[5]:,.1f}M high bids"

def outcome_row(cid, name, sales, status, year, extra_note="", conf="high"):
    held = [s for s in sales if s in T2D]
    quote = "; ".join(outcome_txt(s) for s in held)
    if len(quote) > 200:
        quote = "; ".join(f"{s}: {T2D[s][3]} bid/{T2D[s][4]} leased" for s in held)
    if len(quote) > 200:
        quote = "Tracts leased: " + ", ".join(f"{s}={T2D[s][4]}" for s in held)
    tracts = sum(T2D[s][4] for s in held)
    lds = "; ".join(f"{s}: {LDS[s]}" for s in sales if s in LDS)
    return dict(ceq_id=cid, project_name=name, metric="sale_outcome_tracts_leased", unit="tracts leased (sum over sales)",
                value_low="", value_central=tracts, value_high="", new_or_existing="new_build",
                status_2026=status, status_year=year, status_source_url=T2 + "; " + LD,
                source_url=T2, source_quote=quote, confidence=conf,
                notes=(extra_note + " Lease status Oct 2026 from BOEM lease data (PROD=producing; UNIT/OPERNS/SOP=held by unit/operations; PRIMRY=primary term, undeveloped; RELINQ/EXPIR/TERMIN=ended; REJECT=high bid rejected): " + lds).strip())

rows = []

# ---------- R0413 base 2012-2017 WPA/CPA multisale EIS ----------
N413 = "GOM 2012-2017 WPA Sales 229/233/238/246/248 & CPA Sales 227/231/235/241/247 Multisale FEIS (OCS EIS/EA BOEM 2012-019)"
rows += [
 dict(ceq_id="R0413", project_name=N413, metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=116, value_central="", value_high=200, new_or_existing="new_build", status_2026="operating", status_year=2017,
      status_source_url=T2, source_url=MS12 + " Ch.2/3, Table 3-1", source_quote=WPA_Q + " [WPA typical sale]",
      confidence="high",
      notes="STATUS CONVENTION: operating = sale(s) held and leases issued (not that leases produce); cancelled = cancelled or zero bids. Implements the 2012-2017 Program (R0824). WPA typical sale; CPA typical sale in R0413b. "
            "BOEM gives low-high only (no central). 40-year analysis period (2012-2051). BASE EIS for all 10 WPA/CPA sales; the supplemental EISs R0414, R0411, R0415, R0412, R0407 (CPA part), R0409, R0739 re-analyze subsets of these same sales with IDENTICAL per-sale ranges: count production once, here."),
 dict(ceq_id="R0413b", project_name=N413, metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=460, value_central="", value_high=894, new_or_existing="new_build", status_2026="operating", status_year=2017,
      status_source_url=T2, source_url=MS12 + " Ch.2/3, Table 3-1", source_quote=CPA_Q + " [CPA typical sale]",
      confidence="high", notes="CPA typical sale. Gas: 1,939-3,903 Bcf per CPA sale; WPA 538-938 Bcf per sale."),
 dict(ceq_id="R0413c", project_name=N413, metric="oil_production_total", unit="MMbbl",
      value_low=2880, value_central="", value_high=5470, new_or_existing="new_build", status_2026="operating", status_year=2017,
      status_source_url=T2, source_url=MS12, source_quote=WPA_Q + "; " + CPA_Q[:60] + "...",
      confidence="medium",
      notes="DERIVED: 5 WPA + 5 CPA typical sales = 5x(116-200) + 5x(460-894). Consistent with 2012-2017 PEIS GOM Table 4.4.1-1 'Potentially available oil (Bbbl) 2.7-5.4' (12 GOM sales incl. 2 EPA)."),
 dict(ceq_id="R0413d", project_name=N413, metric="gas_production_total", unit="Bcf",
      value_low=12385, value_central="", value_high=24205, new_or_existing="new_build", status_2026="operating", status_year=2017,
      status_source_url=T2, source_url=MS12, source_quote="WPA: 0.538-0.938 Tcf of gas [per sale]; CPA: 1.939-3.903 Tcf of gas [per sale]",
      confidence="medium", notes="DERIVED: 5x(538-938) + 5x(1,939-3,903) Bcf. PEIS GOM: 12-24 tcf."),
 outcome_row("R0413e", N413, ['229','233','238','246','248','227','231','235','241','247'], "operating", 2017,
      "All 10 sales held 2012-2017. Sum of tracts leased = 1,359."),
]

# ---------- R0416 216/222 SEIS (2007-2012 Program) ----------
N416 = "GOM 2012 CPA Lease Sale 216/222 Final SEIS (OCS EIS/EA BOEM 2012-058)"
S216 = W("http://www.boem.gov/BOEM-Newsroom/Library/Publications/2012/2012-058_vol_1-pdf.aspx")
rows += [
 dict(ceq_id="R0416", project_name=N416, metric="oil_production_total", unit="MMbbl",
      value_low=801, value_central="", value_high=1624, new_or_existing="new_build", status_2026="operating", status_year=2012,
      status_source_url=T2, source_url=S216 + " Ch.2/3 (Table 3-1)",
      source_quote="result of the proposed CPA lease sale is 0.801-1.624 billion barrels of oil (BBO) and 3.332-6.560 trillion cubic feet (Tcf) of gas",
      confidence="high",
      notes="FLAG: implements the 2007-2012 Program (third program, not R0824/R0738); Sales 216 and 222 combined into one sale held 6/20/2012. Supplements the 2007-2012 Multisale EIS (MMS 2007-018) and 2009-2012 SEIS (MMS 2008-041), which are outside this list. Gas 3,332-6,560 Bcf. 40-year analysis period. Downstream GHG not quantified."),
 dict(ceq_id="R0416b", project_name=N416, metric="gas_production_total", unit="Bcf", value_low=3332, value_central="", value_high=6560,
      new_or_existing="new_build", status_2026="operating", status_year=2012, status_source_url=T2, source_url=S216,
      source_quote="0.801-1.624 BBO and 3.332-6.560 Tcf of gas", confidence="high", notes="Single combined CPA sale 216/222."),
 outcome_row("R0416c", N416, ['222'], "operating", 2012, "Table 2 lists the combined sale as 222."),
]

# ---------- R0414 231/233 SEIS ----------
N414 = "GOM 2013-2014 WPA Sale 233 / CPA Sale 231 Final SEIS (OCS EIS/EA BOEM 2013-0118)"
S414 = W("http://www.boem.gov/uploadedFiles/BOEM/BOEM_Newsroom/Library/Publications/2013/BOEM%202013-0118.pdf")
rows += [
 dict(ceq_id="R0414", project_name=N414 + " - WPA Sale 233", metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=116, value_central="", value_high=200,
      new_or_existing="new_build", status_2026="operating", status_year=2014, status_source_url=T2, source_url=S414,
      source_quote="0.116-0.200 billion barrels of oil (BBO) and 0.538-0.938 trillion cubic feet (Tcf) of gas (Table 3-1 of the 2012-2017 WPA/CPA Multisale EIS)",
      confidence="high",
      notes="OVERLAP with R0413: re-analyzes Sales 231 and 233 using R0413's Table 3-1 ranges. Do not add to R0413. Gas 538-938 Bcf. Implements 2012-2017 Program."),
 dict(ceq_id="R0414c", project_name=N414 + " - CPA Sale 231", metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=460, value_central="", value_high=894,
      new_or_existing="new_build", status_2026="operating", status_year=2014, status_source_url=T2, source_url=S414,
      source_quote="Lease Sale 231 is 0.460-0.894 BBO and 1.939-3.903 Tcf of gas (Table 3-1 of the 2012-2017 WPA/CPA",
      confidence="high", notes="OVERLAP with R0413. Gas 1,939-3,903 Bcf."),
 outcome_row("R0414b", N414, ['233','231'], "operating", 2014),
]

# ---------- R0410 EPA 225/226 FEIS ----------
N410 = "GOM 2014 and 2016 EPA Lease Sales 225 and 226 Final EIS (OCS EIS/EA BOEM 2013-200)"
S410 = W("http://www.boem.gov/BOEM-2013-200-v1/")
rows += [
 dict(ceq_id="R0410", project_name=N410, metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=0, value_central="", value_high=71, new_or_existing="new_build", status_2026="cancelled", status_year=2016,
      status_source_url=T2, source_url=S410,
      source_quote="projected to be developed as a result of a proposed EPA lease sale is 0-0.071 billion barrels of oil (BBO) and 0-0.162 Tcf of gas ... over a 40-year period",
      confidence="high",
      notes="Gas 0-162 Bcf per sale; 40-year period. Implements 2012-2017 Program. Both sales HELD BUT RECEIVED ZERO BIDS (Table 2: 225 on 3/19/2014, 134 tracts offered; 226 on 3/23/2016, 162 tracts offered; 0 bid) => nothing leased, effective production 0. Sale 226 re-analyzed in R0407 (overlap). 2016-065 Sec 6.2: 'two lease sales held in the GOM Eastern Planning Area are not considered because no bids were received'."),
 outcome_row("R0410b", N410, ['225','226'], "cancelled", 2016, "Zero bids on both sales."),
]

# ---------- R0411 WPA 238/246/248 SEIS ----------
N411 = "GOM 2014-2016 WPA Lease Sales 238, 246, 248 Final SEIS (OCS EIS/EA BOEM 2014-009)"
rows += [
 dict(ceq_id="R0411", project_name=N411, metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=116, value_central="", value_high=200, new_or_existing="new_build", status_2026="operating", status_year=2016,
      status_source_url=T2, source_url=W("http://www.boem.gov/BOEM-2014-009/"),
      source_quote="(e.g., proposed WPA Lease Sale 238) is 0.116-0.200 billion barrels of oil (BBO) and 0.538-0.938 trillion cubic feet (Tcf) of gas",
      confidence="high", notes="OVERLAP with R0413 (same WPA typical-sale range); also overlaps R0412 (246, 248) and R0409 (248). Gas 538-938 Bcf per sale. 2012-2017 Program."),
 outcome_row("R0411b", N411, ['238','246','248'], "operating", 2016),
]

# ---------- R0415 CPA 235/241/247 SEIS ----------
N415 = "GOM 2015-2017 CPA Lease Sales 235, 241, 247 Final SEIS (OCS EIS/EA BOEM 2014-655)"
rows += [
 dict(ceq_id="R0415", project_name=N415, metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=460, value_central="", value_high=894, new_or_existing="new_build", status_2026="operating", status_year=2017,
      status_source_url=T2, source_url=W("http://www.boem.gov/BOEM-2014-655/"),
      source_quote="(i.e., proposed CPA Lease Sale 235) is 0.460-0.894 billion barrels of oil (BBO) and 1.939-3.903 trillion cubic feet (Tcf) of gas",
      confidence="high", notes="OVERLAP with R0413; also overlaps R0407 (241, 247) and R0739 (247). Gas 1,939-3,903 Bcf per sale. 2012-2017 Program."),
 outcome_row("R0415b", N415, ['235','241','247'], "operating", 2017),
]

# ---------- R0412 WPA 246/248 SEIS ----------
N412 = "GOM 2015 and 2016 WPA Lease Sales 246 and 248 Final SEIS (OCS EIS/EA BOEM 2015-008)"
rows += [
 dict(ceq_id="R0412", project_name=N412, metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=116, value_central="", value_high=200, new_or_existing="new_build", status_2026="operating", status_year=2016,
      status_source_url=T2, source_url=W("http://www.boem.gov/BOEM-2015-008/"),
      source_quote="(e.g., proposed WPA Lease Sale 246) is 0.116-0.200 billion barrels of oil (BBO) and 0.538-0.938 trillion cubic feet (Tcf) of gas",
      confidence="high", notes="OVERLAP with R0413 and R0411 (same sales 246, 248). 2012-2017 Program."),
 outcome_row("R0412b", N412, ['246','248'], "operating", 2016),
]

# ---------- R0407 CPA 241/247 + EPA 226 SEIS ----------
N407 = "GOM 2016 and 2017 CPA Lease Sales 241 and 247, EPA Lease Sale 226 Final SEIS (OCS EIS/EA BOEM 2015-033)"
rows += [
 dict(ceq_id="R0407", project_name=N407 + " - CPA Sales 241, 247", metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=460, value_central="", value_high=894, new_or_existing="new_build",
      status_2026="operating", status_year=2017, status_source_url=T2, source_url=W("http://www.boem.gov/BOEM-2015-033/"),
      source_quote="(i.e., proposed CPA Lease Sale 241) is 0.460-0.894 billion barrels of oil (BBO) and 1.939-3.903 trillion cubic feet (Tcf) of gas",
      confidence="high",
      notes="OVERLAP with R0413/R0415 (CPA 241, 247) and R0410 (EPA 226). 2012-2017 Program."),
 dict(ceq_id="R0407c", project_name=N407 + " - EPA Sale 226", metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=0, value_central="", value_high=71, new_or_existing="new_build",
      status_2026="cancelled", status_year=2016, status_source_url=T2, source_url=W("http://www.boem.gov/BOEM-2013-200-v1/"),
      source_quote="projected to be developed as a result of a proposed EPA lease sale is 0-0.071 billion barrels of oil (BBO) and 0-0.162 Tcf of gas",
      confidence="medium",
      notes="EPA range taken from R0410 (BOEM 2013-200), not re-verified in this SEIS. Sale 226 received ZERO bids => 0 production. OVERLAP with R0410."),
 outcome_row("R0407b", N407, ['241','247','226'], "operating", 2017, "EPA 226 received zero bids."),
]

# ---------- R0409 WPA 248 SEIS ----------
N409 = "GOM 2016 WPA Lease Sale 248 Final SEIS (OCS EIS/EA BOEM 2016-005)"
rows += [
 dict(ceq_id="R0409", project_name=N409, metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=116, value_central="", value_high=200, new_or_existing="new_build", status_2026="operating", status_year=2016,
      status_source_url=T2, source_url=W("http://www.boem.gov/BOEM-2016-005/"),
      source_quote="(e.g., proposed WPA Lease Sale 248) is 0.116-0.200 billion barrels of oil (BBO) and 0.538-0.938 trillion cubic feet (Tcf) of gas",
      confidence="high", notes="OVERLAP with R0413, R0411, R0412 (all cover Sale 248). Sale 248: 24 tracts leased, none producing Oct 2026 (13 relinquished, 11 expired). 2012-2017 Program."),
 outcome_row("R0409b", N409, ['248'], "operating", 2016),
]

# ---------- R0739 CPA 247 SEIS ----------
N739 = "GOM 2017 CPA Lease Sale 247 Final SEIS (OCS EIS/EA BOEM 2016-061)"
rows += [
 dict(ceq_id="R0739", project_name=N739, metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=460, value_central="", value_high=894, new_or_existing="new_build", status_2026="operating", status_year=2017,
      status_source_url=T2, source_url=W("http://www.boem.gov/BOEM-2016-061/"),
      source_quote="(i.e., proposed CPA Lease Sale 247) is 0.460-0.894 billion barrels of oil (BBO) and 1.939-3.903 trillion cubic feet (Tcf) of gas",
      confidence="high",
      notes="OVERLAP with R0413, R0415, R0407 (all cover Sale 247). Gas 1,939-3,903 Bcf. Last sale of the 2012-2017 Program (held 3/22/2017). SEIS states 'Downstream greenhouse gases are not quantified but are qualitatively' discussed."),
 outcome_row("R0739b", N739, ['247'], "operating", 2017),
]

# ---------- R0408 2017-2022 GOM multisale ----------
N408 = "GOM 2017-2022 Lease Sales 249-261 Final Multisale EIS (OCS EIS/EA BOEM 2017-009)"
rows += [
 dict(ceq_id="R0408", project_name=N408, metric="oil_production_total_per_typical_sale", unit="MMbbl per sale",
      value_low=211, value_central="", value_high=1118, new_or_existing="new_build", status_2026="operating", status_year=2023,
      status_source_url=T2 + "; " + LD, source_url=MS17 + " Ch.2.2.2.1, Table 3-1",
      source_quote="typical proposed regionwide lease sale are 0.211-1.118 billion barrels of oil (BBO) and 0.547-4.424 trillion cubic feet (Tcf) of gas (refer to Table 3-1)",
      confidence="high",
      notes="Implements the 2017-2022 Program (R0738). Per regionwide sale; 10 sales (249, 250, 251, 252, 253, 254, 256, 257, 259, 261). Table 3-1 'Lease Sale (2017-2066)' = 50-year life. 'a regionwide lease sale ... would represent 1.2-4.2 percent of the total OCS Program production in the GOM'. "
            "CAUTION: 10x typical-sale (2,110-11,180 MMbbl) exceeds the PEIS GOM program estimate (2,105-5,593 MMbbl; R0738); use the PEIS figure for the program total, not 10x. Lifecycle GHG only discussed qualitatively by reference to 2016-065 (Vol II p.4-26/27)."),
 dict(ceq_id="R0408b", project_name=N408, metric="gas_production_total_per_typical_sale", unit="Bcf per sale",
      value_low=547, value_central="", value_high=4424, new_or_existing="new_build", status_2026="operating", status_year=2023,
      status_source_url=T2, source_url=MS17 + " Table 3-1",
      source_quote="Table 3-1. Projected Oil and Gas in the Gulf of Mexico OCS ... Alternative A ... Lease Sale (2017-2066) Oil (BBO) 0.211-1.118 ... Gas (Tcf) 0.547-4.424",
      confidence="high", notes="OCS cumulative 2017-2086: 15.482-25.806 BBO, 57.875-108.513 Tcf (all OCS activity, not attributable to this EIS)."),
 dict(outcome_row("R0408c", N408, ['249','250','251','252','253','254','256','257','259','261'], "operating", 2023,
      "Table 2 (via 2024 capture) covers 249-256 (sum leased 868). Sales 257 (held 11/17/2021; vacated by court Jan 2022; leases issued under Inflation Reduction Act 2022 mandate - from memory, verify), 259 and 261 (held 2023 under IRA mandate - from memory, verify) are NOT in that Table 2 capture: from BOEM lease data, 257 = 307, 259 = 299, 261 = 299 non-rejected lease records (my count; medium confidence), so all-10-sale total = 1,773 leases. value_central = 868 (Table 2, sales 249-256) + 905 (my tally of lease records for 257/259/261 net of REJECT)."), value_central=1773, confidence="medium"),
]

# ---------- R0210 Cook Inlet 244 ----------
N210 = "Cook Inlet Planning Area Oil and Gas Lease Sale 244 (Final EIS, OCS EIS/EA BOEM 2016-069)"
CI = W("http://www.boem.gov/Cook-Inlet-Lease-Sale-244-Final-EIS-Volume-1/")
rows += [
 dict(ceq_id="R0210", project_name=N210, metric="oil_production_total", unit="MMbbl",
      value_low=150, value_central="", value_high=215, new_or_existing="new_build", status_2026="operating", status_year=2017,
      status_source_url=LDAK, source_url=CI + " Table 2.4.3-2 (E&D Scenario)",
      source_quote="Total Oil Production (MMbbl) 150-215; Total Gas Production (Bcf) 81-571; Peak Oil Rate (Mbbl/day) 68; Peak Gas Rate (MMcf/day) 181 ... Years of Activity 36-39",
      confidence="high",
      notes="FLAG: Sale 244 implements the 2012-2017 Program (FEIS abstract: 'a proposed oil and gas lease sale in the Final 2012-2017 Five-Year Oil and Gas Leasing Program'), not 2017-2022. E&D scenario: 215 MMbbl oil and 571 Bcf gas in two fields; production ~33 years after platforms installed. "
            "Held 6/21/2017 ('more than $3 million in high bids', BOEM Sale 244 page). BOEM AK lease data: 14 leases (Y02434-Y02447), ALL RELINQUISHED (2024 and Sept 2026) => no production ever; status 'operating' only per convention (sale held, leases issued)."),
 dict(ceq_id="R0210b", project_name=N210, metric="gas_production_total", unit="Bcf", value_low=81, value_central="", value_high=571,
      new_or_existing="new_build", status_2026="operating", status_year=2017, status_source_url=LDAK, source_url=CI,
      source_quote="undiscovered economic resource of approximately 215 million barrels (MMbbl) of oil, and 571 billion cubic feet (Bcf) of natural gas in two fields",
      confidence="high", notes=""),
 dict(ceq_id="R0210c", project_name=N210, metric="oil_production_peak", unit="bbl/d", value_low="", value_central=68000, value_high="",
      new_or_existing="new_build", status_2026="operating", status_year=2017, status_source_url=LDAK, source_url=CI,
      source_quote="Peak Oil Rate (Mbbl/day) 68; Peak Gas Rate (MMcf/day) 181", confidence="high",
      notes="Gas peak 181 MMcf/d (= 66 Bcf/yr). Upper end of scenario."),
 dict(ceq_id="R0210d", project_name=N210, metric="ghg_lifecycle_gross", unit="MtCO2e total", value_low="", value_central=129.2, value_high="",
      new_or_existing="new_build", status_2026="operating", status_year=2017, status_source_url=LDAK, source_url=CI + " Sec 4.3.1, Table 4.3.1-3",
      source_quote="estimates that 129,208,568 total metric tons of CO2e may be produced as a result of Lease Sale 244. Of this total, 98,530,000 metric tons would result from oil ... gas ... 30,678,000",
      confidence="high", notes="Mid-case lifecycle (Psarianos pers. comm. 10/24/16). Matches 2016-065 Cook Inlet magnitude order."),
 dict(ceq_id="R0210e", project_name=N210, metric="ghg_net_vs_noaction", unit="MtCO2e total", value_low="", value_central=-21.4, value_high="",
      new_or_existing="new_build", status_2026="operating", status_year=2017, status_source_url=LDAK, source_url=CI + " Table 4.3.1-3",
      source_quote="BOEM estimates that 150,570,000 total metric tons of CO2e may be produced from replacement energy sources under the No Action alternative, mid-case scenario",
      confidence="high", notes="DERIVED difference: 129.209 - 150.570 = -21.4 MtCO2e (Program minus No Action; negative = sale lower). No Action figure equals 2016-065 Table 8-1 Cook Inlet mid No Action (150,570 kt)."),
 dict(ceq_id="R0210f", project_name=N210, metric="sale_outcome_tracts_leased", unit="leases", value_low="", value_central=14, value_high="",
      new_or_existing="new_build", status_2026="operating", status_year=2017, status_source_url=LDAK, source_url=LDAK,
      source_quote="Y02434 ... Y02447 [14 leases] L RELINQ 09/17/2024 or 09/15/2026 ... effective 10/01/2017 ... SALE NO 244",
      confidence="high", notes="Count from BOEM lease data (my tally). Related 2017-2022 Program Cook Inlet Sale 258 (held Dec 2022 under IRA, not in this list): 1 lease, Y02448, relinquished 09/15/2026."),
]
