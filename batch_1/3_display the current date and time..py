"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
import datetime as dt
current_datetime = dt.datetime.now()
print("Current Datetime :", current_datetime)

# accessing date and time :
"""print("_________________________________________________")
print("current time :",current_datetime.strftime("%H:%M:%S"))
print("current time : hour :",current_datetime.hour)
print("current month :",current_datetime.month)
print("current time with microsec :",current_datetime.time())
print("current date :",current_datetime.date())"""


