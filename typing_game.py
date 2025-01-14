import time
import random

# List of sentences to type
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a fun and versatile programming language.",
    "Typing fast and accurately takes practice!",
    "Code, debug, and repeat for success.",
    "Challenge yourself to type this sentence quickly!"
]

def typing_speed_test():
    """Test your typing speed and accuracy."""
    print("Welcome to the Typing Speed Test! 🚀")
    print("Type the following sentences as quickly and accurately as you can.")
    print("Press Enter to start...")
    input()

    # Select a random sentence
    sentence = random.choice(SENTENCES)
    print("\nYour sentence is:")
    print(f"👉 {sentence}")
    print("\nReady? Start typing below and press Enter when done!")

    # Start the timer
    start_time = time.time()

    # Get user input
    typed_sentence = input("\nType here: ")

    # Stop the timer
    end_time = time.time()

    # Calculate time taken
    time_taken = end_time - start_time

    # Calculate accuracy
    correct_chars = sum(1 for i, c in enumerate(typed_sentence) if i < len(sentence) and c == sentence[i])
    total_chars = len(sentence)
    accuracy = (correct_chars / total_chars) * 100

    # Show results
    print("\n🎉 Results 🎉")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Typed characters: {len(typed_sentence)} / {total_chars}")
    print("\nThanks for playing! Try again to beat your score! 🏆")

if __name__ == "__main__":
    typing_speed_test()
