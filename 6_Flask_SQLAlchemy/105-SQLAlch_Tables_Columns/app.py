from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from security import authenticate, identity
from resources.user import UserRegister  # resources package
from resources.item import Item, ItemList  # resources package
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
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
    db.init_app(app)
    app.run(port=5000, debug=True)
