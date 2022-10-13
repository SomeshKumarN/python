# # Python program to find the common elements in two lists

# def common_member(a, b):
# 	a_set = set(a)
# 	b_set = set(b)

# 	if (a_set & b_set):
# 		print(a_set & b_set)
# 	else:
# 		print("No common elements")
		

# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# common_member(a, b)

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9]
# common_member(a, b)


# a = {1,"df",4,5,6,7}
# b = {"df",2,1,4,7,6,5}
# print(a and b)


# def common_member(a, b):
#    result = [i for i in a if i in b]
#    return result

# a = {1, 2, "xd", 4.5, 5}
# b = {5, "xd", 7, 8, 9, 4.5}

# print("The common elements in the two lists are: ")
# print(common_member(a, b))
# value = []
# for c in a :
#    if c in b :
#        print(c)
#        value.append(c)
# print(value)

# a = 2.0
# b = 1.0

# if 25 - 1 % 8 == 0:
#     print(True)
# else:
#     print('fail')    

# print(25 - 1 % 8) 

# def fun(a):
     
#     return all((a[i] != a[i+1]) for i in range(len(a)-1))
    
        
# x = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# y = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# z = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# b = (1,2,3,4,4,5,6,7,8,9,9)
# print(fun(x))
# print("\n---------------")
# print(fun(y))
# print("\n---------------")
# print(fun(b))

# a = [20, 10, 40, 40, 10, 40, 30, 40, 10, 30, 20, 40, 10, 20, 30, 40]
# for i in range(len(a)-1):
#     if a[i] != a[i+1]:
#         print(a[i],a[i+1],True)
#     else:
#         print(False)    
# print(a[3])

# a = lambda x : x+1
# print(a(5))

# b = lambda x, e, f : x*e*f
# print(b(3,4,6))

# print((lambda x : x +2 ,3))

# mul_agr = lambda *agr : sum(agr)
# print(mul_agr(3,4,5,7,8))

# d = lambda x, y : x + y(x)
# print(d(10 , lambda x : x *x))

# num = [1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x :x%2 ,num)))

# def square(n):
#     return n*n
# num = [1,2,3,4,5,6,7,8,9]

# print(list(map(lambda d : d*d, num)))
# class a:
#     a = {"name": "somnath","name":"vishnu"}

# print(a)

# import csv
# i = open("pandas/Book1.csv","r")
# o = open("pandas/Book1.csv",'w')
# d = csv.writer(o)
# for row in csv.reader(i):
#     print(row)
# print(d.writerow(i))
# for i in range(5):
#     print("hi")
# else:
#     print("Loop Completed")
# d = open("pandas/book1.csv","r+")

# c = d.read()
# d.write('some'+'\n')
# print(c)
# fname = "andka.csv"
# print(fname.isalpha())
# fname = input("Enter Your New File Name :")
# print(fname.isalpha())
# filename = ['som.csv']
# def name():
#     return filename[0]
# print(name())    
# print(name()[0].isalnum())
# import pandas 
# columnnames = ''
# count = 0
# read_csv = (pandas.read_csv('som.csv'))
# column = read_csv.columns.values
# for i in column:
#     columnnames=(columnnames+i)+' '
#     count = count+1
# print("FILE COLUMNS :",columnnames)  
# user = input("Enter your data :")
# data = user.replace(' ',',')

# if count-1 == data.count(','):
#     print(True)
# else:
#     print(False)    

# with open('som.csv','r') as r:
#     d = r.readlines(1)
#     if len(d) == 0:
#         print('create a new file.')
#     else:
#         print("already file have columns.")

# add columns 
# import csv

# data = [1,2,3,4,5]
# with open("som.csv", "a") as fp:
#     wr = csv.writer(fp, dialect='excel')
#     wr.writerow(data)

# with open('33.csv', 'r+') as f:
#     lines = f.readlines()     
#     lines.insert(0, ',zer line')   
#     f.seek(0)                 
#     f.writelines(lines)  
# with open('33.csv','a') as d:
#     line = d.readlines()
#     line.insert(0,'hi')

    # for i  in range(len(s)):
    #     for j in s[i]:
    #         print(j)
        
    # s = 'som,23,male' in r
# with open("somm.csv",'r') as read:
#     r = read.readlines()
    
#     h = []
#     for i in r:
#         s = i.split(",")
#         for j in s:
#             k = '23' == j
#             h.append(str(k))

#     print(h)        
        # print('True' in h)   
    # if ('True' in h ):
    #     print('Your Enter Wrong Data. Please, Enter Your Correct Data.')
    # else:
    #     print('successfully deleted Your Data.')

