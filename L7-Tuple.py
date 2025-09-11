# A tuple in Python is an immutable ordered collection of elements.

# Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
# Tuples can hold elements of different data types.
# The main characteristics of tuples are being ordered , heterogeneous and immutable.


# Creating a Tuple

tup = ()
print(tup)

# Using String
tup = ('Gens', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Gens')
print(tup)


# Creating a Tuple with Mixed Datatypes.

tup = (5, 'Welcome', 7, 'Gens')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'gen')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Gens',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Gens')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)



# Python Tuple Basic Operations

# Accessing of Python Tuples

# Accessing Tuple with Indexing
tup = tuple("Gens")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Gens", "For", "robot")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

# Concatenation of Tuples

tup1 = (0, 1, 2, 3)
tup2 = ("Gens", "For", "robot")

tup3 = tup1 + tup2
print(tup3)

# Slicing of Tuple

tup = tuple('NEWGENROBOTICS')

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])


# Deleting a Tuple

tup = (0, 1, 2, 3, 4)
del tup

print(tup)

# Tuple Unpacking with Asterisk (*)
# In Python, the " * " operator can be used in tuple unpacking to grab multiple items into a list. 
# This is useful when you want to extract just a few specific elements and collect the rest together.


tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a) 
print(b) 
print(c)



