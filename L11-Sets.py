# Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain
# duplicates. The order of elements in a set is not preserved and can change.


# Creating a Set in Python

set1 = {1, 2, 3, 4}
print(set1)


# Using the set() function

set1 = set()
print(set1)

set1 = set("Newgen-Robotics")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Gens", "For", "Robotics"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Gens", "for", "Robotics")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Gens": 1, "for": 2, "robot": 3}
print(set(d))

# Unordered, Unindexed and Mutability

set1 = {3, 1, 4, 1, 5, 9, 2}

print(set1)  # Output may vary: {1, 2, 3, 4, 5, 9}

# Unindexed: Accessing elements by index is not possible
# This will raise a TypeError
try:
    print(set1[0])
except TypeError as e:
    print(e)

# Adding Elements to a Set in Python

# Creating a set
set1 = {1, 2, 3}

# Add one item
set1.add(4)

# Add multiple items
set1.update([5, 6])

print(set1)

# Accessing a Set in Python

set1 = set(["Gens", "For", "Robots"])

# Accessing element using For loop
for i in set1:
    print(i, end=" ")

# Checking the element# using in keyword
print("Gens" in set1)

# Removing Elements from the Set in Python

# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)


# Using pop() Method

set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)

# Using pop on an empty set
set1.clear()  # Clear the set to make it empty
try:
    set1.pop()
except KeyError as e:
    print("Error:", e)

# Using clear() Method

set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)

# Frozen Sets in Python

# A frozenset in Python is a built-in data type that is similar to a set but with one key difference that is immutability. This means that once a frozenset is created, 
# we cannot modify its elements that is we cannot add, remove or change any items in it. Like regular sets, a frozenset cannot contain duplicate elements.
# If no parameters are passed, it returns an empty frozenset.  


# Creating a frozenset from a list
fset = frozenset([1, 2, 3, 4, 5])
print(fset)  

# Creating a frozenset from a set
set1 = {3, 1, 4, 1, 5}
fset = frozenset(set1)
print(fset)

# Typecasting Objects into Sets


# Typecasting list into set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
set1 = set(li)
print(set1)

# Typecasting string into set
s = "NewGenRobotics"
set1 = set(s)
print(set1)

# Typecasting dictionary into set
d = {1: "One", 2: "Two", 3: "Three"}
set1 = set(d)
print(set1)

