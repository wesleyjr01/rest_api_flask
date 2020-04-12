from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    """@jwt_required() for authentication."""

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None) is not None:
            return {"message": f"An item with name {name} already exists."}, 400

        received_data = Item.parser.parse_args()
        new_item = {"name": name, "price": received_data["price"]}
        items.append(new_item)
        return new_item, 201

    @jwt_required()
    def delete(self, name):
        """ My Own Implementation. """
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            items.remove(item)
            return {"item deleted": item}, 200
        return f"Item {name} not found", 404

    @jwt_required()
    def put(self, name):
        """ Lecture Implementation. """
        received_data = Item.parser.parse_args()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item is None:
            item = {"name": name, "price": received_data["price"]}
            items.append(item)
        else:
            item.update(received_data)
        return item, 200

    # @jwt_required()
    # def delete(self, name):
    #     """ Lecture Implementation. """
    #     global items
    #     items = list(filter(lambda x: x["name"] != name, items))
    #     return {"message": "item deleted"}, 200

    # @jwt_required()
    # def put(self, name):
    #     """ My Own Implementation. """
    #     received_data = Item.parser.parse_args()
    #     new_item = {"name": name, "price": received_data["price"]}
    #     old_item = next(filter(lambda x: x["name"] == name, items), None)
    #     if old_item:
    #         items.remove(old_item)
    #     items.append(new_item)
    #     return {"item": new_item}, 200


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

# For good error messages debug=True
app.run(port=5000, debug=True)
