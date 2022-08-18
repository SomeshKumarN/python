# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

def solve(x,y):
    try:
        add = x + y
        return(add**2)
    except:
        return "Invalid Input"    
print(solve(4,3))
print(solve("",""))
print(solve(-2,90))
print(solve("",-3))
print(solve(-5,-3))
