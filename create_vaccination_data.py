import pandas as pd 
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

vacc_df = pd.read_csv('data/covid stats - weekly.csv')
print(vacc_df.iloc[0]['1801_1'])


print(vacc_df.head(7))

vacc_dict = {}

regions = ['East of England', 'London', 'Midlands', 'North East and Yorkshire', 'North West', 'South East', 'South West']
dates = ['1801', '1901', '2001', '2101', '2201']

for i, region in enumerate(regions):
    vacc_dict[region] = {}
    for date in dates:
        # print(date[2:], date[0:2])
        vacc_dict[region]['2021'+'-'+date[2:]+'-'+date[0:2]] = {}
        print(vacc_dict[region])
        vacc_dict[region]['2021'+'-'+date[2:]+'-'+date[0:2]]['cumPeopleReceivedFirstDose'] = int(vacc_df.iloc[i][f'{date}_1'].replace(',', '')) - int(vacc_df.iloc[i][f'{date}_2'].replace(',', ''))
        vacc_dict[region]['2021'+'-'+date[2:]+'-'+date[0:2]]['cumPeopleReceivedSecondDose'] = int(vacc_df.iloc[i][f'{date}_2'].replace(',', ''))
        vacc_dict[region]['2021'+'-'+date[2:]+'-'+date[0:2]]['cumVaccinesGiven'] = int(vacc_df.iloc[i][f'{date}_cum'].replace(',', ''))

pp.pprint(vacc_dict)
with open("data/vacc_json.txt", "w") as f:
    json.dump(vacc_dict, f)
