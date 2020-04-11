lst = [{"name": "item1", "price": 1}, {"name": "item2", "price": 2}]

name = "item1"
print(next(filter(lambda x: x["name"] == name, lst), None))
