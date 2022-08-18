"""Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20."""

#Solution:
def sumTwoNumber(val1:int, val2:int):
    if 15<(val1+val2)<20 :
        print("20")
    else:
        print("False")

#Tests
sumTwoNumber(12,20)
sumTwoNumber(12,5)