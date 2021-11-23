### crittografia dei link delle lezioni e delle eventuali password ###
from utils.cryptUtils import *

if __name__ == "__main__":

    # get the plain link
    original = input("Link da crittografare: ")

    cryptText(original)

