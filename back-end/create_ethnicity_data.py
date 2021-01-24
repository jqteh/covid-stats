import json

ethnicities = {"East of England": {"White": 5507e3, "Mixed": 114e3, "Asian": 309e3, "Black": 143e3, "Other": 58e3}, 
                "London": {"White": 5175e3, "Mixed": 367e3, "Asian": 1625e3, "Black": 1092e3, "Other": 529e3}, 
                "Midlands": {"White": 8903e3, "Mixed": 152e3, "Asian": 1037e3, "Black": 306e3, "Other": 127e3}, 
                "North East and Yorkshire": {"White": 7326e3, "Mixed": 81e3, "Asian": 451e3, "Black": 113e3, "Other": 90e3}, 
                "North West": {"White": 6419, "Mixed": 83e3, "Asian": 480e3, "Black": 150e3, "Other": 88e3}, 
                "South East": {"White": 8165e3, "Mixed": 137e3, "Asian": 459e3, "Black": 150e3, "Other": 114e3}, 
                "South West": {"White": 5243e3, "Mixed": 65e3, "Asian": 122e3, "Black": 44e3, "Other": 42e3}}


with open("data/ethnicities_json.txt", "w") as f:
    json.dump(ethnicities, f)
