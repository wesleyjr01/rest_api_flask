class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        """
        Class Methods are often used as factories.
        """
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        """
        Doesnt bring any information about the Class,
        or the Object.
        """
        print("Called static_method.")


test = ClassTest()
test.instance_method()
ClassTest.class_method()
ClassTest.static_method()


# Factory example
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"\n<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)


book1 = Book("Harry Potter", "hardcover", 1500)
print(book1)


book2 = Book.hardcover("Harry Potter", 1500)
print(book2)
