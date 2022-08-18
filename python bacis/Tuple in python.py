"""
Tuple  
There are immutable

"""
"""
a = (1, 2, 3, 4, 5)
print(a,"type is ",type(a))
print(a[0])
print(a[0:])
b = list(a)
print(b)
b.append(2)
print(b)
a = tuple(b)
print(a)

if 2 in a:
    print("2 is found")
else :
    print("2 is not found")

tu = (1, 2, 3, 4, 5)
del tu
print(tu)
"""
a = (1, 2, 3, 4, 5, 6)
b = (7, 8, 9, 10)
print(a+b)

a = (1, 2, 3, 4, 5, 6)
b = (7, 8, 9, 10)
print(a,b)

print(min(a))
print(max(a))


