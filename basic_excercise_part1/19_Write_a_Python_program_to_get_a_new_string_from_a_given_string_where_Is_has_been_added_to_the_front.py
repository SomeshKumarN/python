# Write a Python program to get a new string from a given string where "Is" 
# has been added to the front.# If the given string already begins with "Is"
# then return the string unchanged.

#Solution:
givenStr = input("Enter any random string:")
if(givenStr[:2] =="is"):
    print("Output:", givenStr)
else:
    print("Output:", "is "+givenStr)