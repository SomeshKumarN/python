"""
Write a Python program to display the examination schedule. 
(extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)

Sample Output : The examination will start from : 11 / 12 / 2014
"""

#Solution:


import datetime

exam_st_date = (11, 12, 2014)
examDate=datetime.datetime(exam_st_date[-1],exam_st_date[1],exam_st_date[0])
print("The examination will start from :",examDate.strftime("%d / %m /%Y"))
