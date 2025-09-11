# In Python, a string is a sequence of characters enclosed in quotes. It can include letters, numbers, symbols or spaces. 
# Since Python has no separate character type, even a single character is treated as a string of length. Strings are widely used 
# for text handling and manipulation.

# Creating a String

s1 = 'NgR'  # single quote
s2 = "NGR"  # double quote
print(s1)
print(s2)

# Multi-line Strings

s = """I am Learning
Python String on Newgen-robotics"""
print(s)

s = '''I'm a 
Newgen robot'''
print(s)


# Accessing characters in String

s = "NewGen-Robotics"
print(s[0])   # first character
print(s[4])   # 5th character


# String Slicing

s = "Newgen-Robotics"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string

# String Iteration

s = "Python"
for char in s:
    print(char)

# String Immutability

# Strings are immutable means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods 
# like concatenation, slicing or formatting to create new strings based on original.

s = "Newgen-Robotics"
s = "G" + s[1:]   # create new string
print(s)

# Deleting a String

s = "GfG"
del s

# Updating a String

s = "hello gens"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("Newgens", "Newgen Robotics")  # replace word
print(s1)
print(s2)


# Common String Methods


#  len(): The len() function returns the total number of characters in a string (including spaces and punctuation).
s = "Newgen-Robotics"
print(len(s))

# upper() and lower(): upper() method converts all characters to uppercase whereas, lower() method converts all characters to lowercase.
s = "Hello World"
print(s.upper())
print(s.lower())

#  strip() and replace(): strip() removes leading and trailing whitespace from the string and replace() replaces all occurrences of a specified substring with another.
s = "   Gfg   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))


# Concatenating and Repeating Strings

# Strings can be combined by using + operator.

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

# We can repeat a string multiple times using * operator.

s = "Hello "
print(s * 3)

# Formatting Strings

# Using f-strings
# The simplest and most preferred way to format strings is by using f-strings.
# Example: Embed variables directly using {} placeholders.


# Using format()

s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)


# String Membership Testing

s = "Newgen-Robotics"
print("Geeks" in s)
print("GfG" in s)

