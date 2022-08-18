# pandas series
import pandas as pd
mylist = [1, 2, 3, 4, 5]
"""myvar = pd.Series(mylist)
print(myvar)"""

# labels or indexing in pandas series 
"""print(myvar[0])
print(myvar[2])"""

# create own index labels
"""myvar = pd.Series(mylist,index= ["One","Two","Three","Four","Five"])
print(myvar)
print("Two",myvar['Two'])"""

# create simple pandas series for 'dictionary'.
calories = { 'day1': 420,'day2': 380,'day3': 390 }
myvar = pd.Series(calories)
"""print(myvar) """

# get particular index
myvar = pd.Series(calories,index=['day1','day2'])
print(myvar) 


