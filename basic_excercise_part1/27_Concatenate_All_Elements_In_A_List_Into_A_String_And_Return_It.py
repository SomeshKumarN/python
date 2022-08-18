"""Write a Python program to concatenate all elements in a list into a 
string and return it."""

#Solution:

test=1

def listConcatination(_list:list):
    global test
    print("\nTest--",test)
    temp=''
    for val in _list:
        temp+=str(val)
    print(temp)
    test+=1


#Tests
listConcatination([1,2,3])
listConcatination([1,'somesh',True])