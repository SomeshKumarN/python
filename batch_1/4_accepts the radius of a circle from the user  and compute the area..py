# Write a Python program which accepts the radius of a circle from the user
# and compute the area.
from numpy import pi
radius = float(input("Enter Radius of circle value :"))
area = pi*radius**2
print("Area value is :", area)