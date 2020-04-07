"""
    We are going to learn about decorating functions with parameters.
    If your original function have parameters, you decorator should
    be able to replace that function and preserve the arguments, we will
    do that using *args and **kwargs in the function that replaces the
    original function.
"""
import functools

user = {"username": "jose", "acess_level": "user"}


def make_secure(func):
    @functools.wraps(func)  # now it keeps the name and documentation of func
    def secure_function(*args, **kwargs):
        if user["acess_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for user {user['username']}."

    return secure_function


# get_admin_password = make_secure(get_admin_password) == @make_secure
@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(get_password("ADMIN"))
