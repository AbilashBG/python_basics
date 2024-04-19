
# IF Else Statement in Python

#   Syntax :
#         if ( condition ) :
#                // body of the statements will execute if the condition is true
#         else :
#                // body of the statements will execute if the condition is false

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
if age >= 18:
    print(name, " age is ", age, " Eligible for Vote.")
else:
    print(name, " age is ", age, " Not Eligible for Vote.")

# output

# Enter Your Name : Ram
# Enter Your Age : 23
# Ram  age is  23  Eligible for Vote.