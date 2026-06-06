# TASK 4
import random
import string

print("=== Simple Random Password Generator ===\n")

length = int(input("Enter password length (recommended 8-16): "))

characters = string.ascii_letters + string.digits + "!@#$%^&*"

password = ''.join(random.choice(characters) for _ in range(length))

print(" Your Password:", password)

# TASK 5
