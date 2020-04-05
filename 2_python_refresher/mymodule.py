"""
    __name__ is a global variable in python, that changes depending on which file you
    are in. So it is a special variable, because it will allow you to differentiate
    between the file you run and a file you import.

    Running in the same file, __name__ == __main__
"""

import libs.mylib


def divide(dividend, divisor):
    return dividend / divisor


print("mymodule.py:", __name__)
