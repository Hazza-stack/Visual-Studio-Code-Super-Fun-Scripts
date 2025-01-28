import time
import random
import string

def generate_random_ip():
    """Generate a random IP address."""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_random_data():
    """Generate random text to simulate 'hacking' data."""
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=random.randint(20, 50)))

def fake_hacking_effect():
    """Interactive fake hacking simulation."""
    print("Welcome to the fake hacking tool! Type 'help' for commands.\n")
    
    while True:
        command = input(">> ").strip().lower()
        
        if command == "help":
            print("\nAvailable commands:")
            print("  scan         - Scan for random IPs")
            print("  connect      - Connect to a random IP")
            print("  hack         - Simulate a fake hack")
            print("  exit         - Exit the tool\n")
        
        elif command == "scan":
            print("Scanning for targets...")
            time.sleep(1)
            for _ in range(5):  # Simulate finding 5 IPs
                print(f"  Found target: {generate_random_ip()}")
                time.sleep(0.5)
            print("Scan complete.\n")
        
        elif command == "connect":
            target_ip = generate_random_ip()
            print(f"Attempting to connect to {target_ip}...")
            time.sleep(1)
            if random.random() > 0.2:  # Simulate successful connections
                print(f"Connection to {target_ip} successful!")
            else:
                print(f"Connection to {target_ip} failed. Retrying...")
                time.sleep(1)
                print(f"Connection to {target_ip} successful!")
            print()
        
        elif command == "hack":
            print("Launching fake hacking sequence...")
            time.sleep(1)
            for _ in range(10):  # Simulate a series of hacking steps
                print(f"Bypassing system at {generate_random_ip()}...")
                time.sleep(0.3)
                print(f"Data retrieved: {generate_random_data()}")
                time.sleep(0.3)
            print("Fake hack complete! Mission accomplished.\n")
        
        elif command == "exit":
            print("Exiting the fake hacking tool. Goodbye!")
            break
        
        else:
            print("Unknown command. Type 'help' for a list of commands.\n")

if __name__ == "__main__":
    fake_hacking_effect()
