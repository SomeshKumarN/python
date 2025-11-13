
def isValidInteger( anyValue):
    result = isinstance(anyValue,int) 
    print_result(result)   
    return result
    
def print_result(result:bool):
    if( result != True):
        print("Given number is NOT an Integer")
    else:
        print("Given number is an Integer")
    

cus_input ='test'
print(isValidInteger(cus_input))

#Python Exponential numbers

variable1 = 541e-3
print(variable1)

# e=10*10*10 = 1000-------->1 * 1000= 1000
# e =1/(10*10*10) = 1/1000 = 0.001 --------> 1*0.001 = 0.001


#Float
# eg: 3.14
from math import pi
float_variable = 3.14242354325345345342534253245
print(float_variable)

# factorial - 
# 3!--> 3x2x1 = 6
# 5!--> 5x4x3x2x1 = 120
# 5! --> 

input =12
output= 1


for i in range(1,5):
    output *=i    

# ==> output = output * i
# ==> output = 1 * 1 = 1    
# ==> output = 1 * 2 = 2    
# ==> output = 2 * 3 = 6    
# ==> output = 6 * 4 = 24    
# output =1

import math
print(math.factorial(12))