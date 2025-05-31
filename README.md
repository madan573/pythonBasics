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
name = "Alice"
age = 25
height = 5.6
is_student = True
```

## 5. User Input and Type Casting
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
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
for i in range(5):
    print(i)
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
def greet(name):
    print("Hello, " + name)

greet("Alice")
```

## 10. Lists, Tuples, and Sets
```python
# List
fruits = ["apple", "banana", "cherry"]

# Tuple
colors = ("red", "green", "blue")

# Set
unique_numbers = {1, 2, 3, 2}
```

## 11. Dictionaries
```python
person = {
    "name": "Alice",
    "age": 25
}
print(person["name"])
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
