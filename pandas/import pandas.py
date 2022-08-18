import pandas as pd

mydataset = {
    'car':["BMW","Volvo","Ford"],
    'passings':[3, 7, 2]}

myvar = pd.DataFrame(mydataset)
print(myvar)

#check pandas version
print(pd.__version__)
