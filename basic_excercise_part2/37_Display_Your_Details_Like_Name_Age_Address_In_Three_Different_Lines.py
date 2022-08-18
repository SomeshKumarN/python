"""Write a Python program to display your details like name, age, address in three different lines."""

#Solution:

personalDetails = input("Enter name, age, address:").split(',')

print("You Name is:",personalDetails[0])
print("You Agg is:",personalDetails[1])
print("You Address is:",personalDetails[2])