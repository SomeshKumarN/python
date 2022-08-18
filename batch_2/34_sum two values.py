# Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20.
def sum(num_1,num_2):
    
        if isinstance(num_1,int) and isinstance(num_2,int):
        #num_1 = int(num_1)
        #num_2 = int(num_2)
            sum = num_1 + num_2
            if sum >= 15 and sum <= 20:
                return 20
            else:
                return sum
        else:
            return "Invalid Input"

print(sum(15,1))        
print(sum(5,5))        
print(sum('5','5'))       
print(sum(-5,-5))
print(sum(5,-5))
print(sum('','')) 
print(sum(2.0,3.3))       
