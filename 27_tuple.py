
# Tuple in Python
# Immutable (not changable)
# Surrounded by Round Brackets (1,1,5)

a = (1, 2.5, True, "Ram")
print(a)
print(type(a))

# output

# (1, 2.5, True, 'Ram')
# <class 'tuple'>

print(a[1])
print(a[-1])
print(a[0:2])

# output

# 2.5
# Ram
# (1, 2.5)

b = list(a)
print(b)

# output

# [1, 2.5, True, 'Ram']

b.append("Raja")
print(b)
print(type(b))

# output

# [1, 2.5, True, 'Ram', 'Raja']
# <class 'list'>

a = tuple(b)
print(a)
print(type(a))

# output

# (1, 2.5, True, 'Ram', 'Raja')
# <class 'tuple'>

for i in a:
    print(i)

# output

# 1
# 2.5
# True
# Ram
# Raja

if "Raj" in a:
    print("Raja is Found")
else:
    print("Not Found")
print(len(a))

# output

# 5
# Not Found

a = (1,)
print(type(a))

# output

# <class 'tuple'>

del a
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = a + b
print(c)
print(c.count(7))

# output

# (1, 2, 7, 4, 5, 6, 7, 8)
# 2

a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = (a, b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])

# output

# ((1, 2, 7, 4), (5, 6, 7, 8))
# (1, 2, 7, 4)
# (5, 6, 7, 8)
# 2

x = ('Joes',) * 10
print(x)

# output

# ('Joes', 'Joes', 'Joes', 'Joes', 'Joes', 'Joes', 'Joes', 'Joes', 'Joes', 'Joes')

a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
print(min(a))
print(max(a))

# output

# 1
# 7










