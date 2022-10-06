# create file--> include column names--> view details
# values inserts---> delete values---> exit
import pandas as pd
import os.path

print("""
Press 1 create new file
Press 2 create column names
Press 3 to access the data
Press Any Key Exit.
""")

filename = input("Enter your access file name :")
def create_file():
    global filename
    f = open(f"{filename}","x")
    f.write("")
    check = os.path.exists(f"{filename}")
    
    if check == True:
        print("Successfully File Created") 

def create_columns(column):
    global filename
    file = open(f"{filename}","a")
    file.write(column+'\n')
def view_details():
    global filename
    file = pd.read_csv(f"{filename}")
    print(file)
def insert_details():
    global filename
    file = open(f"{filename}","a")
    file.write(f"{filename}")
def delete_details():
    pass

while True:
    cho = int(input("Enter your option :"))
    if cho == 1:
        fname = input("Enter Your New File Name With File Exists :")
        # filename.append(fname)
        create_file()
    elif cho == 2:
        # file = input("Enter your file name :")
        columnnames = input("Enter column names with separated by comma :")
        create_columns(columnnames)
    elif cho == 3:
        # file = input("Enter your CSV file name :")
        view_details()
    elif cho == 4:
        userdata = input("Enter your data with separater by comma :")
        insert_details()
    elif cho == 5:
        delete_details()
    else:
        exit()        
