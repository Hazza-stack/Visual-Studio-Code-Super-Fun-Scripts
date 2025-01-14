# Importing the math module for additional functionality (optional)
import math

# Function to calculate the factorial of a number
def calculate_factorial(number):
    """
    Calculate the factorial of a given number using recursion.
    
    Parameters:
    number (int): A non-negative integer to find the factorial of.
    
    Returns:
    int: The factorial of the given number.
    """
    # Base case: factorial of 0 or 1 is 1
    if number <= 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return number * calculate_factorial(number - 1)

# Main function to interact with the user
def main():
    """
    Main function to take user input and display the factorial.
    """
    try:
        # Take input from the user
        user_input = int(input("Enter a non-negative integer to calculate its factorial: "))
        
        if user_input < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            # Calculate the factorial
            result = calculate_factorial(user_input)
            print(f"The factorial of {user_input} is: {result}")
    except ValueError:
        print("Invalid input! Please enter a valid non-negative integer.")

# Call the main function
if __name__ == "__main__":
    main()
