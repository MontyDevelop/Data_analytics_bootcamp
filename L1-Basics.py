# What is computer language?
# What is programming?
# What is python?

# Basic commands in python programming

# Python is one of the most popular programming languages. It’s simple to use, packed with features and supported by a wide range of libraries and frameworks. Its clean syntax makes it beginner-friendly.
    # A high-level language, used in web development, data science, automation, AI and more.
    # Known for its readability, which means code is easier to write, understand and maintain.
    # Backed by library support, so we don’t have to build everything from scratch, there’s probably a library that already does what we need.


# Why to Learn Python?
    # Requires fewer lines of code compared to other programming languages like Java.
    # Provides Libraries / Frameworks like Django, Flask and many more for Web Development, and Pandas, Tensorflow, Scikit-learn and many more for, AI/ML, Data Science and Data Analysis
    # Cross-platform, works on Windows, Mac and Linux without major changes.
    # Used by top tech companies like Google, Netflix and NASA.
    # Many Python coding job opportunities in Software Development, Data Science and AI/ML.


print("Hello world")
print(1+2)

# Understanding input and output operations is fundamental to Python programming. With the print() function, we can display output in various formats, 
# while the input() function enables interaction with users by gathering input during program execution.



# Python's input() function is used to take user input. By default, it returns the user input in form of a string. 

# name = input("Enter your name: ")
# print("Hello,", name, "! Welcome!")


# Printing Output using print() in Python
# At its core, printing output in Python is straightforward, thanks to the print() function. This function allows us to display text, 
# variables and expressions on the console. Let's begin with the basic usage of the print() function:

# In this example, "Hello, World!" is a string literal enclosed within double quotes. When executed, this statement will output the text
# to the console.


# Printing Variables
# We can use the print() function to print single and multiple variables. We can print multiple variables by 
# separating them with commas.

# Single variable
s = "Bob"
print(s)

# Multiple Variables
s = "Alice"
age = 25
city = "New York"
print(s, age, city)

# Take Multiple Input in Python

# We are taking multiple input from the user in a single line, splitting the values entered by the user into separate variables for each value 
# using the split() method. Then, it prints the values with corresponding labels, either two or three, based on the number of inputs provided by 
# the user.

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)