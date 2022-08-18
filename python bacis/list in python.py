"""
list is sequence type 
mutable   
"""

"""a = [1, 2, 3, 4, 5]
print(type(a))
a[0] = 100
a[1] = 200
print(a)

print("------------------------")
print("Slicing")
print(a)
print(a[0])
print(a[1])
print(a[0:])
print(a[1:])
print(a[-1])
print(a[-2])
print(a[:-1])
print(a[0:4])
print(a[0:-1])
print('-------------------')

# include different datatypes in list
b =[2, True, 'bala', 2.0, [1, 2, 3, 4, 5]]
print(a)
print(type(b[0]))
print(type(b[1]))
print(type(b[2]))
print(type(b[3]))
print(type(b[4]))
print('--------------------')

# clear, copy..ect inbulit functions in list
c = [1, 2, 3, 4, 5] 
b =[]
print(c)
c.clear()
print(c)
c = [10, 20, 30, 20,  40, 50, 60, 70] 
b = c.copy()
print(b)
c.pop()
print(c)
print(c.count(20))
print(c.index(20))
print(c.index(20, 2))
c.remove(20)
print(c)
print(len(c))
print(max(c))
print(min(c))
print("--------------------")
"""
'''
# update... in list
names = ['ram']
names.append('sam')
print(names)
name_2 = ['dheva','veera']
names.extend(name_2)
print(names)
names.insert(3, 'somnath')
print(names)
print("--------------------")
'''

# sorting in list
print(list(range(5)))
print(list("somnath"))
a = [100, 20, 300, 40, 500]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
b = ['somnath', 'veera', 'deva', 'somesh']
b.sort(key = len)
print(b)






