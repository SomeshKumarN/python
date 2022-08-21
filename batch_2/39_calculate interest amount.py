# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
def future_amount(amount,interest,years):
    
    return amount*((1+(0.01*interest))**years) 


def futureAmt(p,r,t):
# p = int(input("Enter the principle amount:"))
# r = float(input("Enter the rate of interest:"))
# t = int(input("Enter the tenure in years:"))
    a= p*(1+(r*t))
    print("Future value of your loan would be-->",a)


print(future_amount(100000 ,12,1))
print(future_amount(5000,7,10))
futureAmt(100000,0.12,1)
futureAmt(5000,0.07,10)