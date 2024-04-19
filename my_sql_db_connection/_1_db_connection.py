
# import mysql.connector when you start the db connection

import mysql.connector

print("DB connected")

# Note : you can give any key like(host,user,password) but values are only give (localhost,root,"")
myDB = mysql.connector.connect(host="localhost",user="root",password="")

# Note : cursor is act like a controller for affect the database
mycursor=myDB.cursor()