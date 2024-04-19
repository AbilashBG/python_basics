import _2_db_creation as dbData

# Connect to the database
myDB = dbData.dbcon.myDB
mycursor = dbData.dbcon.mycursor

# Explicitly select the database
mycursor.execute("USE employee")

# ------------------------------------------------------------
# 1. insert (add) data to the database using db connection
# ------------------------------------------------------------

def insertData(name, address):
    qry = "INSERT INTO emp_details (name, address) VALUES (%s, %s);"
    mycursor.execute(qry, (name, address))
    myDB.commit()
    print("Employee Details Added")

# <------------------------------------------------------------>

def updateData(name, address, emp_id):
    qry = "UPDATE emp_details SET name = %s, address = %s WHERE id = %s;"
    dbData.dbcon.mycursor.execute(qry, (name, address, emp_id))
    dbData.dbcon.myDB.commit()
    print("Employee Details Updated")

# <------------------------------------------------------------>

def deleteData(emp_id):
    qry = "DELETE FROM emp_details WHERE id = %s;"
    dbData.dbcon.mycursor.execute(qry, (emp_id,))
    dbData.dbcon.myDB.commit()
    print("User Details Deleted")

# <------------------------------------------------------------>

def selectData():
    qry = "SELECT * FROM emp_details"
    dbData.dbcon.mycursor.execute(qry)
    result = dbData.dbcon.mycursor.fetchall()
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

ch = 1
while ch == 1:
    c = int(input("Select your choice : "))

    if c == 1:
        # Add new record
        print("Add new record")
        name = input("Enter name : ")
        address = input("Enter address : ")

        insertData(name, address)

    elif c == 2:
        # Update record
        print("Edit a record")
        emp_id = input("Enter ID : ")
        name = input("Enter Name : ")
        address = input("Enter Address : ")

        updateData(name, address, emp_id)

    elif c == 3:
        # Delete record
        print("Delete a record")
        emp_id = input("Enter ID : ")

        deleteData(emp_id)

    elif c == 4:
        # Select records
        print("Print all records")
        selectData()

    else:
        print("Invalid selection")

    ch = int(input("Enter 1 to continue: "))
