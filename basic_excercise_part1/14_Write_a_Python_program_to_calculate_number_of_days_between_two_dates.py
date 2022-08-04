"""
Write a Python program to calculate number of days between two dates.

Sample dates : (2014, 7, 2), (2014, 7, 11)

Expected output : 9 days
"""

#Solution:

import datetime

date1 = datetime.datetime(2014,7,2)
date2 = datetime.datetime(2015,5,11)
print((date2-date1).days)