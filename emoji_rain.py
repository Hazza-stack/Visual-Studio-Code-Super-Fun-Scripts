import random
import time
import os

# List of fun emojis 🎉
EMOJIS = ["😀", "😂", "🥳", "🎉", "🌟", "🔥", "💖", "🐱", "🐶", "🦄", "🍕", "🎵", "🌈", "⚡"]

def clear_console():
    """Clear the console for a fresh rain of emojis!"""
    os.system('cls' if os.name == 'nt' else 'clear')

def emoji_rain():
    """Generate a fun, colorful rain of emojis!"""
    while True:
        clear_console()
        rows = random.randint(5, 15)  # Random number of rows
        for _ in range(rows):
            line = ''.join(random.choices(EMOJIS, k=random.randint(5, 15)))
            print(line)
        time.sleep(0.5)  # Pause for a moment before refreshing

if __name__ == "__main__":
    print("Press Ctrl+C to stop the Emoji Rain 🌧️")
    try:
        emoji_rain()
    except KeyboardInterrupt:
        print("\nThanks for playing with Emoji Rain! 🎉")
