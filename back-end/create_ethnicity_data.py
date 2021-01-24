import json

ethnicities = {"East of England": {"White British": 5097e3, "All Other White": 410e3, "Mixed": 114e3, "Asian": 309e3, "Black": 143e3, "Other": 58e3}, 
                "London": {"White British": 3753e3, "All Other White": 1422e3, "Mixed": 367e3, "Asian": 1625e3, "Black": 1092e3, "Other": 529e3}, 
                "Midlands": {"White British": 8403e3, "All Other White": 500e3, "Mixed": 152e3, "Asian": 1037e3, "Black": 306e3, "Other": 127e3}, 
                "North East and Yorkshire": {"White British": 7064e3, "All Other White": 262e3, "Mixed": 81e3, "Asian": 451e3, "Black": 113e3, "Other": 90e3}, 
                "North West": {"White British": 6162e3, "All Other White": 257e3, "Mixed": 83e3, "Asian": 480e3, "Black": 150e3, "Other": 88e3}, 
                "South East": {"White British": 7621e3, "All Other White": 544e3, "Mixed": 137e3, "Asian": 459e3, "Black": 150e3, "Other": 114e3}, 
                "South West": {"White British": 4979e3, "All Other White": 264e3, "Mixed": 65e3, "Asian": 122e3, "Black": 44e3, "Other": 42e3}}


with open("data/ethnicities_json.txt", "w") as f:
    json.dump(ethnicities, f)
