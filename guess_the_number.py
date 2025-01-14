import random

def guess_the_number():
    """A fun number guessing game."""
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    print("I have chosen a number between 1 and 100.")
    print("Your goal is to guess it in as few tries as possible. Let's begin!\n")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Prompt the player to guess
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("🔼 Too low! Try again.")
            elif guess > secret_number:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts! 🏆")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
