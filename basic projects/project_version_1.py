import os.path
import pandas as pd
name = ''
"""
issue1:Done: accepting numerical and specialchar , thwoing exception---
issue2:Inprogress-
issue3:NotStarted:
"""
def create_file(name):

    f = open(name,"x")
    f.write("")
    check = os.path.exists(name)

    if check == True:
        print("Successfully File Created")

def create_columns(Fname,column):
    with open(f"{Fname}","a") as file:
        file.write(column+'\n')
    


def view_details(filename):
    print(pd.read_csv(filename))
    print(name)

def insert_details(filename,data):
    with open(f"{filename}","a") as file:
        file.write(f"{data}"+'\n')
    

def delete_details(delete,Filename):
    import csv
    lines = list()
    memberName = delete
    with open(f'{Filename}', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == memberName:
                    lines.remove(row)

    with open(f'{Filename}', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

while True:
    print("""
    Press 1 create new file
    Press 2 create column names
    Press 3 to access the data
    Press 10 exit. 
    """)

    option = int(input("Enter your option :"))
    if option == 1:
        fname = input("Enter Your New File Name :")
        if fname.isalpha() != True :
            exit()
        name = name + f"{fname}.csv"
        create_file(name)

    elif option == 2: 
        try:
            if name[1].isalnum() and '.' in name:
                Fname = name
            else:
                Fname = input("Enter file name with exists :")
                name = name + Fname
        except:
            Fname = input("Enter file name with exists :")
            name = name + Fname 

        check = os.path.exists(name)
        if check != True:
            print("Please Enter Correct File Name.")
        else:
            clmname = input("Enter your column names \nSpace between column names :") 
            columnnam = clmname.replace(' ',',')    
            create_columns(Fname,columnnam)    

   

    elif option == 3:
        print("""
        Press 1 view details
        Press 2 insert data
        Press 3 delete data
        Press above 4 exit
        """)
        
        accessoption = int(input("Enter your option :"))

        if accessoption == 1:

            try:
                if name[1].isalnum() and '.' in name:
                    Fname = name
                else:
                    Fname = input("Enter file name with exists :")
                    name = name + Fname

            except:
                Fname = input("Enter file name with exists :")
                name = name + Fname 

            check = os.path.exists(name)
            if check != True:
                print("Please Enter Correct File Name.")
            else:
                view_details(Fname)

        elif accessoption == 2: # multiple insert columns
            try:
                if name[1].isalnum() and '.' in name:
                    Fname = name
                else:
                    Fname = input("Enter file name with exists :")
                    name = name + Fname
            except:
                Fname = input("Enter file name with exists :")
                name = name + Fname

            check = os.path.exists(name)
            if check != True:
                print("Please Enter Correct File Name.")
            else:
                import pandas 
                columnnames = ''
                read_csv = (pandas.read_csv(Fname))
                column = read_csv.columns.values
                for i in column:
                    columnnames = (columnnames+i)+' '
                print("FILE COLUMNS :",columnnames)  
       
                userdat = input("Enter your data \nspace between one data to another data :")
                userdata = userdat.replace(' ',',')
                insert_details(Fname,userdata)     

        elif accessoption == 3:
            try:
                if name[1].isalnum() and '.' in name:
                    Fname = name
                else:
                    Fname = input("Enter file name with exists :")
                    name = name + Fname
            except:
                Fname = input("Enter file name with exists :")
                name = name + Fname

            check = os.path.exists(name)
            if check != True:
                print("Please Enter Correct File Name.")
            else:
                delete = input("Which Row You Want Delete ?\nEnter The Row Number :")
                delete_details(delete,Fname)

        else:
            exit()

    elif option == 10:
        exit()

    else:
        print("PLEASE ENTER YOUR CORRECT OPTION")