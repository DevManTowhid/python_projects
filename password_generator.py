import random
import string
from string import punctuation


def generate_password(length, include_special = True):
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired length:"))

password = generate_password(length)

print("Generated Password:", password)