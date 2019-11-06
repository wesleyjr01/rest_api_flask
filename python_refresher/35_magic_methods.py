class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
            This magic method gets called for you,
            when you want to turn your object into a string.
        """
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        """
            The magic method repr is used to print out
            an unambiguous representation of an object,
            so that you can use that to recreate your
            object.
        """
        return f"<Person('{self.name}', {self.age})>"


bob = Person("Bob", 35)

print(bob)
print(bob.__repr__())
