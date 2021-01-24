from flask import Flask, request, render_template
import json
from infection_vaccination_graph import historical_data

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    # step 1
    if request.method=="POST":
        data_frontend = request.get_json() # parses as json

        region = data_frontend["region"]
        age = data_frontend["age"]
        handwash = data_frontend["wash"]
        # vacDose = data_frontend["vacDose"]

    # step 2: need to extract the required things from that big dictionary
    # need to send infection history (array), vaccination history (array) and risk of infection (int)
    n_days = 7 # default
    nhsregion_dict = historical_data(n_days = n_days, region)

    # step 3: convert dictionary to JSON - is this needed?
    nhsregion_json = json.dumps(nhsregion, indent = 4)

    return nhsregion_json