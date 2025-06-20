# Relational Operator
# 1. Less Than (<)
# 2. Greater Than (>)
# 3. Less Than or Equal (<=)
# 4. Greater Than or Equal (>=)
# 5. Equal to (==)
# 6. Not Equal to (!=)
# All these operators are going to result only either TRUE or FALSE


#Less Than
a = 10
b = 5
print("Action-1---->",a < b)
print("Action-2---->",a > b)
b = 10
print("Action-3---->",a <= b)
print("Action-4---->",a >= b)

print("Action-5---->",a == b)
print("Action-6---->",a != b)

x = "test"
y = "test1"

print("Action-7---->",x == y)
print("Action-8---->",x != y)
print("Action-8---->",x < y)

age = 10

if(age>=18):
    print ('Person is eligible to Vote')
else:
    print ('Person is NOT eligible to Vote')


def checkCity(city :str):
    isMatched = (city == 'Thanjavur')
    # if(isMatched):
    #     print('City Matched')
    # else:
    #     print('city not matched')
    return isMatched
        
personDetails = [
    {'name': 'Somesh', 'city': 'Thanjavur'},  #0
    {'name': 'Kumar', 'city': 'Chennai'},     #1
    {'name': 'Selva', 'city': 'Bangalore'},   #2
    {'name': 'Kumari', 'city': 'Pune'},       #3
    {'name': 'Anjali', 'city': 'Delhi'},      #4
    {'name': 'Rajesh', 'city': 'Thanjavur'},  #5
    {'name': 'Meena', 'city': 'Coimbatore'},  #6
    {'name': 'Vignesh', 'city': 'Madurai'},   #7
    {'name': 'Rekha', 'city': 'Ahmedabad'},   #8
    {'name': 'Prakash', 'city': 'Thanjavur'},    #9
    {'name': 'Swathi', 'city': 'Trichy'},     #10
    {'name': 'Arun', 'city': 'Kolkata'},      #11
    {'name': 'Divya', 'city': 'Vizag'},       #12
    {'name': 'Naveen', 'city': 'Thanjavur'},#13
    {'name': 'Lakshmi', 'city': 'Ernakulam'}, #14
    {'name': 'Gokul', 'city': 'Vellore'},     #15
    {'name': 'Preethi', 'city': 'Salem'},     #16
    {'name': 'Surya', 'city': 'Kanchipuram'}, #17
    {'name': 'Deepa', 'city': 'Tiruchendur'}, #18
    {'name': 'Sathish', 'city': 'Erode'},     #19
    {'name': 'Harini', 'city': 'Noida'},      #20
    {'name': 'Ravi', 'city': 'Mysore'},       #21
    {'name': 'Vidya', 'city': 'Thrissur'},    #22
    {'name': 'Manoj', 'city': 'Bhubaneswar'}, #23
    {'name': 'Pooja', 'city': 'Guwahati'},    #24
]
             
print(personDetails[1])
print(personDetails[1]['city'])
print(checkCity(personDetails[1]['city']))

for data in personDetails:
    city = data['city']
    if(checkCity(city)):
        print(data['name'])