# import csv
# with open('somm.csv') as p:
#     h = p.readline()
# #     p.writelines("somnath")
# with open('somm.csv','a+') as w: 
#     r = w.readlines()
#     w.seek(0)
#     r.insert(16,',hi')
#     w.seek(27)
#     f = w.writelines(r)
    
# import pandas as pd
# r = pd.read_csv('somm.csv')
# for i,j in r.items():
#     print(j)
# column = ['id','name','age','address']

    # 
    # c[-1]
    # c.extend(['hi','som'])
    # d = csv.reader(h)
    # data = [line for line in d]
    # print(data)



# initialize list
# test_list = ['gf\ng', 'i\ns', 'b\nest', 'fo\nr', 'geeks\n']

# printing original list
# print("The original list : " + str(test_list))

# Removing newline character from string
# Using regex
# res = []
# for sub in test_list:
	# res.append(re.sub('\n', '', sub))

# printing result
# print("List after newline character removal : " + str(res))
# import re
# s = input('Enter :')
# dat = s.split(',')
# print(dat)
# with open('som.csv') as f:
#     h = f.readline()
#     d= h.split(',')
#     data = []
#     for i in d:
#         data.append(re.sub('\n','',i))
#     data.extend(dat)
#     print(data)
#     r = csv.reader(f)
#     da = [line for line in r]
# with open('som.csv','w',newline='') as f:
#     w = csv.writer(f)
#     w.writerow(data)
#     w.writerows(da)



# with open('somm.csv', 'w',newline='') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(lines)
# # 
# import csv
# def check_delete():
#     lines=[]
#     with open('somm.csv','r') as read:
#         lines = list(csv.reader(read))      
#     if(len(lines)>2):
#         lines.pop(2)
#         with open('somm.csv', 'w',newline='') as writeFile:
#             writer = csv.writer(writeFile)
#             writer.writerows(lines)
#     else:
#         print("Incorrect row no")
       
# check_delete()
#         for i in lines:
#             s = i.split(",")
#             for j in s:
#                 if str(delete) == j:
#                     h.append('True')
#                     break
#                 else :
#                     h.append('False')
#     return 'True' in h  
# import csv 
# delete = 1
# Filename = 'somm.csv'
# if check_delete() == True:
#     count = 0
#     lines = list()
#     memberName = delete
#     with open(Filename, 'r') as readFile:
#         reader = csv.reader(readFile)
#         # print(list(reader))
        # for row in reader:
        #     # print('row :',row)
        #     lines.append(row)
        #     count = count +1
        #     for field in row:
        #         # print(field)
        #         if field == (count==1):
        #             # print(field,":",delete)
        #             lines.remove(row)
#     print(count)
#     # print('lines :',lines)
#     with open(Filename, 'w',newline='') as writeFile:
#         writer = csv.writer(writeFile)
#         writer.writerows(lines)
#     if check_delete() == False:
#         print('Data Deleted.')
#     else:
#         print('Data is not delete.')
# else:
#     print('This data not found.')       
# import os
# import pandas as pd
# filename = 'm.csv'
# if os.stat(filename).st_size > 0:
#     print(pd.read_csv(filename))
#     # print("File name is :",flname())
# else:
#     print('No Data In This File.')

# elif accessoption == 4:
#     with open(Fname) as rd:
#             print('Column Names :',rd.readline().upper())
#     print('Which column u want delete.')
#     col_umn = input('Enter column Name :')
#     if col_umn.isnumeric()==False:
#         delete_columns(col_umn) 
#     else :
#         print('Please Enter Column Names Only.') 
# import os
# filename = ['som.sv']
# def flname():
#     return filename[0]
# def check_file():   
#     try:
#         if flname()[0].isalnum() and '.' in flname():
#             return flname()
#         else:
#             Fname = input("Enter file name with exists :")
#             filename.clear()
#             filename.append(Fname)
#             return Fname
#     except:
#         Fname = input("Enter file name with exists :")
#         filename.clear()
#         filename.append(Fname)
#         return Fname
# print(check_file())
    # check = os.path.exists(flname())
    # if check != True:
    #     print("Please Enter Correct File Name.")
    #     filename.clear()
# def check_file():
#     check = os.path.exists(flname())
#     if check != True:
#         print("Please Enter Correct File Name.")
#         filename.clear()
#         return False
#     else:
#         return True   
# if (check_file() == False):
#     pass
import pandas
d = pandas.read_csv('som.csv')
print(len(d.values))