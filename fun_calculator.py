import random
import math
from datetime import datetime

# Function for basic operations
def basic_operations():
    print("\nChoose an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    choice = input("Enter the number of your choice: ")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == "1":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == "4":
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Invalid choice. Please select a valid operation.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Function to generate a random number
def random_number():
    try:
        lower = int(input("\nEnter the lower bound: "))
        upper = int(input("Enter the upper bound: "))
        if lower > upper:
            print("The lower bound must be less than or equal to the upper bound!")
        else:
            print(f"Your random number between {lower} and {upper} is: {random.randint(lower, upper)}")
    except ValueError:
        print("Invalid input! Please enter integers only.")

# Function to square a number
def square_number():
    try:
        num = float(input("\nEnter a number to square: "))
        print(f"The square of {num} is {num**2}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Function to calculate the square root
def square_root():
    try:
        num = float(input("\nEnter a number to find its square root: "))
        if num < 0:
            print("Error: Square root of a negative number is not allowed!")
        else:
            print(f"The square root of {num} is {math.sqrt(num)}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Function to calculate age in days
def age_in_days():
    try:
        birth_date = input("\nEnter your birthdate (YYYY-MM-DD): ")
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.now()
        delta = today - birth_date
        print(f"You are approximately {delta.days} days old!")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")

# Function to flip a coin
def flip_coin():
    print("\nFlipping a coin...")
    result = random.choice(["Heads", "Tails"])
    print(f"It's {result}!")

# Function to convert temperatures
def temperature_conversion():
    print("\nChoose a conversion:")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")
    try:
        temp = float(input("Enter the temperature: "))
        if choice == "1":
            result = (temp * 9/5) + 32
            print(f"{temp}°C is {result}°F")
        elif choice == "2":
            result = (temp - 32) * 5/9
            print(f"{temp}°F is {result}°C")
        else:
            print("Invalid choice. Please choose 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Function to count words in a sentence
def count_words():
    sentence = input("\nEnter a sentence: ")
    words = sentence.split()
    print(f"The sentence contains {len(words)} words.")

# Function to generate a random joke
def random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? Because it had too many problems.",
        "Why was the computer cold? It left its Windows open.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!"
    ]
    print("\nHere's a joke for you:")
    print(random.choice(jokes))

# Main menu
def main_menu():
    while True:
        print("\n=== Super Fun Calculator ===")
        print("1: Basic Operations (Add, Subtract, Multiply, Divide)")
        print("2: Generate a Random Number")
        print("3: Square a Number")
        print("4: Find Square Root")
        print("5: Calculate Your Age in Days")
        print("6: Flip a Coin")
        print("7: Convert Temperatures")
        print("8: Count Words in a Sentence")
        print("9: Generate a Random Joke")
        print("10: Quit")

        choice = input("Choose an option (1-10): ")
        if choice == "1":
            basic_operations()
        elif choice == "2":
            random_number()
        elif choice == "3":
            square_number()
        elif choice == "4":
            square_root()
        elif choice == "5":
            age_in_days()
        elif choice == "6":
            flip_coin()
        elif choice == "7":
            temperature_conversion()
        elif choice == "8":
            count_words()
        elif choice == "9":
            random_joke()
        elif choice == "10":
            print("Thanks for using the Super Fun Calculator! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the script
if __name__ == "__main__":
    main_menu()
