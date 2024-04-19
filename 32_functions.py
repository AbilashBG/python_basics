
# Functions in python

# 1.No Return Type With Argument Function
# 2.No Return Type Without Argument Function
# 3.Return Type Without Argument Function
# 4.Return Type With Argument Function

# 5.Arbitrary Arguments Function in Python (*)
# 6.Keyword Arguments Function in Python
# 7.Arbitrary Keyword Arguments in Python(**)
# 8.Default Parameter Function in Python
# 9.Passing a List as an Argument in Function Python
# 10.recursive function
# 11.Lambda function

def welcome():
    print("Welcome To Tutor Joes")
 
 
welcome()

# output

# Welcome To Tutor Joes

# <----------------------------------------------------------------------------------------------->
 
# 1.No Return Type Without Argument Function in Python

def add():
    a=int(input("Enter The Value of A : "))
    b=int(input("Enter The Value of B : "))
    c=a+b
    print("Total ",c)
 
add()

# output

# Enter The Value of A : 10
# Enter The Value of B : 20
# Total  30

# <----------------------------------------------------------------------------------------------->
 
# 2.No Return Type With Argument Function in Python

def sub(a, b):
    c = a - b
    print("Difference : ", c)
 
 
sub(25, 2)

# output

# Difference :  23

# <----------------------------------------------------------------------------------------------->
 
# 3.Return Type Without Argument Function in Python

def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a * b
    return c
 
 
x=mul()
print("Mul ",x)

# output

# Enter The Value of A : 20
# Enter The Value of B : 10
# Mul  200

# <----------------------------------------------------------------------------------------------->
 
# 4.Return Type With Argument Function in Python

def div(a, b):
    c = a / b
    return c
 
 
x = div(25, 2)
print("Division ", x)

# output

# Division  12.5

# <----------------------------------------------------------------------------------------------->
 
# 5.Arbitrary Arguments Function in Python (*)

def class_10(*students):
    print(students)
    for user in students:
        print(user)
 
 
class_10("Ram", "Sam", "Raja", "Sara")

# output

# ('Ram', 'Sam', 'Raja', 'Sara')
# Ram
# Sam
# Raja
# Sara

# <----------------------------------------------------------------------------------------------->
 
# 6.Keyword Arguments Function in Python
 
def message(name, age):
    print(name, " age is ", age)
 
 
message(age=25, name="Ram")

# output

# Ram  age is  25

# <----------------------------------------------------------------------------------------------->
 
# 7.Arbitrary Keyword Arguments in Python(**)

def bioData(**data):
    print(data)
 
 
bioData(name="Ram Kumar", age=25, gender="Male")

# output

# {'name': 'Ram Kumar', 'age': 25, 'gender': 'Male'}

# <----------------------------------------------------------------------------------------------->

# 8.Default Parameter Function in Python

def user(name, city="Salem"):
    print(name, " is from ", city)
 
 
user("Ram", "Namakkal")
user("Sam")

# output

# Ram  is from  Namakkal
# Sam  is from  Salem

# <----------------------------------------------------------------------------------------------->
 
# 9.Passing a List as an Argument in Function Python

def total(marks):
    return sum(marks)
 
 
print("Total : ",total([55, 75, 80, 95, 47]))

# output

# Total :  352

# <----------------------------------------------------------------------------------------------->
 
# 10.recursive function
# 1 * 2 * 3 * 4 * 5=120

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))
 
 
print("Factorial : ", factorial(5))

"""
factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1
120
"""

# output

# Factorial :  120

# <----------------------------------------------------------------------------------------------->
 
#  11.Lambda function

c = lambda a: a + 50
print(c(5))
 
c = lambda a, b: a * b
print(c(10, 25))

# output

# 55
# 250

# <----------------------------------------------------------------------------------------------->
