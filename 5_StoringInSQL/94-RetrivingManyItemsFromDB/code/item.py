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

    @classmethod
    def insert(cls, new_item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (new_item["name"], new_item["price"]))
        connection.commit()
        connection.close()

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item["price"], item["name"]))
        connection.commit()
        connection.close()

    @jwt_required()
    def get(self, name):
        try:
            item = self.find_by_name(name)
        except:
            return {"message": "Failed to run the search method."}, 500
        if item:
            return item
        return {"message": "Item not found."}, 400

    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {"message": f"An item with name {name} already exists."}, 400

        received_data = Item.parser.parse_args()
        new_item = {"name": name, "price": received_data["price"]}

        try:
            self.insert(new_item)
        except:
            return {"message": "An error ocurred inserting the item."}, 500

        return {"Item Created:": new_item}, 201

    @jwt_required()
    def delete(self, name):
        """ Lecture Implementation. """
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {"message": f"item {name} deleted!"}, 200

    @jwt_required()
    def put(self, name):
        """ Lecture Implementation. """
        received_data = Item.parser.parse_args()
        item = self.find_by_name(name)
        new_item = {"name": name, "price": received_data["price"]}
        if item is None:
            try:
                self.insert(new_item)
            except:
                return {"message": "An error occured inserting the item."}, 500
        else:
            try:
                self.update(new_item)
            except:
                return {"message": "An error occured updating the item"}, 500
        return new_item, 200


class ItemList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        items = cursor.execute(query)
        items.fetchall()
        return {"items": items}, 201
