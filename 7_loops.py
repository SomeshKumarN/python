# Loops 
# # Loops are used to iterate over a sequence (like a list, tuple, or string)
# # or to repeat a block of code multiple times.
# 1. For Loop
# 2. While Loop
# 3. Nested Loops
# 4. Loop Control Statements (break, continue, pass)


# 1. For Loop
# A for loop is used to iterate over a sequence (like a list, tuple, or string).

numbers = [11,50,25, 29, 103, 4, 5]

for number in numbers:
    
    if ( number>20 and number<30):
        continue;
    
    if( number >100):
        break;

    print("\n\nInput number is:", number)
    if number<10 or number%2==0:
        print("Number is less than 10 or even")
        print("Result is:",number +2)
    else:
        print("Condition not met")
        

range1 = [1,2,3,4,5,"Chumma",6,7,8,9]        



for i in range1:
    if(i=="Chumma"):
        continue
    if(i==7):
        break
    # print('*' * i)
    
range2 = [1,2,3,4,5]  

bharathi = range2[4]

for i in range2:
    value = ' '* (bharathi-i)+'*' * i
    # print(value)
    
# **********
#  ********
#   ****** 
#    ****
#     ** 
#     **
#    ****
#   ******
#  ********
# **********    


# while(condition):
    # statements
    # code
# else:
    # statement

index=1
while(index != 5):
    # print('*' * index)
    index +=1
    
n =25   
index = n
while(index>0):
    print(' '*(n-index)+'*'* index+'*'* index)
    index -=1
    
temp = n   
for i in range(n):
    print(' '* (temp-i)+'*' * i+"*" *i)


N = range(7)
for I in N:
    print(' '*I +"*****")
