
from password_checker import PasswordChecker
import os

def clear_screen():
    """Clear terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    """Display main menu and return choice"""
    print("\n" + "=" * 60)
    print("🔐 PASSWORD STRENGTH CHECKER 🔐".center(60))
    print("=" * 60)
    print("1. Check password strength")
    print("2. Check multiple passwords")
    print("3. Get tips for strong passwords")
    print("4. Exit")
    print("=" * 60)
    
    choice = input("Select option (1-4): ").strip()
    return choice

def check_single_password():
    """Check a single password"""
    print("\n" + "-" * 60)
    password = input("Enter password to check: ")
    
    if not password:
        print("❌ Password cannot be empty!")
        return
    
    checker = PasswordChecker()
    result = checker.evaluate(password)
    checker.display_result(result)

def check_multiple_passwords():
    """Check multiple passwords in sequence"""
    print("\n" + "-" * 60)
    print("Check multiple passwords (enter 'done' to finish)\n")
    
    count = 1
    while True:
        password = input(f"Password #{count}: ")
        
        if password.lower() == 'done':
            print("\n✅ Finished checking passwords!")
            break
        
        if not password:
            print("❌ Password cannot be empty, try again.\n")
            continue
        
        checker = PasswordChecker()
        result = checker.evaluate(password)
        checker.display_result(result)
        count += 1

def show_tips():
    """Display tips for creating strong passwords"""
    tips = """
╔════════════════════════════════════════════════════════════╗
║        💡 TIPS FOR CREATING STRONG PASSWORDS 💡           ║
╚════════════════════════════════════════════════════════════╝

✅ DO:
  • Use at least 12 characters (more is better)
  • Mix uppercase, lowercase, numbers, and special characters
  • Use unique passwords for different accounts
  • Use a password manager to store passwords securely
  • Update passwords every 3-6 months
  • Create passphrases (e.g., "BlueSky#Sunrise2024!")

❌ DON'T:
  • Use common words (password, admin, letmein)
  • Use personal information (birthdate, names)
  • Use sequential patterns (12345, qwerty)
  • Reuse passwords across multiple sites
  • Share passwords with anyone
  • Use single character types only (all lowercase, etc.)
  • Write passwords on paper or share via email

📋 EXAMPLE STRONG PASSWORDS:
  ✓ Tr0ub4dor&3   (14 chars, all criteria met)
  ✓ P@ssw0rd#2024  (14 chars, all criteria met)
  ✓ MyDog$RunsFast! (16 chars, all criteria met)

═══════════════════════════════════════════════════════════════
    """
    print(tips)

def main():
    """Main program loop"""
    while True:
        choice = main_menu()
        
        if choice == "1":
            check_single_password()
        
        elif choice == "2":
            check_multiple_passwords()
        
        elif choice == "3":
            show_tips()
        
        elif choice == "4":
            print("\n👋 Thank you for using Password Strength Checker!")
            print("Stay secure! 🔐\n")
            break
        
        else:
            print("❌ Invalid option, please choose 1-4.\n")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    clear_screen()
    main()
