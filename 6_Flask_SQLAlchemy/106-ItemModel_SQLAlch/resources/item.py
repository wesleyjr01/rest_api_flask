import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    """@jwt_required() for authentication."""

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {"message": "Item not found."}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": f"An item with name {name} already exists."}

        received_data = Item.parser.parse_args()
        item = ItemModel(name, received_data["price"])

        try:
            item.save_to_db()
        except:
            return {"message": "An error ocurred inserting the item."}

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Item Deleted."}, 200

    @jwt_required()
    def put(self, name):
        """ Lecture Implementation. """
        received_data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, received_data["price"])
        else:
            try:
                item.price = received_data["price"]
            except:
                return {"message": "An error occured updating the item"}, 500
        item.save_to_db()
        return item.json(), 200


class ItemList(Resource):
    @jwt_required()
    def get(self):
        try:
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()
            query = "SELECT * FROM items"
            retrieved_data = cursor.execute(query)
            items = [{"name": f[0], "price": f[1]} for f in retrieved_data]
            connection.close()
            return {"items": items}, 200
        except:
            return {"message": "Failed to retrive items."}, 500
