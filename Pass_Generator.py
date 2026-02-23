import string
import random


def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    # Build the character pool based on user preferences
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("No character types selected! Please enable at least one option.")

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")
    length = int(input("Enter password length: "))

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()