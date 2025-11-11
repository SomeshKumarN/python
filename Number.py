
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




