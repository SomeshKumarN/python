# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name = input("Enter Your first Name :")
last_name = input("Enter Your Last Name :")
name = first_name+" "+last_name
print("Given Name Is :"+name.capitalize())
rev = last_name+" "+first_name
print("Reversed Name Is :"+rev.capitalize())


