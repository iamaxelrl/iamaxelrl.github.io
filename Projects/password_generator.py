import random
import string

print("Password generator")

length = int(input("How long should the password be? "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for i in range(length))

print("Your password is:", password)
