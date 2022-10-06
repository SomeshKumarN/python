# File opening and closing

import pandas as pd
output = pd.read_csv("countries.csv")
f = open("countries.csv","r")
file = f.read()
print(pd.DataFrame(output))

# close file
f.close()

# check file closed or not
print(f.closed)