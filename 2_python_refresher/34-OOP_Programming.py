class Student:
    def __init__(self, name, grades, **kwargs):
        self.name = name
        self.grades = grades
        self.kwargs = kwargs

    def avereage_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (50, 70, 43, 90), **{"corona": "virus", "flango": "flito"})
print(student.name)
print(student.grades)
print(student.avereage_grade())
print(student.kwargs)
