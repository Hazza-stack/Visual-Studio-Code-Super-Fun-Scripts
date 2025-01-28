import time
import random
import string

def generate_random_ip():
    """Generate a random IP address."""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_random_hex():
    """Generate random hexadecimal data."""
    return ''.join(random.choices("0123456789ABCDEF", k=32))

def generate_random_data():
    """Generate random alphanumeric data."""
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=random.randint(20, 50)))

def display_loading(message, duration=2):
    """Display a loading animation."""
    print(message, end="")
    for _ in range(duration):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def interactive_hacking():
    """Simulate an advanced fake hacking tool."""
    print("=== Welcome to Advanced Fake Hacking Tool ===")
    print("Type 'help' for a list of commands.\n")

    while True:
        command = input("HACK>> ").strip().lower()

        if command == "help":
            print("\nCommands:")
            print("  trace       - Trace a target's location")
            print("  inject      - Simulate code injection")
            print("  exploit     - Simulate exploiting a vulnerability")
            print("  scan        - Scan for active devices")
            print("  shutdown    - Fake system shutdown simulation")
            print("  exit        - Exit the program\n")

        elif command == "trace":
            target_ip = generate_random_ip()
            print(f"Tracing target at {target_ip}...")
            display_loading("Locating")
            print(f"Location found: Latitude {random.uniform(-90, 90):.4f}, Longitude {random.uniform(-180, 180):.4f}")
            print("Trace complete.\n")

        elif command == "inject":
            print("Injecting malicious code into target system...")
            for _ in range(5):
                print(f"  Code injected: {generate_random_hex()}")
                time.sleep(0.5)
            print("Injection successful! Backdoor access established.\n")

        elif command == "exploit":
            print("Scanning for vulnerabilities...")
            display_loading("Searching")
            print(f"Exploit found: CVE-{random.randint(2010, 2025)}-{random.randint(1000, 99999)}")
            time.sleep(1)
            print("Exploiting vulnerability...")
            display_loading("Deploying payload", duration=3)
            print("Exploit successful! System compromised.\n")

        elif command == "scan":
            print("Scanning for active devices...")
            for _ in range(5):
                print(f"  Device found: {generate_random_ip()} - Status: ONLINE")
                time.sleep(0.5)
            print("Scan complete.\n")

        elif command == "shutdown":
            print("WARNING: System shutdown initiated!")
            display_loading("Encrypting files", duration=3)
            print("Shutdown complete. System locked. (Just kidding!)\n")

        elif command == "exit":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Unknown command. Type 'help' for a list of commands.\n")

if __name__ == "__main__":
    interactive_hacking()
