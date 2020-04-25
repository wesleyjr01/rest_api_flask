from flask_restful import Resource
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_identity
from models.store import StoreModel


class Store(Resource):
    @jwt_required
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"message": "Store not found"}, 404

    @jwt_required
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": f"Store {name} already exists."}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error ocurred inserting the item."}, 500
        return store.json()

    @jwt_required
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "Store Deleted."}, 200


class StoreList(Resource):
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        stores = [store.json() for store in StoreModel.find_all()]
        if user_id:
            return {"Stores": stores}, 200
        return (
            {
                "Stores": [store["name"] for store in stores],
                "message": "More data available if you log in.",
            },
            200,
        )
