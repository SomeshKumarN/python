#Operator Precedence
# Operator precedence determines the order in which operators are evaluated in an expression.
# PEMDAS is a common acronym used to remember the order of operations:
# P - Parentheses ()
# E - Exponents (^) or (** in Python)
# M - Multiplication (*) and Division (/) (from left to right)
# D - Division (/) and Multiplication (*) (from left to right)
# A - Addition (+) and Subtraction (-) (from left to right)
# S - Subtraction (-) and Addition (+) (from left to right)

# Example 1
result = 10 - 7 + 3 + 2 ** 2 * 4 / 2

# Breaking down the expression step by step
# 1. Calculate the exponent: 2 ** 2 = 4
# 2. Substitute the result back into the expression: 10 - 7 + 3 + 4 * 4 / 2
# 3. Perform multiplication and division from left to right: 4 * 4 = 16, then 16 / 2 = 8
# 4. Substitute the result back into the expression: 10 - 7 + 3 + 8
# 5. Perform addition and subtraction from left to right: 10 - 7 = 3, then 3 + 3 = 6, and finally 6 + 8 = 14
print("Result of Example 1:", result)

# Example 2
result2 = 2 ** 3 ** 2


# Breaking down the expression step by step
# 1. Calculate the exponent: 3 ** 2 = 9
# 2. Substitute the result back into the expression: 2 ** 9
# 3. Calculate the final result: 2 ** 9 = 512

print("Result of Example 2:", result2)

# 1. Basic Arithmetic Precedence
expression = 5 + 3 * 2 
print("Result of Basic Arithmetic Precedence:", expression)
# Breaking down the expression step by step
# 1. Perform multiplication: 3 * 2 = 6
# 2. Substitute the result back into the expression: 5 + 6
# 3. Perform addition: 5 + 6 = 11

# 2. Parentheses Precedence
expression2 = (5 + 3) * 2
print("Result of Parentheses Precedence:", expression2)
# Breaking down the expression step by step
# 1. Calculate the expression inside the parentheses: 5 + 3 = 8
# 2. Substitute the result back into the expression: 8 * 2
# 3. Perform multiplication: 8 * 2 = 16

# 3. Multiple Operations with Parentheses
expression3 = 5 + (3 * 2) - 4   
print("Result of Multiple Operations with Parentheses:", expression3)
# Breaking down the expression step by step
# 1. Calculate the expression inside the parentheses: 3 * 2 = 6
# 2. Substitute the result back into the expression: 5 + 6 - 4
# 3. Perform addition: 5 + 6 = 11

# 4. Exponents and Parentheses
expression =3 + 2 ** (1 + 2)
print("Result of Exponents and Parentheses:", expression)
# Breaking down the expression step by step 
# 1. Calculate the expression inside the parentheses: 1 + 2 = 3
# 2. Substitute the result back into the expression: 3 + 2 ** 3
# 3. Calculate the exponent: 2 ** 3 = 8
# 4. Substitute the result back into the expression: 3 + 8
# 5. Perform addition: 3 + 8 = 11

# 5. Mixed Operations
expression = (2 + 3) * 4 / 2 ** 2
print("Result of Mixed Operations:", expression)
# Breaking down the expression step by step
# 1. Calculate the expression inside the parentheses: 2 + 3 = 5
# 2. Substitute the result back into the expression: 5 * 4 / 2 ** 2
# 3. Calculate the exponent: 2 ** 2 = 4
# 4. Substitute the result back into the expression: 5 * 4 / 4
# 5. Perform multiplication: 5 * 4 = 20
# 6. Perform division: 20 / 4 = 5
