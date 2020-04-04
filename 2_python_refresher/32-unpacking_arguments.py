"""
    Defining a function that take any number of arguments.
"""


def multiply(*args):
    print(args)


multiply(1, 3, 5)


# Named args
def add(x, y):
    return x + y


nums = {"x": 15, "y": 25}
print(add(**nums))
