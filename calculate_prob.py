from math import comb 
import numpy as np

def prob_of_infection(region_pop, region_cases, age = None, vacc = None):

    #################################################################################################
    # STEP 1: Initialisation of variables involved

    n = 10 # number of people in a location
    m = 5 # number of people you come into contact with
    dc = 10 # amount of time in direct contact with other people (average minutes)
    lamb = 0.001 # time constant for exponential distribution

    #################################################################################################
    # STEP 2: Calculate probability based on how people statistics - number of people around, infected

    p = region_cases/region_pop # the prevalence of disease in that region

    ptr = 1-np.exp(-lamb*dc) # probability of transmission
    term = 0
    for i in range(n):
        term = comb(n,i)*(p**i)*((1-p)**(n-i))
        term = term * (1-(i*ptr)/n)**m

    prob = 1 - term

    #################################################################################################
    # STEP 3: Account for age

    if age!=None:
        prob = prob # TODO

    if vacc!=None:
        if vacc== 0: # not vaccinated
            prob = prob # TODO
        if vacc == 1: # given the first dose
            prob = prob
        if vacc == 2: # given the second dose
            prob = prob # TODO


    return prob


