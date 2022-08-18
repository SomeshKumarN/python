"""Write a Python program to check whether a specified value is contained 
in a group of values."""

#Solution:

test = 1

def isValueAvailable(_list:list, value):
    global test
    print("\nTest-->",test)
    print("Given list is -- ",_list)
    if value in _list:
        print(value,"is available in the list")
    else:
        print(value,"is NOT available in the list")
    test+=1


#Tests

isValueAvailable([1,2,3,4,5],4)
isValueAvailable([1,2,3,4,5],9)
isValueAvailable([1,2,3,4,5],'som')
isValueAvailable([11,2,3,4,5],True)