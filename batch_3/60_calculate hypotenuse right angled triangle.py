# Write a Python program to calculate the hypotenuse of a right angled triangle.
import math
def x(a, b):
    try:
        c = math.sqrt(a**2 + b**2)
        print(c)
    except:
        print('Integer only allowed')    
x(2, 2)
x(3, 4)    
x("",3)