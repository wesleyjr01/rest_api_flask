from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister # resources package
from resources.item import Item, ItemList # resources package
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)

app.config["JWT_AUTH_URL_RULE"] = "/auth"
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=3600)
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    # For good error messages debug=True
    app.run(port=5000, debug=True)
