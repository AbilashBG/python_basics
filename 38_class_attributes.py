
# class attributes

# 1.getting attributes => 1.getattr method 2.Dot Notation
# 2.setting attributes => 1.setattr method 2.Dot Notation
# 3.deleting attributes

class Student():
    name = "Ram Kumar"
    age = 25

#  1.getting attributes => 1.getattr method
#  =========================================
    
print(getattr(Student, 'name'))
print(getattr(Student, 'age'))
# we can give third attribute for avoiding exception
print(getattr(Student, 'gender', 'No Such Attribute Found'))

# output

# Ram Kumar
# 25
# No Such Attribute Found

# <------------------------------------------------------------------------------>

#  1.getting attributes => 2.Dot Notation
#  =========================================

print(Student.name)
print(Student.age)

# output

# Ram Kumar
# 25

# <------------------------------------------------------------------------------>

# 2.setting attributes => 1.setattr method
# =========================================

setattr(Student, 'name', 'Narendra Modi')
print(Student.name)
 
setattr(Student, 'gender', 'Male')
print(Student.gender)

# output

# Narendra Modi
# Male

# <------------------------------------------------------------------------------>

# 2.setting attributes => 2.Dot Notation
# =========================================

Student.city = "Salem"
print(Student.city)

# output

# Salem

# <------------------------------------------------------------------------------>

# 3.deleting attributes
# =====================

print(Student.__dict__)

# city will delete
delattr(Student,"city")
print(Student.__dict__)

# gender will delete
del Student.gender
print(Student.__dict__)

# output

# {'__module__': '__main__', 'name': 'Narendra Modi', 'age': 25, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None, 'gender': 'Male', 'city': 'Salem'}
# {'__module__': '__main__', 'name': 'Narendra Modi', 'age': 25, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None, 'gender': 'Male'}
# {'__module__': '__main__', 'name': 'Narendra Modi', 'age': 25, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}

# <----------------------------------------------------------------->