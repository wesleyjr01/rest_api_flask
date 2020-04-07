"""
    You will need a wrapper on pretty much every decorator you
    write, and @functools.wraps(func) will be needed.

    Terminology:
    1) make_secure is the decorator
    2) secure_function is just another function that will replace some other one.
"""

import functools


def make_secure(func):
    @functools.wraps(func)  # now it keeps the name and documentation of func
    def secure_function():
        if user["acess_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for user {user['username']}."

    return secure_function


# get_admin_password = make_secure(get_admin_password) == @make_secure
@make_secure
def get_admin_password():
    return "1234"


user = {"username": "jose", "acess_level": "user"}
print(get_admin_password.__name__)
print(get_admin_password())
