import random
import string


def generate_password(length, letters, numbers, symbols):

    characters = ""

    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if characters == "":
        return None

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


def check_strength(password):

    length = len(password)

    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_letter, has_digit, has_symbol])

    if length >= 12 and score == 3:
        return "Strong"
    elif length >= 8 and score >= 2:
        return "Medium"
    else:
        return "Weak"


while True:

    print("\n===== PASSWORD GENERATOR MENU =====")
    print("1. Generate Single Password")
    print("2. Generate Multiple Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        length = int(input("Enter password length: "))

        letters = input("Include letters? (y/n): ").lower() == "y"
        numbers = input("Include numbers? (y/n): ").lower() == "y"
        symbols = input("Include symbols? (y/n): ").lower() == "y"

        password = generate_password(length, letters, numbers, symbols)

        if password:
            print("\nGenerated Password:", password)
            print("Password Strength:", check_strength(password))
        else:
            print("Error: Select at least one character type.")

    elif choice == "2":

        count = int(input("How many passwords to generate? "))
        length = int(input("Enter password length: "))

        letters = input("Include letters? (y/n): ").lower() == "y"
        numbers = input("Include numbers? (y/n): ").lower() == "y"
        symbols = input("Include symbols? (y/n): ").lower() == "y"

        for i in range(count):

            password = generate_password(length, letters, numbers, symbols)

            if password:
                print(f"Password {i+1}: {password}  | Strength:", check_strength(password))
            else:
                print("Error: Select at least one character type.")
                break

    elif choice == "3":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")