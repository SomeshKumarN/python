# Arithmetic Operators
    #a. Addition (+)
    #b. Subtraction (-)
    #c. Multiplication (*)
    #d. Division (/)
    #e. Floor Division (//)
    #f. Modulus (%)
    #g. Exponentiation (**)
    

#Arithmetic Operators
#   # Addition
a = 10
b = 3
result = a+ b
print("Addition:", result)
result1 = 10 +18
print("Addition:", result1)
print("Addition:", 10 + 15)

str1 = "Hello"
str2 = "World"
finalString = str1 + str2
print("String Concatenation:", finalString)

finalString1 = "Test" + "String"
print("String Concatenation:", finalString1)

print("String Concatenation:", "Test" + "String")
#   # Subtraction
result = a - b
print("Subtraction:", result)
result1 = 10 - 18-12-54-545-87
print("Subtraction:", result1)      
#   # Multiplication
result = a * b  
print("Multiplication:", result)
result1 = 10 * 18
print("Multiplication:", result1)
#   # Division
result = a / b
print("Division:", result)
result1 = 10 / 18
print("Division:", result1)

#   # Floor Division
result = a // b
# print("Floor Division:", result)
result1 = 10 // 3
print("Floor Division:", result1)


input1 = 25
input2 = 4
div_result = input1 / input2 
fd_result = input1 // input2
print("div_result", div_result)
print("fd_result",fd_result)
exp_result = div_result - fd_result
print("expected_result--",exp_result)

# from the division restult after the dot(.)

# Modular Operator
input1 = 9
input2 = 3
result = input1 % input2

print("Modular--", result)


def findAfterDot(input1, input2):
    result = input1 / input2
    result = str(result)
    dotIndex = result.find(".")
    result = result[dotIndex:len(result)]
    return result

output = findAfterDot(10,3)
print("Output --->",output)

# Exponential Operator
input1 = 2
input2 = 126
result = input1 ** input2
print("Exponential Result is -->" , result)

# 2 ^ 6


def exponentials_1(intput1, input2):
    #Attempt1
    result = input1 * input1
    #Attempt2
    result1 = result * input1
    #Attempt3
    result2 = result1 * input1
    #Attempt4
    result3 = result2 * input1
    #Attempt5
    result4 = result3 * input1
    
    return result4

def exponentials_2(input1, input2):
    result = input1 * input1* input1* input1* input1* input1
    return result 
result =0
def exponentials_3(input1, input2):
    #Attempt1
    result = input1 * input1
    #Attempt2
    result = result * input1
    #Attempt3
    result = result * input1
    #Attempt4
    result = result * input1
    #Attempt5
    result = result * input1
    return result

def exponentials_4(input1, input2):
    result = 1
    for attempt in range(input2):
        result = result * input1
    return result
    

print("Final Result for 1 --->", exponentials_1(2,6))
print("Final Result for 2 --->", exponentials_2(2,6))
print("Final Result for 3 --->", exponentials_3(2,6))
print("Final Result for 4 --->", exponentials_4(2,6))


