#Write a Python program to get a string which is n (non-negative integer) 
# copies of a given string.

#Solution:
test=1

def copyStr(string, noOfCopy):
    global test
    print("\nTest-->",test)
    temp=""
    for i in range(noOfCopy):
        temp+=string
    print(temp)
    test+=1


#Tests

copyStr('som',5)
copyStr('kk',2)

