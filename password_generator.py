import random
import string

def make_password(length=8):
    characters = string.ascii_letters
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

p1 = make_password()
p2 = make_password(12)

print("password:", p1)
print("length:", len(p1))
print("password:", p2)
print("length:", len(p2))