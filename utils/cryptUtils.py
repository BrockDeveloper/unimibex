# TechAle
# See LICENSE file.
#
# Developed by
# TechAle (https://github.com/TechAle)
#
# This source code is distributed under the CC BY-NC-SA 4.0 license:
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# you are FREE to SHARE and ADAPT UNDER THE FOLLOWING TERMS:
#
# ATTRIBUTION You must give appropriate credit, provide a link to the
# license, and indicate if changes were made.
#
# NON COMMERCIAL You may not use the material for commercial purposes.
#
# SHARE ALIKE If you remix, transform, or build upon the material, you
# must distribute your contributions under the same license as the original.
#
#
# This source code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY.
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
