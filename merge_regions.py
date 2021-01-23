import pandas as pd
import json
import pprint

# Merging regions into NHS regions

with open('data/API_data_regions.txt') as file:
    data = json.load(file)

pp = pprint.PrettyPrinter(indent=4)

# pp.pprint(data_regions.keys())

data['midlands'] = {}

print(data['east midlands']['2021-01-22']['cases']['daily'])

print(len(data['west midlands']))

east_dates = data['east midlands'].keys()
west_dates = data['west midlands'].keys()

for date in east_dates:
    if date in west_dates:
        data['midlands'][date] = {}

        data['midlands'][date]['cases'] = {}
        for case_type in data['east midlands'][date]['cases'].keys():
            try:
                data['midlands'][date]['cases'][case_type] = data['east midlands'][date]['cases'][case_type] + data['west midlands'][date]['cases'][case_type]
            except:
                data['midlands'][date]['cases'][case_type] = 0

        data['midlands'][date]['deaths'] = {}
        for case_type in data['east midlands'][date]['deaths'].keys():
            try: 
                data['midlands'][date]['deaths'][case_type] = data['east midlands'][date]['deaths'][case_type] + data['west midlands'][date]['deaths'][case_type]
            except:
                data['midlands'][date]['deaths'][case_type] = 0
                
data['north east and yorkshire'] = {}

ne_dates = data['north east'].keys()
yh_dates = data['yorkshire and the humber'].keys()

for date in ne_dates:
    if date in yh_dates:
        data['north east and yorkshire'][date] = {}

        data['north east and yorkshire'][date]['cases'] = {}
        for case_type in data['north east'][date]['cases'].keys():
            try:
                data['north east and yorkshire'][date]['cases'][case_type] = data['north east'][date]['cases'][case_type] + data['yorkshire and the humber'][date]['cases'][case_type]
            except:
                data['north east and yorkshire'][date]['cases'][case_type] = 0


        data['north east and yorkshire'][date]['deaths'] = {}
        for case_type in data['east midlands'][date]['deaths'].keys():
            try:
                data['north east and yorkshire'][date]['deaths'][case_type] = data['north east'][date]['deaths'][case_type] + data['yorkshire and the humber'][date]['deaths'][case_type]
            except:
                data['north east and yorkshire'][date]['deaths'][case_type] = 0

data.pop('east midlands')
data.pop('west midlands')
data.pop('north east')
data.pop('yorkshire and the humber')

print(data.keys())

with open('data/data_merged_regions.txt', 'w') as file:
    json.dump(data, file)
