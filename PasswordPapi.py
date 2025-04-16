import random
import string
import os

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    """
    Generate a strong random password based on the selected parameters.
    :param length: The desired length of the password (minimum 8 characters)
    :param use_upper: Whether to include uppercase letters
    :param use_digits: Whether to include digits
    :param use_symbols: Whether to include symbols
    :return: A randomly generated password string
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine selected character sets
    all_chars = lower + upper + digits + symbols

    if not all_chars:
        raise ValueError("At least one character set must be selected.")

    # Start the password with at least one character from each selected set
    password = [
        random.choice(lower),
        random.choice(upper) if use_upper else '',
        random.choice(digits) if use_digits else '',
        random.choice(symbols) if use_symbols else ''
    ]

    # Add remaining random characters from the combined set
    password += [random.choice(all_chars) for _ in range(length - len(password))]
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def display_menu(length, use_upper, use_digits, use_symbols):
    """
    Display the main menu options for the user to select from.
    :param length: The current password length
    :param use_upper: Whether uppercase letters are enabled
    :param use_digits: Whether digits are enabled
    :param use_symbols: Whether symbols are enabled
    """
    print("\n=== PasswordPapi: Secure Password Generator ===")
    print(f"\nCurrent Configuration: "
          f"\nPassword Length: {length} "
          f"\nUppercase Letters: {'Enabled' if use_upper else 'Disabled'} "
          f"\nDigits: {'Enabled' if use_digits else 'Disabled'} "
          f"\nSymbols: {'Enabled' if use_symbols else 'Disabled'}")
    
    print("""
Options:
1. Change Password Length
2. Toggle Uppercase Letters
3. Toggle Digits
4. Toggle Symbols
5. Generate Password(s)
0. Exit
""")

def export_to_txt(passwords, directory):
    """
    Export generated passwords to a .txt file at the specified directory.
    :param passwords: The list of generated passwords
    :param directory: The directory where the file should be saved
    """
    if not os.path.exists(directory):
        print("Error: The specified directory does not exist.")
        return

    file_path = os.path.join(directory, "generated_passwords.txt")
    with open(file_path, "w") as f:
        for pwd in passwords:
            f.write(f"{pwd}\n")
    print(f"Passwords successfully exported to {file_path}\n")

def selection_menu():
    """
    Main menu for interacting with the Password Generator.
    """
    # Initial settings
    length = 16
    use_upper = True
    use_digits = True
    use_symbols = True
    generated_passwords = []

    while True:
        display_menu(length, use_upper, use_digits, use_symbols)
        choice = input("Select an option (0-5): ").strip()

        if choice == "1":
            # Update password length
            try:
                new_length = int(input("Enter new password length (minimum 8): ").strip())
                if new_length < 8:
                    print("Warning: Password length must be at least 8 characters for better security.")
                else:
                    length = new_length
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == "2":
            # Toggle uppercase letters
            use_upper = not use_upper
            print(f"Uppercase letters are now {'enabled' if use_upper else 'disabled'}.")

        elif choice == "3":
            # Toggle digits
            use_digits = not use_digits
            print(f"Digits are now {'enabled' if use_digits else 'disabled'}.")

        elif choice == "4":
            # Toggle symbols
            use_symbols = not use_symbols
            print(f"Symbols are now {'enabled' if use_symbols else 'disabled'}.")

        elif choice == "5":
            # Generate passwords
            try:
                count = int(input("How many passwords do you want to generate?: ").strip())
                if count <= 0:
                    print("Please generate at least one password.")
                    continue
                print("\n=== Generated Passwords ===")
                generated_passwords = []
                for i in range(count):
                    pwd = generate_password(length, use_upper, use_digits, use_symbols)
                    generated_passwords.append(pwd)
                    print(f"[{i + 1}] {pwd}")
                print("\nPassword generation complete.\n")

                # Clean up UI after generation
                input("Press Enter to continue to the export prompt...")

                # Prompt for export
                export_choice = input("Would you like to export the generated passwords to a .txt file? (y/n): ").strip().lower()
                if export_choice == "y":
                    dir_path = input("Enter the directory path (e.g., C:\\Users\\yourusername\\Documents\\): ").strip()
                    export_to_txt(generated_passwords, dir_path)
                else:
                    print("Passwords were not exported.\n")

            except ValueError:
                print("Error: Please enter a valid number for the password count.")
        
        elif choice == "0":
            print("Exiting PasswordPapi. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number between 0 and 5.")

if __name__ == "__main__":
    selection_menu()
