"""
    How does these two stars work?
    1) They can be used in a function to collect
    named arguments into a dictionary.
    2) Or they can be used in a function call to
    unpack a dictionary into keyword arguments.

    *args -> positional arguments

    **kwargs -> named arguments

    This sintax is used to accep an unlimited number of arguments.Example:
    
    def post(url, data=None, json=None, **kwargs):
        return request("post", url, data=data, json=json, **kwargs)
"""


def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}:{value}")


details = {"name": "Bob", "age": 25}

print(details)
# **details means unpacked, f(**details) == f(name="Bob", age=25)
named(**details)
print_nicely(**details)
