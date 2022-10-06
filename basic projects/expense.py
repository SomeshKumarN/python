import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="mysql",database="details")
from tabulate import tabulate

def show_details():
    
    connection = mydb.cursor()
    quary = "SELECT * FROM tab"
    connection.execute(quary)
    res = connection.fetchall()
    print(tabulate(res))

def update_details(id,date,content,cost):
    connection = mydb.cursor()
    q = "insert into tab(id,date,content,how_much) values(%s,%s,%s,%s)"
    tab = (id,date,content,cost)
    connection.execute(q,tab)
    mydb.commit()
    show_details()

def delete_details(idnumber):
    connection = mydb.cursor()
    q = "delete from tab where id=%s"
    t = (idnumber,)
    connection.execute(q,t)
    mydb.commit()
    show_details()

while True:
    print("""
    Enter 1 : See details 
    Enter 2 : Update details
    Enter 3 : Delete details
    Enter 4 : quit
    """)
    choose = int(input("Enter your choice :"))
    if choose == 1:
        show_details()
    elif choose == 2:
        id = int(input("Enter your number :"))
        date = input("Enter your Date :")
        content = input("Enter your Content :")
        cost = input("How Much Cost :")
        update_details(id,date,content,cost)
    elif choose == 3:
        idnumber = int(input("Enter which id you want delete :"))
        delete_details(idnumber)
    elif choose == 4:
        quit()
    else:
        print("Sorry, You Enter Your correct option")                
