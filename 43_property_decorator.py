
# Property Decorator
 
class user:
    def __init__(self, name, age):

#  self.name, self.age are instance variables
        self.name = name
        self.age = age
        # self.msg = self.name + " is " + str(self.age) + " years old"

# if more person working in the same project ,they use msg as attribute but ,
# we use msg as function so that wont affect the code therfore we use @property 
 
    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " years old"
 
 
o = user("Raman", 25)
print(o.name)
print(o.age)
# if we use msg as function only then use print(o.msg()) 
print(o.msg)
o.age = 45
# if we use msg as function only then use print(o.msg()) 
print(o.msg)

# output

# Raman
# 25
# Raman is 25 years old
# Raman is 45 years old