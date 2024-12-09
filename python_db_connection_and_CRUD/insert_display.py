import mysql.connector

# Establish connection to MySQL
try:
    con = mysql.connector.connect(host='localhost', user='root', password='root', database='employees')  # Fixed typo: 'database'
    
    if con.is_connected():
        cur = con.cursor()
        opt = 'y'
        
        while opt.lower() == 'y':
            try:
                # Take input from the user
                emp_no = int(input('Enter employee number: '))
                name = input('Enter the employee name: ')
                gender = input('Enter employee gender (m/f): ')
                salary = int(input('Enter employee salary: '))
                
                # Use parameterized queries to prevent SQL injection
                query = "INSERT INTO EMP (ENO, ENAME, GENDER, SALARY) VALUES (%s, %s, %s, %s)"
                values = (emp_no, name, gender, salary)
                cur.execute(query, values)  # Execute the query with the provided values
                con.commit()
                print("Record stored successfully")
            except ValueError:
                print("Please enter valid input (e.g., integer for employee number and salary).")
            
            # Ask if the user wants to add another employee
            opt = input("Do you want to add another employee's details (y/n): ")

        # After insertion, retrieve and display all employee data
        query = "SELECT * FROM EMP"
        cur.execute(query)
        data = cur.fetchall()
        print("\nEmployee Records:")
        for record in data:
            print(record)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if con.is_connected():
        con.close()  # Ensure the connection is closed after the operations
