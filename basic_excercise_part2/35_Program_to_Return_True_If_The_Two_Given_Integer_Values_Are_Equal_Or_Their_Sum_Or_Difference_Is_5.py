"""Write a Python program that will return true if the two given integer
 values are equal or their sum or difference is 5."""

#Solution:

def returnValue(val1:int, val2:int):
    if val1==val2 or (val1+val2)==5 or (val1-val2)==5 :
        print(True)
    else:
        print(False)

#Tests
returnValue(2,2)
returnValue(7,2)
returnValue(3,2)
returnValue(3,4)