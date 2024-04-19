
# dictionary in Python

# They are Immutable
# A set doesn’t allow duplicate elements
# The key cannot be changed

user = {
    "name": "Ram",
    "age": 25,
    "isMarried": True
}
print(user)
print(type(user))
print(user["name"])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())

# output

# {'name': 'Ram', 'age': 25, 'isMarried': True}
# <class 'dict'>
# Ram
# 25
# dict_keys(['name', 'age', 'isMarried'])
# dict_values(['Ram', 25, True])
# dict_items([('name', 'Ram'), ('age', 25), ('isMarried', True)])

for x in user:
    print(x," ",user[x])
for x in user.values():
    print(x)
for x in user.keys():
    print(x)
for x,y in user.items():
    print(x,y)
if "gender" in user:
    print("Present")

# output 

# name   Ram
# age   25
# isMarried   True
# Ram
# 25
# True
# name
# age
# isMarried
# name Ram
# age 25
# isMarried True


# Changing Values

user.update({"gender":"male"})
print(user)
user["age"]=35
print(user)
user.pop("age")
print(user)
user.clear()
print(user)
users={
    "user1": {
        "name": "Ram",
        "age": 25,
        "isMarried": True
    },
"user2": {
        "name": "SAm",
        "age": 35,
        "isMarried": False
    }
}
print(users)
# for user in users:
#     print(user["name"])

# output

# {'name': 'Ram', 'age': 25, 'isMarried': True, 'gender': 'male'}
# {'name': 'Ram', 'age': 35, 'isMarried': True, 'gender': 'male'}
# {'name': 'Ram', 'isMarried': True, 'gender': 'male'}
# {}
# {'user1': {'name': 'Ram', 'age': 25, 'isMarried': True}, 'user2': {'name': 'SAm', 'age': 35, 'isMarried': False}
# }