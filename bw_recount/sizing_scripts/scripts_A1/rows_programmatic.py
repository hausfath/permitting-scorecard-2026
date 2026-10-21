OSTS_CH4 = "http://ostseis.anl.gov/documents/peis2012/chp/OSTS_Chapter_4.pdf (2012 OSTS Proposed RMP Amendments/Final PEIS Ch.4; read via web.archive.org)"
OSTS_ES = "http://ostseis.anl.gov/documents/peis2012/chp/OSTS_Executive_Summary.pdf (via web.archive.org)"
NPRA_ROD = "https://www.blm.gov/epl-front-office/projects/nepa/5251/42462/45213/NPR-A_FINAL_ROD_2-21-13.pdf (NPR-A IAP ROD Feb 2013; via web.archive.org)"
GOMREF = "BOEM 2017-009 Multisale EIS Vol II reference list (cites 'Atlantic OCS proposed geological and geophysical activities ... final programmatic environmental impact statement ... OCS EIS/EA BOEM 2014-001')"

rows = [
 dict(ceq_id="R0790", project_name="PROGRAMMATIC - Allocation of Oil Shale and Tar Sands Resources (CO, UT, WY) 2012 Final PEIS / 2013 ROD",
      metric="oil_production_rate_per_hypothetical_facility", unit="bbl/d per facility",
      value_low=25000, value_central="", value_high=50000, new_or_existing="programmatic", status_2026="predevelopment", status_year=2013,
      status_source_url="", source_url=OSTS_CH4 + " Sec 4.1",
      source_quote="Future production levels ... are unknown ... assumed that surface or underground mining based operations would produce at ... 25,000 to 30,000 bbl/day and in situ ... 30,000 to 50,000 bbl/day",
      confidence="high",
      notes="Allocation (land-use plan amendment) decision only; NO reasonably foreseeable development total or number of facilities given. Preferred/Proposed Plan Alt 2(b): 676,967 acres available for oil shale (RD&D-first) and 129,567 acres for tar sands (ES). 2008 PEIS had assumed 50,000 (mining) and 200,000 (in situ) bbl/d. "
            "No commercial federal oil shale/tar sands production is known to have resulted (status from general knowledge, not verified; treat as predevelopment). Do not weight by production."),
 dict(ceq_id="R0667", project_name="National Petroleum Reserve-Alaska (NPR-A) Integrated Activity Plan 2012 FEIS / Feb 2013 ROD",
      metric="area_available_for_leasing", unit="million acres",
      value_low="", value_central=11.8, value_high="", new_or_existing="programmatic", status_2026="operating", status_year=2013,
      status_source_url="", source_url=NPRA_ROD,
      source_quote="makes approximately 11.8 million acres of the approximately 22.8 million acres of subsurface ... available ... contain nearly three-fourths of estimated economically recoverable oil",
      confidence="high",
      notes="Production/RFD estimate NOT FOUND: the ROD gives no bbl/d; the FEIS RFD scenario (likely Vol 1 Ch.4 / appendix on eplanning project 5251) was not retrieved. ROD context: USGS 2010 cut NPR-A technically recoverable oil ~90% 'from approximately 10 billion barrels to less than 1 billion barrels'. "
            "Land-use allocation plan governing subsequent annual NPR-A lease sales (and later projects such as GMT-1/GMT-2/Willow, which had their own EISs); superseded by the 2020 IAP, then 2022 reinstatement of 2013 IAP (from memory, verify). status 'operating' = plan in effect and leasing occurred."),
 dict(ceq_id="R0804", project_name="PROGRAMMATIC - Atlantic OCS G&G Activities, Mid- and South Atlantic Planning Areas Final PEIS (OCS EIS/EA BOEM 2014-001)",
      metric="no_production_decision", unit="n/a", value_low="", value_central="", value_high="", new_or_existing="programmatic",
      status_2026="unknown", status_year=2014, status_source_url="", source_url=GOMREF,
      source_quote="Atlantic OCS proposed geological and geophysical activities; Mid-Atlantic and South-Atlantic planning areas--final programmatic environmental impact statement. 3 vols. ... OCS EIS/EA BOEM 2014-001",
      confidence="medium",
      notes="Characterization only: authorizes/frames G&G (seismic, HRG, geotechnical) survey permitting; no leasing or production decision; no production estimate expected. Atlantic planning areas were not included in the 2017-2022 PFP (R0738), so no Atlantic leasing followed. Document itself not opened."),
 dict(ceq_id="N0039", project_name="Geological and Geophysical Activities on the Gulf of Mexico OCS (Final Programmatic EIS, 2017)",
      metric="no_production_decision", unit="n/a", value_low="", value_central="", value_high="", new_or_existing="programmatic",
      status_2026="unknown", status_year=2017, status_source_url="", source_url="",
      source_quote="", confidence="low",
      notes="Characterization only (document not opened; based on CEQ title): programmatic analysis of G&G survey activity (seismic etc.) supporting permitting in the GOM; no ROD in CEQ list; no production decision. Production attributable to GOM leasing is already in R0738/R0408/R0413; do not add."),
 dict(ceq_id="N0028", project_name="NOAA/NMFS Effects of Oil and Gas Activities in the Arctic Ocean (Final EIS, Oct 2016)",
      metric="no_production_decision", unit="n/a", value_low="", value_central="", value_high="", new_or_existing="programmatic",
      status_2026="unknown", status_year=2016, status_source_url="", source_url="",
      source_quote="", confidence="low",
      notes="Characterization only (document not opened): NMFS EIS for issuing MMPA incidental take authorizations for seismic surveys and exploratory drilling in the Beaufort/Chukchi Seas; no leasing or production decision. Arctic OCS sales were dropped from both the 2012-2017 (as implemented) and 2017-2022 programs, and Chukchi leases were nearly all relinquished by 2016 (per R0738 PFP text). Effective production ~0."),
]
