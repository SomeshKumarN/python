# Write a Python program to convert height (in feet and inches) to centimeters.
def heigth(feet, inches):
    try:
        cm = ((feet*12)+inches)*2.54
        print(cm,'centimeters')
    except:
        print('Integer only allowed') 

#Test
heigth(feet = 5,inches = 1)    
heigth('5','2')
heigth(5,3)
