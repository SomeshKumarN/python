#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 

#Solution:

from audioop import reverse


firstName = input("Enter First Name:")
lastName = input("Enter Last Name:")
print("Given name is",firstName+" "+lastName)
print("Reversed name is",lastName+" "+firstName)

#by slicing the string
print("Reversed name is",lastName[::-1]+" "+firstName[::-1])

#using inbuid reversed method
print("Reversed name is",''.join(reversed(lastName))+" "+''.join(reversed(firstName)))