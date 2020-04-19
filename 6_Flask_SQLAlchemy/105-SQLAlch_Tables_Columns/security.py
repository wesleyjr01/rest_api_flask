"""
    We need here a in memory table of our registered users.
    We do this so we dont have to iterate over 'users' every time.

    Lets create our two functions:
    1) One function will authenticate a user. It's the function that
    given a user name and password, is going to select the correct user name
    from our list 'users'.
"""

from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """ Takes in a payload, and the payload is the contents of the JWT Token
    and then we're going to extract the user ID from that payload, and once
    we have the user ID we can retrieve the specific user that matches this payload.
    """
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)
