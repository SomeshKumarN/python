import pandas as pd

df = pd.read_csv('pandas/data.csv')

df.fillna(130, inplace = True)
print(df.to_string())

#-------------------------------------

import pandas as pd

df = pd.read_csv('pandas/data.csv')

df["Calories"].fillna(130, inplace=True)
print(df.to_string())
