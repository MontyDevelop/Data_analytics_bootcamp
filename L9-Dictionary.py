# Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can 
# be duplicated, whereas keys can't be repeated and must be immutable.

d = {1: 'Gens', 2: 'For', 3: 'robot'}
print(d)

# How to Create a Dictionary

d1 = {1: 'Gens', 2: 'For', 3: 'Robots'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "Gens", b = "for", c = "Robotics")
print(d2)

# Accessing Dictionary Items

d = { "name": "Monty", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))


# Adding and Updating Dictionary Items

d = {1: 'Gens', 2: 'For', 3: 'robotics'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)

# Removing Dictionary Items

d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)

# Iterating Through a Dictionary

d = {1: 'Gens', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")


# Nested Dictionaries

d = {1: 'Gens', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Robotics'}}
print(d)