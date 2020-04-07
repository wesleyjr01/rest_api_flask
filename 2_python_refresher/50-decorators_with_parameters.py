"""
    In the last lecture, we were looking at decorating
    functions with parameters, now we are going to add
    parameters to the decorators themselves.
"""

import functools

user = {"username": "jose", "acess_level": "guest"}


# Factory: A function used to create a decorator
def make_secure(acess_level):
    def decorator(func):
        @functools.wraps(func)  # now it keeps the name and documentation of func
        def secure_function():
            if user["acess_level"] == acess_level:
                return func()
            else:
                return f"No admin permissions for user {user['username']}."

        return secure_function

    return decorator


@make_secure("admin")
def get_admin_password():
    return "1234"


@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())

user = {"username": "jose", "acess_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())
