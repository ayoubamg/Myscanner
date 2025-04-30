
import os
import sys

def show_menu():
    print("\n==========================")
    print("🔍 Welcome to Myscanner 🔍")
    print("==========================")
    print("1. Full Scan")
    print("2. Advanced Scan")
    print("3. Help")
    print("4. Quit")

def full_scan():
    print("\n[+] Launching Full Scan...")
    os.system("bash repository.sh")  # Example: pulls scan resources
    # Add actual full scan logic here

def advanced_scan():
    print("\n[+] Advanced Scan Options")
    target = input("Enter target URL: ")
    print(f"[+] Scanning {target} with advanced options...")
    # Example of calling a scan script
    os.system(f"python3 apps/advanced_scan.py {target}")  # Placeholder

def show_help():
    print("\nMyscanner Help")
    print("- Full Scan: Run a complete vulnerability scan on default settings.")
    print("- Advanced Scan: Customize your scan with additional options.")
    print("- Make sure your tools in 'apps/' and 'otp/' are properly configured.")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            full_scan()
        elif choice == '2':
            advanced_scan()
        elif choice == '3':
            show_help()
        elif choice == '4':
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("\n[!] Invalid option. Please try again.")

if __name__ == "__main__":
    main()
