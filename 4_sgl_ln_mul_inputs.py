# Single line multiple inputs 

# 1.below code split names by space 
name1,name2,name3=input("Enter 3 names : ").split()

print("Name 1 is: ",name1)
print("Name 2 is: ",name2)
print("Name 3 is: ",name3)

# output
# Enter 3 names : ram sam kumar
# Name 1 is:  ram
# Name 2 is:  sam
# Name 3 is:  kumar

# 1.below code split names by (,) 
name4,name5,name6=input("Enter 3 names : ").split(",")

print("Name 4 is: ",name4)
print("Name 5 is: ",name5)
print("Name 6 is: ",name6)

# output

# Enter 3 names : Ram Kumar,Sam,Pradeep
# Name 4 is:  Ram Kumar
# Name 5 is:  Sam
# Name 6 is:  Pradeep