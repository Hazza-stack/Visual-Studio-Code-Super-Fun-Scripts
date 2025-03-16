import time
import os

frames = [
    """
      🚀
     """,
    """
      🚀
     💨""",
    """
      🚀
     💨💨""",
    """
      🚀
     💨💨💨""",
    """
      🚀
     💨💨💨💨""",
    """
      🚀
     💨💨💨💨💨
    """,
]

while True:
    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")  # Clears the terminal
        print(frame)
        time.sleep(0.3)  # Wait for a bit before showing the next frame
