# List comprehension is a concise and powerful way to create new lists by applying an expression to each item in an existing iterable 
# (like a list, tuple or range). It helps you write clean, readable and efficient code compared to traditional loops.

a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)

# Why Use List Comprehension?
# Cleaner code: Combines looping, filtering and transformation in one line.
# More readable: Avoids verbose loops and temporary variables.
# Faster execution: Often faster than equivalent for-loops.

# For Loop vs. List Comprehension
# A for loop takes multiple lines to build a new list by iterating and appending each item manually. List comprehension does same in just one line, making code shorter 
# and easier to read.

a = [1, 2, 3, 4, 5]
res = []
for val in a:
    res.append(val * 2)
print(res)



a = [1, 2, 3, 4, 5]
res = [val * 2 for val in a]
print(res)

# Conditional Statements in List Comprehension
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)


# Creating a list from a range

a = [i for i in range(10)]
print(a)

# Using nested loops

c = [(x, y) for x in range(3) for y in range(3)]
print(c)

# Flattening a list of lists

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)

