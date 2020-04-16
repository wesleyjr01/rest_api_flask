import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    """@jwt_required() for authentication."""

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {"name": row[0], "price": row[1]}, 200
        return None

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {"message": "Item not found."}, 400

    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {"message": f"An item with name {name} already exists."}, 400

        received_data = Item.parser.parse_args()
        new_item = {"name": name, "price": received_data["price"]}

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (new_item["name"], new_item["price"]))
        connection.commit()
        connection.close()

        return {"Item Created:": new_item}, 200

    @jwt_required()
    def delete(self, name):
        """ Lecture Implementation. """
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "item deleted"}, 200

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


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": items}
