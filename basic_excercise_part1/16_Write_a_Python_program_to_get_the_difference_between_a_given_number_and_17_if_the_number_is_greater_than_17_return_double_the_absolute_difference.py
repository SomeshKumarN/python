# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

#Solution:

givenNo = int(input("Enter any number:"))
difference = givenNo-17
if(difference>17):
    print("Result:",difference*2)
else:
    print("Result:",givenNo)