
# Class Methods
class Student:
    name = "Python Program"
    age = 25
 
    def printall():
        print("Name : ", Student.name)
        print("Age  : ", Student.age)
 
 
Student.printall()
print(Student.__dict__)

# output

# Name :  Python Program
# Age  :  25
# {'__module__': '__main__', 'name': 'Python Program', 'age': 25, 'printall': <function Student.printall at 0x0000
# 018BF0F75440>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__'
# of 'Student' objects>, '__doc__': None}
# PS D:\python_basics>
 
print(getattr(Student, "printall"))
# you can use () in last because it is function 
getattr(Student, "printall")()

# output

# <function Student.printall at 0x0000020982255440>
# Name :  Python Program
# Age  :  25
 
Student.__dict__['printall']()

# output

# Name :  Python Program
# Age  :  25
 