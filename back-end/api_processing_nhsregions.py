from requests import get
import pprint
import json
from json import dumps

ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
AREA_TYPE = ['region', 'nhsRegion']

AREA_NAME_REGION = ['London', 'East of England', 'East Midlands', 'West Midlands', 
                    'North East', 'North West', 'South East', 'South West', 'Yorkshire and the Humber']

AREA_NAME_NHSREGION = ['East of England', 'London', 'Midlands', 'North East and Yorkshire', 'North West', 'South East', 'South West']                  

Data_regions = {}

for j in range(len(AREA_NAME_NHSREGION)):
    
    filters = [
        f"areaType={ AREA_TYPE[1] }",
        f"areaName={ AREA_NAME_NHSREGION[j] }"
    ]
    ### valid metrics for nhsRegion:  
    ## "newAdmissions", "cumAdmissions", "cumAdmissionsByAge", "covidOccupiedMVBeds", "hospitalCases", 
    ## "transmissionRateGrowthRateMin", "transmissionRateGrowthRateMax", 

    structure = {
        "date": "date",
        "name": "areaName",
        "hospitalCases": "hospitalCases",
        "admissions": {
            "newAdmissions": "newAdmissions",
            "cumAdmissions": "cumAdmissions", 
            "cumAdmissionsByAge": "cumAdmissionsByAge"
        },
        "transmission": {
            "transmissionRateMin": "transmissionRateMin",
            "transmissionRateMax": "transmissionRateMax",
            "transmissionRateGrowthRateMin": "transmissionRateGrowthRateMin",
            "transmissionRateGrowthRateMax": "transmissionRateGrowthRateMax"
        },
        "covidOccupiedMVBeds":"covidOccupiedMVBeds"
    }

    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":"))
    }

    response = get(ENDPOINT, params=api_params, timeout=10)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    Data_regions[AREA_NAME_NHSREGION[j]] = response.json()   

    Master_data = {}

for i in Data_regions.keys():
    Data_holder = {}
    for j in range(Data_regions[i]['length']):
    
        date = str(Data_regions[i]['data'][j]['date'])
        hospitalCases = Data_regions[i]['data'][j]['hospitalCases']
        admissions = Data_regions[i]['data'][j]['admissions']
        transmission = Data_regions[i]['data'][j]['transmission']
        covidOccupiedMVBeds = Data_regions[i]['data'][j]['covidOccupiedMVBeds']  

        Data_holder[date] = {'hospitalCases': hospitalCases, 'admissions': admissions, 'transmission': transmission, 'covidOccupiedMVBeds': covidOccupiedMVBeds}
    
    Master_data[i] = Data_holder

## Create JSON

with open ('data/API_data_nhsregions.txt', 'w') as f:
    json.dump(Master_data, f)