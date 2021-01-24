import json

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


with open('data/populations_json.txt') as file:
    population_data = json.load(file)

with open('data/collated_data_final.txt') as file:
    collated_data = json.load(file)

with open('data/vacc_json.txt') as file:
    vaccination_data = json.load(file)

locations = collated_data.keys()
number_of_previous_days = 7
cases_infection_scaling_factor = 4.0
first_dose_protection = 0.48
second_dose_protection = 0.05
infection_risk_dict = {}

for i in locations:
    dates = collated_data[i].keys()
    previous_dates = list(dates)[0:number_of_previous_days]

    list_cases_previous_dates = []
    list_deaths_previous_dates = []
    for j in previous_dates:
        list_cases_previous_dates.append(collated_data[i][j]['cases']['daily'])
        list_deaths_previous_dates.append(collated_data[i][j]['deaths']['newDeathsByDeathDate'])


plt.plot(previous_dates, list_cases_previous_dates)
plt.show()