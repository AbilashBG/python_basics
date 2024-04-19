
# init method in Python
 
class user:
    def __init__(self, name):
        print("Call When new Instance Created")
        self.name = name
 
    def printall(self):
        print("Name : ", self.name)

# Note : each time you call the instance(object) __init__ method will call
 
 
o1 = user("Basic Python")
 
o1.printall()
print(o1.__dict__)
o2 = user("Python")
o2.printall()
print(o2.__dict__)
print(user.__dict__)

# output

# Call When new Instance Created
# Name :  Basic Python
# {'name': 'Basic Python'}      
# Call When new Instance Created
# Name :  Python
# {'name': 'Python'}
# {'__module__': '__main__', '__init__': <function user.__init__ at 0x000001B57BEE5440>, 'printall': <function user.printall at 0x000001B57BEE5260>, '__dict__': <attribute '__dict__' of 'user' objects>, '__weakref__': <attribute '__weakref__' of 'user' objects>, '__doc__': None}