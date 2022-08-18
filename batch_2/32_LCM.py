# Write a Python program to get the least common multiple (LCM) of two positive integers
def  lcm(x,y):   
    try: 
        x = abs(x)  
        y = abs(y)
        g = max(x, y)
        greater = g 

        while(True):
            if ((greater % x == 0) and (greater % y == 0)):  
                print(greater)
                break
            greater += 1
    except:
        print("Invalid Input")        
lcm (4,9)
lcm ('s',4)
lcm(-2,-5)
lcm ('','')
lcm (8,-4)




