import pandas as pd
import numpy as np
import json

with open("data/ethnicities_json.txt") as file:
    ethnicity_data = json.load(file)

regions = ethnicity_data.keys()

#print(regions)

ethnicities = ethnicity_data.values()

#print(ethnicities)

df = pd.DataFrame.from_dict(ethnicity_data)
print(df)

total_deaths = sum([61,19,159,85,95,67,16,8,180,80,29,30,186,85,119,75,1939,1184,112,54,188,96,514,306,78,55,525,357,144,99,351,226,286,156,20531,18201])
print(total_deaths)




