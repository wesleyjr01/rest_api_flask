"""
    Functions that are just variables, so you can pass them in as
    arguments to functions and use them in the same way you would
    use any other variable.
"""


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)
