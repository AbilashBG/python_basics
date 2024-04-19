
# Multilevel Inheritance

#   Syntax :
#          class base1 :
#                   body of base class
#          class derived1( base1 ) :
#                   body of derived class
#          class derived2( derived1 ) :
#                   body of derived class
        

class GrandFather:
    def ownHouse(self):
        print("Grandpa House")
 
 
class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike")
 
 
class Son(Father):
    def ownBook(self):
        print("Son Have a Book")
 
 
o = Son()
o.ownHouse()
o.ownBike()
o.ownBook()

# output

# Grandpa House
# Father's Bike
# Son Have a Book