# Membership operators
# # In Python, there are two membership operators: in and not in.
# This can be used in Lists, Tuples, Sets, Dictionaries, Strings, etc.

# Identity operators
# In Python, there are two identity operators: is and is not.

amazon_subscribed_customers = ["Alice", "Bob", "Charlie", "David"]


new_customer = "James"


# for customer in amazon_subscribed_customers:
#     if(customer == new_customer):
#         print("new customer is already subscribed to Amazon.")
#         break
    # print("Checking if customer is subscribed to Amazon...")


is_subscribed = new_customer not in amazon_subscribed_customers
print(is_subscribed)



print("Sting check --","Ama" in "Amazon")

print("Sting check --","Ama" not in "Amazon")

# if(new_customer in amazon_subscribed_customers):
#     print(f"{new_customer} is already subscribed to Amazon.")
# else:
#     print(f"{new_customer} is not subscribed to Amazon. Adding to the list.")
    
integer_list = [1, 2, 3, 4, 5]
new_number = 6

print(new_number in integer_list)


## Identity operators
# Identity operators are used to compare the memory locations of two objects.
# In Python, there are two identity operators: is and is not.   

print('2' == '2')  # True, same value
print('2' is '2')  # True, same memory location
print(2 is 2)  # True, same memory location
print(2 == 2)  # True, same memory location
