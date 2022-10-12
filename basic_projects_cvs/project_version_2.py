# issue1:Done: user option -> thwoing exception -> numerical value only allowed.  
# issue2:Done: create file -> program repairing -> already present filename is not acceptalbe. 
# issue3:Done: insert column names -> once insert a column names acknowledgement message to user.
# issue4:Done: insert values -> file have two columns but user insert three or more values -> should handle this error.
# issue5:Done: create file -> allow file creation in alpha and numerical values.
# issue6:Done: view details-> read empty file -> message to user. This file is empty.
# issue7:Done: create column name -> add column names.
# issue8:inprogress: insert values -> insert multiple values.
# issue9:Done: delete row -> ackwonledgement message to user.
# issue10:Done: optimize user message
# issue11:Done: no one file insert columns they will create new file. so, fix it problem.
# issue12:Done: view details-> file have no data -> message to user 'No data in this file'
# issue13:Done: column names only insert firstline.
# issue14:Done: change value input method -> separator by comma.
# issue15:inprogress:delete details -> get proper input for deletion
# issue16:Done: insert data -> if file is empty. can not insert values.
# issue17:Done: create column -> already file have columns. view columns names and add columns names

import os.path
import pandas as pd
import re
import csv
filename = []
def flname():
    return filename[0]

def create_file(name):
    try:
        f = open(name,"x")
        f.write("")
        check = os.path.exists(name)

        if check == True:
            print("Successfully File Created")
    except:
        print("Already This File Is Avaialbe.So,This file Name Is Not Acceptable.")

def create_columns(Fname,column):
    columnlist = column.split(',')

    if os.stat(Fname).st_size > 0:
        
        with open(Fname) as f:
            read = f.readline()
            splitdata= read.split(',')
            columns = []
            for i in splitdata:
                columns.append(re.sub('\n','',i))
            columns.extend(columnlist)
            readfile = csv.reader(f)
            data = [line for line in readfile]
        with open(Fname,'w',newline='') as f:
            w = csv.writer(f)
            w.writerow(columns)
            w.writerows(data)
            print("Successfully Added Your Columns.")
    else :
        with open(f"{Fname}","w") as file:
            file.write(column+'\n')
            print("Successfully Created Your Columns.")

def view_details(filename):
    
    if os.stat(filename).st_size > 0:
        print(pd.read_csv(filename))
        print("File name is :",flname())
    else:
        print('No Data In This File.')

def insert_details(filename,data):
    with open(f"{filename}","a") as file:
        file.write(f"{data}"+'\n')
        print("Successfully Inserted Your Data.")
    
