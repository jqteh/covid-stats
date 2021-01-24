import json

with open('data/populations_json.txt') as file:
    population_data = json.load(file)

with open('data/collated_data_final.txt') as file:
    collated_data = json.load(file)

with open('data/vacc_json.txt') as file:
    vaccination_data = json.load(file)

locations = collated_data.keys()
number_of_previous_days = 7
cases_infection_scaling_factor = 4.0
first_dose_protection = 0.35
second_dose_protection = 0.05
infection_risk_dict = {}

for i in locations:
    dates = collated_data[i].keys()
    previous_dates = list(dates)[0:number_of_previous_days]

    list_cases_previous_dates = []
    for j in previous_dates:
        list_cases_previous_dates.append(collated_data[i][j]['cases']['daily'])

    non_zero_count = sum(x > 0 for x in list_cases_previous_dates)
    if non_zero_count == 0:
        non_zero_count = 1

    mean_daily_cases_previous_dates = sum(list_cases_previous_dates) / non_zero_count
    expected_infections_next_30_dates = 30*mean_daily_cases_previous_dates*cases_infection_scaling_factor
    percentage_population_cases_next_30_days = expected_infections_next_30_dates / population_data[i] * 100
    one_dose = percentage_population_cases_next_30_days*first_dose_protection
    two_doses = percentage_population_cases_next_30_days*second_dose_protection

    print('In ', i)
    print('Running mean of daily cases = ', mean_daily_cases_previous_dates)
    print('Predicted infections over the next 30 days = ', expected_infections_next_30_dates)
    print('Percentage of population likely to be infected in the next 30 days =', percentage_population_cases_next_30_days, "%")
    print('If vaccinated with one dose, the risk over the next 30 days drops to', one_dose, "%")
    print('If vaccinated with two dose, the risk over the next 30 days drops to', two_doses, "%")

    infection_risk_dict[i] = {'normal' : percentage_population_cases_next_30_days,
                              'one_dose' : one_dose,
                              'two_doses' : two_doses
                              } 

