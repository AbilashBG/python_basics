

# Single Inheritance

#   Syntax :
#          class base1 :
#               body of base class
#          class derived( base1) :
#               body of derived class

class Nokia:
    company = "Nokia India"
    webiste = "www.nokia-india.com"
 
    def contact_details(self):
        print("Address : Cherry Road,Near Bus Stand ,Salem")
 
 
class Nokia1100(Nokia):
    def __init__(self):
        self.name = "Nokia 1100"
        self.year = 1998
 
    def product_details(self):
        print("Name     : ", self.name)
        print("Year     : ", self.year)
        print("Company  : ", self.company)
        print("Website  : ", self.webiste)
 
 
mobile = Nokia1100()
mobile.product_details()
mobile.contact_details()

# output

# Name     :  Nokia 1100
# Year     :  1998
# Company  :  Nokia India
# Website  :  www.nokia-india.com
# Address : Cherry Road,Near Bus Stand ,Salem