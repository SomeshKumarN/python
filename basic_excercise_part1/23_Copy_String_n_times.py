"""Write a Python program to get the n (non-negative integer) copies of the 
first 2 characters of a given string. Return the n copies of the whole string 
if the length is less than 2."""

#Solution:

test =1

def copyString(string:str,nCopies:int):
    global test
    print("\nTest-->",test)
    if string.__len__()>2:
        print(string[:2]*nCopies)
    else:
        print(string*nCopies)
    test+=1


#Tests
copyString('somesh',4)
copyString('s',4)
copyString('s0',4)
copyString(2341,4)