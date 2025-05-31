isApplicationReceived = False

def submit_application_using_individual_input_from_user():
    print("Welcome to the Application Form!")
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    email = input("Please enter your email: ")
    submit_application_form(name, age, email)
    
def submit_application_using_only_one_input_from_user():
    print("Welcome to the Application Form!")
    userInput = input("Please enter your details(name,age,email): ")
    splitedInput = userInput.split(",")
    print("Splitted Input: ", splitedInput)
    name = splitedInput[0]
    age = splitedInput[1]
    email = splitedInput[2]
    submit_application_form(name, age, email)
    
def submit_application_form(name, age, email):

    print("\nThank you for filling out the form!")
    print("\n\n\nHere are the details you provided:")
    print("Provided   Name: "+name)
    print("Provided    Age: "+age)
    print("Provided  Email: "+ email)
    
    print("\n\n\nValidating the provided details...")
    # Validating the provided details
    nameValidationResult = isNameValid(name)
    ageValidationResult = isAgeValid(age)
    emailValidationResult = isEmailValid(email)
    print("isNameValid-----",nameValidationResult)
    print("isAgeValid------",ageValidationResult )
    print("isEmailValid----",emailValidationResult)
    
    result = nameValidationResult and ageValidationResult and emailValidationResult
    print("validation result is ----", result)
    
    updateStatus(result)

def isNameValid(name):
    if len(name) < 3:
        print("****************Name must be at least 3 characters long.\n")
        return False
    else:
        return True

def isAgeValid(age):
    if not age.isdigit() or int(age) < 18:
        print("****************Age must be a number and at least 18.\n")
        return False
    else:
        return True

def isEmailValid(email):
    if "@" not in email or "." not in email:
        print("****************Email must contain '@' and '.'\n")
        return False
    else:
        return True

def updateStatus(isResultValid: bool):
    if(isResultValid):
        global isApplicationReceived
        isApplicationReceived = True
def applicationStatus():
    if isApplicationReceived:
        print("\n\nApplication has been received successfully!")
    else:
        print("\n\nApplication has not been received yet.")
        
#Approach 1: Using individual inputs from user        
# submit_application_using_individual_input_from_user()
# applicationStatus()

#Approach 2: Using only one input from user
submit_application_using_only_one_input_from_user()
applicationStatus()

#Basic Logical Operations 
# True -- 1
# False  -- 0

# # Logical Operations - OR (Addition)
# 1+1 = 2(ture)
# 1+0 = 1 (true)
# 0+1 = 1 (true)
# 0+0 = 0 (false)

# # Logical Operations - AND (Multiplication)
# 1*1 = 1 (true)
# 1*0 = 0 (false)
# 0*1 = 0 (false)
# 0*0 = 0 (false)

# 1+1+1 = 3 (true)
# 1*1*1 = 1 (true)
# 1*1*1*1*1*1*0   = 0 (false)

# True and True and True = True
# True and True and False = False