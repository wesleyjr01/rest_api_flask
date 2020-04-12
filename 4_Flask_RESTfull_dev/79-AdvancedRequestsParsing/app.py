from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)

"""
    In the PUT definition (Lecture Definition), when updating the item
we use the entire payload parsed. If the payload were to include a name,
the item's name would change alongside this update, and that may not be 
what we want.
    So we are going to make sure that only some elements can be passed in
through the JSON payload with reqparse.

* reqparse : 
"""
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    """ with with @jwt_required(), we are going to have to
    authenticate before can call the get method """

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None) is not None:
            return {"message": f"An item with name {name} already exists."}, 400
        parser = reqparse.RequestParser()
        parser.add_argument(
            "price", type=float, required=True, help="This field cannot be left blank!"
        )
        received_data = parser.parse_args()
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

    # @jwt_required()
    # def delete(self, name):
    #     """ Lecture Implementation. """
    #     global items
    #     items = list(filter(lambda x: x["name"] != name, items))
    #     return {"message": "item deleted"}, 200

    # @jwt_required()
    # def put(self, name):
    #     """ My Own Implementation. """
    #     received_data = request.get_json(silent=True)
    #     new_item = {"name": name, "price": received_data["price"]}
    #     old_item = next(filter(lambda x: x["name"] == name, items), None)
    #     if old_item:
    #         items.remove(old_item)
    #     items.append(new_item)
    #     return {"item": new_item}, 200

    @jwt_required()
    def put(self, name):
        """ Lecture Implementation.
        We defined a parser here, and defined only "price" as an argument
        for the parser, so anything else that comes with the payload will be
        erased. """
        parser = reqparse.RequestParser()
        parser.add_argument(
            "price", type=float, required=True, help="This field cannot be left blank!"
        )
        received_data = parser.parse_args()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item is None:
            item = {"name": name, "price": received_data["price"]}
            items.append(item)
        else:
            item.update(received_data)
        return item, 200


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

# For good error messages debug=True
app.run(port=5000, debug=True)
