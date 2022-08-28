# Write a Python program to get execution time for a Python method.
import datetime as dt
a = dt.datetime.now()
def checktime():
    print('execution time')
    print(a.time())
checktime()    
