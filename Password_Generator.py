import random
import string

def generate_password(length):
    """
    Generate a strong and unique password of a given length.

    :param length: The length of the password to generate.
    :return: A strong and unique password.
    """
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Ensure the password has at least one uppercase letter, one lowercase letter, one digit, and one special character
    while (not any(c.isupper() for c in password) or
           not any(c.islower() for c in password) or
           not any(c.isdigit() for c in password) or
           not any(c in string.punctuation for c in password)):
        password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Generate a password of length 12
password = generate_password(12)

print("Generated Password : ", password)