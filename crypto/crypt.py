### crittografia dei link delle lezioni e delle eventuali password ###

import pyperclip
from cryptography.fernet import Fernet

# personal key
KEY = b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# crypto with the personal key
coder = Fernet(KEY)

# get the plain link
original = input("Link da crittografare: ")

encrypted = coder.encrypt(original.encode())

print(encrypted.decode())
pyperclip.copy(encrypted.decode())