import json

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

with open('data/populations_json.txt') as file:
        population_data = json.load(file)

with open('data/collated_data_final.txt') as file:
    collated_data = json.load(file)

with open('data/vacc_json.txt') as file:
    vaccination_data = json.load(file)


vac_dates = vaccination_data['London'].keys()
data_dates = collated_data['London'].keys()

print(vac_dates)
print(data_dates)