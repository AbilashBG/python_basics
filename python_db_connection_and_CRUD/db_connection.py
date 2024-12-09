import mysql.connector

# Function to create database
def create_db():
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='root')
        if con.is_connected(): 
            cur = con.cursor()
            q = 'CREATE DATABASE IF NOT EXISTS employees'  # Check if the database already exists
            cur.execute(q)
            print('Employee database created successfully or already exists.')
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        con.close()  # Always close the connection

# Function to create table
def create_table():
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='root', database='employees')
        if con.is_connected():
            cur = con.cursor()
            q = '''CREATE TABLE IF NOT EXISTS EMP (
                        ENO INT PRIMARY KEY,
                        ENAME VARCHAR(20),
                        GENDER VARCHAR(3),
                        SALARY INT
                    )'''
            cur.execute(q)
            print('Employee table created successfully or already exists.')
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        con.close()  # Always close the connection

# Main function to interact with the user
def main():
    ch = 'y'
    while ch.lower() == 'y':
        print('\nInterfacing Python with MySQL')
        print('1. To create database')
        print('2. To create table')
        try:
            opt = int(input('Enter your choice: '))
            if opt == 1:
                create_db()
            elif opt == 2:
                create_table()
            else:
                print('Invalid choice.')
        except ValueError:
            print('Please enter a valid number.')

        ch = input('Do you want to perform another operation (y/n): ').strip()

# Run the program
if __name__ == "__main__":
    main()
