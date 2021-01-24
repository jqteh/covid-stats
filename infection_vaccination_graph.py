import json

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

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


def days_herd_immunity():
    with open('data/populations_json.txt') as file:
        population_data = json.load(file)

    with open('data/collated_data_final.txt') as file:
        collated_data = json.load(file)

    with open('data/vacc_json.txt') as file:
        vaccination_data = json.load(file)

    locations = vaccination_data.keys()
    herd_immunity_threshold = 0.9

    days_till_herd_immunity = {}

    for i in locations:
            dates = vaccination_data[i].keys()
            previous_dates = list((dates))

            vacc_number = []
            day_number = []

            for j, k in enumerate(previous_dates):

                day_number.append(j)
                vacc_number.append(vaccination_data[i][k]['cumPeopleReceivedFirstDose'])

                x = np.array(vacc_number)
                y = np.array(day_number)

            regr = linear_model.LinearRegression()
            regr.fit(x[:, None], y)

            x_threshold = [[]]
            x_threshold[0].append(population_data[i]*herd_immunity_threshold)
            days = regr.predict(x_threshold)

            days_till_herd_immunity[i] = days
            
    return days_till_herd_immunity
        
def vaccinated_population():
    with open('data/vacc_json.txt') as file:
        vaccination_data = json.load(file)

    with open('data/populations_json.txt') as file:
        population_data = json.load(file)

    locations = population_data.keys()
    vaccinated_population_percentage = {}

    for i in locations:
        population = population_data[i]
        date = list(vaccination_data[i].keys())
        vaccinated_population = vaccination_data[i][date[-1]]['cumPeopleReceivedFirstDose']
        percentage_vaccinated = 100*vaccinated_population/population

        vaccinated_population_percentage[i] = percentage_vaccinated
    
    return vaccinated_population_percentage


percentage = vaccinated_population()

print(percentage)





    

