
# Diamond Problem

# it is working like switch case 

class A:
    def display(self):
        print("I am the display of Class A")
 
 
class B(A):
    def display(self):
        print("I am the display of Class B")
 
 
class C(A):
    def display(self):
        print("I am the display of Class C")
 
 
class D(B, C):
    def display(self):
        print("I am the display of Class D")
 
 
o = D()
o.display()

# output  
# Note :(if d not declared b will display , b not contains function c display, c also not contains function a display)

# I am the display of Class D