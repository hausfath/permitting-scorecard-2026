"""Candidate energy EISs from the CEQ Dec-2018 workbook, with a primary B&W-subsector guess (from title)
and allowed alternates. 'NONE' = not in B&W's 171. Used by reconstruct_bw.py."""
T = {'Solar':(22,2.42),'Wind':(13,3.55),'Transmission':(42,3.82),'Hydro':(14,4.72),'Geothermal':(3,2.04),
     'Nuclear':(2,6.27),'PumpStorage':(1,5.51),'Pipeline':(18,2.13),'Liquefaction':(7,3.73),'Regasification':(1,3.39),
     'GasPlant':(2,1.67),'CoalPlant':(2,2.00),'Mine-Coal':(4,6.99),'Mine-Gas':(6,6.95),'Energy-Programmatic':(15,3.23),
     'Waste':(8,5.30),'BioPlant':(2,3.70),'BioRefinery':(1,1.71),'CarbonCapture':(2,2.09),'Mine-Other':(4,4.63),'Other-Energy':(2,2.70)}
GROUP = {**{k:'Clean' for k in ['Solar','Wind','Transmission','Hydro','Geothermal','Nuclear','PumpStorage']},
         **{k:'Fossil' for k in ['Pipeline','Liquefaction','Regasification','GasPlant','CoalPlant','Mine-Coal','Mine-Gas']},
         **{k:'Other' for k in ['Energy-Programmatic','Waste','BioPlant','BioRefinery','CarbonCapture','Mine-Other','Other-Energy']}}
C = {}
def add(primary, ids, alts=()):
    for i in ids.split():
        C[i] = (primary, tuple(alts))
# --- clean
add('Solar', 'R0024 R0110 R0136 R0168 R0239 R0314 R0370 R0475 R0501 R0607 R0631 R0726 R0746 R0933 R0944 R0946 R0983 R1036 R0011 R0517 R0860 R0846 R0870 R0750 N0096', ['NONE'])
add('NONE', 'N0062', ['Solar'])
add('NONE', 'R0476', ['Solar','Other-Energy'])
add('Wind', 'R0023 R0174 R0633 R0725 R0912 R1121 R0235 R0336 R0422 R0499 R0390 R0480 R0949 R1138', ['NONE','Transmission'])
add('NONE', 'R0262', ['Wind'])
add('Transmission', 'R0014 R0047 R0052 R0054 R0075 R0085 R0091 R0111 R0139 R0158 R0162 R0176 R0285 R0286 R0287 R0349 R0383 R0392 R0426 R0452 R0503 R0520 R0531 R0606 R0634 R0717 R0731 R0768 R0905 R0932 R0963 R0966 R0998 R1008 R1009 R1040 R1041 R1046 R1101 R1125 N0046', ['NONE','Wind'])
add('Transmission', 'R0267 R0712', ['Wind','NONE'])
add('NONE', 'R0423 R0601', ['Transmission'])
add('NONE', 'R0402', ['Transmission','GasPlant','Other-Energy'])
add('Hydro', 'R0079 R0115 R0604 R0660 R1001 R1002 R1032 R1119 N0049 N0051 N0063 N0067 N0069 N0078', ['NONE'])
add('NONE', 'R0569 R0533 R0061 R0179 R0626 R0320 R0497 R0442 R0588 R0072 R1068 R1069 R0230 R0166 R0858', ['Hydro'])
add('Geothermal', 'R0149 R0897 R0371', ['NONE','Energy-Programmatic'])
add('Nuclear', 'R0263 R0288 R0553 R0701 R0956 R1053 R1107 R1110 R1145 N0016 N0021 N0022', ['NONE'])
add('NONE', 'R0352 R0353 R0354 R0355 R0356 R0357 R0358 R0359 R0360 R0361 R0362 R0363 R0364 R0365 R0366 R0367 R0368 N0072 N0038', ['Nuclear','Energy-Programmatic'])
add('PumpStorage', 'R0260', ['NONE'])
# --- fossil
add('Pipeline', 'R0017 R0050 R0063 R0066 R0202 R0550 R0651 R0652 R0683 R0693 R0753 R0880 R0887 R0890 R0931 R0961 N0050 N0004', ['NONE'])
add('Pipeline', 'R0889 R1063', ['NONE'])
add('Pipeline', 'R0515', ['Liquefaction','NONE'])
add('Liquefaction', 'R0141 R0216 R0340 R0380 R0540 R0593 R0255', ['NONE','Regasification'])
add('Liquefaction', 'R0773', ['Regasification','NONE'])
add('Regasification', 'R0009 R0772', ['Liquefaction','NONE'])
add('GasPlant', 'R0233 R0526', ['CoalPlant','NONE','Other-Energy'])
add('CoalPlant', 'R0342 R1016', ['CarbonCapture','GasPlant','NONE'])
add('NONE', 'R0334', ['CoalPlant','Mine-Coal'])
add('Mine-Coal', 'R0125 R0272 R1154 R0304 R0305 N0043 R0892 R1000', ['NONE','Energy-Programmatic'])
add('NONE', 'R0704 R0990 R0187', ['Mine-Coal','Energy-Programmatic','Mine-Other'])
add('Mine-Gas', 'R0206 R0393 R0643 R1060 R1128 R0127 R0958 R0920 R0771', ['NONE','Energy-Programmatic','Other-Energy'])
add('Energy-Programmatic', 'R0835 R0316 R0730 R0751 R1061 R1139 R0787 R0667 R0095 N0028 R0867 R0668', ['Mine-Gas','NONE'])
# --- other
add('Energy-Programmatic', 'R0210 R0407 R0408 R0409 R0410 R0411 R0412 R0413 R0414 R0415 R0416 R0738 R0739 R0824 R0804 N0039', ['NONE'])
add('Energy-Programmatic', 'R0240 R0861 R1122 R0790 R1013 N0076', ['NONE'])
add('Energy-Programmatic', 'R0827', ['NONE','Solar'])
add('Energy-Programmatic', 'R1071', ['NONE','Wind'])
add('Energy-Programmatic', 'R0828', ['NONE','Mine-Other'])
add('Energy-Programmatic', 'N0075 R0796 R0797', ['NONE','BioPlant'])
add('Waste', 'R0428 R1129 N0025 R0852 R0201 R0128 R0922 N0056 R0832', ['NONE'])
add('Waste', 'R0793', ['NONE','Energy-Programmatic'])
add('Waste', 'N0007', ['NONE','BioPlant'])
add('NONE', 'R0935 R1156 R0185 R0204 R0205', ['Waste'])
add('BioPlant', 'R0101', ['NONE'])
add('NONE', 'R0910', ['BioPlant','GasPlant','Other-Energy'])
add('BioRefinery', 'R0008', ['NONE'])
add('CarbonCapture', 'R0539 R1111', ['NONE'])
add('Mine-Other', 'R0067 R0245 R0576 R0644 R0694 R0988 R0346 R0575 R0923', ['NONE'])
add('NONE', 'R0261 R0350 R0319 R0716 R0438 R0723', ['Mine-Other'])
add('Other-Energy', 'R0451', ['NONE'])
