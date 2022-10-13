# Python program to find the common elements in two lists

def common_member(a, b):
	a_set = set(a)
	b_set = set(b)

	if (a_set & b_set):
		print(a_set & b_set)
	else:
		print("No common elements")
		

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
common_member(a, b)


a = {1,"df",4,5,6,7}
b = {"df",2,1,4,7,6,5}
print(a and b)


def common_member(a, b):
   result = [i for i in a if i in b]
   return result

a = {1, 2, "xd", 4.5, 5}
b = {5, "xd", 7, 8, 9, 4.5}

print("The common elements in the two lists are: ")
print(common_member(a, b))
value = []
for c in a :
   if c in b :
       print(c)
       value.append(c)
print(value)

a = 2.0
b = 1.0

if 25 - 1 % 8 == 0:
    print(True)
else:
    print('fail')    

print(25 - 1 % 8) 

def fun(a):
     
    return all((a[i] != a[i+1]) for i in range(len(a)-1))
    
        
x = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
y = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
z = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
b = (1,2,3,4,4,5,6,7,8,9,9)
print(fun(x))
print("\n---------------")
print(fun(y))
print("\n---------------")
print(fun(b))

a = [20, 10, 40, 40, 10, 40, 30, 40, 10, 30, 20, 40, 10, 20, 30, 40]
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        print(a[i],a[i+1],True)
    else:
        print(False)    
print(a[3])

a = lambda x : x+1
print(a(5))

b = lambda x, e, f : x*e*f
print(b(3,4,6))

print((lambda x : x +2 ,3))

mul_agr = lambda *agr : sum(agr)
print(mul_agr(3,4,5,7,8))

d = lambda x, y : x + y(x)
print(d(10 , lambda x : x *x))

num = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x :x%2 ,num)))

def square(n):
    return n*n
num = [1,2,3,4,5,6,7,8,9]

print(list(map(lambda d : d*d, num)))
class a:
    a = {"name": "somnath","name":"vishnu"}

print(a)

import csv
i = open("pandas/Book1.csv","r")
o = open("pandas/Book1.csv",'w')
d = csv.writer(o)
for row in csv.reader(i):
    print(row)
print(d.writerow(i))
for i in range(5):
    print("hi")
else:
    print("Loop Completed")
d = open("pandas/book1.csv","r+")

c = d.read()
d.write('some'+'\n')
print(c)
fname = "andka.csv"
print(fname.isalpha())
fname = input("Enter Your New File Name :")
print(fname.isalpha())
