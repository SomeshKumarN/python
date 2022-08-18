"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

#Solution
test=1
def rangeCheck(number):
    global test
    print("\nTest-->",test)    
    if(abs(1000-number)<=100 or abs(2000-number)<=100):
        print("Given number",number,"is with in range.")
    else:
        print("Given number",number,"is NOT with in range.")
    test+=1
    


#Tests
rangeCheck(999)
rangeCheck(901)
rangeCheck(900)
rangeCheck(899)
rangeCheck(-899)
rangeCheck(-500)
rangeCheck(1901)
rangeCheck(-500)