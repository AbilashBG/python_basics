
# List in Python
"""
Sequence Type
Mutable (We can change any index of values)
a[5]
a={1,2,3,4,5}
a[0]
"""
a = [1, 2, 3, 4, 5]
print(a)
print(type(a))
a[0] = 100
print(a)
print("Slicing")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])
print("-----------------------------")

# output

# [1, 2, 3, 4, 5]
# <class 'list'>
# [100, 2, 3, 4, 5]
# Slicing
# 2
# 5
# [100, 2, 3]
# [3, 4, 5]
# [100, 2, 3]
# -----------------------------

a = [1, True, 'Ram', 2.5, [1, 2, 3, 4]]
print(a)
print(type(a))
print(a[0], " type is ", type(a[0]))
print(a[1], " type is ", type(a[1]))
print(a[2], " type is ", type(a[2]))
print(a[3], " type is ", type(a[3]))
print(a[4], " type is ", type(a[4]))
print(a[4][1])
print("-----------------------------")

# output

# [1, True, 'Ram', 2.5, [1, 2, 3, 4]]
# <class 'list'>
# 1  type is  <class 'int'>
# True  type is  <class 'bool'>
# Ram  type is  <class 'str'>
# 2.5  type is  <class 'float'>
# [1, 2, 3, 4]  type is  <class 'list'>
# 2
# -----------------------------

a = [10, 25, 35, 45]
print(a)
a.clear()
print(a)
a = [10, 25, 35, 45]
b = a.copy()
print(b)
a = [10, 25, 35, 45, 25, 4, 25]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(0)  # remove Element using index
print(a)
a = [10, 25, 35, 45, 25, 4, 25]
a.remove(25)  # Values (first value)
print(a)
print("-----------------------------")

# output

# [10, 25, 35, 45]
# []
# [10, 25, 35, 45]
# 3
# 1
# 7
# 45
# 4
# [10, 25, 35, 45, 25, 4, 25]
# [25, 35, 45, 25, 4, 25]
# [10, 35, 45, 25, 4, 25]
# -----------------------------

names = ["Ram"]
print(names)
names.append("Sam")
names.append("Ravi")
names.append("Kumar")
print(names)
name2 = ["Sara", "Anitha"]
names.extend(name2)
print(names)
names.insert(0,"Suriya")
print(names)
print("-----------------------------")

# output

# ['Ram']
# ['Ram', 'Sam', 'Ravi', 'Kumar']
# ['Ram', 'Sam', 'Ravi', 'Kumar', 'Sara', 'Anitha']
# ['Suriya', 'Ram', 'Sam', 'Ravi', 'Kumar', 'Sara', 'Anitha']
# -----------------------------

print(list(range(5)))
print(list("Tutorjoes"))
a=[10,50,100,25,85]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["Orange","Apple","Zebra"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["Orange","Apple","Zebra"]
a.sort(key=len)
print(a)
print("-----------------------------")

# output

# [0, 1, 2, 3, 4]
# ['T', 'u', 't', 'o', 'r', 'j', 'o', 'e', 's']
# [10, 50, 100, 25, 85]
# [10, 25, 50, 85, 100]
# [100, 85, 50, 25, 10]
# ['Apple', 'Orange', 'Zebra']
# ['Zebra', 'Orange', 'Apple']
# ['Apple', 'Zebra', 'Orange']
# -----------------------------