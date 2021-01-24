import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('data/data_merged_regions.txt') as file:
    data_merged = json.load(file)

print(data_merged.keys())

with open('data/API_data_nhsregions.txt') as file:
    data_nhs_region = json.load(file)

#print(data_nhs_region.keys())

#print(data_merged['london'].keys())
#print(data_nhs_region['london'].keys())

#print(data_merged['london']['2021-01-22'].keys())
#print(data_nhs_region['london']['2021-01-22'].keys())

#print(len(data_merged['london']))
#print(len(data_nhs_region['london']))

for i in data_merged.keys():
    dates_merged = data_merged[i].keys()
    dates_nhs_region = data_nhs_region[i].keys()

    for j in dates_merged:
        for k in dates_nhs_region:
            if j == k:
                data_merged[i][j].update(data_nhs_region[i][j])
            else:
                pass       

with open ('data/collated_data_final.txt', 'w') as f:
    json.dump(data_merged, f)





