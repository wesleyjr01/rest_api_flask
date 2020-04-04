"""
        The lambda function is a different type of function,
    which doesnt have a name, and is only used to return
    values.
        Lambda functions are exclusively used to operate on
    inputs and return outputs.
"""


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
