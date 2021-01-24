import json
EoE = [892627,1026193,411211,341267,231706,461940,213052,275882,571713,598034,310040,264220,177744,395918,183125,174341]
London = [329771,190034,341806,185143,251160,306870,271523,227412,1510806,212906,290841,259552,353134,305222,324745,276983,1819271, 1504810]
Mid = [137595,129944,219600,226837,157308,264651,323136,179854,1026426,761224,1043665,338592,354224,407490,321596,506073,285478,263357,1180567,480456,273851,195147,788587,736219]
NEandY = [246866,117459,311890,265411,584853,207913,322434,150976,277705,504875,319371,530094,675944,318400,259778,159563,172292,366072,428231,211455,246604,193183,348312,793139,590901]
NW = [287550,190990,222412,237110,258834,293423,260063,237354,328662,552858,129410,150862,498042,160226,116184,180585,210014,324011,727223,149696,139446,178547,382746,114306,194337,203825,332696]
SE = [1860111,211709,96564,436701,201071,141771,225387,214905,217701,252520,570799,676171,491349,546626,1049170,290885,557229,857166]
SW =[571802,1200739,562225,963522,921917,773839,637070]
pop_EoE = sum(EoE)
pop_London = sum(London) 
pop_Mid = sum(Mid)
pop_NEandY = sum(NEandY)
pop_NW = sum(NW)
pop_SE = sum(SE)
pop_SW = sum(SW)

populations = {"East of England": pop_EoE, "London": pop_London, "Midlands": pop_Mid, "North East and Yorkshire": pop_NEandY, 
               "North West": pop_NW, "South East": pop_SE, "South West": pop_SW}
print(populations)

with open("data/populations_json.txt", "w") as f:
    json.dump(populations, f)