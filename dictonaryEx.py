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
