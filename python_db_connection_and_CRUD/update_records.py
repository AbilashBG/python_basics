import mysql.connector
con=mysql.connector.connect(host='localhost',username='root',password='root',database='employees')
if con.is_connected():
    cur=con.cursor()
    print('************')
    print('welcome to employees detail update screen')
    print('***********')
    no=int(input('enter the employee to update:'))
    query='select * from emp where eno={}'.format(no)
    cur.execute(query)
    data=cur.fetchone()
    if data!=None:
        print('record found details are : ')
        print(data)
        ans=input('do u want to update the salary of te above employee(y/n)')
        if ans=='y' or ans=='y':
            new_sal=int(input('enter the new salary of an employee'))
            q1='update emp set salary={} where eno={}'.format(new_sal,no)
            cur.execute(q1)
            con.commit()
            print('employee salary updated seccessfully')
            q2='select * from emp'
            cur.execute(q2)
            data=cur.fetchall()
            for i in data:
                print(i)

    else:
        print('record not found')    
           