# Unpacking example 01
def multiply(*args):
    """
    *args is a tuple of arguments.
    """
    print(args)


multiply(1, 3, 5)


# Unpacking example 02
def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))


# Unpacking example 03
def subtract(x, y):
    return x - y


Nums = {"x": 15, "y": 25}
print(subtract(**Nums))


# Unpacking example 04
def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided"


print(apply(1, 2, 5, 6, 7, operator="+"))

