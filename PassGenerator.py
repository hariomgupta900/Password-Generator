import random
import string

# Function to generate a random password
def generate_password(length, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters  # Include both lowercase and uppercase letters

    if include_digits:
        characters += string.digits  # Include digits (0-9)

    if include_special_chars:
        characters += string.punctuation  # Include special characters

    if length < 1:
        return "Password length must be at least 1 character."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input for password length and complexity
length = int(input("Enter the length of the password: "))
include_digits = input("Include digits (yes/no): ").strip().lower() == "yes"
include_special_chars = input("Include special characters (yes/no): ").strip().lower() == "yes"

# Generate and display the password
password = generate_password(length, include_digits, include_special_chars)
print("Generated Password:", password)
