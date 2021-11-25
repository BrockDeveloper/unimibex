### generazione di una chiave di crittografia utilizzabile ###

from cryptography.fernet import Fernet
import pyperclip


key = Fernet.generate_key()
print(key.decode())
pyperclip.copy(key.decode())