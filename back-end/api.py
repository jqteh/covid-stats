from flask import Flask, request, render_template, jsonify
import json
from infection_vaccination_graph import historical_data, days_herd_immunity, vaccinated_population
from test_api import pythonify

app = Flask(__name__, static_folder='../build', static_url_path='/')

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/api', methods=['GET','POST'])
def api():
    # step 1
    if request.method=="GET":
        return {'message': "hello"}
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
    nhsregion_dict = pythonify(nhsregion_dict)

    return nhsregion_dict

