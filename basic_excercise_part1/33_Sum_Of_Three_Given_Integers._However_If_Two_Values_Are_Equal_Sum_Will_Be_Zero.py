"""Write a Python program to sum of three given integers.
 However, if two values are equal sum will be zero."""

#Solution:
def sumThreeNumbers(val1:int,val2:int,val3:int):
    if val1==val2 or val2 == val3 or val3==val1:
        print("Result is '0'")
    else:
        print("No Result:")

#Tests
sumThreeNumbers(1,1,2)
sumThreeNumbers(1,2,2)
sumThreeNumbers(3,1,3)
sumThreeNumbers(1,2,3)