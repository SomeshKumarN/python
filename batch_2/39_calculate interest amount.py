# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
def future_amount(amount,interest,years):
    
    return amount*((1+(0.01*interest))**years)
print(future_amount(10000 ,3.5 ,7))


