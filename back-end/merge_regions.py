import pandas as pd
import json
import pprint

# Merging regions into NHS regions

with open('data/API_data_regions.txt') as file:
    data = json.load(file)

pp = pprint.PrettyPrinter(indent=4)

# pp.pprint(data_regions.keys())

data['Midlands'] = {}

print(data['East Midlands']['2021-01-22']['cases']['daily'])

print(len(data['West Midlands']))

east_dates = data['East Midlands'].keys()
west_dates = data['West Midlands'].keys()

for date in east_dates:
    if date in west_dates:
        data['Midlands'][date] = {}

        data['Midlands'][date]['cases'] = {}
        for case_type in data['East Midlands'][date]['cases'].keys():
            try:
                data['Midlands'][date]['cases'][case_type] = data['East Midlands'][date]['cases'][case_type] + data['West Midlands'][date]['cases'][case_type]
            except:
                data['Midlands'][date]['cases'][case_type] = 0

        data['Midlands'][date]['deaths'] = {}
        for case_type in data['East Midlands'][date]['deaths'].keys():
            try: 
                data['Midlands'][date]['deaths'][case_type] = data['East Midlands'][date]['deaths'][case_type] + data['West Midlands'][date]['deaths'][case_type]
            except:
                data['Midlands'][date]['deaths'][case_type] = 0
                
data['North East and Yorkshire'] = {}

ne_dates = data['North East'].keys()
yh_dates = data['Yorkshire and the Humber'].keys()

for date in ne_dates:
    if date in yh_dates:
        data['North East and Yorkshire'][date] = {}

        data['North East and Yorkshire'][date]['cases'] = {}
        for case_type in data['North East'][date]['cases'].keys():
            try:
                data['North East and Yorkshire'][date]['cases'][case_type] = data['North East'][date]['cases'][case_type] + data['Yorkshire and the Humber'][date]['cases'][case_type]
            except:
                data['North East and Yorkshire'][date]['cases'][case_type] = 0


        data['North East and Yorkshire'][date]['deaths'] = {}
        for case_type in data['East Midlands'][date]['deaths'].keys():
            try:
                data['North East and Yorkshire'][date]['deaths'][case_type] = data['North East'][date]['deaths'][case_type] + data['Yorkshire and the Humber'][date]['deaths'][case_type]
            except:
                data['North East and Yorkshire'][date]['deaths'][case_type] = 0

data.pop('East Midlands')
data.pop('West Midlands')
data.pop('North East')
data.pop('Yorkshire and the Humber')

print(data.keys())

with open('data/data_merged_regions.txt', 'w') as file:
    json.dump(data, file)
