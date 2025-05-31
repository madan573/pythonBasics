# -------------------------------
# Example: Python Tuple
# -------------------------------

# A tuple is like a list, but it cannot be changed after creation.
# Tuples are ordered and allow duplicates.

colors = ("red", "green", "blue", "green")  # tuple with duplicate

print("Tuple of colors:", colors)
print("Second color:", colors[1])           # access by index

# colors[1] = "yellow"   # This will give an error because tuples are immutable
