# Python Basics

**Python** is a high-level, interpreted programming language known for its simple and readable syntax. It was created by **Guido van Rossum** and first released in **1991**. Python is general-purpose, meaning it can be used for a wide range of applications like web development, data analysis, artificial intelligence, automation, scientific computing, and more.

### Why Python is so popular:

1. **Easy to Learn and Use**: Its syntax is clear and close to human language, making it beginner-friendly.
2. **Versatile**: Works well for everything from simple scripts to complex machine learning systems.
3. **Large Community and Support**: A strong, active community means lots of tutorials, libraries, and help available.
4. **Extensive Libraries**: Python has powerful libraries like NumPy, Pandas, Django, Flask, TensorFlow, etc., which speed up development.
5. **Cross-platform**: It runs on Windows, macOS, and Linux without major changes in the code.
6. **Open Source**: Free to use and modify, which encourages innovation and collaboration.

# Python Tutorial for Beginners

Welcome to this Python tutorial designed for complete beginners. This guide covers Python basics from scratch up to file handling.

---

## Table of Contents
1. [Introduction to Python](#1-introduction-to-python)
2. [Installing Python](#2-installing-python)
3. [Hello World Program](#3-hello-world-program)
4. [Variables and Data Types](#4-variables-and-data-types)
5. [User Input and Type Casting](#5-user-input-and-type-casting)
6. [Operators](#6-operators)
7. [Conditional Statements](#7-conditional-statements)
8. [Loops](#8-loops)
9. [Functions](#9-functions)
10. [Lists, Tuples, and Sets](#10-lists-tuples-and-sets)
11. [Dictionaries](#11-dictionaries)
12. [String Handling](#12-string-handling)
13. [Exception Handling](#13-exception-handling)
14. [File Handling](#14-file-handling)

---

## 1. Introduction to Python
Python is a high-level, interpreted programming language with simple and readable syntax. It is widely used in web development, data analysis, AI, scripting, and more.

## 2. Installing Python
- Download from [python.org](https://www.python.org/)
- Verify installation:
  ```bash
  python --version
  ```

## 3. Hello World Program
```python
print("Hello, World!")
```

## 4. Variables and Data Types
```python
name = "Madan"
age = 36
height = 5.7
is_student = True
fruits = ["apple", "banana", "mango"]
coordinates = (10.5, 20.8)
student = {
    "name": "Madan",
    "age": 36,
    "class": 10,
    "passed": True
}
unique_numbers = {1, 2, 3, 4}

```

## 5. User Input and Type Casting
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
```

## 6. Operators
- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `and`, `or`, `not`

## 7. Conditional Statements
```python
if age >= 18:
    print("Adult")
elif age > 12:
    print("Teenager")
else:
    print("Child")
```

## 8. Loops
**For Loop:**
```python
for i in range(1, 6):
    print(i)  

```
```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```
```python
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
```
```python
# Example: else runs after loop finishes normally
for i in range(3):
    print("Looping:", i)
    # to test and understand properly use break
else:
    print("Loop finished successfully.")
```
**While Loop:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## 9. Functions
```python
# A function is defined using the 'def' keyword.
# This function takes two numbers as input (parameters)
# and returns their sum.
def add_numbers(a, b):
    result = a + b
    # return the result to the caller
    return result  
  
# Calling (using) the function with arguments 5 and 3
sum_result = add_numbers(5, 3)
# Print the returned value
print("The sum is:", sum_result)
```
```python
# -------------------------------
# Palindrome Checker using Function
# -------------------------------

# A palindrome is a word that reads the same forwards and backwards.
# Example: "madam", "racecar", "level"

# Define a function to check for palindrome
def is_palindrome(word):
    # Convert to lowercase to make the check case-insensitive
    word = word.lower()

    # Reverse the word using slicing [::-1]
    reversed_word = word[::-1]

    # Compare original and reversed
    if word == reversed_word:
        return True
    else:
        return False

# Take user input
user_input = input("Enter a word to check if it's a palindrome: ")

# Call the function and display result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")

```
## 10. Lists, Tuples, and Sets
```python
# List
# -------------------------------
# Example: Python List
# -------------------------------

# A list is used to store multiple items in a single variable.
# Lists are ordered (indexed), mutable (can be changed), and allow duplicate values.

fruits = ["apple", "banana", "mango", "banana"]  # list with duplicate item

print("List of fruits:", fruits)           # print the entire list
print("First fruit:", fruits[0])           # access by index
fruits[1] = "orange"                       # update item at index 1
print("Updated list:", fruits)
```

```python

# Tuple
# -------------------------------
# Example: Python Tuple
# -------------------------------

# A tuple is like a list, but it cannot be changed after creation.
# Tuples are ordered and allow duplicates.

colors = ("red", "green", "blue", "green")  # tuple with duplicate

print("Tuple of colors:", colors)
print("Second color:", colors[1])           # access by index

# colors[1] = "yellow"   # This will give an error because tuples are immutable
```

```python

# Set
# -------------------------------
# Example: Python Set
# -------------------------------

# A set is used to store unique values (no duplicates).
# Sets are unordered, unindexed, and mutable (but elements cannot be accessed by index).

numbers = {1, 2, 3, 2, 4}

print("Set of numbers:", numbers)  # Duplicate '2' is automatically removed

numbers.add(5)                     # Add new element
print("Updated set:", numbers)

# print(numbers[0])  # This will give an error because sets are unindexed

```

## 11. Dictionaries
```python
# -------------------------------
# Dictionary in Python - Example
# -------------------------------

# A dictionary to store information about a student
student = {
    "name": "Aaradhya",     # 'name' is the key, "Aaradhya" is the value
    "age": 7,
    "grade": "Class 1",
    "passed": True
}

# Print the entire dictionary
print("Student info:", student)

# Accessing individual elements using keys
print("Name:", student["name"])       # Access value of key 'name'
print("Age:", student["age"])

# Adding a new key-value pair
student["school"] = "Sunrise Public School"

# Updating an existing value
student["age"] = 8  # changed from 7 to 8

# Removing a key-value pair
del student["passed"]

# Print the updated dictionary
print("Updated student info:", student)

# Loop through dictionary keys
print("All keys:")
for key in student:
    print(key)

# Loop through dictionary values
print("All values:")
for value in student.values():
    print(value)

# Loop through both keys and values
print("All key-value pairs:")
for key, value in student.items():
    print(key, ":", value)

```

## 12. String Handling
```python
message = "Hello, World!"
print(message.upper())
print(message.lower())
print(message[0:5])
```

## 13. Exception Handling
```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
```

## 14. File Handling
**Write to a file:**
```python
with open("demo.txt", "w") as file:
    file.write("Hello File")
```

**Read from a file:**
```python
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)
```

---

> This is a beginner-friendly tutorial. Practice each section by writing code and modifying it to learn better!
