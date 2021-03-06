from flask import Flask, request, render_template
import json
from infection_vaccination_graph import historical_data, days_herd_immunity, vaccinated_population

def test_api():
    everything = {}
    region = 'East of England'

    # GET THE HISTORICAL DATA PER NHSREGION
    n_days = 7 # default
    nhsregion_dict = historical_data(n_days, region) # for a single region

    print('0')
    print(nhsregion_dict.keys())

    # GET THE NUMBER OF DAYS TILL HERD IMMUNITY PER NHSREGION
    herd_imm_dict = days_herd_immunity()
    herd_imm_dict = herd_imm_dict[region]
    print('1')
    print(herd_imm_dict)

    percent_pop_vacc = vaccinated_population()
    percent_pop_vacc = percent_pop_vacc[region]

    # COMBINE THE TWO
    # for region in herd_imm_dict.keys():
    #     nhsregion_dict[region]['herd_imm_days'] = herd_imm_dict[region]
    #     nhsregion_dict[region]['percent_vacc'] = percent_pop_vacc[region]

    nhsregion_dict['herd_imm_days'] = [herd_imm_dict]
    nhsregion_dict['percent_vacc'] = [percent_pop_vacc]

    # nhsregion_dict = json.dumps(nhsregion_dict, indent = 4)

    return nhsregion_dict

def pythonify(json_data):
    for key, value in json_data.items():
        if isinstance(value, list):
            value = [ pythonify(item) if isinstance(item, dict) else item for item in value ]
        elif isinstance(value, dict):
            value = pythonify(value)
        # try:
        #     newkey = int(key)
        #     del json_data[key]
        #     key = newkey
        # except TypeError:
        #     pass
        json_data[key] = value
    return json_data

ans = test_api()
ans = pythonify(ans)
for key in ans.keys():
    print(key)
    try:
        for k in ans[key].keys():
            print(type(k))
            # print(type(ans[key][k]))
    except:
        pass

    print(type(ans[key]))