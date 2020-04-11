"""
    JWT stands for JSON Web Token, and all it is, is an
    obfuscation of data. And that is we're going to be
    encoding some data, and that's a JSON Web Token.

    So a user is going to be an entity that has a unique
    identifying number and a username and a password. The user
    is going to send us a username and a password, and we're going
    to send them, the client really, a JWT and that JWT is going to be
    the user ID.

    When the client has the JWT, they can send it to us with any request
    they make, and when they do that it's going to tell us that they have
    previously authenticated, and that means they are logged in.
"""

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item is not None else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None) is not None:
            return {"message": f"An item with name {name} already exists."}, 400
        posted_data = request.get_json(silent=True)
        new_item = {"name": name, "price": posted_data["price"]}
        items.append(new_item)
        return new_item, 201


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

# For good error messages debug=True
app.run(port=5000, debug=True)
