# --------------------------------
# File Handling in Python
# --------------------------------

# Writing to a file
file = open("example.txt", "w")  # 'w' = write mode
file.write("Hello, this is a test file.\n")
file.write("Second line of text.")
file.close()  # Always close the file

# Reading from a file
file = open("example.txt", "r")  # 'r' = read mode
content = file.read()            # read entire content
print("File content:\n", content)
file.close()

# Appending to a file
file = open("example.txt", "a")  # 'a' = append mode
file.write("\nThis line is added later.")
file.close()

# Reading again after appending
file = open("example.txt", "r")
print("\nAfter appending:\n", file.read())
file.close()
