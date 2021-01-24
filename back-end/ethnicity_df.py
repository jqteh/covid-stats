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



