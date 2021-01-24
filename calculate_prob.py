from scipy.special import comb
import numpy as np

def prob_of_infection(region_pop, region_cases, region_pop_vacc, age = None, vacc = None):
    # vacc - value either None, 0, 1 or 2 depending on number of doses

    #################################################################################################
    # STEP 1: Initialisation of variables involved

    n = 100 # number of people in a location
    m = 20 # number of people you come into contact with
    dc = 15 # amount of time in direct contact with other people (average minutes)
    lamb = 0.001 # time constant for exponential distribution.
    vacc_efficacy = [0, 0.60, 0.95] # efficacy of vaccine of not getting, getting 1 dose, and getting 2 doses

    #################################################################################################
    # STEP 2: Calculate probability based on how people statistics - number of people around, infected

    p = region_cases/region_pop # the prevalence of disease in that region

    ptr = 1-np.exp(-lamb*dc) # probability of transmission. The paper referred found the relationship to be exponential.
    term = 0
    for i in range(n):
        term += comb(n,i)*(p**i)*((1-p)**(n-i))*(1-(i*ptr)/n)**m

    prob = 1 - term

    # Step 2.1: Account for vaccinations done in that NHS Region??



    #################################################################################################
    # STEP 3: Account for personal age

    if age!=None:
        prob = prob # TODO

    #################################################################################################
    # STEP 3: Account for personal vaccination status

    if vacc!=None:
        prob = (1-vacc_efficacy[vacc]) * prob # assumes vacc will be one of 0, 1 or 2


    return prob

if __name__ == "__main__":
    print(prob_of_infection(1000000, 100000))


