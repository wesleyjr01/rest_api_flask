from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
        return {"item": None}, 404

    def post(self, name):
        # silent=True doesnt give an error, it returns None.
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
