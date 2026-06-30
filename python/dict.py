# What is a Dictionary?

# A dictionary is an unordered collection of items. Each item is stored as a key-value pair.
# एक शब्दकोश मदों का एक अव्यवस्थित संग्रह है। प्रत्येक मद को कुंजी-मान युग्म के रूप में संग्रहित किया जाता है।

#     Unordered : Historically, dictionaries were unordered. From Python 3.7 onwards, dictionaries maintain insertion order.
#     Mutable: You can add, remove, and modify key-value pairs after the dictionary has been created.
#     Values can be anything: Values can be of any data type and can be duplicates.
#     Mapping: Dictionaries are often referred to as "mappings" because they map keys to values.
#     We use the : operator to separate the key and value




# empty dictionary (खाली शब्दकोश)
# a = {} # dict()
# print(a)

#example like this..
# a = { "name": "Anil", "age": 30, "city": "japan" }
# a = {
#     "name": "Anil",
#     "age": 30,
#     "city": "japan"
# }
# print(a)


#example like this..
# a= {
#     "name": "Bob",
#     1: "one",
#     3.14: "pi",
#     (1, 2): "tuple key"
# }
# print(a)

#example like this..
# a = dict(
#     name="Charlie",
#     id=101,
#     grade="A"
# )
# print(a)


#get method use...
# print( a.get("name") )


# delete mathod use... 
# a = [ 1, 2, 3]
# del a[-1]
# print(a)

# Pop method use...
# a= a.pop("name")
# print(a)

# clear method use....
# a.clear()
# print(a)

# example like this...
# a = {
#     "name": "Bob",
#     "age": 25,
#     "gender": "Male"
# }

# Length
# print(len( a ))
# Membership (checks for key)
# print('name' in profile)
# print('Bob' in profile)


# Dictionary Methods

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# # d1.update(d2)
# # print(d1)

# d2.update(d1)
# print(d2)

# a = {"name": "Anil"}
# email = ("email", "unknown@example.com")
# print(a, email)
# a= list(range(1, 51))

# counter = 0
# while counter < len(a):
#     a[counter] = "key" + str(a[counter])
#     counter += 1

# print(a)
# b = (["key1", "key2", "key3"], 0)
# print(b)

# b = (data, 50)
# print(b)


#zip method use....
# name = ["Alice", "Bob", "Charlie", "Vipin"]
# ages = [30, 24, 35]
# cities = ["NY", "LA"]
# data = zip( names, ages, cities )
# print(data)

# for x in data:
#     print(x)

# for x, y in zip(a, b):
#     c[x] = y
# print(c)

# for name, age, city in zip(names, ages, cities):
#     print(f"{name} is {age} years old and lives in {city}.")



# Nested for Loops
# You can place a for loop inside another for loop. The inner loop will complete all its iterations for each single iteration of the outer loop. This is commonly used for working with 2D data structures (like matrices) or generating combinations.
    
# a = {
#     "number": [ 1, 2, 3, 4, 5, 6, 7, 8 ],
#     "float": [ 1.1, 2.2, 3.3, 4.4, 5.0, 6.0, 7.0, 8.0],
#     "string": "this is a string"
# }


# for x in a:
#     print(x) # "float"
#     for y in a.get(x):
#         print(y)

# *
# **
# ***
# ****
# *****

# for x in range(1, 6):
#     print( "*" * x )


# sticks = 21

# print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
# print("Whoever will take the last stick will lose")

# while True:
#     print("Sticks left: " , sticks)
#     sticks_taken = int(input("Take sticks(1-4):"))
#     if sticks == 1:
#         print("You took the last stick, you lose")
#         break
#     if sticks_taken >= 5 or sticks_taken <= 0:
#         print("Wrong choice")
#         continue
#     print("Computer took: " , (5 - sticks_taken) , "\n")
#     sticks -= 5
