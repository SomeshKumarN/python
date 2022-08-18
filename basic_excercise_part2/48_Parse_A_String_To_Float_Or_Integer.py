"""Write a Python program to parse a string to Float or Integer."""

#Solution:

from operator import truediv
import string

def isFloat(input:string):
    try:
        float(input)
        return True
    except:
        return False
        
inputString=input("Enter an Interger or float:")

if(inputString.isdigit()):
    print("Input value converted to int",int(inputString))
elif(isFloat(inputString)):
    print("Input value converted to float",float(inputString))
else:
    print("Enter Int or Float")
