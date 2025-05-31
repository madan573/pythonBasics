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
    #output without using f string
    print(user_input,"is a palindrome!")
else:
    #output using f string
    print(f"'{user_input}' is not a palindrome.")