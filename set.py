# -------------------------------
# Example: Python Set
# -------------------------------

# A set is used to store unique values (no duplicates).
# Sets are unordered, unindexed, and mutable (but elements cannot be accessed by index).

numbers = {1, 2, 3, 2, 4}

print("Set of numbers:", numbers)  # Duplicate '2' is automatically removed

numbers.add(5)                     # Add new element
print("Updated set:", numbers)
# This will give an error because sets are unindexed
#print(numbers[0])