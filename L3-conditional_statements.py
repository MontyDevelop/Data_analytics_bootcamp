# Conditional statements in Python are used to execute certain blocks of code based on specific conditions. These statements help control the flow 
# of a program, making it behave differently in different situations.


# if

# If statement is the simplest form of a conditional statement. It executes a block of code if the given condition is true.

age = 20
if age >= 18:
    print("Eligible to vote.")

# Short Hand if

age = 19
if age > 18: print("Eligible to Vote.")


# if else

age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

# Short Hand if-else

marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")

# elif Statement

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


# Nested if..else

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")



# Ternary Conditional Statement
# A ternary conditional statement is a compact way to write an if-else condition in a single line. It’s sometimes called a "conditional expression."

# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)



# Match-Case Statement

# match-case statement is Python's version of a switch-case found in other languages. It allows us to match a variable's value against a set of patterns.

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")