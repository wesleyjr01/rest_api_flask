class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book_dict = {"name": "Zurich Axioms", "book_type": "yellowpaper", "weight": 350}
book1 = Book(**book_dict)
print(book1)

book2 = Book.hardcover("Harry Potter", 1500)
print(book2)

book3 = Book.paperback("Missbehaving", 750)
print(book3)
