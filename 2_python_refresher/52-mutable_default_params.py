"""
    Mutable Default Parameters (and why they're a bad Idea.)
    Never make a parameter equal to a mutable value by default.
    __init__(self, List[int] = []) # Bad
    __init__(self, List[int] = None) # Good
"""

from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


# Check the problem here, both bob and rolf are sharing the same list
bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
