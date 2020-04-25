from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"message": "Store not found"}, 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": f"Store {name} already exists."}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error ocurred inserting the item."}, 500
        return store.json()

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "Store Deleted."}, 200


class StoreList(Resource):
    @jwt_required()
    def get(self):
        try:
            return (
                {"Stores": [store.json() for store in StoreModel.find_all()]},
                200,
            )
        except:
            return {"message": "Failed to retrive items."}, 500
