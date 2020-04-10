from flask import Flask, jsonify, request

app = Flask(__name__)

stores = {
    "stores": [
        {
            "name": "My Wonderful Store",
            "items": [
                {"name": "My Item", "price": 15.99},
                {"name": "Your Item", "price": 2.99},
            ],
        },
        {
            "name": "Shitty Store",
            "items": [
                {"name": "Shitty Chicken", "price": 19.99},
                {"name": "Shitty Flango", "price": 999.99},
            ],
        },
    ]
}
"""
By default, when you use app.route, that is a GET request.
And browsers, by default, only do get requests.
So we need to specify POST in methods.
"""

# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores["stores"].append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route("/store/<string:name>")  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    for store in stores["stores"]:
        if name == store["name"]:
            return jsonify(store)
    return jsonify({"message": "Store not found"})


# GET /stores
@app.route("/store")
def get_stores():
    return jsonify(stores)


# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores["stores"]:
        if name == store["name"]:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return jsonify(store)
    return jsonify({"message": "Store not found."})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores["stores"]:
        if name == store["name"]:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "Store not found"})


app.run(port=5000)
