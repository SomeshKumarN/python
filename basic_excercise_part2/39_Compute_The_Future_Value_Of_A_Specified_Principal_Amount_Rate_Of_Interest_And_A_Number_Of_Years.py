"""Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years."""

#Solution:

# Simple Loan Future value formula is A=P(1+rt)
# P-principal amount
# r- rate of interest in percent(5%=0.05)
# t- no.of years

p = int(input("Enter the principle amount:"))
r = float(input("Enter the rate of interest:"))
t = int(input("Enter the tenure in years:"))
a= p*(1+r*t)
print("Future value of your loan would be-->",a)