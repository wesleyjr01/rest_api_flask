"""
    In python, all things are mutable, because everything
    is an object, unless there are specifically no ways
    of changing the properties of the object itself.
    Ex:
    * For example defining tuples, they are immutable.
    * Strings, Integers, Float and Booleans are also immutable.
"""


a = []
b = a

# 'a' and 'b' are names for the same object
print(id(a))
print(id(b))
print("\n")

a = 1515
b = 1515
print(id(a))
print(id(b))
print("\n")

a = 1516
print(id(a))
print(id(b))
print("\n")
