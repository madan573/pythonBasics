# -------------------------------
# Exception Handling in Python
# -------------------------------

try:
    # Ask user to enter a number
    num = int(input("Enter a number: "))

    # Divide 100 by the entered number
    result = 100 / num

    print("Result is:", result)

except ZeroDivisionError:
    # This block runs if the user enters 0
    print("You cannot divide by zero!")

except ValueError:
    # This block runs if the input is not a number
    print("Invalid input! Please enter a number.")

else:
    # This runs only if there was no exception
    print("Division successful.")

finally:
    # This block always runs
    print("Program execution completed.")
