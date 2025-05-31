# -------------------------------
# User Input and Type Casting in Python
# -------------------------------

# input() function is used to take input from the user.
# By default, input() returns data as a string type.

# To use the input as a number (e.g., for math), we must convert it using type casting:
# int() for integer, float() for decimal number, etc.

# -------------------------------
# Example: Take user input and convert (cast) it
# -------------------------------

# Taking name as input (no need to cast because string is okay)
name = input("Enter your name: ")

# Taking age as input and casting it to integer
age = int(input("Enter your age: "))

# Taking height as input and casting it to float
height = float(input("Enter your height in feet: "))

# Boolean input example (simple way - check if input is 'yes')
is_student_input = input("Are you a student? (yes/no): ")
is_student = is_student_input.lower() == "yes"

# -------------------------------
# Displaying the results
# -------------------------------
print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Height:", height, "feet")
print("Student:", is_student)
