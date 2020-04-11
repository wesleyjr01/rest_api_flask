"""
    We need here a in memory table of our registered users.
    We do this so we dont have to iterate over 'users' every time.

    Lets create our two functions:
    1) One function will authenticate a user. It's the function that
    given a user name and password, is going to select the correct user name
    from our list 'users'.
"""

from user import User
from werkzeug.security import safe_str_cmp

users = [User(_id=1, username="bob", password="asdf")]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """ Takes in a payload, and the payload is the contents of the JWT Token
    and then we're going to extract the user ID from that payload, and once
    we have the user ID we can retrieve the specific user that matches this payload.
    """
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)
