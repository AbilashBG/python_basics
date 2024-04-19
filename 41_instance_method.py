
# instance Methods

class Student:
    name = "Raman"
    age = 25
 
#  Note : if you use instance method the function automatically take the first paramater => self (which is defined by us)
    def printall(self):
        print("Name : ", Student.name)
        print("Age  : ", Student.age)

# create object for the class
o=Student()

# 1.you can use dot method directly => this is recently used by everyone
o.printall()

# output
# Name :  Raman
# Age  :  25

# 2.Also you can use this method => this is old method
Student.printall(o)

# output
# Name :  Raman
# Age  :  25

# <--------------------------------------------------->

class Students:
    name = "Raman"
    age = 25
 
    #  you can pass more params though the function
    def printall(self, gender):
        print("Name : ", Students.name)
        print("Age  : ", Students.age)
        print("Gender  : ", gender)

# create object for the class
x = Students()

x.printall("Male")
Students.printall(x, "Male")

# output

# Name :  Raman
# Age  :  25
# Gender  :  Male
# Name :  Raman
# Age  :  25
# Gender  :  Male

# <---------------------------------------------------->

