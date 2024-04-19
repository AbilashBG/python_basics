
# Class and Object in Python

# Syntax of Class:
#       class Class_Name :
#             # statements
     
# Syntax of Object:
#       object_name = class_name ( arguments )

class car():
# pass is used for not affect the class which has no attributes and functions  
    pass
 
 
a = 10
print(type(a))
print(type(car))

# create object for a class below
swift=car()
 
print(isinstance(swift,car))
print(isinstance(a,int))
print(type(swift))

# output

# <class 'int'>
# <class 'type'>
# True
# True
# <class '__main__.car'>