"""
Server VIEW: (opposite to browser view.)
    POST - used to receive data (create a store)
    GET - used to send data back only (send back a list of stores)

So the endpoints we are going to create are:
    1) POST for store, creating a new store, with a given name.
    # POST /store data: {name:}
    is a name.

    2) Get a store for a given name.
    # GET /store/<string:name>

    3) Return a list of all the stores.
    # GET /stores

    4) Create an item inside a specific store, with a given name.
    # POST /store/<string:name>/item {name:, price:}

    5) Get all the items in a specific store.
    # GET /store/<string:name>/item
"""


from flask import Flask

app = Flask(__name__)

stores = [
    {"name": "My Wonderful Store", "items": [{"name": "My Item", "price": 15.99}]}
]
"""
By default, when you use app.route, that is a GET request.
And browsers, by default, only do get requests.
So we need to specify POST in methods.
"""

# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    pass


# GET /store/<string:name>
@app.route("/store/<string:name>")  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    pass


# GET /stores
@app.route("/store")
def get_stores():
    pass


# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    pass


app.run(port=5000)
