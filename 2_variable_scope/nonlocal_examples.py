
def outter():
    msg = "Hello from outer function"
    print("Outer function called, message:", msg)
    def inner():
        nonlocal msg
        msg = "Hello from inner function"
        print("Inner function called, message:", msg)
        def inner_inner():
            nonlocal msg
            msg = "Hello from inner_inner function"
            print("Inner inner function called, message:", msg)
        inner_inner()
    inner()
    print("Outer function called, message:", msg)
    
# outter()

# # outter()

# def parent():
#     list_name = "Groceries"

#     def child():
#         # nonlocal list_name  # Use the parent's variable, not a new one
#         list_name = "Electronics"  # Change it
#         print("Inside child:", list_name)

#     child()
#     print("Inside parent:", list_name)
    

# # parent()

# def get_middle_three_chars(str1):
#     print("Original String is", str1)

#     # first get middle index number
#     mi = int(len(str1) / 2)

#     # use string slicing to get result characters
#     res = str1[mi - 1:mi + 2]
#     print("Middle three chars are:", res)

# get_middle_three_chars("JhonDipPeta1")
# get_middle_three_chars("JaSonAy1")

# # number = 113
# number =254
 

# if( number % 2 == 1 ):
#     print("ODD")
# else:
#     print("EVEN")


name = "John"

def greet():
    global name  # Use the global variable
    print("Hello", name)
    name = "Doe"  # Local variable
    print("Hello", name)  # Prints local variable
    
def age_greet():
   age = 30  # Local variable
   print("Age before inner_greet function is", age)
   def inner_greet():
       nonlocal age # Use the nonlocal variable from age_greet
       age = 25  # Local variable in inner function
       print("Inner age is", age)
       def inner_inner_greet():        
           nonlocal age
           age = 20           
           print("Inner inner age is", age)
       inner_inner_greet()
   inner_greet()
   print("Age after inner_greet function is", age)

# age_greet()  # Calls the function, prints "Hello Doe"

# "4. Enclosing (Nonlocal) Scope
# Write a function outer() that defines a variable text = ""outer"". 
# Inside it, define a function inner() that changes text to ""inner"" 
# using the nonlocal keyword and prints it. Call inner() inside outer() 
# and then print text in outer()."

def outter():
    text = "outer"
    print("Outer function called, text:", text)
    
    def inner():
        nonlocal text
        text = "inner"
        print("Inner function called, text:", text)    
    inner()
    
    print("Outer function called, text after inner call:", text)
    
outter()  # Calls the function, prints "Hello Doe"


def math_operations():
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    return add, subtract, multiply  # Return the functions


add_function, subtract_function, multiply_function = math_operations()  # Unpack the returned functions

add_output = add_function(4,23)
print("Add Output--",add_output)

subtract_output = subtract_function(332,23)
print("Subtract output --", subtract_output)

# Personal Details example

def someshkumar_details():
    def official_name():
        return "Someshkumar Nagarajan"
    def living_city():
        return "thanjavur"
    def country():
        return "India"
    def marrital_status():
        print("married")
    return official_name,living_city,country

official_name, living_city, country=someshkumar_details()

print(official_name())
print(living_city())
print(country())

peru, ooru, nnadu=someshkumar_details()

print(peru())
print(ooru())
print(nnadu())
    
# Another example for non-local

def account():
    account_balance =0
    def deposit(amount):
        nonlocal account_balance
        account_balance += amount     
        print("Deposit function called, amount deposited is:", amount)

    def withdraw(amount):
        nonlocal account_balance
        account_balance -=amount
        print("Withdraw function called, amount withdrawed is:", amount)
        
    def balance_inquiry():
        return account_balance
    return deposit, withdraw, balance_inquiry
    
        
deposit, withdraw, balance_inquiry = account() 
print("\n\nBanking opertions\n~~~~~~~~~~~~~~~~~~~~\n")
print("Account Balance is", balance_inquiry())
deposit(10000)
print("Account Balance is", balance_inquiry())

withdraw(1000)
print("Account Balance is", balance_inquiry())