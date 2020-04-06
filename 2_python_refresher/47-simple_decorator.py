"""
    Decorators allows us to easly modify functions.
"""


def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["acess_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for user {user['username']}."

    return secure_function


""" This simple decorator will create a function,
    and replace the original function with the
    secure one. So that you can no loger call
    get_admin_password without having the admin
    acess level.
"""
get_admin_password = make_secure(get_admin_password)
user = {"username": "jose", "acess_level": "user"}
print(get_admin_password())
