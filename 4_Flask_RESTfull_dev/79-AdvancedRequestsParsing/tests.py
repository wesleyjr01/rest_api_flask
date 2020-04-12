l1 = [{"name": "bob", "price": 15}, {"name": "joe", "price": 11}]

name = "joe"
item = next(filter(lambda x: x["name"] == name, l1), None)
print(item)

if item:
    item.update({"price": 150})
    print(f"item:{item}")
    print(f"item list:{l1}")
