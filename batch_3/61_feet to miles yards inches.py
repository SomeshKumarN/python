# Write a Python program to convert the distance (in feet) to inches, yards, and miles.
def distance(feet):
        # 1 feet = 12 inches
        inches = 12*feet
        # 1 yards = 3feet
        yards = feet/3
        # 1 yard = 1760 yards
        # input is feet so convert yard to feet 
        miles = feet/5280
   
        print(inches,'inches')
        print(yards,'yards')
        print(miles,'miles')    
try:
    feet = int(input('Enter the Feet value :')) 
    distance(feet)       
except:
    print('Integer only allowed')
   