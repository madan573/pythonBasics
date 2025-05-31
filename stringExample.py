# ------------------------------------
# String Handling in Python
# ------------------------------------

# Creating strings
name = "Aaradhya Pandey"
greeting = 'Hello'
multiline_text = """This is
a multiline
string."""

# Printing strings
print("Name:", name)
print("Greeting:", greeting)
print("Multiline Text:\n", multiline_text)

# String Concatenation (joining strings)
full_greeting = greeting + ", " + name + "!"
print("Full Greeting:", full_greeting)

# Accessing characters using index (starts at 0)
print("First letter of name:", name[0])
print("Last letter of name:", name[-1])  # -1 means last character

# String Slicing (get part of the string)
print("First 4 letters:", name[0:4])     # from index 0 to 3
print("From 5th letter to end:", name[4:])

# String Methods
print("Uppercase:", name.upper())        # convert to uppercase
print("Lowercase:", name.lower())        # convert to lowercase
print("Length of name:", len(name))      # count characters
print("Does name contain 'Pandey'?", "Pandey" in name)  # check substring

# Replace a word
new_name = name.replace("Pandey", "Kumar")
print("Updated Name:", new_name)

# Remove spaces from both ends
message = "   Hello Python!   "
print("Trimmed message:", message.strip())

# Split string into list
words = name.split(" ")
print("Words in name:", words)
