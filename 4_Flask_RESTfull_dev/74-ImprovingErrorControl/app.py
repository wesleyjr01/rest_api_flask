"""
    New concepts:
    1) Use of next() function, retrieving the first element found, or None
    if doesnt find anything.
    2) "ternery if statement": Ternary operators also known as conditional 
    expressions are operators that evaluate something based on a condition 
    being true or false.
    3) HTTP Status:
        * 404 - Not Found.
        * 400 - Bad Request.
        * 201 - Something was created successfully.
        * 200 - Status Success.
"""

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
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
