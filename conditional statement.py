# -------------------------------
# Conditional Statements in Python
# -------------------------------

# Conditional statements are used to make decisions in a program.
# Python uses if, elif, and else keywords.

# Syntax:
# if condition:
#     # code block
# elif another_condition:
#     # another block
# else:
#     # final block

# -------------------------------
# Example 1: Check if number is positive, negative, or zero
# -------------------------------

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")