
#SQLite datacase connection 

# in this section we can learn how to connect sqlite database in python 
# before write the code , create SQLite database in the SQLite browser

import sqlite3

con = sqlite3.connect('students.db')

cur = con.cursor()
# Create the 'students' table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        AGE INTEGER NOT NULL,
        CITY TEXT NOT NULL
    );
''')

# ------------------------------------------------------------
#1. insert (add) data to the database using db connection
# ------------------------------------------------------------

def insertData(name,age,city):
    qry="insert into students (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("User Details Added")

# <------------------------------------------------------------>
    
def updateData(name, age, city, student_id):
    qry = "update students set NAME=?, AGE=?, CITY=? where ID=?;"
    con.execute(qry, (name, age, city, student_id))
    con.commit()
    print("User Details Updated")

# <------------------------------------------------------------>
    
def deleteData(student_id):
    qry = "delete from students where ID=?;"
    con.execute(qry, (student_id,))
    con.commit()
    print("User Details Deleted")

# <------------------------------------------------------------>

def selectData():
    qry = "select * from students"
    result = con.execute(qry)
    for row in result:
        print(row)

# <------------------------------------------------------------>

print(
"""
1.Insert
2.Update
3.Delete
4.Select
"""
)

ch=1
while ch ==1:
    c= int(input("Select your choice : "))
    if(c==1):
        print("Add new record")
        name = input("Enter name : ")
        age = int(input("Enter age : "))
        city = input("Enter city : ")

        insertData(name,age,city)


    elif(c==2):
        print("Edit a record")
        id=input("Enter ID : ")
        name=input("Enter Name : ")
        age=input("Enter Age : ")
        city=input("Enter City : ")
        updateData(name,age,city,id)
    

    elif(c==3):
        print("Delete a record")
        id=input("Enter ID : ")
        deleteData(id)


    elif(c==4):
        print("Print all records")
        selectData()


    else:
        print("Invalid selection")

        ch=int(input("Enter 1 to continue"))            
