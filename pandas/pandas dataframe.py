import pandas as pd
data = {
    'calories':['300','400','500'],
    'duration':['50','40','45']   
}

myvar = pd.DataFrame(data,index=['day1', 'day2','day3'])
print(myvar)

# Locate row: get row and column name

print(myvar.loc['day1'])

print(myvar.loc[['day1','day2']])




