import pandas as pd 
print('''
    press 1 to view file
    press 2 to update
    press 3 to delete
      ''')  

def view_details():
    file = pd.read_csv("pandas/Book1.csv")
    print(file) 
def update_details(msg):
    file = open("pandas/Book1.csv","a")
    file.write(msg+"\n")
    file.close()
    view_details()
def delete_detail():
    pass   

while True:
    choice = int(input('Enter your choice :'))
    if choice == 1:
        view_details()
    elif choice == 2:
        msg = input('Enter content')
        update_details(msg)
    elif choice == 3:
        delete_detail()
    else:
        print('exit')       