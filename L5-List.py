# In Python, a list is a built-in data structure that can hold an ordered collection of items. Unlike arrays in some languages, 
# Python lists are very flexible:

# Can contain duplicate items
# Mutable: items can be modified, replaced, or removed
# Ordered: elements maintain the order in which they were added
# Index-based: items are accessed using their position (starting from 0)
# Can store mixed data types (integers, strings, booleans, even other lists)


# Creating a List

a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)


# Using list() Constructor

a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("NGR")
print(b)

# Creating List with Repeated Elements

a = [2] * 5
b = [0] * 7

print(a)
print(b)

# Accessing List Elements

a = [10, 20, 30, 40, 50]
print(a[0])    
print(a[-1])
print(a[1:4])   # elements from index 1 to 3

# Adding Elements into List

a = []

a.append(10)  
print("After append(10):", a)  

a.insert(0, 5)
print("After insert(0, 5):", a) 

a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 

a.clear()
print("After clear():", a)

# Updating Elements into List


a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)

# Removing Elements from List

a = [10, 20, 30, 40, 50]

a.remove(30)  
print("After remove(30):", a)

popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

del a[0]  
print("After del a[0]:", a)

# Iterating Over Lists

a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)

# Nested Lists

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])

# List Comprehension

squares = [x**2 for x in range(1, 6)]
print(squares)

