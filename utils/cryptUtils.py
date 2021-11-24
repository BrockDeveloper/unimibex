from cryptography.fernet import Fernet
import pyperclip

# personal key
KEY = b'yBwTtp2U1JkO64DJkQZ8fhK6ROpSos5P3qTguW4yFGE='
coder = Fernet(KEY)

def cryptText(text, returnValue=False):

    encrypted = coder.encrypt(text.encode())

    if returnValue:
        return encrypted.decode()
    else:
        print(encrypted.decode())
        pyperclip.copy(encrypted.decode())
