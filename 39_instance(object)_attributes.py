
# Instance(object) Attributes in Python

class user:
    course = 'Java'

o = user()
print(user.__dict__)
print(user.course)  # Print Class attribute
print(o.__dict__)  
print(o.course)  # it has empty attributes => {} so it checks from it's class attributes 
o.course = "C++"   # it will not affect the class attributes
print(o.__dict__) 
print(o.course)
 
o2 = user()
print(o2.course)  # it will not affect the class attributes

# output

# {'__module__': '__main__', 'course': 'Java', '__dict__': <attribute '__dict__' of 'user' objects>, '__weakref__': <attribute '__weakref__' of 'user' objects>, '__doc__': None}
# Java
# {}
# Java
# {'course': 'C++'}
# C++
# Java

# <--------------------------------------------------------->

