"""Write a Python program that will accept the base and height of a
 triangle and compute the area."""

#Solution:

from glob import glob


test=1

def areaOfTriangle(base, height):
    global test
    print("\nTest--",test)
    print('Area of triangle is-',(base*height)/2)
    test+=1


#Test
areaOfTriangle(2,4)
areaOfTriangle(2,-3)