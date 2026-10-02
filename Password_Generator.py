import string
import secrets


# ==================================================
#              PASSWORD GENERATOR
#              Developed by MinzaiX
#              GitHub: decodewithaayat
# ==================================================

print("""
==================================================
                 PASSWORD GENERATOR
                 Developed by MinzaiX
                 GitHub: decodewithaayat
==================================================
""")


while True:

    print("\nChoose Password Type:")
    print("1. Numbers Only")
    print("2. Alphabets Only")
    print("3. Alphanumeric")
    print("4. Alphanumeric + Symbols")

    choice = input("\nEnter your choice (1-4): ")

    # Select characters
    if choice == "1":
        chars = string.digits

    elif choice == "2":
        chars = string.ascii_letters

    elif choice == "3":
        chars = string.ascii_letters + string.digits

    elif choice == "4":
        chars = string.ascii_letters + string.digits + string.punctuation

    else:
        print("❌ Invalid choice!")
        continue

    # Password length
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("❌ Please enter a number.")
        continue

    if length < 4:
        print("❌ Password length should be at least 4.")
        continue

    # Generate password
    password = ""

    for i in range(length):
        password += secrets.choice(chars)

    # Display password
    print("\n" + "=" * 50)
    print("             GENERATED PASSWORD")
    print("=" * 50)

    print(password)

    # Simple strength
    if length < 8:
        print("\nPassword Strength: Weak")
    elif length < 12:
        print("\nPassword Strength: Medium")
    else:
        print("\nPassword Strength: Strong")

    print("=" * 50)

    # Generate again
    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("\nThank you for using Password Generator!")
        print("Developed by MinzaiX")
        break