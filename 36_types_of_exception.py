
# types of Exception

# there are 158 types of exceptions in python we will see mostly used 5 exceptions here

try:
    print(a)
except NameError as e:
    print("A is not Defined")
 
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("denominator cant be zero")
 
try:
    a = int("Joes")
except ValueError as e:
    print("Please Enter Numbers only")
 
try:
    a = [10, 20, 30, 40]
    print(a[10])
except IndexError as e:
    print("Invalid Index")
 
try:
    f = open("tesot.txt")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())


# output

# A is not Defined
# denominator cant be zero
# Please Enter Numbers only
# Invalid Index
# File Not Found