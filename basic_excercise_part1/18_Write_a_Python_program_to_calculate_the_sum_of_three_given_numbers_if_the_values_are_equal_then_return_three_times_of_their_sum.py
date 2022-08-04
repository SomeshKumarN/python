# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum.

#Solution:

list = list(map(int, input("Enter 3 number in comma separated:").split(',')))
if(list[0]==list[1]==list[-1]):
    print("Result is:", pow(list[1],3))
else:
    print("Result:",list[0]+list[1]+list[2])