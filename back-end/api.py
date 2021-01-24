from flask import Flask, request, render_template, jsonify
import json
from infection_vaccination_graph import historical_data, days_herd_immunity, vaccinated_population

app = Flask(__name__)

@app.route('/api', methods=['GET','POST'])
def api():
    # step 1
<<<<<<< HEAD
=======
    if request.method=="GET":
        return jsonify('hello')
>>>>>>> 0c27b4d4845eeb61017f186ae87cda6e02ba483c
    if request.method=="POST":
        data_frontend = request.get_json() # parses as json
        region = data_frontend["region"]
        age = data_frontend["age"]
        handwash = data_frontend["wash"]
        # vacDose = data_frontend["vacDose"]

    everything = {}

    # GET THE HISTORICAL DATA PER NHSREGION
    n_days = 7 # default
    nhsregion_dict = historical_data(n_days, region) # for a single region

  #  print('0')
  #  print(nhsregion_dict.keys())

    # GET THE NUMBER OF DAYS TILL HERD IMMUNITY PER NHSREGION
    herd_imm_dict = days_herd_immunity()
    herd_imm_dict = herd_imm_dict[region]
    #print('1')
   # print(herd_imm_dict)

    percent_pop_vacc = vaccinated_population()
    percent_pop_vacc = percent_pop_vacc[region]

    # COMBINE THE TWO
    # for region in herd_imm_dict.keys():
    #     nhsregion_dict[region]['herd_imm_days'] = herd_imm_dict[region]
    #     nhsregion_dict[region]['percent_vacc'] = percent_pop_vacc[region]

    nhsregion_dict['herd_imm_days'] = herd_imm_dict
    nhsregion_dict['percent_vacc'] = [percent_pop_vacc]

    # nhsregion_dict = json.dumps(nhsregion_dict, indent = 4)

    return nhsregion_dict
    