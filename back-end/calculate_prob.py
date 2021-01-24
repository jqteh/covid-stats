from scipy.special import comb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def prob_of_infection(region_pop, region_cases, region_pop_vacc=None, age = None, vacc = None, length_days = None):
    # vacc - value either None, 0, 1 or 2 depending on number of doses

    #################################################################################################
    # STEP 1: Initialisation of variables involved

    n = 100 # number of people in a location
    m = 15 # number of people you come into contact with
    dc = 20 # amount of time in direct contact with other people (average minutes)
    lamb = 0.1 # time constant for exponential distribution.
    vacc_efficacy = [0, 0.60, 0.95] # efficacy of vaccine of not getting, getting 1 dose, and getting 2 doses
    scale_factor = 4.5

    #################################################################################################
    # STEP 2: Calculate probability based on how people statistics - number of people around, infected

    p = scale_factor*region_cases/region_pop # the prevalence of disease in that region

    ptr = 1-np.exp(-lamb*dc) # probability of transmission. The paper referred found the relationship to be exponential.
    term = 0
    for i in range(n):
        term += comb(n,i)*(p**i)*((1-p)**(n-i))*(1-(i*ptr)/n)**m

    prob = 1 - term

    # Step 2.1: Account for vaccinations done in that NHS Region??


    #################################################################################################
    # STEP 3: Account for personal age

    if age!=None:
        factor = np.exp(age/100) # TODO
        prob = factor*prob 

    #################################################################################################
    # STEP 3: Account for personal vaccination status

    if vacc!=None:
        prob = (1-vacc_efficacy[vacc]) * prob # assumes vacc will be one of 0, 1 or 2

    if length_days!=None:
        prob = 1 - (1-prob)**length_days

    return prob

if __name__ == "__main__":
    print(prob_of_infection(1000000, 100, age = 50, length_days = 60))


## graph of probability of infection against length of days, for several age groups ##

days_list = list(range(1, 180, 1))
ages_list = list(range(20, 90, 10))
probs_dict = {}

for i in ages_list:
    probs_list = []
    for j in days_list:
        probs_list.append(prob_of_infection(1000000, 100, region_pop_vacc=None, age = i, vacc = None, length_days = j))
    
    probs_dict[i] = probs_list
    plt.plot(days_list, probs_dict[i])

plt.show()






print(probs_dict)



