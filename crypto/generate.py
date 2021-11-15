### generazione di una chiave di crittografia utilizzabile ###

from cryptography.fernet import Fernet
import base64


key = Fernet.generate_key()
print(key.decode())