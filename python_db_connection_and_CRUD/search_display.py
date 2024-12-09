import mysql.connector
con=mysql.connector.connect(host='localhost',username='root',password='root',database='employees')
if con.is_connected():
    cur=con.cursor()
    print('*************')
    print('wlcome to employee search screen')
    print('**************')
    no=int(input('enter the employee number to search : '))
    query='select * from emp where eno={}'.format(no)
    cur.execute(query)
    data=cur.fetchone()
    if data!=None:
        print(data)
    else:
        print('record not found !!!')
con.close()            
