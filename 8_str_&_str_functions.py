
# Syring and String Functions

# upper, lower, capitalize, title, count, endswith, find, replace,
# isupper, islower, isalnum, isalpha,splitlines,split,len,strip,partition, ......etc

s="Basic String Functions"

print(s)

# <---------------Variable Type-------------->
print(type(s))
# output
# <class 'str'>

# <---------------Upper Case----------------->

print(s.upper())

# output
# BASIC STRING FUNCTIONS

# <---------------Lower Case----------------->

print(s.lower())

# output
# basic string functions

# <---------------Capitalize----------------->

print(s.capitalize())

# output (capital only first letter)
# Basic string functions

# <---------------Title----------------->

print(s.title())

# output (capital each word first letter)
# Basic String Functions

# <---------------Count----------------->

print(s.count("s"))

# output (count the given letter)
# 2

# <---------------Ends with----------------->

print(s.endswith("ns"))

# output (confirm the last letters)
# True

# <---------------Find----------------->

print(s.find("t"))

# output (find particular letter first position)
# 7

print(s.find("t",8))

# output (find particular letter particular (after 8)position)
# 17

# <---------------Replace----------------->

print(s.replace("u","8"))

# output (replace the particular letter)
# Basic String F8nctions

# <---------------isupper----------------->

a="Basic"

print(a.isupper())

# output (find the given string is in uppercase)
# False

# <---------------islower----------------->

a="basic"

print(a.islower())

# output (find the given string is in lowercase)
# True

# <---------------isalnum----------------->

a="basic"

print(a.isalnum())

# output (find the given string contains alphabetics or numbers)
# True

# <---------------isalpha----------------->

a="basic81079"

print(a.isalpha())

# output (find the given string contains alphabetics only)
# False

# <---------------isalpha----------------->

a="he\nis a\ngood boy"

print(a)
print(a.splitlines())
print(a.splitlines(True))

# output 
# he
# is a
# good boy

# ['he', 'is a', 'good boy']

# ['he\n', 'is a\n', 'good boy']

# <---------------length----------------->

a="basic81079"

print(a.__len__())

# output
# 10

# <---------------strip----------------->

a="    basic81079    "

print(len(a.strip()))

# output(remove unwanted space)
# 10

print(len(a.lstrip()))

# output(remove unwanted left side space)
# 14

print(len(a.rstrip()))

# output(remove unwanted right side space)
# 14

# <---------------partition----------------->

a="20-01-2024"

print(a.partition("-"))

# output
# ('20', '-', '01-2024')
