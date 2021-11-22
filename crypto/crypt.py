### crittografia dei link delle lezioni e delle eventuali password ###

import pyperclip
from cryptography.fernet import Fernet

# personal key
KEY = b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def cryptText(text):
    coder = Fernet(KEY)

    encrypted = coder.encrypt(text.encode())

    print(encrypted.decode())
    pyperclip.copy(encrypted.decode())

if __name__ == "__main__":

    # crypto with the personal key
    coder = Fernet(KEY)

    # get the plain link
    original = input("Link da crittografare: ")

    cryptText(original)

