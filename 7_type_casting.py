
# type casting 

# type conversion constructors are 
# 1. int()
# 2. float()
# 3. str()

a=10.0

print(a)
print(type(a))

#you can casting the type by asigning the new variable and change the type of that old variable
b=int(a)

print(b)
print(type(b))

# output

# 10.0
# <class 'float'>
# 10
# <class 'int'>


# <------------------------------------------------------->

c=int(input("Enter the value C : "))
d=int(input("Enter the value D : "))

e=c+d
print("Total : ",e)

# you can also give like 

print("Total is : "+ str(e))

# output 

# Enter the value C : 25
# Enter the value D : 28
# Total :  53
# Total is : 53

# <------------------------------------------------------->