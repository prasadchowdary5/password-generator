import secrets
import string


def generate_password(length):
    # Define character sets for different complexity levels
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Create a pool of characters based on user's choice
    pool = lowercase + uppercase + digits

    # Add special characters if user wants a complex password
    if length >= 12:
        pool += special_characters

    # Generate the password
    password = ''.join(secrets.choice(pool) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length should be at least 1.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid length as an integer.")


if __name__ == "__main__":
    main()
