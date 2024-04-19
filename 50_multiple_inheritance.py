
# Multiple Inheritance

#   Syntax :
#          class Parent1 :
#                   # attributes and methods of Parent1
#          class Parent2 :
#                   # attributes and methods of Parent2
#          class Child( Parent1, Parent2 ) :
#                   # attributes and methods of Child

class Father:
    def fishing(self):
        print("Fishing in Rivers")
 
    def chess(self):
        print("Playing Chess From Father")
 
 
class Mother:
    def cooking(self):
        print("Cooking Food")
 
    def chess(self):
        print("Playing Chess From Mother")
 
 
class Son(Mother,Father):
    def ride(self):
        print("Riding Bicycle")
o = Son()
o.ride()
o.fishing()
o.cooking()
o.chess()

# output

# Riding Bicycle
# Fishing in Rivers
# Cooking Food
# Playing Chess From Mother