"""
Write a Python program which accepts the radius of a circle from the user and compute the area. 
Sample Output :
r = 1.1
Area = 3.8013271108436504"

"""

#Solution:

from cmath import pi

radius = float(input("Enter radius of the circle:"))
areaOfCircle = pi*pow(radius,2)
print("Area of Circle is:",areaOfCircle)