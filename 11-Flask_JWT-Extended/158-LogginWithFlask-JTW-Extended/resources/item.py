from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.item import ItemModel


class Item(Resource):
    """@jwt_required() for authentication."""

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )

    parser.add_argument(
        "store_id", type=int, required=True, help="This field cannot be left blank!"
    )

    @jwt_required
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {"message": "Item not found."}, 404

    @jwt_required
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": f"An item with name {name} already exists."}, 400

        received_data = Item.parser.parse_args()
        item = ItemModel(name, **received_data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error ocurred inserting the item."}, 500

        return item.json(), 201

    @jwt_required
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Item Deleted."}, 200

    @jwt_required
    def put(self, name):
        """ Lecture Implementation. """
        received_data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **received_data)
        else:
            try:
                item.price = received_data["price"]
                item.store_id = received_data["store_id"]
            except:
                return {"message": "An error occured updating the item"}, 500
        item.save_to_db()
        return item.json(), 200


class ItemList(Resource):
    @jwt_required
    def get(self):
        try:
            return (
                {"Items": [item.json() for item in ItemModel.find_all()]},
                200,
            )
        except:
            return {"message": "Failed to retrive items."}, 500
