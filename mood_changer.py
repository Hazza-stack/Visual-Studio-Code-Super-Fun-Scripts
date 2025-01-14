import random
import time
import os

def print_with_colors(message, fg_color, bg_color):
    """Print text with foreground and background colors."""
    colors = {
        "black": "30", "red": "31", "green": "32", "yellow": "33",
        "blue": "34", "magenta": "35", "cyan": "36", "white": "37"
    }
    fg = colors.get(fg_color, "37")  # Default to white
    bg = colors.get(bg_color, "40")  # Default to black
    print(f"\033[{fg};{int(bg) + 10}m{message}\033[0m")

def mood_changer():
    """Randomly selects and displays a mood."""
    moods = [
        ("Sunny vibes 🌞", "yellow", "blue"),
        ("Feeling fiery 🔥", "red", "black"),
        ("Chill like the ocean 🌊", "cyan", "white"),
        ("Magical moments ✨", "magenta", "black"),
        ("Nature's calm 🌿", "green", "black"),
        ("Bright and cheerful 🌼", "white", "yellow"),
    ]

    print("\n💫 Welcome to the Mood Changer! 💫")
    print("Changing your mood in 3... 2... 1...\n")
    time.sleep(1)

    mood = random.choice(moods)
    print_with_colors(f"Your mood: {mood[0]}", mood[1], mood[2])

    print("\n✨ Keep shining and coding! ✨")

if __name__ == "__main__":
    mood_changer()
    