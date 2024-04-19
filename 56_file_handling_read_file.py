
# file handling (read file)

try:
    # you must give file location
    file = open("open_file.txt","r")
    print(file.read())

except FileNotFoundError:
    print("Error is: File Not Found")
else:
    file.close()

# output

# This file is used for file handling in python

# This file will read when you use read command
    
#<------------------------------------------------------> 

 # Note: below are the commands which are used in file handling
    
 #f=open("data.txt",'a')
 #f=open("data.txt",'r')
 #print(f.read())
 #print(f.readline())

