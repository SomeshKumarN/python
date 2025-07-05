# Decision Making
# This module contains functions for decision-making processes.
# If statements
# IF-else Statements
# If-elif-else Statements
# Nested If Statements
# Ternary Operator


# Syntax for if statements:
# if condition:
#     # code to execute if condition is true

# Example:

from calendar import week


def markGT35(mark):
    return mark>35

mark = 15
# isHePassed = mark>35


# if markGT35(mark):  # True condition
#     print("Passed")
# else:
#     print("Fail")
    
    
lightingStatus = "OFF"

def isLightOn():
    # if lightingStatus == "ON":
    #     return True
    # else: 
    #     return False
    return lightingStatus == "ON"
    
def checkLightStatus():
    if isLightOn():
        print("Light is Already ON")
    else:
        print("Light is OFF. So turn the Light ON")
        global lightingStatus
        lightingStatus = "ON"
        checkLightStatus()

# checkLightStatus()

# if-elif-else    
temparature = 1
NormalValue = 35
    
if temparature == NormalValue:
    print("Normal Temparature")
elif temparature < 0:
    print("Extreme Cold Weather")
elif temparature > 100:
    print("Extreme Hot Weather")
elif temparature < NormalValue :
    print("Below Normal")
elif temparature > NormalValue:
    print("Above Normal")

else:
    print("else block")
    
# Ternary Operator

resutl = "Normal Temparature" if temparature == NormalValue else "Not Normal"

result =""
if( temparature == NormalValue)    :
    result ="Normal Temparature"
else:
    result ="Not Normal"
    
    
    
#Nested If 

groomDetails ={
    'name':'Thirumal',
    'age':26,
    'gender':'Male',
    'blood_group':'B+ve',
    'has_sibling': True,
    'salary':50000,
    'isWorking':True,
    'education':'BCA'
}

# age=26
# sibliges - yes
# education - MCA
# salary - 40000

if groomDetails['education'] == "BCA":
    print("Good education.proceed with further conditions")
    if groomDetails['isWorking'] == True:
        print("He is working, proceed furhter")
        if groomDetails["salary"] >35000:
            print("Salary condition met.")
        else:
            print('Salary condtion not met.')
    else:
        print("He is not working. So condition not met.")
else:
    print("Primary condition not met.")
    
    
if (groomDetails['education'] == "BCA" and 
    groomDetails['isWorking'] and 
    groomDetails["salary"] >35000):
    print("all conditions met")
else:
    print("conditions not met.")






# Switch Case Statements
# Python does not have a built-in switch-case statement like some other languages.
# However, you can achieve similar functionality using dictionaries or if-elif-else statements.



def switch_case_example(value):
    switcher = {
        "TEST": "Case 1",
        "BEST": "Case 2",
        "OOP": "Case 3"
    }
    return switcher.get(value, "Default case")


def switch_case_example_if(value):
    if value == 1:
        return "Case 1"
    elif value == 2:
        return "Case 2"
    elif value == 3:
        return "Case 3"
    else:
        return "Default case"

result = switch_case_example("TEST")
print(result)  
