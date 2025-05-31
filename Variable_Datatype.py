# -------------------------------
# Variables and Data Types in Python
# -------------------------------

# A variable is a container for storing data values.
# You don't need to declare the type of variable explicitly in Python.

# Python is dynamically typed, so the type is inferred at runtime.

# Common data types:
# 1. int – Integer (whole numbers)
# 2. float – Decimal numbers
# 3. str – String (text)
# 4. bool – Boolean (True or False)
# 5. list – Ordered collection of items
# 6. tuple – Ordered and immutable collection
# 7. dict – Key-value pairs (dictionary)
# 8. set – Unordered collection of unique items

# -------------------------------
# Examples of variables and their types
# -------------------------------

# Integer
age = 35

# Float
height = 5.9

# String
name = "Madan"

# Boolean
is_student = True

# List – can store multiple values
fruits = ["apple", "banana", "mango"]

# Tuple – similar to list but immutable
coordinates = (10.5, 20.8)

# Dictionary – stores data in key:value pairs
student = {
    "name": "Madan",
    "age": 36,
    "class": 10,
    "passed": True
}

# Set – unordered and unique items
unique_numbers = {1, 2, 3, 4}

# -------------------------------
# You can check the type using the type() function
# -------------------------------
print(type(age))         
print(type(height))      
print(type(name))       
print(type(is_student))  

# To print values you can simply use print function without using type() function.

print("\n", age)
print(height)
print(name)
print(is_student)
print(fruits)
print(coordinates)
print(student)
print(unique_numbers)

# To print all dictionary elements
print("\n",student)
# To print value of single dictionary element
print(student["class"])