#Ternary Operator
# A ternary operator is a shorthand way to write an if-else statement in a single
# line. It is often used for simple conditional assignments.
# The syntax is: `value_if_true if condition else value_if_false`

mark = 75
if mark > 35:
    result = "Pass"
else:
    result = "Fail"
print("Using if-else:", result)

113
254

# Using a ternary operator
result = "Pass" if mark>35 else "Fail"
print("Using Ternary Operator:", result)

#Example 1
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# Example 2
def get_max(a, b):
    return a if a > b else b

print("Check Even or Odd:", check_even_odd(10))  # Output: Even
print("Check Even or Odd:", check_even_odd(7))   # Output: Odd
print("Max of 10 and 20:", get_max(10, 20))  # Output: 20
print("Max of 20 and 10:", get_max(20, 10)) # Output: 20

# Example 3
def get_sign(num):
    return "Positive" if num > 0 else "Negative" if num < 0 else "Zero" 

def get_sign1(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print("Sign of 10:", get_sign(10))    # Output: Positive
print("Sign of -5:", get_sign(-5))    # Output: Negative
print("Sign of 0:", get_sign(0))      # Output: Zero