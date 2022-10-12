# issue1:Done: insert values -> insert multiple values.
# issue2:Done: delete details -> get proper input for deletion
# issue3:Done: stay sub comment line.
# issue4:Done: decrease program code 
import os.path
import pandas as pd
import re
import csv
filename = []
def flname():
    return filename[0]
filename = []

def check_file_name():   
    try:
        if flname()[0].isalnum() and '.' in flname():
            return flname()
        else:
            Fname = input("Enter file name with exists :")
            filename.clear()
            filename.append(Fname)
            return Fname
    except:
        Fname = input("Enter file name with exists :")
        filename.clear()
        filename.append(Fname)
        return Fname 

def check_file():
    check = os.path.exists(flname())
    if check != True:
        print("//Please Enter Correct File Name.//")
        filename.clear()
        return False
    else:
        return True   

def create_file(name):
    try:
        f = open(name,"x")
        f.write("")
        check = os.path.exists(name)
        if check == True:
            print("//Successfully File Created.//")
    except:
        print("//Already This File Is Avaialbe.So,This file Name Is Not Acceptable.//")

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
            print("//Successfully Added Your Columns.//")
    else :
        with open(Fname,"w") as file:
            file.write(column+'\n')
            print("//Successfully Created Your Columns.//")

def view_details(filename):
    if os.stat(filename).st_size > 0:
        data = pd.read_csv(filename)
        print(data.to_string())
        print("File name is :",flname())
    else:
        print('//No Data In This File.//')

def insert_details(filename,data):
    with open(filename,'a',newline='') as insert:
        insert.writelines(data)
        print("//Successfully Inserted Your Data.//")
    
def delete_details(delete,Filename):
    lines = []
    with open(Filename) as read:
        lines = list(csv.reader(read))
        if len(lines)>delete+1:
            lines.pop(delete+1)
            with open(Filename,'w',newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
                print('//\nSuccessfully Deleted.//')
        else:
            print(f'//Incorrect Row Number ,Only {len(lines)} Rows are avaiable in file.//')
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
        print("//Please Enter Numerical Values Only.//") 
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
        Fname = check_file_name()
        if check_file() == False:
            pass
        else:
            if os.stat(Fname).st_size > 0: 
                print('//Already File Have columns.\n//')
                with open(Fname) as rd:
                    print('Column Names :',rd.readline().upper())
                try:    
                    columnoption = int(input('//If you want add column names.Press 1\nPress any number to Exit.//\n\nEnter Your Number :'))
                    if columnoption == 1:
                        clmname = input('//Enter Column Names\nComma between one data to another data.//')
                    else:
                        print('//Thank You.//')
                        continue
                except:
                    print('//Enter Numerical Values Only.//')
                    continue    
            else:
                clmname = input("//Enter Column Names\nComma between one data to another Data.//")
            try:
                if clmname[0].isalnum() == True:
                    create_columns(Fname,clmname)
                else:
                    print("//Unsuccessfull.//")
            except:
                print("//Unsuccessfull.//")             
    elif option == 3:
        def loop(accessoption):
            if accessoption == 4:
                return False
            else:
                return True       
        accessoption = 0  
        while loop(accessoption) :
            print("""
            Press 1  : View Details
            Press 2  : Insert Data
            Press 3  : Delete Data
            Press 4  : Previous Page.
            Press 10 : Exit
            """)
            try:
                accessoption = int(input("Enter your option :"))
            except:
                print("//Please Enter correct option.//")
                continue
            if accessoption == 1:
                Fname = check_file_name()
                if check_file() == False:
                    pass
                else:
                    view_details(Fname)
            elif accessoption == 2: 
                Fname = check_file_name()
                if check_file() == False:
                    pass
                else:
                    columnnames = ''
                    import pandas
                    if os.stat(Fname).st_size > 0:
                        read_csv = pandas.read_csv(Fname)
                        column = read_csv.columns.values
                    else:
                        print('//No Columns In This File.//')
                        continue
                    for i in column:
                        columnnames = (columnnames+i)+' ' 
                    print("\nCOLUMNS NAMES :",columnnames.upper())
                    print("\n//Enter Your Data. \nComma between one data to another data \nPress Double Enter Exit To Write Rows://")  
                    import pandas
                    a = pandas.read_csv(Fname)
                    d = len(a.columns.values)
                    lis = []
                    while True:
                        i = input()
                        if i:
                            length = i.split(',')
                            if len(length) <= d:
                                lis.append(i+'\n')
                            else:
                                print('\n'f"//File have {d} Columns.But, You Insert Above {d} Values.\nEnter Data Again.//")    
                        else:
                            break
                    if len(lis) >= 1:   
                        insert_details(Fname,lis)
                    else:
                        print('//Unsuccesfull.//')    
            elif accessoption == 3:
                Fname = check_file_name()
                if check_file() == False:
                    pass
                else:
                    print(' ')
                    if os.stat(Fname).st_size > 0:
                        import pandas
                        read = pandas.read_csv(Fname)
                        check_values = len(read.values) 
                        if os.stat(Fname).st_size > 0 and check_values > 0:
                            view_details(Fname)
                            try:
                                delete = int(input("//Which Row You Want Delete ?//\nEnter The Row Number :"))
                                delete_details(delete,Fname)
                            except:
                                print('//Enter Numbers Only.//')    
                        else:
                            print('//No Data This File.//')
                    else:
                            print('//No Data This File.//')                
            elif accessoption == 10:
                exit()
            else:
                if accessoption != 4:
                    print("//PLEASE ENTER YOUR CORRECT OPTION.//")  
        else:
            continue
    elif option == 10:
        exit()
    else:
        print("//PLEASE ENTER YOUR CORRECT OPTION.//")