def delete_details(delete,Filename):
    def check_delete():
        with open(Filename,'r') as read:
            r = read.readlines()
            h = []
            for i in r:
                s = i.split(",")
                for j in s:
                    if str(delete) == j:
                        h.append('True')
                        break
                    else :
                        h.append('False')
        return 'True' in h   

    if check_delete() == True:
        lines = list()
        with open(Filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == str(delete):
                        lines.remove(row)

        print('Enter Numbers Only.')
        with open(Filename, 'w',newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        if check_delete() == False:
            print('Data Deleted.')
        else:
            print('Data is not delete.')
    else:
        print('This data not found.')
    
while True:
    print("""
    Press 1  : Create New file
    Press 2  : Create and Add Column names
    Press 3  : Access the data
    Press 10 : Exit. 
    """)
    try:
        option = int(input("Enter your option :"))
    except:
        print("Please Enter Numerical Values Only.") 
        continue  
    if option == 1:
        fname = input("Enter Your New File Name :")
        if fname.isalnum() != True :
            print("Try Again.")
            continue
        filename.clear()
        filename.append(f"{fname}.csv")
        name = flname()
        create_file(name)

    elif option == 2: 
        try:
            if flname()[0].isalnum() and '.' in flname():
                Fname = flname()
            else:
                Fname = input("Enter file name with exists :")
                filename.clear()
                filename.append(Fname)
        except:
            Fname = input("Enter file name with exists :")
            filename.clear()
            filename.append(Fname)
 
        check = os.path.exists(flname())
        if check != True:
            
            print("Please Enter Correct File Name.")
        else:
            if os.stat(Fname).st_size > 0: 
                print('Already File Have columns.\n')
                with open(Fname) as rd:
                    print('Column Names :',rd.readline().upper())
                try:    
                    columnoption = int(input('If you want add column names.Press 1\nPress any number to Exit.\n\nEnter Your Number :'))
                    if columnoption == 1:
                        clmname = input('Enter Column Names\nMust be column Id\nComma between one data to another data:')
                    else:
                        print('Thank You.')
                        continue
                except:
                    print('Enter Numerical Values Only.')
                    continue    
            else:
                clmname = input("Enter your column names\nMust be column Id\nComma between one data to another data:")
            
            try:
                if clmname[0].isalnum() == True:
                    create_columns(Fname,clmname)
                else:
                    print("Unsuccessful")
            except:
                print("Unsuccessful")             

    elif option == 3:
        print("""
        Press 1  : View Details
        Press 2  : Insert Data
        Press 3  : Delete Data
        Press 10 : Exit
        """)
        try:
            accessoption = int(input("Enter your option :"))
        except:
            print("Please Enter correct option.")
            continue
        if accessoption == 1:
            try:
                if flname()[0].isalnum() and '.' in flname():
                    Fname = flname()
                else:
                    Fname = input("Enter file name with exists :")
                    filename.clear()
                    filename.append(Fname)
            except:
                Fname = input("Enter file name with exists :")
                filename.clear()
                filename.append(Fname)
    
            check = os.path.exists(flname())
            if check != True:
                print("Please Enter Correct File Name.")
            else:
                view_details(Fname)

        elif accessoption == 2: 
            try:
                if flname()[0].isalnum() and '.' in flname():
                    Fname = flname()
                else:
                    Fname = input("\nEnter file name with exists :")
                    filename.clear()
                    filename.append(Fname)
            except:
                Fname = input("\nEnter file name with exists :")
                filename.clear()
                filename.append(Fname)
    
            check = os.path.exists(flname())
            if check != True:
                print("Please Enter Correct File Name.")
            else:
                import pandas 
                columnnames = ''
                
                if os.stat(Fname).st_size > 0:
                    read_csv = (pandas.read_csv(Fname))
                    column = read_csv.columns.values
                else:
                    print('No Columns In This File.')
                    continue
                for i in column:
                    columnnames = (columnnames+i)+' '
                  
                print("\nCOLUMNS NAMES :",columnnames.upper())  
       
                import pandas
                a = pandas.read_csv('som.csv')
                d = len(a.columns.values)
                
                lis = []
                while True:
                    i = input('Enter data :')
                    if i:
                        length = i.split(',')
                        if len(length) == d:
                            lis.append(i+'\n')
                        else:
                            print(f"File have {d} Columns.But, You Insert Above {d} Values.\nTry Again.")    
                    else:
                        break

        elif accessoption == 3:
            try:
                if flname()[0].isalnum() and '.' in flname():
                    Fname = flname()
                else:
                    Fname = input("Enter file name with exists :")
                    filename.clear()
                    filename.append(Fname)
            except:
                Fname = input("Enter file name with exists :")
                filename.clear()
                filename.append(Fname)
    
            check = os.path.exists(flname())
            if check != True:
                print("Please Enter Correct File Name.")
            else:
                try:
                    delete = int(input("Which Row You Want Delete ?\nEnter The Row Number :"))
                    delete_details(delete,Fname)
                except:
                    print('Enter Numbers Only.')

        elif accessoption == 10:
            exit()

        else:
            print("PLEASE ENTER YOUR CORRECT OPTION") 
    elif option == 10:
        exit()

    else:
        print("PLEASE ENTER YOUR CORRECT OPTION")