from flask import Flask, request, render_template
import json
from infection_vaccination_graph import historical_data, days_herd_immunity, vaccinated_population

app = Flask(__name__)

@app.route('/api', methods=['GET','POST'])
def api():
    # step 1
    if request.method=="GET":
        return 'hello'
    if request.method=="POST":
        data_frontend = request.get_json() # parses as json

        region = data_frontend["region"]
        age = data_frontend["age"]
        handwash = data_frontend["wash"]
        # vacDose = data_frontend["vacDose"]

    everything = {}

    # GET THE HISTORICAL DATA PER NHSREGION
    n_days = 7 # default
    nhsregion_dict = historical_data(n_days, region)

    # GET THE NUMBER OF DAYS TILL HERD IMMUNITY PER NHSREGION
    herd_imm_dict = days_herd_immunity()
    percent_pop_vacc = vaccinated_population()

    # COMBINE THE TWO
    for region in herd_imm_dict.keys():
        nhsregion_dict[region]['herd_imm_days'] = herd_imm_dict[region]
        nhsregion_dict[region]['percent_vacc'] = percent_pop_vacc[region]

    nhsregion_dict = json.dumps(nhsregion_dict, indent = 4)

    return nhsregion_dict