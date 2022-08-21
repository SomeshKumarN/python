# Write a Python program to add two objects if both objects are an integer type

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    return "given objects is not integer"
print(add(2,5.8))
print(add(2,"3"))
print(add(2,4))
print(add('',''))

list = [1,2,3,4,5]
for i in list:
    print(i)
    print(type(i))
    print(type(i) == int)



