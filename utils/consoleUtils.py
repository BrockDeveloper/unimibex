# import call method from subprocess module
from subprocess import call
import os

# import sleep to show output for some time period
from time import sleep


# define clear function
def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')