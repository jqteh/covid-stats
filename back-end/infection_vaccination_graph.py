import json

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def historical_data(n_days, region):

    with open('data/populations_json.txt') as file:
        population_data = json.load(file)

    with open('data/collated_data_final.txt') as file:
        collated_data = json.load(file)

    with open('data/vacc_json.txt') as file:
        vaccination_data = json.load(file)

    locations = collated_data.keys()

    cases_infection_scaling_factor = 4.0
    first_dose_protection = 0.48
    second_dose_protection = 0.05

    historical_estimated_new_infections_dict = {}
    historical_new_cases_dict = {}
    historical_new_deaths_dict = {}
    historical_hospital_cases = {}
    historical_patients_on_ventalitors = {}

    for i in locations:
        dates = collated_data[i].keys()
        previous_dates = list((dates))[0:n_days]
        list.reverse(previous_dates)
        historical_new_cases_dict[i] = {}
        historical_new_deaths_dict[i] = {}
        historical_estimated_new_infections_dict[i] = {}
        historical_hospital_cases[i] = {}
        historical_patients_on_ventalitors[i] = {}

        for j in previous_dates:

            historical_new_cases_dict[i][j] = collated_data[i][j]['cases']['daily'] 
            historical_estimated_new_infections_dict[i][j] = collated_data[i][j]['cases']['daily']*cases_infection_scaling_factor
            historical_new_deaths_dict[i][j] = collated_data[i][j]['deaths']['newDeathsByDeathDate']
            historical_hospital_cases[i][j] = collated_data[i][j]['hospitalCases']
            historical_patients_on_ventalitors[i][j] = collated_data[i][j]['covidOccupiedMVBeds']


    return {'historical_new_cases_dict' : historical_new_cases_dict[region], 'historical_estimated_new_infections_dict' : historical_estimated_new_infections_dict[region], 'historical_new_deaths_dict' : historical_new_deaths_dict[region], 'historical_hospital_cases' : historical_hospital_cases[region], 'historical_patients_on_ventalitors' : historical_patients_on_ventalitors[region]}

data = historical_data(7, 'London')





    

