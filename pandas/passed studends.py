#passed_out_studends = myvar['Marks']
#print(passed_out_studends)
#mean = myvar['Marks'].mean()
#sum = myvar['Marks'].sum()
#max = myvar['Marks'].max()
#min = myvar['Marks'].min()
#count1 = myvar['Marks'].count()
#median1 = myvar['Marks'].median()
#print(sum)



import pandas as pd
"""studend_data = {
    'Studend Names':['prem','arun','rahul','sam','ram','somu','raju','bala','gopi','kumar'],
    'Rollno':[1,2,3,4,5,6,7,8,9,10],
    'Marks':[18,35,40,90,35,80,70,12,13,65]print("Studend_Details :\n")
}"""

Studend_Data = pd.read_csv("../Users/dell/Downloads/studend details.csv")

myvar = pd.DataFrame(Studend_Data)
print(myvar,'\n')

c = (myvar['tamil']>= 35) & (myvar['english']>= 35) & (myvar['maths']>= 35) & (myvar['science']>= 35) & (myvar['social']>= 35)

pass_out_studends = myvar[c]

fail_stu = pd.DataFrame(Studend_Data[(myvar['tamil'] < 35) | (myvar['english'] < 35) | (myvar['maths'] < 35) | (myvar['science'] < 35) | (myvar['social'] < 35)])

print("Passed Out Studends :\n\n", pass_out_studends)


print("Fail Studends Details :\n\n",fail_stu)



